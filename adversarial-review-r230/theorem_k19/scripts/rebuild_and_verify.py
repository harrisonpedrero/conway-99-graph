"""Reproduce and SHA-verify the k>=19 certificate CNFs from the tracked recipe.

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


def cnf_sha(cnf) -> str:
    buf = io.StringIO()
    buf.write(f"p cnf {cnf.nv} {len(cnf.clauses)}\n")
    for cl in cnf.clauses:
        buf.write(" ".join(str(x) for x in cl) + " 0\n")
    return hashlib.sha256(buf.getvalue().encode("ascii")).hexdigest()


def build_with_units(base_template, units):
    from pysat.formula import CNF
    cnf = CNF()
    cnf.extend(base_template.clauses)
    cnf.nv = base_template.nv
    for lit in units:
        cnf.append([lit])
    return cnf


def edge_var(edge_vars, labels, a, b):
    i, j = labels.index(tuple(a)), labels.index(tuple(b))
    return edge_vars[(min(i, j), max(i, j))]


def main():
    base, labels, edge_vars, _ = build_base_cnf()
    certs = []  # (name, units, expected_sha)

    # --- k=20: manifest_certfull ---
    cf = json.load(open(os.path.join(CERT_DIR, "manifest_certfull.json")))
    good20 = [u["literal"] for u in cf["common_good_fiber_units"]]
    for name, rec in cf["certificates"].items():
        certs.append((f"k20/{name}", good20 + [rec["defect_unit"]["literal"]],
                      rec.get("sha256")))

    # --- k=19: rep_table (good units as labels) + manifest_k19 (defects) ---
    table = json.load(open(os.path.join(CERT_DIR, "rep_table_k19.json")))
    good19 = {}
    for orb in table["orbits"]:
        lits = [edge_var(edge_vars, labels, e[0], e[1])
                for e in orb["good_fiber_units"]]
        good19[orb["orbit_type"]] = lits
    k19 = json.load(open(os.path.join(CERT_DIR, "manifest_k19.json")))
    for rec in k19["certs"]:
        units = good19[rec["orbit"]] + [rec["defect_literal"]]
        certs.append((rec["filename"], units, rec.get("sha256")))

    print(f"rebuilding {len(certs)} certificate CNFs; checking SHA-256")
    ok = bad = skip = 0
    for name, units, expected in certs:
        if not expected:
            skip += 1
            continue
        actual = cnf_sha(build_with_units(base, units))
        if actual == expected:
            ok += 1
        else:
            bad += 1
            print(f"  MISMATCH {name}: {actual[:16]} != {expected[:16]}")
    print(f"MATCH={ok} MISMATCH={bad} SKIPPED={skip}")
    print("PASS" if bad == 0 and ok >= 30 else "FAIL")
    raise SystemExit(0 if bad == 0 and ok >= 30 else 1)


if __name__ == "__main__":
    main()
