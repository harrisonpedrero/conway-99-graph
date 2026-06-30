"""
Audit the SAT encoding of the R227 intersecting-fiber D8-coset shadow.

The SAT file duplicates a few CP-SAT helper functions to avoid a circular import.
This audit proves the duplicate is identical to the CP-SAT source relation and
checks the relative-permutation orientation used by the Tseitin definitions.
"""
import argparse
import json
from itertools import combinations
from pathlib import Path

from root_cell_cpsat import labels_by_fiber, make_labels, overlap
from root_cell_permutation_csp import intersecting_coset_projection_rows as csp_coset_rows
from root_cell_permutation_sat import (
    PERMS,
    PERM_ID,
    PermutationSat,
    compose_perm,
    disjoint,
    intersecting_coset_projection_rows as sat_coset_rows,
    intersecting_residual_rows,
    invert_perm,
    perm_ids_by_right_coset,
    right_coset_id_by_perm,
)


def target_matrix(labels, by_fiber, fa, fb):
    return tuple(
        tuple(2 - overlap(labels, idx_a, idx_b) for idx_b in by_fiber[fb])
        for idx_a in by_fiber[fa]
    )


def audit_relative_orientation():
    failures = []
    for left in PERMS:
        for right in PERMS:
            expected = compose_perm(invert_perm(right), left)
            for q in PERMS:
                matches = all(left[u] == right[q[u]] for u in range(4))
                if matches != (q == expected):
                    failures.append(
                        {
                            "left": left,
                            "right": right,
                            "q": q,
                            "expected": expected,
                            "matches": matches,
                        }
                    )
                    if len(failures) >= 5:
                        return failures
    return failures


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json-out")
    ap.add_argument("--build-formula", action="store_true")
    args = ap.parse_args()

    labels = make_labels(14)
    by_fiber = {fiber: sorted(indices) for fiber, indices in labels_by_fiber(labels).items()}
    fibers = sorted(by_fiber)

    coset_id = right_coset_id_by_perm()
    buckets = perm_ids_by_right_coset()
    bucket_sizes = [len(bucket) for bucket in buckets]
    coset_partition_ok = (
        sorted(coset_id.values()) == [0] * 8 + [1] * 8 + [2] * 8
        and bucket_sizes == [8, 8, 8]
    )

    orientation_failures = audit_relative_orientation()
    pair_reports = []
    unique_targets = {}
    for fa, fb in combinations(fibers, 2):
        if disjoint(fa, fb):
            continue
        common_fibers = [fc for fc in fibers if disjoint(fc, fa) and disjoint(fc, fb)]
        target = target_matrix(labels, by_fiber, fa, fb)
        full_rows = intersecting_residual_rows(target)
        sat_rows = sat_coset_rows(target)
        csp_rows = csp_coset_rows(target)
        projected = sorted(
            {
                tuple(coset_id[PERMS[perm_id]] for perm_id in row)
                for row in full_rows
            }
        )
        ok = sat_rows == csp_rows == projected
        pair_reports.append(
            {
                "fa": fa,
                "fb": fb,
                "common_fibers": common_fibers,
                "full_rows": len(full_rows),
                "allowed_coset_rows": len(sat_rows),
                "forbidden_coset_rows": 3**6 - len(sat_rows),
                "sat_matches_csp_and_projection": ok,
            }
        )
        unique_targets.setdefault(target, pair_reports[-1])

    formula_stats = None
    if args.build_formula:
        enc = PermutationSat(card_encoding="direct", triangle_rep_index=0, intersecting_coset_cuts=True).build()
        formula_stats = enc.stats

    failures = [report for report in pair_reports if not report["sat_matches_csp_and_projection"]]
    result = {
        "type": "root_cell_intersecting_coset_sat_audit_v1",
        "ok": not failures and not orientation_failures and coset_partition_ok,
        "coset_partition_ok": coset_partition_ok,
        "coset_bucket_sizes": bucket_sizes,
        "relative_orientation_failures": orientation_failures,
        "intersecting_pairs": len(pair_reports),
        "unique_target_count": len(unique_targets),
        "full_rows_range": [min(r["full_rows"] for r in pair_reports), max(r["full_rows"] for r in pair_reports)],
        "allowed_coset_rows_range": [
            min(r["allowed_coset_rows"] for r in pair_reports),
            max(r["allowed_coset_rows"] for r in pair_reports),
        ],
        "forbidden_coset_rows_range": [
            min(r["forbidden_coset_rows"] for r in pair_reports),
            max(r["forbidden_coset_rows"] for r in pair_reports),
        ],
        "failures": failures[:5],
        "formula_stats": formula_stats,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if args.json_out:
        path = Path(args.json_out)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if not result["ok"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
