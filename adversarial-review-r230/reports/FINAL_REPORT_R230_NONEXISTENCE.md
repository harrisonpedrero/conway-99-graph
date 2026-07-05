# Conway 99-Graph: R230 Certificate — Corrected Claim

## Strengthening (2026-07-05): no vertex with ≥17 Paley fibers

The R230 result below excludes a *fully* Paley-perfect vertex (all 21 fibers
C4). A subsequent certificate campaign strengthens this to: **no
`srg(99,14,1,2)` has a vertex at which 17 or more of its 21 rooted fibers
induce a C4** (conditional on the same honest rooted-base encoding). The
mechanism is a *fiber completion lemma* — enough good C4 fibers force the
remaining ones — reduced by symmetry to 158 tiny certificates:
6 for the 20-fiber rung, 24 for the 19-fiber rung, 72 forcing certificates for
the four 18-fiber triple orbits plus 1 index-triangle residual, and 54 forcing
certificates for the nine 17-fiber quadruple orbit-types plus 1 C4-cycle
residual. The 17-fiber rung splits the C(21,4)=5985 four-edge subgraphs into
ten S7 orbit-types: nine are per-fiber forcing (54 certs) and the tenth is the
C4-cycle joint residual. Each is independently `drat-trim`-verified, with
vacuity controls (`base + good-fiber units only` times out at 900 s) confirming
the premises carry the content. The 18-fiber residual is dual-confirmed by an
independent CryptoMiniSat + XOR UNSAT; the 17-fiber C4-cycle residual is
triple-verified (a genuine deep `drat-trim` proof — 140K core clauses, 12.5K
RAT lemmas — plus `lrat-check` and CMS+XOR with forced Gaussian elimination).
See `../theorem_k19/` (theorem note, certificate manifests, and a reproducer
that rebuilds all 158 CNFs byte-identically — `MATCH=158 MISMATCH=0`). This is
still **not** unconditional nonexistence: vertices with ≤16 C4 fibers remain
unexcluded and Conway's problem stays open.

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
