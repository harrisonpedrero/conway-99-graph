"""
root_cell_permutation_csp.py -- rooted k=14 fiber-permutation formulation.

For srg(99,14,1,2), the R202/R204 rooted far graph has 21 fibers, one for each
edge of K7.  Each fiber has four vertices and a forced C4.  Between two disjoint
fibers, R204 forces the 4x4 free-edge block to be a permutation matrix.

This model uses those 105 S4 blocks as the primary variables.  The full far-pair
common-neighbour equations become equality-count constraints between permutation
images.  SAT reconstructs a full rooted graph and verifies the SRG equations;
INFEASIBLE would be a nonexistence certificate candidate for the rooted model.
"""
import argparse
import json
import time
from functools import lru_cache
from itertools import combinations, permutations
from pathlib import Path

from ortools.sat.python import cp_model

from root_cell_cpsat import (
    build_full_graph,
    forced_free_edge_value,
    labels_by_fiber,
    make_labels,
    overlap,
    verify_srg,
)
from root_cell_permutation_sat import matching_triangle_allowed_triples


PERMS = list(permutations(range(4)))
PERM_ID = {perm: idx for idx, perm in enumerate(PERMS)}
BLOCK_REPS = {
    "square": (0, 1, 2, 3),
    "nonsquare": (0, 1, 3, 2),
}
SQUARE_ORBIT = {
    (0, 1, 2, 3),
    (0, 2, 1, 3),
    (1, 0, 3, 2),
    (1, 3, 0, 2),
    (2, 0, 3, 1),
    (2, 3, 0, 1),
    (3, 1, 2, 0),
    (3, 2, 1, 0),
}


def perm_parity(perm):
    inversions = 0
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            inversions += int(perm[i] > perm[j])
    return inversions % 2


def disjoint(a, b):
    return set(a).isdisjoint(b)


def invert_perm(perm):
    out = [0] * len(perm)
    for i, j in enumerate(perm):
        out[j] = i
    return tuple(out)


def compose_perm(left, right):
    return tuple(left[i] for i in right)


@lru_cache(maxsize=1)
def right_coset_id_by_perm():
    h = sorted(SQUARE_ORBIT, key=PERMS.index)
    unseen = set(PERMS)
    cosets = []

    first = set(h)
    cosets.append(first)
    unseen -= first

    while unseen:
        rep = min(unseen, key=PERMS.index)
        coset = {compose_perm(rep, sym) for sym in h}
        cosets.append(coset)
        unseen -= coset

    out = {}
    for idx, coset in enumerate(cosets):
        for perm in coset:
            out[perm] = idx
    return out


def coset_id_rows():
    coset_id = right_coset_id_by_perm()
    return [(coset_id[perm], *perm) for perm in PERMS]


def perm_id_coset_rows():
    coset_id = right_coset_id_by_perm()
    return [(coset_id[perm], PERM_ID[perm]) for perm in PERMS]


def perm_parity_rows():
    return [(perm_parity(perm), PERM_ID[perm]) for perm in PERMS]


def matching_holonomy_rows():
    return [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)]


def square_adjacent(a, b):
    return a != b and bin(a ^ b).count("1") == 1


def residual_matrix_for_block(perm):
    inv = invert_perm(perm)
    rows = []
    for ua in range(4):
        row = []
        for ub in range(4):
            endpoint = (
                int(perm[ua] == ub)
                + int(square_adjacent(inv[ub], ua))
                + int(square_adjacent(perm[ua], ub))
            )
            row.append(2 - endpoint)
        rows.append(tuple(row))
    return tuple(rows)


def matrix_sum(perms):
    rows = [[0] * 4 for _ in range(4)]
    for perm in perms:
        for ua, ub in enumerate(perm):
            rows[ua][ub] += 1
    return tuple(tuple(row) for row in rows)


def perm_id_rows():
    return [(idx, *perm) for idx, perm in enumerate(PERMS)]


def relative_perm_rows():
    rows = []
    for left in PERMS:
        for right in PERMS:
            rel = compose_perm(invert_perm(right), left)
            rows.append((PERM_ID[rel], *left, *right))
    return rows


def disjoint_residual_rows():
    rows = []
    for direct in PERMS:
        target = residual_matrix_for_block(direct)
        for q1 in PERMS:
            partial1 = matrix_sum([q1])
            for q2 in PERMS:
                partial2 = [[partial1[i][j] for j in range(4)] for i in range(4)]
                for ua, ub in enumerate(q2):
                    partial2[ua][ub] += 1
                q3 = []
                ok = True
                for ua in range(4):
                    ones = []
                    for ub in range(4):
                        rem = target[ua][ub] - partial2[ua][ub]
                        if rem == 1:
                            ones.append(ub)
                        elif rem != 0:
                            ok = False
                            break
                    if not ok or len(ones) != 1:
                        ok = False
                        break
                    q3.append(ones[0])
                if ok and tuple(sorted(q3)) == (0, 1, 2, 3):
                    rows.append((PERM_ID[direct], PERM_ID[q1], PERM_ID[q2], PERM_ID[tuple(q3)]))
    return rows


def subtract_perm_from_matrix(matrix, perm):
    rows = [list(row) for row in matrix]
    for ua, ub in enumerate(perm):
        if rows[ua][ub] <= 0:
            return None
        rows[ua][ub] -= 1
    return tuple(tuple(row) for row in rows)


@lru_cache(maxsize=None)
def intersecting_residual_rows(target):
    rows = []

    def rec(matrix, depth, acc):
        if depth == 0:
            if all(value == 0 for row in matrix for value in row):
                rows.append(tuple(PERM_ID[perm] for perm in acc))
            return
        for perm in PERMS:
            next_matrix = subtract_perm_from_matrix(matrix, perm)
            if next_matrix is not None:
                rec(next_matrix, depth - 1, (*acc, perm))

    rec(target, 6, ())
    return rows


@lru_cache(maxsize=None)
def intersecting_pair_projection_rows(target, left_idx, right_idx):
    return sorted(
        {
            (row[left_idx], row[right_idx])
            for row in intersecting_residual_rows(target)
        }
    )


@lru_cache(maxsize=None)
def intersecting_triple_projection_rows(target, left_idx, middle_idx, right_idx):
    return sorted(
        {
            (row[left_idx], row[middle_idx], row[right_idx])
            for row in intersecting_residual_rows(target)
        }
    )


@lru_cache(maxsize=None)
def intersecting_parity_projection_rows(target):
    return sorted(
        {
            tuple(perm_parity(PERMS[idx]) for idx in row)
            for row in intersecting_residual_rows(target)
        }
    )


@lru_cache(maxsize=None)
def intersecting_coset_projection_rows(target):
    coset_id = right_coset_id_by_perm()
    return sorted(
        {
            tuple(coset_id[PERMS[idx]] for idx in row)
            for row in intersecting_residual_rows(target)
        }
    )


def bool_eq_const(model, var, value, name):
    b = model.NewBoolVar(name)
    model.Add(var == value).OnlyEnforceIf(b)
    model.Add(var != value).OnlyEnforceIf(b.Not())
    return b


def bool_eq_var(model, left, right, name):
    b = model.NewBoolVar(name)
    model.Add(left == right).OnlyEnforceIf(b)
    model.Add(left != right).OnlyEnforceIf(b.Not())
    return b


def build_model(
    add_symmetry_seed=False,
    add_coset_projection=False,
    add_disjoint_tables=False,
    add_matching_holonomy=False,
    add_matching_triangle_tables=False,
    add_intersecting_tables=False,
    add_intersecting_pair_tables=False,
    add_intersecting_triple_tables=False,
    add_intersecting_parity_table=False,
    add_intersecting_coset_table=False,
    block_rep="none",
):
    if add_matching_holonomy and not add_disjoint_tables:
        raise ValueError("--matching-holonomy requires --disjoint-tables")
    if add_matching_triangle_tables and not add_disjoint_tables:
        raise ValueError("--matching-triangle-tables requires --disjoint-tables")
    if add_symmetry_seed:
        if block_rep not in {"none", "square"}:
            raise ValueError("--symmetry-seed conflicts with --block-rep nonsquare")
        block_rep = "square"
    if block_rep != "none" and block_rep not in BLOCK_REPS:
        raise ValueError(f"unknown block representative {block_rep}")

    labels = make_labels(14)
    by_fiber = {fiber: sorted(indices) for fiber, indices in labels_by_fiber(labels).items()}
    fibers = sorted(by_fiber)
    model = cp_model.CpModel()

    p = {}
    inverse_constraints = 0
    all_diff_constraints = 0
    pid = {}
    coset = {}
    q = {}
    q_parity = {}
    q_coset = {}
    table_constraints = 0
    coset_table_constraints = 0
    coset_eq_bools = 0
    coset_macro_constraints = 0
    disjoint_table_constraints = 0
    q_parity_table_constraints = 0
    matching_holonomy_constraints = 0
    matching_triangle_table_constraints = 0
    intersecting_table_constraints = 0
    intersecting_pair_table_constraints = 0
    intersecting_triple_table_constraints = 0
    intersecting_parity_table_constraints = 0
    intersecting_coset_table_constraints = 0
    intersecting_parity_vars = 0
    intersecting_coset_vars = 0
    disjoint_relative_perm_vars = 0
    intersecting_relative_perm_vars = 0
    for fa in fibers:
        for fb in fibers:
            if fa == fb or not disjoint(fa, fb):
                continue
            vars_ab = [
                model.NewIntVar(0, 3, f"p_{fa[0]}_{fa[1]}__{fb[0]}_{fb[1]}_{u}")
                for u in range(4)
            ]
            p[fa, fb] = vars_ab
            model.AddAllDifferent(vars_ab)
            all_diff_constraints += 1

    for i, fa in enumerate(fibers):
        for fb in fibers[i + 1:]:
            if not disjoint(fa, fb):
                continue
            model.AddInverse(p[fa, fb], p[fb, fa])
            inverse_constraints += 1

    if (
        add_disjoint_tables
        or add_intersecting_tables
        or add_intersecting_pair_tables
        or add_intersecting_triple_tables
        or add_intersecting_parity_table
        or add_intersecting_coset_table
    ):
        rel_rows = relative_perm_rows()

    if add_coset_projection:
        rows = coset_id_rows()
        for fa, fb in p:
            coset[fa, fb] = model.NewIntVar(0, 2, f"coset_{fa[0]}_{fa[1]}__{fb[0]}_{fb[1]}")
            model.AddAllowedAssignments([coset[fa, fb], *p[fa, fb]], rows)
            coset_table_constraints += 1

        for fa, fb in p:
            common_fibers = [fc for fc in fibers if disjoint(fc, fa) and disjoint(fc, fb)]
            if len(common_fibers) != 3:
                raise AssertionError((fa, fb, common_fibers))

            direct_square = model.NewBoolVar(f"coset_direct_square_{fa}_{fb}")
            model.Add(coset[fa, fb] == 0).OnlyEnforceIf(direct_square)
            model.Add(coset[fa, fb] != 0).OnlyEnforceIf(direct_square.Not())

            equalities = []
            for fc in common_fibers:
                eq = bool_eq_var(
                    model,
                    coset[fa, fc],
                    coset[fb, fc],
                    f"coset_eq_{fa}_{fb}_{fc}",
                )
                equalities.append(eq)
                coset_eq_bools += 1

            for eq in equalities:
                model.Add(eq == 1).OnlyEnforceIf(direct_square)

            total = sum(equalities)
            zero_case = model.NewBoolVar(f"coset_nonsquare_zero_{fa}_{fb}")
            two_case = model.NewBoolVar(f"coset_nonsquare_two_{fa}_{fb}")
            model.Add(total == 0).OnlyEnforceIf(zero_case)
            model.Add(total != 0).OnlyEnforceIf(zero_case.Not())
            model.Add(total == 2).OnlyEnforceIf(two_case)
            model.Add(total != 2).OnlyEnforceIf(two_case.Not())
            model.AddBoolOr([zero_case, two_case]).OnlyEnforceIf(direct_square.Not())
            coset_macro_constraints += 1

    if add_disjoint_tables:
        id_rows = perm_id_rows()
        residual_rows = disjoint_residual_rows()
        parity_rows = perm_parity_rows()
        for fa, fb in p:
            pid[fa, fb] = model.NewIntVar(0, 23, f"pid_{fa[0]}_{fa[1]}__{fb[0]}_{fb[1]}")
            model.AddAllowedAssignments([pid[fa, fb], *p[fa, fb]], id_rows)
            table_constraints += 1
            disjoint_table_constraints += 1

        for ia, fa in enumerate(fibers):
            for fb in fibers[ia + 1:]:
                if not disjoint(fa, fb):
                    continue
                common_fibers = [fc for fc in fibers if disjoint(fc, fa) and disjoint(fc, fb)]
                rel_vars = []
                for fc in common_fibers:
                    q[fa, fb, fc] = model.NewIntVar(0, 23, f"q_{fa}_{fb}_{fc}")
                    model.AddAllowedAssignments([q[fa, fb, fc], *p[fa, fc], *p[fb, fc]], rel_rows)
                    table_constraints += 1
                    disjoint_table_constraints += 1
                    disjoint_relative_perm_vars += 1
                    rel_vars.append(q[fa, fb, fc])
                    if add_matching_holonomy:
                        q_parity[fa, fb, fc] = model.NewBoolVar(f"q_parity_{fa}_{fb}_{fc}")
                        model.AddAllowedAssignments([q_parity[fa, fb, fc], q[fa, fb, fc]], parity_rows)
                        table_constraints += 1
                        q_parity_table_constraints += 1
                model.AddAllowedAssignments([pid[fa, fb], *rel_vars], residual_rows)
                table_constraints += 1
                disjoint_table_constraints += 1

        if add_matching_triangle_tables:
            triangle_rows = sorted(matching_triangle_allowed_triples())
            for ia, fa in enumerate(fibers):
                for ib in range(ia + 1, len(fibers)):
                    fb = fibers[ib]
                    if not disjoint(fa, fb):
                        continue
                    for fc in fibers[ib + 1:]:
                        if not disjoint(fa, fc) or not disjoint(fb, fc):
                            continue
                        model.AddAllowedAssignments(
                            [pid[fa, fb], pid[fa, fc], pid[fb, fc]],
                            triangle_rows,
                        )
                        table_constraints += 1
                        matching_triangle_table_constraints += 1

        if add_matching_holonomy:
            for ia, fa in enumerate(fibers):
                for ib in range(ia + 1, len(fibers)):
                    fb = fibers[ib]
                    if not disjoint(fa, fb):
                        continue
                    for fc in fibers[ib + 1:]:
                        if not disjoint(fa, fc) or not disjoint(fb, fc):
                            continue
                        model.AddAllowedAssignments(
                            [
                                q_parity[fa, fb, fc],
                                q_parity[fb, fc, fa],
                                q_parity[fa, fc, fb],
                            ],
                            matching_holonomy_rows(),
                        )
                        table_constraints += 1
                        matching_holonomy_constraints += 1

    if (
        add_intersecting_tables
        or add_intersecting_pair_tables
        or add_intersecting_triple_tables
        or add_intersecting_parity_table
        or add_intersecting_coset_table
    ):
        parity_rows = perm_parity_rows()
        coset_rows = perm_id_coset_rows()
        for ia, fa in enumerate(fibers):
            for fb in fibers[ia + 1:]:
                if disjoint(fa, fb):
                    continue
                common_fibers = [fc for fc in fibers if disjoint(fc, fa) and disjoint(fc, fb)]
                rel_vars = []
                for fc in common_fibers:
                    q[fa, fb, fc] = model.NewIntVar(0, 23, f"q_{fa}_{fb}_{fc}")
                    model.AddAllowedAssignments([q[fa, fb, fc], *p[fa, fc], *p[fb, fc]], rel_rows)
                    table_constraints += 1
                    intersecting_table_constraints += 1
                    intersecting_relative_perm_vars += 1
                    rel_vars.append(q[fa, fb, fc])
                    if add_intersecting_parity_table:
                        q_parity[fa, fb, fc] = model.NewBoolVar(f"q_parity_inter_{fa}_{fb}_{fc}")
                        model.AddAllowedAssignments([q_parity[fa, fb, fc], q[fa, fb, fc]], parity_rows)
                        table_constraints += 1
                        intersecting_parity_vars += 1
                        intersecting_parity_table_constraints += 1
                    if add_intersecting_coset_table:
                        q_coset[fa, fb, fc] = model.NewIntVar(0, 2, f"q_coset_inter_{fa}_{fb}_{fc}")
                        model.AddAllowedAssignments([q_coset[fa, fb, fc], q[fa, fb, fc]], coset_rows)
                        table_constraints += 1
                        intersecting_coset_vars += 1
                        intersecting_coset_table_constraints += 1
                target = tuple(
                    tuple(2 - overlap(labels, idx_a, idx_b) for idx_b in by_fiber[fb])
                    for idx_a in by_fiber[fa]
                )
                if add_intersecting_parity_table:
                    model.AddAllowedAssignments(
                        [q_parity[fa, fb, fc] for fc in common_fibers],
                        intersecting_parity_projection_rows(target),
                    )
                    table_constraints += 1
                    intersecting_parity_table_constraints += 1
                if add_intersecting_coset_table:
                    model.AddAllowedAssignments(
                        [q_coset[fa, fb, fc] for fc in common_fibers],
                        intersecting_coset_projection_rows(target),
                    )
                    table_constraints += 1
                    intersecting_coset_table_constraints += 1
                if add_intersecting_pair_tables:
                    for left_idx, right_idx in combinations(range(len(rel_vars)), 2):
                        model.AddAllowedAssignments(
                            [rel_vars[left_idx], rel_vars[right_idx]],
                            intersecting_pair_projection_rows(target, left_idx, right_idx),
                        )
                        table_constraints += 1
                        intersecting_pair_table_constraints += 1
                if add_intersecting_triple_tables:
                    for left_idx, middle_idx, right_idx in combinations(range(len(rel_vars)), 3):
                        model.AddAllowedAssignments(
                            [rel_vars[left_idx], rel_vars[middle_idx], rel_vars[right_idx]],
                            intersecting_triple_projection_rows(target, left_idx, middle_idx, right_idx),
                        )
                        table_constraints += 1
                        intersecting_triple_table_constraints += 1
                if add_intersecting_tables:
                    model.AddAllowedAssignments(rel_vars, intersecting_residual_rows(target))
                    table_constraints += 1
                    intersecting_table_constraints += 1

    if block_rep != "none":
        fa = (0, 1)
        fb = (2, 3)
        for u, v in enumerate(BLOCK_REPS[block_rep]):
            model.Add(p[fa, fb][u] == v)

    equality_bools = 0
    pair_equations = 0
    for ia, fa in enumerate(fibers):
        for fb in fibers[ia + 1:]:
            if fa == fb:
                continue
            common_fibers = [fc for fc in fibers if disjoint(fc, fa) and disjoint(fc, fb)]
            if not common_fibers and not disjoint(fa, fb):
                continue
            for ua, label_idx_a in enumerate(by_fiber[fa]):
                for ub, label_idx_b in enumerate(by_fiber[fb]):
                    terms = []
                    for fc in common_fibers:
                        eq = bool_eq_var(
                            model,
                            p[fa, fc][ua],
                            p[fb, fc][ub],
                            f"eq_{fa}_{fb}_{fc}_{ua}_{ub}",
                        )
                        terms.append(eq)
                        equality_bools += 1

                    rhs = 2 - overlap(labels, label_idx_a, label_idx_b)
                    if disjoint(fa, fb):
                        edge_ab = bool_eq_const(
                            model,
                            p[fa, fb][ua],
                            ub,
                            f"x_{fa}_{fb}_{ua}_{ub}",
                        )
                        terms.append(edge_ab)
                        equality_bools += 1
                        # Common neighbours can also lie inside either endpoint
                        # fiber: the forced C4 neighbours of a are common with b
                        # exactly when b's permutation-block neighbour in fa is
                        # one of those forced C4 neighbours, and symmetrically.
                        forced_a = [
                            pos
                            for pos, idx in enumerate(by_fiber[fa])
                            if pos != ua and forced_free_edge_value(labels, label_idx_a, idx) == 1
                        ]
                        forced_b = [
                            pos
                            for pos, idx in enumerate(by_fiber[fb])
                            if pos != ub and forced_free_edge_value(labels, label_idx_b, idx) == 1
                        ]
                        for pos in forced_a:
                            terms.append(
                                bool_eq_const(
                                    model,
                                    p[fb, fa][ub],
                                    pos,
                                    f"same_a_{fa}_{fb}_{ua}_{ub}_{pos}",
                                )
                            )
                            equality_bools += 1
                        for pos in forced_b:
                            terms.append(
                                bool_eq_const(
                                    model,
                                    p[fa, fb][ua],
                                    pos,
                                    f"same_b_{fa}_{fb}_{ua}_{ub}_{pos}",
                                )
                            )
                            equality_bools += 1
                    model.Add(sum(terms) == rhs)
                    pair_equations += 1

    return {
        "model": model,
        "labels": labels,
        "by_fiber": by_fiber,
        "fibers": fibers,
        "p": p,
        "inverse_constraints": inverse_constraints,
        "all_diff_constraints": all_diff_constraints,
        "disjoint_tables": add_disjoint_tables,
        "matching_holonomy": add_matching_holonomy,
        "matching_triangle_tables": add_matching_triangle_tables,
        "coset_projection": add_coset_projection,
        "intersecting_tables": add_intersecting_tables,
        "intersecting_pair_tables": add_intersecting_pair_tables,
        "intersecting_triple_tables": add_intersecting_triple_tables,
        "intersecting_parity_table": add_intersecting_parity_table,
        "intersecting_coset_table": add_intersecting_coset_table,
        "coset_vars": len(coset),
        "coset_table_constraints": coset_table_constraints,
        "coset_eq_bools": coset_eq_bools,
        "coset_macro_constraints": coset_macro_constraints,
        "perm_id_vars": len(pid),
        "relative_perm_vars": len(q),
        "relative_perm_parity_vars": len(q_parity),
        "relative_perm_coset_vars": len(q_coset),
        "disjoint_relative_perm_vars": disjoint_relative_perm_vars,
        "intersecting_relative_perm_vars": intersecting_relative_perm_vars,
        "table_constraints": table_constraints,
        "disjoint_table_constraints": disjoint_table_constraints,
        "q_parity_vars": len(q_parity),
        "q_parity_table_constraints": q_parity_table_constraints,
        "matching_holonomy_constraints": matching_holonomy_constraints,
        "matching_triangle_table_constraints": matching_triangle_table_constraints,
        "intersecting_table_constraints": intersecting_table_constraints,
        "intersecting_pair_table_constraints": intersecting_pair_table_constraints,
        "intersecting_triple_table_constraints": intersecting_triple_table_constraints,
        "intersecting_parity_vars": intersecting_parity_vars,
        "intersecting_coset_vars": intersecting_coset_vars,
        "intersecting_parity_table_constraints": intersecting_parity_table_constraints,
        "intersecting_coset_table_constraints": intersecting_coset_table_constraints,
        "equality_bools": equality_bools,
        "pair_equations": pair_equations,
        "block_rep": block_rep,
        "symmetry_seed": add_symmetry_seed,
    }


def extract_far_adjacency(built, solver):
    labels = built["labels"]
    by_fiber = built["by_fiber"]
    p = built["p"]
    m = len(labels)
    A = [[0] * m for _ in range(m)]

    for i in range(m):
        for j in range(i + 1, m):
            forced = forced_free_edge_value(labels, i, j)
            if forced is not None:
                val = forced
            else:
                fa = next(fiber for fiber, indices in by_fiber.items() if i in indices)
                fb = next(fiber for fiber, indices in by_fiber.items() if j in indices)
                ui = by_fiber[fa].index(i)
                uj = by_fiber[fb].index(j)
                val = int(solver.Value(p[fa, fb][ui]) == uj)
            A[i][j] = A[j][i] = val
    return A


def model_size(model):
    proto = model.Proto()
    bool_vars = sum(1 for var in proto.variables if list(var.domain) == [0, 1])
    int_vars = len(proto.variables) - bool_vars
    return {
        "total_vars": len(proto.variables),
        "bool_vars": bool_vars,
        "int_vars": int_vars,
        "constraints": len(proto.constraints),
    }


def write_solution(path, built, far_adj, adj):
    payload = {
        "type": "root_cell_permutation_solution_v1",
        "labels": built["labels"],
        "far_edges": [
            [i, j]
            for i in range(len(far_adj))
            for j in range(i + 1, len(far_adj))
            if far_adj[i][j]
        ],
        "full_edges": [
            [i, j]
            for i in range(len(adj))
            for j in range(i + 1, len(adj))
            if adj[i][j]
        ],
    }
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description="Rooted k=14 fiber-permutation CSP")
    ap.add_argument("--time-cap", type=float, default=60.0)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--out", default="scratchpad/root_cell_permutation_solution.json")
    ap.add_argument("--json-out")
    ap.add_argument("--log", action="store_true")
    ap.add_argument("--symmetry-seed", action="store_true")
    ap.add_argument("--coset-projection", action="store_true")
    ap.add_argument("--disjoint-tables", action="store_true")
    ap.add_argument("--matching-holonomy", action="store_true")
    ap.add_argument("--matching-triangle-tables", action="store_true")
    ap.add_argument("--intersecting-tables", action="store_true")
    ap.add_argument("--intersecting-pair-tables", action="store_true")
    ap.add_argument("--intersecting-triple-tables", action="store_true")
    ap.add_argument("--intersecting-parity-table", action="store_true")
    ap.add_argument("--intersecting-coset-table", action="store_true")
    ap.add_argument("--block-rep", choices=["none", "square", "nonsquare"], default="none")
    args = ap.parse_args()

    t0 = time.time()
    built = build_model(
        add_symmetry_seed=args.symmetry_seed,
        add_coset_projection=args.coset_projection,
        add_disjoint_tables=args.disjoint_tables,
        add_matching_holonomy=args.matching_holonomy,
        add_matching_triangle_tables=args.matching_triangle_tables,
        add_intersecting_tables=args.intersecting_tables,
        add_intersecting_pair_tables=args.intersecting_pair_tables,
        add_intersecting_triple_tables=args.intersecting_triple_tables,
        add_intersecting_parity_table=args.intersecting_parity_table,
        add_intersecting_coset_table=args.intersecting_coset_table,
        block_rep=args.block_rep,
    )
    build_s = time.time() - t0
    size = model_size(built["model"])

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = args.time_cap
    solver.parameters.num_search_workers = args.workers
    solver.parameters.log_search_progress = bool(args.log)

    print(
        "ROOT-CELL PERM-CSP k=14 fibers=%d directed_blocks=%d inverse=%d "
        "pair_eqs=%d eq_bools=%d coset=%s tables=%d block_rep=%s vars=%d constraints=%d build=%.2fs cap=%.1fs workers=%d"
        % (
            len(built["fibers"]),
            len(built["p"]),
            built["inverse_constraints"],
            built["pair_equations"],
            built["equality_bools"],
            built["coset_projection"],
            built["table_constraints"],
            built["block_rep"],
            size["total_vars"],
            size["constraints"],
            build_s,
            args.time_cap,
            args.workers,
        ),
        flush=True,
    )
    status = solver.Solve(built["model"])
    status_name = solver.StatusName(status)
    print(f"STATUS {status_name}", flush=True)
    print(
        f"wall={solver.WallTime():.2f}s conflicts={solver.NumConflicts()} "
        f"branches={solver.NumBranches()}",
        flush=True,
    )

    result = {
        "type": "root_cell_permutation_csp_run_v1",
        "status": status_name,
        "sat": status in (cp_model.OPTIMAL, cp_model.FEASIBLE),
        "unsat": status == cp_model.INFEASIBLE,
        "wall_seconds": round(solver.WallTime(), 4),
        "conflicts": solver.NumConflicts(),
        "branches": solver.NumBranches(),
        "build_seconds": round(build_s, 4),
        "model_size": size,
        "directed_blocks": len(built["p"]),
        "inverse_constraints": built["inverse_constraints"],
        "all_diff_constraints": built["all_diff_constraints"],
        "pair_equations": built["pair_equations"],
        "equality_bools": built["equality_bools"],
        "disjoint_tables": built["disjoint_tables"],
        "matching_holonomy": built["matching_holonomy"],
        "matching_triangle_tables": built["matching_triangle_tables"],
        "coset_projection": built["coset_projection"],
        "intersecting_tables": built["intersecting_tables"],
        "intersecting_pair_tables": built["intersecting_pair_tables"],
        "intersecting_triple_tables": built["intersecting_triple_tables"],
        "intersecting_parity_table": built["intersecting_parity_table"],
        "intersecting_coset_table": built["intersecting_coset_table"],
        "coset_vars": built["coset_vars"],
        "coset_table_constraints": built["coset_table_constraints"],
        "coset_eq_bools": built["coset_eq_bools"],
        "coset_macro_constraints": built["coset_macro_constraints"],
        "perm_id_vars": built["perm_id_vars"],
        "relative_perm_vars": built["relative_perm_vars"],
        "relative_perm_parity_vars": built["relative_perm_parity_vars"],
        "relative_perm_coset_vars": built["relative_perm_coset_vars"],
        "disjoint_relative_perm_vars": built["disjoint_relative_perm_vars"],
        "intersecting_relative_perm_vars": built["intersecting_relative_perm_vars"],
        "table_constraints": built["table_constraints"],
        "disjoint_table_constraints": built["disjoint_table_constraints"],
        "q_parity_vars": built["q_parity_vars"],
        "q_parity_table_constraints": built["q_parity_table_constraints"],
        "matching_holonomy_constraints": built["matching_holonomy_constraints"],
        "matching_triangle_table_constraints": built["matching_triangle_table_constraints"],
        "intersecting_table_constraints": built["intersecting_table_constraints"],
        "intersecting_pair_table_constraints": built["intersecting_pair_table_constraints"],
        "intersecting_triple_table_constraints": built["intersecting_triple_table_constraints"],
        "intersecting_parity_vars": built["intersecting_parity_vars"],
        "intersecting_coset_vars": built["intersecting_coset_vars"],
        "intersecting_parity_table_constraints": built["intersecting_parity_table_constraints"],
        "intersecting_coset_table_constraints": built["intersecting_coset_table_constraints"],
        "block_rep": built["block_rep"],
        "symmetry_seed": args.symmetry_seed,
    }

    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        far_adj = extract_far_adjacency(built, solver)
        adj = build_full_graph(14, built["labels"], far_adj)
        ok, why = verify_srg(adj, 14)
        result["verify_srg"] = {"ok": ok, "why": why}
        print(f"FULL SRG VERIFY: {ok} ({why})", flush=True)
        if ok:
            write_solution(args.out, built, far_adj, adj)
            print(f"WROTE {args.out}", flush=True)
        else:
            raise SystemExit("permutation CSP solution did not verify as SRG")
    elif status == cp_model.INFEASIBLE:
        print("INFEASIBLE: no rooted fiber-permutation solution under this exact model.", flush=True)
    else:
        print("UNKNOWN: no mathematical verdict under this bounded run.", flush=True)

    if args.json_out:
        path = Path(args.json_out)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"WROTE {path}", flush=True)


if __name__ == "__main__":
    main()
