# Conway 99-Graph — Certificate Work

This repository collects machine-checkable partial results on **Conway's
99-graph problem**: does a strongly regular graph with parameters
`srg(99,14,1,2)` exist? The question is open. Nothing here closes it.

What this repository *does* contain is a growing body of **verified partial
theorems** about the local structure any such graph would need, organised for
adversarial review. Two independent certification methods are used, and they
agree wherever both apply.

## Current status, honestly

All results here are about a **rooted** hypothetical `srg(99,14,1,2)` — pick a
vertex, and study the 21 "fibers" its neighbourhood imposes on the 84 far
vertices. A fiber is either a good `C4` (Paley) pattern or "exceptional".

**Established (conditional on the rooted counting model faithfully describing a
hypothetical graph):**

- **No vertex has 13 or more C4 fibers.** A fiber-completion ladder reduces
  this to small certified cases, rung by rung from 20 fibers down to 13. This
  is the SAT certificate ladder; see
  [`adversarial-review-r230/theorem_k19/README_theorem_k19.md`](adversarial-review-r230/theorem_k19/README_theorem_k19.md).
  The k≥14 rungs are fully proof-checked; the k=13 rung is complete and
  cloud-verified with one residual (res1) whose proof is being re-verified, so
  the fully proof-backed frontier is k≥14 and k≥13 carries that one caveat.
- Most of that ladder is now **also** proved by an independent
  Euclidean-representation method whose certificates are tiny and checkable in
  exact rational arithmetic — no SAT solver, no proof-checker trust, no
  multi-gigabyte proof bodies. The forcing layer needs no search at all. See
  [`adversarial-review-r230/reports/GRAM_PSD_EUCLIDEAN_CERTIFICATES.md`](adversarial-review-r230/reports/GRAM_PSD_EUCLIDEAN_CERTIFICATES.md).
- The earliest result, R230: **no vertex is fully "Paley-perfect"** (all 21
  fibers C4). This strengthens Makhnev (1988) and Keramatipour (2023), who
  refuted the *every-vertex* version. See
  [`adversarial-review-r230/reports/FINAL_REPORT_R230_NONEXISTENCE.md`](adversarial-review-r230/reports/FINAL_REPORT_R230_NONEXISTENCE.md).

**Not established:** existence or nonexistence of the graph; anything about
vertices with 12 or fewer C4 fibers (that descent is in progress); a
third-party clean-machine replay.

> An early revision of this bundle overclaimed unconditional nonexistence. An
> adversarial review found the "forced-edge table" it relied on was an unproven
> assumption whose global form was in fact refuted in 1988. That claim was
> retracted; the correction trail is in
> [`adversarial-review-r230/reports/ADVERSARIAL_REVIEW_FINDINGS.md`](adversarial-review-r230/reports/ADVERSARIAL_REVIEW_FINDINGS.md).
> Every claim above is deliberately scoped to what is checked.

## The two methods

| | SAT certificate ladder | Gram / Euclidean certificates |
|---|---|---|
| Proves | each residual case UNSAT | each residual case has no PSD completion |
| Artifact | CNF + DRAT/LRAT proof (up to 28 GB) | exact rational `Z` + multipliers (KB) |
| Checked by | CaDiCaL + `drat-trim` / `cake_lpr` | exact-arithmetic standalone verifier |
| Rests on | rooted counting model + solver/checker soundness | rooted counting model + `theta=-4` representation |
| Coverage | full k≥14 ladder | most of k≥14; 6 even/degree-heavy cores excepted |

The Gram method removes the solver-and-checker trust for the cases it covers
and replaces gigabyte proofs with certificates a person can re-derive. The six
cores it does not yet cover (`K4`, `K2,3`, `C6`, the C4-cycle, and two dense
k14 residuals) remain SAT/LRAT-certified.

## Where to start

- **The corrected R230 theorem and its full case split:**
  [`adversarial-review-r230/reports/FINAL_REPORT_R230_NONEXISTENCE.md`](adversarial-review-r230/reports/FINAL_REPORT_R230_NONEXISTENCE.md)
- **The fiber-completion ladder (k≥14):**
  [`adversarial-review-r230/theorem_k19/README_theorem_k19.md`](adversarial-review-r230/theorem_k19/README_theorem_k19.md)
- **The exact Gram/Euclidean certificate layer:**
  [`adversarial-review-r230/reports/GRAM_PSD_EUCLIDEAN_CERTIFICATES.md`](adversarial-review-r230/reports/GRAM_PSD_EUCLIDEAN_CERTIFICATES.md)
- **The human-checkable reduction and review checklist:**
  [`adversarial-review-r230/README.md`](adversarial-review-r230/README.md)
- **Cached primary literature** (Makhnev 1988, Keramatipour, Cesarz–Woldar,
  Lou–Murin, Reimbayev): [`literature/`](literature/)

## A note on artifacts

Large CNF/DRAT proof bodies for the R230 certificate are included via Git LFS
under `adversarial-review-r230/scratchpad/root_cell_triangle_rep_cloud_r229_seq_intercoset/`;
a plain checkout without `git lfs pull` will see pointer files there. The
ladder's certificate manifests and reproducers are tracked under
`adversarial-review-r230/theorem_k19/`. Ephemeral solver working directories and
the largest proof bodies are kept out of Git by design.
