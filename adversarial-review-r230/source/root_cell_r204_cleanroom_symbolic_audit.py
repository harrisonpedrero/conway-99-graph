"""Clean-room symbolic audit for the R204 rooted permutation reduction.

This script intentionally does not import the project encoding modules.  It
rebuilds the rooted far-cell labels from the SRG parameters, derives the forced
same/intersecting-fiber adjacencies, and checks two R204 facts:

1. The same-fiber equations force the free-neighbour sets of the four vertices
   in each fiber to be pairwise disjoint.  Together with the k=14 degree count,
   this proves every disjoint 4x4 fiber block is a permutation matrix.
2. For every distinct-fiber far pair, the compact R204 equality-count equation
   is exactly the symbolic expansion of the full far-pair SRG equation

       common_F(x,y) + edge_F(x,y) = 2 - |label(x) cap label(y)|.

The comparison is by canonical symbolic term multisets, not by sampling any
permutation assignment.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from itertools import combinations
from pathlib import Path


K = 14


def local_mate(i: int) -> int:
    return i ^ 1


def make_labels(k: int = K) -> list[tuple[int, int]]:
    return [
        (a, b)
        for a in range(k)
        for b in range(a + 1, k)
        if local_mate(a) != b
    ]


def label_pair_ids(label: tuple[int, int]) -> tuple[int, int]:
    return tuple(sorted((label[0] // 2, label[1] // 2)))


def labels_by_fiber(labels: list[tuple[int, int]]) -> dict[tuple[int, int], list[int]]:
    by_fiber: dict[tuple[int, int], list[int]] = {}
    for idx, label in enumerate(labels):
        by_fiber.setdefault(label_pair_ids(label), []).append(idx)
    return {fiber: sorted(indices) for fiber, indices in by_fiber.items()}


def overlap(labels: list[tuple[int, int]], i: int, j: int) -> int:
    return len(set(labels[i]) & set(labels[j]))


def disjoint_fibers(left: tuple[int, int], right: tuple[int, int]) -> bool:
    return set(left).isdisjoint(right)


def forced_far_edge(labels: list[tuple[int, int]], i: int, j: int) -> int | None:
    fi = label_pair_ids(labels[i])
    fj = label_pair_ids(labels[j])
    ov = overlap(labels, i, j)
    if fi == fj:
        return 1 if ov == 1 else 0
    if disjoint_fibers(fi, fj):
        return None
    return 0


def fiber_positions(by_fiber: dict[tuple[int, int], list[int]]) -> dict[int, tuple[tuple[int, int], int]]:
    out = {}
    for fiber, indices in by_fiber.items():
        for pos, idx in enumerate(indices):
            out[idx] = (fiber, pos)
    return out


def canonical_var(fa: tuple[int, int], fb: tuple[int, int], ua: int, ub: int) -> tuple:
    """Canonical Boolean for the free edge between two disjoint fiber positions."""
    if fa == fb or not disjoint_fibers(fa, fb):
        raise ValueError("free variable requested for non-disjoint fibers")
    if fa < fb:
        return ("x", fa, fb, ua, ub)
    return ("x", fb, fa, ub, ua)


def edge_expr(
    labels: list[tuple[int, int]],
    pos: dict[int, tuple[tuple[int, int], int]],
    i: int,
    j: int,
):
    if i == j:
        return 0
    forced = forced_far_edge(labels, i, j)
    if forced is not None:
        return forced
    fi, ui = pos[i]
    fj, uj = pos[j]
    return canonical_var(fi, fj, ui, uj)


def multiply_terms(left, right):
    if left == 0 or right == 0:
        return None
    if left == 1:
        return right
    if right == 1:
        return left
    if left == right:
        return left
    return ("and", left, right) if repr(left) <= repr(right) else ("and", right, left)


def forced_positions(
    labels: list[tuple[int, int]],
    by_fiber: dict[tuple[int, int], list[int]],
    fiber: tuple[int, int],
    pos: int,
) -> list[int]:
    idx = by_fiber[fiber][pos]
    return [
        other_pos
        for other_pos, other_idx in enumerate(by_fiber[fiber])
        if other_pos != pos and forced_far_edge(labels, idx, other_idx) == 1
    ]


def full_far_pair_lhs_terms(labels, by_fiber, index_pos, i: int, j: int) -> Counter:
    """Symbolic full equation LHS: common far neighbours plus endpoint edge."""
    terms = Counter()
    for z in range(len(labels)):
        if z == i or z == j:
            continue
        term = multiply_terms(
            edge_expr(labels, index_pos, i, z),
            edge_expr(labels, index_pos, j, z),
        )
        if term is not None:
            terms[term] += 1

    endpoint_edge = edge_expr(labels, index_pos, i, j)
    if endpoint_edge != 0:
        terms[endpoint_edge] += 1
    return terms


def compact_r204_lhs_terms(labels, by_fiber, fibers, index_pos, i: int, j: int) -> Counter:
    fi, ui = index_pos[i]
    fj, uj = index_pos[j]
    terms = Counter()
    common_fibers = [
        fc for fc in fibers if disjoint_fibers(fc, fi) and disjoint_fibers(fc, fj)
    ]

    for fc in common_fibers:
        for w in range(4):
            terms[multiply_terms(
                canonical_var(fi, fc, ui, w),
                canonical_var(fj, fc, uj, w),
            )] += 1

    if disjoint_fibers(fi, fj):
        terms[canonical_var(fi, fj, ui, uj)] += 1
        for same_fi_pos in forced_positions(labels, by_fiber, fi, ui):
            terms[canonical_var(fj, fi, uj, same_fi_pos)] += 1
        for same_fj_pos in forced_positions(labels, by_fiber, fj, uj):
            terms[canonical_var(fi, fj, ui, same_fj_pos)] += 1
    return terms


def same_fiber_free_disjointness_certificate(labels, by_fiber) -> dict:
    failures = []
    checked_pairs = 0
    for fiber, indices in by_fiber.items():
        for i, j in combinations(indices, 2):
            edge = forced_far_edge(labels, i, j)
            ov = overlap(labels, i, j)
            required_far_common = 2 - ov - edge
            forced_same_common = sum(
                1
                for z in indices
                if z not in {i, j}
                and forced_far_edge(labels, i, z) == 1
                and forced_far_edge(labels, j, z) == 1
            )
            checked_pairs += 1
            if required_far_common != forced_same_common:
                failures.append(
                    {
                        "fiber": fiber,
                        "pair": [i, j],
                        "labels": [labels[i], labels[j]],
                        "required_far_common": required_far_common,
                        "forced_same_common": forced_same_common,
                    }
                )
    return {
        "ok": not failures,
        "checkedPairs": checked_pairs,
        "failures": failures,
    }


def run() -> dict:
    labels = make_labels()
    by_fiber = labels_by_fiber(labels)
    fibers = sorted(by_fiber)
    index_pos = fiber_positions(by_fiber)
    mismatches = []
    checked_equations = 0
    rhs_hist = Counter()
    type_hist = Counter()

    for i, j in combinations(range(len(labels)), 2):
        fi, _ = index_pos[i]
        fj, _ = index_pos[j]
        if fi == fj:
            continue
        full_terms = full_far_pair_lhs_terms(labels, by_fiber, index_pos, i, j)
        compact_terms = compact_r204_lhs_terms(labels, by_fiber, fibers, index_pos, i, j)
        checked_equations += 1
        rhs_hist[2 - overlap(labels, i, j)] += 1
        type_hist["disjoint_fibers" if disjoint_fibers(fi, fj) else "intersecting_fibers"] += 1
        if full_terms != compact_terms:
            mismatches.append(
                {
                    "pair": [i, j],
                    "labels": [labels[i], labels[j]],
                    "fibers": [fi, fj],
                    "fullOnly": sorted((repr(k), v) for k, v in (full_terms - compact_terms).items()),
                    "compactOnly": sorted((repr(k), v) for k, v in (compact_terms - full_terms).items()),
                }
            )
            break

    same_fiber = same_fiber_free_disjointness_certificate(labels, by_fiber)
    disjoint_block_count = sum(
        1 for fa, fb in combinations(fibers, 2) if disjoint_fibers(fa, fb)
    )
    vertices_per_fiber = sorted({len(indices) for indices in by_fiber.values()})
    disjoint_fiber_count_per_fiber = sorted(
        {
            sum(1 for fb in fibers if disjoint_fibers(fa, fb))
            for fa in fibers
        }
    )
    forced_degree_inside_fiber = sorted(
        {
            sum(
                1
                for j in by_fiber[fiber]
                if j != i and forced_far_edge(labels, i, j) == 1
            )
            for fiber, indices in by_fiber.items()
            for i in indices
        }
    )
    free_degree_per_vertex = K - 2 - forced_degree_inside_fiber[0]

    return {
        "type": "root_cell_r204_cleanroom_symbolic_audit_v1",
        "ok": not mismatches and same_fiber["ok"],
        "k": K,
        "farVertices": len(labels),
        "fibers": len(fibers),
        "verticesPerFiber": vertices_per_fiber,
        "disjointBlocks": disjoint_block_count,
        "symbolicPairEquationsChecked": checked_equations,
        "symbolicMismatches": mismatches,
        "rhsHistogram": dict(sorted(rhs_hist.items())),
        "pairTypeHistogram": dict(sorted(type_hist.items())),
        "sameFiberFreeDisjointness": same_fiber,
        "permutationBlockCertificate": {
            "forcedDegreeInsideFiber": forced_degree_inside_fiber,
            "freeDegreePerVertex": free_degree_per_vertex,
            "disjointFibersPerFiber": disjoint_fiber_count_per_fiber,
            "candidateVerticesPerFiber": disjoint_fiber_count_per_fiber[0] * vertices_per_fiber[0],
            "coveredByFourDisjointFreeNeighbourSets": 4 * free_degree_per_vertex,
            "conclusion": "each disjoint 4x4 fiber block has every row and every column equal to one",
            "ok": (
                vertices_per_fiber == [4]
                and forced_degree_inside_fiber == [2]
                and free_degree_per_vertex == 10
                and disjoint_fiber_count_per_fiber == [10]
                and same_fiber["ok"]
            ),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Clean-room symbolic audit for R204")
    parser.add_argument("--json-out")
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.json_out:
        path = Path(args.json_out)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text + "\n", encoding="utf-8")
    raise SystemExit(0 if result["ok"] else 1)


if __name__ == "__main__":
    main()
