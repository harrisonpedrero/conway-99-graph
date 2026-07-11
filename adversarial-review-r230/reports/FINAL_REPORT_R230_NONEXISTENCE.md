# Conway 99-Graph: R230 Certificate — Corrected Claim

## Independent method (2026-07-11): exact Gram/Euclidean certificates

The entire SAT-ladder narrative below is now **also** obtained by an
independent Euclidean-representation method whose certificates are exact
rational and checkable in exact arithmetic — no SAT solver, no proof checker,
no gigabyte proof bodies. It reproves most of the k≥14 ladder (and reproduces
the whole forcing layer by exact propagation, with no search), resting only on
the rooted counting model and the standard `theta=-4` representation rather than
on solver/checker soundness. Six even/degree-heavy cores (`K4`, `K2,3`, `C6`,
the C4-cycle, and two dense k14 residuals) remain SAT/LRAT-only. Full statement,
soundness basis, and limits:
[`GRAM_PSD_EUCLIDEAN_CERTIFICATES.md`](GRAM_PSD_EUCLIDEAN_CERTIFICATES.md). The
SAT ladder below remains the authoritative record for the six excepted cores and
for the rungs not yet re-covered.

## Strengthening (2026-07-05): no vertex with ≥14 Paley fibers

The R230 result below excludes a *fully* Paley-perfect vertex (all 21 fibers
C4). A subsequent certificate campaign strengthens this to: **no
`srg(99,14,1,2)` has a vertex at which 14 or more of its 21 rooted fibers
induce a C4** (conditional on the same honest rooted-base encoding). The
mechanism is a *fiber completion lemma* — enough good C4 fibers force the
remaining ones — reduced by symmetry to 830 tiny certificates:
6 for the 20-fiber rung, 24 for the 19-fiber rung, 72 forcing certificates for
the four 18-fiber triple orbits plus 1 index-triangle residual, 54 forcing
certificates for the nine 17-fiber quadruple orbit-types plus 1 C4-cycle
residual, 114 forcing certificates for the nineteen 16-fiber quintuple
orbit-types plus 2 joint residuals, 210 forcing certificates for the
thirty-five 15-fiber six-subset orbit-types plus 6 joint residuals, and 330
forcing certificates for the fifty-five 14-fiber seven-subset orbit-types plus
10 joint residuals. The 15-fiber rung splits the C(21,6)=54264 six-edge
subgraphs into 41 S7 orbit-types: thirty-five are per-fiber forcing (210 certs)
and the other six are the 2-connected / multi-cycle core orbits — K4, C6 (the
6-cycle), K_{2,3} (complete bipartite), a bowtie, two disjoint triangles, and one
further K4-ish graph — each a joint residual. The 14-fiber rung splits the
C(21,7)=116280 seven-edge subgraphs into 65 S7 orbit-types: fifty-five are
per-fiber forcing (330 certs) and the other ten are joint residuals — the dense
7-edge 2-connected cores. All ten 14-fiber residuals are UNSAT and certified by
`cake_lpr`, the formally-verified (HOL4/CakeML) LRAT proof checker (`s VERIFIED
UNSAT` each), because their proofs are large (up to 28GB) so independent
`drat-trim` checking would be infeasible; no residual is SAT, so no floor is
reached and the completion argument holds at every 14-fiber orbit. Each residual
is independently verified, with vacuity controls (`base + good-fiber units only`
times out at 900 s) confirming the premises carry the content. The 18-fiber residual is dual-confirmed by an
independent CryptoMiniSat + XOR UNSAT; the 17-fiber C4-cycle residual is
double-verified (a genuine deep `drat-trim` `s VERIFIED` proof — 140K core
clauses, 12.5K RAT lemmas — plus CMS+XOR with forced Gaussian elimination);
the two 16-fiber residuals are each `drat-trim` VERIFIED (C5: 46790 core
clauses, 3036 RAT lemmas; K4minusE: 29778 core clauses, 1129 RAT lemmas) and
re-confirmed by CMS+XOR with forced Gaussian elimination. Of the six 15-fiber
residuals, five are `drat-trim` VERIFIED (bowtie 158974 core; K4 275195 core /
71360 RAT lemmas via `cadical --chrono=0 --unsat`; res2 36264; two-triangles
50453; C6 235458) and the sixth — the K_{2,3} residual, the hardest instance in
the whole ladder — is certified via `cake_lpr`, a formally-verified (HOL4/CakeML)
LRAT proof checker whose soundness is a machine-checked theorem, `s VERIFIED UNSAT`
on a 22.4GB LRAT proof after `drat-trim` could not check its 4.88GB DRAT proof
locally (backward-mode OOM/timeout); `cake_lpr` is a stronger guarantee than
`drat-trim`. (The standard bundled `lrat-check` is deliberately NOT used: an
adversarial audit found it unsound — it trusts the solver's hints and prints
`c VERIFIED` on a bogus proof of a satisfiable formula — so all earlier
`lrat-check` corroboration was retracted; see `../theorem_k19/tools/cake_lpr/PROVENANCE.md`.)
All six are also
re-confirmed by CMS+XOR with forced Gaussian elimination. See `../theorem_k19/`
(theorem note, certificate manifests, and a reproducer that rebuilds all 830
CNFs byte-identically — `MATCH=830 MISMATCH=0`). This is still **not**
unconditional nonexistence: vertices with ≤13 C4 fibers remain unexcluded and
Conway's problem stays open.

## Verdict (corrected 2026-07-01)

**Theorem (what R230 actually proves).** No strongly regular graph
`srg(99,14,1,2)` contains a *Paley-perfect* vertex — a vertex at which all 21
rooted far-cell fibers induce a C4 (equivalently: at which the R204 forced-edge
table holds; equivalently: whose 21 rooted 9-vertex fiber closures all induce
the Paley graph of order 9).

This is a checked computational certificate of that statement: the case split
covers all rooted configurations under the stated hypothesis, and every fixed
case is independently proof-checked UNSAT.

**What R230 does NOT prove:** unconditional nonexistence of `srg(99,14,1,2)`.
An earlier revision of this report overclaimed that. The forced-edge table is a
*hypothesis*, not a theorem: an adversarial review (see
`ADVERSARIAL_REVIEW_FINDINGS.md`) showed it is unproven, and a literature
search then showed (a) its global version was already refuted by Makhnev in
1988 and independently by Keramatipour in 2023, and (b) the conjectured truth
(Keramatipour, Conjecture 3.4.4) is that *no* fiber is ever a C4 — the
opposite direction. Proving the table (the "kernel lemma") in either direction
is equivalent to resolving Conway's problem itself.

## Relation to published work

- **Makhnev 1988** (Mat. Zametki 44:5, Theorem 2): no `srg(99,14,1,2)`
  satisfies condition (\*) — the *every-vertex* Paley-perfect hypothesis.
- **Keramatipour 2023** (Cambridge MPhil / arXiv:2604.23037, Theorem 3.4.2):
  independent modern re-proof ("Paley(9) pattern").
- **Cesarz–Woldar** (Algebraic Combinatorics, arXiv:2308.02978, Remark 5.6):
  even a single Paley(9) inside a 99-graph is unresolved.
- **R230 (this bundle)**: no *single* Paley-perfect vertex — strictly stronger
  than the published every-vertex results, machine-certified with DRAT proofs.
  To our knowledge the single-vertex statement is new.

Source PDFs are cached under `../../literature/`.

## Certificate Bundle

Primary summary:

```powershell
artifacts\audit_json\r229_all24_ascii_drat_checked_summary.json
```

Recorded result:

- `ok=true`
- `reps=24`
- `unsatCount=24`
- `verifiedCount=24`
- solver: `scratchpad\tools\cadical\cadical.exe 3.0.0 --no-binary`
- checker: `scratchpad\tools\drat-trim\drat-trim.exe`
- total CNF bytes: `273647640`
- total ASCII DRAT bytes: `986182510`

Every representative `0..23` has an exact R229 CNF, an ASCII DRAT proof, a
CaDiCaL log containing `s UNSATISFIABLE`, a `drat-trim` log containing
`s VERIFIED`, and SHA-256 hashes recorded in the summary.

Independent re-verification (adversarial review, 2026-07-01):

- all 24 CNFs rebuild **byte-identical** from
  `source/root_cell_permutation_sat.py` (manifest SHA-256 match, 24 distinct);
- all 24 DRAT proofs re-checked `s VERIFIED` with an independently compiled
  `drat-trim`;
- R220 orbit split re-verified (24 orbits, sizes sum exactly 13824), and
  reproduced on a second disjoint fiber triple `((0,2),(1,4),(3,6))`;
- `S2 wr S7` verified transitive on each far-pair class
  (`scratchpad/pair_orbit_check/`).

## Reduction Chain (hypothesis-first)

1. Assume a hypothetical `srg(99,14,1,2)` has a Paley-perfect vertex; root
   there. The neighborhood is `7K2`; the 84 far vertices split into 21 rooted
   fibers, and the forced-edge table holds **by hypothesis**.
2. R204: the free far-edge surface reduces exactly to a 105-block `S4`
   permutation CSP. The clean-room symbolic audit
   (`root_cell_r204_cleanroom_symbolic_audit.json`, `ok=true`,
   `symbolicPairEquationsChecked=3360`, `symbolicMismatches=[]`) verifies the
   algebra downstream of the hypothesis.
3. R220: 24 orbit representatives cover all `24^3=13824` triangle assignments.
4. R229: exact intersecting-fiber D8-coset cuts
   (`root_cell_intersecting_coset_sat_audit_r229b.json`, `ok=true`).
5. R230: all 24 CNFs UNSAT with independent DRAT verification.

Hence no graph with a Paley-perfect vertex exists.

## Reproduction Commands

Core reduction audits:

```powershell
python source\root_cell_r204_cleanroom_symbolic_audit.py --json-out artifacts\audit_json\root_cell_r204_cleanroom_symbolic_audit.json
python source\root_cell_permutation_formula_audit.py --json-out scratchpad\root_cell_permutation_formula_audit_r229.json
python source\root_cell_triangle_orbit_audit.py --json-out scratchpad\root_cell_triangle_orbit_audit_r229.json
python source\root_cell_triangle_rep_unit_audit.py --json-out scratchpad\root_cell_triangle_rep_unit_audit_r229.json
python source\root_cell_block_rep_audit.py --json-out scratchpad\root_cell_block_rep_audit_r229.json
python source\root_cell_intersecting_coset_sat_audit.py --build-formula --json-out scratchpad\root_cell_intersecting_coset_sat_audit_r229b.json
```

Export the R229 suite:

```powershell
python source\root_cell_triangle_rep_cloud_suite.py --out-dir scratchpad\root_cell_triangle_rep_cloud_r229_seq_intercoset --card-encoding seqcounter --intersecting-coset-cuts
```

Check the certificate bundle:

```powershell
python source\root_cell_r229_certificate_audit.py --json-out scratchpad\root_cell_r229_certificate_audit_current.json
```

## What Remains Open

Conway's problem. A hypothetical graph in which **every** vertex has at least
one non-C4 fiber is untouched by this certificate. The corresponding "flip"
SAT instances are each equivalent to the open problem: UNSAT would prove the
forced table (and hence, with this certificate, nonexistence); SAT would
construct the graph. Treat any such computation as a moonshot, not a gap-fill.

## Caveat

This is a repository-local computational proof of the corrected claim. For
publication-grade use, archive the source tree, exact CNFs/DRATs, hashes,
solver/checker builds, and replay on a clean independent machine
(see `../../CLEAN_MACHINE_PLAN.md`).
