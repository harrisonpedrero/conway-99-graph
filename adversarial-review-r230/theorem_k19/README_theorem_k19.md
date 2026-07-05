# The k>=19 theorem note

This directory contains a paper-grade theorem note:

- `theorem_k19.tex`
- `README_theorem_k19.md`

## Plain-English statement

Assuming the repository's honest rooted CNF base faithfully encodes the rooted
`srg(99,14,1,2)` equations, no vertex of a Conway 99-graph can have 19 or more
of its 21 rooted fibers inducing the Paley/C4 pattern.

The key mechanism is fiber completion. If 20 fibers at a root are C4, the last
fiber is forced to be C4. The k=19 extension says that if 19 fibers are C4, the
two remaining fibers are also forced to be C4. That makes the root fully
Paley-perfect, which contradicts the existing R230 certificate that no single
Paley-perfect vertex exists.

## What is machine-certified

- k=20: 6 defect certificates, all `s UNSATISFIABLE` by CaDiCaL and
  `s VERIFIED` by `drat-trim2.exe`.
- k=19: 24 defect certificates, all `s UNSATISFIABLE` by CaDiCaL and
  `s VERIFIED` by `drat-trim2.exe`.
- Vacuity controls: removing the good-fiber units gives `UNKNOWN(timeout)` at
  600 seconds for the k=20 control and both k=19 controls, so the good-fiber
  premises carry the content.
- Symmetry: 21 fibers form one orbit; pairs of exceptional fibers form exactly
  two orbits, disjoint and intersecting.

## What is not claimed

This is not an unconditional proof that `srg(99,14,1,2)` does not exist.
Conway's problem remains open. Vertices with 18 or fewer C4 fibers are not
excluded. The current k=18 descent note leaves the triangle exceptional-fiber
orbit open: 35 of 1330 triples remain as the residual case.

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
- `reports/FINAL_REPORT_R230_NONEXISTENCE.md`
- `../literature/README.md`
- `scratchpad/.work/descent_k19.md` for the k=18 limitation

## Re-verification

The available replay scripts re-run CaDiCaL and `drat-trim2.exe` on the
existing CNFs and DRAT proof files:

```bash
bash scratchpad/ladder/g2prime/final/solve_all.sh
bash scratchpad/ladder/g2prime/k19/solve_k19.sh
```

Expected summaries:

```text
6 k=20 certs: all s UNSATISFIABLE, all s VERIFIED
24 k=19 certs: PASS=24 FAIL=0
k=20 control: UNKNOWN(timeout)
k=19 controls: UNKNOWN(timeout), UNKNOWN(timeout)
```

For a clean rebuild, regenerate the honest base from
`scratchpad/honest_flip_cnf.py:build_base_cnf`, append the good-fiber and
defect units recorded in the two manifests, then compare SHA-256 values against
the tables in `theorem_k19.tex` before replaying CaDiCaL and `drat-trim2.exe`.
The manifests record the base builder, label source, unit counts, and certificate
hashes needed for that comparison.
