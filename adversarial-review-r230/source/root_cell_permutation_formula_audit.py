"""
root_cell_permutation_formula_audit.py -- audit the compact permutation equations.

This does not solve the CSP.  It samples arbitrary assignments of one permutation
per disjoint fiber block, reconstructs the full rooted far graph, and checks that
the compact R204 equality-count formula gives exactly the same far common-neighbour
count as the reconstructed graph for every far pair.
"""
import argparse
import json
import random
from itertools import combinations
from pathlib import Path

from root_cell_cpsat import forced_free_edge_value, labels_by_fiber, make_labels, overlap


def disjoint(a, b):
    return set(a).isdisjoint(b)


def random_assignment(fibers, seed):
    rng = random.Random(seed)
    p = {}
    for i, fa in enumerate(fibers):
        for fb in fibers[i + 1:]:
            if not disjoint(fa, fb):
                continue
            perm = list(range(4))
            rng.shuffle(perm)
            inv = [0] * 4
            for u, v in enumerate(perm):
                inv[v] = u
            p[fa, fb] = perm
            p[fb, fa] = inv
    return p


def reconstruct(labels, by_fiber, p):
    index_to_fiber_pos = {}
    for fiber, indices in by_fiber.items():
        for pos, idx in enumerate(indices):
            index_to_fiber_pos[idx] = (fiber, pos)

    n = len(labels)
    A = [[0] * n for _ in range(n)]
    for i in range(n):
        fi, ui = index_to_fiber_pos[i]
        for j in range(i + 1, n):
            forced = forced_free_edge_value(labels, i, j)
            if forced is not None:
                val = forced
            else:
                fj, uj = index_to_fiber_pos[j]
                val = int(p[fi, fj][ui] == uj)
            A[i][j] = A[j][i] = val
    return A, index_to_fiber_pos


def forced_positions(labels, by_fiber, fiber, pos):
    idx = by_fiber[fiber][pos]
    return [
        other_pos
        for other_pos, other_idx in enumerate(by_fiber[fiber])
        if other_pos != pos and forced_free_edge_value(labels, idx, other_idx) == 1
    ]


def compact_common(labels, by_fiber, fibers, p, index_to_fiber_pos, i, j):
    fi, ui = index_to_fiber_pos[i]
    fj, uj = index_to_fiber_pos[j]
    if fi == fj:
        return sum(
            1
            for z in by_fiber[fi]
            if z not in {i, j}
            and forced_free_edge_value(labels, i, z) == 1
            and forced_free_edge_value(labels, j, z) == 1
        )

    common = 0
    for fc in fibers:
        if disjoint(fc, fi) and disjoint(fc, fj):
            common += int(p[fi, fc][ui] == p[fj, fc][uj])

    if disjoint(fi, fj):
        common += int(p[fj, fi][uj] in forced_positions(labels, by_fiber, fi, ui))
        common += int(p[fi, fj][ui] in forced_positions(labels, by_fiber, fj, uj))
    return common


def run(samples):
    labels = make_labels(14)
    by_fiber = {fiber: sorted(indices) for fiber, indices in labels_by_fiber(labels).items()}
    fibers = sorted(by_fiber)
    total_pairs = 0
    for seed in range(samples):
        p = random_assignment(fibers, seed)
        A, index_to_fiber_pos = reconstruct(labels, by_fiber, p)
        for i, j in combinations(range(len(labels)), 2):
            full_common = sum(1 for z in range(len(labels)) if A[i][z] and A[j][z])
            compact = compact_common(labels, by_fiber, fibers, p, index_to_fiber_pos, i, j)
            if full_common != compact:
                return {
                    "ok": False,
                    "seed": seed,
                    "pair": [i, j],
                    "labels": [labels[i], labels[j]],
                    "full_common": full_common,
                    "compact_common": compact,
                }
            total_pairs += 1
    return {
        "ok": True,
        "samples": samples,
        "pairs_checked": total_pairs,
        "type": "root_cell_permutation_formula_audit_v1",
    }


def main():
    ap = argparse.ArgumentParser(description="Audit compact permutation common-neighbour formula")
    ap.add_argument("--samples", type=int, default=20)
    ap.add_argument("--json-out")
    args = ap.parse_args()

    result = run(args.samples)
    print(json.dumps(result, sort_keys=True))
    if not result["ok"]:
        raise SystemExit(1)
    if args.json_out:
        path = Path(args.json_out)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"WROTE {path}")


if __name__ == "__main__":
    main()
