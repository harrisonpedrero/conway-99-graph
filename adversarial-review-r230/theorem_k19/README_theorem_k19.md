# The k>=16 theorem note

This directory contains a paper-grade theorem note:

- `theorem_k19.tex`
- `README_theorem_k19.md`

## Plain-English statement

Assuming the repository's honest rooted CNF base faithfully encodes the rooted
`srg(99,14,1,2)` equations, no vertex of a Conway 99-graph can have 16 or more
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

The k=17 extension splits on the ten orbit-types of the four exceptional fibers
(the C(21,4)=5985 four-edge subgraphs on the seven matched-pair indices). Nine
orbit-types are per-fiber forced: in each, one exceptional fiber has all six of
its defects refuted by the base plus the 68 good-fiber units. The tenth is the
C4-cycle orbit, which is not per-fiber forced by BCP; instead, one joint residual
instance proves the four cycle fibers cannot all be non-C4. Hence 17 C4 fibers
force at least 18 C4 fibers, and the k=18 result applies.

The k=16 extension splits on the 21 orbit-types of the five exceptional fibers
(the C(21,5)=20349 five-edge subgraphs on the seven matched-pair indices).
Nineteen orbit-types are per-fiber forced: in each, one exceptional fiber has all
six of its defects refuted by the base plus the 64 good-fiber units. The other
two are the 2-connected core orbits with no free fiber — C5 (the 5-cycle) and
K4minusE (K4 minus one edge) — which are not per-fiber forced by BCP; instead,
each is a joint residual instance proving its five exceptional fibers cannot all
be non-C4. Hence 16 C4 fibers force at least 17 C4 fibers, and the k=17 result
applies.

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
- k=17 Part A: 54 forcing certificates for the nine forcing quadruple
  orbit-types (9 orbits x 1 forcing fiber x 6 defects), all `s UNSATISFIABLE`
  by CaDiCaL and `s VERIFIED` by `drat-trim`; solve log line
  `k17A certs: PASS=54 FAIL=0`.
- k=17 Part B: one C4-cycle residual CNF, base + 68 good-fiber units + four
  six-literal non-C4 clauses, `s UNSATISFIABLE` by CaDiCaL in 700 seconds with
  a 524MB DRAT proof; `drat-trim` VERIFIED (803 s; 139977 core clauses, 404332
  lemmas, 30.8M resolution steps, 12532 RAT lemmas). Triple-verified: also
  `c VERIFIED` by `cadical --lrat` + `lrat-check`, and `s UNSATISFIABLE` by
  CMS+XOR with forced Gaussian elimination.
- k=16 Part A: 114 forcing certificates for the nineteen forcing quintuple
  orbit-types (19 orbits x 1 forcing fiber x 6 defects), all `s UNSATISFIABLE`
  by CaDiCaL and `s VERIFIED` by `drat-trim`; solve log line
  `k16A certs: PASS=114 FAIL=0`.
- k=16 Part B: two joint residual CNFs, each base + 64 good-fiber units + five
  six-literal non-C4 clauses. The C5 residual is `s UNSATISFIABLE` by CaDiCaL in
  28 seconds with a 256MB DRAT proof; `drat-trim` VERIFIED (123 s; 46790 core
  clauses, 3036 RAT lemmas). The K4minusE residual is `s UNSATISFIABLE` by
  CaDiCaL in 27 seconds with a 280MB DRAT proof; `drat-trim` VERIFIED (59 s;
  29778 core clauses, 1129 RAT lemmas). Both independently re-confirmed by
  `s UNSATISFIABLE` under CMS+XOR with forced Gaussian elimination.
- Total local completion instances in `scripts/rebuild_and_verify.py`: 274
  SHA-checked recipes.
- Vacuity controls: removing the good-fiber units gives `UNKNOWN(timeout)` at
  600 seconds for the k=20 control and both k=19 controls, so the good-fiber
  premises carry the content. For the k=18 residual, base + 72 good units
  without the three non-C4 clauses gives `UNKNOWN(timeout)` at 900 seconds, so
  those clauses carry the residual content. For the k=17 residual, base + 68
  good units without the four non-C4 clauses gives `UNKNOWN(timeout)` at 900
  seconds (1.38M conflicts, never UNSAT), so those clauses carry the residual
  content. For the two k=16 residuals, base + 64 good units without the five
  non-C4 clauses gives `UNKNOWN(timeout)` at 900 seconds (the C5 control with
  1.40M conflicts, the K4minusE control with 1.12M conflicts, never UNSAT), so
  those clauses carry the residual content.
- Symmetry: 21 fibers form one orbit; pairs of exceptional fibers form exactly
  two orbits, disjoint and intersecting; triples of exceptional fibers form
  exactly five orbits; quadruples of exceptional fibers form exactly ten orbits
  (sizes summing to C(21,4)=5985); quintuples of exceptional fibers form exactly
  21 orbits (sizes summing to C(21,5)=20349).

## What is not claimed

This is not an unconditional proof that `srg(99,14,1,2)` does not exist.
Conway's problem remains open. Vertices with 15 or fewer C4 fibers are not
excluded. The k<=15 range remains open.

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
- `theorem_k19/certificates/k17/rep_table_k17.json`
- `theorem_k19/certificates/k17/manifest_k17A.json`
- `theorem_k19/certificates/k17/solve_k17A_results.txt`
- `theorem_k19/certificates/k17/manifest_k17B.json`
- `theorem_k19/certificates/k17/residual_verdict.txt`
- `theorem_k19/certificates/k16/rep_table_k16.json`
- `theorem_k19/certificates/k16/manifest_k16A.json`
- `theorem_k19/certificates/k16/solve_k16A_results.txt`
- `theorem_k19/certificates/k16/manifest_k16B.json`
- `theorem_k19/certificates/k16/residual_verdict.txt`
- `reports/FINAL_REPORT_R230_NONEXISTENCE.md`
- `../literature/README.md`

## Re-verification

The available replay scripts re-run CaDiCaL and `drat-trim2.exe` on the
existing CNFs and DRAT proof files:

```bash
bash scratchpad/ladder/g2prime/final/solve_all.sh
bash scratchpad/ladder/g2prime/k19/solve_k19.sh
bash scratchpad/ladder/g2prime/k18/solve_k18A.sh
# k=18 residual: replay k18B_residual_triangle.cnf with CaDiCaL + drat-trim;
# see theorem_k19/certificates/k18/residual_verdict.txt
# k=17 and k=16 rungs have no bundled shell script: their certificate CNFs are
# rebuilt byte-identically by scripts/rebuild_and_verify.py (all 274 instances),
# and re-verified by running CaDiCaL --no-binary + drat-trim2 on any rebuilt CNF.
# Recorded per-cert / per-residual verdicts (s UNSATISFIABLE / s VERIFIED):
#   certificates/k17/solve_k17A_results.txt   (k17A certs: PASS=54 FAIL=0)
#   certificates/k17/residual_verdict.txt     (C4-cycle residual)
#   certificates/k16/solve_k16A_results.txt   (k16A certs: PASS=114 FAIL=0)
#   certificates/k16/residual_verdict.txt     (C5 and K4minusE residuals)
```

Expected summaries:

```text
6 k=20 certs: all s UNSATISFIABLE, all s VERIFIED
24 k=19 certs: PASS=24 FAIL=0
72 k=18 Part-A certs: PASS=72 FAIL=0
k=18 triangle residual: s UNSATISFIABLE, s VERIFIED; CMS+XOR UNSAT
54 k=17 Part-A certs: PASS=54 FAIL=0
k=17 C4-cycle residual: s UNSATISFIABLE, s VERIFIED; lrat-check VERIFIED; CMS+XOR-Gauss UNSAT
114 k=16 Part-A certs: PASS=114 FAIL=0
k=16 C5 residual: s UNSATISFIABLE, s VERIFIED; CMS+XOR-Gauss UNSAT
k=16 K4minusE residual: s UNSATISFIABLE, s VERIFIED; CMS+XOR-Gauss UNSAT
k=20 control: UNKNOWN(timeout)
k=19 controls: UNKNOWN(timeout), UNKNOWN(timeout)
k=18 residual control base+72good-only: UNKNOWN(timeout 900s)
k=17 residual control base+68good-only: UNKNOWN(timeout 900s)
k=16 residual controls base+64good-only: UNKNOWN(timeout 900s), UNKNOWN(timeout 900s)
```

For a clean rebuild, regenerate the honest base from
`theorem_k19/scripts/honest_flip_cnf.py:build_base_cnf`, append the good-fiber
units, defect units, and residual clauses recorded in the manifests, then run:

```bash
python theorem_k19/scripts/rebuild_and_verify.py
```

Expected rebuild summary: `MATCH=274 MISMATCH=0 SKIPPED=0` and `PASS`. This
does not run a SAT solver or DRAT checker; it verifies that the committed recipe
rebuilds the exact certified CNF bytes.
