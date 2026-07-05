"""Reproduce and SHA-verify the k>=18 certificate CNFs from the tracked recipe.

Regenerates every certificate CNF from the honest rooted base builder plus the
unit lists recorded in the manifests / representative table, and checks each
rebuilt CNF's SHA-256 against the manifest.  This closes the reproducibility
chain: (committed base builder) + (committed unit recipe) => the exact CNFs
whose DRAT proofs were independently drat-trim-verified (evidence in the
solve_*_results.txt files).

It does NOT run a SAT solver or DRAT checker -- see README_theorem_k19.md for
that step (needs CaDiCaL + drat-trim binaries).  It proves only that the
committed recipe rebuilds the exact certified CNF bytes.

Usage:   python rebuild_and_verify.py
Requires pysat; honest_flip_cnf.py (same dir) which imports root_cell_cpsat
from ../../source.
"""
import hashlib
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BUNDLE = os.path.normpath(os.path.join(HERE, "..", ".."))  # adversarial-review-r230
sys.path.insert(0, HERE)      # for honest_flip_cnf
sys.path.insert(0, BUNDLE)    # so `import source.root_cell_cpsat` resolves

from honest_flip_cnf import build_base_cnf  # noqa: E402

CERT_DIR = os.path.normpath(os.path.join(HERE, "..", "certificates"))


def clause_line(clause) -> bytes:
    return (" ".join(str(x) for x in clause) + " 0\n").encode("ascii")


def clause_body(clauses) -> bytes:
    buf = io.BytesIO()
    for clause in clauses:
        buf.write(clause_line(clause))
    return buf.getvalue()


def cnf_sha(base_body: bytes, nv: int, base_clause_count: int, extra_clauses) -> str:
    h = hashlib.sha256()
    h.update(f"p cnf {nv} {base_clause_count + len(extra_clauses)}\n".encode("ascii"))
    h.update(base_body)
    for clause in extra_clauses:
        h.update(clause_line(clause))
    return h.hexdigest()


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def unit_clauses(units):
    return [[lit] for lit in units]


def edge_var(edge_vars, labels, a, b):
    i, j = labels.index(tuple(a)), labels.index(tuple(b))
    return edge_vars[(min(i, j), max(i, j))]


def edge_lits(edge_vars, labels, edge_specs):
    return [edge_var(edge_vars, labels, edge[0], edge[1]) for edge in edge_specs]


def residual_non_c4_clauses(manifest):
    if "nonC4_clauses" in manifest:
        return [list(rec["clause"]) for rec in manifest["nonC4_clauses"]]
    return [list(clause) for clause in manifest["dimacs_nonC4_clauses_in_base_vars"]]


def collect_cert_recipes(labels, edge_vars):
    certs = []  # (name, extra_clauses, expected_sha)

    # --- k=20: manifest_certfull ---
    cf = load_json(os.path.join(CERT_DIR, "manifest_certfull.json"))
    good20 = [u["literal"] for u in cf["common_good_fiber_units"]]
    for name, rec in cf["certificates"].items():
        certs.append((f"k20/{name}",
                      unit_clauses(good20 + [rec["defect_unit"]["literal"]]),
                      rec.get("sha256")))

    # --- k=19: rep_table (good units as labels) + manifest_k19 (defects) ---
    table = load_json(os.path.join(CERT_DIR, "rep_table_k19.json"))
    good19 = {}
    for orb in table["orbits"]:
        lits = edge_lits(edge_vars, labels, orb["good_fiber_units"])
        good19[orb["orbit_type"]] = lits
    k19 = load_json(os.path.join(CERT_DIR, "manifest_k19.json"))
    for rec in k19["certs"]:
        units = unit_clauses(good19[rec["orbit"]] + [rec["defect_literal"]])
        certs.append((rec["filename"], units, rec.get("sha256")))

    # --- k=18 Part A: four forced triple orbits ---
    k18_dir = os.path.join(CERT_DIR, "k18")
    table18 = load_json(os.path.join(k18_dir, "rep_table_k18.json"))
    good18 = {}
    for orb in table18["part_A_forcing_orbits"]:
        lits = edge_lits(edge_vars, labels, orb["good_fiber_units"])
        if len(lits) != 72:
            raise ValueError(f"k18 orbit {orb['orbit_type']} has {len(lits)} good units")
        good18[orb["orbit_type"]] = lits
    k18a = load_json(os.path.join(k18_dir, "manifest_k18A.json"))
    for rec in k18a["certs"]:
        units = unit_clauses(good18[rec["orbit"]] + [rec["defect"]["literal"]])
        certs.append((rec["file"], units, rec.get("sha256")))

    # --- k=18 Part B: triangle residual, three non-C4 clauses ---
    part_b = table18["part_B_residual_orbit"]
    good18b = edge_lits(edge_vars, labels, part_b["good_fiber_units"])
    if len(good18b) != 72:
        raise ValueError(f"k18 residual has {len(good18b)} good units")
    k18b = load_json(os.path.join(k18_dir, "manifest_k18B.json"))
    residual_clauses = unit_clauses(good18b) + residual_non_c4_clauses(k18b)
    certs.append((k18b["file"], residual_clauses, k18b.get("sha256")))

    return certs


def main():
    base, labels, edge_vars, _ = build_base_cnf()
    base_body = clause_body(base.clauses)
    certs = collect_cert_recipes(labels, edge_vars)
    if len(certs) != 103:
        raise RuntimeError(f"expected 103 certificate recipes, got {len(certs)}")

    print(f"rebuilding {len(certs)} certificate CNFs; checking SHA-256")
    ok = bad = skip = 0
    for name, extra_clauses, expected in certs:
        if not expected:
            skip += 1
            continue
        actual = cnf_sha(base_body, base.nv, len(base.clauses), extra_clauses)
        if actual == expected:
            ok += 1
        else:
            bad += 1
            print(f"  MISMATCH {name}: {actual[:16]} != {expected[:16]}")
    print(f"MATCH={ok} MISMATCH={bad} SKIPPED={skip}")
    passed = bad == 0 and skip == 0 and ok >= 103
    print("PASS" if passed else "FAIL")
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
