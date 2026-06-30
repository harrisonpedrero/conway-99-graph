"""
root_cell_cpsat.py -- CP-SAT probe for the fixed-root type skeleton.

This probes the formulation derived in root_cell_scheme.py.  For k=14, SAT is
equivalent to a full srg(99,14,1,2) with one rooted 7K2 neighbourhood, because
the fixed local labels plus the constraints below exactly enforce every
lambda=1 / mu=2 pair type.

The model is deliberately bounded and honest:

    python root_cell_cpsat.py --k 4 --time-cap 10
    python root_cell_cpsat.py --k 14 --time-cap 60 --workers 8

Statuses:
  OPTIMAL/FEASIBLE -> reconstruct and verify the full SRG.
  INFEASIBLE       -> a nonexistence proof for this rooted formulation.
  UNKNOWN          -> no mathematical verdict.
"""
import argparse
import json
import time
from pathlib import Path

from ortools.sat.python import cp_model


def local_mate(i):
    return i ^ 1


def make_labels(k):
    labels = []
    for a in range(k):
        for b in range(a + 1, k):
            if local_mate(a) != b:
                labels.append((a, b))
    return labels


def overlap(labels, i, j):
    return len(set(labels[i]) & set(labels[j]))


def label_pair_ids(label):
    return tuple(sorted((label[0] // 2, label[1] // 2)))


def labels_by_fiber(labels):
    by_fiber = {}
    for idx, label in enumerate(labels):
        by_fiber.setdefault(label_pair_ids(label), []).append(idx)
    return by_fiber


def forced_free_edge_value(labels, i, j):
    """Return 1/0 for forced pairs, or None for genuine free candidates."""
    fi = label_pair_ids(labels[i])
    fj = label_pair_ids(labels[j])
    ov = overlap(labels, i, j)
    if fi == fj:
        return 1 if ov == 1 else 0
    if set(fi).isdisjoint(fj):
        return None
    return 0


def product_expr(model, a, b, name):
    if isinstance(a, int) and isinstance(b, int):
        return a * b
    if isinstance(a, int):
        return b if a else 0
    if isinstance(b, int):
        return a if b else 0
    p = model.NewBoolVar(name)
    model.AddMultiplicationEquality(p, [a, b])
    return p


def build_model(k, add_commutation=True, free_edge_vars=False, fiber_permutation=False):
    if fiber_permutation and not free_edge_vars:
        raise ValueError("fiber_permutation requires free_edge_vars")
    labels = make_labels(k)
    m = len(labels)
    model = cp_model.CpModel()

    x = {}
    forced_edges = {}
    for i in range(m):
        for j in range(i + 1, m):
            forced = forced_free_edge_value(labels, i, j) if free_edge_vars else None
            if forced is None:
                x[i, j] = model.NewBoolVar(f"x_{i}_{j}")
            else:
                forced_edges[i, j] = forced

    def edge(i, j):
        if i == j:
            raise ValueError("diagonal edge requested")
        key = (i, j) if i < j else (j, i)
        if key in x:
            return x[key]
        return forced_edges[key]

    s_neighbours = {
        i: [j for j in range(m) if j != i and overlap(labels, i, j) == 1]
        for i in range(m)
    }

    # Far graph degree: each far vertex has k-2 neighbours inside Gamma_2(root).
    for i in range(m):
        model.Add(sum(edge(i, j) for j in range(m) if j != i) == k - 2)

    fiber_permutation_constraints = 0
    if fiber_permutation:
        by_fiber = labels_by_fiber(labels)
        fibers = sorted(by_fiber)
        for pos, fa in enumerate(fibers):
            for fb in fibers[pos + 1:]:
                if not set(fa).isdisjoint(fb):
                    continue
                left = by_fiber[fa]
                right = by_fiber[fb]
                for i in left:
                    model.Add(sum(edge(i, j) for j in right) == 1)
                    fiber_permutation_constraints += 1
                for j in right:
                    model.Add(sum(edge(i, j) for i in left) == 1)
                    fiber_permutation_constraints += 1

    # L-F lambda/mu equations: A_F N = 2J - N(I+M).
    for i, lab in enumerate(labels):
        lab_set = set(lab)
        for local in range(k):
            rhs = 2 - int(local in lab_set) - int(local_mate(local) in lab_set)
            model.Add(
                sum(edge(i, j) for j, other in enumerate(labels)
                    if j != i and local in other)
                == rhs
            )

    # F-F lambda/mu equations:
    #   common_F(i,j) + x_ij + overlap(i,j) = 2.
    products = {}
    for i in range(m):
        for j in range(i + 1, m):
            common_terms = []
            for z in range(m):
                if z == i or z == j:
                    continue
                key = tuple(sorted((i, j, z)))
                # The product depends on the centre z as well as pair i,j; do
                # not share across triples with different edge pairs.
                key = (i, j, z)
                p = product_expr(model, edge(i, z), edge(j, z), f"p_{i}_{j}_{z}")
                products[key] = p
                common_terms.append(p)
            model.Add(sum(common_terms) + edge(i, j) == 2 - overlap(labels, i, j))

    # Linear consequence made explicit for propagation:
    # R142 shows AS=SA is already implied by AN plus symmetry, since
    # N N^T = S + 2I.  It is not an independent rank cut, but it is still much
    # cheaper for the solver to see directly than to rediscover indirectly.
    if add_commutation:
        for i in range(m):
            for j in range(i + 1, m):
                model.Add(
                    sum(edge(i, z) for z in s_neighbours[j] if z != i)
                    ==
                    sum(edge(j, z) for z in s_neighbours[i] if z != j)
                )

    metadata = {
        "free_edge_vars": free_edge_vars,
        "edge_vars": len(x),
        "forced_edge_constants": sum(1 for value in forced_edges.values() if value == 1),
        "forced_nonedge_constants": sum(1 for value in forced_edges.values() if value == 0),
        "fiber_permutation": fiber_permutation,
        "fiber_permutation_constraints": fiber_permutation_constraints,
    }
    return model, labels, x, metadata


def extract_far_adjacency(labels, xvars, solver, free_edge_vars=False):
    m = len(labels)
    A = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(i + 1, m):
            var = xvars.get((i, j))
            if var is None:
                forced = forced_free_edge_value(labels, i, j) if free_edge_vars else None
                if forced is None:
                    raise ValueError(f"missing edge variable for {(i, j)}")
                val = forced
            else:
                val = int(solver.Value(var))
            A[i][j] = A[j][i] = val
    return A


def build_full_graph(k, labels, far_adj):
    root = 0
    local_offset = 1
    far_offset = 1 + k
    n = 1 + k + len(labels)
    adj = [[False] * n for _ in range(n)]

    def add(u, v):
        adj[u][v] = adj[v][u] = True

    for local in range(k):
        add(root, local_offset + local)
    for local in range(0, k, 2):
        add(local_offset + local, local_offset + local + 1)
    for i, lab in enumerate(labels):
        u = far_offset + i
        for local in lab:
            add(u, local_offset + local)
    for i in range(len(labels)):
        for j in range(i + 1, len(labels)):
            if far_adj[i][j]:
                add(far_offset + i, far_offset + j)
    return adj


def verify_srg(adj, k, lam=1, mu=2):
    n = len(adj)
    degrees = [sum(row) for row in adj]
    if any(d != k for d in degrees):
        return False, f"degree set {sorted(set(degrees))}"
    for i in range(n):
        for j in range(i + 1, n):
            common = sum(1 for z in range(n) if adj[i][z] and adj[j][z])
            if adj[i][j] and common != lam:
                return False, f"edge {(i, j)} has lambda {common}"
            if not adj[i][j] and common != mu:
                return False, f"nonedge {(i, j)} has mu {common}"
    return True, "ok"


def write_solution(path, k, labels, far_adj, adj):
    payload = {
        "type": "root_cell_solution_v1",
        "k": k,
        "n": len(adj),
        "labels": labels,
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
    ap = argparse.ArgumentParser(description="CP-SAT root-cell skeleton probe")
    ap.add_argument("--k", type=int, default=14, help="SRG degree; use 4 for rook9, 14 for srg99")
    ap.add_argument("--time-cap", type=float, default=60.0)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--out", default="scratchpad/root_cell_cpsat_solution.json")
    ap.add_argument("--log", action="store_true", help="print CP-SAT internal search log")
    ap.add_argument("--no-commute", action="store_true",
                    help="do not add the implied linear AS=SA constraints")
    ap.add_argument("--free-edge-vars", action="store_true",
                    help="use the forced/free Gamma_2 split and create variables only for genuine free edges")
    ap.add_argument("--fiber-permutation", action="store_true",
                    help="add the k=14 consequence that each disjoint 4x4 fiber block is a permutation matrix")
    args = ap.parse_args()

    if args.k % 2 != 0 or args.k < 4:
        raise SystemExit("--k must be even and at least 4")

    t0 = time.time()
    model, labels, xvars, metadata = build_model(
        args.k,
        add_commutation=not args.no_commute,
        free_edge_vars=args.free_edge_vars,
        fiber_permutation=args.fiber_permutation,
    )
    build_s = time.time() - t0

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = args.time_cap
    solver.parameters.num_search_workers = args.workers
    solver.parameters.log_search_progress = bool(args.log)

    print(f"ROOT-CELL CP-SAT k={args.k} far={len(labels)} "
          f"edge_vars={len(xvars)} commute={not args.no_commute} "
          f"free_edge_vars={args.free_edge_vars} "
          f"fiber_permutation={args.fiber_permutation} "
          f"forced_edges={metadata['forced_edge_constants']} "
          f"forced_nonedges={metadata['forced_nonedge_constants']} "
          f"fiber_perm_constraints={metadata['fiber_permutation_constraints']} "
          f"build={build_s:.2f}s "
          f"time_cap={args.time_cap}s workers={args.workers}", flush=True)
    status = solver.Solve(model)
    status_name = solver.StatusName(status)
    print(f"STATUS {status_name}", flush=True)
    print(f"wall={solver.WallTime():.2f}s conflicts={solver.NumConflicts()} "
          f"branches={solver.NumBranches()}", flush=True)

    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        far_adj = extract_far_adjacency(labels, xvars, solver, free_edge_vars=args.free_edge_vars)
        adj = build_full_graph(args.k, labels, far_adj)
        ok, why = verify_srg(adj, args.k)
        print(f"FULL SRG VERIFY: {ok} ({why})", flush=True)
        if ok:
            write_solution(args.out, args.k, labels, far_adj, adj)
            print(f"WROTE {args.out}", flush=True)
        else:
            raise SystemExit("solver model did not verify as SRG")
    elif status == cp_model.INFEASIBLE:
        print("INFEASIBLE: the rooted type skeleton has no solution for this k.", flush=True)
    else:
        print("UNKNOWN: no mathematical verdict under this bounded run.", flush=True)


if __name__ == "__main__":
    main()
