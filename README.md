# Conway 99-Graph R230 Review Bundle

This repository contains a consolidated adversarial-review bundle for the R230
computational certificate about `srg(99,14,1,2)` (Conway's 99-graph problem).

## The claim (corrected 2026-07-01)

**Theorem.** No `srg(99,14,1,2)` contains a *Paley-perfect* vertex — a vertex
all 21 of whose rooted far-cell fibers induce a C4 (equivalently, at which the
R204 forced-edge table holds).

This strengthens Makhnev (1988, Theorem 2) and Keramatipour (2023, Theorem
3.4.2), who refuted the corresponding *every-vertex* hypothesis, and is
machine-certified: 24 case CNFs, each with an independently verified DRAT
unsatisfiability proof.

**This repository does NOT claim unconditional nonexistence of the 99-graph.**
An earlier revision did; an adversarial review found the forced-edge table was
an unproven assumption, and a literature search showed its global version was
refuted in 1988 and that the conjectured truth (Keramatipour, Conj. 3.4.4) is
the opposite direction. Conway's problem remains open. See
`adversarial-review-r230/reports/FINAL_REPORT_R230_NONEXISTENCE.md` for the
full corrected statement and
`adversarial-review-r230/scratchpad/ADVERSARIAL_REVIEW_FINDINGS.md` for the
review that forced the correction.

Start here:

- `adversarial-review-r230/README.md` for the review checklist.
- `adversarial-review-r230/latex/conway_99_r230_nonexistence.tex` for the
  LaTeX writeup of the corrected theorem.
- `adversarial-review-r230/reports/FINAL_REPORT_R230_NONEXISTENCE.md` for the
  concise result report.
- `literature/` for cached primary sources (Makhnev 1988, Keramatipour thesis,
  Cesarz–Woldar, Lou–Murin, Reimbayev).
- `CLEAN_MACHINE_PLAN.md` for the independent clean-machine replay plan.

Large CNF/DRAT proof bodies are included via Git LFS under
`adversarial-review-r230/scratchpad/root_cell_triangle_rep_cloud_r229_seq_intercoset/`.
Several DRAT proofs exceed GitHub's normal 100 MB file limit, so a plain Git
checkout without LFS will only contain pointer files for those bodies.
