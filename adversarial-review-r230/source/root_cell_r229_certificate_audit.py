"""Audit the R229/R230 proof-certificate bundle.

This is not a SAT solver or proof checker.  It verifies that the recorded
independent proof-check run is internally consistent: every representative has
UNSAT + VERIFIED logs, every CNF/DRAT hash matches the summary, and the
reduction-chain audit JSON files are green.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


DEFAULT_SUMMARY = Path("artifacts/audit_json/r229_all24_ascii_drat_checked_summary.json")

DEFAULT_AUDITS = [
    Path("artifacts/audit_json/root_cell_r204_cleanroom_symbolic_audit.json"),
    Path("artifacts/audit_json/root_cell_permutation_formula_audit_r229.json"),
    Path("artifacts/audit_json/root_cell_triangle_orbit_audit_r229.json"),
    Path("artifacts/audit_json/root_cell_triangle_rep_unit_audit_r229.json"),
    Path("artifacts/audit_json/root_cell_block_rep_audit_r229.json"),
    Path("artifacts/audit_json/root_cell_intersecting_coset_sat_audit_r229b.json"),
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_json(path: Path):
    with path.open("r", encoding="utf-8-sig") as f:
        return json.load(f)


def has_marker(path: Path, marker: str) -> bool:
    data = path.read_bytes()
    return marker.encode("ascii") in data or marker.encode("utf-16le") in data


def audit(args: argparse.Namespace) -> dict:
    failures: list[str] = []
    summary_path = Path(args.summary)
    if not summary_path.exists():
        return {
            "ok": False,
            "failures": [f"missing summary: {summary_path}"],
            "summary": str(summary_path),
        }

    summary = read_json(summary_path)
    results = summary.get("results", [])

    if summary.get("ok") is not True:
        failures.append("summary ok is not true")
    if summary.get("reps") != 24 or len(results) != 24:
        failures.append(f"expected 24 reps, got summary reps={summary.get('reps')} len={len(results)}")
    if summary.get("verifiedCount") != 24:
        failures.append(f"verifiedCount={summary.get('verifiedCount')} != 24")
    if summary.get("unsatCount") != 24:
        failures.append(f"unsatCount={summary.get('unsatCount')} != 24")

    rep_ids = sorted(result.get("rep") for result in results)
    if rep_ids != list(range(24)):
        failures.append(f"rep ids are not 0..23: {rep_ids}")

    checked_reps = []
    for result in sorted(results, key=lambda item: item.get("rep", -1)):
        rep = result.get("rep")
        rep_failures = []
        if result.get("unsat") is not True:
            rep_failures.append("unsat is not true")
        if result.get("verified") is not True:
            rep_failures.append("verified is not true")

        cnf = Path(result.get("cnf", ""))
        drat = Path(result.get("drat", ""))
        solve_log = Path(result.get("solveLog", ""))
        check_log = Path(result.get("checkLog", ""))
        for label, path in [("cnf", cnf), ("drat", drat), ("solveLog", solve_log), ("checkLog", check_log)]:
            if not path.exists():
                rep_failures.append(f"missing {label}: {path}")

        if cnf.exists() and not args.skip_hash:
            actual = sha256_file(cnf)
            if actual != result.get("cnfSha256"):
                rep_failures.append(f"cnf sha256 mismatch: {actual} != {result.get('cnfSha256')}")
        if drat.exists() and not args.skip_hash:
            actual = sha256_file(drat)
            if actual != result.get("dratSha256"):
                rep_failures.append(f"drat sha256 mismatch: {actual} != {result.get('dratSha256')}")

        if solve_log.exists():
            if not has_marker(solve_log, "s UNSATISFIABLE"):
                rep_failures.append("solve log lacks 's UNSATISFIABLE'")
        if check_log.exists():
            if not has_marker(check_log, "s VERIFIED"):
                rep_failures.append("check log lacks 's VERIFIED'")

        checked_reps.append(
            {
                "rep": rep,
                "ok": not rep_failures,
                "cnf": str(cnf),
                "drat": str(drat),
                "failures": rep_failures,
            }
        )
        failures.extend(f"rep {rep}: {failure}" for failure in rep_failures)

    audit_records = []
    for audit_path in [Path(path) for path in args.audit_json]:
        record = {"path": str(audit_path), "ok": False}
        if not audit_path.exists():
            record["failure"] = "missing"
            failures.append(f"missing audit json: {audit_path}")
        else:
            data = read_json(audit_path)
            record["ok"] = data.get("ok") is True
            if data.get("ok") is not True:
                record["failure"] = f"ok={data.get('ok')!r}"
                failures.append(f"audit not ok: {audit_path}")
        audit_records.append(record)

    return {
        "type": "root_cell_r229_certificate_audit_v1",
        "ok": not failures,
        "summary": str(summary_path),
        "solver": summary.get("solver"),
        "checker": summary.get("checker"),
        "skip_hash": bool(args.skip_hash),
        "reps": len(results),
        "verifiedCount": summary.get("verifiedCount"),
        "unsatCount": summary.get("unsatCount"),
        "auditRecords": audit_records,
        "checkedReps": checked_reps,
        "failures": failures,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary", default=str(DEFAULT_SUMMARY))
    parser.add_argument("--audit-json", action="append", default=[str(path) for path in DEFAULT_AUDITS])
    parser.add_argument("--skip-hash", action="store_true")
    parser.add_argument("--json-out")
    args = parser.parse_args()

    result = audit(args)
    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.json_out:
        Path(args.json_out).write_text(text + "\n", encoding="utf-8")
    raise SystemExit(0 if result["ok"] else 1)


if __name__ == "__main__":
    main()
