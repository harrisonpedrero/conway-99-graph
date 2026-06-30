"""
root_cell_permutation_sat.py -- CNF encoding of the R204 rooted permutation CSP.

This is a SAT-oriented companion to root_cell_permutation_csp.py.  It uses one
Boolean variable for each possible entry of each disjoint 4x4 fiber block, with
row/column exactly-one clauses, then Tseitin-encodes the compact equality-count
common-neighbour equations.

SAT reconstructs and verifies a full srg(99,14,1,2).  UNSAT from this prototype
is not yet a proof-grade nonexistence certificate unless a proof-logging backend
and independent checker are added.
"""
import argparse
import hashlib
import json
import time
from functools import lru_cache
from itertools import combinations, permutations, product
from pathlib import Path

from pysat.card import CardEnc, EncType
from pysat.formula import CNF, IDPool
from pysat.solvers import Cadical153, Cadical195, Cadical300

from root_cell_cpsat import build_full_graph, forced_free_edge_value, labels_by_fiber, make_labels, overlap, verify_srg


BLOCK_REPS = {
    "square": (0, 1, 2, 3),
    "nonsquare": (0, 1, 3, 2),
}
PERMS = list(permutations(range(4)))
PERM_ID = {perm: idx for idx, perm in enumerate(PERMS)}
TRIANGLE_REP_FIBERS = ((0, 1), (2, 3), (4, 5))
TRIANGLE_REP_IDS = [
    (0, 0, 0),
    (0, 0, 1),
    (0, 0, 2),
    (0, 0, 3),
    (0, 0, 7),
    (0, 0, 9),
    (0, 0, 10),
    (0, 0, 23),
    (0, 1, 1),
    (0, 1, 3),
    (0, 1, 4),
    (0, 1, 5),
    (0, 1, 6),
    (0, 1, 8),
    (0, 1, 11),
    (0, 1, 17),
    (0, 1, 22),
    (1, 1, 1),
    (1, 1, 3),
    (1, 1, 5),
    (1, 1, 9),
    (1, 1, 17),
    (1, 4, 5),
    (1, 4, 9),
]
TRIANGLE_SURVIVOR_REP_INDICES = [0, 2, 7, 8, 10, 15, 21, 22]
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

SOLVER_CLASSES = {
    "cadical153": Cadical153,
    "cadical195": Cadical195,
    "cadical300": Cadical300,
}


def file_sha256(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def disjoint(a, b):
    return set(a).isdisjoint(b)


def invert_perm(perm):
    out = [0] * len(perm)
    for i, j in enumerate(perm):
        out[j] = i
    return tuple(out)


def compose_perm(left, right):
    return tuple(left[i] for i in right)


def triangle_transform_local(triple, actions):
    p01, p02, p12 = triple
    h0, h1, h2 = actions
    return (
        compose_perm(h1, compose_perm(p01, invert_perm(h0))),
        compose_perm(h2, compose_perm(p02, invert_perm(h0))),
        compose_perm(h2, compose_perm(p12, invert_perm(h1))),
    )


def triangle_permute_fibers(triple, sigma):
    p01, p02, p12 = triple
    directed = {
        (0, 1): p01,
        (1, 0): invert_perm(p01),
        (0, 2): p02,
        (2, 0): invert_perm(p02),
        (1, 2): p12,
        (2, 1): invert_perm(p12),
    }
    return (
        directed[(sigma[0], sigma[1])],
        directed[(sigma[0], sigma[2])],
        directed[(sigma[1], sigma[2])],
    )


def matching_triangle_allowed_triples():
    allowed = set()
    for rep_idx in TRIANGLE_SURVIVOR_REP_INDICES:
        rep = tuple(PERMS[i] for i in TRIANGLE_REP_IDS[rep_idx])
        for actions in product(SQUARE_ORBIT, repeat=3):
            moved = triangle_transform_local(rep, actions)
            for sigma in permutations(range(3)):
                key = tuple(PERM_ID[p] for p in triangle_permute_fibers(moved, sigma))
                allowed.add(key)
    return frozenset(allowed)


@lru_cache(maxsize=1)
def right_coset_id_by_perm():
    square = sorted(SQUARE_ORBIT, key=PERMS.index)
    unseen = set(PERMS)
    cosets = []

    first = set(square)
    cosets.append(first)
    unseen -= first

    while unseen:
        rep = min(unseen, key=PERMS.index)
        coset = {compose_perm(rep, sym) for sym in square}
        cosets.append(coset)
        unseen -= coset

    out = {}
    for idx, coset in enumerate(cosets):
        for perm in coset:
            out[perm] = idx
    return out


@lru_cache(maxsize=1)
def perm_ids_by_right_coset():
    coset_id = right_coset_id_by_perm()
    buckets = [[] for _ in range(3)]
    for perm_id, perm in enumerate(PERMS):
        buckets[coset_id[perm]].append(perm_id)
    return tuple(tuple(bucket) for bucket in buckets)


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
def intersecting_coset_projection_rows(target):
    coset_id = right_coset_id_by_perm()
    return sorted(
        {
            tuple(coset_id[PERMS[perm_id]] for perm_id in row)
            for row in intersecting_residual_rows(target)
        }
    )


class PermutationSat:
    def __init__(
        self,
        block_rep="none",
        card_encoding="seqcounter",
        triangle_rep_index=None,
        matching_triangle_cuts=False,
        intersecting_coset_cuts=False,
    ):
        if block_rep != "none" and block_rep not in BLOCK_REPS:
            raise ValueError(f"unknown block representative {block_rep}")
        if card_encoding not in {"seqcounter", "direct"}:
            raise ValueError(f"unknown cardinality encoding {card_encoding}")
        if triangle_rep_index is not None and not (0 <= triangle_rep_index < len(TRIANGLE_REP_IDS)):
            raise ValueError(f"triangle_rep_index must be 0..{len(TRIANGLE_REP_IDS) - 1}")
        if triangle_rep_index is not None and block_rep != "none":
            first_perm = PERMS[TRIANGLE_REP_IDS[triangle_rep_index][0]]
            if first_perm != BLOCK_REPS[block_rep]:
                raise ValueError("--triangle-rep-index conflicts with --block-rep")
        self.labels = make_labels(14)
        self.by_fiber = {fiber: sorted(indices) for fiber, indices in labels_by_fiber(self.labels).items()}
        self.fibers = sorted(self.by_fiber)
        self.block_rep = block_rep
        self.card_encoding = card_encoding
        self.triangle_rep_index = triangle_rep_index
        self.matching_triangle_cuts = matching_triangle_cuts
        self.intersecting_coset_cuts = intersecting_coset_cuts
        self.vpool = IDPool()
        self.cnf = CNF()
        self.equality_image_cache = {}
        self.relative_perm_cache = {}
        self.relative_coset_cache = {}
        self.stats = {
            "block_rep": block_rep,
            "block_rep_unit_clauses": 0,
            "card_encoding": card_encoding,
            "triangle_rep_index": triangle_rep_index,
            "triangle_rep_ids": (
                list(TRIANGLE_REP_IDS[triangle_rep_index])
                if triangle_rep_index is not None
                else None
            ),
            "triangle_rep_unit_clauses": 0,
            "matching_triangle_cuts": bool(matching_triangle_cuts),
            "matching_triangle_allowed_triples": 0,
            "matching_triangle_forbidden_triples": 0,
            "matching_triangle_cut_clauses": 0,
            "intersecting_coset_cuts": bool(intersecting_coset_cuts),
            "intersecting_coset_tables": 0,
            "intersecting_coset_allowed_rows": 0,
            "intersecting_coset_forbidden_rows": 0,
            "intersecting_coset_cut_clauses": 0,
            "intersecting_coset_vars": 0,
            "intersecting_rel_perm_vars": 0,
            "intersecting_rel_perm_def_clauses": 0,
            "intersecting_coset_def_clauses": 0,
            "intersecting_coset_exactly_one_clauses": 0,
            "block_vars": 0,
            "row_col_exactly_one": 0,
            "equality_terms": 0,
            "and_terms": 0,
            "pair_equations": 0,
        }

    def var(self, fa, fb, ua, ub):
        if fa == fb or not disjoint(fa, fb):
            raise ValueError("block variable requested for non-disjoint fibers")
        if fa < fb:
            return self.vpool.id(("x", fa, fb, ua, ub))
        return self.vpool.id(("x", fb, fa, ub, ua))

    def add_card_equals(self, lits, bound):
        if self.card_encoding == "seqcounter":
            enc = CardEnc.equals(lits=lits, bound=bound, vpool=self.vpool, encoding=EncType.seqcounter)
            self.cnf.extend(enc.clauses)
            return

        if bound < 0 or bound > len(lits):
            self.cnf.append([])
            return
        if bound == 0:
            self.cnf.extend([[-lit] for lit in lits])
            return
        if bound == len(lits):
            self.cnf.extend([[lit] for lit in lits])
            return

        # At most bound: no bound+1 literals can be true.
        for combo in combinations(lits, bound + 1):
            self.cnf.append([-lit for lit in combo])
        # At least bound: no len(lits)-bound+1 literals can be false.
        for combo in combinations(lits, len(lits) - bound + 1):
            self.cnf.append(list(combo))

    def add_permutation_blocks(self):
        for fa, fb in combinations(self.fibers, 2):
            if not disjoint(fa, fb):
                continue
            for ua in range(4):
                self.add_card_equals([self.var(fa, fb, ua, ub) for ub in range(4)], 1)
                self.stats["row_col_exactly_one"] += 1
            for ub in range(4):
                self.add_card_equals([self.var(fa, fb, ua, ub) for ua in range(4)], 1)
                self.stats["row_col_exactly_one"] += 1
        self.stats["block_vars"] = 105 * 16

    def add_and_equiv(self, a, b):
        t = self.vpool.id(("and", a, b))
        self.cnf.append([-t, a])
        self.cnf.append([-t, b])
        self.cnf.append([t, -a, -b])
        self.stats["and_terms"] += 1
        return t

    def add_or_equiv(self, terms):
        e = self.vpool.id(("eq", tuple(terms)))
        for t in terms:
            self.cnf.append([-t, e])
        self.cnf.append([-e] + list(terms))
        self.stats["equality_terms"] += 1
        return e

    def equality_image_lit(self, fa, fb, ua, ub, fc):
        key = (fa, fb, ua, ub, fc)
        if key in self.equality_image_cache:
            return self.equality_image_cache[key]
        terms = [
            self.add_and_equiv(self.var(fa, fc, ua, w), self.var(fb, fc, ub, w))
            for w in range(4)
        ]
        lit = self.add_or_equiv(terms)
        self.equality_image_cache[key] = lit
        return lit

    def add_block_representative(self):
        if self.block_rep == "none":
            return
        fa = (0, 1)
        fb = (2, 3)
        self.add_block_units(fa, fb, BLOCK_REPS[self.block_rep], "block_rep_unit_clauses")

    def add_block_units(self, fa, fb, perm, stat_key):
        for ua, ub in enumerate(perm):
            self.cnf.append([self.var(fa, fb, ua, ub)])
            self.stats[stat_key] += 1

    def add_triangle_representative(self):
        if self.triangle_rep_index is None:
            return
        rep = TRIANGLE_REP_IDS[self.triangle_rep_index]
        fa, fb, fc = TRIANGLE_REP_FIBERS
        self.add_block_units(fa, fb, PERMS[rep[0]], "triangle_rep_unit_clauses")
        self.add_block_units(fa, fc, PERMS[rep[1]], "triangle_rep_unit_clauses")
        self.add_block_units(fb, fc, PERMS[rep[2]], "triangle_rep_unit_clauses")

    def add_matching_triangle_cuts(self):
        if not self.matching_triangle_cuts:
            return
        allowed = matching_triangle_allowed_triples()
        forbidden = [
            triple
            for triple in product(range(len(PERMS)), repeat=3)
            if triple not in allowed
        ]
        matching_triples = [
            triple
            for triple in combinations(self.fibers, 3)
            if disjoint(triple[0], triple[1])
            and disjoint(triple[0], triple[2])
            and disjoint(triple[1], triple[2])
        ]
        self.stats["matching_triangle_allowed_triples"] = len(allowed)
        self.stats["matching_triangle_forbidden_triples"] = len(forbidden)
        for fa, fb, fc in matching_triples:
            for pa, pb, pc in forbidden:
                clause = []
                for left, right, perm_id in (
                    (fa, fb, pa),
                    (fa, fc, pb),
                    (fb, fc, pc),
                ):
                    clause.extend(
                        -self.var(left, right, ua, ub)
                        for ua, ub in enumerate(PERMS[perm_id])
                    )
                self.cnf.append(clause)
                self.stats["matching_triangle_cut_clauses"] += 1

    def add_small_exactly_one(self, lits, stat_key):
        self.cnf.append(list(lits))
        self.stats[stat_key] += 1
        for a, b in combinations(lits, 2):
            self.cnf.append([-a, -b])
            self.stats[stat_key] += 1

    def relative_perm_lit(self, fa, fb, fc, perm_id):
        key = (fa, fb, fc, perm_id)
        if key in self.relative_perm_cache:
            return self.relative_perm_cache[key]
        lit = self.vpool.id(("relperm", fa, fb, fc, perm_id))
        eqs = [
            self.equality_image_lit(fa, fb, ua, ub, fc)
            for ua, ub in enumerate(PERMS[perm_id])
        ]
        for eq in eqs:
            self.cnf.append([-lit, eq])
            self.stats["intersecting_rel_perm_def_clauses"] += 1
        self.cnf.append([lit] + [-eq for eq in eqs])
        self.stats["intersecting_rel_perm_def_clauses"] += 1
        self.stats["intersecting_rel_perm_vars"] += 1
        self.relative_perm_cache[key] = lit
        return lit

    def relative_coset_lit(self, fa, fb, fc, coset_id):
        key = (fa, fb, fc, coset_id)
        if key in self.relative_coset_cache:
            return self.relative_coset_cache[key]
        lit = self.vpool.id(("relcoset", fa, fb, fc, coset_id))
        rels = [
            self.relative_perm_lit(fa, fb, fc, perm_id)
            for perm_id in perm_ids_by_right_coset()[coset_id]
        ]
        for rel in rels:
            self.cnf.append([-rel, lit])
            self.stats["intersecting_coset_def_clauses"] += 1
        self.cnf.append([-lit] + rels)
        self.stats["intersecting_coset_def_clauses"] += 1
        self.stats["intersecting_coset_vars"] += 1
        self.relative_coset_cache[key] = lit
        return lit

    def add_intersecting_coset_cuts(self):
        if not self.intersecting_coset_cuts:
            return
        all_coset_rows = set(product(range(3), repeat=6))
        for fa, fb in combinations(self.fibers, 2):
            if disjoint(fa, fb):
                continue
            common_fibers = [
                fc for fc in self.fibers if disjoint(fc, fa) and disjoint(fc, fb)
            ]
            if len(common_fibers) != 6:
                raise AssertionError((fa, fb, common_fibers))
            target = tuple(
                tuple(2 - overlap(self.labels, idx_a, idx_b) for idx_b in self.by_fiber[fb])
                for idx_a in self.by_fiber[fa]
            )
            allowed = set(intersecting_coset_projection_rows(target))
            forbidden = sorted(all_coset_rows - allowed)
            self.stats["intersecting_coset_tables"] += 1
            self.stats["intersecting_coset_allowed_rows"] += len(allowed)
            self.stats["intersecting_coset_forbidden_rows"] += len(forbidden)
            for fc in common_fibers:
                self.add_small_exactly_one(
                    [self.relative_coset_lit(fa, fb, fc, coset_id) for coset_id in range(3)],
                    "intersecting_coset_exactly_one_clauses",
                )
            for row in forbidden:
                clause = [
                    -self.relative_coset_lit(fa, fb, fc, coset_id)
                    for fc, coset_id in zip(common_fibers, row)
                ]
                self.cnf.append(clause)
                self.stats["intersecting_coset_cut_clauses"] += 1

    def forced_positions(self, fiber, pos):
        idx = self.by_fiber[fiber][pos]
        return [
            other_pos
            for other_pos, other_idx in enumerate(self.by_fiber[fiber])
            if other_pos != pos and forced_free_edge_value(self.labels, idx, other_idx) == 1
        ]

    def add_pair_equations(self):
        for fa, fb in combinations(self.fibers, 2):
            common_fibers = [fc for fc in self.fibers if disjoint(fc, fa) and disjoint(fc, fb)]
            for ua, label_idx_a in enumerate(self.by_fiber[fa]):
                for ub, label_idx_b in enumerate(self.by_fiber[fb]):
                    terms = [
                        self.equality_image_lit(fa, fb, ua, ub, fc)
                        for fc in common_fibers
                    ]
                    rhs = 2 - overlap(self.labels, label_idx_a, label_idx_b)
                    if disjoint(fa, fb):
                        terms.append(self.var(fa, fb, ua, ub))
                        for pos in self.forced_positions(fa, ua):
                            terms.append(self.var(fb, fa, ub, pos))
                        for pos in self.forced_positions(fb, ub):
                            terms.append(self.var(fa, fb, ua, pos))
                    self.add_card_equals(terms, rhs)
                    self.stats["pair_equations"] += 1

    def build(self):
        self.add_permutation_blocks()
        self.add_block_representative()
        self.add_triangle_representative()
        self.add_matching_triangle_cuts()
        self.add_intersecting_coset_cuts()
        self.add_pair_equations()
        self.stats["cnf_vars"] = self.vpool.top
        self.stats["cnf_clauses"] = len(self.cnf.clauses)
        return self

    def far_adjacency_from_model(self, model):
        index_to_fiber_pos = {}
        for fiber, indices in self.by_fiber.items():
            for pos, idx in enumerate(indices):
                index_to_fiber_pos[idx] = (fiber, pos)

        n = len(self.labels)
        A = [[0] * n for _ in range(n)]
        true_vars = set(model)
        for i in range(n):
            fi, ui = index_to_fiber_pos[i]
            for j in range(i + 1, n):
                forced = forced_free_edge_value(self.labels, i, j)
                if forced is not None:
                    val = forced
                else:
                    fj, uj = index_to_fiber_pos[j]
                    val = int(self.var(fi, fj, ui, uj) in true_vars)
                A[i][j] = A[j][i] = val
        return A


def solve(cnf, solver_name, time_cap):
    solver = SOLVER_CLASSES[solver_name](bootstrap_with=cnf.clauses)
    start = time.time()
    sat = None
    model = None
    try:
        while True:
            solver.conf_budget(10000)
            sat = solver.solve_limited(expect_interrupt=True)
            if sat is not None:
                break
            if time.time() - start >= time_cap:
                break
        if sat:
            model = solver.get_model()
        accum = solver.accum_stats()
        return sat, model, accum, time.time() - start
    finally:
        solver.delete()


def main():
    ap = argparse.ArgumentParser(description="SAT prototype for R204 rooted permutation CSP")
    ap.add_argument("--time-cap", type=float, default=60.0)
    ap.add_argument("--solver", choices=sorted(SOLVER_CLASSES), default="cadical195")
    ap.add_argument(
        "--block-rep",
        choices=["none", "square", "nonsquare"],
        default="none",
        help="optional exhaustive symmetry-slice representative for block (0,1)x(2,3)",
    )
    ap.add_argument(
        "--card-encoding",
        choices=["seqcounter", "direct"],
        default="seqcounter",
        help="encoding for small exactly-k constraints",
    )
    ap.add_argument(
        "--triangle-rep-index",
        type=int,
        help="optional 24-case matching-triangle symmetry representative from R220",
    )
    ap.add_argument(
        "--matching-triangle-cuts",
        action="store_true",
        help="add the R220 full matching-triangle forbidden-triple clauses to every matching triple",
    )
    ap.add_argument(
        "--intersecting-coset-cuts",
        action="store_true",
        help="add the R227 D8-coset projection clauses for every intersecting fiber pair",
    )
    ap.add_argument("--json-out")
    ap.add_argument("--cnf-out", help="write the encoded formula as DIMACS CNF")
    ap.add_argument("--no-solve", action="store_true", help="build/export only; do not invoke a SAT solver")
    ap.add_argument("--solution-out", default="scratchpad/root_cell_permutation_sat_solution.json")
    args = ap.parse_args()

    t0 = time.time()
    enc = PermutationSat(
        block_rep=args.block_rep,
        card_encoding=args.card_encoding,
        triangle_rep_index=args.triangle_rep_index,
        matching_triangle_cuts=args.matching_triangle_cuts,
        intersecting_coset_cuts=args.intersecting_coset_cuts,
    ).build()
    build_s = time.time() - t0
    print(
        "ROOT-CELL PERM-SAT vars=%d clauses=%d pair_eqs=%d eq_terms=%d and_terms=%d block_rep=%s triangle_rep=%s triangle_cuts=%s intersect_coset=%s card=%s build=%.2fs solver=%s cap=%.1fs"
        % (
            enc.stats["cnf_vars"],
            enc.stats["cnf_clauses"],
            enc.stats["pair_equations"],
            enc.stats["equality_terms"],
            enc.stats["and_terms"],
            args.block_rep,
            args.triangle_rep_index,
            args.matching_triangle_cuts,
            args.intersecting_coset_cuts,
            args.card_encoding,
            build_s,
            args.solver,
            args.time_cap,
        ),
        flush=True,
    )

    cnf_info = None
    if args.cnf_out:
        cnf_path = Path(args.cnf_out)
        cnf_path.parent.mkdir(parents=True, exist_ok=True)
        enc.cnf.to_file(str(cnf_path))
        cnf_info = {
            "path": str(cnf_path),
            "sha256": file_sha256(cnf_path),
            "bytes": cnf_path.stat().st_size,
        }
        print(
            "WROTE CNF %s sha256=%s bytes=%d"
            % (cnf_info["path"], cnf_info["sha256"], cnf_info["bytes"]),
            flush=True,
        )

    if args.no_solve:
        sat = None
        model = None
        accum = {}
        solve_s = 0.0
        status = "NOT_RUN"
        print("STATUS NOT_RUN (--no-solve)", flush=True)
    else:
        sat, model, accum, solve_s = solve(enc.cnf, args.solver, args.time_cap)
        status = "SAT" if sat is True else "UNSAT" if sat is False else "UNKNOWN"
        print(f"STATUS {status}", flush=True)
        print(f"wall={solve_s:.2f}s stats={accum}", flush=True)

    result = {
        "type": "root_cell_permutation_sat_run_v1",
        "status": status,
        "sat": sat is True,
        "unsat": sat is False,
        "build_seconds": round(build_s, 4),
        "solve_seconds": round(solve_s, 4),
        "solver": args.solver,
        "solver_stats": accum,
        "encoding_stats": enc.stats,
        "cnf_out": cnf_info,
        "no_solve": bool(args.no_solve),
    }
    if sat is True:
        far_adj = enc.far_adjacency_from_model(model)
        adj = build_full_graph(14, enc.labels, far_adj)
        ok, why = verify_srg(adj, 14)
        result["verify_srg"] = {"ok": ok, "why": why}
        print(f"FULL SRG VERIFY: {ok} ({why})", flush=True)
        if ok:
            payload = {
                "type": "root_cell_permutation_sat_solution_v1",
                "labels": enc.labels,
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
            path = Path(args.solution_out)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            print(f"WROTE {path}", flush=True)
        else:
            raise SystemExit("SAT model did not verify as SRG")

    if args.json_out:
        path = Path(args.json_out)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"WROTE {path}", flush=True)


if __name__ == "__main__":
    main()
