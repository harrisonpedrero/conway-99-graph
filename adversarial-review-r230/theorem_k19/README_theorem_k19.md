# The k>=18 theorem note

This directory contains a paper-grade theorem note:

- `theorem_k19.tex`
- `README_theorem_k19.md`

## Plain-English statement

Assuming the repository's honest rooted CNF base faithfully encodes the rooted
`srg(99,14,1,2)` equations, no vertex of a Conway 99-graph can have 18 or more
of its 21 rooted fibers inducing the Paley/C4 pattern.

The key mechanism is fiber completion. If 20 fibers at a root are C4, the last
fiber is forced to be C4. The k=19 extension says that if 19 fibers are C4, the
two remaining fibers are also forced to be C4. That makes the root fully
Paley-perfect, which contradicts the existing R230 certificate that no single
Paley-perfect vertex exists.

The k=18 extension splits on the five orbit-types of the three exceptional
fibers. Four orbit-types are per-fiber forced by defect certificates. The
index-triangle orbit is not per-fiber forced by BCP; instead, one joint residual
instance proves the three triangle fibers cannot all be non-C4. Hence 18 C4
fibers force at least 19 C4 fibers, and the k=19 result applies.

## What is machine-certified

- k=20: 6 defect certificates, all `s UNSATISFIABLE` by CaDiCaL and
  `s VERIFIED` by `drat-trim2.exe`.
- k=19: 24 defect certificates, all `s UNSATISFIABLE` by CaDiCaL and
  `s VERIFIED` by `drat-trim2.exe`.
- k=18 Part A: 72 defect certificates for `star_K1_3`, `path_P4`,
  `P3_plus_edge`, and `three_matching`, all `s UNSATISFIABLE` by CaDiCaL and
  `s VERIFIED` by `drat-trim2.exe`.
- k=18 Part B: one triangle residual CNF, base + 72 good-fiber units + three
  six-literal non-C4 clauses, `s UNSATISFIABLE` by CaDiCaL in 16.7 seconds and
  DRAT-verified with a 205MB proof; independently CMS+XOR UNSAT.
- Total local completion instances in `scripts/rebuild_and_verify.py`: 103
  SHA-checked recipes.
- Vacuity controls: removing the good-fiber units gives `UNKNOWN(timeout)` at
  600 seconds for the k=20 control and both k=19 controls, so the good-fiber
  premises carry the content. For the k=18 residual, base + 72 good units
  without the three non-C4 clauses gives `UNKNOWN(timeout)` at 900 seconds, so
  those clauses carry the residual content.
- Symmetry: 21 fibers form one orbit; pairs of exceptional fibers form exactly
  two orbits, disjoint and intersecting; triples of exceptional fibers form
  exactly five orbits.

## What is not claimed

This is not an unconditional proof that `srg(99,14,1,2)` does not exist.
Conway's problem remains open. Vertices with 17 or fewer C4 fibers are not
excluded. The k<=17 range remains open.

The CNF proof checking verifies the emitted CNFs. The mathematical bridge from
a hypothetical graph to those CNFs rests on the honest rooted base equations:
far degree 12, local-far quota equations, and far-far common-neighbor equations.

## Source artifacts

Primary sources used by the note:

- `scratchpad/.work/g2prime_audit_v2.md`
- `scratchpad/.work/makhnev_k20_report.md`
- `scratchpad/ladder/g2prime/final/manifest_certfull.json`
- `scratchpad/ladder/g2prime/final/solve_all_results.txt`
- `scratchpad/ladder/g2prime/final/transitivity_report.json`
- `scratchpad/ladder/g2prime/k19/rep_table_k19.json`
- `scratchpad/ladder/g2prime/k19/cnf/manifest_k19.json`
- `scratchpad/ladder/g2prime/k19/cnf/solve_k19_results.txt`
- `theorem_k19/certificates/k18/rep_table_k18.json`
- `theorem_k19/certificates/k18/manifest_k18A.json`
- `theorem_k19/certificates/k18/solve_k18A_results.txt`
- `theorem_k19/certificates/k18/manifest_k18B.json`
- `theorem_k19/certificates/k18/residual_verdict.txt`
- `reports/FINAL_REPORT_R230_NONEXISTENCE.md`
- `../literature/README.md`

## Re-verification

The available replay scripts re-run CaDiCaL and `drat-trim2.exe` on the
existing CNFs and DRAT proof files:

```bash
bash scratchpad/ladder/g2prime/final/solve_all.sh
bash scratchpad/ladder/g2prime/k19/solve_k19.sh
bash scratchpad/ladder/g2prime/k18/solve_k18A.sh
# residual: replay k18B_residual_triangle.cnf with CaDiCaL + drat-trim;
# see theorem_k19/certificates/k18/residual_verdict.txt
```

Expected summaries:

```text
6 k=20 certs: all s UNSATISFIABLE, all s VERIFIED
24 k=19 certs: PASS=24 FAIL=0
72 k=18 Part-A certs: PASS=72 FAIL=0
k=18 triangle residual: s UNSATISFIABLE, s VERIFIED; CMS+XOR UNSAT
k=20 control: UNKNOWN(timeout)
k=19 controls: UNKNOWN(timeout), UNKNOWN(timeout)
k=18 residual control base+72good-only: UNKNOWN(timeout 900s)
```

For a clean rebuild, regenerate the honest base from
`theorem_k19/scripts/honest_flip_cnf.py:build_base_cnf`, append the good-fiber
units, defect units, and residual clauses recorded in the manifests, then run:

```bash
python theorem_k19/scripts/rebuild_and_verify.py
```

Expected rebuild summary: `MATCH=103 MISMATCH=0 SKIPPED=0` and `PASS`. This
does not run a SAT solver or DRAT checker; it verifies that the committed recipe
rebuilds the exact certified CNF bytes.
