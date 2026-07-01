"""Lightweight consistency check for the pushed R230 review bundle.

This intentionally does not replace DRAT verification.  It checks the compact
artifacts that are safe to keep in normal Git history.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT_DIR = ROOT / "artifacts" / "audit_json"
LOG_DIR = ROOT / "artifacts" / "proof_logs"


def read_json(path: Path):
    with path.open("r", encoding="utf-8-sig") as f:
        return json.load(f)


def has_marker(path: Path, marker: str) -> bool:
    data = path.read_bytes()
    return marker.encode("ascii") in data or marker.encode("utf-16le") in data


def main() -> int:
    failures: list[str] = []
    summary = read_json(AUDIT_DIR / "r229_all24_ascii_drat_checked_summary.json")
    if summary.get("ok") is not True:
        failures.append("summary ok is not true")
    if summary.get("reps") != 24 or len(summary.get("results", [])) != 24:
        failures.append("summary does not contain 24 representatives")
    if summary.get("unsatCount") != 24:
        failures.append(f"unsatCount is {summary.get('unsatCount')}, expected 24")
    if summary.get("verifiedCount") != 24:
        failures.append(f"verifiedCount is {summary.get('verifiedCount')}, expected 24")

    audit_names = [
        "root_cell_r204_cleanroom_symbolic_audit.json",
        "root_cell_permutation_formula_audit_r229.json",
        "root_cell_triangle_orbit_audit_r229.json",
        "root_cell_triangle_rep_unit_audit_r229.json",
        "root_cell_block_rep_audit_r229.json",
        "root_cell_intersecting_coset_sat_audit_r229b.json",
    ]
    for name in audit_names:
        path = AUDIT_DIR / name
        if not path.exists():
            failures.append(f"missing audit JSON: {name}")
        elif read_json(path).get("ok") is not True:
            failures.append(f"audit JSON not ok: {name}")

    reps = sorted(result.get("rep") for result in summary.get("results", []))
    if reps != list(range(24)):
        failures.append(f"representative ids are not 0..23: {reps}")

    for rep in range(24):
        solve_log = LOG_DIR / f"root_cell_triangle_rep_{rep:02d}_cadical_ascii_proof.log"
        check_log = LOG_DIR / f"root_cell_triangle_rep_{rep:02d}_drat_trim_ascii.log"
        if not solve_log.exists():
            failures.append(f"missing solve log for rep {rep}")
        elif not has_marker(solve_log, "s UNSATISFIABLE"):
            failures.append(f"solve log lacks UNSAT marker for rep {rep}")
        if not check_log.exists():
            failures.append(f"missing checker log for rep {rep}")
        elif not has_marker(check_log, "s VERIFIED"):
            failures.append(f"checker log lacks VERIFIED marker for rep {rep}")

    result = {
        "ok": not failures,
        "reps": len(summary.get("results", [])),
        "unsatCount": summary.get("unsatCount"),
        "verifiedCount": summary.get("verifiedCount"),
        "failures": failures,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
