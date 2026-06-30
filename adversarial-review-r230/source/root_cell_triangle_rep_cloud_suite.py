"""
root_cell_triangle_rep_cloud_suite.py -- one-command R220 SAT suite export.

This script rebuilds the 24 matching-triangle representative CNFs, runs the
independent unit-propagation audit, and exports DIMACS only for the surviving
representatives.  The killed representatives need no SAT proof run: they are
already contradicted by level-0 propagation in the encoded clauses.
"""
import argparse
import json
import time
from pathlib import Path

from root_cell_permutation_sat import (
    PermutationSat,
    TRIANGLE_REP_IDS,
    file_sha256,
    solve,
)
from root_cell_triangle_rep_unit_audit import unit_propagate


def write_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description="Export the R220 triangle-representative SAT suite")
    ap.add_argument("--out-dir", default="scratchpad/root_cell_triangle_rep_cloud_r220")
    ap.add_argument("--card-encoding", choices=["direct", "seqcounter"], default="direct")
    ap.add_argument("--solver", default="cadical195")
    ap.add_argument(
        "--matching-triangle-cuts",
        action="store_true",
        help="export survivor CNFs with the R222 full matching-triangle forbidden-triple clauses",
    )
    ap.add_argument(
        "--intersecting-coset-cuts",
        action="store_true",
        help="export survivor CNFs with the R229 intersecting-fiber D8-coset shadow clauses",
    )
    ap.add_argument("--smoke-solve", action="store_true", help="run a bounded local SAT smoke on survivor CNFs")
    ap.add_argument("--time-cap", type=float, default=5.0, help="local smoke cap per survivor")
    ap.add_argument("--no-export", action="store_true", help="audit only; do not write DIMACS files")
    args = ap.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    start = time.time()

    records = []
    for idx, rep in enumerate(TRIANGLE_REP_IDS):
        build_start = time.time()
        enc = PermutationSat(
            card_encoding=args.card_encoding,
            triangle_rep_index=idx,
            matching_triangle_cuts=args.matching_triangle_cuts,
            intersecting_coset_cuts=args.intersecting_coset_cuts,
        ).build()
        bcp = unit_propagate(enc.cnf)
        record = {
            "index": idx,
            "rep": list(rep),
            "unit_conflict": bcp["conflict"],
            "assigned": bcp["assigned"],
            "propagation_steps": bcp["propagation_steps"],
            "conflict_clause_index": bcp.get("conflict_clause_index"),
            "conflict_clause": bcp.get("conflict_clause"),
            "encoding_stats": enc.stats,
            "build_seconds": round(time.time() - build_start, 4),
        }

        if not bcp["conflict"] and not args.no_export:
            cut_tag = "_trianglecuts" if args.matching_triangle_cuts else ""
            coset_tag = "_intercoset" if args.intersecting_coset_cuts else ""
            cnf_path = out_dir / f"root_cell_triangle_rep_{idx:02d}_{args.card_encoding}{cut_tag}{coset_tag}.cnf"
            enc.cnf.to_file(str(cnf_path))
            record["cnf"] = {
                "path": str(cnf_path),
                "sha256": file_sha256(cnf_path),
                "bytes": cnf_path.stat().st_size,
            }

        if not bcp["conflict"] and args.smoke_solve:
            sat, model, stats, solve_s = solve(enc.cnf, args.solver, args.time_cap)
            del model
            record["smoke"] = {
                "status": "SAT" if sat is True else "UNSAT" if sat is False else "UNKNOWN",
                "sat": sat is True,
                "unsat": sat is False,
                "solve_seconds": round(solve_s, 4),
                "solver": args.solver,
                "solver_stats": stats,
            }

        records.append(record)

    killed = [r["index"] for r in records if r["unit_conflict"]]
    survivors = [r["index"] for r in records if not r["unit_conflict"]]
    manifest = {
        "type": "root_cell_triangle_rep_cloud_suite_v1",
        "ok": True,
        "card_encoding": args.card_encoding,
        "matching_triangle_cuts": args.matching_triangle_cuts,
        "intersecting_coset_cuts": args.intersecting_coset_cuts,
        "exported_cnfs": not args.no_export,
        "representatives": len(records),
        "unit_conflict_count": len(killed),
        "unit_conflict_indices": killed,
        "survivor_count": len(survivors),
        "survivor_indices": survivors,
        "out_dir": str(out_dir),
        "elapsed_seconds": round(time.time() - start, 4),
        "records": records,
    }
    manifest_path = out_dir / "manifest.json"
    write_json(manifest_path, manifest)

    print(json.dumps({k: manifest[k] for k in (
        "ok",
        "representatives",
        "unit_conflict_count",
        "unit_conflict_indices",
        "survivor_count",
        "survivor_indices",
        "matching_triangle_cuts",
        "intersecting_coset_cuts",
        "exported_cnfs",
        "out_dir",
        "elapsed_seconds",
    )}, indent=2, sort_keys=True))
    print(f"WROTE {manifest_path}")


if __name__ == "__main__":
    main()
