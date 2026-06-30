# Conway 99-graph research loop — progress

**Goal:** Find a strongly regular graph srg(99,14,1,2), OR produce new reusable
constraints toward proving none exists.

**Reality anchor (read this every resume):** This is *Conway's 99-graph problem*,
a famous OPEN problem with a $1000 prize, unsolved since it was posed (Biggs 1969 /
Conway 1975, prize 2014) and still open as of 2025. It has resisted decades of
expert attack. An LLM loop will almost certainly NOT find the graph or a full
nonexistence proof. The honest, valuable deliverable is **verified incremental
constraints**, computational experiments that are actually run, and an organized
compendium — never a fabricated "solution." Adversarially verify every claimed new
constraint before recording it (math-olympiad ethos: calibrated confidence, no bluff).

**R230 update:** the current repository now contains a checked computational
nonexistence certificate from the rooted proof-SAT route.  Treat older "open"
language as historical unless it is explicitly part of an external/publication
claim.  The local acceptance standard is the R204/R220/R229 reduction audits plus
independently checked UNSAT proofs for all 24 R220 triangle representatives.

---

## R230 -- all R229 representatives independently proof-checked [2026-06-30]
## OUTCOME: verified computational nonexistence certificate for `srg(99,14,1,2)`.

ARTIFACTS:
 - new: `root_cell_r229_certificate_audit.py`
 - new: `FINAL_REPORT_R230_NONEXISTENCE.md`
 - proof summary:
   `scratchpad\root_cell_triangle_rep_cloud_r229_seq_intercoset\r229_all24_ascii_drat_checked_summary.json`
 - proof tools built locally:
   `scratchpad\tools\cadical\cadical.exe` (CaDiCaL 3.0.0, run with `--no-binary`) and
   `scratchpad\tools\drat-trim\drat-trim.exe`
 - proof inputs/outputs:
   `scratchpad\root_cell_triangle_rep_cloud_r229_seq_intercoset\root_cell_triangle_rep_XX_seqcounter_intercoset.cnf`
   and matching `*_ascii.drat`, `*_cadical_ascii_proof.log`, `*_drat_trim_ascii.log` files for
   `XX=00..23`.

CERTIFICATE SUMMARY:
`r229_all24_ascii_drat_checked_summary.json` reports `ok=true`, `reps=24`,
`unsatCount=24`, and `verifiedCount=24`.  Total checked material is
`273647640` CNF bytes and `986182510` ASCII DRAT bytes.  Every representative
`0..23` has a CaDiCaL `s UNSATISFIABLE` solve log and an independent drat-trim
`s VERIFIED` checker log.  The eight previously live R220 representatives
`[0,2,7,8,10,15,21,22]` are included; the 16 unit-dead representatives were also
exported, solved, and checked for a uniform all-24 certificate.

REDUCTION CHAIN:
 - R204: root-cell fiber-block reduction to the 105-block `S4` permutation CSP;
   `root_cell_permutation_formula_audit.py` returned `ok=true`, `pairs_checked=69720`.
 - R220: triangle representative split covers all `24^3=13824` root triangle assignments by
   24 orbits; `root_cell_triangle_orbit_audit.py` and `root_cell_triangle_rep_unit_audit.py`
   returned `ok=true`.
 - R229: intersecting D8-coset SAT projection is exact; `root_cell_intersecting_coset_sat_audit.py`
   returned `ok=true` with 105 intersecting pairs, 35280 full rows per target, 182 allowed
   coset rows out of 729, and no orientation failures.
 - R230: every resulting fixed-representative CNF is independently DRAT-verified UNSAT.

ONE-COMMAND LOCAL CERTIFICATE AUDIT:
`python root_cell_r229_certificate_audit.py --json-out scratchpad\root_cell_r229_certificate_audit_current.json`

VERDICT:
Accepted as a checked computational proof, within the repository's exact reduction chain, that no
`srg(99,14,1,2)` exists.  A publication-grade claim should archive the exact CNFs/DRATs, hashes,
source tree, and tool binaries and ideally get an independent replay, but the project stop condition
is met locally: the search surface covers all cases and every case is proof-checked UNSAT.

R43 STRUCTURAL SWITCH CONSOLIDATION:
The `r=3` / 45-vertex star-complement Stage-A route remains validated and one-command runnable
(`s3_cloud_r3_stagea.py`), but it is now superseded as the decisive route by the R230 rooted SAT
certificate.  Keep it only as an independent search-cost cross-check or fallback if the proof bundle
is challenged.

NEXT ACTION:
No more search is required for the local goal.  If continuing for publication/reproducibility, package
and replay the R230 certificate bundle on a clean machine, then produce a formal proof note explaining
the R204/R220/R229 reductions in theorem form.

---

## R229 -- intersecting D8-coset shadow moved into proof-SAT [2026-06-30]
## OUTCOME: all eight R220 survivor reps are SAT-solver UNSAT with the new cuts; superseded by R230 proof certificates.

ARTIFACTS:
 - updated: `root_cell_permutation_sat.py --intersecting-coset-cuts`
 - updated: `root_cell_triangle_rep_cloud_suite.py --intersecting-coset-cuts`
 - new: `root_cell_intersecting_coset_sat_audit.py`
 - note: `ROOT_CELL_INTERSECTING_COSET_SAT_R229.md`
 - key outputs:
   `scratchpad\root_cell_intersecting_coset_sat_audit_r229b.json`,
   `scratchpad\root_cell_triangle_rep_cloud_r229_unsat_suite\manifest.json`,
   `scratchpad\root_cell_triangle_rep_cloud_r229_seq_intercoset\manifest.json`,
   `scratchpad\root_cell_sat_toolchain_audit_current_r229.json`

ENCODING:
The R227 intersecting-fiber D8-coset projection is now encoded in CNF through exact relative-permutation
literals tied back to the original S4 block-entry variables.  For each of the 105 intersecting rooted
fiber pairs, the six common disjoint fibers get right-D8-coset literals, and the CNF forbids the
`729-182=547` impossible coset patterns induced by the exact 35280-row R210 table.  This is finer than
the R228 pure coset quotient because the coset literals are backed by S4 entry equalities.

AUDITS:
`root_cell_intersecting_coset_sat_audit.py --build-formula` returned `ok=true`: 105 intersecting pairs,
3 target types, full row range `[35280,35280]`, allowed coset row range `[182,182]`, forbidden row range
`[547,547]`, and no relative-orientation failures over all `24 x 24` block pairs.  The reduction-chain
audits were rerun and passed: `root_cell_permutation_formula_audit.py` (`pairs_checked=69720`),
`root_cell_triangle_orbit_audit.py` (24 orbits over 13824 triples),
`root_cell_triangle_rep_unit_audit.py` (same 16 unit-dead / 8 live R220 split), and
`root_cell_block_rep_audit.py` (2 D8 double cosets, covering all 24 S4 permutations).

MEASURED SAT EVIDENCE:
One-command suite:
`python root_cell_triangle_rep_cloud_suite.py --out-dir scratchpad\root_cell_triangle_rep_cloud_r229_unsat_suite --card-encoding seqcounter --intersecting-coset-cuts --smoke-solve --solver cadical153 --time-cap 120 --no-export`
completed in `516.6051s`.  All eight R220 survivor reps solved `UNSAT`:
 - rep0 `22.8648s`, rep2 `45.5025s`, rep7 `88.0111s`, rep8 `92.4448s`,
   rep10 `11.9727s`, rep15 `98.4614s`, rep21 `70.0938s`, rep22 `60.9130s`.
The exported proof-input suite is:
`python root_cell_triangle_rep_cloud_suite.py --out-dir scratchpad\root_cell_triangle_rep_cloud_r229_seq_intercoset --card-encoding seqcounter --intersecting-coset-cuts`

READINESS / CAVEAT:
Historical R229 caveat: at this point the proof certificates were still missing.  R230 supersedes this:
standalone CaDiCaL and drat-trim were built locally, all 24 representatives were exported/solved, and
the all-24 summary reports `unsatCount=24`, `verifiedCount=24`.

NEXT ACTION:
Superseded by R230.  Use `root_cell_r229_certificate_audit.py` for replay/archival rather than more
heuristic SAT tuning.

---

## R228 -- pure D8-coset quotient checked [2026-06-30]
## OUTCOME: feasible; coset quotient does not prove nonexistence or shrink the exact R220 survivors.

ARTIFACTS:
 - new: `root_cell_coset_quotient_probe.py`
 - note: `ROOT_CELL_COSET_QUOTIENT_R228.md`
 - outputs:
   `scratchpad\root_cell_coset_quotient_unfixed_r228.json`,
   `scratchpad\root_cell_coset_quotient_all_reps_r228.json`

MODEL:
The quotient keeps `210` directed block-coset variables and `945` relative-coset variables, with exact
projection constraints from inverse blocks, relative composition, R209 disjoint residual rows, R227
intersecting coset rows, and R222 matching-triangle rows.  Infeasibility would be a sound obstruction.

RESULT:
The unfixed quotient is feasible (`OPTIMAL`, wall `2.4067s`).  Fixing each R220 representative only at
coset level gives:
 - UNSAT: `[1,3,5,9,11,14]`
 - SAT: `[0,2,4,6,7,8,10,12,13,15,16,17,18,19,20,21,22,23]`
All eight exact R220 survivors `[0,2,7,8,10,15,21,22]` remain feasible in the quotient.

VERDICT:
Accepted as a clean boundary result.  The D8-coset shadow is useful propagation inside the full CP-SAT
model, but the coset quotient alone is too weak.  The extra R220 unit kills beyond `[1,3,5,9,11,14]`
depend on finer S4 permutation-entry structure.

NEXT ACTION:
Do not retry the pure coset quotient as a standalone obstruction.  If pursuing cosets, combine them
with selected finer S4-entry constraints or move the R227 shadow into a proof-SAT encoding.

---

## R227 -- compact intersecting-table parity/coset shadows tested [2026-06-30]
## OUTCOME: D8-coset shadow is the strongest short-run rooted CP-SAT profile; still UNKNOWN at 180s.

ARTIFACTS:
 - updated: `root_cell_permutation_csp.py --intersecting-parity-table --intersecting-coset-table`
 - new: `root_cell_intersecting_shadow_audit.py`
 - note: `ROOT_CELL_INTERSECTING_SHADOWS_R227.md`
 - outputs:
   `scratchpad\root_cell_intersecting_shadow_audit_r227.json`,
   `scratchpad\root_cell_permutation_csp_best_plus_intersect_parity_r227.json`,
   `scratchpad\root_cell_permutation_csp_best_plus_intersect_coset_r227.json`,
   `scratchpad\root_cell_permutation_csp_best_plus_intersect_coset_parity_r227.json`,
   `scratchpad\root_cell_permutation_csp_triangle_intersect_coset_r227.json`,
   `scratchpad\root_cell_permutation_csp_intersect_coset_r227.json`,
   `scratchpad\root_cell_permutation_csp_intersect_coset_180s_r227.json`

RESULT:
The exact R210 table has compact shadows:
 - parity: `52/64` allowed patterns;
 - D8-coset: `182/729` allowed patterns.
Audit returned `ok=true`; both shadows exactly match the full table projections.

MEASUREMENTS:
All short runs used `--time-cap 60 --workers 8` and returned `UNKNOWN`.
 - R225 default (`--disjoint-tables --matching-triangle-tables --intersecting-pair-tables`):
   `14788` conflicts / `400367` branches.
 - R225 + parity: `8863` conflicts / `652149` branches.
 - R225 + coset: `8016` conflicts / `234594` branches.
 - R225 + coset + parity: `8960` conflicts / `629971` branches.
 - matching-triangle + coset, no pair projections: `9236` conflicts / `173732` branches.
 - coset only over disjoint tables: `5` conflicts / `16507` branches.

Longer check:
`--disjoint-tables --intersecting-coset-table --time-cap 180` remained `UNKNOWN`,
`83847` conflicts / `1852607` branches.

VERDICT:
Accepted as a real compact algebraic projection and the strongest short-run rooted CP-SAT profile so far.
It is not a proof.  The local diagnostic default should shift to `--disjoint-tables
--intersecting-coset-table`.  Do not add parity by default.  Pair projections and matching-triangle
tables remain exact but worsened the 60s branch profile once the coset shadow was present; use them only
for targeted benchmarks or a different solver.

NEXT ACTION:
Try to convert the D8-coset shadow into SAT/CNF or a proof-solver-friendly formulation, or extract
additional compact coset-level constraints.  Bounded CP-SAT timeouts are not evidence of nonexistence.

---

## R226 -- intersecting-fiber ternary projections audited but not hot-path viable [2026-06-30]
## OUTCOME: exact arity-3 R210 projections exist, but CP-SAT spends the budget before search.

ARTIFACTS:
 - updated: `root_cell_permutation_csp.py --intersecting-triple-tables`
 - new: `root_cell_intersecting_triple_projection_audit.py`
 - note: `ROOT_CELL_INTERSECTING_TRIPLE_PROJECTIONS_R226.md`
 - outputs:
   `scratchpad\root_cell_intersecting_triple_projection_audit_r226.json`,
   `scratchpad\root_cell_permutation_csp_triangle_intersect_pair_triple_r226.json`

RESULT:
The arity-3 projections of the full R210 intersecting table are exact: audit returned `ok=true`,
`projection_count=20`, `projection_row_histogram={3252:20}`, `total_ternary_rows=65040`.

MEASUREMENT:
`python root_cell_permutation_csp.py --time-cap 60 --workers 8 --disjoint-tables --matching-triangle-tables --intersecting-pair-tables --intersecting-triple-tables ...`
returned `UNKNOWN` with `25515` vars / `55755` constraints / `5040` tables, but `0` conflicts and
`0` branches after `62.24s`.  This repeats the R210 presolve/table-handling failure mode.

VERDICT:
Accepted as an exact relation but not a viable local CP-SAT layer.  Keep the binary R225 projections
as the default; do not add `--intersecting-triple-tables` unless the relation is decomposed further
or moved to a solver/table encoding that handles these ternary tables efficiently.

NEXT ACTION:
Avoid heavier extensional tables in CP-SAT.  If continuing the intersecting-fiber line, look for
compact algebraic/parity/coset consequences rather than arity-3+ table projections.

---

## R225 -- R210 intersecting-fiber table decomposed into binary projections [2026-06-30]
## OUTCOME: strongest rooted CP-SAT propagation profile so far; still UNKNOWN.

ARTIFACTS:
 - updated: `root_cell_permutation_csp.py --intersecting-pair-tables`
 - new: `root_cell_intersecting_pair_projection_audit.py`
 - note: `ROOT_CELL_INTERSECTING_PAIR_PROJECTIONS_R225.md`
 - outputs:
   `scratchpad\root_cell_intersecting_pair_projection_audit_r225.json`,
   `scratchpad\root_cell_permutation_csp_intersect_pair_r225.json`,
   `scratchpad\root_cell_permutation_csp_triangle_intersect_pair_r225.json`,
   `scratchpad\root_cell_permutation_csp_triangle_intersect_pair_holonomy_r225.json`

RESULT:
R210's full intersecting-fiber table has arity 6 and `35280` rows, too heavy for local CP-SAT.  R225
uses all 15 binary projections of the exact table.  Audit returned `ok=true`: each projection has
`356` allowed pairs out of `24^2=576`, forbidding `220` pairs, and exactly matches the full table's
projection.  Total binary rows per intersecting target: `5340`.

MEASUREMENTS:
All runs used `--time-cap 60 --workers 8` and returned `UNKNOWN`.
 - baseline `--disjoint-tables`: `40018` conflicts / `886008` branches.
 - `--disjoint-tables --matching-triangle-tables`: `30041` conflicts / `562026` branches.
 - `--disjoint-tables --intersecting-pair-tables`: `12403` conflicts / `466352` branches.
 - `--disjoint-tables --matching-triangle-tables --intersecting-pair-tables`:
   `14788` conflicts / `400367` branches.
 - adding `--matching-holonomy` on top worsened branch count to `445293`.

VERDICT:
Accepted as a real decomposition of an exact but previously unusable relation.  It is not a proof, but
it changes the rooted CP-SAT default: use `--disjoint-tables --matching-triangle-tables
--intersecting-pair-tables`; leave parity holonomy off unless a later profile reverses this.

NEXT ACTION:
Either derive stronger low-arity projections from the R210 table (triples, parity/coset summaries) or
move this improved rooted CP-SAT/SAT surface to proof-grade solving.  Do not revive the full arity-6
`--intersecting-tables` hot path.

---

## R224 -- global R222 triangle-table quotient checked [2026-06-30]
## OUTCOME: clean negative; the global table alone kills no additional R220 survivors.

ARTIFACTS:
 - new: `root_cell_global_triangle_table_probe.py`
 - note: `ROOT_CELL_GLOBAL_TRIANGLE_TABLE_R224.md`
 - output: `scratchpad\root_cell_global_triangle_table_probe_all_reps_r224.json`

COMMAND:
`python root_cell_global_triangle_table_probe.py --all-reps --time-cap 10 --workers 8 --json-out scratchpad\root_cell_global_triangle_table_probe_all_reps_r224.json`

RESULT:
The quotient keeps only the 105 direct block-id variables plus the 105 R222 matching-triangle tables.
It kills exactly the same 16 representatives already killed by R220:
`[1,3,4,5,6,9,11,12,13,14,16,17,18,19,20,23]`.  All eight R220 survivors
`[0,2,7,8,10,15,21,22]` are globally feasible in this quotient.

VERDICT:
Accepted as a clean negative.  The R222 table is useful propagation but not a standalone survivor prune;
further progress needs actual permutation-entry structure, intersecting-fiber information, or full
common-neighbour equations.

NEXT ACTION:
Do not spend more time on the pid-only global matching-triangle quotient unless adding a new exact table
changes the quotient.

---

## R223 -- R222 matching-triangle table added to rooted CP-SAT [2026-06-30]
## OUTCOME: compact CP-SAT propagation win; still UNKNOWN, and parity holonomy is not a default add-on.

ARTIFACTS:
 - updated: `root_cell_permutation_csp.py --matching-triangle-tables`
 - note: `ROOT_CELL_CSP_TRIANGLE_TABLES_R223.md`
 - outputs:
   `scratchpad\root_cell_permutation_csp_disjoint_tables_r223_baseline.json`,
   `scratchpad\root_cell_permutation_csp_matching_triangle_tables_r223.json`,
   `scratchpad\root_cell_permutation_csp_triangle_tables_holonomy_r223.json`

COMMANDS / RESULTS:
All runs used `--time-cap 60 --workers 8` and returned `UNKNOWN`.
 - baseline `--disjoint-tables`: `24885` vars / `51345` constraints / `630` tables;
   `40018` conflicts / `886008` branches.
 - `--disjoint-tables --matching-triangle-tables`: `24885` vars / `51450` constraints / `735` tables
   (`105` matching-triangle tables); `30041` conflicts / `562026` branches.
 - `--disjoint-tables --matching-triangle-tables --matching-holonomy`: `25200` vars / `51870`
   constraints / `1155` tables; `34357` conflicts / `615402` branches.

VERDICT:
Accepted as a real compact propagation improvement, not a proof.  The full matching-triangle table
is much better than parity-only holonomy on this surface; once the full table is present, the parity
holonomy worsens the measured branch count and should stay off by default.

NEXT ACTION:
For rooted CP-SAT diagnostics, prefer `--disjoint-tables --matching-triangle-tables`.  For proof-SAT,
continue to benchmark lean R220 versus cut-heavy R222 CNFs, or derive a stronger exact relation that
reduces the eight survivor reps.

---

## R222 -- full matching-triangle forbidden-triple cuts added to rooted SAT [2026-06-30]
## OUTCOME: R220 survivor orbits are globalized into a sound optional SAT cut family; all 8 reps remain UNKNOWN locally.

ARTIFACTS:
 - updated: `root_cell_permutation_sat.py --matching-triangle-cuts`
 - updated: `root_cell_triangle_rep_cloud_suite.py --matching-triangle-cuts`
 - new: `root_cell_matching_triangle_cut_audit.py`
 - note: `ROOT_CELL_MATCHING_TRIANGLE_CUTS_R222.md`
 - outputs:
   `scratchpad\root_cell_matching_triangle_cut_audit_r222.json`,
   `scratchpad\root_cell_permutation_sat_tri0_direct_trianglecuts_r222.json`,
   `scratchpad\root_cell_permutation_sat_trianglecuts_5s_summary_r222.json`,
   `scratchpad\root_cell_triangle_rep_cloud_r222_noexport\manifest.json`

RESULT:
The eight R220 survivor orbits contain exactly `2176` direct-block triples out of `24^3=13824`.
Thus `11648` direct triples are forbidden on every matching of three pairwise-disjoint rooted fibers.
There are `105` rooted matching triples, so `--matching-triangle-cuts` adds `1223040` length-12
clauses and no new variables.

VALIDATION:
 - `python root_cell_matching_triangle_cut_audit.py --json-out scratchpad\root_cell_matching_triangle_cut_audit_r222.json`
   returned `ok=true`, `mismatch_count=0`, `allowed_triples=2176`, `forbidden_triples=11648`,
   `matching_triples=105`, `expected_cut_clauses=1223040`.
 - Build-only rep 0 direct cut CNF:
   `77280` vars / `1628772` clauses, `matching_triangle_cut_clauses=1223040`, build `8.98s`.
 - No-export cloud-suite sanity:
   `python root_cell_triangle_rep_cloud_suite.py --out-dir scratchpad\root_cell_triangle_rep_cloud_r222_noexport --card-encoding direct --matching-triangle-cuts --no-export`
   rebuilt all 24 cut formulas in `231.0s` and preserved the R220 partition:
   killed `[1,3,4,5,6,9,11,12,13,14,16,17,18,19,20,23]`, survivors `[0,2,7,8,10,15,21,22]`.
 - Five-second Cadical195 smoke on the eight survivors with cuts remained all `UNKNOWN`, but local
   decisions/propagations dropped to roughly `37k-62k` decisions and `29M-42M` propagations versus
   the lean R220 survivor smoke's roughly `82k-122k` decisions and `58M-73M` propagations.

VERDICT:
Accepted as a sound structural strengthening and optional proof-SAT mode, not as a proof.  The tradeoff:
lean R220 survivor CNF is `77280/405732`; R222 cut survivor CNF is `77280/1628772`.  Use R222 when
solver propagation is worth the larger CNF.  Proof-grade nonexistence still requires all 8 live CNFs
to be solved UNSAT with independently checked proofs, or another exact reduction first.

NEXT ACTION:
Either run cloud proof-logging on the 8 R220/R222 survivor CNFs, benchmark cut-vs-lean on one survivor
with the actual proof solver, or look for a stronger table/reconstruction relation that reduces the
8 survivors without exploding CNF size.

---

## R221 -- residual one-block split after R220 probed [2026-06-30]
## OUTCOME: mostly negative; only reps 8/10/22 have small one-block unit kills, not a default route.

ARTIFACTS:
 - new: `root_cell_triangle_next_block_probe.py`
 - note: `ROOT_CELL_TRIANGLE_NEXT_BLOCK_R221.md`
 - output: `scratchpad\root_cell_triangle_next_block_probe_r221.json`

COMMAND:
`python root_cell_triangle_next_block_probe.py --json-out scratchpad\root_cell_triangle_next_block_probe_r221.json`

RESULT:
For each R220 survivor, the probe computed the residual rooted symmetry group, residual orbits of
candidate disjoint fiber blocks, and block-stabilizer orbits of the 24 possible S4 assignments.
Each assignment-orbit representative was tested by exact unit propagation after adding four block
unit assumptions.

Residual group sizes matched the orbit-stabilizer check from the 6144-element matching-triple
stabilizer: reps `0,2,7,8,10,15,21,22` have residual sizes `96,48,96,16,8,16,24,48`.

Maximum killed assignment weight by survivor:
`rep0=0/24`, `rep2=0/24`, `rep7=0/24`, `rep8=8/24`, `rep10=8/24`,
`rep15=0/24`, `rep21=0/24`, `rep22=8/24`.

VERDICT:
Accepted as a measured mostly-negative result.  A residual one-block split increases proof case count
and gives only small optional kills for three reps, so it should not replace the R220 survivor suite.
Its useful lesson was to globalize the R220 survivor orbits into the R222 matching-triangle table cuts.

NEXT ACTION:
Do not pursue ad hoc second-block splitting unless a concrete proof-solver profile says a specific
subcase split pays for its added case count.

---

## R220 -- matching-triangle rooted SAT split and survivor CNF suite [2026-06-30]
## OUTCOME: R206/R208 two-block SAT split is superseded by 24 triangle reps, with only 8 live CNFs.

ARTIFACTS:
 - updated: `root_cell_permutation_sat.py --triangle-rep-index`
 - new: `root_cell_triangle_orbit_audit.py`
 - new: `root_cell_triangle_rep_unit_audit.py`
 - new: `root_cell_triangle_rep_cloud_suite.py`
 - note: `ROOT_CELL_TRIANGLE_REP_SPLIT_R220.md`
 - outputs:
   `scratchpad\root_cell_triangle_orbit_audit_r220.json`,
   `scratchpad\root_cell_triangle_rep_unit_audit_r220.json`,
   `scratchpad\root_cell_triangle_rep_cloud_r220\manifest.json`,
   `scratchpad\root_cell_triangle_rep_cloud_r220\root_cell_triangle_rep_{00,02,07,08,10,15,21,22}_direct.cnf`

COMMANDS:
 - `python root_cell_triangle_orbit_audit.py --json-out scratchpad\root_cell_triangle_orbit_audit_r220.json`
 - `python root_cell_triangle_rep_unit_audit.py --json-out scratchpad\root_cell_triangle_rep_unit_audit_r220.json`
 - `python root_cell_triangle_rep_cloud_suite.py --out-dir scratchpad\root_cell_triangle_rep_cloud_r220 --card-encoding direct`

RESULT:
For the fixed matching triple of rooted fibers `(0,1),(2,3),(4,5)`, the three direct S4 blocks
have `24^3=13824` ambient assignments.  Exhaustive orbit BFS under the actual rooted-label stabilizer
matches the abstract `D8^3 semidirect S3` action exactly and gives `24` orbit representatives, with
size histogram `{64:2, 128:4, 256:2, 384:5, 768:8, 1536:3}`.

Each `--triangle-rep-index` direct-cardinality CNF has `77280` vars / `405732` clauses.  Independent
plain Boolean unit propagation kills 16 representatives:
`[1,3,4,5,6,9,11,12,13,14,16,17,18,19,20,23]`.  Survivors are
`[0,2,7,8,10,15,21,22]`.  This exactly matches the 5s Cadical195 smoke suite's zero-decision UNSAT
set versus UNKNOWN set.

SURVIVOR CNF HASHES:
 - rep 0 `(0,0,0)`:  `6c3c01cf908defc4571ff9fb9f15b6610f332312832b6b0ebb18575db956176d`
 - rep 2 `(0,0,2)`:  `2eb94fb0029c73679b40d83c47601d1b2e9eeb91562ed805d856ffb9bfd0ed58`
 - rep 7 `(0,0,23)`: `26f0bbe7f1431aacabfa440b4aa9fc99167e976a4169b52ad8c9c2dd65e0bdc4`
 - rep 8 `(0,1,1)`:  `35b11a3b8a2d9d70862b5f3640f5d7be28e2f90b71a6588e4d768923a01b6d7a`
 - rep 10 `(0,1,4)`: `0c192e6615fd5d499c4d87821a4ecef9b7ff1f0037fc0d17b227f2d47927e6ad`
 - rep 15 `(0,1,17)`: `180da713dddebb4875281174c55148e22f2e826f3ed5e5ca7d3e4e7ba47fcc77`
 - rep 21 `(1,1,17)`: `28bfe0f0b9eac7895e4a8224a9a04de28b19d397c8d849655853b80098d4d0cb`
 - rep 22 `(1,4,5)`:  `baf9a7305a2587766e97c71d6791472eda0b9ca7ce6e8183f41c255fa2c22557`

VALIDATION:
 - `python -m py_compile root_cell_permutation_sat.py root_cell_triangle_orbit_audit.py root_cell_triangle_rep_unit_audit.py root_cell_triangle_rep_cloud_suite.py` passed.
 - Orbit audit rerun after cleanup returned `ok=true`.
 - Unit audit rerun returned `unit_conflict_count=16`, `survivor_count=8`.
 - One-command suite export rebuilt all 24 reps in 19.0s and wrote the 8 survivor CNFs plus manifest
   `FA61BBF30CC7FEC972E909D3224B8DCD814A8E875BAAEE63629C56E60A87EBF6`.

VERDICT:
Accepted as a real correctness-preserving proof-cost reduction for rooted SAT, not as evidence of
existence/nonexistence.  The killed 16 reps require no SAT proof beyond the encoded unit contradiction
and the orbit audit; the remaining proof stack is the 8 fixed-hash survivor CNFs.  Any nonexistence
claim still requires proof-logging UNSAT and independent checking for all 8 survivors.  Any SAT model
must reconstruct and verify a full `srg(99,14,1,2)`.

R43 STRUCTURAL SWITCH CONSOLIDATION:
The `r=3` / 45-vertex star-complement Stage-A route remains the primary cloud measurement route
(R199/R218).  R220 is a separate proof-SAT route; it reduces rooted proof cases but does not replace
the r=3 frontier-cost experiment.

NEXT ACTION:
Either launch proof-logging SAT on the 8 R220 survivor CNFs, or derive another exact relation that kills
or shrinks those survivors before spending cloud proof time.  For search-cost measurement, run the R43
`r=3` cloud wrapper; keep the two tracks separate in reports.

---

## R219 -- rooted SAT DIMACS export added for proof-grade cloud tooling [2026-06-30]
## OUTCOME: R206/R208 representative SAT slices are now fixed hashable CNFs; no SAT/UNSAT verdict.

ARTIFACTS:
 - updated: `root_cell_permutation_sat.py --cnf-out --no-solve`
 - note: `ROOT_CELL_SAT_DIMACS_EXPORT_R219.md`
 - outputs:
   `scratchpad\root_cell_permutation_sat_direct_square_r219.cnf`,
   `scratchpad\root_cell_permutation_sat_direct_nonsquare_r219.cnf`,
   `scratchpad\root_cell_permutation_sat_direct_square_export_r219.json`,
   `scratchpad\root_cell_permutation_sat_direct_nonsquare_export_r219.json`

COMMANDS:
 - `python root_cell_permutation_sat.py --block-rep square --card-encoding direct --cnf-out scratchpad\root_cell_permutation_sat_direct_square_r219.cnf --no-solve --json-out scratchpad\root_cell_permutation_sat_direct_square_export_r219.json`
 - `python root_cell_permutation_sat.py --block-rep nonsquare --card-encoding direct --cnf-out scratchpad\root_cell_permutation_sat_direct_nonsquare_r219.cnf --no-solve --json-out scratchpad\root_cell_permutation_sat_direct_nonsquare_export_r219.json`

RESULT:
Both direct-cardinality representative slices export as DIMACS with `77280` vars / `405724` clauses,
file size `7714533` bytes.  SHA-256:
 - square: `d244fc73c930f3c679c08836001985c23a2d01b0b1c73a38bee61e975478fda0`
 - nonsquare: `25891300867286ee445506491cd84688836f6c675eed691211e8e4a9d1f363b0`

VALIDATION:
 - `python -m py_compile root_cell_permutation_sat.py` passed.
 - PySAT read-back loaded both DIMACS files and checked `nv=77280`, `clauses=405724`, matching JSON
   encoder stats for each slice.

VERDICT:
Accepted as a runnable proof-grade cloud preparation step, not as mathematical evidence.  A future
nonexistence result from this split requires both exact CNFs to be solved UNSAT by a proof-logging SAT
solver and independently checked against these hashes.  SAT still requires full graph reconstruction.

NEXT ACTION:
Run a cloud proof stack on both CNFs, or continue deriving stronger rooted constraints that reduce these
formulas before proof logging.

---

## R218 -- full r=3 soundness gate rerun with sufficient wall time [2026-06-30]
## OUTCOME: R216 gate caveat cleared; cloud experiment is now backed by a fresh full green gate.

ARTIFACTS:
 - note: `READINESS_R218_FULL_GATE.md`

COMMAND:
`python s3_slice_harness.py --gate`

RESULT:
Foreground wall time `238.5s`; gate ended with `SOUNDNESS GATE: ALL GREEN`.

VERIFICATION DETAILS:
 - rook(9) replay accepted all `9! = 362880` vertex orders;
 - triangle counter matched exact rook(9) triangle count `t=6`;
 - srg99 r=3 spectral gates rejected `0/511` nonempty rook(9) induced subgraphs;
 - triangle-split identity passed all `512` rook(9) subsets;
 - T(7) end-to-end r=3 reconstruction passed with `det(A_H'-3I)=390625`;
 - blind column search found `735` diagonal-valid columns and recovered all 6 true star columns;
 - maximum compatible clique size was `6`;
 - cadical195 SAT clique closed to exact 0/1 `A_X`;
 - T(7) Stage-A false rejects over `5242` real induced subgraphs were `G-a=0`, `G-b=0`.

READINESS VERDICT:
The R199/R216 one-command r=3 Stage-A cloud experiment is now ready with a fresh full local gate,
not merely the older R199/R200 evidence.  This is still not a proof or construction.  The next decisive
experiment is the full r=3 depth-45 measurement, keeping exact and sampled rows separated.

NEXT ACTION:
Run the primary r=3 cloud measurement, or if staying local, pursue proof-grade rooted SAT/SMS rather
than parity-only holonomy.

---

## R217 -- matching-triangle relative-permutation holonomy audited [2026-06-30]
## OUTCOME: exact S4 parity holonomy found, implemented, and measured; not a CP-SAT cost win.

ARTIFACTS:
 - script: `root_cell_matching_holonomy_audit.py`
 - updated: `root_cell_permutation_csp.py --matching-holonomy`
 - note: `ROOT_CELL_MATCHING_HOLONOMY_R217.md`
 - outputs:
   `scratchpad\root_cell_matching_holonomy_audit_r217.json`,
   `scratchpad\root_cell_permutation_csp_matching_holonomy_r217.json`

RESULT:
For every matching of three pairwise-disjoint rooted fibers `A,B,C`, the three stored R209 relative
permutations satisfy an exact holonomy parity law:
`parity(q_AB^C)+parity(q_BC^A)+parity(q_AC^B)=0 mod 2`.  Finite enumeration over `S4^3`
checked all `24^3=13824` direct-block triples; the admissible relative triples are exactly
`6912/13824`, equal to the even-parity condition, with `105` matching triples in the rooted K7-edge
fiber geometry.

VALIDATION / MEASUREMENT:
 - `python -m py_compile root_cell_permutation_csp.py root_cell_matching_holonomy_audit.py` passed.
 - `python root_cell_matching_holonomy_audit.py --json-out scratchpad\root_cell_matching_holonomy_audit_r217.json`
   returned `ok=true`, empty mismatch set, and `12` possible third q-values per ordered q-pair.
 - `python root_cell_permutation_csp.py --time-cap 60 --workers 8 --disjoint-tables --matching-holonomy --json-out scratchpad\root_cell_permutation_csp_matching_holonomy_r217.json --out scratchpad\root_cell_permutation_solution_matching_holonomy_r217.json`
   returned `UNKNOWN`, `25200` vars / `51765` constraints, `34143` conflicts / `894736` branches.

VERDICT:
Accepted as a real exact holonomy relation and optional diagnostic propagation flag.  It is only parity
level and is entailed by the direct `S4` block variables, so it does not solve the rooted CSP.  Compared
with R209 disjoint tables alone (`34799` conflicts / `756900` branches), conflicts improve slightly but
branch count worsens; do not put `--matching-holonomy` in the default path.

NEXT ACTION:
Do not spend more cycles on parity-only holonomy.  Either derive a richer full-permutation cycle relation,
move R206/R208 to proof-logging SAT, or run the full-gate + r=3 cloud measurement with sufficient wall time.

---

## R216 -- readiness verdict refreshed after R213-R215 [2026-06-30]
## OUTCOME: runnable experiment remains ready-with-caveats; no proof/construction.

ARTIFACTS:
 - note: `READINESS_R216.md`
 - wrapper manifest: `scratchpad\r3_stagea_dry_r216_manifest.json`
 - smoke stats: `scratchpad\r3_slice_smoke_r216_stats.json`

VERIFICATION:
 - Compile check passed:
   `python -m py_compile lou_murin_hminus_audit.py root_cell_coset_csp.py root_cell_class_projection_csp.py root_cell_permutation_csp.py root_cell_disjoint_table_audit.py`
 - `python s3_cloud_r3_stagea.py --dry-run --target-depth 12 --node-budget 4000 --time-cap 20 --level-cap 200 --out-dir scratchpad\r3_stagea_dry_r216 --manifest-out scratchpad\r3_stagea_dry_r216_manifest.json`
   emitted the expected `--gate` then `--slice` commands.
 - Full `python s3_slice_harness.py --gate` exceeded the 124s command cap; escaped process `43892`
   was identified as `s3_slice_harness.py --gate` and stopped.  Therefore R216 does NOT claim a fresh
   full green gate; the last full green gate remains the R199/R200 evidence.
 - Bounded no-gate smoke:
   `python s3_slice_harness.py --slice --target-depth 7 --node-budget 1000 --time-cap 30 --level-cap 500 --stats-out scratchpad\r3_slice_smoke_r216_stats.json`
   passed with `N1..N7=1,2,4,9,21,62,208`, `expanded=307`, all prune counters `0`, no flags, wall `0.53s`.

READINESS VERDICT:
Ready as a runnable experiment, not ready as a proof.  The R199 r=3 cloud wrapper is one-command
runnable and dry-run verified, and the shallow generator smoke remains stable.  Before a paid/decisive
cloud run, rerun the full soundness gate with a longer cap on the target machine.  The decisive unknowns
remain the deep spectral-collapse curve and proof-grade rooted SAT/SMS.

NEXT ACTION:
Either run the full gate + r=3 cloud measurement with sufficient wall time, or continue rooted work at
actual relative-permutation cycle/holonomy/proof-logging level.  Do not spend more cycles on coarse
class projections alone.

---

## R215 -- six-class `(right D8 coset, parity)` projection tested; no obstruction [2026-06-30]
## OUTCOME: stronger macro projection than R214 is constructively satisfiable; close this projection route.

ARTIFACTS:
 - script: `root_cell_class_projection_csp.py`
 - note: `ROOT_CELL_CLASS_PROJECTION_R215.md`
 - outputs:
   `scratchpad\root_cell_class_projection_csp_r215_recheck.json`,
   `scratchpad\root_cell_class_projection_csp_class1_r215.json`

RESULT:
The projected R209 local relation has six classes of size `4`, `10368` allowed arity-7 tuples out of
`6^7=279936`, and each exact relative permutation has `6` compatible class-pairs.  However the unsliced
projection is constructively satisfiable: assign every directed block to class `0` (right `D8` coset 0,
even parity).  A nonzero fixed-class CP-SAT slice spent 30s in table/presolve and returned `UNKNOWN`
with no search branches, so that table encoding is not useful as a sliced macro solver.

VERDICT:
No obstruction.  The route "project S4 to a small class label" is now tested at 3 classes and 6 classes;
both are too weak.  Future rooted holonomy work must keep actual relative permutations or a richer
quotient that can rule out the all-square macro shadow.

NEXT ACTION:
Return to actual relative-permutation cycle/holonomy equations or proof-logging SAT for the R209/R214
rooted formulation; do not spend more cycles on coarse class projections alone.

---

## R214 -- rooted S4 coset macro-projection audited and measured [2026-06-30]
## OUTCOME: new exact necessary macro layer for the R204/R209 permutation CSP; not an obstruction.

ARTIFACTS:
 - script: `root_cell_coset_csp.py`
 - updated: `root_cell_permutation_csp.py --coset-projection`
 - note: `ROOT_CELL_COSET_PROJECTION_R214.md`
 - outputs:
   `scratchpad\root_cell_coset_csp_r214.json`,
   `scratchpad\root_cell_coset_csp_coset0_r214.json`,
   `scratchpad\root_cell_coset_csp_coset1_r214.json`,
   `scratchpad\root_cell_coset_csp_coset2_r214.json`,
   `scratchpad\root_cell_permutation_csp_coset_projection_r214.json`,
   `scratchpad\root_cell_permutation_csp_disjoint_coset_r214.json`

DERIVATION:
Project each directed `S4` block to its right coset modulo the square subgroup `D8 <= S4`.  The R209
disjoint residual table projects to the exact rule:
 - square direct block => all three common relative permutations are square;
 - nonsquare direct block => exactly `0` or `2` of the three common relative permutations are square.
Because `P_BC^-1 P_AC` is square iff `P_AC` and `P_BC` have the same right `D8` coset, this is a
3-colour necessary CSP on the directed Kneser block arcs.

VALIDATION / RESULTS:
 - `python -m py_compile root_cell_permutation_csp.py root_cell_coset_csp.py root_cell_disjoint_table_audit.py` passed.
 - Finite audit: `576` pairwise composition checks passed; R209 table projection is exactly
   square-direct `72` rows with three square relatives and nonsquare-direct `288+96` rows with `0/2`.
 - Standalone macro CSP is `OPTIMAL` in `~0.24s`; all three fixed-coset slices are also satisfiable.
   Therefore this macro projection is not a nonexistence obstruction.
 - Full CP-SAT measurements:
   `--coset-projection` alone is worse than R204 (`UNKNOWN`, `319254` conflicts / `1519082` branches).
   `--disjoint-tables --coset-projection` remains `UNKNOWN` but changes R209's profile from
   `34799` conflicts / `756900` branches to `50442` conflicts / `617908` branches.

VERDICT:
Accepted as a sound macro audit and optional CP-SAT propagation layer.  Do not replace R209 with it.
It may be useful with `--disjoint-tables` when branch count dominates, but it is not a proof-grade
breakthrough.  Next rooted target is a richer intermediate relation or genuine cycle/holonomy equation.

NEXT ACTION:
Continue extracting structural constraints from the R209 relative-permutation tables, aiming for a
smaller exact relation stronger than 3 cosets but cheaper than full `S4`, or a certified cycle relation.

---

## R213 -- Lou-Murin order-9 forbidden motif audited; sound but low-yield [2026-06-30]
## OUTCOME: recovered and tested the literature-backed `srg(9,4,1,2)-e` cut; useful proof note, not a decisive cost lever.

ARTIFACTS:
 - script: `lou_murin_hminus_audit.py`
 - note: `LOU_MURIN_HMINUS_R213.md`

CLAIM:
Lou-Murin Section 2 uses the Wilbrink-Brouwer counting lemma to show that, in a hypothetical
`srg(99,14,1,2)`, a subgraph isomorphic to `H-e` for `H=srg(9,4,1,2)` forces the missing edge and
the nine vertices induce `H`. Hence an induced `H-e` is forbidden. This is parameter-specific to
`(99,14,1,2)`, not a generic lambda=1,mu=2 predicate.

VALIDATION / MEASUREMENT:
 - `python -m py_compile lou_murin_hminus_audit.py` passed.
 - `python lou_murin_hminus_audit.py` passed controls:
   rook9 is recognized as exact `srg(9,4,1,2)`, rook9 itself contains no induced `H-e`, rook9-minus-one
   edge is recognized, and the shipped local/spectral r=3 gates admit `H-e` (so this is not redundant).
 - `python lou_murin_hminus_audit.py --scan-defaults --max-examples 2` scanned current frontiers:
   depth 9 `1/5311`, depth 10 `8/42422`, R189 depth-11 shards 0..17 `12/129794`.

VERDICT:
Accepted as a sound forbidden induced motif and a reusable audit.  Measured hit rate is only about
`1e-4`, so do not add a naive all-9-subsets online detector to the hot path.  A bounded shallow check
or offline frontier filter is safe, but the next meaningful lever should target the rooted `Gamma_2`
matrix-square-root / S4 permutation-CSP structure rather than spend cycles on this low-yield cut.

NEXT ACTION:
Pursue a stronger rooted structural equation: audit the fixed `Gamma_2(root)` matrix equation
`X^2 + X = M`, its spectral root splits, and whether it can strengthen or certify the R204/R209
permutation-CSP surface.

---

## R212 -- R189 d10->d11 shards 16..17 completed; shards 0..17 now cover 28.13% [2026-06-30]
## OUTCOME: current R189 exact-refresh measurement advanced to eighteen-shard coverage.

ARTIFACTS:
 - note: `R3_D10_D11_R189_SHARDS_016_017_R212.md`
 - outputs:
   `scratchpad\r3_d10_to_d11_r189_stats_probe\r3_d10_to_d11_r189_shard64_exact_016.json`,
   `scratchpad\r3_d10_to_d11_r189_stats_probe\r3_d10_to_d11_r189_shard64_exact_017.json`,
   `scratchpad\r3_d10_to_d11_r189_frontiers_probe\r3_d10_to_d11_r189_shard64_exact_016_frontier.jsonl`,
   `scratchpad\r3_d10_to_d11_r189_frontiers_probe\r3_d10_to_d11_r189_shard64_exact_017_frontier.jsonl`,
   `scratchpad\r3_d10_to_d11_r189_016_017_aggregate_probe.json`,
   `scratchpad\r3_d10_to_d11_r189_000_017_aggregate_probe.json`

COMMAND:
`python .\s3_cloud_r3_d11_r189.py --skip-gate --indices 16-17 --out-dir .\scratchpad\r3_d10_to_d11_r189_stats_probe --frontier-out-dir .\scratchpad\r3_d10_to_d11_r189_frontiers_probe --aggregate-out .\scratchpad\r3_d10_to_d11_r189_016_017_aggregate_probe.json`

VALIDATION / RESULTS:
 - Source frontier SHA-256 remains
   `68241a7ace8b0b118245e088a7d3289452927955dbf030df5fe63620d5129871`.
 - Shard 16: `663 -> 6574`, wall `114.80s`; shard 17: `663 -> 6227`, wall `117.06s`.
 - Shards 16..17 loaded `1326/42422` parents and produced `12801` depth-11 children; diagnostic
   scaled `N11 ~= 409535.5`.
 - Shards 0..17 now cover `11934/42422` parents (`28.1316%`) and produce `129794` children;
   diagnostic scaled `N11 ~= 461381.0`.
 - No budget/time/sample flags.  Aggregate counters over shards 0..17:
   `expanded=141728`, `iso_dups=48552`, `canonical_parent_reject=1576457`,
   `canonical_parent_cache_hit=443758`, and all local/spectral/triangle-split prune counters `0`.
 - Fresh shard frontiers 16 and 17 scan clean under R184, R185, R186, and R189; real-witness controls
   stayed green.  The near-full scan checked `12801` fresh rows with `0` global or near-full violations.

VERDICT:
Accepted as real R189 d10->d11 refresh progress.  It remains diagnostic, not exact; exact R189 `N11`
still requires all 64 shards and a strict aggregate without `--allow-incomplete`.

NEXT ACTION:
Continue exact R189 d10->d11 refresh with shards `18-19`, or resume rooted structural work from the
R208/R209 surfaces.

---

## R211 -- R189 d10->d11 shards 14..15 completed; shards 0..15 now cover 25.01% [2026-06-30]
## OUTCOME: current R189 exact-refresh measurement advanced to sixteen-shard coverage.

ARTIFACTS:
 - note: `R3_D10_D11_R189_SHARDS_014_015_R211.md`
 - outputs:
   `scratchpad\r3_d10_to_d11_r189_stats_probe\r3_d10_to_d11_r189_shard64_exact_014.json`,
   `scratchpad\r3_d10_to_d11_r189_stats_probe\r3_d10_to_d11_r189_shard64_exact_015.json`,
   `scratchpad\r3_d10_to_d11_r189_frontiers_probe\r3_d10_to_d11_r189_shard64_exact_014_frontier.jsonl`,
   `scratchpad\r3_d10_to_d11_r189_frontiers_probe\r3_d10_to_d11_r189_shard64_exact_015_frontier.jsonl`,
   `scratchpad\r3_d10_to_d11_r189_014_015_aggregate_probe.json`,
   `scratchpad\r3_d10_to_d11_r189_000_015_aggregate_probe.json`

COMMAND:
`python .\s3_cloud_r3_d11_r189.py --skip-gate --indices 14-15 --out-dir .\scratchpad\r3_d10_to_d11_r189_stats_probe --frontier-out-dir .\scratchpad\r3_d10_to_d11_r189_frontiers_probe --aggregate-out .\scratchpad\r3_d10_to_d11_r189_014_015_aggregate_probe.json`

VALIDATION / RESULTS:
 - Source frontier SHA-256 remains
   `68241a7ace8b0b118245e088a7d3289452927955dbf030df5fe63620d5129871`.
 - Shard 14: `663 -> 7512`, wall `112.93s`; shard 15: `663 -> 7290`, wall `116.76s`.
 - Shards 14..15 loaded `1326/42422` parents and produced `14802` depth-11 children; diagnostic
   scaled `N11 ~= 473552.4`.
 - Shards 0..15 now cover `10608/42422` parents (`25.0059%`) and produce `116993` children;
   diagnostic scaled `N11 ~= 467861.7`.
 - No budget/time/sample flags.  Aggregate counters over shards 0..15:
   `expanded=127601`, `iso_dups=44847`, `canonical_parent_reject=1394079`,
   `canonical_parent_cache_hit=390927`, and all local/spectral/triangle-split prune counters `0`.
 - Fresh shard frontiers 14 and 15 scan clean under R184, R185, R186, and R189; real-witness controls
   stayed green.  The near-full scan checked `14802` fresh rows with `0` global or near-full violations.

VERDICT:
Accepted as real R189 d10->d11 refresh progress.  It remains diagnostic, not exact; exact R189 `N11`
still requires all 64 shards and a strict aggregate without `--allow-incomplete`.

NEXT ACTION:
Continue exact R189 d10->d11 refresh with shards `16-17`, or move to a structural reduction only if it
is expected to beat the current R208/R209 rooted surfaces.

---

## R210 -- intersecting-fiber table prototype audited but not hot-path viable [2026-06-30]
## OUTCOME: exact intersecting table relation exists, but CP-SAT table form spends budget in presolve and is not useful locally.

ARTIFACTS:
 - note: `ROOT_CELL_INTERSECTING_TABLES_R210.md`
 - new audit: `root_cell_intersecting_table_audit.py`
 - updated script: `root_cell_permutation_csp.py --intersecting-tables`
 - outputs:
   `scratchpad\root_cell_intersecting_table_audit_r210.json`,
   `scratchpad\root_cell_permutation_csp_intersecting_tables_probe_r210.json`,
   `scratchpad\root_cell_permutation_csp_intersecting_tables_r210.json`

VALIDATION / RESULTS:
 - `python -m py_compile .\root_cell_permutation_csp.py .\root_cell_intersecting_table_audit.py` passed.
 - The intersecting-fiber target table is exact: arity `6`, `35280` rows per target, ambient invalid
   space `24^6 = 191102976`, audit `ok=true`.
 - `--intersecting-tables` 10s probe returned `UNKNOWN` only after `38.5853s` wall, with `0` conflicts
   and `0` branches.
 - `--intersecting-tables` 60s probe also returned `UNKNOWN`, `62.9618s` wall, `0` conflicts,
   `0` branches.  Model size was `24990` vars / `51450` constraints with `630` intersecting
   relative-permutation vars and `735` table constraints.

VERDICT:
The relation is mathematically exact but the current CP-SAT extensional-table implementation is too
heavy for the hot path.  Do not scale `--intersecting-tables` unless it is decomposed into smaller
constraints or moved to a solver that handles large tables better.  No construction and no nonexistence
proof have been obtained.

NEXT ACTION:
Return to r=3 exact measurement shards or pursue a smaller decomposition of the intersecting relation.

---

## R209 -- disjoint-fiber residual table constraints audited [2026-06-30]
## OUTCOME: exact redundant CP-SAT propagation improves the R204 permutation CSP profile; still UNKNOWN.

ARTIFACTS:
 - note: `ROOT_CELL_DISJOINT_TABLES_R209.md`
 - new audit: `root_cell_disjoint_table_audit.py`
 - updated script:
   `root_cell_permutation_csp.py --disjoint-tables --block-rep {none,square,nonsquare}`
 - outputs:
   `scratchpad\root_cell_disjoint_table_audit_r209.json`,
   `scratchpad\root_cell_permutation_csp_disjoint_tables_r209.json`,
   `scratchpad\root_cell_permutation_csp_tables_square_smoke_r209.json`,
   `scratchpad\root_cell_permutation_csp_tables_square_r209.json`,
   `scratchpad\root_cell_permutation_csp_tables_nonsquare_r209.json`

VALIDATION / RESULTS:
 - `python -m py_compile .\root_cell_permutation_csp.py .\root_cell_disjoint_table_audit.py` passed.
 - Finite audit checked all `24 * 24^3 = 331776` direct/relative-permutation combinations and proved
   the residual table exactly matches the 16 disjoint-pair common-neighbour equations.
 - The table has `456` rows: square direct blocks (`8` values) allow `9` relative triples each;
   nonsquare direct blocks (`16` values) allow `24` relative triples each.
 - Unsplit `--disjoint-tables` model size: `24885` vars, `51345` constraints, including `210`
   permutation-id vars, `315` relative-permutation vars, and `630` table constraints.
 - Unsplit table model: 60s CP-SAT `UNKNOWN`, `34799` conflicts, `756900` branches.
 - R204 repaired permutation CSP without these tables was 60s `UNKNOWN`, `187506` conflicts,
   `1299396` branches, so the redundant table is a real local CP-SAT propagation improvement.
 - Table representative slices remain `UNKNOWN`: square `37216` conflicts / `881176` branches;
   nonsquare `29856` conflicts / `708547` branches.  The split is sound only as a two-case suite and
   did not improve CP-SAT over the unsplit table model locally.

VERDICT:
Accepted as an exact structural encoding improvement, not as construction/nonexistence evidence.
No construction and no nonexistence proof have been obtained.

NEXT ACTION:
Either add analogous table/relative-permutation structure for intersecting fiber pairs, or move the
R208 SAT / R209 CP-SAT formulations to proof-capable cloud tooling.

---

## R208 -- direct cardinality SAT encoding verified and measured [2026-06-30]
## OUTCOME: R206 two-slice SAT remains UNKNOWN, but `--card-encoding direct` is a verified local cost improvement.

ARTIFACTS:
 - note: `ROOT_CELL_DIRECT_CARD_R208.md`
 - new audit: `root_cell_card_encoding_audit.py`
 - updated script: `root_cell_permutation_sat.py --card-encoding {seqcounter,direct}`
 - outputs:
   `scratchpad\root_cell_card_encoding_audit_r208.json`,
   `scratchpad\root_cell_permutation_sat_direct_square_smoke_r208.json`,
   `scratchpad\root_cell_permutation_sat_direct_square_r208.json`,
   `scratchpad\root_cell_permutation_sat_direct_nonsquare_r208.json`

VALIDATION / RESULTS:
 - `python -m py_compile .\root_cell_permutation_sat.py .\root_cell_card_encoding_audit.py` passed.
 - Direct exactly-k audit exhaustively checked all `n <= 8`, all bounds, and all assignments:
   `assignments_checked=4097`, `ok=true`.
 - Per R206 representative slice, direct encoding changes CNF size from `137760` vars / `384724`
   clauses to `77280` vars / `405724` clauses.
 - `square + direct`: 60s Cadical195 `UNKNOWN`, `390037` conflicts, `857171` decisions,
   `556351116` propagations.
 - `nonsquare + direct`: 60s Cadical195 `UNKNOWN`, `410040` conflicts, `1003204` decisions,
   `513286710` propagations.
 - Compared with R206 seqcounter, direct improves square decisions `1021023 -> 857171` and conflicts
   `440053 -> 390037`; nonsquare decisions `1016005 -> 1003204` and conflicts `450026 -> 410040`.

VERDICT:
Accepted as a verified encoding/cost improvement, not as mathematical evidence for existence or
nonexistence.  Cloud SAT runs should explicitly use `--card-encoding direct` on both R206 representatives.

NEXT ACTION:
Continue with a stronger exact structural equation for the permutation CSP, or run the R206/R208 two-case
CNF on a proof-logging cloud SAT stack.

---

## R207 -- local SAT proof-toolchain and CaDiCaL variant audit [2026-06-30]
## OUTCOME: more CaDiCaL bindings are runnable, but local proof-grade UNSAT is not available.

ARTIFACTS:
 - note: `ROOT_CELL_SAT_TOOLCHAIN_R207.md`
 - new audit: `root_cell_sat_toolchain_audit.py`
 - updated script: `root_cell_permutation_sat.py --solver {cadical153,cadical195,cadical300}`
 - outputs:
   `scratchpad\root_cell_sat_toolchain_audit_r207.json`,
   `scratchpad\root_cell_permutation_sat_cadical300_square_smoke_r207.json`,
   `scratchpad\root_cell_permutation_sat_cadical300_square_r207.json`,
   `scratchpad\root_cell_permutation_sat_cadical300_nonsquare_r207.json`,
   `scratchpad\root_cell_permutation_sat_cadical153_square_probe_r207.json`

VALIDATION / RESULTS:
 - `python -m py_compile .\root_cell_sat_toolchain_audit.py .\root_cell_permutation_sat.py` passed.
 - No standalone `cadical`, `kissat`, `drat-trim`, `gratgen`, `lrat-check`, `lingeling`, or
   `cryptominisat` binary is on PATH.
 - PySAT `cadical153`, `cadical195`, and `cadical300` all support bounded solving (`conf_budget`,
   `solve_limited`) and solve a tiny UNSAT formula without proof enabled.
 - Proof-enabled child probes return empty proof lists and abnormal child return code `3221226505`,
   so local PySAT proof traces are not usable as independent certificates here.
 - Cadical300 R206 slices are both `UNKNOWN` at 60s: square `480036` conflicts / `1088797` decisions;
   nonsquare `470041` conflicts / `1083032` decisions.  This is worse than the Cadical195 R206
   decision profile.
 - Cadical153 square 15s probe is `UNKNOWN` with `130013` conflicts / `342951` decisions; no clear
   improvement signal.

VERDICT:
Accepted as a tooling/cost audit.  Keep Cadical195 as the local default; use Cadical300/153 as
cross-checks only.  Proof-grade nonexistence would require a cloud/toolchain step with proof logging
and an independent DRAT/LRAT checker.  No construction and no nonexistence proof have been obtained.

NEXT ACTION:
Look for a stronger exact structural equation/pruning condition on the R204 permutation CSP, or move
the R206 two-slice CNF to a proof-logging cloud SAT stack.

---

## R206 -- rooted block-representative SAT split audited [2026-06-30]
## OUTCOME: R205 SAT now has a proof-safe two-case block representative split; both 60s slices remain UNKNOWN.

ARTIFACTS:
 - note: `ROOT_CELL_BLOCK_REP_R206.md`
 - new audit: `root_cell_block_rep_audit.py`
 - updated script: `root_cell_permutation_sat.py --block-rep {none,square,nonsquare}`
 - outputs:
   `scratchpad\root_cell_block_rep_audit_r206.json`,
   `scratchpad\root_cell_permutation_sat_square_r206.json`,
   `scratchpad\root_cell_permutation_sat_nonsquare_r206.json`

VALIDATION / RESULTS:
 - `python -m py_compile .\root_cell_permutation_sat.py .\root_cell_block_rep_audit.py` passed.
 - Finite audit enumerated all `24` permutations in `S4` under the legal left/right `D8` square action
   on the two endpoint fibers.  It found exactly two double cosets: `square` rep `(0,1,2,3)` of size
   `8`, and `nonsquare` rep `(0,1,3,2)` of size `16`; `covered_permutations=24`, `ok=true`.
 - SAT slices add only four unit clauses to the R205 base encoding, yielding `137760` vars and
   `384724` clauses per slice.
 - `--block-rep square`: 60s Cadical195 `UNKNOWN`, `440053` conflicts, `1021023` decisions,
   `545898107` propagations.
 - `--block-rep nonsquare`: 60s Cadical195 `UNKNOWN`, `450026` conflicts, `1016005` decisions,
   `578159908` propagations.
 - Compared with unsliced R205 (`1285475` decisions at 60s), each representative slice cuts decisions
   by about 20%, but the two-slice suite is still not decisive.

VERDICT:
Accepted as a sound exhaustive SAT case split, not as a prune.  Running only one representative would
over-prune; running both covers every possible witness up to root-ball relabelling.  No construction and
no nonexistence proof have been obtained.

NEXT ACTION:
Either add proof logging / independent checking for the two representative SAT slices, or look for a
stronger exact structural equation that cuts both slices before committing cloud-scale solver time.

---

## R205 -- rooted permutation SAT thin-slice prototype built [2026-06-30]
## OUTCOME: R204 105-block S4 permutation CSP now has a bounded one-command CNF experiment; no SAT/UNSAT verdict.

ARTIFACTS:
 - note: `ROOT_CELL_PERMUTATION_SAT_R205.md`
 - new script: `root_cell_permutation_sat.py`
 - outputs:
   `scratchpad\root_cell_permutation_sat_cadical_r205.json`,
   `scratchpad\root_cell_permutation_sat_cadical_smoke_r205.json`

COMMANDS:
 - `python -m py_compile .\root_cell_permutation_sat.py`
 - `python .\root_cell_permutation_sat.py --time-cap 60 --solver cadical195 --json-out .\scratchpad\root_cell_permutation_sat_cadical_r205.json --solution-out .\scratchpad\root_cell_permutation_sat_solution_r205.json`
 - smoke after solver-safety patch:
   `python .\root_cell_permutation_sat.py --time-cap 5 --solver cadical195 --json-out .\scratchpad\root_cell_permutation_sat_cadical_smoke_r205.json --solution-out .\scratchpad\root_cell_permutation_sat_solution_smoke_r205.json`

VALIDATION / RESULTS:
 - Compile check passed.
 - CNF size: `137760` variables, `384720` clauses, `1680` permutation block variables,
   `840` row/column exactly-one equations, `15120` equality terms, `60480` AND terms, and
   `3360` compact common-neighbour pair equations.
 - Main Cadical195 bounded run: `UNKNOWN` at `60.4003s`, with `440040` conflicts,
   `1285475` decisions, `548094919` propagations, and `24853` restarts.
 - Post-patch smoke run: same encoding, `UNKNOWN` at `5.3035s`, with `40001` conflicts,
   `138237` decisions, `59344567` propagations, and `2510` restarts.
 - A Glucose attempt did not return within the outer command budget and is discarded as evidence.
   The script is now narrowed to Cadical195, the backend that obeyed the bounded polling loop here.
 - SAT models reconstruct and verify the full `srg(99,14,1,2)` before any solution is written.
   UNSAT from this PySAT prototype would still not be proof-grade without proof logging and
   independent checking.

VERDICT:
Accepted as a runnable SAT thin-slice for the R204 rooted permutation formulation, not as a solution.
No construction and no nonexistence proof have been obtained.

NEXT ACTION:
Make the R204/R205 encoding proof-grade (proof-logging SAT/SMS backend plus independent checker), add
sound rooted symmetry breaking, or return to exact R189 r=3 measurement shards if structural SAT work
does not move.

---

## R204 -- rooted fiber-permutation formulation built and audited [2026-06-30]
## OUTCOME: R202 free-edge surface reduced to a 105-block S4 permutation CSP; no SAT/UNSAT verdict.

ARTIFACTS:
 - note: `ROOT_CELL_FIBER_PERMUTATION_R204.md`
 - new scripts:
   `root_cell_fiber_permutation.py`,
   `root_cell_permutation_formula_audit.py`,
   `root_cell_permutation_csp.py`
 - updated model: `root_cell_cpsat.py --fiber-permutation`
 - outputs:
   `scratchpad\root_cell_fiber_permutation_r204.json`,
   `scratchpad\root_cell_cpsat_rook9_fiberperm_r204.json`,
   `scratchpad\root_cell_cpsat_srg99_fiberperm_r204.json`,
   `scratchpad\root_cell_cpsat_srg99_fiberperm_nocommute_r204.json`,
   `scratchpad\root_cell_permutation_formula_audit_r204.json`,
   `scratchpad\root_cell_permutation_csp_r204_repaired.json`,
   `scratchpad\root_cell_permutation_csp_symseed_r204.json`

LEMMA:
Within each rooted far-cell fiber, the four free-neighbour sets are pairwise disjoint.  For k=14,
`4*(k-4)=40` equals the number of vertices in the ten disjoint fibers, so every disjoint `4x4`
fiber block is a permutation matrix.  Thus the rooted free graph is determined by `105` permutations
in `S4`, one per edge of `K(7,2)`.

VALIDATION / RESULTS:
 - `python -m py_compile .\root_cell_cpsat.py .\root_cell_fiber_permutation.py .\root_cell_permutation_csp.py .\root_cell_permutation_formula_audit.py` passed.
 - Real-witness checks: rook(9) all roots pass vacuously; BvLS(243) roots `0,1,2` pass the general
   same-fiber free-neighbour disjointness check.  BvLS block profile is not a permutation matrix, as
   expected because the k=14 covering-count specialization does not apply to k=22.
 - k=4 reduced rooted CP-SAT with `--fiber-permutation` reconstructs rook(9).
 - Independent formula audit: `30` random permutation assignments, `104580` far pairs checked, compact
   equality-count formula exactly matched direct full common-neighbour counts.
 - R204 added `840` block row/column equations to the R202 free-edge CP-SAT surface.  Bounded k=14 run:
   `UNKNOWN` at 60s, conflicts `161`, branches `293774`; mild profile improvement over R202, not a
   verdict.  No-commute counterpart also `UNKNOWN`.
 - New permutation CSP size: `840` int vars, `23520` bool vars, `50715` constraints, `3360` pair
   equations.  Bounded 60s run is `UNKNOWN` (`187506` conflicts, `1299396` branches).  Optional
   symmetry-seeded diagnostic is also `UNKNOWN`.
 - IMPORTANT: an earlier draft permutation CSP omitted endpoint-fiber common neighbours and returned
   `INFEASIBLE`; that was an invalid overconstraint and must not be used as evidence.

VERDICT:
Accepted as a genuine rooted structural reduction and exact formulation, not as a solution.  The current
best structural target is now a proof-logged SAT/SMS encoding of the 105-block `S4` permutation CSP with
sound symmetry breaking.

NEXT ACTION:
Build a purpose-specific SAT/SMS encoding for the R204 permutation CSP, or return to exact R189 r=3
measurement shards only if no structural encoding work is being attempted.

---

## R203 -- R189 d10->d11 shards 12..13 completed; shards 0..13 now cover 21.88% [2026-06-30]
## OUTCOME: current R189 exact-refresh measurement advanced to fourteen-shard coverage.

ARTIFACTS:
 - note: `R3_D10_D11_R189_SHARDS_012_013_R203.md`
 - outputs:
   `scratchpad\r3_d10_to_d11_r189_stats_probe\r3_d10_to_d11_r189_shard64_exact_012.json`,
   `scratchpad\r3_d10_to_d11_r189_stats_probe\r3_d10_to_d11_r189_shard64_exact_013.json`,
   `scratchpad\r3_d10_to_d11_r189_frontiers_probe\r3_d10_to_d11_r189_shard64_exact_012_frontier.jsonl`,
   `scratchpad\r3_d10_to_d11_r189_frontiers_probe\r3_d10_to_d11_r189_shard64_exact_013_frontier.jsonl`,
   `scratchpad\r3_d10_to_d11_r189_012_013_aggregate_probe.json`,
   `scratchpad\r3_d10_to_d11_r189_000_013_aggregate_probe.json`

COMMAND:
`python .\s3_cloud_r3_d11_r189.py --skip-gate --indices 12-13 --out-dir .\scratchpad\r3_d10_to_d11_r189_stats_probe --frontier-out-dir .\scratchpad\r3_d10_to_d11_r189_frontiers_probe --aggregate-out .\scratchpad\r3_d10_to_d11_r189_012_013_aggregate_probe.json`

VALIDATION / RESULTS:
 - Source frontier SHA-256 remains
   `68241a7ace8b0b118245e088a7d3289452927955dbf030df5fe63620d5129871`.
 - Shard 12: `663 -> 6819`, wall `71.25s`; shard 13: `663 -> 7184`, wall `69.91s`.
 - Shards 12..13 loaded `1326/42422` parents and produced `14003` depth-11 children; diagnostic scaled
   `N11 ~= 447990.4`.
 - Shards 0..13 now cover `9282/42422` parents (`21.8802%`) and produce `102191` children; diagnostic
   scaled `N11 ~= 467048.8`.
 - No budget/time/sample flags.  Aggregate counters over shards 0..13:
   `expanded=111473`, `iso_dups=39668`, `canonical_parent_reject=1216289`,
   `canonical_parent_cache_hit=340131`, and all local/spectral/triangle-split prune counters `0`.
 - Fresh shard frontiers 12 and 13 scan clean under R184, R185, R186, and R189; real-witness controls
   stayed green.  The near-full scan checked `14003` fresh rows with `0` global or near-full violations.

VERDICT:
Accepted as real R189 d10->d11 refresh progress.  It remains diagnostic, not exact; exact R189 `N11`
still requires all 64 shards and a strict aggregate without `--allow-incomplete`.

NEXT ACTION:
Continue exact R189 d10->d11 refresh with shards `14-15`, or switch to the R202 reduced rooted
free-graph SAT/SMS encoding for structural work.

---

## R202 -- rooted forced/free split ported into CP-SAT variable reduction [2026-06-30]
## OUTCOME: exact rooted model surface shrank; still no construction or UNSAT.

ARTIFACTS:
 - note: `ROOT_CELL_FORCED_FREE_R202.md`
 - new validator: `root_cell_forced_free.py`
 - updated model: `root_cell_cpsat.py --free-edge-vars`
 - outputs:
   `scratchpad\root_cell_forced_free_r202.json`,
   `scratchpad\root_cell_cpsat_rook9_freevars_r202.json`,
   `scratchpad\root_cell_cpsat_rook9_default_r202.json`,
   `scratchpad\root_cell_cpsat_srg99_freevars_r202.json`,
   `scratchpad\root_cell_cpsat_srg99_freevars_nocommute_r202.json`

VALIDATION / RESULTS:
 - `python -m py_compile .\root_cell_cpsat.py .\root_cell_forced_free.py` passed.
 - The forced/free `Gamma_2(root)` split was validated on rook(9) all 9 roots and BvLS(243)
   roots `0,1,2`, with no violations.  For srg99 it forces `84` far C4 edges and
   `1722` far nonedges, leaving `1680` genuine free edge candidates; the free graph is
   forced 10-regular with `420` edges and `140` all-free far triangles.
 - Reduced k=4 rooted CP-SAT reconstructs rook(9) with `edge_vars=0`, `forced_edges=4`,
   and `forced_nonedges=2`; default k=4 rooted CP-SAT still reconstructs rook(9).
 - Model-size audit at k=14 with commutation:
   raw R141 surface `3486` edge vars, `289338` total vars, `294084` constraints;
   forced/free surface `1680` edge vars, `67201` total vars, `73752` constraints.
 - Bounded srg99 reduced probes are still only `UNKNOWN`:
   with commutation, 60s, `conflicts=220`, `branches=304020`;
   without commutation, 60s, `conflicts=288`, `branches=492979`.

VERDICT:
Accepted as a real exact encoding reduction, not as a solver proof.  The CP-SAT status remains
`UNKNOWN`, and the search profile is mixed, but the rooted formulation now exposes the correct
1,680-variable free-edge surface for a purpose-built SAT/SMS/Traces or exact-cover encoding.

NEXT ACTION:
Do not grind generic CP-SAT `UNKNOWN` runs.  Either build the specialized free-graph SAT/SMS encoding
on the 1,680 candidate edges, or resume exact R189 r=3 measurement shards while keeping the reduced
rooted model as the next structural target.

---

## R201 -- R189 d10->d11 shards 10..11 completed; shards 0..11 now cover 18.75% [2026-06-30]
## OUTCOME: current R189 exact-refresh measurement advanced to twelve-shard coverage.

ARTIFACTS:
 - note: `R3_D10_D11_R189_SHARDS_010_011_R201.md`
 - outputs:
   `scratchpad\r3_d10_to_d11_r189_stats_probe\r3_d10_to_d11_r189_shard64_exact_010.json`,
   `scratchpad\r3_d10_to_d11_r189_stats_probe\r3_d10_to_d11_r189_shard64_exact_011.json`,
   `scratchpad\r3_d10_to_d11_r189_frontiers_probe\r3_d10_to_d11_r189_shard64_exact_010_frontier.jsonl`,
   `scratchpad\r3_d10_to_d11_r189_frontiers_probe\r3_d10_to_d11_r189_shard64_exact_011_frontier.jsonl`,
   `scratchpad\r3_d10_to_d11_r189_010_011_aggregate_probe.json`,
   `scratchpad\r3_d10_to_d11_r189_000_011_aggregate_probe.json`

COMMAND:
`python .\s3_cloud_r3_d11_r189.py --skip-gate --indices 10-11 --out-dir .\scratchpad\r3_d10_to_d11_r189_stats_probe --frontier-out-dir .\scratchpad\r3_d10_to_d11_r189_frontiers_probe --aggregate-out .\scratchpad\r3_d10_to_d11_r189_010_011_aggregate_probe.json`

VALIDATION / RESULTS:
 - Source frontier SHA-256 remains
   `68241a7ace8b0b118245e088a7d3289452927955dbf030df5fe63620d5129871`.
 - Shard 10: `663 -> 7320`, wall `71.85s`; shard 11: `663 -> 7631`, wall `69.40s`.
 - Shards 10..11 loaded `1326/42422` parents and produced `14951` depth-11 children; diagnostic scaled
   `N11 ~= 478319.2`.
 - Shards 0..11 now cover `7956/42422` parents (`18.7544%`) and produce `88188` children; diagnostic
   scaled `N11 ~= 470225.2`.
 - No budget/time/sample flags.  Aggregate counters over shards 0..11:
   `expanded=96144`, `iso_dups=33054`, `canonical_parent_reject=1040867`,
   `canonical_parent_cache_hit=290280`, and all local/spectral/triangle-split prune counters `0`.
 - Fresh shard frontiers 10 and 11 scan clean under R184, R185, R186, and R189; real-witness controls
   stayed green.

VERDICT:
Accepted as real R189 d10->d11 refresh progress.  It remains diagnostic, not exact; exact R189 `N11`
still requires all 64 shards and a strict aggregate without `--allow-incomplete`.

NEXT ACTION:
Continue exact R189 d10->d11 refresh with shards `12-13`, or pivot only for a clearly stronger
structural lever than the exhausted R192-R194 aggregate/column-shadow family.

---

## R200 -- integrated predicate replay extended to BvLS real-witness samples [2026-06-30]
## OUTCOME: the current lambda=1,mu=2 local/completion predicate bundle has a larger real-witness no-overprune check.

ARTIFACTS:
 - script: `s3_integrated_predicate_replay.py`
 - output: `scratchpad\s3_integrated_predicate_replay_r200.json`

QUESTION:
The production `PartialGraph` is specialized to srg99 (`v=99,k=14`), so a full BvLS replay through that
class would be meaningless because BvLS has degree 22.  Can the same predicate formulas be replayed with
the real host parameters on known lambda=1,mu=2 witnesses?

VALIDATION / RESULTS:
 - `python -m py_compile .\s3_integrated_predicate_replay.py` passed.
 - `python .\s3_integrated_predicate_replay.py --bvls-samples 200 --triangle-samples 100 --max-size 30 --json-out .\scratchpad\s3_integrated_predicate_replay_r200.json`
   passed with `ok=true`.
 - Rook(9) exhaustive order replay: `362880/362880` accepted, `0` violations.
 - BvLS(243) sampled induced-order replay: `200` random orders, subset sizes `0..30`, `0` violations.
 - BvLS triangle-split identity sample: `100` random subsets, `0` violations.
 - Predicates covered together in the replay: degree caps; lambda/mu common-neighbour caps; pair
   lower-closure; lambda=1 neighbourhood matching-completion; outside-degree moment; R189 near-full
   subset moment with remove<=2; triangle counter and sampled triangle-split identities.

VERDICT:
Accepted as a correctness-strengthening validation harness.  It does not add a pruning predicate or solve
the problem, but it reduces the risk that the current Stage-A hot path is silently over-pruning real
lambda=1,mu=2 witnesses.  The BvLS check is sampled, not exhaustive; rook(9) remains the exhaustive
small witness.

NEXT ACTION:
Keep this replay as part of future predicate audits whenever a new local/completion predicate is added.
Next meaningful work must either push the decisive cloud measurement, find a genuinely new structural
cut, or extract obstruction information from deeper failed/surviving slices.

---

## R199 -- r=3 Stage-A cloud wrapper added and exact-smoke validated [2026-06-30]
## OUTCOME: the R43/R44/R45 45-vertex Stage-A measurement is now one-command runnable with a built-in gate.

ARTIFACTS:
 - script: `s3_cloud_r3_stagea.py`
 - smoke outputs:
   `scratchpad\r3_stagea_smoke_r199\r3_stagea_d7_root_stats.json`,
   `scratchpad\r3_stagea_smoke_r199\r3_frontier_d7.jsonl`,
   `scratchpad\r3_stagea_smoke_r199\r3_stagea_d7_aggregate.json`,
   `scratchpad\r3_stagea_smoke_r199\r3_stagea_d8_shard000_of_002_stats.json`,
   `scratchpad\r3_stagea_smoke_r199\r3_stagea_d8_shard001_of_002_stats.json`,
   `scratchpad\r3_stagea_smoke_r199\r3_stagea_d8_sharded_aggregate.json`
 - dry-run manifests:
   `scratchpad\r3_stagea_cloud_dryrun_r199b\r3_stagea_d45_root_manifest.json`,
   `scratchpad\r3_stagea_cloud_dryrun_r199b\r3_stagea_d8_shard001_of_002_manifest.json`

COMMANDS / VALIDATION:
 - `python -m py_compile .\s3_cloud_r3_stagea.py .\s3_slice_harness.py .\s3_run_shards.py .\s3_aggregate_shards.py .\s3_merge_frontiers.py .\s3_cloud_r3_d11_r189.py` passed.
 - `python .\s3_slice_harness.py --gate` passed live: rook(9) replay accepted all `362880/362880`
   vertex orders; rook(9) spectral false rejects `0/511`; rook(9) triangle-split identities
   `512/512`; T(7) r=3 CRS reconstruction exact; T(7) Stage-A false rejects `0/5242`.
 - Full cloud dry run:
   `python .\s3_cloud_r3_stagea.py --dry-run --out-dir .\scratchpad\r3_stagea_cloud_dryrun_r199b`
   emits exactly two commands: the gate, then an unseeded `s3_slice_harness.py --slice` at
   `--target-depth 45 --node-budget 200000000 --time-cap 86400 --level-cap 2000000` with stats output.
   The wrapper intentionally never passes `--seed-triangle`.
 - Root smoke:
   `python .\s3_cloud_r3_stagea.py --skip-gate --target-depth 7 --node-budget 10000 --time-cap 60 --level-cap 10000 --out-dir .\scratchpad\r3_stagea_smoke_r199 --frontier-out .\scratchpad\r3_stagea_smoke_r199\r3_frontier_d7.jsonl`
   reproduced exact `N1..N7 = 1,2,4,9,21,62,208`, no budget/time/sample flags, and wrote a complete
   depth-7 frontier.
 - Strict aggregate:
   `python .\s3_aggregate_shards.py .\scratchpad\r3_stagea_smoke_r199\r3_stagea_d7_root_stats.json --expect 7=208 --out .\scratchpad\r3_stagea_smoke_r199\r3_stagea_d7_aggregate.json`
   marked depths 1..7 exact and passed `7=208`.
 - Distributed smoke from the new d7 frontier:
   wrapper shard `0/2` produced `499` depth-8 children; shard `1/2` produced `417`.
   Strict aggregate
   `python .\s3_aggregate_shards.py .\scratchpad\r3_stagea_smoke_r199\r3_stagea_d8_shard000_of_002_stats.json .\scratchpad\r3_stagea_smoke_r199\r3_stagea_d8_shard001_of_002_stats.json --expect 8=916 --out .\scratchpad\r3_stagea_smoke_r199\r3_stagea_d8_sharded_aggregate.json`
   marked depths 7 and 8 exact and passed `8=916`.

VERDICT:
Accepted as a real readiness repair.  The primary R43 structural switch is now operationally consolidated:
`s3_cloud_r3_stagea.py` is the one-command entry point for the r=3 / 45-vertex Stage-A cloud measurement,
running the soundness gate first by default and producing auditable stats/manifests.  This is not a
construction or nonexistence proof.  It does not measure the deep `k~34..45` spectral-collapse curve; it
only proves that the current measurement path is runnable, unseeded, and exact on shallow root/shard
controls.

NEXT ACTION:
For decisive evidence, run the R199 wrapper on a cloud node from the unseeded root, or use an R48+
complete prefix frontier and run distributed wrapper shards until exact rows approach the first
spectral-bite range.  In parallel, continue only structural probes that can reduce this measurement cost
or prove a new safe pruning predicate.

---

## R198 -- R189 d10->d11 shards 8..9 completed; shards 0..9 now cover 15.63% [2026-06-30]
## OUTCOME: current R189 exact-refresh measurement advanced to ten-shard coverage.

ARTIFACTS:
 - note: `R3_D10_D11_R189_SHARDS_008_009_R198.md`
 - outputs:
   `scratchpad\r3_d10_to_d11_r189_stats_probe\r3_d10_to_d11_r189_shard64_exact_008.json`,
   `scratchpad\r3_d10_to_d11_r189_stats_probe\r3_d10_to_d11_r189_shard64_exact_009.json`,
   `scratchpad\r3_d10_to_d11_r189_frontiers_probe\r3_d10_to_d11_r189_shard64_exact_008_frontier.jsonl`,
   `scratchpad\r3_d10_to_d11_r189_frontiers_probe\r3_d10_to_d11_r189_shard64_exact_009_frontier.jsonl`,
   `scratchpad\r3_d10_to_d11_r189_008_009_aggregate_probe.json`,
   `scratchpad\r3_d10_to_d11_r189_000_009_aggregate_probe.json`

COMMAND:
`python .\s3_cloud_r3_d11_r189.py --skip-gate --indices 8-9 --out-dir .\scratchpad\r3_d10_to_d11_r189_stats_probe --frontier-out-dir .\scratchpad\r3_d10_to_d11_r189_frontiers_probe --aggregate-out .\scratchpad\r3_d10_to_d11_r189_008_009_aggregate_probe.json`

VALIDATION / RESULTS:
 - Source frontier SHA-256 remains
   `68241a7ace8b0b118245e088a7d3289452927955dbf030df5fe63620d5129871`.
 - Shard 8: `663 -> 6609`, wall `69.58s`; shard 9: `663 -> 7234`, wall `71.05s`.
 - Shards 8..9 loaded `1326/42422` parents and produced `13843` depth-11 children; diagnostic scaled
   `N11 ~= 442871.6`.
 - Shards 0..9 now cover `6630/42422` parents (`15.6287%`) and produce `73237` children; diagnostic
   scaled `N11 ~= 468606.3`.
 - No budget/time/sample flags.  Aggregate counters over shards 0..9:
   `expanded=79867`, `iso_dups=26303`, `canonical_parent_reject=868828`,
   `canonical_parent_cache_hit=242093`, and all local/spectral/triangle-split prune counters `0`.
 - Fresh shard frontiers 8 and 9 scan clean under R184, R185, R186, and R189; real-witness controls
   stayed green.

VERDICT:
Accepted as real R189 d10->d11 refresh progress.  It remains diagnostic, not exact; exact R189 `N11`
still requires all 64 shards and a strict aggregate without `--allow-incomplete`.

NEXT ACTION:
Continue exact R189 d10->d11 refresh with shards `10-11`, or pivot only for a clearly stronger
structural lever than the exhausted R192-R194 aggregate/column-shadow family.

---

## R197 -- R189 d10->d11 shards 6..7 completed; shards 0..7 now cover 12.50% [2026-06-30]
## OUTCOME: current R189 exact-refresh measurement advanced to one-eighth shard coverage.

ARTIFACTS:
 - note: `R3_D10_D11_R189_SHARDS_006_007_R197.md`
 - outputs:
   `scratchpad\r3_d10_to_d11_r189_stats_probe\r3_d10_to_d11_r189_shard64_exact_006.json`,
   `scratchpad\r3_d10_to_d11_r189_stats_probe\r3_d10_to_d11_r189_shard64_exact_007.json`,
   `scratchpad\r3_d10_to_d11_r189_frontiers_probe\r3_d10_to_d11_r189_shard64_exact_006_frontier.jsonl`,
   `scratchpad\r3_d10_to_d11_r189_frontiers_probe\r3_d10_to_d11_r189_shard64_exact_007_frontier.jsonl`,
   `scratchpad\r3_d10_to_d11_r189_006_007_aggregate_probe.json`,
   `scratchpad\r3_d10_to_d11_r189_000_007_aggregate_probe.json`

COMMAND:
`python .\s3_cloud_r3_d11_r189.py --skip-gate --indices 6-7 --out-dir .\scratchpad\r3_d10_to_d11_r189_stats_probe --frontier-out-dir .\scratchpad\r3_d10_to_d11_r189_frontiers_probe --aggregate-out .\scratchpad\r3_d10_to_d11_r189_006_007_aggregate_probe.json`

VALIDATION / RESULTS:
 - Source frontier SHA-256 remains
   `68241a7ace8b0b118245e088a7d3289452927955dbf030df5fe63620d5129871`.
 - Shard 6: `663 -> 7489`, wall `69.73s`; shard 7: `663 -> 7648`, wall `70.15s`.
 - Shards 6..7 loaded `1326/42422` parents and produced `15137` depth-11 children; diagnostic scaled
   `N11 ~= 484269.8`.
 - Shards 0..7 now cover `5304/42422` parents (`12.5029%`) and produce `59394` children; diagnostic
   scaled `N11 ~= 475040.0`.
 - No budget/time/sample flags.  Aggregate counters over shards 0..7:
   `expanded=64698`, `iso_dups=21512`, `canonical_parent_reject=695359`,
   `canonical_parent_cache_hit=194594`, and all local/spectral/triangle-split prune counters `0`.
 - Fresh shard frontiers 6 and 7 scan clean under R184, R185, R186, and R189; real-witness controls
   stayed green.

VERDICT:
Accepted as real R189 d10->d11 refresh progress.  It remains diagnostic, not exact; exact R189 `N11`
still requires all 64 shards and a strict aggregate without `--allow-incomplete`.

NEXT ACTION:
Continue exact R189 d10->d11 refresh with shards `8-9`, or pivot only for a clearly stronger structural
lever than the exhausted R192-R194 aggregate/column-shadow family.

---

## R196 -- R189 d10->d11 shards 4..5 completed; shards 0..5 now cover 9.38% [2026-06-30]
## OUTCOME: current R189 exact-refresh measurement advanced again with clean frontiers.

ARTIFACTS:
 - note: `R3_D10_D11_R189_SHARDS_004_005_R196.md`
 - outputs:
   `scratchpad\r3_d10_to_d11_r189_stats_probe\r3_d10_to_d11_r189_shard64_exact_004.json`,
   `scratchpad\r3_d10_to_d11_r189_stats_probe\r3_d10_to_d11_r189_shard64_exact_005.json`,
   `scratchpad\r3_d10_to_d11_r189_frontiers_probe\r3_d10_to_d11_r189_shard64_exact_004_frontier.jsonl`,
   `scratchpad\r3_d10_to_d11_r189_frontiers_probe\r3_d10_to_d11_r189_shard64_exact_005_frontier.jsonl`,
   `scratchpad\r3_d10_to_d11_r189_004_005_aggregate_probe.json`,
   `scratchpad\r3_d10_to_d11_r189_000_005_aggregate_probe.json`

COMMAND:
`python .\s3_cloud_r3_d11_r189.py --skip-gate --indices 4-5 --out-dir .\scratchpad\r3_d10_to_d11_r189_stats_probe --frontier-out-dir .\scratchpad\r3_d10_to_d11_r189_frontiers_probe --aggregate-out .\scratchpad\r3_d10_to_d11_r189_004_005_aggregate_probe.json`

VALIDATION / RESULTS:
 - Source frontier SHA-256 remains
   `68241a7ace8b0b118245e088a7d3289452927955dbf030df5fe63620d5129871`.
 - Shard 4: `663 -> 7672`, wall `69.98s`; shard 5: `663 -> 7016`, wall `68.77s`.
 - Shards 4..5 loaded `1326/42422` parents and produced `14688` depth-11 children; diagnostic scaled
   `N11 ~= 469905.2`.
 - Shards 0..5 now cover `3978/42422` parents (`9.3772%`) and produce `44257` children; diagnostic
   scaled `N11 ~= 471963.4`.
 - No budget/time/sample flags.  Aggregate counters over shards 0..5:
   `expanded=48235`, `iso_dups=16114`, `canonical_parent_reject=521600`,
   `canonical_parent_cache_hit=146919`, and all local/spectral/triangle-split prune counters `0`.
 - Fresh shard frontiers 4 and 5 scan clean under R184, R185, R186, and R189; real-witness controls
   stayed green.

VERDICT:
Accepted as real R189 d10->d11 refresh progress.  It remains diagnostic, not exact; exact R189 `N11`
still requires all 64 shards and a strict aggregate without `--allow-incomplete`.

NEXT ACTION:
Continue exact R189 d10->d11 refresh with shards `6-7`, or pivot only for a clearly stronger structural
lever than the exhausted R192-R194 aggregate/column-shadow family.

---

## R195 -- R189 d10->d11 shards 2..3 completed; shards 0..3 now cover 6.25% [2026-06-30]
## OUTCOME: current R189 exact-refresh measurement advanced with clean frontiers.

ARTIFACTS:
 - note: `R3_D10_D11_R189_SHARDS_002_003_R195.md`
 - outputs:
   `scratchpad\r3_d10_to_d11_r189_stats_probe\r3_d10_to_d11_r189_shard64_exact_002.json`,
   `scratchpad\r3_d10_to_d11_r189_stats_probe\r3_d10_to_d11_r189_shard64_exact_003.json`,
   `scratchpad\r3_d10_to_d11_r189_frontiers_probe\r3_d10_to_d11_r189_shard64_exact_002_frontier.jsonl`,
   `scratchpad\r3_d10_to_d11_r189_frontiers_probe\r3_d10_to_d11_r189_shard64_exact_003_frontier.jsonl`,
   `scratchpad\r3_d10_to_d11_r189_002_003_aggregate_probe.json`,
   `scratchpad\r3_d10_to_d11_r189_000_003_aggregate_probe.json`

COMMAND:
`python .\s3_cloud_r3_d11_r189.py --skip-gate --indices 2-3 --out-dir .\scratchpad\r3_d10_to_d11_r189_stats_probe --frontier-out-dir .\scratchpad\r3_d10_to_d11_r189_frontiers_probe --aggregate-out .\scratchpad\r3_d10_to_d11_r189_002_003_aggregate_probe.json`

VALIDATION / RESULTS:
 - Source frontier SHA-256 remains
   `68241a7ace8b0b118245e088a7d3289452927955dbf030df5fe63620d5129871`.
 - Shard 2: `663 -> 7351`, wall `68.99s`; shard 3: `663 -> 7394`, wall `70.33s`.
 - Shards 2..3 loaded `1326/42422` parents and produced `14745` depth-11 children; diagnostic scaled
   `N11 ~= 471728.8`.
 - Shards 0..3 now cover `2652/42422` parents (`6.2515%`) and produce `29569` children; diagnostic
   scaled `N11 ~= 472992.5`.
 - No budget/time/sample flags.  Aggregate counters over shards 0..3:
   `expanded=32221`, `iso_dups=10960`, `canonical_parent_reject=349669`,
   `canonical_parent_cache_hit=100011`, and all local/spectral/triangle-split prune counters `0`.
 - Fresh shard frontiers 2 and 3 scan clean under R184, R185, R186, and R189; real-witness controls
   stayed green.  Compile sweep including the new R194 probe passed.

VERDICT:
Accepted as real R189 d10->d11 refresh progress.  It remains diagnostic, not exact; exact R189 `N11`
still requires all 64 shards and a strict aggregate without `--allow-incomplete`.

NEXT ACTION:
Continue exact R189 d10->d11 refresh with shards `4-5`, or pivot only for a clearly stronger structural
lever than the exhausted R192-R194 aggregate/column-shadow family.

---

## R194 -- exact outside-column shadow feasibility tested; no gain beyond current Stage-A [2026-06-30]
## OUTCOME: terminal column-incidence relaxation validated but not integrated.

ARTIFACTS:
 - note: `S3_COLUMN_SHADOW_NOGAIN_R194.md`
 - script: `s3_column_shadow_probe.py`
 - outputs:
   `scratchpad\s3_column_shadow_probe_r194_d10_r189_full.json`,
   `scratchpad\s3_column_shadow_probe_r194_d11_diagnostic.json`,
   `scratchpad\s3_column_shadow_probe_r194_d12_sample.json`,
   `scratchpad\s3_column_shadow_probe_smoke_r194.json`

QUESTION:
Can the Stage-B column viewpoint be pulled earlier?  For each unplaced vertex `x`, let
`B_x=N(x) cap P`.  The multiset of outside columns must exactly realize every placed vertex's
residual degree and every placed pair's residual common-neighbour demand.  This gives an exact MILP
over allowed support types, with lambda=1 matching-completion imposed on each support.

VALIDATION / RESULTS:
 - `python -m py_compile .\s3_column_shadow_probe.py` passed.
 - Real-witness controls passed, including actual outside-column reconstruction checks:
   rook(9) exhaustive `0/512`; T(7) sampled `0/200` under generic SRG column rules; BvLS sampled
   `0/100` for subset size at most 12.
 - Clean R189 d10 frontier: `42422/42422` solved `OPTIMAL`, `0` infeasible, `0` extra over current
   Stage-A, `0` limit rows.
 - R189 d10->d11 pilot shard frontiers 0 and 1: first `5000` rows from each solved `OPTIMAL`, `0`
   infeasible, `0` extra.
 - Old R90 d11 first `5000`: `3` column-shadow infeasible rows, all already killed by R185
   matching-completion; extra over current Stage-A `0`.
 - Known d12 sample first `8000` rows of shard r103_004: `2` column-shadow infeasible rows, both
   already killed by R186/R189; extra over current Stage-A `0`.  The two half-second limit rows were
   rerun with a 20s cap and both solved feasible in under `0.7s`.

VERDICT:
The column-shadow formulation is sound but currently no-gain and too costly for the hot path.  It is
left as a diagnostic/no-gain artifact, not integrated into `PartialGraph.can_add()`.

NEXT ACTION:
Do not spend more on column-incidence MILPs unless a deeper refreshed frontier produces failures not
already explained by R185/R186/R189, or unless the MILP failures yield a cheap Farkas-style structural
certificate.  Continue with R189 exact d11 measurement or a different structural lever.

---

## R193 -- adjacent-edge split outside-moment tested; no gain beyond R189 [2026-06-30]
## OUTCOME: matching-aware `(S,D,A)` relaxation measured and not integrated.

ARTIFACT:
 - note: `S3_EDGE_SPLIT_MOMENT_NOGAIN_R193.md`

QUESTION:
R186/R189 count total residual pair-common-neighbour demand.  Since an outside vertex's placed
neighbourhood has adjacent pairs forming a matching, split the residual demand into total pair demand
`D` and adjacent-edge demand `A`, and test feasibility of `(S,D,A)` over outside degree bins with
`0 <= A_x <= floor(s_x/2)`.

MEASUREMENTS:
 - Simple per-vertex incident-demand capacity bound: zero hits on clean R189 d10 and old R90 d11.
 - Global `(S,D,A)` split:
   clean R189 d10 `0/42422`; old R90 d11 `27/463636`, all already global R186 violations, extra over
   R189 `0`.
 - Near-full `(S,D,A)` split for `U=P\{u}` and `U=P\{u,v}`:
   clean R189 d10 `0/42422`.

VERDICT:
The edge-split relaxation is sound but no-gain on current evidence and weaker than R189 on old d11.
It is not integrated into the Stage-A hot path.

NEXT ACTION:
Stay with R189 as the current primary cloud path.  Further useful work needs either exact R189 d11
measurement or a different structural obstruction, not another aggregate outside-degree relaxation.

---

## R192 -- remove-3 near-full subset moment tested; no gain beyond R189 [2026-06-30]
## OUTCOME: sound bounded extension rejected for hot path due measured zero extra pruning.

ARTIFACTS:
 - note: `S3_NEARFULL_REMOVE3_NOGAIN_R192.md`
 - updated script: `s3_nearfull_subset_moment_probe.py` now supports `--max-remove N`
 - outputs:
   `scratchpad\s3_nearfull_subset_moment_probe_r192_remove3_d10_r189.json`,
   `scratchpad\s3_nearfull_subset_moment_probe_r192_remove3_d11_r90.json`,
   `scratchpad\s3_nearfull_subset_moment_probe_r192_remove3_d12_sample200k.json`

QUESTION:
R189 checks the subset outside-degree moment bound for `U=P\{u}` and `U=P\{u,v}`.  The next bounded
variant is `|P\U|<=3`, which is sound but adds `binom(k,3)` subset checks per candidate.

VALIDATION / RESULTS:
 - `python -m py_compile .\s3_nearfull_subset_moment_probe.py` passed.
 - Clean R189 d10 frontier with `--max-remove 3`: `0/42422` violations.  Real-witness controls passed:
   rook(9) exhaustive `0/512`; T(7) sampled `0/1000`; BvLS sampled `0/500`.
 - Old R90 d11 frontier with `--max-remove 3`: near-full violations `14/463636`, exactly the same total
   as R189 remove<=2; no new remove-3 rows.
 - Known d12 bounded sample, first 200000 rows across available frontier files:
   remove<=2 violations `31`, remove<=3 violations `31`, extra remove-3 over remove-2 `0`.

VERDICT:
Remove-3 is sound but currently no-gain.  The harness should remain at R189 remove<=2 unless a deeper
refreshed frontier shows actual remove-3-only rows.

NEXT ACTION:
Do not add remove-3 to the hot path now.  Continue with R189 as primary cloud path or seek a different
structural lever that changes d11/d12 behaviour.

---

## R191 -- R189 d10->d11 shards 0..1 aggregate completed [2026-06-30]
## OUTCOME: current R189 two-shard diagnostic is clean and slightly below the R186 two-shard diagnostic.

ARTIFACTS:
 - note: `R3_D10_D11_R189_TWO_SHARD_R191.md`
 - outputs:
   `scratchpad\r3_d10_to_d11_r189_stats_probe\r3_d10_to_d11_r189_shard64_exact_001.json`,
   `scratchpad\r3_d10_to_d11_r189_frontiers_probe\r3_d10_to_d11_r189_shard64_exact_001_frontier.jsonl`,
   `scratchpad\r3_d10_to_d11_r189_001_aggregate_probe.json`,
   `scratchpad\r3_d10_to_d11_r189_000_001_aggregate_probe.json`,
   `scratchpad\s3_nearfull_subset_moment_probe_r191_d11_shard001.json`,
   `scratchpad\s3_outside_degree_moment_probe_r191_d11_shard001.json`

VALIDATION / RESULTS:
 - R189 shards 0..1 loaded `1326/42422` parents (`3.1257%`) and produced `14824` depth-11 children.
 - Shard 0: `663 -> 7336`, wall `69.25s`; shard 1: `663 -> 7488`, wall `71.85s`.
 - Diagnostic scaled `N11 ~= 474256.2`; not exact.
 - No budget/time/sample flags.
 - Fresh shard-1 frontier scans clean under R189 and R186, both with real-witness controls green.
 - R188's R186 two-shard diagnostic was `14832` children and scaled `N11 ~= 474523.3`.  The R189
   two-shard diagnostic is lower by 8 children, but this is not an exact delta because the R189 d10
   row removal changes modulo shard membership after that row.

VERDICT:
The R189 cloud path is actual-run verified over shards 0 and 1.  Exact R189 `N11` still requires all
64 shards and strict aggregation without `--allow-incomplete`.

NEXT ACTION:
Run remaining R189 d10->d11 shards for the exact refreshed d11 frontier, or pivot to another structural
constraint that can fire at d11/d12 before spending the full shard budget.

---

## R190 -- R189 d10->d11 shard-0 pilot completed [2026-06-30]
## OUTCOME: current R189 one-command refresh actual-run verified; shard-0 child count reduced vs R186.

ARTIFACTS:
 - note: `R3_D10_D11_R189_PILOT_R190.md`
 - outputs:
   `scratchpad\r3_d10_to_d11_r189_stats_probe\r3_d10_to_d11_r189_shard64_exact_000.json`,
   `scratchpad\r3_d10_to_d11_r189_frontiers_probe\r3_d10_to_d11_r189_shard64_exact_000_frontier.jsonl`,
   `scratchpad\r3_d10_to_d11_r189_000_aggregate_probe.json`,
   `scratchpad\s3_nearfull_subset_moment_probe_r190_d11_shard000.json`,
   `scratchpad\s3_outside_degree_moment_probe_r190_d11_shard000.json`

COMMAND:
`python .\s3_cloud_r3_d11_r189.py --skip-gate --indices 0 --out-dir .\scratchpad\r3_d10_to_d11_r189_stats_probe --frontier-out-dir .\scratchpad\r3_d10_to_d11_r189_frontiers_probe --aggregate-out .\scratchpad\r3_d10_to_d11_r189_000_aggregate_probe.json`

VALIDATION / RESULTS:
 - Source frontier `scratchpad\r3_frontier_d10_r189_nearfull_subset_moment.jsonl`, SHA-256
   `68241a7ace8b0b118245e088a7d3289452927955dbf030df5fe63620d5129871`.
 - Shard 0 loaded `663/42422` parents (`1.5629%`) and produced `7336` depth-11 children.
 - Diagnostic scaled `N11 ~= 469393.4`; not exact.
 - No budget/time/sample flags; wall `69.25s`.
 - Fresh shard frontier scans clean under R189 and R186, both with real-witness controls green.
 - Comparison: the R188 R186 shard-0 pilot produced `7403` children from the same parent count, so
   R189 removes `67` children on this shard.

VERDICT:
R189 is not just a d10 frontier cleanup; it prunes inside d10->d11.  Exact R189 `N11` still requires
all 64 shards and strict aggregation without `--allow-incomplete`.

NEXT ACTION:
Run the remaining R189 d10->d11 shards, or seek another structural lever that fires at/after d11.

---

## R189 -- near-full subset outside-degree moment closure added to Stage-A [2026-06-30]
## OUTCOME: new proof-grade R186 strengthening shipped; exact d10 prefix reduced to 42422.

ARTIFACTS:
 - note: `S3_NEARFULL_SUBSET_MOMENT_R189.md`
 - updated scripts: `s3_slice_harness.py`, `s3_nearfull_subset_moment_probe.py`,
   `s3_cloud_r3_d11_r189.py`
 - outputs:
   `scratchpad\s3_nearfull_subset_moment_probe_r189_d10_r186.json`,
   `scratchpad\s3_nearfull_subset_moment_probe_r189_d10_r185.json`,
   `scratchpad\s3_nearfull_subset_moment_probe_r189_d11_r90.json`,
   `scratchpad\s3_nearfull_subset_moment_known_d12_r189.json`,
   `scratchpad\s3_nearfull_subset_moment_d9_to_d10_r189.json`,
   `scratchpad\r3_frontier_d10_r189_nearfull_subset_moment.jsonl`,
   `scratchpad\s3_nearfull_subset_moment_probe_r189_d10_new.json`,
   `scratchpad\s3_outside_degree_moment_probe_r189_d10_new.json`,
   `scratchpad\s3_neighborhood_matching_closure_probe_r189_d10_new.json`

THEOREM:
For any subset `U` of the placed prefix `P`, while the outside set remains the unplaced vertices
`X=V\P`, the residual outside degrees into `U` must realize
`S_U=sum_{u in U}(14-deg_P(u))` and
`D_U=sum_{a<b in U}(tau(a,b)-common_P(a,b))`.  R189 ships the cheap near-full cases
`U=P\{u}` and `U=P\{u,v}` using the same min/max outside pair-moment bounds as R186.

VALIDATION / RESULTS:
 - Synthetic control fires on a real R186-clean d10 row: global R186 passes, but `P\{9}` has
   `S=90`, `D=0`, and lower bound `1`.
 - Real-witness checks passed: rook(9) exhaustive `0/512`; T(7) sampled `0/1000`; BvLS sampled
   `0/500`.
 - `python -m py_compile .\s3_slice_harness.py .\s3_nearfull_subset_moment_probe.py
   .\s3_cloud_r3_d11_r189.py` passed.
 - `python .\s3_slice_harness.py --gate` stayed ALL GREEN.
 - Frontier scans:
   clean R186 d10 `1/42423` near-full violation, extra over global R186 `1`;
   R185 d10 global R186 `2/42425`, near-full `1/42425`, combined effect `3`;
   old R90 d11 global R186 `27/463636`, near-full `14/463636`, extra `10`, direct union `37`;
   known d12 global R186 `141/1174677`, near-full `153/1174677`, extra `87`, direct union `228`.
 - Regenerated exact prefix:
   `N10=42422` from the R185 d9 frontier, down from R186 `42423`, R185 `42425`, and pre-R185 `42430`.
 - The new R189 d10 frontier scans clean under R189, R186, and R185.
 - `s3_cloud_r3_d11_r189.py` compiles and dry-runs to the expected one-command R189 d10->d11 shard
   refresh over `scratchpad\r3_frontier_d10_r189_nearfull_subset_moment.jsonl`.
 - The R188 shard 0/1 pilot frontiers scan clean under R189, so that diagnostic remains representative
   for those shard indices.

VERDICT:
This is a real Stage-A pruning improvement.  It is still small at shallow depth, but it has measured
extra hits beyond R186 and is cheap enough to keep in the harness.

IMPORTANT CAVEAT:
Like R186, R189 is sound as a prefix predicate but old later-depth direct scans are not exact refreshed
counts.  Exact R189 `N11` requires a d10->d11 refresh from
`scratchpad\r3_frontier_d10_r189_nearfull_subset_moment.jsonl`.

NEXT ACTION:
Use `s3_cloud_r3_d11_r189.py` as the current primary exact d10->d11 cloud refresh.  Do not continue
R186/R90 d11->d12 work except as historical diagnostic evidence.

---

## R188 -- R186 d10->d11 two-shard pilot completed [2026-06-30]
## OUTCOME: current one-command cloud refresh produced clean stats/frontier artifacts; exact N11 still pending.

ARTIFACTS:
 - note: `R3_D10_D11_R186_PILOT_R188.md`
 - outputs:
   `scratchpad\r3_d10_to_d11_r186_stats_probe\r3_d10_to_d11_r186_shard64_exact_000.json`,
   `scratchpad\r3_d10_to_d11_r186_stats_probe\r3_d10_to_d11_r186_shard64_exact_001.json`,
   `scratchpad\r3_d10_to_d11_r186_frontiers_probe\r3_d10_to_d11_r186_shard64_exact_000_frontier.jsonl`,
   `scratchpad\r3_d10_to_d11_r186_frontiers_probe\r3_d10_to_d11_r186_shard64_exact_001_frontier.jsonl`,
   `scratchpad\r3_d10_to_d11_r186_000_001_aggregate_probe.json`,
   `scratchpad\s3_outside_degree_moment_probe_r188_d11_shard000.json`,
   `scratchpad\s3_outside_degree_moment_probe_r188_d11_shard001.json`,
   `scratchpad\s3_neighborhood_matching_closure_probe_r188_d11_shard000.json`,
   `scratchpad\s3_neighborhood_matching_closure_probe_r188_d11_shard001.json`

COMMAND:
`python .\s3_cloud_r3_d11_r186.py --skip-gate --indices 0-1 --out-dir .\scratchpad\r3_d10_to_d11_r186_stats_probe --frontier-out-dir .\scratchpad\r3_d10_to_d11_r186_frontiers_probe --aggregate-out .\scratchpad\r3_d10_to_d11_r186_000_001_aggregate_probe.json`

VALIDATION / RESULTS:
 - Source frontier `scratchpad\r3_frontier_d10_r186_outside_moment.jsonl`, SHA-256
   `afe0a15025dd6b759785a1c439893bfbc49737026483a6cb1ae81eb8824f6ac7`.
 - Shards 0 and 1 loaded `1326/42423` parents (`3.1257%`) and produced `14832` depth-11 children.
 - Shard 0: `663 -> 7403`, wall `58.93s`; shard 1: `663 -> 7429`, wall `58.71s`.
 - Diagnostic scaled `N11 ~= 474523.3`; not exact.
 - No budget/time/sample flags.  Aggregate counters: `expanded=16158`, `iso_dups=5908`,
   `canonical_parent_reject=174240`, `canonical_parent_cache_hit=49575`.
 - Fresh shard-frontier scans were clean under R186 outside-degree moment and R185 matching completion:
   all four scans reported `frontier_violations=0` with real-witness controls green.

VERDICT:
The R186 d10->d11 cloud refresh is now actual-run verified, not just dry-run verified.  Exact R186
`N11` still requires all 64 shards and a strict aggregate without `--allow-incomplete`.

NEXT ACTION:
For decisive measurement, run the remaining R186 d10->d11 shards (or distribute all 64 cleanly), then
merge the exact d11 frontier before any refreshed d11->d12 work.  The problem remains open.

---

## R187 -- exact outside-degree histogram feasibility checked; no extra current prune [2026-06-30]
## OUTCOME: stronger-in-principle R186 variant tested and not shipped to hot path.

ARTIFACTS:
 - note: `S3_OUTSIDE_DEGREE_DISTRIBUTION_R187.md`
 - script: `s3_outside_degree_distribution_probe.py`
 - outputs:
   `scratchpad\s3_outside_degree_distribution_probe_r187_d10_r186.json`,
   `scratchpad\s3_outside_degree_distribution_probe_r187_d10_r185.json`,
   `scratchpad\s3_outside_degree_distribution_probe_r187_d11_r90.json`,
   `scratchpad\s3_outside_degree_distribution_known_d12_r187.json`

QUESTION:
R186 asks only whether the residual outside pair demand `D` lies in the min/max interval for
`sum_x binom(s_x,2)` at fixed outside-degree sum `S`.  The exact strengthening asks whether an integer
histogram `c_i` of outside degrees actually realizes both `S` and `D`.

VALIDATION / RESULTS:
 - `python -m py_compile .\s3_outside_degree_distribution_probe.py` passed.
 - Real-witness checks passed: rook(9) exhaustive `0/512`; T(7) sampled `0/1000`; BvLS sampled `0/500`.
 - Clean R186 d10 frontier: distribution violations `0/42423`, extra over R186 `0`.
 - Pre-R186/R185 d10 frontier: distribution violations `2/42425`, exactly the same two R186 range
   violations, extra over R186 `0`.
 - Old R90 d11 frontier: distribution violations `27/463636`, exactly the same as R186, extra over
   R186 `0`.
 - Known d12 frontier files: distribution violations `141/1174677`, exactly the same as R186, extra
   over R186 `0`.

VERDICT:
The predicate is sound and stricter than R186 in abstract, but it adds no measured pruning on the
current r=3 frontier evidence.  It is intentionally left as a probe/no-gain artifact, not integrated
into the Stage-A hot path.

NEXT ACTION:
Do not spend more time on outside-degree histogram refinements unless a deeper frontier actually lands
in an exact feasibility gap.  The decisive runnable experiment remains the R186 d10->d11 refresh, or a
new structural lever that fires before the existing d12 plateau.

---

## R186 -- outside-degree moment completion closure added to Stage-A [2026-06-30]
## OUTCOME: new global residual-demand predicate shipped; exact d10 prefix reduced again.

ARTIFACTS:
 - note: `S3_OUTSIDE_DEGREE_MOMENT_R186.md`
 - updated scripts: `s3_slice_harness.py`, `s3_outside_degree_moment_probe.py`,
   `s3_cloud_r3_d11_r186.py`
 - outputs:
   `scratchpad\s3_outside_degree_moment_probe_r186_d9_r185.json`,
   `scratchpad\s3_outside_degree_moment_probe_r186_d10_r185.json`,
   `scratchpad\s3_outside_degree_moment_probe_r186_d11_r90.json`,
   `scratchpad\s3_r185_r186_overlap_d11_r90.json`,
   `scratchpad\s3_outside_degree_moment_known_d12_r186.json`,
   `scratchpad\s3_outside_degree_moment_d9_to_d10_r186.json`,
   `scratchpad\r3_frontier_d10_r186_outside_moment.jsonl`,
   `scratchpad\s3_outside_degree_moment_probe_r186_d10_new.json`,
   `scratchpad\s3_neighborhood_matching_closure_probe_r186_d10_new.json`

THEOREM:
For a partial induced subgraph `P`, write `X=V\P` and `s_x=|N(x) cap P|`.
Then
`sum_x s_x = sum_{p in P}(14-deg_P(p))`, and
`sum_x binom(s_x,2) = sum_{a<b in P}(tau(a,b)-common_P(a,b))`, where `tau` is
`lambda=1` on adjacent pairs and `mu=2` on non-adjacent pairs.  The second sum
must lie between the balanced minimum and greedy-filled maximum possible over
`99-|P|` outside vertices with `0 <= s_x <= min(14, |P|)`.  A value outside this
range cannot be completed to an SRG.

VALIDATION / RESULTS:
 - Synthetic local-valid impossible partial fired: `|P|=10`, residual degree sum `100` over 89 outside
   vertices forces minimum pair moment 11, but the prefix demands only 10.
 - Real-witness checks passed: rook(9) exhaustive `0/512`; T(7) sampled `0/1000`; BvLS sampled
   `0/500` in the initial probe.
 - `python -m py_compile .\s3_slice_harness.py .\s3_pair_lower_closure_probe.py
   .\s3_neighborhood_matching_closure_probe.py .\s3_outside_degree_moment_probe.py
   .\s3_cloud_r3_d11_r186.py` passed.
 - `python .\s3_slice_harness.py --gate` stayed ALL GREEN.
 - Old/new frontier scans:
   R185 d9 `0/5310`, R185 d10 `2/42425`, old R90 d11 `27/463636` direct violations.
 - Old R90 d11 overlap scan: R185 direct violations `29`, R186 direct violations `27`, overlap `0`,
   either `56`.
 - All 89 available d12 frontier files were scanned: `141/1174677` direct rows violate R186.
 - Regenerated exact prefix:
   `N10=42423` from the R185 d9 frontier, down from R185 `42425` and pre-R185 `42430`; the new d10
   frontier scans clean under both R185 and R186.
 - `s3_cloud_r3_d11_r186.py` compiles and dry-runs to the expected one-command R186 d10->d11 shard
   refresh over `scratchpad\r3_frontier_d10_r186_outside_moment.jsonl`.

VERDICT:
This is proof-grade and implemented, but small at depth 10.  It catches a global outside-degree
completion impossibility that local matching and pair lower-closure miss.

IMPORTANT CAVEAT:
R186 is a necessary predicate on each prefix, but its displayed later-depth row statistic is not
monotone.  Therefore the old R90 d11 direct scan is not an exact refreshed `N11` count.  The exact R186
`N11` must be measured by rerunning d10->d11 from `scratchpad\r3_frontier_d10_r186_outside_moment.jsonl`
with `s3_cloud_r3_d11_r186.py`.

NEXT ACTION:
Run the R186 d10->d11 refresh to produce a clean exact d11 frontier, or pursue a stronger structural
lever such as exact outside-degree distribution feasibility.  Do not quote `463580` as exact under
R186; it is only the old-R90 direct-row union count.

---

## R185 -- neighbourhood matching-completion closure added to Stage-A [2026-06-30]
## OUTCOME: R37 locally-7K2 predicate strengthened; exact shallow counts reduced.

ARTIFACTS:
 - note: `S3_NEIGHBORHOOD_MATCHING_CLOSURE_R185.md`
 - updated scripts: `s3_slice_harness.py`, `s3_neighborhood_matching_closure_probe.py`,
   `s3_cloud_r3_d11_r185.py`
 - outputs:
   `scratchpad\s3_neighborhood_matching_closure_probe_r185_d9_r50.json`,
   `scratchpad\s3_neighborhood_matching_closure_probe_r185_d10_r52.json`,
   `scratchpad\s3_neighborhood_matching_closure_probe_r185_d11_r90_full.json`,
   `scratchpad\s3_neighborhood_matching_closure_known_d12_r185.json`,
   `scratchpad\s3_neighborhood_matching_closure_slice_d9_r185.json`,
   `scratchpad\r3_frontier_d9_r185_matchingclosure.jsonl`,
   `scratchpad\s3_neighborhood_matching_closure_d9_to_d10_r185.json`,
   `scratchpad\r3_frontier_d10_r185_matchingclosure.jsonl`

THEOREM:
In a `lambda=1`, `k`-regular graph, every full neighbourhood is a perfect matching.  For a placed
vertex `v` in a partial induced subgraph, with `d=|N_P(v)|` and `m` current matching edges inside
`N_P(v)`, the necessary completion condition is `d - 2m <= k - d`.  The left side counts currently
unpaired neighbours; the right side is the number of future neighbour slots.  The deficit is monotone
under extension, so a violation cannot be repaired later.

VALIDATION / RESULTS:
 - Synthetic local-valid impossible partial fired: 8 unpaired neighbours, 6 future slots.
 - Real-witness checks passed: rook(9) exhaustive `0/512`; BvLS sampled `0/5000` in each run.
 - `python -m py_compile .\s3_slice_harness.py .\s3_neighborhood_matching_closure_probe.py
   .\s3_pair_lower_closure_probe.py` passed.
 - `python .\s3_slice_harness.py --gate` stayed ALL GREEN: all `362880/362880` rook(9) orders
   accepted; T(7) reconstruction remained green.
 - Old exact frontier scans found dead rows:
   old d9 `1/5311`, old d10 `5/42430`, old d11/R90 `29/463636`.
 - All 89 available d12 frontier files were scanned: `57/1174677` rows violate the new predicate,
   in 19 files.
 - Regenerated exact prefix:
   `N9=5310` (old `5311`), `N10=42425` (old `42430`); the new d9/d10 frontiers scan clean.
 - By monotonicity, corrected exact `N11` for the old R90 tree is `463636 - 29 = 463607` without a
   full rerun of the d10->d11 shard set.
 - `s3_cloud_r3_d11_r185.py` compiles and dry-runs to the expected one-command R185 d10->d11 shard
   refresh over `scratchpad\r3_frontier_d10_r185_matchingclosure.jsonl`.

VERDICT:
This is a proof-grade, implemented pruning improvement.  The reduction is small at shallow depth, but
it fixes a real missing completion condition in the local block and starts before the spectral gates.
The 99-graph problem remains open.

NEXT ACTION:
Future exact shard work should use `s3_cloud_r3_d11_r185.py` to refresh the R185 d11 frontier, or
regenerate affected prefixes with the new predicate; do not mix old and new counts without subtracting
the scanned dead rows.  Higher-leverage work remains finding a stronger structural obstruction or
measuring the deep spectral-gate regime.

---

## R184 -- pair lower-closure Stage-A predicate added and witness-gated [2026-06-30]
## OUTCOME: new sound necessary condition shipped; no depth-12 or shallow-prefix pruning yet.

ARTIFACTS:
 - note: `S3_PAIR_LOWER_CLOSURE_R184.md`
 - updated scripts: `s3_slice_harness.py`, `s3_pair_lower_closure_probe.py`
 - outputs:
   `scratchpad\s3_pair_lower_closure_probe_r184_shard84.json`,
   `scratchpad\s3_pair_lower_closure_probe_r184_shard85.json`,
   `scratchpad\s3_pair_lower_closure_slice_d9_r184.json`

THEOREM:
For any placed pair `u,v` in a partial induced subgraph of a `k`-regular SRG,
`common_P(u,v) + min(k-deg_P(u), k-deg_P(v)) >= lambda_or_mu(u,v)` is necessary.
Every future common neighbour consumes one remaining degree slot from both endpoints.

VALIDATION / RESULTS:
 - Synthetic impossible partial fired.
 - Real-witness no-overprune checks passed: rook(9) exhaustive `0/512` violations; T(7) sampled
   `0/5000`; BvLS sampled `0/5000` on each probe run.
 - Current R183 depth-12 frontiers stayed clean: shard 84 `0/12969` violations; shard 85
   `0/13347` violations.
 - `python -m py_compile .\s3_slice_harness.py .\s3_pair_lower_closure_probe.py` passed.
 - `python .\s3_slice_harness.py --gate` passed: all `362880/362880` rook(9) orders accepted and
   T(7) reconstruction remained green.
 - Shallow exact r=3 prefix through depth 9 remained unchanged:
   `1,2,4,9,21,62,208,916,5311`; prune counters all 0.

VERDICT:
The predicate is sound and now part of `PartialGraph.can_add()`, but it is a late degree-saturation
guard, not a demonstrated cloud-cost breakthrough.  It does not change the known R90/R183 d11/d12
measurement evidence and does not solve the problem.

NEXT ACTION:
Use the R184 predicate in future continuation runs.  For progress beyond bookkeeping, either drive a
deeper measurement toward levels where residual-degree saturation can occur, or find a genuinely new
structural obstruction that fires before the current d12 plateau.

---

## R183 -- exact r=3 d11->d12 shards 84..85 completed; known coverage now 89/512 [2026-06-30]
## OUTCOME: one-command cloud measurement still healthy; no prune and no proof.

ARTIFACTS:
 - note: `R3_CLOUD_SHARDS_R183.md`
 - outputs:
   `scratchpad\r3_d11_to_d12_shard512_exact_r183_084.json`,
   `scratchpad\r3_d11_to_d12_shard512_exact_r183_085.json`,
   `scratchpad\r3_d11_to_d12_shard512_084_085_exact_aggregate_r183.json`,
   `scratchpad\r3_d11_to_d12_shard512_known89_aggregate_r183.json`,
   matching frontier JSONL files in `scratchpad\r3_d11_to_d12_frontiers\`

VALIDATION / RESULTS:
 - Shard 84: 906 parents -> 12,969 depth-12 children; branch 14.315; wall 131.68s; no
   budget/time/sample flags; local/spectral/triangle-split prunes all 0; frontier physical row count
   matched stats.
 - Shard 85: 906 parents -> 13,347 depth-12 children; branch 14.732; wall 130.79s; no
   budget/time/sample flags; local/spectral/triangle-split prunes all 0; frontier physical row count
   matched stats.
 - Two-shard aggregate: 1,812 loaded parents, 26,316 depth-12 children, diagnostic scaled
   `N12 ~= 6.7335e6`.
 - Updated known aggregate over shards `0..85,128,256,384`: 80,633/463,636 depth-11 parents
   (17.3914%), 1,174,677 measured depth-12 children, diagnostic scaled `N12 ~= 6.7543e6`.

VERDICT:
The primary R43 r=3 cloud measurement route remains one-command runnable and reproducible.  It is still
only a cost/frontier measurement: no local, spectral, or triangle-split pruning has fired by depth 12,
and no Stage-B conclusion is sound before completed 45-vertex H' candidates exist.

NEXT ACTION:
Next contiguous exact shards are 86..87 if continuing the measurement.  Higher-leverage alternatives are
to find a valid Stage-A obstruction or drive a deeper measurement into the spectral-gate regime.

---

## R182 -- terminal H-only residual-demand precheck derived from Stage-B closure equations [2026-06-30]
## OUTCOME: cheap terminal pre-column-generation check added and real-witness validated; not a partial prune.

ARTIFACTS:
 - note: `S3_TERMINAL_H_SHADOW_PRECHECK_R182.md`
 - updated scripts: `s3_stageb_columns_cpsat.py`, `s3_slice_harness.py`
 - outputs:
   `scratchpad\s3_stageb_shadow_precheck_t7_selftest_r182.json`,
   `scratchpad\s3_stageb_shadow_precheck_t7_selftest_r182b.json`,
   `scratchpad\terminal_h_shadow_t7_sample200_r182.json`

VALIDATION / RESULTS:
 - `terminal_h_shadow_precheck()` checks terminal H-only residual demands before column generation:
   residual star degrees `k-deg_H(h)` and H-H residual common-neighbour demands
   `lambda/mu - common_H(h,h')`.
 - `python -m py_compile s3_slice_harness.py s3_stageb_columns_cpsat.py` passed.
 - On a real T(7) r=3 star complement, the shadow precheck is ok: residual degree range 2..5,
   residual degree sum 48, pair residual demand range 0..4, and 99 H-H pairs have positive residual
   demand.  Full CP-SAT closure still passes.
 - Shadow-only sample over 200 random real T(7) r=3 star complements: 200/200 passed, 0 failures,
   wall 0.026s.  Residual degree min range 1..2, max range 4..6, sum range 36..50; pair demand max
   range 2..5.
 - Harness smoke remains green: `s3_slice_harness.py --stageb-demo --target-depth 10 --node-budget
   20000 --time-cap 20 --stageb-engine auto` uses CP-SAT on a partial generated candidate and skips
   terminal-only constraints as intended.

VERDICT:
This is an exact terminal precheck and a small cloud-cost reducer before Stage-B column generation.  It
is not valid on partial d12 frontiers without a new lookahead theorem.  The 99-graph problem remains
open.

NEXT ACTION:
Either prove sound lookahead bounds that make the residual-demand check useful before depth 45, or return
to exact Stage-A measurement from the R90 frontier.

---

## R181 -- full-closure Stage-B CP-SAT validated on 12 random T(7) star complements [2026-06-30]
## OUTCOME: R179/R180 Stage-B solver has multi-witness real-graph validation; problem still open.

ARTIFACT:
 - note: `S3_STAGEB_T7_SAMPLE_SUITE_R181.md`
 - output: `scratchpad\s3_stageb_fullclosure_t7_sample12_r181.json`

VALIDATION / RESULTS:
 - Sampled 12 distinct 15-vertex r=3 star complements of real `T(7)=srg(21,10,5,4)` using seed 181.
 - For every sample, CP-SAT diagonal generation matched exact brute enumeration, recovered the true star
   columns, true closure matched the real star-set graph, full-closure CP-SAT found a target-6 solution,
   and the selected closure verified as `srg(21,10,5,4)`.
 - Aggregate: 12/12 passed, 16 attempts, total wall 56.9662s, CP-SAT diagonal wall sum 4.1989s,
   full-closure clique wall sum 3.1673s.
 - Column/constraint spread across samples: diagonal-valid columns 274..765, degree-forced-off columns
   15..76, X-X common-neighbour forced-off pairs 1,298..10,627, H-X forced-off columns 258..678.

VERDICT:
The R179/R180 full-closure Stage-B model is now validated on multiple real r=3 star complements, not
just one.  This materially strengthens correctness confidence for terminal-H processing, but gives no
construction/nonexistence result without completed 45-vertex H' candidates.

NEXT ACTION:
Return to the Stage-A bottleneck: reduce or measure the 45-vertex r=3 star-complement search, or find a
new structural obstruction that prunes before terminal H' generation.

---

## R180 -- R179 full-closure Stage-B CP-SAT wired into the main r=3 harness [2026-06-30]
## OUTCOME: terminal Stage-B path is now one-command reachable from `s3_slice_harness.py`; still no terminal candidates.

ARTIFACTS:
 - note: `S3_STAGEB_HARNESS_INTEGRATION_R180.md`
 - updated script: `s3_slice_harness.py`
 - validation output: `scratchpad\s3_stageb_fullclosure_cpsat_t7_selftest_r179b.json`

VALIDATION / RESULTS:
 - Full compile sweep over the touched harness/tooling scripts passed.
 - `python s3_slice_harness.py --gate` passed: rook(9) local replay, rook(9) spectral/triangle-split
   checks, and T(7) end-to-end reconstruction all remain green.
 - `python s3_stageb_columns_cpsat.py --self-test --time-cap 30 --json-out scratchpad\s3_stageb_fullclosure_cpsat_t7_selftest_r179b.json`
   passed with full-closure CP-SAT status `OPTIMAL`, selected 6/6, closure true, wall 0.4909s.
 - `python s3_slice_harness.py --stageb-demo --target-depth 10 --node-budget 20000 --time-cap 20 --stageb-engine auto`
   exercised the integrated CP-SAT diagonal path on a generated nonsingular 10-vertex partial.  It used
   engine `cpsat`, found 0 diagonal-valid columns, and correctly skipped terminal-only full-closure
   constraints because the candidate was partial.

VERDICT:
The main r=3 harness can now route completed 45-vertex H' candidates to the R179 full-closure CP-SAT
Stage-B solver.  This closes an implementation gap in the decisive path, but no completed terminal H'
has been generated and the problem remains open.

NEXT ACTION:
Return to Stage-A cost reduction/measurement: either continue exact r=3 d11->d12 cloud coverage from
the R90 frontier, or find a new validated structural obstruction that reduces the 45-vertex search.

---

## R179 -- full SRG closure equations added to r=3 Stage-B CP-SAT model [2026-06-30]
## OUTCOME: strongest Stage-B terminal model so far; validated on T(7), not yet wired into terminal cloud workers.

ARTIFACTS:
 - note: `S3_STAGEB_FULLCLOSURE_CPSAT_R179.md`
 - updated script: `s3_stageb_columns_cpsat.py`
 - output: `scratchpad\s3_stageb_fullclosure_cpsat_t7_selftest_r179.json`

VALIDATION / RESULTS:
 - `python -m py_compile s3_stageb_columns_cpsat.py` passed.
 - The CP-SAT Stage-B model now enforces the full final closure equations over selected columns:
   star-set degrees, X-X common-neighbour equations, H-degree equations, H-H common-neighbour equations,
   and H-X common-neighbour equations.
 - On real `T(7)=srg(21,10,5,4)`, diagonal generation still exactly matched brute force: 735 columns
   both ways, same set, status `OPTIMAL`, wall 0.5198s.
 - The full closure target-6 model remained `OPTIMAL`, selected 6 columns, closed exactly, and the
   assembled graph verified as `srg(21,10,5,4)`.  Final solve wall 0.4966s, with 0 conflicts and
   0 branches.
 - T(7) control counters: 256,752 incompatible pairs; 6,196 compatible 1-pairs; 6,797 compatible
   0-pairs; 61 degree-forced-off columns; 9,225 X-X common-neighbour forced-off pairs; 3,768 active
   X-X constraints; 15 H-degree constraints; 105 H-H constraints; 9,308 H-X constraints; 633 H-X
   forced-off columns.

VERDICT:
Stage-B is now much closer to a genuine terminal solver: it encodes the SRG closure equations directly
instead of relying on compatibility plus post-verification.  It is proof-safe and real-witness gated, but
it does not affect partial d12 frontiers or solve the problem without completed 45-vertex `H'` candidates.

NEXT ACTION:
Wire the full-closure CP-SAT Stage-B model into terminal `s3_slice_harness.py` processing, or continue
the r=3 cloud measurement toward completed 45-vertex candidates.

---

## R178 -- X-X common-neighbour equations added to r=3 Stage-B CP-SAT clique [2026-06-30]
## OUTCOME: stronger exact Stage-B model validated on T(7); not a Stage-A prune.

ARTIFACTS:
 - note: `S3_STAGEB_COMMON_CPSAT_R178.md`
 - updated script: `s3_stageb_columns_cpsat.py`
 - output: `scratchpad\s3_stageb_xxcommon_cpsat_t7_selftest_r178.json`

VALIDATION / RESULTS:
 - `python -m py_compile s3_stageb_columns_cpsat.py` passed.
 - The CP-SAT clique can now enforce X-X common-neighbour equations: for a selected pair of star
   columns, common neighbours from `H'` plus selected star columns must equal `lambda` or `mu` according
   to the reconstructed star-set adjacency.
 - On real `T(7)=srg(21,10,5,4)`, diagonal generation still exactly matched brute force: 735 columns
   both ways, same set, status `OPTIMAL`, wall 0.5177s.
 - The strengthened target-6 clique model remained `OPTIMAL`, selected 6 columns, closed exactly, and
   the assembled graph verified as `srg(21,10,5,4)`.
 - Counters on the T(7) control: degree constraints forced off 61/735 columns; X-X common-neighbour
   equations forced off 9,225 compatible column pairs and left 3,768 active pair constraints; clique
   wall 1.5712s.

VERDICT:
This is another mathematically safe Stage-B pruning improvement, expressed entirely as final SRG
common-neighbour equations over selected star columns.  It is witness-gated and not a Stage-A cut.
The 99-graph problem remains open.

NEXT ACTION:
Extend the same exact-final-condition encoding to H-X and H-H common-neighbour equations, or wire the
strengthened CP-SAT Stage-B model into terminal 45-vertex H' processing.

---

## R177 -- exact star-set degree constraints added to r=3 Stage-B CP-SAT clique [2026-06-30]
## OUTCOME: safe Stage-B strengthening validated on T(7); no Stage-A pruning claim.

ARTIFACTS:
 - note: `S3_STAGEB_DEGREE_CPSAT_R177.md`
 - updated script: `s3_stageb_columns_cpsat.py`
 - output: `scratchpad\s3_stageb_degree_cpsat_t7_selftest_r177.json`

VALIDATION / RESULTS:
 - `python -m py_compile s3_stageb_columns_cpsat.py` passed.
 - The CP-SAT compatibility clique now optionally enforces the exact final degree equation
   `deg_X(b)=k-|b|` for every selected star column.
 - On real `T(7)=srg(21,10,5,4)`, diagonal generation still exactly matched brute force:
   735 columns both ways, same set, status `OPTIMAL`, wall 0.5311s.
 - The degree-aware target-6 clique model remained `OPTIMAL`, selected 6 columns, closed exactly, and
   the assembled graph verified as `srg(21,10,5,4)`.
 - The degree rule forced 61/735 diagonal-valid T(7) columns off before clique search; clique wall was
   1.6319s versus R176's 3.218s control run.

VERDICT:
This is a mathematically safe Stage-B pruning improvement: it is just regularity of the reconstructed
star set expressed in column language.  It must not be used as a Stage-A cut and it does not change the
existence status.

NEXT ACTION:
Add exact common-neighbour equations to the Stage-B CP-SAT clique, gated on T(7), or integrate the
degree-aware CP-SAT Stage-B solver into terminal 45-vertex H' processing.

---

## R176 -- CP-SAT compatibility/clique layer for r=3 Stage-B validated on T(7) [2026-06-30]
## OUTCOME: Stage-B prototype now covers diagonal columns + compatibility clique + exact closure on a real witness.

ARTIFACTS:
 - note: `S3_STAGEB_FULL_CPSAT_R176.md`
 - updated script: `s3_stageb_columns_cpsat.py`
 - outputs:
   `scratchpad\s3_stageb_full_cpsat_t7_selftest_r176.json`,
   `scratchpad\s3_stageb_columns_cpsat_frontier082_row0_r176.json`,
   `scratchpad\s3_stageb_columns_cpsat_frontier082_rows0_19_r176.json`

VALIDATION / RESULTS:
 - `python -m py_compile s3_stageb_columns_cpsat.py` passed.
 - On real `T(7)=srg(21,10,5,4)`, CP-SAT diagonal generation exactly matched brute force:
   735 columns both ways, same set, status `OPTIMAL`, wall 0.5245s.
 - The true 6 star columns were recovered, pairwise compatible, closed to the real `T(7)` star-set
   graph, and the assembled graph verified as `srg(21,10,5,4)`.
 - The new CP-SAT compatibility model solved a target-6 clique over the 735 columns with status
   `OPTIMAL` in 3.218s; the selected clique closed exactly and also verified as `srg(21,10,5,4)`.
 - Current R173 d12 frontier smoke remains only an algorithm test: row 0 and rows 0..19 of shard 82
   match brute force with 0 diagonal-valid columns.  These partial rows are not terminal-H pruning
   objects.

VERDICT:
This is a real Stage-B readiness improvement: diagonal generation, compatibility, clique selection,
and closure are now all exercised through CP-SAT on a real r=3 witness.  It does not prove existence or
nonexistence, and it must not be applied as a Stage-A prune before a completed 45-vertex `H'` exists.

NEXT ACTION:
Integrate the CP-SAT Stage-B path into the terminal `s3_slice_harness.py` worker path, or continue exact
r=3 d11->d12 measurement only when it improves the decisive cost model.  The primary R43 structural
switch remains the 45-vertex eigenvalue-3 star-complement search, with the current exact cloud prefix at
d11 and measured d12 coverage still only diagnostic.

---

## R175 -- CP-SAT prototype for Stage-B diagonal column generation [2026-06-30]
## OUTCOME: Stage-B diagonal-column building block added and real-witness gated; not yet a terminal-H solver.

ARTIFACTS:
 - note: `S3_STAGEB_COLUMNS_CPSAT_R175.md`
 - new script: `s3_stageb_columns_cpsat.py`
 - outputs:
   `scratchpad\s3_stageb_columns_cpsat_t7_selftest_r175.json`,
   `scratchpad\s3_stageb_columns_cpsat_frontier082_row0_r175.json`

VALIDATION / RESULTS:
 - `python -m py_compile s3_stageb_columns_cpsat.py` passed.
 - On real `T(7)=srg(21,10,5,4)` r=3 star-complement control, CP-SAT diagonal generation exactly
   matched brute force: `nH=15`, 735 columns both ways, same set, status `OPTIMAL`, wall 0.5272s.
 - On current R173 d12 frontier row 0, CP-SAT and brute force both found 0 diagonal-valid columns; the
   first 20 rows of shard-82 frontier also matched brute force with 0 columns.  This was an algorithmic
   smoke test only: partial rows are not terminal-H Stage-B pruning objects.

VERDICT:
A concrete Stage-B tooling gap was closed for the diagonal equation, but the 99-graph problem was
unchanged.  R176 supersedes this by adding compatibility/clique/closure validation on top of the columns.

NEXT ACTION:
Use the R176 full Stage-B prototype rather than the R175 diagonal-only prototype for future terminal-H
validation work.

---

## R174 -- edge-vector Gram probe repaired and run on R173 d12 frontiers [2026-06-30]
## OUTCOME: diagnostic tool fixed; invariant validated but non-pruning at depth 12.

ARTIFACTS:
 - note: `EDGE_VECTOR_GRAM_R174.md`
 - updated script: `s3_edge_vector_gram_probe.py`
 - outputs:
   `scratchpad\r3_d12_frontier_strata_r173_082_083.json`,
   `scratchpad\edge_vector_gram_probe_r173_082.json`,
   `scratchpad\edge_vector_gram_probe_r173_083.json`

VALIDATION / RESULTS:
 - `s3_edge_vector_gram_probe.py` now accepts current frontier graph rows with `k` as well as older
   rows with `depth`.
 - `python -m py_compile s3_edge_vector_gram_probe.py` passed.
 - `python s3_edge_vector_gram_probe.py --self-test` passed on real controls T(7) and rook9.
 - R173 shard 82/83 d12 frontier strata: 21,733 rows, edges min/max/mean `6/25/18.229`, triangles
   min/max/mean `0/7/2.464`, max `lambda2=2.604789`, min `lambda_min=-3.309592`, spectral gate
   violations 0.
 - Edge-vector Gram scans on the two frontiers: 0 negative/rank/upper violations; max rank 11;
   max largest eigenvalue 157.2921 and 154.5928 versus the srg99 bound 539.

VERDICT:
This repairs a real measurement bug and gives clean negative evidence: the edge-vector Gram invariant is
now runnable on current r=3 frontiers, but it is far from pruning depth-12 rows.  Keep it as a diagnostic
for deeper/denser frontiers; do not promote it to a claimed gate without new evidence.

NEXT ACTION:
For a new pruning lever, target a genuinely different invariant (for example a partial-linear-space
hexagon/order-six capacity bound) and validate it on real witnesses before trying it on r=3 frontiers.

---

## R173 -- exact r=3 d11->d12 shards 82..83 completed; known coverage now 87/512 [2026-06-30]
## OUTCOME: one-command cloud measurement remains healthy; no prune and no proof.

ARTIFACTS:
 - note: `R3_CLOUD_SHARDS_R173.md`
 - outputs:
   `scratchpad\r3_d11_to_d12_shard512_exact_r173_082.json`,
   `scratchpad\r3_d11_to_d12_shard512_exact_r173_083.json`,
   `scratchpad\r3_d11_to_d12_shard512_082_083_exact_aggregate_r173.json`,
   `scratchpad\r3_d11_to_d12_shard512_known87_aggregate_r173.json`,
   `scratchpad\r3_d11_to_d12_frontiers\r3_d11_to_d12_shard512_exact_r173_082_frontier.jsonl`,
   `scratchpad\r3_d11_to_d12_frontiers\r3_d11_to_d12_shard512_exact_r173_083_frontier.jsonl`

VALIDATION / RESULTS:
 - `s3_cloud_r3_d12.py --help` passed and the dry-run resolved to the expected `s3_run_shards.py`
   command.  No prior shard 82/83 stats were present.
 - Shard 82: 906 parents -> 10,532 depth-12 children; branch 11.6247; wall 138.58s; no
   budget/time/sample flags; local/spectral/triangle prunes all 0; frontier rows written.
 - Shard 83: 906 parents -> 11,201 depth-12 children; branch 12.3631; wall 134.12s; no
   budget/time/sample flags; local/spectral/triangle prunes all 0; frontier rows written.
 - Updated known aggregate over shards `0..83,128,256,384`: 78,821/463,636 depth-11 parents
   (17.0006%), 1,148,361 measured depth-12 children, diagnostic scaled `N12 ~= 6.7548e6`.

VERDICT:
The primary R43 r=3 cloud measurement route remains one-command runnable and reproducible.  It is still
only a cost/frontier measurement: no local, spectral, or triangle-split pruning has fired by depth 12,
and no Stage-B/CRS conclusion is sound before completed 45-vertex star complements exist.

NEXT ACTION:
Next contiguous exact shards are 84..85 if continuing the measurement.  Higher-leverage alternatives are
to add a real terminal-H Stage-B generator/solver, or find a new structural gate that can be validated on
known witnesses before adding it to Stage-A.

---

## R172 -- row-representative symmetry lifts for local Farkas cuts [2026-06-30]
## OUTCOME: sound lifted cut libraries built; row 0 still SAT, but branch cost drops sharply.

ARTIFACTS:
 - note: `ROOT_CELL_FARKAS_LIFT_R172.md`
 - new scripts:
   `root_cell_farkas_lift.py`,
   `root_cell_farkas_lift_single.py`
 - key outputs:
   `scratchpad\root_cell_pair_farkas_lift_rep0_sig_r172.json`,
   `scratchpad\root_cell_pair_farkas_lift_rep0_pairmin2_r172.json`,
   `scratchpad\root_cell_single_farkas_lift_rep0_outmin2_r172.json`,
   `scratchpad\root_cell_row_layer_paircap_rep0_singlelift46_pairlift130_t120_r172.json`,
   `scratchpad\root_cell_fixed_y_local_farkas_rep0_singlelift46_pairlift130_witness_rat64_r172.json`

VALIDATION / RESULTS:
 - `python -m py_compile root_cell_farkas_lift.py root_cell_farkas_lift_single.py` passed.
 - Row representative 0 has 16 actual automorphisms inside the 7,680-permutation fixed-label
   stabilizer.  The broad R171 rooted-label orbits are not automatically sound; R172 only lifts along
   this row-representative-preserving subgroup.
 - Every emitted lifted cut was rebuilt from the transformed fixed-y witness and rechecked as an exact
   integer Farkas contradiction.  Pair lifts: 13 exact source pair certificates -> 208 exact lifted
   images -> 130 one-per-pair cuts.  Single lifts: accumulated exact one-outside sources -> 560 exact
   lifted images -> 46 one-per-outside cuts.
 - Row-0 measurement, 120s cap, 16 workers: R168's 15 one-outside cuts found SAT in 85.6612s with
   194,733 branches.  The best R172 lifted library (46 single-min + 130 pair-min cuts) still found SAT,
   but in 59.0780s with 13,171 branches.
 - Residual scan of that best witness still found 8 fresh exact one-outside Farkas certificates.

VERDICT:
Actual row-representative symmetry lifting is a sound propagation improvement and a reusable validation
tool, but it does not close row representative 0.  Fresh exact local obstructions continue to regenerate,
so blind Benders accumulation is not a finite proof route on the current evidence.

NEXT ACTION:
Stop treating row-layer Farkas accumulation as the decisive line unless a new finite template theorem is
proved.  Use the lifted libraries as diagnostics/propagation aids, and pivot back to a proof-status-aware
lever: Stage-B shadow checks on r=3 frontiers, a cloud measurement slice, or a new structural obstruction.

---

## R171 -- pair-local Farkas orbit recurrence measured [2026-06-30]
## OUTCOME: reusable diagnostic added; repeated pair-certificate orbits found, but no finite library yet.

ARTIFACTS:
 - note: `ROOT_CELL_PAIR_ORBITS_R171.md`
 - new script: `root_cell_farkas_orbits.py`
 - outputs:
   `scratchpad\root_cell_fixed_y_pair_farkas_rep0_6localcores_skip_single_all_r171.json`,
   `scratchpad\root_cell_fixed_y_pair_farkas_rep0_12localcores_skip_single_all_r171.json`,
   `scratchpad\root_cell_fixed_y_pair_farkas_rep0_15localcores_skip_single_all_r171.json`,
   `scratchpad\root_cell_pair_farkas_orbits_r171.json`

VALIDATION / RESULTS:
 - `python -m py_compile root_cell_farkas_orbits.py` passed.
 - Pair-only scans skipping one-outside failures:
   6-core witness: 2,211 pairs scanned, 0 exact pair certificates;
   12-core witness: 2,145 pairs scanned, 0 exact pair certificates;
   15-core witness: 2,145 pairs scanned, 3 exact pair certificates.
 - Together with the two R170 pair-scan files, 9 exact pair-only certificates collapse to 6 rooted-label
   orbits under the fixed-label stabilizer.
 - Three orbits recur twice: `((0,4),(4,6))`, `((1,4),(4,6))`, `((1,4),(5,6))`.

VERDICT:
Pair-local certificates show some orbit recurrence, so they are not pure one-off noise.  The evidence is
not yet strong enough for a finite obstruction library.  Template mining should focus on the repeated
orbits and must stay certificate-backed.

NEXT ACTION:
Mine multiplier/support templates for the repeated pair orbits, or pivot to Stage-B shadow checks if
pair templates stay witness-specific.

---

## R170 -- pair-local symmetric Farkas cuts tested [2026-06-30]
## OUTCOME: strongest rooted-residual pressure so far; still no row prune.

ARTIFACTS:
 - note: `ROOT_CELL_PAIR_FARKAS_R170.md`
 - updated scripts:
   `root_cell_fixed_y_farkas.py`,
   `root_cell_row_layer_cpsat.py`
 - outputs:
   `scratchpad\root_cell_fixed_y_pair_farkas_rep0_farkascuts15_skip_single_300_r170.json`,
   `scratchpad\root_cell_fixed_y_pair_farkas_rep0_farkascuts15_skip_single_all_r170.json`,
   `scratchpad\root_cell_row_layer_paircap_rep0_farkascuts15_pair2_t120_r170.json`,
   `scratchpad\root_cell_row_layer_paircap_rep0_farkascuts15_pair2_t240_r170.json`,
   `scratchpad\root_cell_fixed_y_pair_farkas_rep0_farkascuts15_minrows_skip_single_all_r170.json`,
   `scratchpad\root_cell_row_layer_paircap_rep0_farkascuts15_pair6_t120_r170.json`,
   `scratchpad\root_cell_row_layer_paircap_rep0_farkascuts15_pair6_t240_r170.json`

CHANGES:
 - `root_cell_fixed_y_farkas.py --scan-outside-pairs` scans two-outside local LPs; with
   `--skip-single-nonoptimal`, any hit is a joint obstruction among individually feasible outside
   vertices.
 - `root_cell_row_layer_cpsat.py --farkas-cut-json` now accepts pair-scan certificates and projects
   multi-outside Farkas inequalities over shared outside-edge coefficients.

VALIDATION / RESULTS:
 - `python -m py_compile root_cell_row_layer_cpsat.py root_cell_fixed_y_farkas.py` passed.
 - On the R168 15-cut witness, skipping single-local failures scanned 2,080 outside pairs and found 2
   exact pair-local certificates: pairs `[39,67]` and `[40,67]`.
 - On the R169 minimized-cut witness, skipping single-local failures scanned 2,016 outside pairs and
   found 4 exact pair-local certificates: pairs `[6,75]`, `[8,75]`, `[22,78]`, `[69,78]`.
 - 15 one-outside cuts only: SAT in 85.6612s.
 - 15 one-outside cuts + 2 pair-local cuts: `UNKNOWN` at both 120s and 240s.
 - 15 one-outside cuts + 6 pair-local cuts: `UNKNOWN` at both 120s and 240s.

VERDICT:
Pair-local Farkas cuts are the strongest rooted-residual cut family so far.  They expose exact joint
obstructions not visible to one-outside scans and push row representative 0 beyond 240s.  However,
timeouts are not proofs: no row representative is pruned and the 99-graph problem remains open.

NEXT ACTION:
Continue only with bounded proof-status-aware pair-local Benders learning, or search for compact/orbit
templates among pair certificates.  Do not report nonexistence from CP-SAT `UNKNOWN`.

---

## R169 -- greedy row-minimization of Farkas certificates tested [2026-06-30]
## OUTCOME: sound simplifier, but weaker row-layer pruning; do not prefer minimized cuts.

ARTIFACTS:
 - note: `ROOT_CELL_FARKAS_MINROWS_R169.md`
 - updated script: `root_cell_fixed_y_farkas.py`
 - outputs:
   `scratchpad\root_cell_fixed_y_local_farkas_rep0_15localcores_minrows_rat64_r169.json`,
   `scratchpad\root_cell_fixed_y_local_farkas_rep0_farkascuts5_t120_minrows_rat64_r169.json`,
   `scratchpad\root_cell_fixed_y_local_farkas_rep0_farkascuts9_15cores_minrows_rat64_r169.json`,
   `scratchpad\root_cell_fixed_y_local_farkas_rep0_farkascuts15_minrows_rat64_r169.json`,
   `scratchpad\root_cell_row_layer_paircap_rep0_farkascuts15_minrows_t120_r169.json`,
   `scratchpad\root_cell_fixed_y_local_farkas_rep0_farkascuts15_minrows_witness_minrows_rat64_r169.json`

CHANGE:
`root_cell_fixed_y_farkas.py --minimize-rows` greedily zeros active Farkas multipliers while preserving
the exact box-bound contradiction.

VALIDATION / RESULTS:
 - `python -m py_compile root_cell_fixed_y_farkas.py root_cell_row_layer_cpsat.py` passed.
 - Minimized certificates remain exact contradictions.
 - Some certificates shrink modestly (examples: 23->19, 20->17, 25->21, 24->20, 15->12 active rows),
   but most do not collapse.
 - Non-minimized 15-cut row-layer run: SAT in 85.6612s, 2,337 conflicts, 194,733 branches.
 - Minimized 15-cut row-layer run: SAT in 33.3453s, 704 conflicts, 72,682 branches.
 - The minimized-cut witness remains full-LP infeasible and has 7/7 rational exact local certificates.

VERDICT:
Greedy row-minimization is sound but counterproductive as a row-layer cut strategy: removing rows makes
cuts cheaper but also weaker.  The removed equations help propagation even when not required for the
source contradiction.  Keep raw certificates for cutting unless a different minimization objective is
defined.

NEXT ACTION:
Do not spend more time on naive row-minimization.  Try canonical/orbit grouping of raw certificates,
pair-local symmetric Farkas cuts, or Stage-B shadow checks.

---

## R168 -- symbolic local-Farkas/Benders cuts added to row-layer CP-SAT [2026-06-30]
## OUTCOME: genuine formulation improvement and solver-pressure evidence; row 0 still not pruned.

ARTIFACTS:
 - note: `ROOT_CELL_FARKAS_BENDERS_R168.md`
 - updated script: `root_cell_row_layer_cpsat.py`
 - outputs:
   `scratchpad\root_cell_row_layer_rook_empty_farkascut_r168.json`,
   `scratchpad\root_cell_row_layer_paircap_rep0_farkascuts5_t120_r168.json`,
   `scratchpad\root_cell_fixed_y_local_farkas_rep0_farkascuts5_t120_rat64_r168.json`,
   `scratchpad\root_cell_row_layer_paircap_rep0_farkascuts9_t120_r168.json`,
   `scratchpad\root_cell_row_layer_paircap_rep0_farkascuts9_15cores_t120_r168.json`,
   `scratchpad\root_cell_fixed_y_local_farkas_rep0_farkascuts9_15cores_rat64_r168.json`,
   `scratchpad\root_cell_row_layer_paircap_rep0_farkascuts15_t120_r168.json`,
   `scratchpad\root_cell_fixed_y_local_farkas_rep0_farkascuts15_rat64_r168.json`

MODEL:
`root_cell_row_layer_cpsat.py --farkas-cut-json` now reads exact one-outside Farkas certificates and
adds the projected Benders inequality `lower(mA(y,z)) <= m b(y,z) <= upper(mA(y,z))` directly over
row-layer z/y variables, using exact integer multipliers from the certificate.  This cuts certificate
violations without freezing a literal assignment.

VALIDATION / RESULTS:
 - `python -m py_compile root_cell_row_layer_cpsat.py root_cell_fixed_y_farkas.py
   root_cell_core_learning_loop.py` passed.
 - Independent exact evaluator confirmed that all five R163 certificates violate the derived symbolic
   box-bound inequality on their source witness with the expected gaps.
 - Rook control with an empty rational Farkas scan file stayed SAT.
 - Five symbolic cuts from the R163 15-core witness changed row-0 behavior from quick SAT to:
   `UNKNOWN` at 60s, then SAT in 71.5558s under a 120s cap.  The regenerated witness remains full-LP
   infeasible and has 4/4 rational exact local certificates.
 - Nine cuts alone were `UNKNOWN` at 120.0136s.
 - Nine cuts plus the prior 15 literal cores found SAT in 21.8184s; the witness remains LP-dead and has
   6/6 rational exact local certificates.
 - Fifteen cuts alone still found SAT in 85.6612s; the witness remains LP-dead and has 6/6 rational exact
   local certificates.

VERDICT:
Symbolic Farkas cuts are the first rooted-residual cut family that visibly stresses row-0 witness
generation more than literal cores, but they are not decisive yet.  Do not report a row prune.  Blindly
adding more raw certificates is likely to become another loop; the next local lever should minimize or
canonicalize certificates, or move to pair-local/symmetric Farkas systems.

SCAMPER / ROUTING NOTE:
Six independent SCAMPER side passes converged on the same priority: replace literal local cores with
symbolic/canonical Farkas cuts, then fall back to Stage-B shadow checks or deep spectral telemetry if
the certificate family stays witness-specific.

NEXT ACTION:
Either (A) build a certificate minimization/canonicalization pass and measure recurrence/strength of
smaller symbolic cuts, or (B) implement a Stage-B shadow feasibility check on sampled r=3 d12 frontiers.
Avoid further shallow d12 shard counting unless a new predicate changes the measured branching.

---

## R167 -- exact r=3 d11->d12 shards 80..81 completed; known coverage now 85/512 [2026-06-30]
## OUTCOME: proof-grade cloud measurement coverage advanced again; problem remains open.

ARTIFACTS:
 - note: `R3_CLOUD_SHARDS_R167.md`
 - outputs:
   `scratchpad\r3_d11_to_d12_shard512_exact_r167_080.json`,
   `scratchpad\r3_d11_to_d12_shard512_exact_r167_081.json`,
   `scratchpad\r3_d11_to_d12_shard512_080_081_exact_aggregate_r167.json`,
   `scratchpad\r3_d11_to_d12_shard512_known85_aggregate_r167.json`,
   matching frontier JSONL files in `scratchpad\r3_d11_to_d12_frontiers\`

COMMAND:
`python s3_cloud_r3_d12.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --indices 80-81 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --tag r3_d11_to_d12_shard512_exact_r167 --aggregate-out scratchpad\r3_d11_to_d12_shard512_080_081_exact_aggregate_r167.json --skip-gate`

RESULTS:
 - shard 80/512: 906 depth-11 parents -> 13,402 depth-12 children, branch 14.792, wall 131.80s.
 - shard 81/512: 906 depth-11 parents -> 11,488 depth-12 children, branch 12.680, wall 133.41s.
 - No budget/time/sample flags; prune counters remained zero.
 - Frontier physical recounts matched stats exactly: 13,402 and 11,488 rows.
 - Two-shard aggregate: 24,890 depth-12 children, diagnostic scaled `N12 ~ 6.3686e6`.
 - Updated known aggregate covers shards `0..81,128,256,384`: 77,009 / 463,636 depth-11 parents
   (16.61%), 1,126,628 measured depth-12 children, diagnostic scaled `N12 ~ 6.7829e6`.

VERDICT:
Exact r=3 measured coverage continues to advance.  The known-shard scaled estimate remains stable near
6.8e6 and no d11->d12 prune category has fired.  Still no construction or nonexistence proof.

NEXT ACTION:
Continue exact coverage on the next contiguous pair `82..83`, or switch only for a genuine new
predicate/cut that can change measured d12 branching.

---

## R166 -- exact r=3 d11->d12 shards 78..79 completed; known coverage now 83/512 [2026-06-30]
## OUTCOME: proof-grade cloud measurement coverage advanced again; problem remains open.

ARTIFACTS:
 - note: `R3_CLOUD_SHARDS_R166.md`
 - outputs:
   `scratchpad\r3_d11_to_d12_shard512_exact_r166_078.json`,
   `scratchpad\r3_d11_to_d12_shard512_exact_r166_079.json`,
   `scratchpad\r3_d11_to_d12_shard512_078_079_exact_aggregate_r166.json`,
   `scratchpad\r3_d11_to_d12_shard512_known83_aggregate_r166.json`,
   matching frontier JSONL files in `scratchpad\r3_d11_to_d12_frontiers\`

COMMAND:
`python s3_cloud_r3_d12.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --indices 78-79 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --tag r3_d11_to_d12_shard512_exact_r166 --aggregate-out scratchpad\r3_d11_to_d12_shard512_078_079_exact_aggregate_r166.json --skip-gate`

RESULTS:
 - shard 78/512: 906 depth-11 parents -> 13,908 depth-12 children, branch 15.351, wall 134.82s.
 - shard 79/512: 906 depth-11 parents -> 13,661 depth-12 children, branch 15.078, wall 132.37s.
 - No budget/time/sample flags; prune counters remained zero.
 - Frontier physical recounts matched stats exactly: 13,908 and 13,661 rows.
 - Two-shard aggregate: 27,569 depth-12 children, diagnostic scaled `N12 ~ 7.0541e6`.
 - Updated known aggregate covers shards `0..79,128,256,384`: 75,197 / 463,636 depth-11 parents
   (16.22%), 1,101,738 measured depth-12 children, diagnostic scaled `N12 ~ 6.7929e6`.

VERDICT:
Exact r=3 measured coverage continues to advance, but the known-shard scaled estimate remains stable
near 6.8e6 and no d11->d12 prune category has fired.  Still no construction or nonexistence proof.

NEXT ACTION:
Continue exact coverage on the next contiguous pair `80..81`, or switch only for a genuine new
predicate/cut that can change measured d12 branching.

---

## R165 -- exact r=3 d11->d12 shards 76..77 completed; known coverage now 81/512 [2026-06-30]
## OUTCOME: proof-grade cloud measurement coverage advanced again; no construction/nonexistence proof.

ARTIFACTS:
 - note: `R3_CLOUD_SHARDS_R165.md`
 - outputs:
   `scratchpad\r3_d11_to_d12_shard512_exact_r165_076.json`,
   `scratchpad\r3_d11_to_d12_shard512_exact_r165_077.json`,
   `scratchpad\r3_d11_to_d12_shard512_076_077_exact_aggregate_r165.json`,
   `scratchpad\r3_d11_to_d12_shard512_known81_aggregate_r165.json`,
   matching frontier JSONL files in `scratchpad\r3_d11_to_d12_frontiers\`

COMMAND:
`python s3_cloud_r3_d12.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --indices 76-77 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --tag r3_d11_to_d12_shard512_exact_r165 --aggregate-out scratchpad\r3_d11_to_d12_shard512_076_077_exact_aggregate_r165.json --skip-gate`

RESULTS:
 - shard 76/512: 906 depth-11 parents -> 11,519 depth-12 children, branch 12.714, wall 134.49s.
 - shard 77/512: 906 depth-11 parents -> 13,440 depth-12 children, branch 14.834, wall 135.96s.
 - No budget/time/sample flags; prune counters remained zero.
 - Frontier physical recounts matched stats exactly: 11,519 and 13,440 rows.
 - Two-shard aggregate: 24,959 depth-12 children, diagnostic scaled `N12 ~ 6.3863e6`.
 - Updated known aggregate covers shards `0..77,128,256,384`: 73,385 / 463,636 depth-11 parents
   (15.83%), 1,074,169 measured depth-12 children, diagnostic scaled `N12 ~ 6.7864e6`.

VERDICT:
Exact r=3 measured coverage continues to advance.  Shard 76 is below recent branch average, but the
known-shard scaled estimate remains near 6.8e6 and no d11->d12 prune category has fired.  This still
does not decide the 99-graph problem.

NEXT ACTION:
Continue exact coverage on the next contiguous pair `78..79`, or switch only for a genuine new
predicate/cut that can change the measured d12 branching.

---

## R164 -- exact r=3 d11->d12 shards 74..75 completed; known coverage now 79/512 [2026-06-30]
## OUTCOME: proof-grade cloud measurement coverage advanced; no construction/nonexistence proof.

ARTIFACTS:
 - note: `R3_CLOUD_SHARDS_R164.md`
 - outputs:
   `scratchpad\r3_d11_to_d12_shard512_exact_r164_074.json`,
   `scratchpad\r3_d11_to_d12_shard512_exact_r164_075.json`,
   `scratchpad\r3_d11_to_d12_shard512_074_075_exact_aggregate_r164.json`,
   `scratchpad\r3_d11_to_d12_shard512_known79_aggregate_r164.json`,
   matching frontier JSONL files in `scratchpad\r3_d11_to_d12_frontiers\`

COMMAND:
`python s3_cloud_r3_d12.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --indices 74-75 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --tag r3_d11_to_d12_shard512_exact_r164 --aggregate-out scratchpad\r3_d11_to_d12_shard512_074_075_exact_aggregate_r164.json --skip-gate`

RESULTS:
 - shard 74/512: 906 depth-11 parents -> 13,341 depth-12 children, branch 14.725, wall 134.02s.
 - shard 75/512: 906 depth-11 parents -> 14,089 depth-12 children, branch 15.551, wall 134.66s.
 - No budget/time/sample flags; prune counters remained zero.
 - Frontier physical recounts matched stats exactly: 13,341 and 14,089 rows.
 - Two-shard aggregate: 27,430 depth-12 children, diagnostic scaled `N12 ~ 7.0185e6`.
 - Updated known aggregate covers shards `0..75,128,256,384`: 71,573 / 463,636 depth-11 parents
   (15.44%), 1,049,210 measured depth-12 children, diagnostic scaled `N12 ~ 6.7966e6`.

VERDICT:
The exact r=3 one-command measurement route remains healthy and reproducible, but still no local,
spectral, or triangle-split prune fires at d11->d12.  This is frontier/cost evidence, not a decision.

NEXT ACTION:
Continue exact coverage on the next contiguous pair `76..77`, or pause cloud counting only for a genuine
new predicate/cut that could change the d12 branching.

---

## R163 -- rational local-Farkas recovery + bounded multi-core test + r=3 shards 72..73 [2026-06-30]
## OUTCOME: validation strengthened and exact N12 coverage advanced; row 0 still not pruned.

ARTIFACTS:
 - note: `ROOT_CELL_MULTICORE_RATIONAL_R163.md`
 - updated scripts:
   `root_cell_core_learning_loop.py`,
   `root_cell_fixed_y_farkas.py`
 - rooted residual outputs:
   `scratchpad\root_cell_multicore_rook_r163_summary.json`,
   `scratchpad\root_cell_multicore_loop_r163_summary.json`,
   `scratchpad\root_cell_row_layer_paircap_rep0_12localcores_r163.json`,
   `scratchpad\root_cell_fixed_y_local_farkas_rep0_12localcores_rat64_r163.json`,
   `scratchpad\root_cell_rational_core_loop_r163_summary.json`,
   `scratchpad\root_cell_row_layer_paircap_rep0_15localcores_r163.json`,
   `scratchpad\root_cell_fixed_y_local_farkas_rep0_15localcores_rat64_r163.json`
 - cloud outputs:
   `scratchpad\r3_d11_to_d12_shard512_exact_r163_072.json`,
   `scratchpad\r3_d11_to_d12_shard512_exact_r163_073.json`,
   `scratchpad\r3_d11_to_d12_shard512_072_073_exact_aggregate_r163.json`,
   `scratchpad\r3_d11_to_d12_shard512_known77_aggregate_r163.json`,
   matching frontier JSONL files in `scratchpad\r3_d11_to_d12_frontiers\`

CHANGES:
 - `root_cell_core_learning_loop.py --local-cores-per-iter N` can now extract several exact
   one-outside local cores from one row-layer witness before regenerating.
 - `root_cell_fixed_y_farkas.py --rational-denominator-limit D` now scales dual rays close to small
   rationals into exact integer Farkas multipliers.  Default `D=1` preserves the prior integer-only
   behavior.

VALIDATION / RESULTS:
 - `python -m py_compile root_cell_core_learning_loop.py root_cell_fixed_y_farkas.py` passed.
 - Rook control with `--local-core --local-cores-per-iter 2` learned zero cores; rational local-Farkas
   scan with denominator limit 64 also found no local failure.
 - From the six R160-R162 local cores, a two-iteration `--local-cores-per-iter 3` run learned six more
   exact local cores with sizes `[101,48,84]` and `[51,54,80]`; final core count 12.
 - With 12 cores forbidden, row representative 0 remained `OPTIMAL` in 7.6658s.  The witness was still
   full-LP infeasible.  Integer-only local scan gave 5 local failures but only 1 exact certificate;
   rational denominator 64 recovered exact certificates for all 5.
 - A further rational-cert pass from the 12-core state learned three more exact local cores
   `[116,86,85]`; with all 15 cores forbidden, row 0 still remained `OPTIMAL` in 8.1588s and still
   had 5/5 rational exact local certificates plus full-LP infeasibility.
 - `python s3_slice_harness.py --gate` stayed ALL GREEN on rook(9) replay and exact T(7)
   reconstruction.
 - Exact r=3 d11->d12 shards 72 and 73 completed via `s3_cloud_r3_d12.py --indices 72-73 --skip-gate`:
   shard 72 produced 13,098 depth-12 children in 131.04s; shard 73 produced 13,376 in 134.32s.
   No budget/time/sample flags; frontier physical recounts matched stats exactly.
 - Updated known-shard aggregate covers shards `0..73,128,256,384`: 69,761 / 463,636 depth-11 parents
   (15.05%), 1,021,780 measured depth-12 children, diagnostic scaled `N12 ~ 6.7908e6`.

VERDICT:
Rational Farkas recovery is a real correctness/proof-artifact upgrade.  It should be kept for local
certificate scans.  But blind local-core accumulation is weak: even 15 exact local cores do not stress
row 0, and every regenerated witness remains LP-dead.  De-prioritize further core accumulation unless
it becomes a symbolic inequality or a genuinely different core-selection rule.

R43 STRUCTURAL SWITCH CONSOLIDATION:
The primary cloud measurement route remains the r=3 / 45-vertex star-complement pipeline.  R163 advanced
the exact one-command d11->d12 coverage from known 75 to known 77 shards.  The rooted residual work is a
separate local validation/cut-mining route and has not replaced the cloud plan.

NEXT ACTION:
For immediate measured progress, continue the r=3 exact d11->d12 wrapper on the next contiguous pair
`74..75`.  For local math progress, mine the rational local Farkas certificates for a symbolic row-layer
inequality; do not keep adding blind local cores without a new lever.

---

## R162 -- integrated local-row-outside formulation + six-core bounded test [2026-06-30]
## OUTCOME: sound stronger formulation and measured Benders progress; row 0 still not pruned.

ARTIFACTS:
 - note: `ROOT_CELL_LOCAL_ROW_OUTSIDE_R162.md`
 - updated script: `root_cell_row_layer_cpsat.py`
 - outputs:
   `scratchpad\root_cell_row_layer_local_rowoutside_k4_r162.json`,
   `scratchpad\root_cell_row_layer_local_rowoutside_rep0_r162.json`,
   `scratchpad\root_cell_local_core_loop_r162_summary.json`,
   `scratchpad\root_cell_local_core_loop_r162_iter00_row.json`,
   `scratchpad\root_cell_local_core_loop_r162_iter00_local_scan.json`,
   `scratchpad\root_cell_local_core_loop_r162_iter00_core.json`,
   `scratchpad\root_cell_local_core_loop_r162_iter01_row.json`,
   `scratchpad\root_cell_local_core_loop_r162_iter01_local_scan.json`,
   `scratchpad\root_cell_local_core_loop_r162_iter01_core.json`,
   `scratchpad\root_cell_local_core_loop_r162_iter02_row.json`,
   `scratchpad\root_cell_local_core_loop_r162_iter02_local_scan.json`,
   `scratchpad\root_cell_local_core_loop_r162_iter02_core.json`,
   `scratchpad\root_cell_row_layer_paircap_rep0_6localcores_r162.json`,
   `scratchpad\root_cell_fixed_y_local_farkas_rep0_6localcores_r162.json`,
   `scratchpad\root_cell_fixed_y_rowoutside_rep0_6localcores_lp_r162.json`

MODEL:
`root_cell_row_layer_cpsat.py --local-row-outside` adds directed variables `lo[o,w]` for each ordered
outside pair and enforces, for every outside vertex `o`, its exact residual `AN`, degree, and row-outside
star equations.  This internalizes the R160 one-outside obstruction while dropping the global edge
symmetry required by full `--row-outside`.

VALIDATION / RESULTS:
 - `python -m py_compile root_cell_row_layer_cpsat.py` passed.
 - rook control with `--outside-pair-cap --local-row-outside`: `OPTIMAL` in 0.0019s.
 - srg99 row representative 0 with `--outside-pair-cap --local-row-outside`: `UNKNOWN` at 60.0245s
   (1694 conflicts, 104107 branches).  The first monolithic encoding is sound but not decisive.
 - Bounded local-core loop seeded with the prior three local cores completed three more iterations:
   new cores of 76, 94, and 22 literals, all from exact local certificates.  Row-layer solves remained
   `OPTIMAL` with walls 8.0672s, 14.9841s, and 9.7855s.
 - With all six local cores (sizes 88, 26, 172, 76, 94, 22) forbidden, row representative 0 is still
   `OPTIMAL` in 10.433s.
 - The six-core witness is still dead: local scan finds 4 nonoptimal one-outside LPs and 3 exact local
   Farkas certificates; full fixed-y row_outside LP is infeasible.

VERDICT:
R162 strengthens the formulation and shows local cores have some search pressure, but row 0 still evades
six learned local cores and the monolithic local-row-outside model is not decisive at 60s.  Do not report
a row prune.  Avoid unbounded blind core accumulation.

NEXT ACTION:
Try symbolic or semi-symbolic local-Farkas cuts from exact local certificates.  Fallback: add a bounded
multi-core-per-witness learner that extracts several small exact local cores from each row witness, then
measure whether row-layer SAT rate/local failure count changes materially.  Stop if row 0 keeps easily
evading learned cores.

---

## R161 -- one-command local-core learning loop is runnable; first cores measured [2026-06-30]
## OUTCOME: local-core loop infrastructure accepted; row 0 still SAT after three local cores.

ARTIFACTS:
 - note: `ROOT_CELL_LOCAL_CORE_LOOP_R161.md`
 - updated script: `root_cell_core_learning_loop.py`
 - outputs:
   `scratchpad\root_cell_local_core_loop_r160_summary.json`,
   `scratchpad\root_cell_local_core_loop_r160_iter00_row.json`,
   `scratchpad\root_cell_local_core_loop_r160_iter00_local_scan.json`,
   `scratchpad\root_cell_local_core_loop_r160_iter00_core.json`,
   `scratchpad\root_cell_local_core_loop_r161_summary.json`,
   `scratchpad\root_cell_local_core_loop_r161_iter00_row.json`,
   `scratchpad\root_cell_local_core_loop_r161_iter00_local_scan.json`,
   `scratchpad\root_cell_local_core_loop_r161_iter00_core.json`

MODEL:
`root_cell_core_learning_loop.py --local-core` now runs the R160 pipeline end-to-end: generate a row-layer
witness under learned cores, scan one-outside LPs, select a locally infeasible outside vertex (preferring
fewest-row exact Farkas certificates), extract a local z/y CP-SAT assumption core, and feed it into the
next iteration.

VALIDATION / RESULTS:
 - `python -m py_compile root_cell_core_learning_loop.py root_cell_fixed_y_core.py
   root_cell_fixed_y_farkas.py root_cell_row_layer_cpsat.py` passed.
 - Smoke 1, seeded with the R160 88-literal local core: row-layer `OPTIMAL` in 7.3760s; local scan
   found 9 nonoptimal one-outside LPs and 7 exact certificates; selected outside 61 label `[6,9]`
   with a 16-row certificate; local core raw 36 literals, minimized to 26 (`z=True:2`, `y=True:20`,
   `y=False:4`).
 - Smoke 2, seeded with the 88-literal and 26-literal local cores: row-layer `OPTIMAL` in 9.0725s;
   local scan found 3 nonoptimal one-outside LPs and 2 exact certificates; selected outside 71 label
   `[7,13]`; local core raw 285 literals, minimized to 172 (`z=False:4`, `y=True:22`, `y=False:146`).
 - The loop is proof-status aware and stops by iteration limit here.  It has not pruned row
   representative 0; after three local cores, row 0 remains SAT in the row-layer pair-cap model.

VERDICT:
Local-core learning is now a runnable, smaller-core alternative to blind global core accumulation.
The first learned local-loop core is small (26 literals), but the next is already bulky (172), so this
is promising infrastructure, not a decisive result.

NEXT ACTION:
Run a bounded multi-iteration local-core loop and measure whether row-0 witness generation cost rises,
local infeasible vertices decrease, or row 0 becomes UNSAT.  If core sizes grow/churn without row-layer
impact, close the local-core route and pivot to symbolic local-Farkas cuts.

---

## R160 -- fixed-y row-outside kills localize to one-outside-vertex LPs [2026-06-30]
## OUTCOME: stronger obstruction localization; local core path validated but not decisive.

ARTIFACTS:
 - note: `ROOT_CELL_LOCAL_FARKAS_R160.md`
 - updated scripts:
   `root_cell_fixed_y_farkas.py`,
   `root_cell_fixed_y_core.py`
 - outputs:
   `scratchpad\root_cell_fixed_y_local_farkas_k4_r160.json`,
   `scratchpad\root_cell_fixed_y_local_farkas_rep0_r160.json`,
   `scratchpad\root_cell_fixed_y_local_farkas_rep0_alt1_r160.json`,
   `scratchpad\root_cell_fixed_y_local_farkas_rep0_alt2_r160.json`,
   `scratchpad\root_cell_fixed_y_local_farkas_rep0_alt3_r160.json`,
   `scratchpad\root_cell_fixed_y_local_farkas_rep0_alt4_r160.json`,
   `scratchpad\root_cell_fixed_y_local_farkas_rep0_coreforbid1_r160.json`,
   `scratchpad\root_cell_fixed_y_local_farkas_rep0_2coreforbid_r160.json`,
   `scratchpad\root_cell_fixed_y_local_farkas_rep0_3coreforbid_r160.json`,
   `scratchpad\root_cell_fixed_y_local_core_k4_r160.json`,
   `scratchpad\root_cell_fixed_y_local_core_rep0_2coreforbid_o18_min_r160.json`,
   `scratchpad\root_cell_row_layer_paircap_rep0_localcore_o18_r160.json`,
   `scratchpad\root_cell_fixed_y_local_farkas_rep0_after_localcore_r160.json`,
   `scratchpad\root_cell_fixed_y_rowoutside_rep0_after_localcore_lp_r160.json`

MODEL:
For a fixed outside vertex `o`, keep only the 14 local `AN` equations, the degree equation,
and the row-outside equations involving `o`.  For row representative 0 this is a 27-row LP over
the 70 variables `x_ow` with `0 <= x_ow <= 1`.  If this one-outside subsystem is infeasible, the
whole fixed-y outside residual system is infeasible.

VALIDATION / RESULTS:
 - `python -m py_compile root_cell_fixed_y_farkas.py root_cell_fixed_y_core.py
   root_cell_fixed_y_iis.py root_cell_fixed_y_residual_an.py` passed.
 - rook fixed-y local scan: scanned 1 outside vertex, 0 nonoptimal local LPs, 0 certificates.
 - all 8 measured killed row-0 fixed-y witnesses have at least one locally infeasible outside vertex.
   Counts `(nonoptimal local LPs, accepted exact certificates)`:
   original R149 `(8,4)`, R154 alt1 `(6,3)`, alt2 `(8,8)`, alt3 `(8,7)`, alt4 `(10,3)`,
   R156 core1 `(8,4)`, core2 `(4,3)`, R157 core3 `(4,3)`.  Total: 56 nonoptimal local LPs and
   35 accepted exact local Farkas certificates.
 - `root_cell_fixed_y_core.py --outside-index` local core control on rook outside 3 is `OPTIMAL`.
 - On R156 `2coreforbid` outside 18, the local Boolean model is infeasible in 0.0768s; raw CP-SAT
   assumption core 374 literals, deletion-minimized to 88 literals in 33.7s.
 - The existing row-layer `--forbid-core-json` path consumes this 88-literal local core.  With only
   that core forbidden, row representative 0 is still SAT in 6.6642s; the new witness matches only
   41/88 core literals and is again locally killed (9 nonoptimal local LPs, 7 exact local certificates;
   full fixed-y row_outside LP infeasible).

VERDICT:
The residual obstruction is often already visible in a single outside vertex's fractional neighbour
star.  This is a better certificate/core mining surface than the full 1917-row LP.  It still does not
prune row representative 0, and one local core is not enough.

R43 STRUCTURAL SWITCH CONSOLIDATION:
No change to the cloud route: r=3 / 45-vertex star-complement search remains the primary runnable
cloud measurement path.  R160 is a rooted-residual structural lever that may reduce row-layer search;
it is not a replacement for the R95+ exact r=3 cloud wrapper.

NEXT ACTION:
Build a bounded local-core learning loop or symbolic local-Farkas cut.  Acceptance criteria: row-0
UNSAT under consumed local cores, or measured evidence that local cores/cuts materially reduce witness
generation cost/diversity without over-pruning rook/known controls.  If cores churn like bulky R156/R157
cores, document the no-go and pivot to symbolic LP cuts.

---

## R159 -- exact Farkas certificate for one fixed-y row-outside LP kill [2026-06-30]
## OUTCOME: proof-grade certificate for the original R149 fixed-y witness; not yet a reusable row cut.

ARTIFACTS:
 - note: `ROOT_CELL_FARKAS_R159.md`
 - new script: `root_cell_fixed_y_farkas.py`
 - outputs:
   `scratchpad\root_cell_fixed_y_farkas_k4_r159.json`,
   `scratchpad\root_cell_fixed_y_farkas_rep0_r159.json`,
   `scratchpad\root_cell_fixed_y_farkas_k4_r159_check.json`,
   `scratchpad\root_cell_fixed_y_farkas_rep0_r159_check.json`,
   `scratchpad\root_cell_fixed_y_farkas_rep0_coreforbid1_r159_check.json`,
   `scratchpad\root_cell_fixed_y_farkas_rep0_2coreforbid_r159_check.json`,
   `scratchpad\root_cell_fixed_y_farkas_rep0_3coreforbid_r159_check.json`

METHOD:
For a fixed row-layer witness, the residual LP is `A x = b, 0 <= x <= 1`.  A row
multiplier vector `m` is an exact box certificate if `m^T b` lies outside the interval
`[sum min(0,c_j), sum max(0,c_j)]`, where `c=m^T A`.  `root_cell_fixed_y_farkas.py`
extracts a HiGHS dual ray, accepts it only when it rounds to integers under tolerance, and then
recomputes the contradiction using integer arithmetic.

VALIDATION / RESULTS:
 - `python -m py_compile root_cell_fixed_y_farkas.py root_cell_fixed_y_iis.py
   root_cell_fixed_y_residual_an.py root_cell_row_layer_cpsat.py root_cell_core_learning_loop.py`
   passed.
 - rook fixed-y control with `--row-outside`: feasible (`model=Optimal`, zero outside-edge vars, no
   certificate), so the extractor does not invent a contradiction on a real witness control.
 - original R149 representative-0 fixed-y witness: exact 17-row Farkas certificate, all rows involving
   outside vertex 74 with label `[8,12]`; active rows are 8 `AN`, 1 `degree`, and 8 `row_outside`.
   The exact integer check gives `m^T b=-7`, box lower `-5`, gap `2`, so infeasibility is certified
   over the continuous box before integrality.
 - later core-forbidden row-0 fixed-y witnesses (`coreforbid1_r156`, `2coreforbid_r156`,
   `3coreforbid_r157`) are still LP-infeasible with HiGHS dual rays, but those rays do not round to
   small integers under this conservative extractor.  No exact certificates were accepted for them.
 - Replaying the 17-row certificate as a label-level template kills only the original R149 witness.
   It does not kill R154 alt1-4 or the three core-forbidden witnesses, so it is not a row-layer cut.

VERDICT:
R159 converts one fixed-y solver status into a compact, checkable Farkas proof and confirms that the
R158 LP obstruction can be small.  It does not prune row representative 0 and does not solve the
99-graph problem.

R43 STRUCTURAL SWITCH CONSOLIDATION:
The primary cloud measurement route remains the R43 r=3 / 45-vertex star-complement pipeline with the
R95+ one-command d11->d12 wrapper in `CLOUD_SPEC_SC.md`.  The rooted residual work is a separate local
structural lever; do not regress the cloud plan to the older s=-4-first route.

NEXT ACTION:
Mine sparse exact LP certificates or derive a symbolic row-layer inequality from row-outside equations.
Acceptance requires either a reusable cut that never over-prunes real controls, or an honest no-go with
evidence.  Avoid broad dense ray rationalization and blind bulky CP-SAT core accumulation.

---

## R158 -- fixed-y row-outside kills are already continuous LP infeasible [2026-06-30]
## OUTCOME: important steering correction; row-outside contradiction is linear/bounds, not integrality.

ARTIFACTS:
 - note: `ROOT_CELL_LP_RELAXATION_R158.md`
 - updated script: `root_cell_fixed_y_residual_an.py`
 - new diagnostics:
   `root_cell_fixed_y_iis.py`,
   `root_cell_fixed_y_lp_groups.py`
 - outputs:
   `scratchpad\root_cell_fixed_y_rowoutside_k4_lp_r158.json`,
   `scratchpad\root_cell_fixed_y_rowoutside_rep0_lp_r158.json`,
   `scratchpad\root_cell_fixed_y_anonly_rep0_lp_r158.json`,
   `scratchpad\root_cell_fixed_y_rowoutside_rep0_coreforbid1_lp_r158.json`,
   `scratchpad\root_cell_fixed_y_rowoutside_rep0_2coreforbid_lp_r158.json`,
   `scratchpad\root_cell_fixed_y_rowoutside_rep0_3coreforbid_lp_r158.json`,
   `scratchpad\root_cell_fixed_y_iis_rep0_r158.json`,
   `scratchpad\root_cell_fixed_y_iis_rep0_r158b.json`

MODEL:
`root_cell_fixed_y_residual_an.py --backend lp` runs the same residual linear system as MILP, but with
continuous variables `0 <= x_ab <= 1`.

VALIDATION / RESULTS:
 - `python -m py_compile root_cell_fixed_y_residual_an.py` passed.
 - rook fixed-y control with `--backend lp --row-outside`: feasible.
 - original R149 row-0 witness: outside `degree+AN` alone is LP feasible; adding row-outside equations
   makes the continuous box LP infeasible.
 - three later row-0 core-forbidden witnesses are also LP infeasible under row-outside:
   `coreforbid1_r156`, `2coreforbid_r156`, and `3coreforbid_r157`.
 - Each LP-infeasible system has 2485 outside-edge variables, 1917 equality constraints, and 852
   row-outside constraints.
 - HiGHS IIS access was probed via `root_cell_fixed_y_iis.py`; HiGHS confirms infeasibility but returns
   valid-empty IIS row/column lists in this Python binding.  Broad LP group localization attempts were
   too slow and produced no accepted artifact, so they are not evidence.

VERDICT:
For measured row-0 fixed-y witnesses, the R153/R154 contradiction is not an integrality phenomenon.
It already follows from real linear equations plus box bounds.  This is a better target than SAT core
accumulation: seek linear/bounds IIS, Farkas certificates, or analytic row-outside inequalities.

NEXT ACTION:
Derive or compute a usable LP/Farkas-style row-outside certificate.  Avoid blind bulky CP-SAT core
accumulation; the obstruction lives in continuous linear feasibility after `y` is fixed.

---

## R157 -- bounded fixed-y core-learning loop is runnable, but bulky cores do not prune row 0 [2026-06-30]
## OUTCOME: one-command core-learning infrastructure; steering result against blind core accumulation.

ARTIFACTS:
 - note: `ROOT_CELL_CORE_LOOP_R157.md`
 - new script: `root_cell_core_learning_loop.py`
 - outputs:
   `scratchpad\root_cell_core_loop_r157_summary.json`,
   `scratchpad\root_cell_core_loop_r157_iter00_row.json`,
   `scratchpad\root_cell_core_loop_r157_iter00_fixed.json`,
   `scratchpad\root_cell_core_loop_r157_iter00_core.json`,
   `scratchpad\root_cell_row_layer_paircap_rep0_3coreforbid_r157.json`,
   `scratchpad\root_cell_fixed_y_rowoutside_rep0_3coreforbid_r157.json`

METHOD:
`root_cell_core_learning_loop.py` runs a bounded foreground generate-kill-core cycle: generate a row-layer
pair-cap witness under learned core clauses, kill it with the R153 fixed-y row-outside oracle, then extract
a CP-SAT assumption core.  It stops on row-layer UNSAT/UNKNOWN, fixed-y SAT/UNKNOWN, core failure, or
iteration limit; timeouts are recorded as stop states, not evidence.

VALIDATION / RESULTS:
 - `python -m py_compile root_cell_core_learning_loop.py root_cell_fixed_y_core.py
   root_cell_fixed_y_residual_an.py root_cell_row_layer_cpsat.py` passed.
 - One-command smoke seeded with the two R156 cores completed one iteration:
   row-layer `OPTIMAL` in 6.6832s, fixed-y row_outside `INFEASIBLE` in 0.0250s, core extraction
   `INFEASIBLE` with a 659-literal core in 60.0223s.  Final learned core count: 3.
 - Learned core sizes are 75, 329, and 659 literals.
 - Feeding all three cores back into row representative 0 still yields a new pair-cap witness in 5.7779s;
   that witness is again killed by fixed-y row_outside in 0.0268s.

VERDICT:
The core-learning loop is now reproducible and proof-status aware, but blind accumulation of large cores
is not enough to prune row representative 0.  The useful next lever is smaller/better cores or integrated
branching, not a long watcher loop that piles up bulky clauses.

NEXT ACTION:
Improve core quality: deletion minimization, smaller residual submodels, MaxSAT/linear IIS extraction,
or branch heuristics that force the integrated R154 model toward row_outside contradictions directly.

---

## R156 -- fixed-y CP-SAT assumption cores become reusable row-layer nogoods [2026-06-30]
## OUTCOME: real algorithmic improvement; no row prune yet.

ARTIFACTS:
 - note: `ROOT_CELL_CORE_NOGOODS_R156.md`
 - new script: `root_cell_fixed_y_core.py`
 - updated script: `root_cell_row_layer_cpsat.py`
 - outputs:
   `scratchpad\root_cell_fixed_y_core_rep0_r156.json`,
   `scratchpad\root_cell_row_layer_paircap_rep0_coreforbid1_r156.json`,
   `scratchpad\root_cell_fixed_y_rowoutside_rep0_coreforbid1_r156.json`,
   `scratchpad\root_cell_fixed_y_core_rep0_coreforbid1_r156.json`,
   `scratchpad\root_cell_fixed_y_core_rep0_coreforbid1_w4_r156.json`,
   `scratchpad\root_cell_row_layer_paircap_rep0_2coreforbid_r156.json`,
   `scratchpad\root_cell_fixed_y_rowoutside_rep0_2coreforbid_r156.json`

METHOD:
`root_cell_fixed_y_core.py` rebuilds the R153 residual model with `z`, `y`, and outside-edge variables,
adds the killed witness's `z/y` truth values as CP-SAT assumptions, and records
`SufficientAssumptionsForInfeasibility()` as a reusable core nogood.  `root_cell_row_layer_cpsat.py`
now accepts `--forbid-core-json`; it adds a clause requiring at least one core truth value to differ.
A source guard prevents applying cores to a different representative file.

VALIDATION / RESULTS:
 - `python -m py_compile root_cell_fixed_y_core.py root_cell_row_layer_cpsat.py` passed.
 - Original R149 row-0 witness produced a 75-literal infeasibility core out of 887 assumptions
   (`z=True:1`, `y=True:21`, `y=False:53`) with 1 worker / 30s.
 - Feeding that core into the pair-cap generator still found a new row-0 witness, but the new witness
   violates the core clause (`50/75` literals match) and is killed by R153 fixed-y row-outside in 0.0295s.
 - A second core from that core-forbidden witness required 4 workers / 60s and had 329 literals
   (`z=True:2`, `z=False:12`, `y=True:51`, `y=False:264`).  The 1-worker / 30s extraction was UNKNOWN,
   so core extraction can be harder than fixed-constant infeasibility.
 - Feeding both cores into the pair-cap generator still found another row-0 witness, which violates both
   core clauses (`49/75` and `249/329` literals match) and is killed by R153 fixed-y row-outside in 0.0263s.

VERDICT:
Reusable core nogoods are implemented and soundly consumed by the row-layer generator.  They are stronger
than exact-assignment forbids but not yet sufficient to prune row representative 0.  This is a real
search-architecture improvement, not a mathematical decision.

NEXT ACTION:
Automate a bounded core-learning loop for row 0 and improve/minimize core extraction.  Useful acceptance
criteria: either integrated row-0 UNSAT/SAT under the R153 layer, or measured evidence that learned cores
substantially change pair-cap witness generation cost/diversity.  Do not report sampled core kills as
row-level pruning.

---

## R155 -- readiness verdict after R154 [2026-06-30]
## OUTCOME: honest go/no-go snapshot; no construction/nonexistence proof.

ARTIFACT:
 - `READINESS_R154.md`

VERDICT:
 - Problem status: unsolved; no graph constructed and no nonexistence proof.
 - Cloud r=3 thin-slice: one-command d11->d12 wrapper is runnable; `--help`, dry-run, py_compile,
   and `python s3_slice_harness.py --gate` passed.  The gate is ALL GREEN on rook(9) replay and exact
   T(7)=srg(21,10,5,4) r=3 reconstruction.
 - Rooted residual: R153/R154 provide a real fixed-y Boolean filter, killing 5/5 sampled row-0 pair-cap
   witnesses with independent MILP agreement, but integrated row-outside row-0 remains `UNKNOWN` at 60s.
   Therefore no row representative is pruned yet.

GO / NO-GO:
Go for exact r=3 cloud measurement if the objective is cost profiling/frontier certification using the
R95+ `s3_cloud_r3_d12.py` wrapper and strict aggregation.  No-go for claiming a mathematical decision:
current evidence does not solve Conway's 99-graph problem.

NEXT ACTION:
Continue rooted residual work: make the integrated R154 row-layer model decisive, or extract reusable
nogoods/cores from R153 fixed-y MILP infeasibilities.  The r=3 cloud wrapper remains ready for exact
measurement, but measurement alone is not proof.

---

## R154 -- row-outside lifted into row-layer; 5/5 lazy fixed-y witnesses killed [2026-06-30]
## OUTCOME: validated integrated formulation plus strong fixed-y filter sample; no row prune yet.

ARTIFACTS:
 - note: `ROOT_CELL_ROW_OUTSIDE_INTEGRATED_R154.md`
 - updated script: `root_cell_row_layer_cpsat.py`
 - outputs:
   `scratchpad\root_cell_row_layer_rowoutside_k4_r154.json`,
   `scratchpad\root_cell_row_layer_rowoutside_rep0_r154.json`,
   `scratchpad\root_cell_row_layer_paircap_rep0_alt1_r154.json`,
   `scratchpad\root_cell_row_layer_paircap_rep0_alt2_r154.json`,
   `scratchpad\root_cell_row_layer_paircap_rep0_alt3_r154.json`,
   `scratchpad\root_cell_row_layer_paircap_rep0_alt4_r154.json`,
   `scratchpad\root_cell_fixed_y_rowoutside_rep0_alt1_r154.json`,
   `scratchpad\root_cell_fixed_y_rowoutside_rep0_alt2_r154.json`,
   `scratchpad\root_cell_fixed_y_rowoutside_rep0_alt3_r154.json`,
   `scratchpad\root_cell_fixed_y_rowoutside_rep0_alt4_r154.json`,
   plus matching `*_milp30_r154.json` independent checks.

MODEL UPGRADE:
`root_cell_row_layer_cpsat.py` now has `--row-outside`, which chooses row matching, `y`, and outside
edges together and enforces outside `AN` plus exact row-outside pair equations (it implies
`--outside-an`).  It also has `--forbid-json`, which forbids exact previously found
`(matching_edges, outside_row_edges)` assignments for lazy generate-and-kill loops.

VALIDATION / RESULTS:
 - `python -m py_compile root_cell_row_layer_cpsat.py` passed.
 - rook integrated control with `--row-outside --outside-pair-cap`: `1/1` SAT.
 - srg99 row representative 0 with integrated `--row-outside --outside-pair-cap`: `UNKNOWN` at 60s
   (77935 conflicts, 339362 branches).  This is not feasibility/infeasibility evidence.
 - Lazy row-0 pair-cap loop generated five distinct `(matching,y)` witnesses, each with 5 matching
   edges and 122 outside-row edges; Hamming distances from the original R149 witness for candidates
   1-4 are `196, 28, 196, 200`.
 - All five fixed-y witnesses are killed by the R153 Boolean `AN + row_outside` oracle:
   CP-SAT infeasible in 0.014-0.028s and independent HiGHS MILP infeasible for every candidate.

VERDICT:
The integrated row-outside formulation is now runnable and rook-validated, but not yet decisive on row
0.  The lazy fixed-y refutation sample shows R153 is a strong filter on easy row-0 pair-cap witnesses.
Do not report row 0 pruned; report only that 5/5 sampled `y` witnesses are dead.

NEXT ACTION:
Turn the lazy generate-and-kill loop into a stronger incremental row-0 search: either add reusable
nogoods/cores from the MILP infeasibilities, improve integrated CP-SAT branching, or search for a
surviving `y` under the R153 Boolean layer.  A row representative is pruned only when the integrated
model proves UNSAT, not when sampled fixed-y witnesses die.

---

## R153 -- R149 representative-0 fixed-y witness killed by Boolean row-outside layer [2026-06-30]
## OUTCOME: exact fixed-y refutation; not yet a row-representative prune.

ARTIFACTS:
 - note: `ROOT_CELL_FIXED_Y_FULL_R153.md`
 - updated script: `root_cell_fixed_y_residual_an.py`
 - outputs:
   `scratchpad\root_cell_fixed_y_full_pair_k4_r153.json`,
   `scratchpad\root_cell_fixed_y_rowoutside_k4_milp_r153.json`,
   `scratchpad\root_cell_fixed_y_rowoutside_only_rep0_30s_r153.json`,
   `scratchpad\root_cell_fixed_y_rowoutside_only_rep0_milp30_r153.json`,
   `scratchpad\root_cell_fixed_y_full_pair_rep0_30s_r153.json`,
   `scratchpad\root_cell_fixed_y_full_pair_rep0_30s_w1_r153.json`,
   `scratchpad\root_cell_fixed_y_paironly_rep0_30s_r153.json`

MODEL UPGRADE:
`root_cell_fixed_y_residual_an.py` now supports `--row-outside`, adding the exact row-outside pair
equations as Boolean linear constraints after `y` and the R144 row matching are fixed.  It also supports
`--outside-pair-equations` for the exact outside-outside quadratic pair equations in CP-SAT, and handles
zero-variable MILP systems for rook controls.

VALIDATION / RESULTS:
 - `python -m py_compile root_cell_fixed_y_residual_an.py` passed.
 - rook fixed-y control with `--row-outside --outside-pair-equations` under CP-SAT: `OPTIMAL`.
 - rook fixed-y control with MILP `--row-outside`: SAT via the exact zero-variable residual system.
 - R149 representative-0 fixed-y witness with CP-SAT `--row-outside`: `INFEASIBLE` in 0.0149s,
   0 conflicts, 0 branches.
 - Same witness with independent HiGHS MILP `--row-outside`: infeasible (status 2) on 1917 constraints
   and 2485 Boolean edge variables.
 - Full CP-SAT with `--row-outside --outside-pair-equations`: reproducibly `INFEASIBLE` with 4 workers
   and 1 worker.  Pair-only quadratic CP-SAT without row-outside rows is `UNKNOWN` at 30s, so the accepted
   kill is the Boolean `AN + row_outside` layer, not a quadratic-pair timeout.

VERDICT:
The particular R149 `y` witness for row representative 0 is refuted exactly.  This is not a proof that
row representative 0 is impossible, because a different outside-to-row incidence `y` might survive.
It does prove that the next row-layer search should include outside-edge variables plus the R153
Boolean `AN + row_outside` constraints before attempting the full outside-outside pair equations.

NEXT ACTION:
Lift R153 into `root_cell_row_layer_cpsat.py`: add an option that chooses `y`, row matching, and
outside edges together while enforcing outside `AN` plus row-outside pair equations.  Test on rook,
representative 0, and then first/stratified R145 rows.  Only UNSAT from that integrated model safely
prunes a row representative.

---

## R152 -- fixed-y row-outside pair equations shrink residual linear space [2026-06-30]
## OUTCOME: real residual-space reduction; no modular inconsistency for the R149 fixed-y witness.

ARTIFACTS:
 - note: `ROOT_CELL_ROW_OUTSIDE_LINEAR_R152.md`
 - updated script: `root_cell_fixed_y_residual_rank.py`
 - outputs:
   `scratchpad\root_cell_fixed_y_residual_rank_k4_r152.json`,
   `scratchpad\root_cell_fixed_y_residual_rank_rep0_r152.json`

MODEL:
Once the R144 row matching and outside-to-row incidence `y` are fixed, each row-outside pair equation
is linear in the remaining outside-edge variables:
`sum_w y(w,r) x(o,w) = 2 - overlap(r,o) - y(o,r) - row_match_common(r,o)`.
This was added to the fixed-y modular rank audit as `row_outside`.

VALIDATION / RESULTS:
 - `python -m py_compile root_cell_fixed_y_residual_rank.py` passed.
 - rook control from `scratchpad\root_cell_row_layer_paircap_k4_r150.json` remains consistent modulo
   `2,3,5,7,1000003`.
 - R149 representative-0 fixed-y witness has no negative row-outside residuals.
 - On the srg99 witness, outside `AN` alone has odd/large-field rank 903 and dimension 1582.
   Adding 852 row-outside rows gives rank 1475 and dimension 1010 over mod `3,5,7,1000003`
   (mod 2 rank 1404, dimension 1081; with degree rows mod 2 rank 1450, dimension 1035).

VERDICT:
The row-outside linear layer is a genuine fixed-y residual-space reduction (572 extra odd-field rank)
and should be enforced before any residual brancher.  It is still consistent, so it does not refute the
R149 fixed-y witness and does not prune a row representative by itself.

NEXT ACTION:
Build the fixed-y residual brancher on the R152 linear closure and add the exact outside-outside pair
equations `x_ab + sum_w x_aw x_bw = tau(a,b)`.  Prioritize propagation from low `tau` pairs and edge
symmetry over generic MILP/CP-SAT timeouts.

---

## R151 -- saturated-pair neighbour-domain audit is exact but too local [2026-06-30]
## OUTCOME: steering result; one-vertex saturated-pair geometry does not kill the R149 fixed-y witness.

ARTIFACTS:
 - note: `ROOT_CELL_NEIGHBOR_DOMAINS_R151.md`
 - new script: `root_cell_fixed_y_neighbor_domains.py`
 - outputs:
   `scratchpad\root_cell_fixed_y_neighbor_domains_k4_r151.json`,
   `scratchpad\root_cell_fixed_y_neighbor_domains_rep0_r151.json`

MODEL:
For fixed outside-to-row `y`, every outside pair has residual target
`tau(a,b) = 2 - overlap(a,b) - row_common_y(a,b) = x_ab + outside_common(a,b)`.
If `tau(a,b)=0`, then `x_ab=0` and no outside vertex may be adjacent to both `a`
and `b`.  Therefore each outside vertex's outside-neighbour set must satisfy its residual
degree/local-column `AN` row and be independent in the graph of `tau=0` pairs.

VALIDATION / RESULTS:
 - `python -m py_compile root_cell_fixed_y_neighbor_domains.py root_cell_fixed_y_residual_an.py`
   passed.
 - rook control from the R150 fixed-y row-layer output: `1/1` SAT.
 - R149 srg99 representative-0 fixed-y witness: `71/71` outside vertex domains SAT, `0` UNSAT,
   `0` UNKNOWN; every solve finished in under 0.006s.
 - Pair target profile on the R149 witness: `tau=0:82`, `tau=1:1046`, `tau=2:1357`.
   All saturated pairs are overlap-1:
   `overlap=0,target=1:478`, `overlap=0,target=2:1357`,
   `overlap=1,target=0:82`, `overlap=1,target=1:568`.
 - Each outside vertex still has 66-70 admissible candidates for residual degree 10 or 11.

VERDICT:
The saturated-pair domain predicate is sound and witness-validated, but too local to prune the measured
fixed-y sample.  The fixed-y residual obstruction, if present, requires global coupling of many outside
neighbourhoods: edge symmetry plus exact pair common-neighbour totals, not just per-vertex AN rows and
`tau=0` local independence.

NEXT ACTION:
Build a full fixed-y residual SAT/CP-SAT layer with exact outside pair equations
`x_ab + sum_w x_aw x_bw = tau(a,b)` and row-outside pair equations, or derive a smaller propagation
from those equations.  The one-vertex saturated-pair domain screen is closed for this witness.

---

## R150 -- fixed-y residual modular rank is consistent; obstruction must be nonlinear [2026-06-30]
## OUTCOME: steering result; closes the cheapest fixed-y residual linear obstruction on the measured witness.

ARTIFACTS:
 - note: `ROOT_CELL_FIXED_Y_RANK_R150.md`
 - new script: `root_cell_fixed_y_residual_rank.py`
 - repaired script: `root_cell_fixed_y_residual_an.py`
 - outputs:
   `scratchpad\root_cell_row_layer_paircap_k4_r150.json`,
   `scratchpad\root_cell_fixed_y_residual_rank_k4_r150.json`,
   `scratchpad\root_cell_fixed_y_residual_an_k4_r150.json`,
   `scratchpad\root_cell_fixed_y_residual_rank_rep0_r150.json`

FIXED-Y SCHEMA REPAIR:
`root_cell_fixed_y_residual_an.py` now infers `k` from the source representative file when the
row-layer JSON omits it, and refuses old row-layer outputs that do not record `outside_row_edges`.
This prevents an old or malformed SAT witness from being silently interpreted as empty `y`.

MEASURED RESULT:
 - `python -m py_compile root_cell_fixed_y_residual_an.py root_cell_fixed_y_residual_rank.py
   root_cell_row_layer_cpsat.py root_cell_linear_rank.py` passed.
 - fresh rook control with `--outside-pair-cap`: `1/1` SAT, residual rank consistent modulo
   `2,3,5,7,1000003`, and fixed-y residual AN CP-SAT returned `OPTIMAL` in 0.0123s.
 - srg99 representative 0 using the R149 pair-cap `y` witness has no negative residual demands.
   The full fixed-y `degree+AN` system on 71 outside vertices / 2485 outside-edge variables is
   consistent modulo every tested prime:
   mod 2 rank=aug=889, dimension 1596; mod 3/5/7/1000003 rank=aug=903, dimension 1582.

VERDICT:
The modular-rank obstruction is exhausted for this fixed-y witness.  The residual outside graph is
not hard because the linear residual `AN` equations are inconsistent; it is hard because of Booleanity
and the quadratic common-neighbour/pair-cap structure.  This does not prove representative 0 is
completable and does not prune any R145 row representative.

R43 STRUCTURAL SWITCH CONSOLIDATION:
The cloud route remains the R43 r=3 / 45-vertex star-complement route as primary, with the older s=-4
route kept only as fallback/cross-check.  `CLOUD_SPEC_SC.md` has the one-command R95+ d11->d12 wrapper
and the R141-R150 rooted-cell updates; do not regress to s=-4-first planning unless a concrete new lever
changes the cost model.

NEXT ACTION:
Build a specialized fixed-y residual outside solver/obstruction using nonlinear structure: saturated
pair-cap forced edge/nonedge classes, a label-geometry b-factor formulation, or a tailored SAT brancher
that enforces exact outside pair common-neighbour equations.  Generic CP-SAT/MILP timeouts and modular
rank consistency are now closed as evidence sources for this fixed-y witness.

---

## R149 -- outside-pair cap is exact but permissive; fixed-y residual AN remains hard [2026-06-30]
## OUTCOME: steering result; localizes the hard part to the residual outside graph factor.

ARTIFACTS:
 - note: `ROOT_CELL_OUTSIDE_PAIRCAP_R149.md`
 - updated scripts: `root_cell_row_layer_cpsat.py`, `root_cell_fixed_y_residual_an.py`
 - outputs:
   `scratchpad\root_cell_row_layer_paircap_k4_r149_probe.json`,
   `scratchpad\root_cell_row_layer_paircap_first5_r149_probe.json`,
   `scratchpad\root_cell_row_layer_paircap_strat32_r149.json`,
   `scratchpad\root_cell_row_layer_paircap_balance_strat16_r149.json`,
   `scratchpad\root_cell_row_layer_paircap_rep0_r149.json`,
   `scratchpad\root_cell_fixed_y_residual_an_rep0_r149.json`,
   `scratchpad\root_cell_fixed_y_residual_an_rep0_milp30_r149.json`

OUTSIDE-PAIR CAP:
For outside vertices `a,b`, the known row-common count must satisfy
`sum_{r in R} y[a,r]y[b,r] <= 2 - overlap(a,b)`, because
`row_common + outside_common + x_ab + overlap(a,b) = 2`.  This exact necessary
condition was added as `--outside-pair-cap`.

MEASURED RESULT:
 - `python -m py_compile root_cell_row_layer_cpsat.py` passed.
 - rook control with `--outside-pair-cap`: `1/1` SAT.
 - first five srg99 row reps with `--outside-pair-cap`: `5/5` SAT.
 - 32 stratified srg99 row reps with `--outside-pair-cap`: `32/32` SAT.
 - 16 stratified srg99 row reps with `--outside-pair-cap --outside-balance`: `16/16` SAT.
Thus the outside-pair cap is useful propagation but not a standalone row filter on measured samples.

FIXED-Y RESIDUAL AN:
`root_cell_fixed_y_residual_an.py` fixes a SAT outside-to-row incidence `y` and asks whether an
outside-outside graph can satisfy exact residual `AN`.

MEASURED RESULT:
 - generated representative-0 pair-cap witness:
   `python root_cell_row_layer_cpsat.py ... --outside-pair-cap --indices 0 ...`
 - fixed-y residual AN with CP-SAT, 120s: `UNKNOWN`.
 - fixed-y residual AN with SciPy/HiGHS MILP, 30s: time-limited status.
These timeouts are not mathematical evidence; they show the residual outside graph factor is the hard
subproblem even after `y` is fixed.

VERDICT:
Accepted as a steering result.  The next real lever is not another row-level cap.  The problem has been
localized to the residual outside graph factor with exact label-demand equations.

NEXT ACTION:
Develop a specialized residual-factor solver or obstruction: parity/modular rank on fixed-y residual
systems, label-geometry b-matching, forced edge/nonedge classes from saturated pair caps, or a tailored
SAT branching scheme.  Generic CP-SAT/MILP timeouts must not be reported as evidence.

---

## R148 -- outside residual AN: aggregate balance too weak; direct CP-SAT too hard [2026-06-30]
## OUTCOME: steering result; no construction/nonexistence proof and no pruning predicate accepted.

ARTIFACTS:
 - note: `ROOT_CELL_OUTSIDE_AN_R148.md`
 - updated script: `root_cell_row_layer_cpsat.py`
 - outputs:
   `scratchpad\root_cell_row_layer_balance_k4_r148.json`,
   `scratchpad\root_cell_row_layer_balance_strat128_r148.json`,
   `scratchpad\root_cell_row_layer_outside_an_k4_r148_probe.json`,
   `scratchpad\root_cell_row_layer_outside_an_first5_r148_probe.json`,
   `scratchpad\root_cell_row_layer_outside_an_rep0_r148_probe.json`,
   `scratchpad\root_cell_row_layer_outside_an_rep0_fixedsearch_r148_probe.json`

AGGREGATE BALANCE TEST:
Added `--outside-balance`, the cheap local-column balance implied by outside residual `AN`:
`sum_o residual_demand(o,l) = sum_{o: l in label(o)} residual_degree(o)`.
This is linear in the outside-to-row variables.

RESULT:
 - `python -m py_compile root_cell_row_layer_cpsat.py` passed.
 - rook control with `--outside-balance`: `1/1` SAT.
 - 128 stratified srg99 row representatives with `--outside-balance`: `128/128` SAT.
Therefore this aggregate balance does not prune the measured sample.

DIRECT OUTSIDE-AN TEST:
Added `--outside-an`, with outside-outside edge variables and exact residual `AN` equations for every
outside vertex/local column.

RESULT:
 - rook control with `--outside-an`: `1/1` SAT.
 - first five srg99 row representatives at 20s each: all `UNKNOWN`.
 - representative 0 at 120s: `UNKNOWN`.
 - representative 0 after adding an explicit decision strategy, again 120s: `UNKNOWN`.
These UNKNOWN runs are not mathematical evidence; they show the naive direct CP-SAT layer is not a
usable quick oracle.

VERDICT:
Accepted as a measured steering result.  The aggregate outside residual balance is too weak, and the
direct residual-AN CP-SAT encoding is too hard in its current form.  Do not spend another cycle on
solver knob-twiddling here unless the formulation changes.

NEXT ACTION:
Reformulate the outside-outside layer structurally: residual degree/label b-matching, a SAT encoding
with better symmetry and row hints, or a smaller derived obstruction from residual demand matrices.
The next accepted layer should either prune a verified set of row seeds or be retired with a proof-grade
reason.

---

## R147 -- row-layer outside-incidence probe is permissive on controls and samples [2026-06-30]
## OUTCOME: negative steering result; outside-to-row equations alone are not a pruning predicate.

ARTIFACTS:
 - note: `ROOT_CELL_ROW_LAYER_R147.md`
 - script: `root_cell_row_layer_cpsat.py`
 - outputs:
   `scratchpad\root_cell_row_layer_k4_r147.json`,
   `scratchpad\root_cell_row_layer_first5_r147.json`,
   `scratchpad\root_cell_row_layer_first100_r147.json`,
   `scratchpad\root_cell_row_layer_rep53_r147.json`,
   `scratchpad\root_cell_row_layer_strat128_r147.json`

MODEL:
For a fixed R145 row representative, choose the R144 internal matching and outside-to-row variables
`y[o,r]`.  Enforce:
 - outside cross-degree `sum_r y[o,r] = 2 - overlap(o,(0,2))`;
 - row far-degree after accounting for `u` and the row matching;
 - row-pair common-neighbour equations after accounting for common neighbour `u`;
 - exact row-vertex `AN` equations for every local column;
 - outside row-contribution upper bounds from each outside vertex's `AN` demand.

UNSAT safely prunes a row representative; SAT is only a partial witness.

VALIDATION / RESULTS:
 - `python -m py_compile root_cell_row_layer_cpsat.py` passed.
 - rook control from `scratchpad\root_cell_row_reps_k4_r145_recheck.json`: `1/1` SAT.
 - first 5 srg99 row representatives: `5/5` SAT.
 - first 100 srg99 row representatives at 5s cap: `99` SAT, `1` UNKNOWN; rerunning the one timeout
   representative 53 at 60s returned SAT.
 - 128 stratified representatives across all 8105 R145 rows at 10s cap: `128/128` SAT.

VERDICT:
Accepted as a measured dead end.  The outside-to-row incidence equations are good propagation to embed
inside a row-seeded solver, but they do not appear to prune row representatives by themselves.  Do not
spend another cycle on this layer alone.

NEXT ACTION:
Extend the row-seeded model to include outside residual `AN` demands and outside-outside edge/common-
neighbour constraints, or derive an aggregate obstruction from those residual demands.  The next layer
must interact with outside-outside structure; row+matching+outside-to-row incidence alone is too loose.

---

## R146 -- row-matching orbit quotient gives only a 9% reduction [2026-06-30]
## OUTCOME: exact steering result; do not chase matching quotient as the next primary lever.

ARTIFACTS:
 - note: `ROOT_CELL_ROW_MATCHING_ORBITS_R146.md`
 - script: `root_cell_row_matching_orbits.py`
 - output: `scratchpad\root_cell_row_matching_orbits_r146.json`

METHOD:
For each of the 8105 R145 first-row representatives, compute its residual stabilizer inside the
fixed-label stabilizer of `(0,2)`, enumerate all R144-compatible perfect matchings on the ten
overlap-0 row labels, and quotient those matchings by the residual stabilizer.

VALIDATION / RESULT:
 - `python -m py_compile root_cell_row_matching_orbits.py` passed.
 - `python root_cell_row_matching_orbits.py scratchpad\root_cell_row_reps_k14_r145.json
   --json-out scratchpad\root_cell_row_matching_orbits_r146.json` completed.
 - rows: 8105.
 - raw R144 row+matching choices: `2,944,568`.
 - row+matching orbits after residual quotient: `2,677,638`.
 - rows with any quotient gain: 1360.
 - row stabilizer histogram:
   `1:6722, 2:1019, 4:182, 8:94, 12:6, 16:40, 20:1, 24:18, 32:14, 40:3, 64:1, 192:2, 256:3`.

VERDICT:
Accepted.  Since most row representatives have trivial residual stabilizer, matching quotienting gives
only about a 9% reduction.  This is not the next decisive lever.

NEXT ACTION:
Use the outside cross-degree/common-neighbour equations from R144, or build row-seeded SAT/CP-SAT
slices from the R145 representatives.  Do not spend the next cycle on a more elaborate row-matching
quotient unless it is coupled to outside constraints.

---

## R145 -- first-row representative list generated and verified [2026-06-30]
## OUTCOME: R143's 8,105 orbit count is now a concrete branch artifact for rooted SAT/SMS.

ARTIFACTS:
 - note: `ROOT_CELL_ROW_REPS_R145.md`
 - enumerator: `root_cell_row_reps_cpsat.py`
 - verifier: `root_cell_row_reps_verify.py`
 - complete representative list: `scratchpad\root_cell_row_reps_k14_r145.json` (~8.4 MB)
 - verification summary: `scratchpad\root_cell_row_reps_verify_k14_r145.json`

METHOD:
`root_cell_row_reps_cpsat.py` solves the one-row `AN` equations for fixed far label `(0,2)` and adds
lex-leader constraints against every element of the fixed-label stabilizer in `S_2 wr S_7`.  Stabilizer
size is `7680`; the model has `599040` nontrivial lex prefix terms.  This turns the Burnside count from
R143 into an actual representative list.

COMMANDS / RESULTS:
 - `python -m py_compile root_cell_row_reps_cpsat.py root_cell_row_reps_verify.py` passed.
 - `python root_cell_row_reps_cpsat.py --k 4 --time-cap 30 --expected-count 1 --max-solutions 1
   --json-out scratchpad\root_cell_row_reps_k4_r145_recheck.json` returned the expected single rook
   representative.
 - `python root_cell_row_reps_cpsat.py --k 14 --time-cap 1500 --expected-count 8105
   --max-solutions 8105 --json-out scratchpad\root_cell_row_reps_k14_r145.json`
   returned `STATUS OPTIMAL`, `solutions=8105`, build `12.909s`, wall `737.155s`, conflicts `6147`,
   branches `165656`.
 - `python root_cell_row_reps_verify.py scratchpad\root_cell_row_reps_k14_r145.json
   --expected-count 8105 --json-out scratchpad\root_cell_row_reps_verify_k14_r145.json` passed:
   8105 distinct representatives, all satisfy the `AN` row target and R144 row split.

R144 MATCHING CHECK:
Every one of the 8105 row representatives admits at least one R144-compatible perfect matching on the
ten overlap-0 row labels; therefore the immediate matching-existence condition is not a row filter.
The total row+matching branch count across representatives is `2,944,568`.  Matching-count histogram:
`292:11, 293:29, 294:10, 295:7, 324:66, 325:18, 328:125, 329:655, 330:196, 359:65, 360:17,
361:26, 364:210, 365:1240, 366:460, 368:80, 370:1459, 371:2398, 372:1033`.

VERDICT:
Accepted.  The first rooted row branch is no longer just a count; it is a reproducible concrete
representative list.  This is a genuine cost-reducing search transformation, but it does not decide
existence/nonexistence.  R144 matching existence alone does not prune rows, so the next constraint must
use the row matchings together with outside cross-degree/common-neighbour equations.

NEXT ACTION:
Build the next rooted layer: either quotient the 2,944,568 row+matching choices under row stabilizers,
or add row representative + R144 matching + outside cross-degree constraints to a row-seeded SAT/CP-SAT
slice.  Use rook(9) as the positive control and require full SRG reconstruction for any SAT result.

---

## R144 -- rooted far-neighbourhood matching lemma validated on real witnesses [2026-06-30]
## OUTCOME: new quadratic-local propagation rule for the R141 rooted formulation; no graph/proof yet.

LEMMA:
Fix a far vertex `u` in the rooted far graph, and let `R=N_F(u)`.  Then:
 - `|R| = k-2`.
 - exactly two vertices of `R` have label-overlap 1 with `u`;
 - those two overlap-1 vertices are isolated inside `A[R]`;
 - the other `k-4` vertices of `R`, with overlap 0 against `u`, form a perfect matching inside
   `A[R]`;
 - every far non-neighbour `w` of `u` has cross-degree `|N_F(w) cap R| = 2 - overlap(u,w)`.

For srg99 (`k=14`), every 12-vertex far-neighbourhood is therefore `5K2 + 2` isolated vertices.
The outside split is forced: 20 outside overlap-1 labels each have cross-degree 1 into `R`, and
51 outside overlap-0 labels each have cross-degree 2 into `R`.

PROOF:
The `AN` row gives far degree `k-2` and exactly two overlap-1 neighbours.  For a far neighbour `v`,
the quadratic pair equation gives `common_F(u,v) + 1 + overlap(u,v) = 2`, so overlap-1 neighbours
have internal row degree 0 and overlap-0 neighbours have internal row degree 1.  For a far non-neighbour
`w`, the same equation gives `common_F(u,w) = 2 - overlap(u,w)`.

ARTIFACTS:
 - note: `ROOT_CELL_NEIGHBORHOOD_R144.md`
 - verifier: `root_cell_neighborhood_lemma.py`
 - output: `scratchpad\root_cell_neighborhood_lemma_r144.json`

VALIDATION:
 - `python -m py_compile root_cell_neighborhood_lemma.py` passed.
 - `python root_cell_neighborhood_lemma.py --json-out scratchpad\root_cell_neighborhood_lemma_r144.json`
   validated the lemma on all 36 rooted far-neighbourhoods of rook(9) and 660 far-neighbourhoods from
   sampled BvLS243 roots `0,1,2`.

VERDICT:
Accepted.  This is the first concrete quadratic-local rule to attach to the R143 row-orbit branch.
After selecting one of the 8,105 first-row orbits, the induced graph on the row is forced to be
`5K2+2I` in the srg99 case, and outside cross-degrees into the row are fixed.  A rooted SAT/SMS
encoding should add these constraints before any large solve.

NEXT ACTION:
Generate first-row orbit representatives and extend the rooted SAT/SMS model with the R144 row matching
and outside cross-degree constraints.  R144 should be used as an early propagation layer, not as a
standalone nonexistence claim.

---

## R143 -- rooted first-row AN patterns collapse to 8,105 stabilizer orbits [2026-06-30]
## OUTCOME: real symmetry cost reduction for the R141 rooted SAT/SMS direction; no graph/proof yet.

SETUP:
Fix the far label `(0,2)` in the rooted 84-label model.  Its far-neighbour row must satisfy the
one-row `AN` local-degree target
`[1,1,1,1,2,2,2,2,2,2,2,2,2,2]`.  The raw dynamic-programming count for this row is the previously
measured `56,011,010` legal 12-neighbour sets.

METHOD:
Applied Burnside's lemma over the stabilizer of `(0,2)` inside the root-local matching group
`S_2 wr S_7`.  The stabilizer has size `2 * 2^5 * 5! = 7680`.  For each stabilizer element,
`root_cell_row_orbits.py` decomposes the induced permutation of the other 83 labels into cycles and
counts invariant legal row sets by exact DP over cycle unions and the local-degree target.

RESULTS:
 - rook control `k=4`: stabilizer size 2, raw legal rows 1, orbit count 1.
 - srg99 rooted row `k=14`: candidate labels 83, stabilizer size 7680,
   raw legal rows `56,011,010`, Burnside sum `62,246,400`, orbit count `8,105`,
   max DP states `471,839`.

ARTIFACTS:
 - note: `ROOT_CELL_ROW_ORBITS_R143.md`
 - script: `root_cell_row_orbits.py`
 - outputs: `scratchpad\root_cell_row_orbits_k4_r143.json`,
   `scratchpad\root_cell_row_orbits_k14_r143.json`

VALIDATION:
 - `python -m py_compile root_cell_row_orbits.py` passed.
 - `python root_cell_row_orbits.py --k 4 --json-out scratchpad\root_cell_row_orbits_k4_r143.json`
   returned the expected single rook row orbit.
 - `python root_cell_row_orbits.py --k 14 --json-out scratchpad\root_cell_row_orbits_k14_r143.json`
   returned identity fixed count `56,011,010`, matching the prior raw DP count, and exact orbit count
   `8,105`.
 - Checked that native `geng`, `labelg`, and `dreadnaut` are not installed in this environment, so no
   nauty-backed representative generator was claimed.

VERDICT:
Accepted.  A row-first rooted branch is much more plausible than the raw 56M count suggested: the
first row has only 8,105 symmetry orbits under the fixed-label stabilizer.  This reduces the decisive
rooted search cost if we can generate one representative per orbit and attach the quadratic
common-neighbour equations.

NEXT ACTION:
Build a sound representative generator or SAT row enumerator for these 8,105 first-row orbits, then
feed each representative into the rooted quadratic SAT/SMS model.  Do not claim completeness from the
orbit count alone; the representative list itself is still missing.

---

## R142 -- rooted linear layer audited; centralizer rank cut is redundant after AN [2026-06-30]
## OUTCOME: structural correction + runnable rank audit. No construction and no nonexistence proof.

PROOF / CORRECTION:
In the R141 rooted model, `N N^T = S + 2I`.  If `A N = R = 2J - N(I+M)` and `A`
is symmetric, then

`A S = A(NN^T - 2I) = R N^T - 2A = 4J - N(I+M)N^T - 2A`.

The right side is symmetric, so `AS` is symmetric; since `A` and `S` are symmetric,
`AS = (AS)^T = SA`.  Thus the centralizer equation `AS=SA` is already implied by
the rooted `AN` equations plus symmetry.  Likewise, summing `AN` over local columns
gives the far degree `k-2`, so degree rows are also redundant.  `AS=SA` may still
help CP-SAT propagation, but it should not be treated as an independent linear
pruning/rank-reduction lever.

ARTIFACTS:
 - proof/measurement note: `ROOT_CELL_LINEAR_R142.md`
 - readiness verdict: `READINESS_R142.md`
 - modular rank audit: `root_cell_linear_rank.py`
 - measured JSON outputs:
   `scratchpad\root_cell_linear_rank_k4_r142.json`,
   `scratchpad\root_cell_linear_rank_k14_final_mod2_dense_r142.json`,
   `scratchpad\root_cell_linear_rank_k14_final_mod3_dense_r142.json`,
   `scratchpad\root_cell_linear_rank_k14_final_mod5_dense_r142.json`,
   `scratchpad\root_cell_linear_rank_k14_final_mod7_dense_r142.json`,
   `scratchpad\root_cell_linear_rank_k14_final_mod1000003_dense_r142.json`,
   `scratchpad\root_cell_linear_rank_k14_all_mod1000003_dense_r142.json`

VALIDATION:
 - `python -m py_compile root_cell_scheme.py root_cell_cpsat.py root_cell_linear_rank.py
   s3_slice_harness.py s3_cloud_r3_d12.py s3_aggregate_shards.py s3_run_shards.py
   s3_merge_frontiers.py` passed.
 - `python root_cell_scheme.py` revalidated the rooted identities on all rook(9) roots and sampled
   BvLS243 roots `0,1,2`.
 - `python root_cell_cpsat.py --k 4 --time-cap 10 --workers 4 --out scratchpad\root_cell_cpsat_rook9_r142.json`
   returned OPTIMAL and rebuilt a verified rook(9).
 - `python s3_slice_harness.py --gate` stayed ALL GREEN: rook(9) local replay, triangle identity,
   and T(7) r=3 CRS/clique reconstruction all passed.
 - `python root_cell_linear_rank.py --k 4 ...` gives a consistent control with `AN` rank 6 on 6
   far-edge variables.
 - For `k=14`, there are 84 far vertices and 3486 edge variables.  The combined linear system is
   consistent modulo `2,3,5,7,1000003`.  Ranks:
   mod 2 rank `1071`, dimension `2415`; mod `3,5,7,1000003` rank `1085`, dimension `2401`.
 - Large-prime breakdown at `p=1000003`: `degree` rank 84, `AN` rank 1085,
   `degree+AN` rank 1085, `commute` rank 1035, `degree+AN+commute` rank 1085.
   This confirms that degree and centralizer rows add no rank beyond `AN`.

CLOUD CHECK:
 - The exact `N12` wrapper remains one-command runnable.  Dry run:
   `python s3_cloud_r3_d12.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --indices 72-73
   --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad
   --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --tag r3_d11_to_d12_shard512_exact_r142_dryrun
   --aggregate-out scratchpad\r3_d11_to_d12_shard512_072_073_exact_aggregate_r142.json --dry-run`
   emitted the `s3_slice_harness.py --gate` command followed by the compatible `s3_run_shards.py`
   shard command with `--allow-incomplete`.

VERDICT:
Accepted as a real correction.  The R141 rooted formulation remains exact and high-leverage, but
the cheap linear layer is too loose: over odd/large-prime linearizations it leaves 2401 affine
degrees of freedom.  Do not spend the next cycle on centralizer rank/block linear algebra unless a
new non-linear constraint is attached.  The next rooted-model lever must attack the quadratic
common-neighbour equations, use a purpose-built SAT/SMS encoding with `S_2 wr S_7` symmetry, or import
additional validated structural constraints.

NEXT ACTION:
Build a rooted SAT/SMS or exact combinatorial branch on the quadratic equations themselves, with
rook(9) as a positive control and full reconstruction verification for any SAT result.  If choosing
compute instead of new math, use `s3_cloud_r3_d12.py` for exact `N12`; do not run more shallow
diagnostics without a new predicate to measure.

---

## R141 -- rooted 84-type second-neighbourhood formulation built and bounded-tested [2026-06-30]
## OUTCOME: genuine formulation change.  Fixing one vertex converts the problem to a labelled
84-vertex second-neighbourhood matrix equation, not another anonymous shallow frontier extension.

PROOF / FORMULATION:
For any `srg(v,k,1,2)`, root at a vertex `oo`.  `N(oo)` is a matching, and every far vertex in
`Gamma_2(oo)` is adjacent to exactly one nonmatched pair of local neighbours.  Thus for srg99 the
84 far vertices are canonically labelled by the cross-pairs of the 7 local matching edges.  If `A`
is the far graph, `N` the fixed far-label/local-incidence matrix, `M` the local matching matrix, and
`S` the fixed label-overlap graph, then every srg99 satisfies:

`A N = 2J - N(I+M)` and `A^2 + A + S = 10I + 2J`.

Conversely, any symmetric 0/1 diagonal-zero `A` satisfying these equations reconstructs a full
`srg(99,14,1,2)`.  The quadratic identity implies the linear centralizer cut `AS=SA`.

ARTIFACTS:
 - proof/experiment note: `ROOT_CELL_SCHEME_R141.md`
 - identity validator: `root_cell_scheme.py`
 - bounded CP-SAT probe: `root_cell_cpsat.py`
 - rook controls:
   `scratchpad\root_cell_cpsat_rook9_r141.json`,
   `scratchpad\root_cell_cpsat_rook9_commute_r141.json`

VALIDATION:
 - `python root_cell_scheme.py` validates the label bijection, `AN`, `A^2+A+S`, and `AS=SA` on
   all roots of rook(9) and sampled roots `0,1,2` of BvLS(243).
 - `python root_cell_cpsat.py --k 4 ...` reconstructs and verifies a real `srg(9,4,1,2)`.
 - strengthened CP-SAT with explicit `AS=SA` also reconstructs rook(9).

BOUNDED SRG99 PROBE:
 - `python root_cell_cpsat.py --k 14 --time-cap 60 --workers 8 --out scratchpad\root_cell_cpsat_srg99_r141.json`
   returned `UNKNOWN` after 60s (8214 branches).
 - `python root_cell_cpsat.py --k 14 --time-cap 60 --workers 8 --out scratchpad\root_cell_cpsat_srg99_commute_r141.json`
   returned `UNKNOWN` after 60s (18734 conflicts, 239677 branches).
 - No construction and no nonexistence proof.

NEGATIVE / NO-SHORTCUT:
Dynamic-programming count of legal neighbour rows under the linear `AN` equations alone gives
56,011,010 legal 12-neighbour patterns for one far label at `k=14`; naive row-pattern enumeration is
not the shortcut.

VERDICT:
Accepted as the current high-leverage direction.  The rooted model is exact and construction/UNSAT
decisive in principle, but the first raw CP-SAT encoding is not decisive.  Next action is not more
plain `N12`; it is to strengthen the rooted model: SAT/SMS encoding with the `S_2 wr S_7` symmetry,
centralizer/block cuts from `AS=SA`, or combine the rooted labels with Taylor edge-template demand
constraints.

NEXT ACTION:
Develop a purpose-built rooted SAT/SMS or symmetry-broken centralizer experiment, with rook(9) as a
positive control and any UNSAT/SAT claim verified by full SRG reconstruction.

---

## R140 -- exact-contributing d11->d12 shards 70..71/512 completed; known N12 coverage now 75/512 [2026-06-30]
## OUTCOME: two more proof-grade shard stats/frontiers were added via the cloud wrapper path.

COMMAND:
`python s3_cloud_r3_d12.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --indices 70-71 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --tag r3_d11_to_d12_shard512_exact_r140 --aggregate-out scratchpad\r3_d11_to_d12_shard512_070_071_exact_aggregate_r140.json --skip-gate`

RESULTS:
 - shard 70/512: 906 depth-11 parents -> 13253 depth-12 children, branching 14.628, wall 164.43s.
 - shard 71/512: 906 depth-11 parents -> 13621 depth-12 children, branching 15.034, wall 213.75s.
 - both frontier files were physically recounted and match their JSON stats/header counts exactly:
   13253 and 13621 rows.
 - batch aggregate `scratchpad\r3_d11_to_d12_shard512_070_071_exact_aggregate_r140.json`:
   1812 depth-11 parents -> 26874 depth-12 children, diagnostic scaled `N12 ~ 6876244`.
 - combined known-shard aggregate:
   `scratchpad\r3_d11_to_d12_shard512_known75_aggregate_r140.json`
   covers shards `0..71,128,256,384`, i.e. 67949/463636 depth-11 parents = 14.6557%,
   with 995306 measured depth-12 children.
 - combined known-shard diagnostic scaled estimate: `N12 ~ 6791265`.
 - no budget/time/sample flags; prune counters remain zero.
 - branch range over the known 75 shards remains 12.476..17.564, with the maximum at shard 64.

VERDICT:
Accepted. These two shards are exact for their owned source-parent slices and can be included in the
final exact 512-shard aggregate/merge. The aggregate remains diagnostic until all 512 shard indexes
are covered without `--allow-incomplete`.

NEXT ACTION:
Rerun the local proof gates after this documentation update, refresh graphify, then either continue
exact `N12` coverage with the next unmeasured contiguous pair `72..73` or pause for a genuinely new
algebraic lever. The shallow d11->d12 band remains non-pruning.

---

## R139 -- exact-contributing d11->d12 shards 68..69/512 completed; known N12 coverage now 73/512 [2026-06-30]
## OUTCOME: two more proof-grade shard stats/frontiers were added via the cloud wrapper path.

COMMAND:
`python s3_cloud_r3_d12.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --indices 68-69 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --tag r3_d11_to_d12_shard512_exact_r139 --aggregate-out scratchpad\r3_d11_to_d12_shard512_068_069_exact_aggregate_r139.json --skip-gate`

RESULTS:
 - shard 68/512: 906 depth-11 parents -> 13890 depth-12 children, branching 15.331, wall 189.12s.
 - shard 69/512: 906 depth-11 parents -> 13574 depth-12 children, branching 14.982, wall 186.65s.
 - both frontier files were physically recounted and match their JSON stats/header counts exactly:
   13890 and 13574 rows.
 - batch aggregate `scratchpad\r3_d11_to_d12_shard512_068_069_exact_aggregate_r139.json`:
   1812 depth-11 parents -> 27464 depth-12 children, diagnostic scaled `N12 ~ 7027207`.
 - combined known-shard aggregate:
   `scratchpad\r3_d11_to_d12_shard512_known73_aggregate_r139.json`
   covers shards `0..69,128,256,384`, i.e. 66137/463636 depth-11 parents = 14.2649%,
   with 968432 measured depth-12 children.
 - combined known-shard diagnostic scaled estimate: `N12 ~ 6788937`.
 - no budget/time/sample flags; prune counters remain zero.
 - branch range over the known 73 shards remains 12.476..17.564, with the maximum at shard 64.

VERDICT:
Accepted. These two shards are exact for their owned source-parent slices and can be included in the
final exact 512-shard aggregate/merge. The aggregate remains diagnostic until all 512 shard indexes
are covered without `--allow-incomplete`.

NEXT ACTION:
Rerun the local proof gates after this documentation update, refresh graphify, then either continue
exact `N12` coverage with the next unmeasured contiguous pair `70..71` or pause for a genuinely new
algebraic lever. The shallow d11->d12 band remains non-pruning.

---

## R138 -- exact-contributing d11->d12 shards 66..67/512 completed; known N12 coverage now 71/512 [2026-06-30]
## OUTCOME: two more proof-grade shard stats/frontiers were added via the cloud wrapper path.

COMMAND:
`python s3_cloud_r3_d12.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --indices 66-67 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --tag r3_d11_to_d12_shard512_exact_r138 --aggregate-out scratchpad\r3_d11_to_d12_shard512_066_067_exact_aggregate_r138.json --skip-gate`

RESULTS:
 - shard 66/512: 906 depth-11 parents -> 12716 depth-12 children, branching 14.035, wall 136.30s.
 - shard 67/512: 906 depth-11 parents -> 13557 depth-12 children, branching 14.964, wall 133.98s.
 - both frontier files were physically recounted and match their JSON stats/header counts exactly:
   12716 and 13557 rows.
 - batch aggregate `scratchpad\r3_d11_to_d12_shard512_066_067_exact_aggregate_r138.json`:
   1812 depth-11 parents -> 26273 depth-12 children, diagnostic scaled `N12 ~ 6722466`.
 - combined known-shard aggregate:
   `scratchpad\r3_d11_to_d12_shard512_known71_aggregate_r138.json`
   covers shards `0..67,128,256,384`, i.e. 64325/463636 depth-11 parents = 13.8740%,
   with 940968 measured depth-12 children.
 - combined known-shard diagnostic scaled estimate: `N12 ~ 6782225`.
 - no budget/time/sample flags; prune counters remain zero.
 - branch range over the known 71 shards remains 12.476..17.564, with the maximum at shard 64.

VERDICT:
Accepted. These two shards are exact for their owned source-parent slices and can be included in the
final exact 512-shard aggregate/merge. The aggregate remains diagnostic until all 512 shard indexes
are covered without `--allow-incomplete`.

NEXT ACTION:
Rerun the local proof gates after this documentation update, refresh graphify, then either continue
exact `N12` coverage with the next unmeasured contiguous pair `68..69` or pause for a genuinely new
algebraic lever. The shallow d11->d12 band remains non-pruning.

---

## R137 -- exact-contributing d11->d12 shards 64..65/512 completed; known N12 coverage now 69/512 [2026-06-30]
## OUTCOME: two more proof-grade shard stats/frontiers were added via the cloud wrapper path; shard 64
sets the current observed high branch among measured d11->d12 shards.

COMMAND:
`python s3_cloud_r3_d12.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --indices 64-65 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --tag r3_d11_to_d12_shard512_exact_r137 --aggregate-out scratchpad\r3_d11_to_d12_shard512_064_065_exact_aggregate_r137.json --skip-gate`

RESULTS:
 - shard 64/512: 906 depth-11 parents -> 15913 depth-12 children, branching 17.564, wall 136.85s.
 - shard 65/512: 906 depth-11 parents -> 13255 depth-12 children, branching 14.630, wall 136.26s.
 - both frontier files were physically recounted and match their JSON stats/header counts exactly:
   15913 and 13255 rows.
 - batch aggregate `scratchpad\r3_d11_to_d12_shard512_064_065_exact_aggregate_r137.json`:
   1812 depth-11 parents -> 29168 depth-12 children, diagnostic scaled `N12 ~ 7463209`.
 - combined known-shard aggregate:
   `scratchpad\r3_d11_to_d12_shard512_known69_aggregate_r137.json`
   covers shards `0..65,128,256,384`, i.e. 62513/463636 depth-11 parents = 13.4832%,
   with 914695 measured depth-12 children.
 - combined known-shard diagnostic scaled estimate: `N12 ~ 6783957`.
 - no budget/time/sample flags; prune counters remain zero.
 - branch range over the known 69 shards is now 12.476..17.564, with the maximum at shard 64.

VERDICT:
Accepted. These two shards are exact for their owned source-parent slices and can be included in the
final exact 512-shard aggregate/merge. The aggregate remains diagnostic until all 512 shard indexes
are covered without `--allow-incomplete`.

NEXT ACTION:
Rerun the local proof gates after this documentation update, then either continue exact `N12` coverage
with the next unmeasured contiguous pair `66..67` or pause for a genuinely new algebraic lever. The
shallow d11->d12 band remains non-pruning.

---

## R136 -- contiguous d11->d12 block 0..63/512 aggregate written [2026-06-30]
## OUTCOME: packaged the first contiguous 64-shard block as its own reproducible checkpoint, separate
from the spaced probes 128/256/384.

COMMAND:
Inline Python selected shard stats with indexes `0..63` and ran:
`python s3_aggregate_shards.py ... --allow-incomplete --out scratchpad\r3_d11_to_d12_shard512_000_063_aggregate_r136.json`

RESULTS:
 - aggregate file: `scratchpad\r3_d11_to_d12_shard512_000_063_aggregate_r136.json`
 - shard indexes: exactly `0..63`
 - coverage: 57984/463636 depth-11 parents = 12.5064%
 - measured depth-12 rows: 846839
 - diagnostic scaled estimate: `N12 ~ 6771265`
 - no budget/time flags; prune counters remain zero.
 - consistency check against `known67`:
   `known67 - block0..63` equals the three spaced probes `128,256,384`, namely 2717 parents and
   38688 depth-12 rows.

VERDICT:
Accepted as a reusable worker-sized checkpoint. It is not an exact global N12 count, but it is exact
for the contiguous owned source-parent block `0..63` and helps cloud reproducibility/auditing.

NEXT ACTION:
Continue exact `N12` coverage with the next unmeasured contiguous pair `64..65`, or pause for a
genuinely new algebraic lever.

---

## R135 -- exact-contributing d11->d12 shards 62..63/512 completed; known N12 coverage now 67/512 [2026-06-30]
## OUTCOME: two more proof-grade shard stats/frontiers were added via the cloud wrapper path.

COMMAND:
`python s3_cloud_r3_d12.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --indices 62-63 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --tag r3_d11_to_d12_shard512_exact_r135 --aggregate-out scratchpad\r3_d11_to_d12_shard512_062_063_exact_aggregate_r135.json --skip-gate`

RESULTS:
 - shard 62/512: 906 depth-11 parents -> 12768 depth-12 children, branching 14.093, wall 134.79s.
 - shard 63/512: 906 depth-11 parents -> 13176 depth-12 children, branching 14.543, wall 138.40s.
 - both frontier files were physically recounted and match their JSON stats/header counts exactly:
   12768 and 13176 rows.
 - batch aggregate `scratchpad\r3_d11_to_d12_shard512_062_063_exact_aggregate_r135.json`:
   1812 depth-11 parents -> 25944 depth-12 children, diagnostic scaled `N12 ~ 6638285`.
 - combined known-shard aggregate:
   `scratchpad\r3_d11_to_d12_shard512_known67_aggregate_r135.json`
   covers shards `0..63,128,256,384`, i.e. 60701/463636 depth-11 parents = 13.0924%,
   with 885527 measured depth-12 children.
 - combined known-shard diagnostic scaled estimate: `N12 ~ 6763681`.
 - no budget/time/sample flags; prune counters remain zero.
 - branch range over the known 67 shards remains 12.476..16.914.

VERDICT:
Accepted. These two shards are exact for their owned source-parent slices and can be included in the
final exact 512-shard aggregate/merge. The aggregate remains diagnostic until all 512 shard indexes
are covered without `--allow-incomplete`.

NEXT ACTION:
The contiguous block `0..63` is now covered for d11->d12, plus spaced probes `128,256,384`. Continue
exact `N12` coverage with the next unmeasured contiguous pair `64..65`, or pause for a genuinely new
algebraic lever. The shallow d11->d12 band remains non-pruning.

---

## R134 -- exact-contributing d11->d12 shards 60..61/512 completed; known N12 coverage now 65/512 [2026-06-30]
## OUTCOME: two more proof-grade shard stats/frontiers were added via the cloud wrapper path.

COMMAND:
`python s3_cloud_r3_d12.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --indices 60-61 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --tag r3_d11_to_d12_shard512_exact_r134 --aggregate-out scratchpad\r3_d11_to_d12_shard512_060_061_exact_aggregate_r134.json --skip-gate`

RESULTS:
 - shard 60/512: 906 depth-11 parents -> 12840 depth-12 children, branching 14.172, wall 137.03s.
 - shard 61/512: 906 depth-11 parents -> 14152 depth-12 children, branching 15.620, wall 182.81s.
 - both frontier files were physically recounted and match their JSON stats/header counts exactly:
   12840 and 14152 rows.
 - batch aggregate `scratchpad\r3_d11_to_d12_shard512_060_061_exact_aggregate_r134.json`:
   1812 depth-11 parents -> 26992 depth-12 children, diagnostic scaled `N12 ~ 6906437`.
 - combined known-shard aggregate:
   `scratchpad\r3_d11_to_d12_shard512_known65_aggregate_r134.json`
   covers shards `0..61,128,256,384`, i.e. 58889/463636 depth-11 parents = 12.7016%,
   with 859583 measured depth-12 children.
 - combined known-shard diagnostic scaled estimate: `N12 ~ 6767539`.
 - no budget/time/sample flags; prune counters remain zero.
 - branch range over the known 65 shards remains 12.476..16.914.

VERDICT:
Accepted. These two shards are exact for their owned source-parent slices and can be included in the
final exact 512-shard aggregate/merge. The aggregate remains diagnostic until all 512 shard indexes
are covered without `--allow-incomplete`.

NEXT ACTION:
Continue exact `N12` coverage (next contiguous pair 62..63) or pause for a genuinely new algebraic
lever. The shallow d11->d12 band remains non-pruning.

---

## R133 -- exact-contributing d11->d12 shards 58..59/512 completed; known N12 coverage now 63/512 [2026-06-30]
## OUTCOME: two more proof-grade shard stats/frontiers were added via the cloud wrapper path.

COMMAND:
`python s3_cloud_r3_d12.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --indices 58-59 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --tag r3_d11_to_d12_shard512_exact_r133 --aggregate-out scratchpad\r3_d11_to_d12_shard512_058_059_exact_aggregate_r133.json --skip-gate`

RESULTS:
 - shard 58/512: 906 depth-11 parents -> 13630 depth-12 children, branching 15.044, wall 201.16s.
 - shard 59/512: 906 depth-11 parents -> 13268 depth-12 children, branching 14.645, wall 192.64s.
 - both frontier files were physically recounted and match their JSON stats/header counts exactly:
   13630 and 13268 rows.
 - batch aggregate `scratchpad\r3_d11_to_d12_shard512_058_059_exact_aggregate_r133.json`:
   1812 depth-11 parents -> 26898 depth-12 children, diagnostic scaled `N12 ~ 6882385`.
 - combined known-shard aggregate:
   `scratchpad\r3_d11_to_d12_shard512_known63_aggregate_r133.json`
   covers shards `0..59,128,256,384`, i.e. 57077/463636 depth-11 parents = 12.3107%,
   with 832591 measured depth-12 children.
 - combined known-shard diagnostic scaled estimate: `N12 ~ 6763130`.
 - no budget/time/sample flags; prune counters remain zero.
 - branch range over the known 63 shards remains 12.476..16.914.

VERDICT:
Accepted. These two shards are exact for their owned source-parent slices and can be included in the
final exact 512-shard aggregate/merge. The aggregate remains diagnostic until all 512 shard indexes
are covered without `--allow-incomplete`.

NEXT ACTION:
Continue exact `N12` coverage (next contiguous pair 60..61) or pause for a genuinely new algebraic
lever. The shallow d11->d12 band remains non-pruning.

---

## R132 -- cloud wrapper exercised on d11->d12 shards 56..57/512; known N12 coverage now 61/512 [2026-06-30]
## OUTCOME: validated the one-command `s3_cloud_r3_d12.py --indices` path on the next shard pair and
added two more proof-grade shard stats/frontiers.

COMMAND:
`python s3_cloud_r3_d12.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --indices 56-57 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --tag r3_d11_to_d12_shard512_exact_r132 --aggregate-out scratchpad\r3_d11_to_d12_shard512_056_057_exact_aggregate_r132.json --skip-gate`

RESULTS:
 - shard 56/512: 906 depth-11 parents -> 13023 depth-12 children, branching 14.374, wall 194.51s.
 - shard 57/512: 906 depth-11 parents -> 13073 depth-12 children, branching 14.429, wall 196.67s.
 - both frontier files were physically recounted and match their JSON stats/header counts exactly:
   13023 and 13073 rows.
 - batch aggregate `scratchpad\r3_d11_to_d12_shard512_056_057_exact_aggregate_r132.json`:
   1812 depth-11 parents -> 26096 depth-12 children, diagnostic scaled `N12 ~ 6677177`.
 - combined known-shard aggregate:
   `scratchpad\r3_d11_to_d12_shard512_known61_aggregate_r132.json`
   covers shards `0..57,128,256,384`, i.e. 55265/463636 depth-11 parents = 11.9200%,
   with 805693 measured depth-12 children.
 - combined known-shard diagnostic scaled estimate: `N12 ~ 6759220`.
 - no budget/time/sample flags; prune counters remain zero.
 - branch range over the known 61 shards remains 12.476..16.914.

VERDICT:
Accepted. The cloud wrapper's targeted-shard path is now directly exercised on real shards, not only
dry-run command expansion. These two shards are exact for their owned source-parent slices and can be
included in the final exact 512-shard aggregate/merge. The aggregate remains diagnostic until all 512
shard indexes are covered without `--allow-incomplete`.

NEXT ACTION:
Continue exact `N12` coverage (next contiguous pair 58..59) or pause for a genuinely new algebraic
lever. The shallow d11->d12 band remains non-pruning.

---

## R131 -- exact-contributing d11->d12 shards 54..55/512 completed; known N12 coverage now 59/512 [2026-06-30]
## OUTCOME: two more proof-grade shard stats/frontiers were added after the R130 reassessment justified
continuing the exact `N12` measurement.

COMMAND:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --indices 54-55 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --tag r3_d11_to_d12_shard512_exact_r131 --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --aggregate-out scratchpad\r3_d11_to_d12_shard512_054_055_exact_aggregate_r131.json --allow-incomplete`

RESULTS:
 - shard 54/512: 906 depth-11 parents -> 13662 depth-12 children, branching 15.079, wall 207.00s.
 - shard 55/512: 906 depth-11 parents -> 12676 depth-12 children, branching 13.991, wall 180.03s.
 - both frontier files were physically recounted and match their JSON stats/header counts exactly:
   13662 and 12676 rows.
 - batch aggregate `scratchpad\r3_d11_to_d12_shard512_054_055_exact_aggregate_r131.json`:
   1812 depth-11 parents -> 26338 depth-12 children, diagnostic scaled `N12 ~ 6739098`.
 - combined known-shard aggregate:
   `scratchpad\r3_d11_to_d12_shard512_known59_aggregate_r131.json`
   covers shards `0..55,128,256,384`, i.e. 53453/463636 depth-11 parents = 11.5291%,
   with 779597 measured depth-12 children.
 - combined known-shard diagnostic scaled estimate: `N12 ~ 6762001`.
 - no budget/time/sample flags; prune counters remain zero.
 - branch range over the known 59 shards remains 12.476..16.914.

VERDICT:
Accepted. These two shards are exact for their owned source-parent slices and can be included in the
final exact 512-shard aggregate/merge. The aggregate remains diagnostic until all 512 shard indexes
are covered without `--allow-incomplete`.

NEXT ACTION:
Continue exact `N12` coverage (next contiguous pair 56..57) or pause for a genuinely new algebraic
lever. The shallow d11->d12 band remains non-pruning.

---

## R130 -- post-R129 graphify reassessment: no better local lever than exact N12 coverage [2026-06-30]
## OUTCOME: checked the graphified corpus before launching more shard batches. The query hits point to
already-closed lines or the R124/R125 edge-Gram line, not to a new bounded local obstruction.

COMMANDS:
 - `graphify query "edge-local eigenspace Gram relations line graph projector strongly regular graph star complement pruning"`
 - `graphify query "partial strongly regular graph nonextendability spectral certificate edge vectors star complement"`
 - `graphify query "r=3 s=-4 star complement bridge eigenvalue constraints edge vector"`
 - `rg -n "H3|h3_forced|h3_propagate|force_mu_saturated|force_lambda_mate" progress.md FINAL_REPORT.md CLOUD_SPEC_SC.md literature_99graph\notes\current_pipeline_summary.md`

RESULTS:
 - Edge-vector/projector queries route back to the R124/R125 Gram-spectrum idea and older rank/lattice
   files, with no new implementable relation surfaced.
 - Nonextendability queries route to `h3_forced.py` / `h3_propagate.py`, but `progress.md` R30 already
   records this H3/n3 line as a clean negative: the H3 environment and counts were fully mapped, `n3`
   stays free, and further linear H3 counting was marked void.
 - The `r=3`/`s=-4` bridge query did not surface a new source-backed bounded test beyond existing
   star-complement and edge-vector work.

DECISION:
Resume exact `N12` coverage as the best near-term verified progress. This is not a mathematical
obstruction, but it is the validated cost/calibration experiment after the SCAMPER/Taylor/edge-vector
branches were falsified or measured as non-pruning.

NEXT ACTION:
Continue exact d11->d12 shards with the next contiguous pair 54..55.

---

## R129 -- exact-contributing d11->d12 shards 52..53/512 completed; known N12 coverage now 57/512 [2026-06-30]
## OUTCOME: two more proof-grade shard stats/frontiers were added to the exact `N12` measurement.

COMMAND:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --indices 52-53 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --tag r3_d11_to_d12_shard512_exact_r129 --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --aggregate-out scratchpad\r3_d11_to_d12_shard512_052_053_exact_aggregate_r129.json --allow-incomplete`

RESULTS:
 - shard 52/512: 906 depth-11 parents -> 12349 depth-12 children, branching 13.630, wall 135.41s.
 - shard 53/512: 906 depth-11 parents -> 12433 depth-12 children, branching 13.723, wall 158.61s.
 - both frontier files were physically recounted and match their JSON stats/header counts exactly:
   12349 and 12433 rows.
 - batch aggregate `scratchpad\r3_d11_to_d12_shard512_052_053_exact_aggregate_r129.json`:
   1812 depth-11 parents -> 24782 depth-12 children, diagnostic scaled `N12 ~ 6340964`.
 - combined known-shard aggregate:
   `scratchpad\r3_d11_to_d12_shard512_known57_aggregate_r129.json`
   covers shards `0..53,128,256,384`, i.e. 51641/463636 depth-11 parents = 11.1383%,
   with 753259 measured depth-12 children.
 - combined known-shard diagnostic scaled estimate: `N12 ~ 6762805`.
 - no budget/time/sample flags; prune counters remain zero.
 - branch range over the known 57 shards remains 12.476..16.914.

VERDICT:
Accepted. These two shards are exact for their owned source-parent slices and can be included in the
final exact 512-shard aggregate/merge. The aggregate remains diagnostic until all 512 shard indexes
are covered without `--allow-incomplete`.

NEXT ACTION:
Continue exact `N12` coverage (next contiguous pair 54..55) or pause for a genuinely new algebraic
lever. The shallow d11->d12 band remains non-pruning.

---

## R128 -- exact-contributing d11->d12 shards 50..51/512 completed; known N12 coverage now 55/512 [2026-06-30]
## OUTCOME: two more proof-grade shard stats/frontiers were added to the exact `N12` measurement.

COMMAND:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --indices 50-51 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --tag r3_d11_to_d12_shard512_exact_r128 --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --aggregate-out scratchpad\r3_d11_to_d12_shard512_050_051_exact_aggregate_r128.json --allow-incomplete`

RESULTS:
 - shard 50/512: 906 depth-11 parents -> 13507 depth-12 children, branching 14.908, wall 150.91s.
 - shard 51/512: 906 depth-11 parents -> 14565 depth-12 children, branching 16.076, wall 138.06s.
 - both frontier files were physically recounted and match their JSON stats/header counts exactly:
   13507 and 14565 rows.
 - batch aggregate `scratchpad\r3_d11_to_d12_shard512_050_051_exact_aggregate_r128.json`:
   1812 depth-11 parents -> 28072 depth-12 children, diagnostic scaled `N12 ~ 7182776`.
 - combined known-shard aggregate:
   `scratchpad\r3_d11_to_d12_shard512_known55_aggregate_r128.json`
   covers shards `0..51,128,256,384`, i.e. 49829/463636 depth-11 parents = 10.7464%,
   with 728477 measured depth-12 children.
 - combined known-shard diagnostic scaled estimate: `N12 ~ 6778145`.
 - no budget/time/sample flags; prune counters remain zero.
 - branch range over the known 55 shards remains 12.476..16.914.

VERDICT:
Accepted. These two shards are exact for their owned source-parent slices and can be included in the
final exact 512-shard aggregate/merge. The aggregate remains diagnostic until all 512 shard indexes
are covered without `--allow-incomplete`.

NEXT ACTION:
Continue exact `N12` coverage (next contiguous pair 52..53) or pause for a genuinely new algebraic
lever. Shallow d11->d12 data still shows no pruning.

---

## R127 -- exact-contributing d11->d12 shards 48..49/512 completed; known N12 coverage now 53/512 [2026-06-30]
## OUTCOME: two more proof-grade shard stats/frontiers were added. Known d11->d12 coverage crossed
10% of the complete depth-11 frontier.

COMMANDS:
 - The first wrapper attempt exited before writing shard 48 output; no partial stats/frontier files
   existed. Direct shard runs were then used:
   `python s3_slice_harness.py --slice --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --shard-index 48 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --stats-out scratchpad\r3_d11_to_d12_shard512_exact_r127_048.json --frontier-out scratchpad\r3_d11_to_d12_frontiers\r3_d11_to_d12_shard512_exact_r127_048_frontier.jsonl`
   and the same command for shard 49.
 - Pair aggregate:
   `python s3_aggregate_shards.py scratchpad\r3_d11_to_d12_shard512_exact_r127_048.json scratchpad\r3_d11_to_d12_shard512_exact_r127_049.json --allow-incomplete --out scratchpad\r3_d11_to_d12_shard512_048_049_exact_aggregate_r127.json`
 - Wrapper resume check:
   `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --indices 48-49 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --tag r3_d11_to_d12_shard512_exact_r127 --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --aggregate-out scratchpad\r3_d11_to_d12_shard512_048_049_exact_aggregate_r127.json --allow-incomplete`
   skipped both completed shards and re-aggregated successfully.

RESULTS:
 - shard 48/512: 906 depth-11 parents -> 11303 depth-12 children, branching 12.476, wall 142.69s.
 - shard 49/512: 906 depth-11 parents -> 13335 depth-12 children, branching 14.719, wall 138.68s.
 - both frontier files were physically recounted and match their JSON stats/header counts exactly:
   11303 and 13335 rows.
 - batch aggregate `scratchpad\r3_d11_to_d12_shard512_048_049_exact_aggregate_r127.json`:
   1812 depth-11 parents -> 24638 depth-12 children, diagnostic scaled `N12 ~ 6304119`.
 - combined known-shard aggregate:
   `scratchpad\r3_d11_to_d12_shard512_known53_aggregate_r127.json`
   covers shards `0..49,128,256,384`, i.e. 48017/463636 depth-11 parents = 10.3577%,
   with 700405 measured depth-12 children.
 - combined known-shard diagnostic scaled estimate: `N12 ~ 6762875`.
 - no budget/time/sample flags; prune counters remain zero.
 - branch range over the known 53 shards is now 12.476..16.914.

VERDICT:
Accepted. These two shards are exact for their owned source-parent slices and can be included in the
final exact 512-shard aggregate/merge. The aggregate remains diagnostic until all 512 shard indexes
are covered without `--allow-incomplete`.

NEXT ACTION:
Continue exact `N12` coverage (next contiguous pair 50..51) or pause for a genuinely new algebraic
lever. Shallow d11->d12 data still shows no pruning, so this remains a measurement/cost calibration
track, not a proof obstruction.

---

## R126 -- exact-contributing d11->d12 shards 46..47/512 completed; known N12 coverage now 51/512 [2026-06-30]
## OUTCOME: two more proof-grade shard stats/frontiers were added to the exact `N12` measurement.

COMMAND:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --indices 46-47 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --tag r3_d11_to_d12_shard512_exact_r126 --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --aggregate-out scratchpad\r3_d11_to_d12_shard512_046_047_exact_aggregate_r126.json --allow-incomplete`

RESULTS:
 - shard 46/512: 906 depth-11 parents -> 13421 depth-12 children, branching 14.813, wall 134.87s.
 - shard 47/512: 906 depth-11 parents -> 12437 depth-12 children, branching 13.727, wall 136.41s.
 - both frontier files were physically recounted and match their JSON stats/header counts exactly:
   13421 and 12437 rows.
 - batch aggregate `scratchpad\r3_d11_to_d12_shard512_046_047_exact_aggregate_r126.json`:
   1812 depth-11 parents -> 25858 depth-12 children, diagnostic scaled `N12 ~ 6616280`.
 - combined known-shard aggregate:
   `scratchpad\r3_d11_to_d12_shard512_known51_aggregate_r126.json`
   covers shards `0..47,128,256,384`, i.e. 46205/463636 depth-11 parents = 9.9658%,
   with 675767 measured depth-12 children.
 - combined known-shard diagnostic scaled estimate: `N12 ~ 6780866`.
 - no budget/time/sample flags; prune counters remain zero.
 - branch range over the known 51 shards remains 12.500..16.914.

VERDICT:
Accepted. These two shards are exact for their owned source-parent slices and can be included in the
final exact 512-shard aggregate/merge. The aggregate remains diagnostic until all 512 shard indexes
are covered without `--allow-incomplete`.

NEXT ACTION:
Continue exact `N12` coverage (next contiguous pair 48..49) or pause for a genuinely new algebraic
lever. Shallow d11->d12 data still shows no pruning, so the measurement value is coverage/cost
calibration rather than a mathematical obstruction.

---

## R125 -- edge-vector projector upper-spectrum certificate added; still no Taylor prune [2026-06-30]
## OUTCOME: strengthened the R124 Gram checker with the full-graph projector eigenvalue bound and
validated it on real graphs. The sharper condition still does not prune the measured Taylor frontiers.

SCRIPT:
`s3_edge_vector_gram_probe.py`

NEW PREDICATE:
For present-edge vectors `y_ab = (A+4I)(e_a-e_b)`, the full-graph Gram matrix has all nonzero
eigenvalues equal to `(r-s)^2(k-r) = 7^2 * 11 = 539`. Therefore every principal edge-vector Gram
matrix in a real partial must be PSD, have rank at most `54`, and have largest eigenvalue at most
`539`.

REAL-WITNESS VALIDATION:
 - `python -m py_compile s3_edge_vector_gram_probe.py`
 - `python s3_edge_vector_gram_probe.py --self-test`
 - T(7)=srg(21,10,5,4): rank `6/6`, largest eigenvalue `175`, upper bound `175`.
 - rook(9)=srg(9,4,1,2): rank `4/4`, largest eigenvalue `27`, upper bound `27`.

MEASUREMENT:
 - `python s3_edge_vector_gram_probe.py scratchpad\taylor_fullhost_frontier_d28_r123.jsonl --out scratchpad\edge_vector_gram_taylor_d28_r125.json`
   scanned 879 rows: bad PSD/rank/upper = `0/0/0`, max rank `26`, max largest eigenvalue
   `309.77824991683514`.
 - `python s3_edge_vector_gram_probe.py scratchpad\taylor_fullhost_frontier_d29_shard64_000_r123.jsonl --out scratchpad\edge_vector_gram_taylor_d29_shard64_000_r125.json`
   scanned 46017 rows: bad PSD/rank/upper = `0/0/0`, max rank `27`, max largest eigenvalue
   `316.5697539152634`.

VERDICT:
 - The edge-vector projector spectrum is a sounder certificate than the R124 PSD/rank-only check and
   now has a real-witness self-test.
 - It is still not an early pruning rule on the measured Taylor full-host data: the frontier rows are
   comfortably below the `539` upper bound.

NEXT ACTION:
Do not spend another cycle on principal edge-vector Gram spectra at d28/d29. Either derive a genuinely
stronger relation among edge-local vectors, or return to the exact `N12` measurement as the validated
cost-reducing experiment.

---

## R124 -- simple edge-vector Gram PSD/rank gate tested; no early prune on Taylor d28/d29 [2026-06-30]
## OUTCOME: the first edge-local eigenspace gate is sound and reusable, but it does not prune the
measured Taylor full-host frontiers through depth 29.

SCRIPT:
`s3_edge_vector_gram_probe.py`

COMMANDS:
 - `python -m py_compile s3_edge_vector_gram_probe.py`
 - `python s3_edge_vector_gram_probe.py scratchpad\taylor_fullhost_frontier_d28_r123.jsonl --out scratchpad\edge_vector_gram_taylor_d28_r124.json`
 - `python s3_edge_vector_gram_probe.py scratchpad\taylor_fullhost_frontier_d29_shard64_000_r123.jsonl --out scratchpad\edge_vector_gram_taylor_d29_shard64_000_r124.json`

RESULTS:
 - d28 full Taylor frontier: 879 rows scanned, bad PSD/rank = 0/0, max rank 26, min least eigenvalue
   about `-1.54e-13` (numeric zero).
 - d29 shard 0/64: 46017 rows scanned, bad PSD/rank = 0/0, max rank 27, min least eigenvalue
   about `-1.52e-13`.

VERDICT:
 - The principal Gram condition for edge-local vectors `(A+4I)(e_a-e_b)` is not an early pruning
   gate on the Taylor full-host route. It remains a reusable validation/certificate check, but do
   not spend another cycle on the same PSD/rank test at these depths.
 - A stronger edge-vector lever would need relations beyond principal PSD/rank, such as forced
   dependencies among many local edge vectors, interaction with the 54-dimensional global span, or
   equations involving non-present edges.

NEXT ACTION:
Either derive a stronger edge-vector relation (not just principal Gram PSD), or return to the
validated exact-N12 cloud measurement as the next cost-reducing experiment. Do not scale naive
Taylor full-host brute force or the simple edge-Gram gate.

---

## R123 -- sound Taylor full-host probe built; naive full-host continuation explodes by d29 [2026-06-30]
## OUTCOME: the R122 sound fallback was implemented and measured. It is runnable and chainable, but
the naive full-host Taylor continuation is not a collapse route without a new algebraic cut.

SCRIPT:
`s3_taylor_fullhost_probe.py`

PROOF NOTE:
`EDGE_LOCAL_EIGENVECTORS_R123.md`

VALIDATION / SMOKE:
 - `python -m py_compile s3_taylor_fullhost_probe.py`
 - `python s3_taylor_fullhost_probe.py --target-depth 27 --out scratchpad\taylor_fullhost_probe_smoke2_r123.json --frontier-out scratchpad\taylor_fullhost_frontier_d27_smoke_r123.jsonl`
 - `python s3_taylor_fullhost_probe.py --frontier-in scratchpad\taylor_fullhost_frontier_d27_smoke_r123.jsonl --target-depth 27 --out scratchpad\taylor_fullhost_probe_smoke2_resume_r123.json`

FULL-HOST d27->d28 MEASUREMENT:
`python s3_taylor_fullhost_probe.py --target-depth 28 --time-cap 600 --out scratchpad\taylor_fullhost_probe_d28_r123.json --frontier-out scratchpad\taylor_fullhost_frontier_d28_r123.jsonl`

 - node counts: depth 27 = 11, depth 28 = 879.
 - saturated-exact rejects: 18496.
 - spectral rejects: 0.
 - BLISS duplicates: 36571.
 - children per parent: 79.909.
 - wall: 127s on rerun with frontier output.
 - complete reusable d28 frontier written to `scratchpad\taylor_fullhost_frontier_d28_r123.jsonl`.

FULL-HOST d28->d29 SHARD MEASUREMENT:
`python s3_taylor_fullhost_probe.py --frontier-in scratchpad\taylor_fullhost_frontier_d28_r123.jsonl --target-depth 29 --shard-count 64 --shard-index 0 --time-cap 600 --out scratchpad\taylor_fullhost_probe_d29_shard64_000_r123.json --frontier-out scratchpad\taylor_fullhost_frontier_d29_shard64_000_r123.jsonl`

 - shard parents: 14 depth-28 reps.
 - depth-29 children in shard: 46017.
 - saturated-exact rejects: 41837.
 - spectral rejects: 0.
 - BLISS duplicates: 32490.
 - branch on this shard: 3286.9 children/parent.
 - wall: 303s.

VERDICT:
 - The full-host Taylor route is now one-command runnable and chainable, and it is sound in the
   sense that it uses only full-host local lambda/mu conditions and hereditary spectral gates.
 - Naive continuation is not a near-term decisive search route: the first d29 shard already explodes,
   and spectral gates still do not fire because the supported 3-eigenvector keeps the templates on
   the boundary rather than beyond it.
 - Do not scale full-host Taylor brute force without a new algebraic cut.

NEXT ACTION:
Exploit the edge-local 3-eigenvector algebra instead of brute-force growth. For every adjacent edge
`a~b` with common neighbour `c`, the Taylor vector is
`(A+4I)(e_a-e_b)`, supported on `{a,b} union N(a) union N(b)`, and lies in the 54-dimensional
3-eigenspace. Build a proof/measurement note for the span/Gram constraints of these 693 edge-vectors
and test whether their local support equations imply a new obstruction or a safe full-host pruning rule.

---

## R122 -- Taylor full-template containment in r=3 star complements is impossible; route redirected to full-host search [2026-06-30]
## OUTCOME: the R121 containment lemma was falsified by an exact supported-eigenvector argument.

COMMAND:
`python s3_taylor_supported_eigenvector.py --out scratchpad\taylor_supported_eigenvector_r122.json`

PROOF NOTE:
`TAYLOR_SUPPORTED_EIGENVECTOR_R122.md`

RESULT:
 - For every one of the 11 Taylor 27-vertex adjacent-pair templates, the same integer vector
   is an exact 3-eigenvector of the induced template:
   `[3,-3,0,1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]`.
 - The script verifies `A_S x = 3x` on all 11 templates and verifies the endpoint structure:
   vertices 0 and 1 have degree 14, share only vertex 2, with twelve 0-only neighbours and
   twelve 1-only neighbours.
 - Algebraic extension argument: any valid new vertex outside the combined neighborhood is
   nonadjacent to 0 and 1. Since 0 and 1 are saturated, the `mu=2` exact requirement forces the
   new vertex to have exactly two neighbors in `N(0)` and exactly two in `N(1)`. The shared
   neighbor 2 has vector weight 0, so the new vertex sees equal total +1 and -1 weights. Thus
   the dot product with the supported vector is 0, and the vector remains a 3-eigenvector in
   every valid induced extension containing the full Taylor template.
 - Consequence: no r=3 star complement can contain a full Taylor adjacent-pair template, because
   an r=3 star complement must have no eigenvalue 3.

VERDICT:
 - The R121 seeded r=3 Stage-A run is now explained: it was following a boundary slice that is
   guaranteed to fail the terminal `mult_3(H)=0` star-complement condition. It is diagnostic only
   and should not be scaled as an H-search.
 - The Taylor local-template lever remains valuable, but only as a sound full-host search seed
   (or as a source of boundary/eigenvector equations), not as a star-complement containment seed.

NEXT ACTION:
Build `s3_taylor_fullhost_probe.py`: start from the 11 Taylor templates, grow induced full-host
partials using lambda=1/mu=2 local gates and hereditary spectral gates, but remove r=3
star-complement-specific edge-band and terminal `mult_3(H)=0` assumptions. Compare depth 30..33
against Taylor's old full-search explosion.

---

## R121 -- Taylor adjacent-pair boundary templates reconstructed; seeded r=3 diagnostic collapses d27->d29 [2026-06-30]
## OUTCOME: the mandatory graphify + SCAMPER breakthrough pass is complete, and it produced a
source-backed local-template lever that is stronger than the ordinary shallow shard track.

SOURCE / SCAMPER MEMO:
 - Wrote `SCAMPER_BREAKTHROUGH_R121.md`.
 - Graphify/source pass used Taylor adjacent-neighborhood classification, star-complement sources,
   Keramatipour SAT, SMS/Traces, Shpectorov-Zhao, Reimbayev, Peeters p-rank, and the current R119
   harness telemetry.
 - Decision: do NOT resume ordinary d11->d12 shard filling as the next move. The Taylor boundary-seed
   line must be tested/proved first, because it reaches the spectral boundary immediately while
   ordinary depth-12 shards still show zero pruning.

COMMANDS / ARTIFACTS:
 - Rebuilt Taylor's 27-vertex adjacent-pair combined-neighborhood templates:
   `python s3_taylor_edge_templates.py --out scratchpad\taylor_edge_templates_r120.json`
 - Added one-command seeded diagnostic probe:
   `s3_taylor_seed_probe.py`
 - Smoke-tested the packaged probe:
   `python s3_taylor_seed_probe.py --target-depth 27 --out scratchpad\taylor_seed_probe_smoke_r121.json`
 - Ran the full d27->d29 seeded diagnostic inline through `generate_stageA(initial_level=templates)`.
 - Reran the main soundness gate after the new scripts:
   `python s3_slice_harness.py --gate`

RESULTS:
 - Taylor notebook count ladder reproduced exactly with current BLISS canonicalization:
   valid graph counts for orders 16..27 =
   `1,11,20,27,40,56,60,85,68,78,38,19`;
   representative counts =
   `1,2,3,5,8,10,17,17,26,19,19,11`.
 - All 11 final templates replay through the current `PartialGraph.can_add` local gate.
 - Template edge core: 41 common edges, 20 varying edges, 61 union edges.
 - Each final template has exact inertia `A-3I = (1,25,1)`, so each has one eigenvalue 3;
   float checks also give `lambda2 = 3` and `lambda_min = -4`.
 - Seeded Stage-A diagnostic from the 11 depth-27 templates:
   depth 27 -> 11 reps, depth 28 -> 11 reps, depth 29 -> 11 reps.
   Spectral prunes: 50784. Local prunes: 0. Triangle-split prunes: 0.
   Canonical-parent rejects: 117032. Cache hits: 114102. Wall: 420.31s.
   No time/budget/sample flags in the d29 run.
 - Main harness soundness gate remained ALL GREEN after the additions.

VERDICT:
 - Accepted as a real, measured diagnostic lever. R122 later falsifies the proof-completeness
   condition for using full Taylor templates as r=3 star-complement seeds: such templates always
   carry a supported 3-eigenvector.
 - Therefore the r=3 H-seeded version should not be scaled. Recast the same source-backed route
   as a full-host Taylor-template continuation with spectral gates and without star-complement-
   specific edge-band assumptions.

NEXT ACTION:
Superseded by R122. Build `s3_taylor_fullhost_probe.py` and measure the sound full-host continuation
from the 11 templates.

---

## R119 -- exact-contributing d11->d12 shards 44..45/512 completed; shard loop paused for mandatory breakthrough pass [2026-06-30]
## OUTCOME: two more proof-grade shard stats/frontiers were added for the eventual exact `N12`
aggregate. Known d11->d12 shard coverage is now 49/512 shards.

COMMANDS RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --indices 44-45 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --tag r3_d11_to_d12_shard512_exact_r119 --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --aggregate-out scratchpad\r3_d11_to_d12_shard512_044_045_exact_aggregate_r119.json --allow-incomplete`

 - then aggregated the known exact-contributing shard set into:
   `scratchpad\r3_d11_to_d12_shard512_known49_aggregate_r119.json`.
 - reran the harness soundness gate:
   `python s3_slice_harness.py --gate`.

RESULTS:
 - shard 44/512: 906 depth-11 parents -> 13519 depth-12 children, branching 14.922.
 - shard 45/512: 906 depth-11 parents -> 12526 depth-12 children, branching 13.826.
 - both frontier files were physically recounted and match their JSON stats/header counts exactly:
   13519 and 12526 rows.
 - batch aggregate `scratchpad\r3_d11_to_d12_shard512_044_045_exact_aggregate_r119.json`:
   1812 depth-11 parents -> 26045 depth-12 children, diagnostic scaled `N12 ~ 6664128`.
 - combined known-shard aggregate over shards 0..45 plus 128,256,384:
   `scratchpad\r3_d11_to_d12_shard512_known49_aggregate_r119.json`
   covers 44393/463636 parents = 9.5750%, with 649909 depth-12 children.
 - combined known-shard diagnostic scaled estimate: `N12 ~ 6787584`.
 - no budget/time/sample flags; prune counters remain zero.
 - branch range remains 12.500..16.914.
 - soundness gate remained all green: rook9 local replay accepts 362880/362880 orders, rook9 has
   0/511 srg99 r=3 spectral false rejects, triangle-split identity holds on all 512 rook9 subsets,
   T(7)=srg(21,10,5,4) r=3 CRS reconstruction/clique recovery succeeds, and Stage-A gates false-reject
   0/5242 real T(7) induced subgraphs.

VERDICT: accepted. These two shards are exact for their owned source-parent slices and can be included
in the final exact 512-shard aggregate/merge. The aggregate remains diagnostic until all shard indexes
0..511 are present. The shallow d11->d12 estimate remains stable around 6.7M-6.8M and still shows no
pruning.

NEXT ACTION: superseded by R121. The mandatory graphify + SCAMPER breakthrough memo is complete;
do not resume ordinary d11->d12 shard filling until the Taylor containment/deeper-seed decision is made.

---

## R118 -- exact-contributing d11->d12 shards 42..43/512 completed [2026-06-30]
## OUTCOME: two more proof-grade shard stats/frontiers were added for the eventual exact `N12`
aggregate. Known d11->d12 shard coverage is now 47/512 shards.

COMMANDS RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --indices 42-43 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --tag r3_d11_to_d12_shard512_exact_r118 --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --aggregate-out scratchpad\r3_d11_to_d12_shard512_042_043_exact_aggregate_r118.json --allow-incomplete`

 - then aggregated the known exact-contributing shard set into:
   `scratchpad\r3_d11_to_d12_shard512_known47_aggregate_r118.json`.
 - reran the harness soundness gate:
   `python s3_slice_harness.py --gate`.

RESULTS:
 - shard 42/512: 906 depth-11 parents -> 14049 depth-12 children, branching 15.507.
 - shard 43/512: 906 depth-11 parents -> 13885 depth-12 children, branching 15.326.
 - both frontier files were physically recounted and match their JSON stats/header counts exactly:
   14049 and 13885 rows.
 - batch aggregate `scratchpad\r3_d11_to_d12_shard512_042_043_exact_aggregate_r118.json`:
   1812 depth-11 parents -> 27934 depth-12 children, diagnostic scaled `N12 ~ 7147466`.
 - combined known-shard aggregate over shards 0..43 plus 128,256,384:
   `scratchpad\r3_d11_to_d12_shard512_known47_aggregate_r118.json`
   covers 42581/463636 parents = 9.1841%, with 623864 depth-12 children.
 - combined known-shard diagnostic scaled estimate: `N12 ~ 6792837`.
 - no budget/time/sample flags; prune counters remain zero.
 - branch range remains 12.500..16.914.
 - soundness gate remained all green: rook9 local replay accepts 362880/362880 orders, rook9 has
   0/511 srg99 r=3 spectral false rejects, triangle-split identity holds on all 512 rook9 subsets,
   T(7)=srg(21,10,5,4) r=3 CRS reconstruction/clique recovery succeeds, and Stage-A gates false-reject
   0/5242 real T(7) induced subgraphs.

VERDICT: accepted. These two shards are exact for their owned source-parent slices and can be included
in the final exact 512-shard aggregate/merge. The aggregate remains diagnostic until all shard indexes
0..511 are present. The shallow d11->d12 estimate remains stable around 6.7M-6.8M and still shows no
pruning.

NEXT ACTION: superseded by R119. Do NOT launch another shard batch until the mandatory graphify +
SCAMPER breakthrough memo is complete.

---

## R117 -- exact-contributing d11->d12 shards 40..41/512 completed [2026-06-30]
## OUTCOME: two more proof-grade shard stats/frontiers were added for the eventual exact `N12`
aggregate. Known d11->d12 shard coverage is now 45/512 shards.

COMMANDS RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --indices 40-41 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --tag r3_d11_to_d12_shard512_exact_r117 --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --aggregate-out scratchpad\r3_d11_to_d12_shard512_040_041_exact_aggregate_r117.json --allow-incomplete`

 - then aggregated the known exact-contributing shard set into:
   `scratchpad\r3_d11_to_d12_shard512_known45_aggregate_r117.json`.
 - reran the harness soundness gate:
   `python s3_slice_harness.py --gate`.

RESULTS:
 - shard 40/512: 906 depth-11 parents -> 13471 depth-12 children, branching 14.869.
 - shard 41/512: 906 depth-11 parents -> 12750 depth-12 children, branching 14.073.
 - both frontier files were physically recounted and match their JSON stats/header counts exactly:
   13471 and 12750 rows.
 - batch aggregate `scratchpad\r3_d11_to_d12_shard512_040_041_exact_aggregate_r117.json`:
   1812 depth-11 parents -> 26221 depth-12 children, diagnostic scaled `N12 ~ 6709161`.
 - combined known-shard aggregate over shards 0..41 plus 128,256,384:
   `scratchpad\r3_d11_to_d12_shard512_known45_aggregate_r117.json`
   covers 40769/463636 parents = 8.7933%, with 595930 depth-12 children.
 - combined known-shard diagnostic scaled estimate: `N12 ~ 6777076`.
 - no budget/time/sample flags; prune counters remain zero.
 - branch range remains 12.500..16.914.
 - soundness gate remained all green: rook9 local replay accepts 362880/362880 orders, rook9 has
   0/511 srg99 r=3 spectral false rejects, triangle-split identity holds on all 512 rook9 subsets,
   T(7)=srg(21,10,5,4) r=3 CRS reconstruction/clique recovery succeeds, and Stage-A gates false-reject
   0/5242 real T(7) induced subgraphs.

VERDICT: accepted. These two shards are exact for their owned source-parent slices and can be included
in the final exact 512-shard aggregate/merge. The aggregate remains diagnostic until all shard indexes
0..511 are present. The shallow d11->d12 estimate remains stable around 6.7M-6.8M and still shows no
pruning.

NEXT ACTION: superseded by R119. Do NOT launch another shard batch until the mandatory graphify +
SCAMPER breakthrough memo is complete.

---

## R116 -- exact-contributing d11->d12 shards 38..39/512 completed [2026-06-30]
## OUTCOME: two more proof-grade shard stats/frontiers were added for the eventual exact `N12`
aggregate. Known d11->d12 shard coverage is now 43/512 shards.

COMMANDS RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --indices 38-39 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --tag r3_d11_to_d12_shard512_exact_r116 --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --aggregate-out scratchpad\r3_d11_to_d12_shard512_038_039_exact_aggregate_r116.json --allow-incomplete`

 - then aggregated the known exact-contributing shard set into:
   `scratchpad\r3_d11_to_d12_shard512_known43_aggregate_r116.json`.
 - reran the harness soundness gate:
   `python s3_slice_harness.py --gate`.

RESULTS:
 - shard 38/512: 906 depth-11 parents -> 14775 depth-12 children, branching 16.308.
 - shard 39/512: 906 depth-11 parents -> 13023 depth-12 children, branching 14.374.
 - both frontier files were physically recounted and match their JSON stats/header counts exactly:
   14775 and 13023 rows.
 - batch aggregate `scratchpad\r3_d11_to_d12_shard512_038_039_exact_aggregate_r116.json`:
   1812 depth-11 parents -> 27798 depth-12 children, diagnostic scaled `N12 ~ 7112668`.
 - combined known-shard aggregate over shards 0..39 plus 128,256,384:
   `scratchpad\r3_d11_to_d12_shard512_known43_aggregate_r116.json`
   covers 38957/463636 parents = 8.4025%, with 569709 depth-12 children.
 - combined known-shard diagnostic scaled estimate: `N12 ~ 6780235`.
 - no budget/time/sample flags; prune counters remain zero.
 - branch range remains 12.500..16.914.
 - soundness gate remained all green: rook9 local replay accepts 362880/362880 orders, rook9 has
   0/511 srg99 r=3 spectral false rejects, triangle-split identity holds on all 512 rook9 subsets,
   T(7)=srg(21,10,5,4) r=3 CRS reconstruction/clique recovery succeeds, and Stage-A gates false-reject
   0/5242 real T(7) induced subgraphs.

VERDICT: accepted. These two shards are exact for their owned source-parent slices and can be included
in the final exact 512-shard aggregate/merge. The aggregate remains diagnostic until all shard indexes
0..511 are present. The shallow d11->d12 estimate remains stable around 6.7M-6.8M and still shows no
pruning.

NEXT ACTION: superseded by R119. Do NOT launch another shard batch until the mandatory graphify +
SCAMPER breakthrough memo is complete.

---

## R115 -- exact-contributing d11->d12 shards 36..37/512 completed [2026-06-30]
## OUTCOME: two more proof-grade shard stats/frontiers were added for the eventual exact `N12`
aggregate. Known d11->d12 shard coverage is now 41/512 shards.

COMMANDS RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --indices 36-37 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --tag r3_d11_to_d12_shard512_exact_r115 --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --aggregate-out scratchpad\r3_d11_to_d12_shard512_036_037_exact_aggregate_r115.json --allow-incomplete`

 - then aggregated the known exact-contributing shard set into:
   `scratchpad\r3_d11_to_d12_shard512_known41_aggregate_r115.json`.
 - reran the harness soundness gate:
   `python s3_slice_harness.py --gate`.

RESULTS:
 - shard 36/512: 906 depth-11 parents -> 13327 depth-12 children, branching 14.710.
 - shard 37/512: 906 depth-11 parents -> 14599 depth-12 children, branching 16.114.
 - both frontier files were physically recounted and match their JSON stats/header counts exactly:
   13327 and 14599 rows.
 - batch aggregate `scratchpad\r3_d11_to_d12_shard512_036_037_exact_aggregate_r115.json`:
   1812 depth-11 parents -> 27926 depth-12 children, diagnostic scaled `N12 ~ 7145419`.
 - combined known-shard aggregate over shards 0..37 plus 128,256,384:
   `scratchpad\r3_d11_to_d12_shard512_known41_aggregate_r115.json`
   covers 37145/463636 parents = 8.0117%, with 541911 depth-12 children.
 - combined known-shard diagnostic scaled estimate: `N12 ~ 6764018`.
 - no budget/time/sample flags; prune counters remain zero.
 - branch range remains 12.500..16.914.
 - soundness gate remained all green: rook9 local replay accepts 362880/362880 orders, rook9 has
   0/511 srg99 r=3 spectral false rejects, triangle-split identity holds on all 512 rook9 subsets,
   T(7)=srg(21,10,5,4) r=3 CRS reconstruction/clique recovery succeeds, and Stage-A gates false-reject
   0/5242 real T(7) induced subgraphs.

VERDICT: accepted. These two shards are exact for their owned source-parent slices and can be included
in the final exact 512-shard aggregate/merge. The aggregate remains diagnostic until all shard indexes
0..511 are present. The shallow d11->d12 estimate remains stable around 6.7M and still shows no pruning.

NEXT ACTION: superseded by R116. Keep filling exact d11->d12 shard coverage in bounded batches
(next 40..41 or 40..43), or run the one-command exact `N12` cloud job via `s3_cloud_r3_d12.py`.

---

## R114 -- exact-contributing d11->d12 shards 34..35/512 completed [2026-06-30]
## OUTCOME: two more proof-grade shard stats/frontiers were added for the eventual exact `N12`
aggregate. Known d11->d12 shard coverage is now 39/512 shards.

COMMANDS RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --indices 34-35 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --tag r3_d11_to_d12_shard512_exact_r114 --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --aggregate-out scratchpad\r3_d11_to_d12_shard512_034_035_exact_aggregate_r114.json --allow-incomplete`

 - then aggregated the known exact-contributing shard set into:
   `scratchpad\r3_d11_to_d12_shard512_known39_aggregate_r114.json`.
 - reran the harness soundness gate:
   `python s3_slice_harness.py --gate`.

RESULTS:
 - shard 34/512: 906 depth-11 parents -> 14660 depth-12 children, branching 16.181.
 - shard 35/512: 906 depth-11 parents -> 13666 depth-12 children, branching 15.084.
 - both frontier files were physically recounted and match their JSON stats/header counts exactly:
   14660 and 13666 rows.
 - batch aggregate `scratchpad\r3_d11_to_d12_shard512_034_035_exact_aggregate_r114.json`:
   1812 depth-11 parents -> 28326 depth-12 children, diagnostic scaled `N12 ~ 7247767`.
 - combined known-shard aggregate over shards 0..35 plus 128,256,384:
   `scratchpad\r3_d11_to_d12_shard512_known39_aggregate_r114.json`
   covers 35333/463636 parents = 7.6208%, with 513985 depth-12 children.
 - combined known-shard diagnostic scaled estimate: `N12 ~ 6744458`.
 - no budget/time/sample flags; prune counters remain zero.
 - branch range remains 12.500..16.914.
 - soundness gate remained all green: rook9 local replay accepts 362880/362880 orders, rook9 has
   0/511 srg99 r=3 spectral false rejects, triangle-split identity holds on all 512 rook9 subsets,
   T(7)=srg(21,10,5,4) r=3 CRS reconstruction/clique recovery succeeds, and Stage-A gates false-reject
   0/5242 real T(7) induced subgraphs.

VERDICT: accepted. These two shards are exact for their owned source-parent slices and can be included
in the final exact 512-shard aggregate/merge. The aggregate remains diagnostic until all shard indexes
0..511 are present. The shallow d11->d12 estimate remains stable around 6.7M and still shows no pruning.

NEXT ACTION: superseded by R115. Keep filling exact d11->d12 shard coverage in bounded batches
(next 38..39 or 38..41), or run the one-command exact `N12` cloud job via `s3_cloud_r3_d12.py`.

---

## R113 -- exact-contributing d11->d12 shards 32..33/512 completed [2026-06-30]
## OUTCOME: two more proof-grade shard stats/frontiers were added for the eventual exact `N12`
aggregate. Known d11->d12 shard coverage is now 37/512 shards.

COMMANDS RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --indices 32-33 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --tag r3_d11_to_d12_shard512_exact_r113 --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --aggregate-out scratchpad\r3_d11_to_d12_shard512_032_033_exact_aggregate_r113.json --allow-incomplete`

 - then aggregated the known exact-contributing shard set into:
   `scratchpad\r3_d11_to_d12_shard512_known37_aggregate_r113.json`.
 - reran the harness soundness gate:
   `python s3_slice_harness.py --gate`.

RESULTS:
 - shard 32/512: 906 depth-11 parents -> 13625 depth-12 children, branching 15.039.
 - shard 33/512: 906 depth-11 parents -> 13963 depth-12 children, branching 15.412.
 - both frontier files were physically recounted and match their JSON stats/header counts exactly:
   13625 and 13963 rows.
 - batch aggregate `scratchpad\r3_d11_to_d12_shard512_032_033_exact_aggregate_r113.json`:
   1812 depth-11 parents -> 27588 depth-12 children, diagnostic scaled `N12 ~ 7058935`.
 - combined known-shard aggregate over shards 0..33 plus 128,256,384:
   `scratchpad\r3_d11_to_d12_shard512_known37_aggregate_r113.json`
   covers 33521/463636 parents = 7.2300%, with 485659 depth-12 children.
 - combined known-shard diagnostic scaled estimate: `N12 ~ 6717252`.
 - no budget/time/sample flags; prune counters remain zero.
 - branch range remains 12.500..16.914.
 - soundness gate remained all green: rook9 local replay accepts 362880/362880 orders, rook9 has
   0/511 srg99 r=3 spectral false rejects, triangle-split identity holds on all 512 rook9 subsets,
   T(7)=srg(21,10,5,4) r=3 CRS reconstruction/clique recovery succeeds, and Stage-A gates false-reject
   0/5242 real T(7) induced subgraphs.

VERDICT: accepted. These two shards are exact for their owned source-parent slices and can be included
in the final exact 512-shard aggregate/merge. The aggregate remains diagnostic until all shard indexes
0..511 are present. The shallow d11->d12 estimate remains stable around 6.7M and still shows no pruning.

NEXT ACTION: superseded by R114. Keep filling exact d11->d12 shard coverage in bounded batches
(next 36..37 or 36..39), or run the one-command exact `N12` cloud job via `s3_cloud_r3_d12.py`.

---

## R112 -- exact-contributing d11->d12 shards 30..31/512 completed [2026-06-30]
## OUTCOME: two more proof-grade shard stats/frontiers were added for the eventual exact `N12`
aggregate. Known d11->d12 shard coverage is now 35/512 shards.

COMMANDS RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --indices 30-31 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --tag r3_d11_to_d12_shard512_exact_r112 --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --aggregate-out scratchpad\r3_d11_to_d12_shard512_030_031_exact_aggregate_r112.json --allow-incomplete`

 - then aggregated the known exact-contributing shard set into:
   `scratchpad\r3_d11_to_d12_shard512_known35_aggregate_r112.json`.
 - reran the harness soundness gate:
   `python s3_slice_harness.py --gate`.

RESULTS:
 - shard 30/512: 906 depth-11 parents -> 13908 depth-12 children, branching 15.351.
 - shard 31/512: 906 depth-11 parents -> 12461 depth-12 children, branching 13.754.
 - both frontier files were physically recounted and match their JSON stats/header counts exactly:
   13908 and 12461 rows.
 - batch aggregate `scratchpad\r3_d11_to_d12_shard512_030_031_exact_aggregate_r112.json`:
   1812 depth-11 parents -> 26369 depth-12 children, diagnostic scaled `N12 ~ 6747030`.
 - combined known-shard aggregate over shards 0..31 plus 128,256,384:
   `scratchpad\r3_d11_to_d12_shard512_known35_aggregate_r112.json`
   covers 31709/463636 parents = 6.8392%, with 458071 depth-12 children.
 - combined known-shard diagnostic scaled estimate: `N12 ~ 6697726`.
 - no budget/time/sample flags; prune counters remain zero.
 - branch range remains 12.500..16.914.
 - soundness gate remained all green: rook9 local replay accepts 362880/362880 orders, rook9 has
   0/511 srg99 r=3 spectral false rejects, triangle-split identity holds on all 512 rook9 subsets,
   T(7)=srg(21,10,5,4) r=3 CRS reconstruction/clique recovery succeeds, and Stage-A gates false-reject
   0/5242 real T(7) induced subgraphs.

VERDICT: accepted. These two shards are exact for their owned source-parent slices and can be included
in the final exact 512-shard aggregate/merge. The aggregate remains diagnostic until all shard indexes
0..511 are present. The shallow d11->d12 estimate remains stable around 6.7M and still shows no pruning.

NEXT ACTION: superseded by R113. Keep filling exact d11->d12 shard coverage in bounded batches
(next 34..35 or 34..37), or run the one-command exact `N12` cloud job via `s3_cloud_r3_d12.py`.

---

## R111 -- exact-contributing d11->d12 shards 28..29/512 completed [2026-06-30]
## OUTCOME: two more proof-grade shard stats/frontiers were added for the eventual exact `N12`
aggregate. Known d11->d12 shard coverage is now 33/512 shards.

COMMANDS RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --indices 28-29 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --tag r3_d11_to_d12_shard512_exact_r111 --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --aggregate-out scratchpad\r3_d11_to_d12_shard512_028_029_exact_aggregate_r111.json --allow-incomplete`

 - then aggregated the known exact-contributing shard set into:
   `scratchpad\r3_d11_to_d12_shard512_known33_aggregate_r111.json`.
 - reran the harness soundness gate:
   `python s3_slice_harness.py --gate`.

RESULTS:
 - shard 28/512: 906 depth-11 parents -> 13486 depth-12 children, branching 14.885.
 - shard 29/512: 906 depth-11 parents -> 12229 depth-12 children, branching 13.498.
 - both frontier files were physically recounted and match their JSON stats/header counts exactly:
   13486 and 12229 rows.
 - batch aggregate `scratchpad\r3_d11_to_d12_shard512_028_029_exact_aggregate_r111.json`:
   1812 depth-11 parents -> 25715 depth-12 children, diagnostic scaled `N12 ~ 6579691`.
 - combined known-shard aggregate over shards 0..29 plus 128,256,384:
   `scratchpad\r3_d11_to_d12_shard512_known33_aggregate_r111.json`
   covers 29897/463636 parents = 6.4484%, with 431702 depth-12 children.
 - combined known-shard diagnostic scaled estimate: `N12 ~ 6694738`.
 - no budget/time/sample flags; prune counters remain zero.
 - branch range remains 12.500..16.914.
 - soundness gate remained all green: rook9 local replay accepts 362880/362880 orders, rook9 has
   0/511 srg99 r=3 spectral false rejects, triangle-split identity holds on all 512 rook9 subsets,
   T(7)=srg(21,10,5,4) r=3 CRS reconstruction/clique recovery succeeds, and Stage-A gates false-reject
   0/5242 real T(7) induced subgraphs.

VERDICT: accepted. These two shards are exact for their owned source-parent slices and can be included
in the final exact 512-shard aggregate/merge. The aggregate remains diagnostic until all shard indexes
0..511 are present. The shallow d11->d12 estimate remains stable around 6.7M and still shows no pruning.

NEXT ACTION: superseded by R112. Keep filling exact d11->d12 shard coverage in bounded batches
(next 32..33 or 32..35), or run the one-command exact `N12` cloud job via `s3_cloud_r3_d12.py`.

---

## R110 -- exact-contributing d11->d12 shards 26..27/512 completed [2026-06-30]
## OUTCOME: two more proof-grade shard stats/frontiers were added for the eventual exact `N12`
aggregate. Known d11->d12 shard coverage is now 31/512 shards.

COMMANDS RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --indices 26-27 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --tag r3_d11_to_d12_shard512_exact_r110 --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --aggregate-out scratchpad\r3_d11_to_d12_shard512_026_027_exact_aggregate_r110.json --allow-incomplete`

 - then aggregated the known exact-contributing shard set into:
   `scratchpad\r3_d11_to_d12_shard512_known31_aggregate_r110.json`.
 - reran the harness soundness gate:
   `python s3_slice_harness.py --gate`.

RESULTS:
 - shard 26/512: 906 depth-11 parents -> 13886 depth-12 children, branching 15.327.
 - shard 27/512: 906 depth-11 parents -> 13287 depth-12 children, branching 14.666.
 - both frontier files were physically recounted and match their JSON stats/header counts exactly:
   13886 and 13287 rows.
 - batch aggregate `scratchpad\r3_d11_to_d12_shard512_026_027_exact_aggregate_r110.json`:
   1812 depth-11 parents -> 27173 depth-12 children, diagnostic scaled `N12 ~ 6952749`.
 - combined known-shard aggregate over shards 0..27 plus 128,256,384:
   `scratchpad\r3_d11_to_d12_shard512_known31_aggregate_r110.json`
   covers 28085/463636 parents = 6.0576%, with 405987 depth-12 children.
 - combined known-shard diagnostic scaled estimate: `N12 ~ 6702161`.
 - no budget/time/sample flags; prune counters remain zero.
 - branch range remains 12.500..16.914.
 - soundness gate remained all green: rook9 local replay accepts 362880/362880 orders, rook9 has
   0/511 srg99 r=3 spectral false rejects, triangle-split identity holds on all 512 rook9 subsets,
   T(7)=srg(21,10,5,4) r=3 CRS reconstruction/clique recovery succeeds, and Stage-A gates false-reject
   0/5242 real T(7) induced subgraphs.

VERDICT: accepted. These two shards are exact for their owned source-parent slices and can be included
in the final exact 512-shard aggregate/merge. The aggregate remains diagnostic until all shard indexes
0..511 are present. Still no evidence of shallow pruning by depth 12; the decisive measurement remains
whether deep spectral gates bite much later.

NEXT ACTION: superseded by R111. Keep filling exact d11->d12 shard coverage in bounded batches
(next 30..31 or 30..33), or run the one-command exact `N12` cloud job via `s3_cloud_r3_d12.py`.

---

## R109 -- exact-contributing d11->d12 shards 24..25/512 completed; order-six route de-duplicated [2026-06-30]
## OUTCOME: two more proof-grade shard stats/frontiers were added for the eventual exact `N12`
aggregate. Known d11->d12 shard coverage is now 29/512 shards.

GROUND-TRUTH CORRECTION:
 - R108 suggested extracting Reimbayev/Filmus order-six formulas as a next local lever. Reading the
   existing ledger showed this route was already substantially closed in R15/R24/R30: the `p6=209286+n3`
   identity was verified on rook9 and BvLS243, Makhnev's `n3=0` conditional was recovered and verified,
   `n3>=3` was proved for any srg99, and order-six counting still leaves `n3` free modulo 3. Do not
   re-run an order-six census unless a new independent handle on `n3` or a completion-capacity bound is found.

COMMANDS RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --indices 24-25 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --tag r3_d11_to_d12_shard512_exact_r109 --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --aggregate-out scratchpad\r3_d11_to_d12_shard512_024_025_exact_aggregate_r109.json --allow-incomplete`

 - then aggregated the known exact-contributing shard set into:
   `scratchpad\r3_d11_to_d12_shard512_known29_aggregate_r109.json`.
 - reran the harness soundness gate:
   `python s3_slice_harness.py --gate`.

RESULTS:
 - shard 24/512: 906 depth-11 parents -> 13717 depth-12 children, branching 15.140.
 - shard 25/512: 906 depth-11 parents -> 14942 depth-12 children, branching 16.492.
 - batch aggregate `scratchpad\r3_d11_to_d12_shard512_024_025_exact_aggregate_r109.json`:
   1812 depth-11 parents -> 28659 depth-12 children, diagnostic scaled `N12 ~ 7332971`.
 - combined known-shard aggregate over shards 0..25 plus 128,256,384:
   `scratchpad\r3_d11_to_d12_shard512_known29_aggregate_r109.json`
   covers 26273/463636 parents = 5.6667%, with 378814 depth-12 children.
 - combined known-shard diagnostic scaled estimate: `N12 ~ 6684878`.
 - no budget/time/sample flags; prune counters remain zero.
 - branch range remains 12.500..16.914.
 - soundness gate remained all green: rook9 local replay accepts 362880/362880 orders, rook9 has
   0/511 srg99 r=3 spectral false rejects, triangle-split identity holds on all 512 rook9 subsets,
   T(7)=srg(21,10,5,4) r=3 CRS reconstruction/clique recovery succeeds, and Stage-A gates false-reject
   0/5242 real T(7) induced subgraphs.

VERDICT: accepted. These two shards are exact for their owned source-parent slices and can be included
in the final exact 512-shard aggregate/merge. The aggregate remains diagnostic until all shard indexes
0..511 are present. The order-six/n3 census line is documented as closed for now, so the active compute
lever is exact `N12` coverage.

NEXT ACTION: superseded by R110. Keep filling exact d11->d12 shard coverage in bounded batches
(next 28..29 or 28..31), or run the one-command exact `N12` cloud job via `s3_cloud_r3_d12.py`.

---

## R108 -- graphify + SCAMPER breakthrough pass and d12 frontier-strata falsification [2026-06-29]
## OUTCOME: source-backed ideation pass completed; one cheap local experiment was implemented and run.

REQUIRED CORPUS WORK:
 - Read `literature_99graph/graphify-out/GRAPH_REPORT.md` and
   `literature_99graph/notes/current_pipeline_summary.md`.
 - Ran graphify queries against the existing literature graph for r=3 star complements, lambda=1/mu=2
   order-six and hexagon counts, srg85 Euclidean/Gram/lattice methods, SAT/SMS/canonical generation, and
   automorphism/cloud-search restrictions.
 - Opened the relevant manifests and PDF/text sources before relying on graph hits:
   direct 99-graph, lambda/mu geometry, computational, association/lattice, star/spectral manifests;
   Keramatipour SAT README; PDF text probes for Reimbayev order-six/hexagons, Shpectorov-Zhao srg85,
   Keramatipour SAT, Kirchweger-Szeider SMS, Cesarz-Woldar automorphisms, and Peeters p-rank.

SCAMPER OUTPUT:
 - Wrote `SCAMPER_BREAKTHROUGH_R108.md` with 10 concrete candidates. Each candidate records source/graph
   evidence, SCAMPER lens, conjectured lemma or computational test, fastest falsification experiment,
   expected files/scripts, risk, and confidence.

CHEAP EXPERIMENT RUN:
`python s3_frontier_strata.py scratchpad\r3_d11_to_d12_frontiers\r3_d11_to_d12_shard512_exact_r107_020_frontier.jsonl scratchpad\r3_d11_to_d12_frontiers\r3_d11_to_d12_shard512_exact_r107_021_frontier.jsonl scratchpad\r3_d11_to_d12_frontiers\r3_d11_to_d12_shard512_exact_r107_022_frontier.jsonl scratchpad\r3_d11_to_d12_frontiers\r3_d11_to_d12_shard512_exact_r107_023_frontier.jsonl --out scratchpad\r3_d12_frontier_strata_r107.json --top-n 10`

RESULTS:
 - scanned 54095 depth-12 rows from R107 shards 20..23.
 - edge range 8..24, mean 18.384, p99 22.
 - triangle range 0..7, mean 2.420, p99 5.
 - top spectral gate margin: max `lambda2=2.646164`, safely below 3.
 - bottom spectral gate margin: min `lambda_min=-3.361325`, safely above -4.
 - spectral gate violations: 0 top, 0 bottom, 0 any.
 - `python -m py_compile s3_cloud_r3_d12.py s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py s3_frontier_strata.py`
   passed.

VERDICT: accepted. R107 shallow d12 rows do not contain near-spectral-boundary strata worth targeting
as a local shortcut. R109 later checked the proposed order-six/hexagon validation lever against the
existing ledger and found the known `n3` census route already characterized, so the compute lever
remains exact N12 coverage/cloud measurement unless a new independent `n3` handle appears.

NEXT ACTION: superseded by R109. Keep filling exact d11->d12 shards (next 26..27 or 26..29), or run the
cloud exact N12 job.

---

## R107 -- exact-contributing d11->d12 shards 20..23/512 completed [2026-06-29]
## OUTCOME: four more proof-grade shard stats/frontiers were added for the eventual exact `N12`
aggregate. Known d11->d12 shard coverage is now 27/512 shards.

COMMANDS RUN:
 - interrupted first attempt completed shard 20 only; verified and resumed with:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --indices 21-23 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --tag r3_d11_to_d12_shard512_exact_r107 --aggregate-out scratchpad\r3_d11_to_d12_shard512_021_023_exact_aggregate_r107.json --allow-incomplete`
 - then aggregated all four R107 shards into:
   `scratchpad\r3_d11_to_d12_shard512_020_023_exact_aggregate_r107.json`.

RESULTS:
 - shard 20/512: 906 depth-11 parents -> 12556 depth-12 children, branching 13.858.
 - shard 21/512: 906 depth-11 parents -> 13357 depth-12 children, branching 14.743.
 - shard 22/512: 906 depth-11 parents -> 13359 depth-12 children, branching 14.745.
 - shard 23/512: 906 depth-11 parents -> 14823 depth-12 children, branching 16.361.
 - each frontier row count matches stats/header exactly: 12556, 13357, 13359, 14823 graph rows.
 - batch aggregate `scratchpad\r3_d11_to_d12_shard512_020_023_exact_aggregate_r107.json`:
   3624 depth-11 parents -> 54095 depth-12 children, diagnostic scaled `N12 ~ 6920637`.
 - combined known-shard aggregate over shards 0..23 plus 128,256,384:
   `scratchpad\r3_d11_to_d12_shard512_known27_aggregate_r107.json`
   covers 24461/463636 parents = 5.2759%, with 350155 depth-12 children.
 - combined known-shard diagnostic scaled estimate: `N12 ~ 6636869`.
 - no budget/time/sample flags; prune counters remain zero.
 - `python -m py_compile s3_cloud_r3_d12.py s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py s3_frontier_strata.py`
   passed.

VERDICT: accepted. These four shards are exact for their owned source-parent slices and can be included
in the final exact 512-shard aggregate/merge. The aggregate remains diagnostic until all shard indexes
0..511 are present. The observed d11->d12 branch range remains 12.500..16.914.

NEXT ACTION: keep filling exact d11->d12 shard coverage in bounded batches (next 24..27), run the cloud
exact N12 job, or use the R108 source-backed order-six/hexagon lever.

---

## R106 -- exact-contributing d11->d12 shards 16..19/512 completed [2026-06-29]
## OUTCOME: four more proof-grade shard stats/frontiers were added for the eventual exact `N12`
aggregate. Known d11->d12 shard coverage is now 23/512 shards.

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --indices 16-19 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --tag r3_d11_to_d12_shard512_exact_r106 --aggregate-out scratchpad\r3_d11_to_d12_shard512_016_019_exact_aggregate_r106.json --allow-incomplete`

RESULTS:
 - shard 16/512: 906 depth-11 parents -> 12510 depth-12 children, branching 13.808.
 - shard 17/512: 906 depth-11 parents -> 13507 depth-12 children, branching 14.908.
 - shard 18/512: 906 depth-11 parents -> 15324 depth-12 children, branching 16.914.
 - shard 19/512: 906 depth-11 parents -> 13615 depth-12 children, branching 15.028.
 - each frontier row count matches stats/header exactly: 12510, 13507, 15324, 13615 graph rows.
 - batch aggregate `scratchpad\r3_d11_to_d12_shard512_016_019_exact_aggregate_r106.json`:
   3624 depth-11 parents -> 54956 depth-12 children, diagnostic scaled `N12 ~ 7030789`.
 - combined known-shard aggregate over shards 0..19 plus 128,256,384:
   `scratchpad\r3_d11_to_d12_shard512_known23_aggregate_r106.json`
   covers 20837/463636 parents = 4.4943%, with 296060 depth-12 children.
 - combined known-shard diagnostic scaled estimate: `N12 ~ 6587516`.
 - no budget/time/sample flags; prune counters remain zero.
 - `python -m py_compile s3_cloud_r3_d12.py s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. These four shards are exact for their owned source-parent slices and can be included
in the final exact 512-shard aggregate/merge. The aggregate remains diagnostic until all shard indexes
0..511 are present. Shard 18 raises the observed d11->d12 branch max to 16.914.

NEXT ACTION: keep filling exact d11->d12 shard coverage in bounded batches (next 20..23), or run the
same work on cloud with `s3_cloud_r3_d12.py`.

---

## R105 -- exact-contributing d11->d12 shards 12..15/512 completed [2026-06-29]
## OUTCOME: four more proof-grade shard stats/frontiers were added for the eventual exact `N12`
aggregate. Known d11->d12 shard coverage is now 19/512 shards.

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --indices 12-15 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --tag r3_d11_to_d12_shard512_exact_r105 --aggregate-out scratchpad\r3_d11_to_d12_shard512_012_015_exact_aggregate_r105.json --allow-incomplete`

RESULTS:
 - shard 12/512: 906 depth-11 parents -> 12285 depth-12 children, branching 13.560.
 - shard 13/512: 906 depth-11 parents -> 12393 depth-12 children, branching 13.679.
 - shard 14/512: 906 depth-11 parents -> 13009 depth-12 children, branching 14.359.
 - shard 15/512: 906 depth-11 parents -> 12545 depth-12 children, branching 13.847.
 - each frontier row count matches stats/header exactly: 12285, 12393, 13009, 12545 graph rows.
 - batch aggregate `scratchpad\r3_d11_to_d12_shard512_012_015_exact_aggregate_r105.json`:
   3624 depth-11 parents -> 50232 depth-12 children, diagnostic scaled `N12 ~ 6426425`.
 - combined known-shard aggregate over shards 0..15 plus 128,256,384:
   `scratchpad\r3_d11_to_d12_shard512_known19_aggregate_r105.json`
   covers 17213/463636 parents = 3.7126%, with 241104 depth-12 children.
 - combined known-shard diagnostic scaled estimate: `N12 ~ 6494190`.
 - no budget/time/sample flags; prune counters remain zero.
 - `python -m py_compile s3_cloud_r3_d12.py s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. These four shards are exact for their owned source-parent slices and can be included
in the final exact 512-shard aggregate/merge. The aggregate remains diagnostic until all shard indexes
0..511 are present.

NEXT ACTION: keep filling exact d11->d12 shard coverage in bounded batches (next 16..19), or run the
same work on cloud with `s3_cloud_r3_d12.py`.

---

## R104 -- exact-contributing d11->d12 shards 8..11/512 completed [2026-06-29]
## OUTCOME: four more proof-grade shard stats/frontiers were added for the eventual exact `N12`
aggregate. Known d11->d12 shard coverage is now 15/512 shards.

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --indices 8-11 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --tag r3_d11_to_d12_shard512_exact_r104 --aggregate-out scratchpad\r3_d11_to_d12_shard512_008_011_exact_aggregate_r104.json --allow-incomplete`

RESULTS:
 - shard 8/512: 906 depth-11 parents -> 13142 depth-12 children, branching 14.506.
 - shard 9/512: 906 depth-11 parents -> 13017 depth-12 children, branching 14.368.
 - shard 10/512: 906 depth-11 parents -> 12116 depth-12 children, branching 13.373.
 - shard 11/512: 906 depth-11 parents -> 13222 depth-12 children, branching 14.594.
 - each frontier row count matches stats/header exactly: 13142, 13017, 12116, 13222 graph rows.
 - batch aggregate `scratchpad\r3_d11_to_d12_shard512_008_011_exact_aggregate_r104.json`:
   3624 depth-11 parents -> 51497 depth-12 children, diagnostic scaled `N12 ~ 6588262`.
 - combined known-shard aggregate over shards 0..11 plus 128,256,384:
   `scratchpad\r3_d11_to_d12_shard512_known15_aggregate_r104.json`
   covers 13589/463636 parents = 2.9310%, with 190872 depth-12 children.
 - combined known-shard diagnostic scaled estimate: `N12 ~ 6512262`.
 - no budget/time/sample flags; prune counters remain zero.
 - `python -m py_compile s3_cloud_r3_d12.py s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. These four shards are exact for their owned source-parent slices and can be included
in the final exact 512-shard aggregate/merge. The aggregate remains diagnostic until all shard indexes
0..511 are present.

NEXT ACTION: keep filling exact d11->d12 shard coverage in bounded batches (next 12..15), or run the
same work on cloud with `s3_cloud_r3_d12.py`.

---

## R103 -- exact-contributing d11->d12 shards 4..7/512 completed [2026-06-29]
## OUTCOME: four more proof-grade shard stats/frontiers were added for the eventual exact `N12`
aggregate. Known d11->d12 shard coverage is now 11/512 shards.

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --indices 4-7 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --tag r3_d11_to_d12_shard512_exact_r103 --aggregate-out scratchpad\r3_d11_to_d12_shard512_004_007_exact_aggregate_r103.json --allow-incomplete`

RESULTS:
 - shard 4/512: 906 depth-11 parents -> 14042 depth-12 children, branching 15.499.
 - shard 5/512: 906 depth-11 parents -> 13225 depth-12 children, branching 14.597.
 - shard 6/512: 906 depth-11 parents -> 11951 depth-12 children, branching 13.191.
 - shard 7/512: 906 depth-11 parents -> 12497 depth-12 children, branching 13.794.
 - each frontier row count matches stats/header exactly: 14042, 13225, 11951, 12497 graph rows.
 - batch aggregate `scratchpad\r3_d11_to_d12_shard512_004_007_exact_aggregate_r103.json`:
   3624 depth-11 parents -> 51715 depth-12 children, diagnostic scaled `N12 ~ 6616152`.
 - combined known-shard aggregate over shards 0,1,2,3,4,5,6,7,128,256,384:
   `scratchpad\r3_d11_to_d12_shard512_known11_aggregate_r103.json`
   covers 9965/463636 parents = 2.1493%, with 139375 depth-12 children.
 - combined known-shard diagnostic scaled estimate: `N12 ~ 6484623`.
 - no budget/time/sample flags; prune counters remain zero.
 - `python -m py_compile s3_cloud_r3_d12.py s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. These four shards are not merely sizing probes; their stats/frontiers are compatible
with the R90 d11 source frontier and can be included in the final exact 512-shard aggregate/merge. The
aggregate is still diagnostic until all 512 shard indexes are present.

NEXT ACTION: keep filling exact d11->d12 shard coverage in bounded batches (next 8..11), or run the
same work on cloud with `s3_cloud_r3_d12.py`.

---

## R102 -- bounded vertical diagnostic: d12->d13 from shard-256 frontier [2026-06-29]
## OUTCOME: third deeper local continuation measured. The d12->d13 diagnostic branch range is now
21.594..23.186 across three different d12 source regions, still with zero pruning.

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_d11_to_d12_frontiers\r3_d11_to_d12_shard512_strat_r97_256_frontier.jsonl --shard-count 64 --indices 0 --target-depth 13 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d12_to_d13_frontiers --tag r3_d12_to_d13_subshard64_strat_r102 --aggregate-out scratchpad\r3_d12_to_d13_subshard64_256_000_aggregate_r102.json --allow-incomplete`

RESULTS:
 - source frontier is `scratchpad\r3_d11_to_d12_frontiers\r3_d11_to_d12_shard512_strat_r97_256_frontier.jsonl`,
   which is complete only for d11 shard 256, not globally complete (`source_frontier_complete=false`).
 - loaded 189/12061 depth-12 parents from that d12 shard frontier (subshard 0/64).
 - produced 4235 depth-13 children, branching 22.407.
 - frontier row count matches stats/header: 4235 graph rows.
 - output frontier is correctly labelled `frontier_complete=false`,
   `frontier_complete_for_loaded_scope=true`.
 - aggregate `scratchpad\r3_d12_to_d13_subshard64_256_000_aggregate_r102.json` is diagnostic:
   coverage 189/12061 local d12 parents = 1.5670%, scaled local-shard estimate `N13 ~ 270256`
   for the R97 shard-256 d12 frontier only.
 - no budget/time/sample flags; prune counters remain zero.
 - `python -m py_compile s3_cloud_r3_d12.py s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted as a bounded vertical diagnostic only. Combined with R99/R100, this strengthens
the evidence that shallow d13 branching is high and that current predicates still do not bite before
the intended deeper spectral-gate range.

NEXT ACTION: run exact `N12` on cloud and merge a complete d12 frontier before making any global d13
claim.

---

## R101 -- readiness verdict captured [2026-06-29]
## OUTCOME: wrote `READINESS_R100.md`, an honest measured verdict for the current r=3 harness state.

RESULTS:
 - Verdict: ready for exact `N12` cloud measurement from `scratchpad\r3_frontier_d11_r90.jsonl`.
 - Not ready for an existence/nonexistence claim, a global `N13` estimate, or a full depth-45
   feasibility claim from shallow extrapolation.
 - Evidence summarized: green gate, exact `N10=42430`, exact `N11=463636`, complete d11 frontier
   SHA `ce3f25d95d2c102eb00d53b23fcd38a449758b55392e51cf0804104db03cfb7b`, seven d12 diagnostic
   shards estimating `N12 ~ 6.409e6`, three d13 local diagnostics with branch 21.6-23.2, and zero
   pruning throughout these shallow continuations.
 - Next best move in the note: run exact `N12` on cloud, then measure d13 from a complete d12 frontier.

VERDICT: accepted as a documentation/control artifact. This is not a mathematical result by itself;
it records the current proof boundary and the next reproducible experiment.

NEXT ACTION: run exact `N12` on cloud, or continue bounded local diagnostics only if they produce
new cost/variance information without pretending to be global counts.

---

## R100 -- bounded vertical diagnostic: d12->d13 from shard-384 frontier [2026-06-29]
## OUTCOME: second deeper local continuation measured from a different d12 source region. It also
shows high d12->d13 branching and zero pruning.

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_d11_to_d12_frontiers\r3_d11_to_d12_shard512_strat_r98_384_frontier.jsonl --shard-count 64 --indices 0 --target-depth 13 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d12_to_d13_frontiers --tag r3_d12_to_d13_subshard64_strat_r100 --aggregate-out scratchpad\r3_d12_to_d13_subshard64_384_000_aggregate_r100.json --allow-incomplete`

RESULTS:
 - source frontier is `scratchpad\r3_d11_to_d12_frontiers\r3_d11_to_d12_shard512_strat_r98_384_frontier.jsonl`,
   which is complete only for d11 shard 384, not globally complete (`source_frontier_complete=false`).
 - loaded 219/13987 depth-12 parents from that d12 shard frontier (subshard 0/64).
 - produced 4729 depth-13 children, branching 21.594.
 - frontier row count matches stats/header: 4729 graph rows.
 - output frontier is correctly labelled `frontier_complete=false`,
   `frontier_complete_for_loaded_scope=true`.
 - aggregate `scratchpad\r3_d12_to_d13_subshard64_384_000_aggregate_r100.json` is diagnostic:
   coverage 219/13987 local d12 parents = 1.5657%, scaled local-shard estimate `N13 ~ 302030`
   for the R98 shard-384 d12 frontier only.
 - no budget/time/sample flags; prune counters remain zero.
 - `python -m py_compile s3_cloud_r3_d12.py s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted as a bounded vertical diagnostic only. The second d12 source region agrees that
early d13 branching is high (21.6-23.2 in these two local probes) and current predicates still do not
prune. This increases the value of exact d12 cloud execution before trying to reason from d13 samples.

NEXT ACTION: prioritize exact `N12`/complete d12 frontier on cloud, or run one more d13 diagnostic
from a lower-branch d12 source to estimate vertical variance.

---

## R99 -- bounded vertical diagnostic: d12->d13 subshard measured [2026-06-29]
## OUTCOME: first deeper local continuation from a completed d12 shard measured. In this local
region, d12->d13 branching jumps to 23.186, and the pruning counters still remain zero.

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_d11_to_d12_frontiers\r3_d11_to_d12_shard512_probe_r91_000_frontier.jsonl --shard-count 64 --indices 0 --target-depth 13 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d12_to_d13_frontiers --tag r3_d12_to_d13_subshard64_probe_r99 --aggregate-out scratchpad\r3_d12_to_d13_subshard64_000_probe_aggregate_r99.json --allow-incomplete`

RESULTS:
 - source frontier is `scratchpad\r3_d11_to_d12_frontiers\r3_d11_to_d12_shard512_probe_r91_000_frontier.jsonl`,
   which is complete only for d11 shard 0, not globally complete (`source_frontier_complete=false`).
 - loaded 177/11325 depth-12 parents from that d12 shard frontier (subshard 0/64).
 - produced 4104 depth-13 children, branching 23.186.
 - frontier row count matches stats/header: 4104 graph rows.
 - output frontier is correctly labelled `frontier_complete=false`,
   `frontier_complete_for_loaded_scope=true`.
 - aggregate `scratchpad\r3_d12_to_d13_subshard64_000_probe_aggregate_r99.json` is diagnostic:
   coverage 177/11325 local d12 parents = 1.5629%, scaled local-shard estimate `N13 ~ 262586`
   for the R91 shard-0 d12 frontier only.
 - no budget/time/sample flags; prune counters remain zero.
 - `python -m py_compile s3_cloud_r3_d12.py s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted as a bounded vertical diagnostic only. It is not a global d13 estimate and not a
proof count. The useful signal is that shallow branching can increase sharply at d13 and the current
local/spectral/triangle predicates still have not begun pruning in this region.

NEXT ACTION: either run more d12->d13 subshards from distinct d12 source shards to estimate early
d13 variance, or prioritize the exact d12 cloud job so a complete d12 frontier exists.

---

## R98 -- stratified d11->d12 probe: shard 384/512 measured [2026-06-29]
## OUTCOME: four-quadrant stratified d11->d12 probe completed. The seven measured shards now give
diagnostic `N12 ~ 6.409e6`, with visible branch variance but still no pruning signal.

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --indices 384 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --tag r3_d11_to_d12_shard512_strat_r98 --aggregate-out scratchpad\r3_d11_to_d12_shard512_384_strat_aggregate_r98.json --allow-incomplete`

RESULTS:
 - shard 384/512 loaded 905 depth-11 parents and produced 13987 depth-12 children, branching 15.455.
 - frontier row count matches stats/header: 13987 graph rows.
 - stratified aggregate over shards 0,1,2,3,128,256,384:
   `python s3_aggregate_shards.py scratchpad\r3_d11_to_d12_shard512_probe_r91_000.json scratchpad\r3_d11_to_d12_shard512_probe_r92_001.json scratchpad\r3_d11_to_d12_shard512_probe_r93_002.json scratchpad\r3_d11_to_d12_shard512_probe_r94_003.json scratchpad\r3_d11_to_d12_shard512_strat_r96_128.json scratchpad\r3_d11_to_d12_shard512_strat_r97_256.json scratchpad\r3_d11_to_d12_shard512_strat_r98_384.json --allow-incomplete --out scratchpad\r3_d11_to_d12_shard512_strat_000_003_128_256_384_aggregate_r98.json`
 - combined coverage: 6341/463636 parents = 1.3676%.
 - combined depth-12 children: 87660, weighted branching 13.824.
 - diagnostic scaled estimate `N12 ~ 6409452`.
 - no budget/time/sample flags; prune counters remain zero.
 - `python -m py_compile s3_cloud_r3_d12.py s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. This is still diagnostic, not exact. The branch range across measured shards is
now 12.500..15.455; exact `N12` plausibly sits in the low-to-mid 6 million range, but the proof-grade
answer requires all 512 shards.

NEXT ACTION: either launch the exact d11->d12 cloud job using `s3_cloud_r3_d12.py`, or move to a
deeper bounded vertical slice from one completed d12 shard to learn when/if spectral gates begin
to bite.

---

## R97 -- stratified d11->d12 probe: shard 256/512 measured [2026-06-29]
## OUTCOME: second spaced shard measured. The six-shard stratified diagnostic estimate remains
stable near `N12 ~ 6.28e6`.

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --indices 256 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --tag r3_d11_to_d12_shard512_strat_r97 --aggregate-out scratchpad\r3_d11_to_d12_shard512_256_strat_aggregate_r97.json --allow-incomplete`

RESULTS:
 - shard 256/512 loaded 906 depth-11 parents and produced 12061 depth-12 children, branching 13.312.
 - frontier row count matches stats/header: 12061 graph rows.
 - stratified aggregate over shards 0,1,2,3,128,256:
   `python s3_aggregate_shards.py scratchpad\r3_d11_to_d12_shard512_probe_r91_000.json scratchpad\r3_d11_to_d12_shard512_probe_r92_001.json scratchpad\r3_d11_to_d12_shard512_probe_r93_002.json scratchpad\r3_d11_to_d12_shard512_probe_r94_003.json scratchpad\r3_d11_to_d12_shard512_strat_r96_128.json scratchpad\r3_d11_to_d12_shard512_strat_r97_256.json --allow-incomplete --out scratchpad\r3_d11_to_d12_shard512_strat_000_003_128_256_aggregate_r97.json`
 - combined coverage: 5436/463636 parents = 1.1724%.
 - combined depth-12 children: 73673, weighted branching 13.553.
 - diagnostic scaled estimate `N12 ~ 6283564`.
 - no budget/time/sample flags; prune counters remain zero.
 - `python -m py_compile s3_cloud_r3_d12.py s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. This remains diagnostic, not exact. The sampled d11->d12 branch range so far is
12.500 to 15.113, and a 1.17% stratified parent sample points to exact `N12` around 6.3 million.

NEXT ACTION: measure one more spaced shard (384) for a four-quadrant sample, or run the exact
d11->d12 cloud job from `s3_cloud_r3_d12.py`.

---

## R96 -- stratified d11->d12 probe: shard 128/512 measured [2026-06-29]
## OUTCOME: moved from adjacent-only probing to a spaced shard sample. Shard 128 gives an independent
frontier-region measurement and keeps the diagnostic `N12` estimate near 6.3e6.

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --indices 128 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --tag r3_d11_to_d12_shard512_strat_r96 --aggregate-out scratchpad\r3_d11_to_d12_shard512_128_strat_aggregate_r96.json --allow-incomplete`

RESULTS:
 - shard 128/512 loaded 906 depth-11 parents and produced 12640 depth-12 children, branching 13.951.
 - frontier row count matches stats/header: 12640 graph rows.
 - stratified aggregate over shards 0,1,2,3,128:
   `python s3_aggregate_shards.py scratchpad\r3_d11_to_d12_shard512_probe_r91_000.json scratchpad\r3_d11_to_d12_shard512_probe_r92_001.json scratchpad\r3_d11_to_d12_shard512_probe_r93_002.json scratchpad\r3_d11_to_d12_shard512_probe_r94_003.json scratchpad\r3_d11_to_d12_shard512_strat_r96_128.json --allow-incomplete --out scratchpad\r3_d11_to_d12_shard512_strat_000_003_128_aggregate_r96.json`
 - combined coverage: 4530/463636 parents = 0.9770%.
 - combined depth-12 children: 61612, weighted branching 13.601.
 - diagnostic scaled estimate `N12 ~ 6305859`.
 - no budget/time/sample flags; prune counters remain zero.
 - `python -m py_compile s3_cloud_r3_d12.py s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. This is diagnostic, not exact. The useful new information is that a non-adjacent
frontier shard behaves similarly to the adjacent 0..3 window; the exact 512-shard job remains the
only proof-grade `N12` count.

NEXT ACTION: measure additional spaced shards (e.g. 256 and 384) to improve variance estimates, or
run the exact d11->d12 cloud job from `s3_cloud_r3_d12.py`.

---

## R95 -- exact d11->d12 cloud measurement is one-command runnable [2026-06-29]
## OUTCOME: added `s3_cloud_r3_d12.py`, a cross-platform wrapper for the current preferred exact
`N12` cloud run from the complete R90 depth-11 frontier.

WHAT CHANGED:
 - `s3_cloud_r3_d12.py` auto-detects `scratchpad\r3_frontier_d11_r90.jsonl` or accepts
   `--frontier-in r3_frontier_d11_r90.jsonl`.
 - Default command runs `s3_slice_harness.py --gate`, then launches all 512 d11->d12 shards via
   `s3_run_shards.py` with strict aggregation (no `--allow-incomplete`).
 - `--worker-count/--worker-index` partitions the 512 shards into balanced contiguous ranges for
   distributed cloud workers; those partial worker aggregates automatically pass `--allow-incomplete`
   and remain diagnostic until all raw shard stats are strictly aggregated.
 - `CLOUD_SPEC_SC.md` now lists the exact one-command launch, the worker pattern, the final strict
   aggregate command, and the complete depth-12 frontier merge command.

VERIFICATION:
 - `python -m py_compile s3_cloud_r3_d12.py s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.
 - exact all-shard dry run expands to:
   `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --target-depth 12 --node-budget 100000 --time-cap 3600.0 --level-cap 100000 --out-dir d11_d12_stats --frontier-out-dir d11_d12_frontiers --tag r3_d11_to_d12_shard512_exact --aggregate-out r3_d11_to_d12_shard512_aggregate.json --start 0 --stop 512`
   with no `--allow-incomplete`.
 - 16-way worker dry run for worker 3 expands to `--start 96 --stop 128 --allow-incomplete`.
 - indices dry run for `0-3` expands with `--indices 0-3 --allow-incomplete`.
 - fresh predicate/CRS gate:
   `python s3_slice_harness.py --gate`
   passed ALL GREEN: rook(9) 362880/362880 vertex-order replay, 0/511 spectral false rejects,
   triangle-split identity on 512 subsets, and exact T(7)=srg(21,10,5,4) r=3 CRS reconstruction.

VERDICT: accepted. This does not solve the 99-graph problem. It does make the next exact cloud
measurement reproducible from a single command and pins the acceptance criteria for exact `N12`.

NEXT ACTION: either run the exact d11->d12 cloud job, or continue local d11->d12 probes while looking
for a mathematically stronger lever before spending cloud time.

---

## R94 -- d11->d12 probe expansion: shards 0..3/512 measured [2026-06-29]
## OUTCOME: fourth deterministic d11->d12 probe completed. Shard 3 is a heavier branch sample,
raising the four-shard diagnostic estimate for `N12` to ~6.265e6.

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --indices 3 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --tag r3_d11_to_d12_shard512_probe_r94 --aggregate-out scratchpad\r3_d11_to_d12_shard512_003_probe_aggregate_r94.json --allow-incomplete`

RESULTS:
 - shard 3/512 loaded 906 depth-11 parents and produced 13692 depth-12 children, branching 15.113.
 - frontier row count matches stats/header: 13692 graph rows.
 - combined probes 0..3:
   `python s3_aggregate_shards.py scratchpad\r3_d11_to_d12_shard512_probe_r91_000.json scratchpad\r3_d11_to_d12_shard512_probe_r92_001.json scratchpad\r3_d11_to_d12_shard512_probe_r93_002.json scratchpad\r3_d11_to_d12_shard512_probe_r94_003.json --allow-incomplete --out scratchpad\r3_d11_to_d12_shard512_000_003_probe_aggregate_r94.json`
 - combined coverage: 3624/463636 parents = 0.7816%.
 - combined depth-12 children: 48972, weighted branching 13.513.
 - diagnostic scaled estimate `N12 ~ 6265227`.
 - no budget/time/sample flags; prune counters remain zero.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. This is still diagnostic, not exact. The new information is variance in
d11->d12 branching across adjacent deterministic shards; exact `N12` needs the 512-shard run.

NEXT ACTION: continue measuring deterministic d11->d12 shards, or launch the full 512-shard exact
`N12` job on cloud using `scratchpad\r3_frontier_d11_r90.jsonl`.

---

## R93 -- d11->d12 probe expansion: shards 0..2/512 measured [2026-06-29]
## OUTCOME: third deterministic d11->d12 probe completed. The three-shard diagnostic estimate for
`N12` is now ~6.018e6, still with zero pruning signal at this shallow depth.

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --indices 2 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --tag r3_d11_to_d12_shard512_probe_r93 --aggregate-out scratchpad\r3_d11_to_d12_shard512_002_probe_aggregate_r93.json --allow-incomplete`

RESULTS:
 - shard 2/512 loaded 906 depth-11 parents and produced 12012 depth-12 children, branching 13.258.
 - frontier row count matches stats/header: 12012 graph rows.
 - combined probes 0..2:
   `python s3_aggregate_shards.py scratchpad\r3_d11_to_d12_shard512_probe_r91_000.json scratchpad\r3_d11_to_d12_shard512_probe_r92_001.json scratchpad\r3_d11_to_d12_shard512_probe_r93_002.json --allow-incomplete --out scratchpad\r3_d11_to_d12_shard512_000_002_probe_aggregate_r93.json`
 - combined coverage: 2718/463636 parents = 0.5862%.
 - combined depth-12 children: 35280, weighted branching 12.980.
 - diagnostic scaled estimate `N12 ~ 6018057`.
 - source frontier SHA-256 remains `ce3f25d95d2c102eb00d53b23fcd38a449758b55392e51cf0804104db03cfb7b`.
 - no budget/time/sample flags; prune counters remain zero.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. This is still diagnostic, not exact; it strengthens the measured cost model for
the exact d12 cloud run and confirms the local/spectral/triangle pruning predicates have not begun
to fire through this slice.

NEXT ACTION: continue measuring deterministic d11->d12 shards, or launch the full 512-shard exact
`N12` job on cloud using `scratchpad\r3_frontier_d11_r90.jsonl`.

---

## R92 -- d11->d12 probe expansion: shards 0..1/512 measured [2026-06-29]
## OUTCOME: second deterministic d11->d12 probe completed. The merged d11 frontier remains usable, and
the two-shard diagnostic estimate for `N12` is now ~5.954e6.

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --indices 1 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --tag r3_d11_to_d12_shard512_probe_r92 --aggregate-out scratchpad\r3_d11_to_d12_shard512_001_probe_aggregate_r92.json --allow-incomplete`

RESULTS:
 - shard 1/512 loaded 906 depth-11 parents and produced 11943 depth-12 children, branching 13.182.
 - frontier row count matches stats/header: 11943 graph rows.
 - combined probes 0..1:
   `python s3_aggregate_shards.py scratchpad\r3_d11_to_d12_shard512_probe_r91_000.json scratchpad\r3_d11_to_d12_shard512_probe_r92_001.json --allow-incomplete --out scratchpad\r3_d11_to_d12_shard512_000_001_probe_aggregate_r92.json`
 - combined coverage: 1812/463636 parents = 0.3908%.
 - combined depth-12 children: 23268, weighted branching 12.841.
 - diagnostic scaled estimate `N12 ~ 5953578`.
 - no budget/time/sample flags; prune counters remain zero.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. This remains diagnostic, not exact. The useful information is that d11->d12
branching is still high and non-pruning at the shallow end.

NEXT ACTION: continue measuring deterministic d11->d12 shards, or launch the full 512-shard exact
`N12` job on cloud using `scratchpad\r3_frontier_d11_r90.jsonl`.

---

## R91 -- merged d11 frontier continuation probe: shard 0/512 reaches depth 12 [2026-06-29]
## OUTCOME: `scratchpad\r3_frontier_d11_r90.jsonl` is not just well-formed; it resumes successfully
as a complete source frontier for d11->d12 work.

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d11_r90.jsonl --shard-count 512 --indices 0 --target-depth 12 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d11_to_d12_frontiers --tag r3_d11_to_d12_shard512_probe_r91 --aggregate-out scratchpad\r3_d11_to_d12_shard512_000_probe_aggregate_r91.json --allow-incomplete`

RESULTS:
 - loaded 906/463636 depth-11 parents from the merged complete frontier, shard 0/512.
 - produced 11325 depth-12 children, branching 12.500.
 - frontier file `scratchpad\r3_d11_to_d12_frontiers\r3_d11_to_d12_shard512_probe_r91_000_frontier.jsonl`
   has 11325 graph rows, matching stats/header.
 - source frontier SHA-256 for `scratchpad\r3_frontier_d11_r90.jsonl`:
   `ce3f25d95d2c102eb00d53b23fcd38a449758b55392e51cf0804104db03cfb7b`.
 - diagnostic scaled estimate from this one shard: `N12 ~ 5795450`; this is not exact.
 - no budget/time/sample flags; prune counters remain zero.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. The exact d11 frontier is chainable, and the first d12 probe suggests shallow
branching remains high. No construction/nonexistence proof and no shallow pruning signal yet.

NEXT ACTION: expand d11->d12 measurement with more deterministic 512-shard probes (or distribute all
512 shards for exact `N12`) and update the cloud spec to use `r3_frontier_d11_r90.jsonl` as the prefix.

---

## R90 -- complete chainable depth-11 frontier merged: `r3_frontier_d11_r90.jsonl` [2026-06-29]
## OUTCOME: the exact depth-11 frontier is now both counted and chainable. All 64 per-shard frontier
JSONLs merged into `scratchpad\r3_frontier_d11_r90.jsonl`.

FINAL BACKFILL COMMAND:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 8-11 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_backfill_r89 --aggregate-out scratchpad\r3_d10_to_d11_shard64_08_11_backfill_aggregate_r89.json --allow-incomplete`

FINAL BACKFILL RESULTS:
 - shard 8: 663 parents -> 7680 children, matching original `r3_d10_to_d11_shard64_runner_r56_008.json`.
 - shard 9: 663 parents -> 7721 children, matching original `r3_d10_to_d11_shard64_runner_r56_009.json`.
 - shard 10: 663 parents -> 6632 children, matching original `r3_d10_to_d11_shard64_runner_r57_010.json`.
 - shard 11: 663 parents -> 7264 children, matching original `r3_d10_to_d11_shard64_runner_r57_011.json`.
 - frontier row counts match headers/stats: 7680, 7721, 6632, 7264 graph rows.

MERGE COMMAND:
`python s3_merge_frontiers.py --glob "scratchpad\r3_d10_to_d11_shard64_backfill_r85_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_backfill_r86_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_backfill_r87_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_backfill_r88_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_backfill_r89_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r71_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r72_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r73_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r74_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r75_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r76_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r77_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r78_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r79_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r80_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r81_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r82_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r83_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r84_*.json" --out scratchpad\r3_frontier_d11_r90.jsonl`

MERGE EVIDENCE:
 - merge accepted 64 frontier-bearing shard stats and wrote `scratchpad\r3_frontier_d11_r90.jsonl`.
 - header says `frontier_complete=true`, `frontier_level=11`, `count_written=463636`,
   `merged_from_shards=[0..63]`, `canonical_parent=true`, `seed_triangle=false`.
 - physical row count check: 463636 graph rows after the header.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. This makes the r=3 d11 frontier a reusable exact prefix for downstream depth-12+
experiments. It does not solve the 99-graph problem, but it materially reduces rerun cost and improves
cloud reproducibility.

NEXT ACTION: validate continuation from `scratchpad\r3_frontier_d11_r90.jsonl` with a small d11->d12
shard, then update the cloud spec with the exact d11 prefix command.

---

## R88 -- depth-11 frontier backfill: shards 0..7 now have frontier rows [2026-06-29]
## OUTCOME: shards 6 and 7 were rerun with `--frontier-out-dir`, exactly reproducing the original
R55 counts while writing chainable depth-11 rows.

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 6-7 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_backfill_r88 --aggregate-out scratchpad\r3_d10_to_d11_shard64_06_07_backfill_aggregate_r88.json --allow-incomplete`

RESULTS:
 - shard 6: 663 parents -> 6745 children, matching original `r3_d10_to_d11_shard64_runner_r55_006.json`.
 - shard 7: 663 parents -> 7881 children, matching original `r3_d10_to_d11_shard64_runner_r55_007.json`.
 - frontier row counts match headers/stats: 6745 and 7881 graph rows.
 - no budget/time/sample flags; prune counters remain zero.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. Backfilled frontier rows now cover shards 0..7; shards 8..11 still need frontier
output before merging a complete depth-11 frontier.

NEXT ACTION: backfill shards 8..11 with frontier output, then merge all 64 shard frontiers.

---

## R87 -- depth-11 frontier backfill: shards 0..5 now have frontier rows [2026-06-29]
## OUTCOME: shards 4 and 5 were rerun with `--frontier-out-dir`, exactly reproducing the original
R54 counts while writing chainable depth-11 rows.

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 4-5 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_backfill_r87 --aggregate-out scratchpad\r3_d10_to_d11_shard64_04_05_backfill_aggregate_r87.json --allow-incomplete`

RESULTS:
 - shard 4: 663 parents -> 7392 children, matching original `r3_d10_to_d11_shard64_runner_r54_004.json`.
 - shard 5: 663 parents -> 7473 children, matching original `r3_d10_to_d11_shard64_runner_r54_005.json`.
 - frontier row counts match headers/stats: 7392 and 7473 graph rows.
 - no budget/time/sample flags; prune counters remain zero.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. Backfilled frontier rows now cover shards 0..5; shards 6..11 still need frontier
output before merging a complete depth-11 frontier.

NEXT ACTION: backfill shards 6..11 with frontier output, then merge all 64 shard frontiers.

---

## R86 -- depth-11 frontier backfill: shards 0..3 now have frontier rows [2026-06-29]
## OUTCOME: shards 2 and 3 were rerun with `--frontier-out-dir`, exactly reproducing the original
R53 counts while writing chainable depth-11 rows.

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 2-3 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_backfill_r86 --aggregate-out scratchpad\r3_d10_to_d11_shard64_02_03_backfill_aggregate_r86.json --allow-incomplete`

RESULTS:
 - shard 2: 663 parents -> 6930 children, matching original `r3_d10_to_d11_shard64_02_stats_r53.json`.
 - shard 3: 663 parents -> 7159 children, matching original `r3_d10_to_d11_shard64_03_stats_r53.json`.
 - frontier row counts match headers/stats: 6930 and 7159 graph rows.
 - no budget/time/sample flags; prune counters remain zero.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. Backfilled frontier rows now cover shards 0..3; shards 4..11 still need frontier
output before merging a complete depth-11 frontier.

NEXT ACTION: backfill shards 4..11 with frontier output, then merge all 64 shard frontiers.

---

## R85 -- depth-11 frontier backfill begins: shards 0..1 now have frontier rows [2026-06-29]
## OUTCOME: chainable frontier backfill started. Shards 0 and 1, previously stats-only from R53,
were rerun with `--frontier-out-dir` and exactly reproduce their original counts while writing rows.

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 0-1 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_backfill_r85 --aggregate-out scratchpad\r3_d10_to_d11_shard64_00_01_backfill_aggregate_r85.json --allow-incomplete`

RESULTS:
 - shard 0: 663 parents -> 7818 children, matching original `r3_d10_to_d11_shard64_00_stats_r53.json`.
 - shard 1: 663 parents -> 7260 children, matching original `r3_d10_to_d11_shard64_01_stats_r53.json`.
 - frontier files wrote and row counts match headers/stats:
   `r3_d10_to_d11_shard64_backfill_r85_000_frontier.jsonl` has 7818 graph rows;
   `r3_d10_to_d11_shard64_backfill_r85_001_frontier.jsonl` has 7260 graph rows.
 - no budget/time/sample flags; prune counters remain zero.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. This strengthens reproducibility and moves toward a complete chainable d11 frontier.

NEXT ACTION: backfill shards 2..11 with frontier output, then merge all 64 shard frontiers.

---

## R84 -- exact d10->d11 shard certification: all 64 shards counted, exact N11=463636 [2026-06-29]
## OUTCOME: exact depth-11 count certified by the strict shard combiner. The r=3 harness now has
complete exact counts through depth 11: `N10=42430`, `N11=463636`.

FINAL PAIR COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 62-63 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r84 --aggregate-out scratchpad\r3_d10_to_d11_shard64_62_63_chain_aggregate_r84.json --allow-incomplete`

FINAL PAIR RESULTS:
 - shard 62: 662 parents -> 6848 children, branching 10.344, wall 53.33s.
 - shard 63: 662 parents -> 6683 children, branching 10.095, wall 52.43s.
 - both shards wrote frontier JSONL files under `scratchpad\r3_d10_to_d11_frontiers\`.
 - actual graph-row counts match header/stat counts: shard 62 has 6848 rows; shard 63 has 6683 rows.

STRICT ALL-SHARD AGGREGATE:
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r71_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r72_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r73_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r74_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r75_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r76_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r77_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r78_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r79_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r80_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r81_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r82_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r83_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r84_*.json" --out scratchpad\r3_d10_to_d11_shard64_00_63_EXACT_aggregate_r84.json`
 - loaded 64 stats files, shard indexes 0..63, `complete_shard_set=true`.
 - exact depth 10 count: 42430, matching `scratchpad\r3_frontier_d10_r52.jsonl`.
 - exact depth 11 count: 463636.
 - exact weighted branching 463636/42430 = 10.927.
 - no budget/time/sample flags; cumulative prune counters remain `pruned_local=0`,
   `pruned_spectral=0`, `pruned_triangle_split=0`.
 - all stats share source frontier SHA-256 `97bebb58e50c1c7a44bdf6d2bca277c5a5f99968b0764975e38855660baa20c3`.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. This is a real exact measurement milestone, not a solution. It proves the r=3
canonical frontier has `N11=463636` under the current validated predicates; it does not construct or
rule out srg(99,14,1,2). No shallow pruning predicate fires by depth 11.

NEXT ACTION: make the depth-11 frontier chainable. Shards 12..63 have frontier JSONL rows, but shards
0..11 were counted before `--frontier-out-dir`; rerun shards 0..11 with frontier output, then run
`s3_merge_frontiers.py` over all 64 shard stats to produce a complete `r3_frontier_d11.jsonl`.

---

## R83 -- d10->d11 shard certification progress: shards 0..61 counted; shards 12..61 preserve frontier rows [2026-06-29]
## OUTCOME: count progress plus more chainable depth-11 frontier material. The counted pilot now
covers 62/64 shards (96.88% of the depth-10 frontier).

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 60-61 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r83 --aggregate-out scratchpad\r3_d10_to_d11_shard64_60_61_chain_aggregate_r83.json --allow-incomplete`

NEW SHARD RESULTS:
 - shard 60: 663 parents -> 7730 children, branching 11.659, wall 54.65s.
 - shard 61: 663 parents -> 7499 children, branching 11.311, wall 54.62s.
 - both shards wrote frontier JSONL files under `scratchpad\r3_d10_to_d11_frontiers\`.
 - actual graph-row counts match header/stat counts: shard 60 has 7730 rows; shard 61 has 7499 rows.

COMBINED PILOT (shards 0..61):
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r71_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r72_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r73_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r74_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r75_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r76_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r77_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r78_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r79_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r80_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r81_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r82_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r83_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_61_aggregate_r83.json`
 - loaded 62 stats files, shard indexes 0..61.
 - coverage 41106/42430 parents = 96.8796%.
 - depth-11 pilot children 450105.
 - weighted branching 450105/41106 = 10.950.
 - diagnostic scaled estimate `N11 ~ 464603`.
 - aggregate remains diagnostic (`complete_shard_set=false`), not exact.
 - no budget/time/sample flags; cumulative prune counters remain `pruned_local=0`,
   `pruned_spectral=0`, `pruned_triangle_split=0`.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. Exact `N11` now needs only shards 62..63 and a final strict aggregate without
`--allow-incomplete`.

NEXT ACTION: run shards 62..63 with `--frontier-out-dir`, then aggregate all 64 shards without
`--allow-incomplete` to certify exact `N11`. A merged depth-11 frontier still additionally needs
frontier rows for shards 0..11.

---

## R82 -- d10->d11 shard certification progress: shards 0..59 counted; shards 12..59 preserve frontier rows [2026-06-29]
## OUTCOME: count progress plus more chainable depth-11 frontier material. The counted pilot now
covers 60/64 shards (93.75% of the depth-10 frontier).

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 58-59 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r82 --aggregate-out scratchpad\r3_d10_to_d11_shard64_58_59_chain_aggregate_r82.json --allow-incomplete`

NEW SHARD RESULTS:
 - shard 58: 663 parents -> 7095 children, branching 10.701, wall 53.09s.
 - shard 59: 663 parents -> 7152 children, branching 10.787, wall 55.49s.
 - both shards wrote frontier JSONL files under `scratchpad\r3_d10_to_d11_frontiers\`.
 - actual graph-row counts match header/stat counts: shard 58 has 7095 rows; shard 59 has 7152 rows.

COMBINED PILOT (shards 0..59):
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r71_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r72_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r73_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r74_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r75_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r76_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r77_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r78_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r79_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r80_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r81_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r82_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_59_aggregate_r82.json`
 - loaded 60 stats files, shard indexes 0..59.
 - coverage 39780/42430 parents = 93.7544%.
 - depth-11 pilot children 434876.
 - weighted branching 434876/39780 = 10.932.
 - diagnostic scaled estimate `N11 ~ 463846`.
 - aggregate remains diagnostic (`complete_shard_set=false`), not exact.
 - no budget/time/sample flags; cumulative prune counters remain `pruned_local=0`,
   `pruned_spectral=0`, `pruned_triangle_split=0`.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. Exact `N11` now needs only shards 60..63. The late-shard behavior confirms the
one-command aggregate should be used for the exact count rather than a scaled estimate.

NEXT ACTION: continue with `--frontier-out-dir` for shards 60..63. A merged depth-11 frontier still
additionally needs frontier rows for shards 0..11.

---

## R81 -- d10->d11 shard certification progress: shards 0..57 counted; shards 12..57 preserve frontier rows [2026-06-29]
## OUTCOME: count progress plus more chainable depth-11 frontier material. The counted pilot now
covers 58/64 shards (90.63% of the depth-10 frontier).

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 56-57 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r81 --aggregate-out scratchpad\r3_d10_to_d11_shard64_56_57_chain_aggregate_r81.json --allow-incomplete`

NEW SHARD RESULTS:
 - shard 56: 663 parents -> 7978 children, branching 12.033, wall 54.91s.
 - shard 57: 663 parents -> 7032 children, branching 10.606, wall 55.66s.
 - both shards wrote frontier JSONL files under `scratchpad\r3_d10_to_d11_frontiers\`.
 - actual graph-row counts match header/stat counts: shard 56 has 7978 rows; shard 57 has 7032 rows.

COMBINED PILOT (shards 0..57):
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r71_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r72_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r73_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r74_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r75_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r76_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r77_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r78_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r79_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r80_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r81_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_57_aggregate_r81.json`
 - loaded 58 stats files, shard indexes 0..57.
 - coverage 38454/42430 parents = 90.6293%.
 - depth-11 pilot children 420629.
 - weighted branching 420629/38454 = 10.938.
 - diagnostic scaled estimate `N11 ~ 464120`.
 - aggregate remains diagnostic (`complete_shard_set=false`), not exact.
 - no budget/time/sample flags; cumulative prune counters remain `pruned_local=0`,
   `pruned_spectral=0`, `pruned_triangle_split=0`.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. Exact `N11` now needs only six remaining shards. The running estimate has risen as
late shards are wider than early shards, so finishing the exact count is the right next step.

NEXT ACTION: continue with `--frontier-out-dir` for shards 58..63. A merged depth-11 frontier still
additionally needs frontier rows for shards 0..11.

---

## R80 -- d10->d11 shard certification progress: shards 0..55 counted; shards 12..55 preserve frontier rows [2026-06-29]
## OUTCOME: count progress plus more chainable depth-11 frontier material. The counted pilot now
covers 56/64 shards (87.50% of the depth-10 frontier).

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 54-55 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r80 --aggregate-out scratchpad\r3_d10_to_d11_shard64_54_55_chain_aggregate_r80.json --allow-incomplete`

NEW SHARD RESULTS:
 - shard 54: 663 parents -> 7990 children, branching 12.051, wall 54.63s.
 - shard 55: 663 parents -> 8010 children, branching 12.081, wall 53.45s.
 - both shards wrote frontier JSONL files under `scratchpad\r3_d10_to_d11_frontiers\`.
 - actual graph-row counts match header/stat counts: shard 54 has 7990 rows; shard 55 has 8010 rows.

COMBINED PILOT (shards 0..55):
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r71_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r72_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r73_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r74_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r75_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r76_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r77_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r78_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r79_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r80_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_55_aggregate_r80.json`
 - loaded 56 stats files, shard indexes 0..55.
 - coverage 37128/42430 parents = 87.5041%.
 - depth-11 pilot children 405619.
 - weighted branching 405619/37128 = 10.925.
 - diagnostic scaled estimate `N11 ~ 463543`.
 - aggregate remains diagnostic (`complete_shard_set=false`), not exact.
 - no budget/time/sample flags; cumulative prune counters remain `pruned_local=0`,
   `pruned_spectral=0`, `pruned_triangle_split=0`.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. The late shards are wider than the early diagnostic sample, so exact `N11` must be
completed; extrapolation alone is no longer a trustworthy stand-in.

NEXT ACTION: continue with `--frontier-out-dir` for shards 56..63. Exact `N11` still needs the remaining
8 counted shards; a merged depth-11 frontier additionally needs frontier rows for shards 0..11.

---

## R79 -- d10->d11 shard certification progress: shards 0..53 counted; shards 12..53 preserve frontier rows [2026-06-29]
## OUTCOME: count progress plus more chainable depth-11 frontier material. The counted pilot now
covers 54/64 shards (84.38% of the depth-10 frontier).

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 52-53 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r79 --aggregate-out scratchpad\r3_d10_to_d11_shard64_52_53_chain_aggregate_r79.json --allow-incomplete`

NEW SHARD RESULTS:
 - shard 52: 663 parents -> 8216 children, branching 12.392, wall 54.96s.
 - shard 53: 663 parents -> 7781 children, branching 11.736, wall 54.24s.
 - both shards wrote frontier JSONL files under `scratchpad\r3_d10_to_d11_frontiers\`.
 - actual graph-row counts match header/stat counts: shard 52 has 8216 rows; shard 53 has 7781 rows.

COMBINED PILOT (shards 0..53):
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r71_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r72_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r73_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r74_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r75_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r76_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r77_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r78_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r79_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_53_aggregate_r79.json`
 - loaded 54 stats files, shard indexes 0..53.
 - coverage 35802/42430 parents = 84.3790%.
 - depth-11 pilot children 389619.
 - weighted branching 389619/35802 = 10.883.
 - diagnostic scaled estimate `N11 ~ 461749`.
 - aggregate remains diagnostic (`complete_shard_set=false`), not exact.
 - no budget/time/sample flags; cumulative prune counters remain `pruned_local=0`,
   `pruned_spectral=0`, `pruned_triangle_split=0`.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. The wide 52-53 pair raised the diagnostic `N11` estimate, reinforcing why the last
shards must be counted rather than extrapolated.

NEXT ACTION: continue with `--frontier-out-dir` for shards 54..63. Exact `N11` still needs the remaining
10 counted shards; a merged depth-11 frontier additionally needs frontier rows for shards 0..11.

---

## R78 -- d10->d11 shard certification progress: shards 0..51 counted; shards 12..51 preserve frontier rows [2026-06-29]
## OUTCOME: count progress plus more chainable depth-11 frontier material. The counted pilot now
covers 52/64 shards (81.25% of the depth-10 frontier).

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 50-51 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r78 --aggregate-out scratchpad\r3_d10_to_d11_shard64_50_51_chain_aggregate_r78.json --allow-incomplete`

NEW SHARD RESULTS:
 - shard 50: 663 parents -> 7969 children, branching 12.020, wall 56.36s.
 - shard 51: 663 parents -> 6983 children, branching 10.532, wall 55.96s.
 - both shards wrote frontier JSONL files under `scratchpad\r3_d10_to_d11_frontiers\`.
 - actual graph-row counts match header/stat counts: shard 50 has 7969 rows; shard 51 has 6983 rows.

COMBINED PILOT (shards 0..51):
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r71_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r72_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r73_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r74_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r75_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r76_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r77_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r78_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_51_aggregate_r78.json`
 - loaded 52 stats files, shard indexes 0..51.
 - coverage 34476/42430 parents = 81.2538%.
 - depth-11 pilot children 373622.
 - weighted branching 373622/34476 = 10.837.
 - diagnostic scaled estimate `N11 ~ 459821`.
 - aggregate remains diagnostic (`complete_shard_set=false`), not exact.
 - no budget/time/sample flags; cumulative prune counters remain `pruned_local=0`,
   `pruned_spectral=0`, `pruned_triangle_split=0`.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. More than 81% of the depth-10 parents are now counted, but this still has no
proof-level consequence until all shards are in.

NEXT ACTION: continue with `--frontier-out-dir` for shards 52..63. Exact `N11` still needs the remaining
12 counted shards; a merged depth-11 frontier additionally needs frontier rows for shards 0..11.

---

## R77 -- d10->d11 shard certification progress: shards 0..49 counted; shards 12..49 preserve frontier rows [2026-06-29]
## OUTCOME: count progress plus more chainable depth-11 frontier material. The counted pilot now
covers 50/64 shards (78.13% of the depth-10 frontier).

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 48-49 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r77 --aggregate-out scratchpad\r3_d10_to_d11_shard64_48_49_chain_aggregate_r77.json --allow-incomplete`

NEW SHARD RESULTS:
 - shard 48: 663 parents -> 6635 children, branching 10.008, wall 53.45s.
 - shard 49: 663 parents -> 7602 children, branching 11.466, wall 54.73s.
 - both shards wrote frontier JSONL files under `scratchpad\r3_d10_to_d11_frontiers\`.
 - actual graph-row counts match header/stat counts: shard 48 has 6635 rows; shard 49 has 7602 rows.

COMBINED PILOT (shards 0..49):
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r71_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r72_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r73_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r74_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r75_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r76_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r77_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_49_aggregate_r77.json`
 - loaded 50 stats files, shard indexes 0..49.
 - coverage 33150/42430 parents = 78.1287%.
 - depth-11 pilot children 358670.
 - weighted branching 358670/33150 = 10.820.
 - diagnostic scaled estimate `N11 ~ 459076`.
 - aggregate remains diagnostic (`complete_shard_set=false`), not exact.
 - no budget/time/sample flags; cumulative prune counters remain `pruned_local=0`,
   `pruned_spectral=0`, `pruned_triangle_split=0`.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. The shallow certificate is close to exact `N11`, but the final 14 shards still matter.
No prune predicate has fired by depth 11.

NEXT ACTION: continue with `--frontier-out-dir` for shards 50..63. Exact `N11` still needs the remaining
14 counted shards; a merged depth-11 frontier additionally needs frontier rows for shards 0..11.

---

## R76 -- d10->d11 shard certification progress: shards 0..47 counted; shards 12..47 preserve frontier rows [2026-06-29]
## OUTCOME: count progress plus more chainable depth-11 frontier material. The counted pilot now
covers 48/64 shards (75.00% of the depth-10 frontier).

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 46-47 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r76 --aggregate-out scratchpad\r3_d10_to_d11_shard64_46_47_chain_aggregate_r76.json --allow-incomplete`

NEW SHARD RESULTS:
 - shard 46: 663 parents -> 7894 children, branching 11.906, wall 54.79s.
 - shard 47: 663 parents -> 7325 children, branching 11.048, wall 54.75s.
 - both shards wrote frontier JSONL files under `scratchpad\r3_d10_to_d11_frontiers\`.
 - actual graph-row counts match header/stat counts: shard 46 has 7894 rows; shard 47 has 7325 rows.

COMBINED PILOT (shards 0..47):
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r71_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r72_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r73_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r74_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r75_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r76_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_47_aggregate_r76.json`
 - loaded 48 stats files, shard indexes 0..47.
 - coverage 31824/42430 parents = 75.0035%.
 - depth-11 pilot children 344433.
 - weighted branching 344433/31824 = 10.823.
 - diagnostic scaled estimate `N11 ~ 459222`.
 - aggregate remains diagnostic (`complete_shard_set=false`), not exact.
 - no budget/time/sample flags; cumulative prune counters remain `pruned_local=0`,
   `pruned_spectral=0`, `pruned_triangle_split=0`.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. The exact-count campaign has reached three quarters coverage. No depth-11
generation/pruning predicate has fired, and the problem remains unsolved.

NEXT ACTION: continue with `--frontier-out-dir` for shards 48..63. Exact `N11` still needs the remaining
16 counted shards; a merged depth-11 frontier additionally needs frontier rows for shards 0..11.

---

## R75 -- d10->d11 shard certification progress: shards 0..45 counted; shards 12..45 preserve frontier rows [2026-06-29]
## OUTCOME: count progress plus more chainable depth-11 frontier material. The counted pilot now
covers 46/64 shards (71.88% of the depth-10 frontier).

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 44-45 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r75 --aggregate-out scratchpad\r3_d10_to_d11_shard64_44_45_chain_aggregate_r75.json --allow-incomplete`

NEW SHARD RESULTS:
 - shard 44: 663 parents -> 6840 children, branching 10.317, wall 54.55s.
 - shard 45: 663 parents -> 7721 children, branching 11.646, wall 54.29s.
 - both shards wrote frontier JSONL files under `scratchpad\r3_d10_to_d11_frontiers\`.
 - actual graph-row counts match header/stat counts: shard 44 has 6840 rows; shard 45 has 7721 rows.

COMBINED PILOT (shards 0..45):
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r71_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r72_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r73_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r74_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r75_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_45_aggregate_r75.json`
 - loaded 46 stats files, shard indexes 0..45.
 - coverage 30498/42430 parents = 71.8784%.
 - depth-11 pilot children 329214.
 - weighted branching 329214/30498 = 10.795.
 - diagnostic scaled estimate `N11 ~ 458015`.
 - aggregate remains diagnostic (`complete_shard_set=false`), not exact.
 - no budget/time/sample flags; cumulative prune counters remain `pruned_local=0`,
   `pruned_spectral=0`, `pruned_triangle_split=0`.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. The exact-count campaign is now roughly 72% complete. There is still no certified
exact `N11` and no solve-level obstruction/construction.

NEXT ACTION: continue with `--frontier-out-dir` for shards 46..63. Exact `N11` still needs the remaining
18 counted shards; a merged depth-11 frontier additionally needs frontier rows for shards 0..11.

---

## R74 -- d10->d11 shard certification progress: shards 0..43 counted; shards 12..43 preserve frontier rows [2026-06-29]
## OUTCOME: count progress plus more chainable depth-11 frontier material. The counted pilot now
covers 44/64 shards (68.75% of the depth-10 frontier).

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 42-43 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r74 --aggregate-out scratchpad\r3_d10_to_d11_shard64_42_43_chain_aggregate_r74.json --allow-incomplete`

NEW SHARD RESULTS:
 - shard 42: 663 parents -> 7519 children, branching 11.341, wall 55.64s.
 - shard 43: 663 parents -> 7082 children, branching 10.682, wall 54.91s.
 - both shards wrote frontier JSONL files under `scratchpad\r3_d10_to_d11_frontiers\`.
 - actual graph-row counts match header/stat counts: shard 42 has 7519 rows; shard 43 has 7082 rows.

COMBINED PILOT (shards 0..43):
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r71_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r72_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r73_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r74_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_43_aggregate_r74.json`
 - loaded 44 stats files, shard indexes 0..43.
 - coverage 29172/42430 parents = 68.7532%.
 - depth-11 pilot children 314653.
 - weighted branching 314653/29172 = 10.786.
 - diagnostic scaled estimate `N11 ~ 457656`.
 - aggregate remains diagnostic (`complete_shard_set=false`), not exact.
 - no budget/time/sample flags; cumulative prune counters remain `pruned_local=0`,
   `pruned_spectral=0`, `pruned_triangle_split=0`.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. The d10->d11 exact-count campaign is now beyond two thirds complete. The
mathematical status is unchanged: measurement only, no construction/nonexistence proof.

NEXT ACTION: continue with `--frontier-out-dir` for shards 44..63. Exact `N11` still needs the remaining
20 counted shards; a merged depth-11 frontier additionally needs frontier rows for shards 0..11.

---

## R73 -- d10->d11 shard certification progress: shards 0..41 counted; shards 12..41 preserve frontier rows [2026-06-29]
## OUTCOME: count progress plus more chainable depth-11 frontier material. The counted pilot now
covers 42/64 shards (65.63% of the depth-10 frontier).

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 40-41 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r73 --aggregate-out scratchpad\r3_d10_to_d11_shard64_40_41_chain_aggregate_r73.json --allow-incomplete`

NEW SHARD RESULTS:
 - shard 40: 663 parents -> 7075 children, branching 10.671, wall 54.50s.
 - shard 41: 663 parents -> 7809 children, branching 11.778, wall 54.65s.
 - both shards wrote frontier JSONL files under `scratchpad\r3_d10_to_d11_frontiers\`.
 - actual graph-row counts match header/stat counts: shard 40 has 7075 rows; shard 41 has 7809 rows.

COMBINED PILOT (shards 0..41):
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r71_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r72_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r73_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_41_aggregate_r73.json`
 - loaded 42 stats files, shard indexes 0..41.
 - coverage 27846/42430 parents = 65.6281%.
 - depth-11 pilot children 300052.
 - weighted branching 300052/27846 = 10.775.
 - diagnostic scaled estimate `N11 ~ 457201`.
 - aggregate remains diagnostic (`complete_shard_set=false`), not exact.
 - no budget/time/sample flags; cumulative prune counters remain `pruned_local=0`,
   `pruned_spectral=0`, `pruned_triangle_split=0`.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. The count certificate now covers just under two thirds of the depth-10 parent frontier.
The exact depth-11 frontier is still unfinished, and this remains measurement rather than a solution.

NEXT ACTION: continue with `--frontier-out-dir` for shards 42..63. Exact `N11` still needs the remaining
22 counted shards; a merged depth-11 frontier additionally needs frontier rows for shards 0..11.

---

## R72 -- d10->d11 shard certification progress: shards 0..39 counted; shards 12..39 preserve frontier rows [2026-06-29]
## OUTCOME: count progress plus more chainable depth-11 frontier material. The counted pilot now
covers 40/64 shards (62.50% of the depth-10 frontier).

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 38-39 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r72 --aggregate-out scratchpad\r3_d10_to_d11_shard64_38_39_chain_aggregate_r72.json --allow-incomplete`

NEW SHARD RESULTS:
 - shard 38: 663 parents -> 6589 children, branching 9.938, wall 53.44s.
 - shard 39: 663 parents -> 7913 children, branching 11.935, wall 54.14s.
 - both shards wrote frontier JSONL files under `scratchpad\r3_d10_to_d11_frontiers\`.
 - actual graph-row counts match header/stat counts: shard 38 has 6589 rows; shard 39 has 7913 rows.

COMBINED PILOT (shards 0..39):
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r71_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r72_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_39_aggregate_r72.json`
 - loaded 40 stats files, shard indexes 0..39.
 - coverage 26520/42430 parents = 62.5029%.
 - depth-11 pilot children 285168.
 - weighted branching 285168/26520 = 10.753.
 - diagnostic scaled estimate `N11 ~ 456247`.
 - aggregate remains diagnostic (`complete_shard_set=false`), not exact.
 - no budget/time/sample flags; cumulative prune counters remain `pruned_local=0`,
   `pruned_spectral=0`, `pruned_triangle_split=0`.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. The cumulative shallow estimate remains in the mid-`4.5e5` range. This still
does not solve the 99-graph problem and still does not certify exact `N11`.

NEXT ACTION: continue with `--frontier-out-dir` for shards 40..63. Exact `N11` still needs the remaining
24 counted shards; a merged depth-11 frontier additionally needs frontier rows for shards 0..11.

---

## R71 -- d10->d11 shard certification progress: shards 0..37 counted; shards 12..37 preserve frontier rows [2026-06-29]
## OUTCOME: count progress plus more chainable depth-11 frontier material. The counted pilot now
covers 38/64 shards (59.38% of the depth-10 frontier).

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 36-37 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r71 --aggregate-out scratchpad\r3_d10_to_d11_shard64_36_37_chain_aggregate_r71.json --allow-incomplete`

NEW SHARD RESULTS:
 - shard 36: 663 parents -> 6665 children, branching 10.053, wall 54.92s.
 - shard 37: 663 parents -> 6399 children, branching 9.652, wall 54.64s.
 - both shards wrote frontier JSONL files under `scratchpad\r3_d10_to_d11_frontiers\`.
 - actual graph-row counts match header/stat counts: shard 36 has 6665 rows; shard 37 has 6399 rows.

COMBINED PILOT (shards 0..37):
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r71_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_37_aggregate_r71.json`
 - loaded 38 stats files, shard indexes 0..37.
 - coverage 25194/42430 parents = 59.3778%.
 - depth-11 pilot children 270666.
 - weighted branching 270666/25194 = 10.743.
 - diagnostic scaled estimate `N11 ~ 455837`.
 - aggregate remains diagnostic (`complete_shard_set=false`), not exact.
 - no budget/time/sample flags; cumulative prune counters remain `pruned_local=0`,
   `pruned_spectral=0`, `pruned_triangle_split=0`.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. The shallow d10->d11 estimate continues to drift downward, but proof status is
unchanged: no exact `N11`, no graph, no nonexistence proof, and no pruning by depth 11.

NEXT ACTION: continue with `--frontier-out-dir` for shards 38..63. Exact `N11` still needs the remaining
26 counted shards; a merged depth-11 frontier additionally needs frontier rows for shards 0..11.

---

## R70 -- d10->d11 shard certification progress: shards 0..35 counted; shards 12..35 preserve frontier rows [2026-06-29]
## OUTCOME: count progress plus more chainable depth-11 frontier material. The counted pilot now
covers 36/64 shards (56.25% of the depth-10 frontier).

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 34-35 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r70 --aggregate-out scratchpad\r3_d10_to_d11_shard64_34_35_chain_aggregate_r70.json --allow-incomplete`

NEW SHARD RESULTS:
 - shard 34: 663 parents -> 7051 children, branching 10.635, wall 53.35s.
 - shard 35: 663 parents -> 6691 children, branching 10.092, wall 53.57s.
 - both shards wrote frontier JSONL files under `scratchpad\r3_d10_to_d11_frontiers\`.
 - actual graph-row counts match header/stat counts: shard 34 has 7051 rows; shard 35 has 6691 rows.

COMBINED PILOT (shards 0..35):
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_35_aggregate_r70.json`
 - loaded 36 stats files, shard indexes 0..35.
 - coverage 23868/42430 parents = 56.2527%.
 - depth-11 pilot children 257602.
 - weighted branching 257602/23868 = 10.793.
 - diagnostic scaled estimate `N11 ~ 457938`.
 - aggregate remains diagnostic (`complete_shard_set=false`), not exact.
 - no budget/time/sample flags; cumulative prune counters remain `pruned_local=0`,
   `pruned_spectral=0`, `pruned_triangle_split=0`.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. The d10->d11 certificate now covers more than 56% of the parent frontier, but
`N11` is still not exact and no pruning predicate has fired by depth 11.

NEXT ACTION: continue with `--frontier-out-dir` for shards 36..63. Exact `N11` still needs the remaining
28 counted shards; a merged depth-11 frontier additionally needs frontier rows for shards 0..11.

---

## R69 -- d10->d11 shard certification progress: shards 0..33 counted; shards 12..33 preserve frontier rows [2026-06-29]
## OUTCOME: count progress plus more chainable depth-11 frontier material. The counted pilot now
covers 34/64 shards (53.13% of the depth-10 frontier).

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 32-33 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r69 --aggregate-out scratchpad\r3_d10_to_d11_shard64_32_33_chain_aggregate_r69.json --allow-incomplete`

NEW SHARD RESULTS:
 - shard 32: 663 parents -> 6725 children, branching 10.143, wall 54.58s.
 - shard 33: 663 parents -> 7181 children, branching 10.831, wall 53.49s.
 - both shards wrote frontier JSONL files under `scratchpad\r3_d10_to_d11_frontiers\`.
 - actual graph-row counts match header/stat counts: shard 32 has 6725 rows; shard 33 has 7181 rows.

COMBINED PILOT (shards 0..33):
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_33_aggregate_r69.json`
 - loaded 34 stats files, shard indexes 0..33.
 - coverage 22542/42430 parents = 53.1275%.
 - depth-11 pilot children 243860.
 - weighted branching 243860/22542 = 10.818.
 - diagnostic scaled estimate `N11 ~ 459009`.
 - aggregate remains diagnostic (`complete_shard_set=false`), not exact.
 - no budget/time/sample flags; cumulative prune counters remain `pruned_local=0`,
   `pruned_spectral=0`, `pruned_triangle_split=0`.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. More than half the d10 frontier is now counted, but `N11` is still not exact.
The chainable frontier set covers shards 12..33; shards 0..11 remain stats-only unless rerun with
frontier output.

NEXT ACTION: continue with `--frontier-out-dir` for shards 34..63. Exact `N11` still needs the remaining
30 counted shards; a merged depth-11 frontier additionally needs frontier rows for shards 0..11.

---

## R68 -- d10->d11 shard certification progress: shards 0..31 counted; shards 12..31 preserve frontier rows [2026-06-29]
## OUTCOME: halfway count progress plus more chainable depth-11 frontier material. The counted pilot now
covers 32/64 shards (50.00% of the depth-10 frontier).

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 30-31 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r68 --aggregate-out scratchpad\r3_d10_to_d11_shard64_30_31_chain_aggregate_r68.json --allow-incomplete`

NEW SHARD RESULTS:
 - shard 30: 663 parents -> 6689 children, branching 10.089, wall 53.93s.
 - shard 31: 663 parents -> 6825 children, branching 10.294, wall 54.19s.
 - both shards wrote frontier JSONL files under `scratchpad\r3_d10_to_d11_frontiers\`.
 - actual graph-row counts match header/stat counts: shard 30 has 6689 rows; shard 31 has 6825 rows.

COMBINED PILOT (shards 0..31):
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_31_aggregate_r68.json`
 - loaded 32 stats files, shard indexes 0..31.
 - coverage 21216/42430 parents = 50.0024%.
 - depth-11 pilot children 229954.
 - weighted branching 229954/21216 = 10.838.
 - diagnostic scaled estimate `N11 ~ 459886`.
 - aggregate remains diagnostic (`complete_shard_set=false`), not exact.
 - no budget/time/sample flags; cumulative prune counters remain `pruned_local=0`,
   `pruned_spectral=0`, `pruned_triangle_split=0`.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. Half the d10 frontier is counted, but `N11` is still not exact. The chainable frontier
set covers shards 12..31; shards 0..11 remain stats-only unless rerun with frontier output.

NEXT ACTION: continue with `--frontier-out-dir` for shards 32..63. Exact `N11` still needs the remaining
32 counted shards; a merged depth-11 frontier additionally needs frontier rows for shards 0..11.

---

## R67 -- d10->d11 shard certification progress: shards 0..29 counted; shards 12..29 preserve frontier rows [2026-06-29]
## OUTCOME: incremental count progress plus more chainable depth-11 frontier material. The counted
pilot now covers 30/64 shards (46.88% of the depth-10 frontier).

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 28-29 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r67 --aggregate-out scratchpad\r3_d10_to_d11_shard64_28_29_chain_aggregate_r67.json --allow-incomplete`

NEW SHARD RESULTS:
 - shard 28: 663 parents -> 7632 children, branching 11.511, wall 54.09s.
 - shard 29: 663 parents -> 7745 children, branching 11.682, wall 54.48s.
 - both shards wrote frontier JSONL files under `scratchpad\r3_d10_to_d11_frontiers\`.
 - actual graph-row counts match header/stat counts: shard 28 has 7632 rows; shard 29 has 7745 rows.

COMBINED PILOT (shards 0..29):
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_29_aggregate_r67.json`
 - loaded 30 stats files, shard indexes 0..29.
 - coverage 19890/42430 parents = 46.8772%.
 - depth-11 pilot children 216440.
 - weighted branching 216440/19890 = 10.882.
 - diagnostic scaled estimate `N11 ~ 461717`.
 - aggregate remains diagnostic (`complete_shard_set=false`), not exact.
 - no budget/time/sample flags; cumulative prune counters remain `pruned_local=0`,
   `pruned_spectral=0`, `pruned_triangle_split=0`.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. This is nearly half of the depth-10 frontier counted, but still not an exact count.
No shallow generation/pruning predicate has fired by depth 11.

NEXT ACTION: continue with `--frontier-out-dir` for shards 30..63. Exact `N11` still needs 34 counted
shards; a merged depth-11 frontier additionally needs frontier rows for shards 0..11.

---

## R66 -- d10->d11 shard certification progress: shards 0..27 counted; shards 12..27 preserve frontier rows [2026-06-29]
## OUTCOME: incremental count progress plus more chainable depth-11 frontier material. The counted
pilot now covers 28/64 shards (43.75% of the depth-10 frontier).

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 26-27 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r66 --aggregate-out scratchpad\r3_d10_to_d11_shard64_26_27_chain_aggregate_r66.json --allow-incomplete`

NEW SHARD RESULTS:
 - shard 26: 663 parents -> 7374 children, branching 11.122, wall 54.92s.
 - shard 27: 663 parents -> 7260 children, branching 10.950, wall 54.08s.
 - both shards wrote frontier JSONL files under `scratchpad\r3_d10_to_d11_frontiers\`.
 - actual graph-row counts match header/stat counts: shard 26 has 7374 rows; shard 27 has 7260 rows.

COMBINED PILOT (shards 0..27):
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_27_aggregate_r66.json`
 - loaded 28 stats files, shard indexes 0..27.
 - coverage 18564/42430 parents = 43.7521%.
 - depth-11 pilot children 201063.
 - weighted branching 201063/18564 = 10.831.
 - diagnostic scaled estimate `N11 ~ 459551`.
 - aggregate remains diagnostic (`complete_shard_set=false`), not exact.
 - no budget/time/sample flags; cumulative prune counters remain `pruned_local=0`,
   `pruned_spectral=0`, `pruned_triangle_split=0`.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. Count and frontier certification continue to move, but this remains shallow
measurement: no exact `N11` and no pruning evidence yet.

NEXT ACTION: continue with `--frontier-out-dir` for shards 28..63. Exact `N11` still needs 36 counted
shards; a merged depth-11 frontier additionally needs frontier rows for shards 0..11.

---

## R65 -- d10->d11 shard certification progress: shards 0..25 counted; shards 12..25 preserve frontier rows [2026-06-29]
## OUTCOME: incremental count progress plus more chainable depth-11 frontier material. The counted
pilot now covers 26/64 shards (40.63% of the depth-10 frontier).

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 24-25 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r65 --aggregate-out scratchpad\r3_d10_to_d11_shard64_24_25_chain_aggregate_r65.json --allow-incomplete`

NEW SHARD RESULTS:
 - shard 24: 663 parents -> 6628 children, branching 9.997, wall 68.17s.
 - shard 25: 663 parents -> 8007 children, branching 12.077, wall 57.49s.
 - both shards wrote frontier JSONL files under `scratchpad\r3_d10_to_d11_frontiers\`.
 - actual graph-row counts match header/stat counts: shard 24 has 6628 rows; shard 25 has 8007 rows.

COMBINED PILOT (shards 0..25):
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_25_aggregate_r65.json`
 - loaded 26 stats files, shard indexes 0..25.
 - coverage 17238/42430 parents = 40.6269%.
 - depth-11 pilot children 186429.
 - weighted branching 186429/17238 = 10.815.
 - diagnostic scaled estimate `N11 ~ 458881`.
 - aggregate remains diagnostic (`complete_shard_set=false`), not exact.
 - no budget/time/sample flags; cumulative prune counters remain `pruned_local=0`,
   `pruned_spectral=0`, `pruned_triangle_split=0`.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. The count estimate remains in the mid-`4.5e5` range; no shallow gate has fired.
The chainable frontier set now covers shards 12..25 only.

NEXT ACTION: continue with `--frontier-out-dir` for shards 26..63. Exact `N11` still needs 38 counted
shards; a merged depth-11 frontier additionally needs frontier rows for shards 0..11.

---

## R64 -- d10->d11 shard certification progress: shards 0..23 counted; shards 12..23 preserve frontier rows [2026-06-29]
## OUTCOME: incremental count progress plus more chainable depth-11 frontier material. The counted
pilot now covers 24/64 shards (37.50% of the depth-10 frontier).

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 22-23 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r64 --aggregate-out scratchpad\r3_d10_to_d11_shard64_22_23_chain_aggregate_r64.json --allow-incomplete`

NEW SHARD RESULTS:
 - shard 22: 663 parents -> 6441 children, branching 9.715, wall 67.33s.
 - shard 23: 663 parents -> 6238 children, branching 9.409, wall 67.54s.
 - both shards wrote frontier JSONL files under `scratchpad\r3_d10_to_d11_frontiers\`.
 - actual graph-row counts match header/stat counts: shard 22 has 6441 rows; shard 23 has 6238 rows.

COMBINED PILOT (shards 0..23):
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_23_aggregate_r64.json`
 - loaded 24 stats files, shard indexes 0..23.
 - coverage 15912/42430 parents = 37.5018%.
 - depth-11 pilot children 171794.
 - weighted branching 171794/15912 = 10.797.
 - diagnostic scaled estimate `N11 ~ 458096`.
 - aggregate remains diagnostic (`complete_shard_set=false`), not exact.
 - no budget/time/sample flags; cumulative prune counters remain `pruned_local=0`,
   `pruned_spectral=0`, `pruned_triangle_split=0`.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. The estimate dropped because shards 22..23 are narrower, but the proof status is
unchanged: no exact `N11` yet and no shallow pruning by depth 11.

NEXT ACTION: continue with `--frontier-out-dir` for shards 24..63. Exact `N11` still needs 40 counted
shards; a merged depth-11 frontier additionally needs frontier rows for shards 0..11.

---

## R63 -- d10->d11 shard certification progress: shards 0..21 counted; shards 12..21 preserve frontier rows [2026-06-29]
## OUTCOME: incremental count progress plus more chainable depth-11 frontier material. The counted
pilot now covers 22/64 shards (34.38% of the depth-10 frontier).

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 20-21 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r63 --aggregate-out scratchpad\r3_d10_to_d11_shard64_20_21_chain_aggregate_r63.json --allow-incomplete`

NEW SHARD RESULTS:
 - shard 20: 663 parents -> 6815 children, branching 10.279, wall 54.84s.
 - shard 21: 663 parents -> 7332 children, branching 11.059, wall 55.12s.
 - both shards wrote frontier JSONL files under `scratchpad\r3_d10_to_d11_frontiers\`.
 - actual graph-row counts match header/stat counts: shard 20 has 6815 rows; shard 21 has 7332 rows.

COMBINED PILOT (shards 0..21):
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_21_aggregate_r63.json`
 - loaded 22 stats files, shard indexes 0..21.
 - coverage 14586/42430 parents = 34.3766%.
 - depth-11 pilot children 159115.
 - weighted branching 159115/14586 = 10.908.
 - diagnostic scaled estimate `N11 ~ 462858`.
 - aggregate remains diagnostic (`complete_shard_set=false`), not exact.
 - no budget/time/sample flags; cumulative prune counters remain `pruned_local=0`,
   `pruned_spectral=0`, `pruned_triangle_split=0`.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. The counted estimate remains in the `4.6e5-4.7e5` band, but it is still only a
deterministic incomplete-shard diagnostic. The chainable frontier set now covers shards 12..21 only.

NEXT ACTION: continue with `--frontier-out-dir` for shards 22..63. Exact `N11` still needs 42 counted
shards; a merged depth-11 frontier additionally needs frontier rows for shards 0..11.

---

## R62 -- d10->d11 shard certification progress: shards 0..19 counted; shards 12..19 preserve frontier rows [2026-06-29]
## OUTCOME: incremental count progress plus more chainable depth-11 frontier material. The counted
pilot now covers 20/64 shards (31.25% of the depth-10 frontier).

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 18-19 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r62 --aggregate-out scratchpad\r3_d10_to_d11_shard64_18_19_chain_aggregate_r62.json --allow-incomplete`

NEW SHARD RESULTS:
 - shard 18: 663 parents -> 6027 children, branching 9.090, wall 57.30s.
 - shard 19: 663 parents -> 6775 children, branching 10.219, wall 56.32s.
 - both shards wrote frontier JSONL files under `scratchpad\r3_d10_to_d11_frontiers\`.
 - actual graph-row counts match header/stat counts: shard 18 has 6027 rows; shard 19 has 6775 rows.

COMBINED PILOT (shards 0..19):
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_19_aggregate_r62.json`
 - loaded 20 stats files, shard indexes 0..19.
 - coverage 13260/42430 parents = 31.2515%.
 - depth-11 pilot children 144968.
 - weighted branching 144968/13260 = 10.933.
 - diagnostic scaled estimate `N11 ~ 463876`.
 - aggregate remains diagnostic (`complete_shard_set=false`), not exact.
 - no budget/time/sample flags; cumulative prune counters remain `pruned_local=0`,
   `pruned_spectral=0`, `pruned_triangle_split=0`.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. Shards 18..19 were narrower, bringing the scaled estimate down to `~4.64e5`.
The qualitative conclusion is unchanged: no shallow pruning by depth 11, and exact `N11` is still
unproven until the shard set is complete.

NEXT ACTION: continue with `--frontier-out-dir` for shards 20..63. Exact `N11` still needs 44 counted
shards; a merged depth-11 frontier additionally needs frontier rows for shards 0..11.

---

## R61 -- d10->d11 shard certification progress: shards 0..17 counted; shards 12..17 preserve frontier rows [2026-06-29]
## OUTCOME: incremental count progress plus more chainable depth-11 frontier material. The counted
pilot now covers 18/64 shards (28.13% of the depth-10 frontier).

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 16-17 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r61 --aggregate-out scratchpad\r3_d10_to_d11_shard64_16_17_chain_aggregate_r61.json --allow-incomplete`

NEW SHARD RESULTS:
 - shard 16: 663 parents -> 7738 children, branching 11.671, wall 56.00s.
 - shard 17: 663 parents -> 7909 children, branching 11.929, wall 57.31s.
 - both shards wrote frontier JSONL files under `scratchpad\r3_d10_to_d11_frontiers\`.
 - actual graph-row counts match header/stat counts: shard 16 has 7738 rows; shard 17 has 7909 rows.

COMBINED PILOT (shards 0..17):
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_17_aggregate_r61.json`
 - loaded 18 stats files, shard indexes 0..17.
 - coverage 11934/42430 parents = 28.1263%.
 - depth-11 pilot children 132166.
 - weighted branching 132166/11934 = 11.075.
 - diagnostic scaled estimate `N11 ~ 469901`.
 - aggregate remains diagnostic (`complete_shard_set=false`), not exact.
 - no budget/time/sample flags; cumulative prune counters remain `pruned_local=0`,
   `pruned_spectral=0`, `pruned_triangle_split=0`.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. Shards 16..17 were wider than the previous pair, so the scaled estimate returned
near `4.70e5`; still a sizing estimate only. The chainable frontier set now covers shards 12..17 only.

NEXT ACTION: continue with `--frontier-out-dir` for shards 18..63. Exact `N11` still needs 46 counted
shards; a merged depth-11 frontier additionally needs frontier rows for shards 0..11.

---

## R60 -- d10->d11 shard certification progress: shards 0..15 counted; shards 12..15 preserve frontier rows [2026-06-29]
## OUTCOME: incremental count progress plus more chainable depth-11 frontier material. One quarter of
the depth-10 frontier is now measured for `N11` diagnostics.

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 14-15 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r60 --aggregate-out scratchpad\r3_d10_to_d11_shard64_14_15_chain_aggregate_r60.json --allow-incomplete`

NEW SHARD RESULTS:
 - shard 14: 663 parents -> 7706 children, branching 11.623, wall 54.59s.
 - shard 15: 663 parents -> 6867 children, branching 10.357, wall 59.81s.
 - both shards wrote frontier JSONL files under `scratchpad\r3_d10_to_d11_frontiers\`.
 - actual graph-row counts match header/stat counts: shard 14 has 7706 rows; shard 15 has 6867 rows.

COMBINED PILOT (shards 0..15):
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_15_aggregate_r60.json`
 - loaded 16 stats files, shard indexes 0..15.
 - coverage 10608/42430 parents = 25.0012%.
 - depth-11 pilot children 116519.
 - weighted branching 116519/10608 = 10.984.
 - diagnostic scaled estimate `N11 ~ 466054`.
 - aggregate remains diagnostic (`complete_shard_set=false`), not exact.
 - no budget/time/sample flags; cumulative prune counters remain `pruned_local=0`,
   `pruned_spectral=0`, `pruned_triangle_split=0`.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. The count estimate remains stable near `4.66e5`, still not a theorem count. The
chainable frontier set now covers shards 12..15 only; exact merged depth-11 frontier still requires
frontier outputs for all 64 shards.

NEXT ACTION: continue with `--frontier-out-dir` for shards 16..63, and plan a rerun of shards 0..11 with
frontier output if the next exact continuation target is a merged depth-11 frontier rather than only an
exact `N11` count.

---

## R59 -- d10->d11 shard certification progress: shards 0..13 counted; shards 12..13 now preserve frontier rows [2026-06-29]
## OUTCOME: incremental count progress plus first chainable d10->d11 shard-frontier artifacts under the
R58 workflow.

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 12-13 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r59 --aggregate-out scratchpad\r3_d10_to_d11_shard64_12_13_chain_aggregate_r59.json --allow-incomplete`

NEW SHARD RESULTS:
 - shard 12: 663 parents -> 7196 children, branching 10.854, wall 56.32s.
 - shard 13: 663 parents -> 6795 children, branching 10.249, wall 54.47s.
 - both shards wrote frontier JSONL files under `scratchpad\r3_d10_to_d11_frontiers\`.
 - frontier headers correctly report `frontier_complete=false` globally (because this is a 64-way shard),
   `frontier_complete_for_loaded_scope=true`, `canonical_parent=true`, `seed_triangle=false`.
 - actual graph-row counts match header/stat counts: shard 12 has 7196 rows; shard 13 has 6795 rows.

COMBINED PILOT (shards 0..13):
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_13_aggregate_r59.json`
 - loaded 14 stats files, shard indexes 0..13.
 - coverage 9282/42430 parents = 21.8760%.
 - depth-11 pilot children 101946.
 - weighted branching 101946/9282 = 10.983.
 - diagnostic scaled estimate `N11 ~ 466017`.
 - aggregate remains diagnostic (`complete_shard_set=false`), not exact.
 - no budget/time/sample flags; cumulative prune counters remain `pruned_local=0`,
   `pruned_spectral=0`, `pruned_triangle_split=0`.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.

VERDICT: accepted. Shards 12..13 are the first d10->d11 shards that are useful both as count evidence
and as future chainable frontier material. Existing shards 0..11 remain valid for counts but still lack
frontier files.

NEXT ACTION: continue future shard ranges with `--frontier-out-dir scratchpad\r3_d10_to_d11_frontiers`.
If a complete depth-11 frontier is desired, rerun or regenerate stats+frontiers for shards 0..11 as well;
do not attempt to merge a mixed set that lacks frontier outputs.

---

## R58 -- chainable shard frontiers: runner writes per-shard frontier JSONL and strict merge tool validates complete sets [2026-06-29]
## OUTCOME: cloud workflow cost/reproducibility improvement. Future d10->d11 shard runs can preserve
their frontier rows, and a complete shard set can be merged into a new globally complete frontier for
exact continuation without rerunning the previous level.

SCAMPER LEVER: Rearrange/Combine. The R53-R57 d10->d11 stats-only shards certify counts but do not
preserve depth-11 frontier rows, so exact d11->d12 continuation would require rerunning d10->d11.
The safe change is to keep generation in `s3_slice_harness.py`, have the runner optionally pass
`--frontier-out` per shard, and add a separate merge command that refuses incomplete/incompatible sets.

IMPLEMENTED:
 - `s3_run_shards.py --frontier-out-dir DIR` writes one per-shard frontier JSONL named
   `<tag>_<idx>_frontier.jsonl` alongside each stats JSON.
 - Runner resume/skip now requires both the stats JSON and requested frontier JSONL to exist before
   skipping a shard.
 - New `s3_merge_frontiers.py`: consumes stats JSON files, reuses `s3_aggregate_shards.py` strict
   compatibility validation, verifies every named frontier file/header/row count/depth, refuses
   incomplete shard sets by default, and writes one merged `frontier_complete=true` JSONL only when
   the aggregate target depth is exact.

VALIDATION:
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py s3_merge_frontiers.py`
   passed.
 - Tiny exact two-shard frontier-output run:
   `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d5_test.jsonl --shard-count 2 --indices 0-1 --target-depth 6 --node-budget 2000 --time-cap 30 --level-cap 10000 --out-dir scratchpad\merge_test --frontier-out-dir scratchpad\merge_test --tag r3_d5_to_d6_merge_test --aggregate-out scratchpad\merge_test\r3_d5_to_d6_merge_aggregate.json`
   reproduced exact aggregate counts `5=21`, `6=62` while writing shard frontiers with 39 and 23 rows.
 - Merge command:
   `python s3_merge_frontiers.py scratchpad\merge_test\r3_d5_to_d6_merge_test_000.json scratchpad\merge_test\r3_d5_to_d6_merge_test_001.json --out scratchpad\merge_test\r3_frontier_d6_merged.jsonl`
   wrote 62 rows at depth 6 with `frontier_complete=true`.
 - Chainability proof:
   `python s3_slice_harness.py --slice --frontier-in scratchpad\merge_test\r3_frontier_d6_merged.jsonl --shard-count 1 --shard-index 0 --target-depth 7 --node-budget 5000 --time-cap 30 --level-cap 10000 --stats-out scratchpad\merge_test\r3_d6merged_to_d7_stats.json`
   followed by
   `python s3_aggregate_shards.py scratchpad\merge_test\r3_d6merged_to_d7_stats.json --expect 6=62 --expect 7=208 --out scratchpad\merge_test\r3_d6merged_to_d7_aggregate.json`
   passed, proving the merged frontier is accepted as a complete source and continues to the known
   exact `N7=208`.
 - Resume/skip proof: rerunning the two-shard runner skipped both shards only after seeing both stats
   and frontier files, then regenerated the exact aggregate.
 - Strictness proof: `python s3_merge_frontiers.py scratchpad\merge_test\r3_d5_to_d6_merge_test_000.json --out scratchpad\merge_test\should_not_exist.jsonl`
   refused the incomplete set with `missing shard indexes [1]`.

VERDICT: accepted workflow improvement. This does not change the mathematical search tree and does not
solve srg99, but it prevents expensive exact-frontier work from becoming stats-only dead end output.

NEXT ACTION: for future d10->d11 shards, use `s3_run_shards.py --frontier-out-dir ...` so completed
shards can later be merged into a chainable exact depth-11 frontier. Existing R53-R57 stats-only shards
remain valid count evidence but would need rerun if their frontier rows are required.

---

## R57 -- d10->d11 shard certification progress: shards 0..11 complete, 18.75% coverage [2026-06-29]
## OUTCOME: incremental exact-shard progress toward certified `N11`. Two additional deterministic shards
completed; twelve of sixty-four depth-10 frontier shards are now measured.

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 10-11 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --tag r3_d10_to_d11_shard64_runner_r57 --aggregate-out scratchpad\r3_d10_to_d11_shard64_10_11_runner_aggregate_r57.json --allow-incomplete`

NEW SHARD RESULTS:
 - shard 10: 663 parents -> 6632 children, branching 10.003, wall 54.45s.
 - shard 11: 663 parents -> 7264 children, branching 10.956, wall 52.70s.
 - two-shard aggregate: 1326/42430 parents, 13896 children, diagnostic scaled `N11 ~ 444651`.

COMBINED PILOT (shards 0..11):
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_11_aggregate_r57.json`
 - loaded 12 stats files, shard indexes 0..11.
 - coverage 7956/42430 parents = 18.7509%.
 - depth-11 pilot children 87955.
 - weighted branching 87955/7956 = 11.055.
 - diagnostic scaled estimate `N11 ~ 469071`.
 - aggregate remains diagnostic (`complete_shard_set=false`), not exact.
 - no budget/time/sample flags; cumulative prune counters remain `pruned_local=0`,
   `pruned_spectral=0`, `pruned_triangle_split=0`.
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py` passed after
   the R57 run (code unchanged; sanity check only).

VERDICT: accepted incremental measurement. The cumulative scaled estimate has stabilized near
`4.7e5`, but this is still not a theorem count. No shallow pruning evidence has appeared by depth 11.
Exact `N11` requires the remaining 52 shards (12..63) and a final aggregate without
`--allow-incomplete`.

NEXT ACTION: continue small foreground shard ranges only if exact shallow `N11` is valuable. For a
more decisive next mathematical step, use the verified runner/spec as the oracle for a faster
nauty/Traces/C generator or for a deeper prefix strategy aimed at the k~34+ spectral-gate regime.

---

## R56 -- d10->d11 shard certification progress: shards 0..9 complete, 15.63% coverage [2026-06-29]
## OUTCOME: incremental exact-shard progress toward certified `N11`. Two more deterministic shards
completed under the R54/R55 runner path; the combined pilot now covers ten of sixty-four depth-10
frontier shards.

PRE-RUN VALIDATION:
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py` passed.
 - `python s3_slice_harness.py --gate` passed: rook(9) all 9! local orders accepted, 0/511 rook
   spectral rejects, triangle-split identities on all 512 rook subsets, and exact T(7) r=3 CRS/CSP
   reconstruction with 0 false rejects over 5242 real induced subgraphs.

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 8-9 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --tag r3_d10_to_d11_shard64_runner_r56 --aggregate-out scratchpad\r3_d10_to_d11_shard64_08_09_runner_aggregate_r56.json --allow-incomplete`

NEW SHARD RESULTS:
 - shard 8: 663 parents -> 7680 children, branching 11.584, wall 54.47s.
 - shard 9: 663 parents -> 7721 children, branching 11.646, wall 53.85s.
 - two-shard aggregate: 1326/42430 parents, 15401 children, diagnostic scaled `N11 ~ 492809`.

COMBINED PILOT (shards 0..9):
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_09_aggregate_r56.json`
 - loaded 10 stats files, shard indexes 0..9.
 - coverage 6630/42430 parents = 15.6257%.
 - depth-11 pilot children 74059.
 - weighted branching 74059/6630 = 11.170.
 - diagnostic scaled estimate `N11 ~ 473955`.
 - aggregate remains diagnostic (`complete_shard_set=false`), not exact.
 - no budget/time/sample flags; cumulative prune counters remain `pruned_local=0`,
   `pruned_spectral=0`, `pruned_triangle_split=0`.

VERDICT: accepted incremental measurement. The certification path is still working and resumable, but
the shallow d10->d11 branch is rising in these later shards and still shows no spectral bite. Exact
`N11` requires the remaining 54 shards (10..63) and a final aggregate without `--allow-incomplete`.

NEXT ACTION: continue foreground shard certification in small ranges (e.g. 10..15) if the goal is an
exact shallow `N11`; if the priority is the decisive k~34+ spectral-bite measurement, spend the next
cycle on a faster nauty/Traces/C port or a deeper prefix strategy rather than treating more shallow
diagnostic shards as decisive.

---

## R55 -- d10->d11 shard certification progress: shards 0..7 complete, 12.5% coverage [2026-06-29]
## OUTCOME: incremental exact-shard progress toward certified `N11`. Two more deterministic shards completed under the R54 runner; the combined pilot now covers one eighth of the depth-10 frontier.

COMMAND RUN:
`python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 6-7 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --tag r3_d10_to_d11_shard64_runner_r55 --aggregate-out scratchpad\r3_d10_to_d11_shard64_06_07_runner_aggregate_r55.json --allow-incomplete`

NEW SHARD RESULTS:
 - shard 6: 663 parents -> 6745 children, branching 10.173, wall 56.26s.
 - shard 7: 663 parents -> 7881 children, branching 11.887, wall 54.82s.
 - two-shard aggregate: 1326/42430 parents, 14626 children, diagnostic scaled `N11 ~ 468010`.

COMBINED PILOT (shards 0..7):
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_07_aggregate_r55.json`
 - loaded 8 stats files, shard indexes 0..7.
 - coverage 5304/42430 parents = 12.5006%.
 - depth-11 pilot children 58658.
 - weighted branching 58658/5304 = 11.059.
 - diagnostic scaled estimate `N11 ~ 469242`.
 - aggregate remains diagnostic (`complete_shard_set=false`), not exact.
 - prune inspection over all eight shard stats: `pruned_local=0`, `pruned_spectral=0`,
   `pruned_triangle_split=0`.

VERDICT: accepted incremental measurement. The certification path is working and resumable. Exact
`N11` still requires 56 more shards (8..63) and a final aggregate without `--allow-incomplete`.

NEXT ACTION: continue the foreground shard certification in small ranges (e.g. 8..15) using
`s3_run_shards.py`, or switch effort to a faster nauty/Traces/C port if the priority is deep k~34
measurement over exact shallow `N11`.

---

## R54 -- resumable shard-range runner; six d10->d11 pilot shards combined [2026-06-29]
## OUTCOME: runnable cloud experiment improvement + larger diagnostic sizing sample. The manual 64-shard recipe is now a foreground one-command resumable runner, verified on shards 4 and 5.

IMPLEMENTED:
 - New `s3_run_shards.py`: a thin wrapper around the verified harness and strict aggregator.
 - It runs a finite shard index set (`--indices` or `--start/--stop`), writes one `--stats-out` JSON per
   shard, skips already completed shard JSON unless `--force`, and optionally aggregates the selected
   stats files.
 - It does not implement graph generation, pruning, or aggregation logic; those stay in
   `s3_slice_harness.py` and `s3_aggregate_shards.py`.

VALIDATION:
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py s3_run_shards.py` passed.
 - Runner command:
   `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 4-5 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --tag r3_d10_to_d11_shard64_runner_r54 --aggregate-out scratchpad\r3_d10_to_d11_shard64_04_05_runner_aggregate_r54.json --allow-incomplete`
   completed shards 4 and 5, then aggregated them as diagnostic.
 - Resume/skip proof: rerunning the same command skipped both existing shard JSON files and regenerated
   only the aggregate.

NEW SHARD RESULTS:
 - shard 4: 663 parents -> 7392 children, branching 11.149, wall 54.34s.
 - shard 5: 663 parents -> 7473 children, branching 11.271, wall 54.31s.
 - two-shard runner aggregate: 1326/42430 parents covered, 14865 children, diagnostic scaled estimate
   `N11 ~ 475658`.

COMBINED PILOT (R53 shards 0..3 + R54 shards 4..5):
 - `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_05_aggregate_r54.json`
 - loaded 6 stats files, coverage 3978/42430 parents = 9.38%.
 - depth-11 pilot children 44032.
 - weighted branching 44032/3978 = 11.069.
 - diagnostic scaled estimate `N11 ~ 469653`.
 - all rows remain diagnostic, not exact, because only 6/64 shards are present.

VERDICT: accepted cloud workflow improvement. Exact `N11` is still not certified, but the certification
run is now one command and resumable. The diagnostic evidence continues to show growth and no pruning by
depth 11.

NEXT ACTION: use `s3_run_shards.py` to complete the remaining d10->d11 shard indexes and aggregate
without `--allow-incomplete` to certify exact `N11`, or move directly to a faster C/nauty port if the
goal is reaching k~34 rather than polishing shallow counts.

---

## R53 -- depth-10 to depth-11 sharded pilot; diagnostic N11 sizing, not a proof count [2026-06-29]
## OUTCOME: cloud sizing measurement + aggregate tooling improvement. Four deterministic 1/64 shards from the exact R52 depth-10 frontier completed cleanly and show d10->d11 branching around 11 with no spectral/local pruning yet.

COMMANDS RUN (one foreground shard at a time):
 - `python s3_slice_harness.py --slice --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --shard-index 0 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --stats-out scratchpad\r3_d10_to_d11_shard64_00_stats_r53.json`
 - same for shard indexes 1, 2, 3.

SHARD RESULTS (exact within each loaded shard):
 - shard 0: 663 depth-10 parents -> 7818 depth-11 children, branching 11.792, wall 53.56s.
 - shard 1: 663 -> 7260, branching 10.950, wall 54.46s.
 - shard 2: 663 -> 6930, branching 10.452, wall 53.87s.
 - shard 3: 663 -> 7159, branching 10.798, wall 54.14s.
 - combined pilot: 2652/42430 depth-10 parents covered (6.2503%), 29167 depth-11 children, weighted
   branching 29167/2652 = 10.997. No local/spectral/triangle prunes fired in any pilot shard.

AGGREGATE TOOLING IMPROVEMENT:
 - `s3_aggregate_shards.py` now includes diagnostic coverage fields for incomplete shard sets:
   `loaded_shard_indexes`, `loaded_parent_count`, `source_parent_count`, `parent_coverage_fraction`,
   and per-depth `diagnostic_scaled_estimate_by_parent_coverage`.
 - Rerun:
   `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_03_aggregate_r53.json`
   produced diagnostic rows only:
      depth 10: aggregate 2652, scaled-est 42430.0.
      depth 11: aggregate 29167, scaled-est 466650.0.
 - Exact-mode regression check:
   `python s3_aggregate_shards.py scratchpad\r3_frontier_d10_stats_r52.json --expect 9=5311 --expect 10=42430 --out scratchpad\r3_frontier_d10_aggregate_r53_recheck.json`
   passed and still marks depths 9 and 10 exact.

HONEST INTERPRETATION:
 - The scaled `N11 ~ 4.67e5` is a sizing estimate from deterministic first-four shards, NOT a certified
   full count and NOT a proof fact. It is useful for cloud planning: a 64-way parallel d10->d11 run should
   have per-worker wall time around a minute on this local machine for these first shards, with around
   7k-8k depth-11 children per shard.
 - To certify exact `N11`, run all 64 shard indexes 0..63 from `scratchpad\r3_frontier_d10_r52.jsonl`
   with `--stats-out`, then aggregate without `--allow-incomplete`. Only then may the depth-11 row be
   read as exact.
 - The mathematical situation is unchanged: no spectral bite by depth 11; the branch is still expanding
   before the expected k~34-45 gate regime.

NEXT ACTION: either complete all 64 d10->d11 shards to certify exact `N11`, or if the goal is deep
spectral-bite measurement rather than exact shallow counts, move the exact R50/R52 generator to a faster
nauty/Traces/C backend and require the R49/R53 aggregate transcript as the acceptance oracle.

---

## R52 -- chainable full-resume frontier metadata fixed; exact depth-10 count measured [2026-06-29]
## OUTCOME: new exact measurement + cloud workflow repair. The R50/R51 depth-9 frontier was extended to a complete depth-10 frontier; `N10=42430` is now aggregate-proven exact.

BUG/WORKFLOW ISSUE FOUND:
 - `--frontier-out` from any `--frontier-in` run used to set `frontier_complete=false` unconditionally.
   That was conservative for true shards, but wrong for a full-scope resume with `--shard-count 1` from a
   complete source frontier. It prevented chaining complete frontiers without manual reinterpretation.

FIX IMPLEMENTED:
 - `frontier_complete` is now true for a resumed output iff:
   source frontier metadata says `frontier_complete=true`,
   `--shard-count 1`, and the new run itself has no sampled-level incompleteness.
 - Added metadata fields:
   `frontier_complete_for_loaded_scope` and `source_frontier_complete`.
 - True shard outputs (`--shard-count N>1`) remain non-global; they must still be aggregated.

VALIDATION:
 - Small metadata test:
   `python s3_slice_harness.py --slice --frontier-in scratchpad\r3_frontier_d5_test.jsonl --shard-count 1 --shard-index 0 --target-depth 6 --node-budget 2000 --time-cap 30 --level-cap 10000 --frontier-out scratchpad\r3_frontier_d6_full_resume_meta_test.jsonl --stats-out scratchpad\r3_d6_full_resume_meta_test.json`
   wrote a header with `frontier_complete=true`, `frontier_complete_for_loaded_scope=true`,
   `source_frontier_complete=true`, and aggregate expectations passed: 5=21, 6=62.
 - Exact depth-10 continuation:
   `python s3_slice_harness.py --slice --frontier-in scratchpad\r3_frontier_d9_r50.jsonl --shard-count 1 --shard-index 0 --target-depth 10 --node-budget 100000 --time-cap 300 --level-cap 100000 --frontier-out scratchpad\r3_frontier_d10_r52.jsonl --stats-out scratchpad\r3_frontier_d10_stats_r52.json`
   completed in 181.47s wall, wrote 42430 depth-10 reps, and header says `frontier_complete=true`.
 - Aggregate proof:
   `python s3_aggregate_shards.py scratchpad\r3_frontier_d10_stats_r52.json --expect 9=5311 --expect 10=42430 --out scratchpad\r3_frontier_d10_aggregate_r52.json`
   passed; aggregate marks depths 9 and 10 exact.

MEASURED FACTS:
 - Exact `N9=5311`, exact `N10=42430`.
 - Branching from depth 9 to 10: `42430 / 5311 = 7.989`.
 - R50 owner-cache hits during the d9->d10 step: 262936.
 - No local/spectral/triangle prunes fired yet at depth 10.
 - The older sampled/local note around ~41k was not a certified full `N10`; the full count is 42430.

VERDICT: accepted. This is the first exact extension beyond the R47/R51 depth-9 prefix and gives a
chainable complete depth-10 frontier for future sharded continuations. It still does not touch the deep
k~34 spectral-bite regime and does not solve srg99.

NEXT ACTION: do not try full unsharded d10->d11 locally unless prepared for a much larger run. Use
`scratchpad\r3_frontier_d10_r52.jsonl` as the source for sharded smoke/measurement, or port the exact
R50 owner-cache generator to nauty/Traces/C if Python shards cannot move exact depths materially closer
to k~34.

---

## R51 -- R50-optimized complete depth-9 frontier regenerated with JSON proof record [2026-06-29]
## OUTCOME: runnable cloud experiment artifact. The current optimized harness has a complete depth-9 prefix frontier and aggregate-verified stats.

COMMAND RUN:
`python s3_slice_harness.py --slice --target-depth 9 --node-budget 20000 --time-cap 120 --level-cap 10000 --frontier-out scratchpad\r3_frontier_d9_r50.jsonl --stats-out scratchpad\r3_frontier_d9_stats_r50.json`

RESULTS:
 - exact clean counts: `N1..N9 = 1,2,4,9,21,62,208,916,5311`.
 - wall time: 20.22s.
 - wrote complete depth-9 frontier: `scratchpad\r3_frontier_d9_r50.jsonl`, 5311 reps, `frontier_complete=True`.
 - wrote stats JSON: `scratchpad\r3_frontier_d9_stats_r50.json`.
 - R50 owner-cache instrumentation: `canonical_parent_cache_hit=37055`.
 - no local/spectral/triangle prunes yet: `pruned_local=0`, `pruned_spectral=0`, `pruned_triangle_split=0`.
 - shallow projection unchanged from R47: Stage-A total ~4.68e20; still only a shallow pre-spectral
   extrapolation, not a feasibility verdict.

AGGREGATE PROOF:
`python s3_aggregate_shards.py scratchpad\r3_frontier_d9_stats_r50.json --expect 1=1 --expect 2=2 --expect 3=4 --expect 4=9 --expect 5=21 --expect 6=62 --expect 7=208 --expect 8=916 --expect 9=5311 --out scratchpad\r3_frontier_d9_aggregate_r50.json`
passed and marked all depths exact.

VERDICT: accepted cloud-ready prefix artifact. This still does not solve srg99 and does not measure the
deep k~34-45 spectral collapse; it gives a current exact R50/R49 starting frontier for distributed
workers.

NEXT ACTION: launch distributed continuations from `scratchpad\r3_frontier_d9_r50.jsonl` with
`--stats-out shard_i.json`, aggregate with `s3_aggregate_shards.py`, and push exact depths as far toward
k~34 as Python allows before deciding whether to port the exact generator to nauty/Traces/C.

---

## R50 -- canonical-parent ownership cache/reorder; exact counts preserved, small-run wall time improves [2026-06-29]
## OUTCOME: search-cost reduction without changing predicates. The generator now avoids repeated BLISS deletion work for child graphs already seen or already owner-classified.

SCAMPER LEVER: Eliminate/Rearrange. R48 made canonical-parent ownership exact but expensive: for each
candidate child, the old order computed all vertex-deleted parent canonical keys before checking whether
the child was an isomorphic duplicate already seen at that level. The safe reorder is:
  1. compute the child BLISS canonical key;
  2. if the key is already accepted in this level, count `iso_dups` and skip ownership;
  3. otherwise look up or compute the child's canonical-parent owner key;
  4. accept only if that owner equals the current parent key.
The owner key is invariant over child isomorphism class, so caching by child canonical key is exact.

IMPLEMENTED:
 - `generate_stageA` now uses a per-level `owner_cache: child_canon_key -> canonical_parent_key`.
 - Added `canonical_parent_cache_hit` to run stats and aggregate sums.
 - No pruning/generation predicate changed; only the evaluation order and memoization changed.

VALIDATION (real commands run):
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py` passed.
 - `python s3_slice_harness.py --gate` still ALL GREEN after the generator edit.
 - Root exact counts:
   `python s3_slice_harness.py --slice --target-depth 7 --node-budget 5000 --time-cap 30 --level-cap 10000 --stats-out scratchpad\r3_root_d7_stats_r50.json`
   followed by aggregate expectations reproduced exactly `1,2,4,9,21,62,208`.
 - Deeper root exact count:
   `python s3_slice_harness.py --slice --target-depth 8 --node-budget 5000 --time-cap 30 --level-cap 10000 --stats-out scratchpad\r3_root_d8_stats_r50.json`
   reproduced exactly `N1..N8=1,2,4,9,21,62,208,916`; aggregate expectations passed.
 - R48/R49 two-shard recombination remains exact:
   optimized shard 0 from depth-5 frontier: 5=11, 6=39, 7=125.
   optimized shard 1: 5=10, 6=23, 7=83.
   aggregate expectations passed: 5=21, 6=62, 7=208.

MEASURED SMALL-RUN IMPACT (not a deep-cloud claim):
 - root depth 7 wall: previous R49 stats path 0.59s; R50 path 0.40s.
 - depth-5 shard 0 to depth 7: previous 0.37s; R50 0.24s.
 - depth-5 shard 1 to depth 7: previous 0.21s; R50 0.15s.
 - root depth 8 R50: wall 2.48s with `canonical_parent_cache_hit=5710`.
Stats counters changed as expected because duplicate children can now be classified before ownership;
the invariant counts and exact aggregate rows are unchanged.

VERDICT: safe accepted cost-reduction. It does not change the mathematical search space or solve srg99,
but it removes redundant canonical-parent BLISS deletion work from the exact distributed generator.

NEXT ACTION: use the R50-optimized R48/R49 cloud workflow. If exact depths still do not approach the
k~34 spectral-bite regime in Python, port this exact owner-cache order plus the same gates to a
nauty/Traces/C engine and require the R49 aggregate expectations as the port acceptance oracle.

---

## R49 -- shard stats JSON + strict aggregate checker; cloud measurement no longer depends on log scraping [2026-06-29]
## OUTCOME: runnable cloud experiment improvement + validation strengthening. Per-worker r=3 slices now emit auditable JSON, and a combiner refuses unsafe/mixed shard sets.

IMPLEMENTED:
 - `s3_slice_harness.py --stats-out PATH` writes a machine-readable `r3_slice_stats_v1` record for
   root or frontier-shard slices. The record includes parameters, node counts by depth, sampled-level
   flags, clean branching metrics, prune counters, completed count, source frontier metadata, and the
   source frontier SHA-256 when `--frontier-in` is used.
 - New `s3_aggregate_shards.py` aggregates `--stats-out` JSON files. It rejects seeded diagnostic
   slices, mixed target depths, mixed shard counts, duplicate shard indexes, missing shards unless
   `--allow-incomplete`, mixed source frontier hashes, and pre-R48 frontier metadata that does not
   declare `canonical_parent=true`.
 - The aggregate output marks each depth as `exact` only when all shards are present, the source
   frontier was complete, and no sampled parent level precedes that depth. This prevents sampled
   continuations from being reported as full `N_d`.

VALIDATION (real commands run):
 - `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py` passed.
 - `python s3_slice_harness.py --gate` still ALL GREEN: rook(9) all 9! local orders accepted, 0/511
   spectral rejects, triangle identity over all 512 rook subsets, and T(7) CRS/CSP reconstruction exact
   with 0 false rejects over 5242 induced subgraphs.
 - Root JSON path:
   `python s3_slice_harness.py --slice --target-depth 7 --node-budget 5000 --time-cap 30 --level-cap 10000 --stats-out scratchpad\r3_root_d7_stats.json`
   then
   `python s3_aggregate_shards.py scratchpad\r3_root_d7_stats.json --expect 1=1 --expect 2=2 --expect 3=4 --expect 4=9 --expect 5=21 --expect 6=62 --expect 7=208 --out scratchpad\r3_root_d7_aggregate.json`
   passed and marked all depths exact.
 - R48 shard recombination proof, now from JSON instead of text logs:
   shard 0 from the complete depth-5 frontier produced depth counts 5=11, 6=39, 7=125.
   shard 1 produced 5=10, 6=23, 7=83.
   `python s3_aggregate_shards.py --glob "scratchpad\r3_shard_d5_to_d7_*.json" --expect 5=21 --expect 6=62 --expect 7=208 --out scratchpad\r3_aggregate_d5_to_d7.json`
   passed. The aggregate JSON records `complete_shard_set=true`, `source_frontier_complete=true`,
   source SHA-256 `5f4ed0a21e05dc2fcf1a11104ea363be1b349f2ef2a91104ae4f57873ac07a4c`, and exact
   depths 5,6,7.

VERDICT: this does not reduce the mathematical search tree and does not solve srg99. It does materially
reduce cloud-run risk: exact per-shard counts and prune histograms can now be combined reproducibly,
with the previous naive-sharding failure mode guarded by metadata and exact-count flags.

NEXT ACTION: run the R48/R49 distributed measurement from a complete prefix frontier:
  1. `python .work/99graph/s3_slice_harness.py --slice --target-depth 9 --node-budget 20000 --time-cap 3600 --level-cap 10000 --frontier-out r3_frontier_d9.jsonl --stats-out r3_frontier_d9_stats.json`
  2. for worker `i=0..N-1`:
     `python .work/99graph/s3_slice_harness.py --slice --frontier-in r3_frontier_d9.jsonl --shard-count N --shard-index i --node-budget 200000000 --time-cap 86400 --target-depth 45 --level-cap 2000000 --stats-out shard_i.json`
  3. `python .work/99graph/s3_aggregate_shards.py --glob "shard_*.json" --out aggregate.json`
  Read only depths marked `exact` as measured `N_d`; if Python cannot push exact depths toward k~34,
  port the same gates to nauty/Traces/C and use this JSON aggregate as the acceptance oracle.

---

## R48 -- exact distributed frontier/shard mode implemented; naive sharding bug found and fixed with canonical-parent ownership [2026-06-29]
## OUTCOME: runnable cloud experiment improvement. The r=3 harness can now save a complete prefix frontier and resume deterministic shards without cross-shard isomorph double-counting.

GROUND TRUTH BUG FOUND: naive modulo sharding of a saved depth-5 frontier is NOT exact for the old
levelwise-BLISS generator. Expanding two shards independently to depth 6 produced 58+54=112 child reps,
while the true complete global depth-6 count is 62. Cause: different depth-5 parents can generate
isomorphic depth-6 children, and only a global dedup pass used to remove them.

FIX IMPLEMENTED:
 - JSONL frontier save/load:
   `--frontier-out PATH` writes retained `PartialGraph` reps plus metadata.
   `--frontier-in PATH --shard-count N --shard-index i` loads a deterministic modulo shard.
 - canonical-parent ownership rule: for each child, compute all vertex-deleted parent canonical BLISS
   keys and accept the child only from the lexicographically least parent key. This makes prefix shards
   disjoint without a cross-worker global dedup pass.
 - stats now expose `canonical_parent_reject`.

VALIDATION (all real commands run):
 - Direct complete run through depth 7 still gives the known counts:
   N1..N7 = 1,2,4,9,21,62,208. So canonical-parent ownership does not lose isomorphism classes.
 - Saved complete depth-5 frontier:
   `python s3_slice_harness.py --slice --target-depth 5 --node-budget 2000 --time-cap 30 --level-cap 10000 --frontier-out scratchpad\r3_frontier_d5_test.jsonl`
   wrote 21 depth-5 reps, complete=True.
 - Full resume from that frontier to depth 7 reproduces exact global continuation:
   depth 5=21, depth 6=62, depth 7=208.
 - Two-shard recombination after fix:
   depth 6: shard0=39, shard1=23, sum=62.
   depth 7: shard0=125, shard1=83, sum=208.
   This directly proves the shard ownership rule over a two-level continuation.
 - Saved complete depth-9 frontier:
   `python s3_slice_harness.py --slice --target-depth 9 --node-budget 20000 --time-cap 60 --level-cap 10000 --frontier-out scratchpad\r3_frontier_d9_test.jsonl`
   wrote 5311 depth-9 reps, complete=True. Counts unchanged: N1..N9=1,2,4,9,21,62,208,916,5311.

VERDICT: the cloud/distributed thin slice is now materially more reproducible. A worker can own a shard
of a saved complete prefix frontier and continue exact canonical augmentation without cross-shard
duplicate pollution. This does not solve srg99; it reduces the risk/cost of measuring the deep prune.

NEXT ACTION: use the exact two-stage cloud workflow:
  1. Generate a complete prefix frontier (depth 9 is locally verified; deeper prefix if a single node can
     complete it).
  2. Launch N workers with `--frontier-in ... --shard-count N --shard-index i --target-depth 45`.
  3. Sum per-shard counts by depth only for shards generated under the canonical-parent rule; do not use
     older pre-R48 frontier/shard files for exact totals.

---

## R47 -- deeper local unseeded measurement reaches complete depth 9; shallow branching rises, still no spectral bite [2026-06-29]
## OUTCOME: measured evidence. Larger local slice gives a better shallow anchor but confirms the decisive question is still deep k~34-46.

COMMAND RUN:
`python s3_slice_harness.py --slice --node-budget 150000 --time-cap 120 --target-depth 12 --level-cap 2000`

RESULTS:
 - complete iso-free counts through depth 9:
   N1..N9 = 1,2,4,9,21,62,208,916,5311.
 - clean branching geomean b=2.922; deepest clean children/node at depth 8 -> 9 is 5.798.
 - level cap is applied after the complete depth-9 count; depths 10-11 are sampled-frontier counts
   (41,427 and 182,954), not full N_d values.
 - no local lower/triangle-split, spectral, or terminal triangle-split pruning fired at these shallow
   depths (`pruned_local=0`, `pruned_spectral=0`, `pruned_triangle_split=0`).
 - shallow projection from depth 9 gives total Stage-A N_A ~ 4.68e20, larger than the depth-8 anchor
   because the shallow branching is still rising. This is NOT a final feasibility estimate; it is the
   unpruned pre-spectral regime.

RUN CAVEAT: `--time-cap` is a soft between-level cap to preserve complete level counts; the 120s run
finished its current level and took 173.6s wall before reporting `time_hit=True`. The script help/output
now says "soft-between-levels" explicitly.

VERDICT: better measurement, no kill. The current evidence makes single-node Python exploration to the
deep spectral bite unlikely; the cloud/C-port plan is still necessary. Any decisive run must either push
complete/split frontiers toward k~34 or port the exact gates to a faster nauty/Traces/C engine.

---

## R46 -- r=3 terminal triangle-split gate implemented + real-witness identity validation [2026-06-29]
## OUTCOME: strengthened correctness/pruning. Adds a hard 45-vtx terminal edge/triangle feasibility gate to s3_slice_harness.py; no shallow N_A change.

DERIVATION (exact counting, lambda=1): for a 45-vtx r=3 star complement H' in a hypothetical
srg(99,14,1,2), let e=e(H') and t=#triangles wholly in H'. Splitting the 231 host triangles by how many
vertices lie in H' gives:
  T2 = e - 3t,
  T1 = 315 - 2e + 3t,
  T0 = e - t - 84.
All are counts of real triangle classes and must be nonnegative. In particular e >= 84. This is the
45-vtx version of the R30 triangle-split polytope and was described in the spec but not enforced by R44.

IMPLEMENTED:
 - `EHP_MIN=84`.
 - safe partial triangle-aware feasibility prune: maintain current triangle count t incrementally and
   reject only if even the maximum possible future edge count cannot make some final (e_f,t_f) satisfy
   t_f>=t, t_f<=e_f/3, and t_f<=e_f-84. This intentionally ignores upper bounds on future triangle
   creation, so it can under-prune but cannot over-prune.
 - terminal exact gate at k=45: require `e-3t >= 0`, `315-2e+3t >= 0`, and `e-t-84 >= 0`.
 - stats now report `pruned_triangle_split` separately.

VALIDATION:
 - `python s3_slice_harness.py --gate` -> ALL GREEN. New controls: the incremental triangle counter
   matches exact rook(9) triangle count (t=6), and the generic triangle-split formulas match the actual
   split on all 512 vertex subsets of rook(9)=srg(9,4,1,2).
 - T(7) r=3 CRS gate remains green: exact diag/compat/closure, backtrack and cadical195 clique size 6,
   and 0 spectral false-rejects over 5242 T(7) induced subgraphs.
 - repaired unseeded slice unchanged through depth 10; `pruned_triangle_split=0` at shallow depth, as
   expected because e>=84 is a near-leaf/terminal feasibility predicate.

VERDICT: safe, cheap terminal strengthening; not a deep-prune solution. It closes a spec/code gap and
prevents terminal 45-vtx candidates with impossible triangle split from entering Stage B. The decisive
cost question remains the deep spectral collapse at k~34-46.

---

## R45 -- R44 HARNESS REPAIR: forced-triangle seed was UNSOUND for decisive cloud measurement; default is now UNSEEDED + local real-witness replay gate [2026-06-29]
## OUTCOME: correctness repair + measurement. s3_slice_harness.py now has a sound default root; `--seed-triangle` is diagnostic only. NO KILL; deep prune still unmeasured.

GROUND TRUTH FOUND BY INSPECTION: the R44 harness started Stage-A from a forced triangle. That is NOT a
proved property of every possible 45-vtx r=3 star complement H'. A valid H' could in principle have no
internal triangle, so the old cloud slice would have measured only the triangle-containing subsearch.
Treat the old b~3.7 number as a DIAGNOSTIC seeded subslice, not as the decisive N_A measurement.

REPAIR MADE:
 - `generate_stageA(..., seed_triangle=False)` is now the default. `--seed-triangle` remains available
   only for diagnostic comparison.
 - `--gate` now validates the actual local generation predicates, not just the r=3 CRS equations:
   rook(9)=srg(9,4,1,2) replay through `PartialGraph.can_add` accepts ALL 9! vertex orders
   (362,880/362,880). Since every ordered induced subgraph is a prefix of some full order, this is an
   exact no-overprune replay for the local F1-F6 predicates on a real lambda=1,mu=2 witness.
 - `--gate` also checks the srg99 r=3 spectral gates on all 511 nonempty rook(9) induced subgraphs:
   0/511 rejected. The T(7)=L(K_7) r=3 CRS reconstruction remains green: diag/compat/closure exact,
   blind column search 735 columns recovers all 6 true columns, backtrack clique size 6, cadical195 SAT
   size 6 closes 0/1, and G-a/G-b have 0 false-reject over 5242 real T(7) induced subgraphs.
 - Stage-B demo messaging repaired: shallow generated partials may have 0 diagonal-valid columns; that is
   now reported honestly. Full clique/SAT coverage is supplied by `--gate` on the real T(7) witness.

MEASURED AFTER REPAIR (real commands run green):
 - `python -m py_compile s3_slice_harness.py`
 - `python s3_slice_harness.py --gate` -> ALL GREEN (17.3s)
 - `python s3_slice_harness.py` -> ALL GREEN default one-command path (gate + repaired unseeded slice, 37s)
 - `python s3_slice_harness.py --slice --node-budget 20000 --time-cap 25 --target-depth 11 --level-cap 400`
   from the UNSEEDED root:
      depths 1..8 complete iso-free counts = 1,2,4,9,21,62,208,916
      clean branching geomean b=2.649; deepest clean children/node at depth 7 = 4.404
      level cap hit after the complete depth-8 count; depths 9-10 are sampled-frontier counts, not full N_d
      shallow projection from depth 8: total Stage-A N_A ~ 6.66e18 (LARGE), explicitly not final because G-a/G-b bite
      only at deep k~34-46.
 - `python s3_slice_harness.py --stageb-demo --target-depth 11 --node-budget 20000 --time-cap 25`
   -> generated 11-vtx H' had det(A-3I)=14384 and 0 diagonal-valid columns; honest smoke only.

UPDATED VERDICT: the r=3 harness is now correctness-sound as a measurement instrument. The decisive
cloud command is one-command runnable and MUST be run WITHOUT `--seed-triangle`. The honest readiness
verdict is still: ready to measure deep prune, NOT ready to claim feasibility/nonexistence. The current
unseeded shallow data says the unpruned tree is enormous; only a depth-45 cloud/distributed run can reveal whether
the hereditary top/bottom spectral gates collapse it.

NEXT ACTION: run the repaired cloud command from the unseeded root:
`python .work/99graph/s3_slice_harness.py --gate` then
`python .work/99graph/s3_slice_harness.py --slice --node-budget 200000000 --time-cap 86400 --target-depth 45 --level-cap 2000000`.
Do NOT pass `--seed-triangle` for the decisive measurement. If the Python BLISS loop is too slow to reach
k>=34, port the exact same gates to nauty/Traces/C and require this `--gate` transcript before accepting
the port.

---

## R44 — TURNKEY r=3 THIN-SLICE HARNESS BUILT + SOUNDNESS-GATED; shallow branching b~3.7 MEASURED; deep prune is the cloud unknown [2026-06-29]
## OUTCOME: tooling/measurement — s3_slice_harness.py (one command); CLOUD_SPEC_SC.md §8 added (turnkey + cloud run cmd). NO KILL. Honest: shallow N_A LARGE; the decisive deep-gate prune at k>=34 is UNMEASURED (= the cloud job).

Script: .work/99graph/s3_slice_harness.py (numpy + igraph BLISS; pysat/cadical optional; sympy for exact
soundness). Runs green this iter. Built in ONE pass per the R43/§7 spec; light validation only.

WHAT WAS BUILT (the §3 thin-vertical-slice instrument for the r=3 / 45-vtx formulation):
 1. Stage-A LEVEL-COMPLETE canonical-augmentation generator: at each depth d hold the COMPLETE
    iso-free set, expand all, BLISS canonical_permutation dedup, record the TRUE iso-free N_d (=>
    honest residual branching b, unlike a budget-truncated DFS whose per-depth counts are artifacts).
    Local block F1-F6 baked into the extension (EXACT R37 online K4/diamond/K_{2,3} reject incl. the
    existing-pair re-check); spectral gates online G-b(#eig>3<=1=F8c'), G-a(lambda_min>=-4 PSD),
    G-c(mult_3<=45-k), edge band. Float eigh + EXACT integer-inertia (rational LDL, 2x2 pivots) fallback.
 2. Stage-B r=3 column CSP: M=A_{H'}-3I, P=M^{-1} exact; DIAGONAL b^T P b=-3; COMPAT b_u^T P b_v in
    {0,1}; clique target=star set; exact 0/1 closure A_X=3I+B^T P B. Backtrack clique + cadical SAT.
 3. bounded driver (--node-budget / --time-cap / --level-cap); --gate / --slice / --stageb-demo modes.

VALIDATION (the soundness gate, ALL GREEN, seconds): end-to-end reconstruction of the REAL r=3 graph
T(7)=L(K_7)=srg(21,10,5,4): DIAGONAL b^T P b=-3 on 6/6 true star columns; COMPAT == true A_X; CLOSURE
A_X=3I+B^T P B == true induced subgraph (exact 0/1); BLIND search 735 diagonal-valid columns, all 6 true
recovered; backtrack clique = 6 = star set; cadical195 SAT clique = 6 closes 0/1; Stage-A gates 0
false-reject over 5242 real induced subgraphs of T(7) (G-a, G-b both 0). Gates verified FIRING: K4 +
diamond rejected by the local reject; spectral gate fires 50/50 on random k=40 dens.25. => harness CORRECT.

MEASURED (tiny bounded srg99 r=3 slice, seconds): CLEAN-level residual branching b ~ 3.67 (range 3.7-5.1
over depths 4-8), consistent with the spec's R35 b~3-10 anchor. iso_dups high (BLISS doing real iso-rejection
work). HONEST FINDING: at shallow depth (k<=10) the local + spectral gates barely prune (pruned_local/
spectral ~0) -- they bite at k>=34-46 per §7.2, so the shallow b is the UNPRUNED local branching.
Naively extrapolating b~3.67 to depth 45 gives N_A ~ 1e23-1e40 (LARGE -- distributed-nauty scale).

CALIBRATED VERDICT (no bluff): the harness is turnkey and soundness-proven, and it CONFIRMS the r=3
machinery (CRS/gates/CSP) is correct on a real graph. But the SHALLOW slice does NOT show the tree
collapsing -- shallow branching alone keeps N_A astronomically large. Whether the search is single-node-
feasible hinges ENTIRELY on how hard the deep spectral gates (G-a/G-b, k>=34-46) prune mid-tree, which a
seconds-scale shallow run CANNOT measure. That deep-prune curve is exactly the §3 measurement the CLOUD
run must produce (§8 has the command). So: tooling/measurement progress + a sound instrument; NOT a
feasibility verdict and NOT a kill. The b^-10 structural win (45 vs 55) is real but is a RATIO -- it does
not make the absolute N_A small if the s=-4 baseline N_A is itself huge.

NEXT ACTION: run the §8 cloud command (`s3_slice_harness.py --slice --target-depth 45` on a 32+ core node,
big budget) to measure the b(depth) curve and find where the spectral gates start collapsing the tree --
the true N_A. If the python ms/node is too slow at depth 45, port the inner extension+BLISS+inertia loop
to nauty/Traces geng + C (re-run --gate against the C port to confirm soundness). Until the deep prune is
measured, do NOT quote a single N_A.

---

## R43 — CHEAPER STAGE-A: the r=3 (45-VERTEX) star complement BEATS the s=-4 (55-vtx) one by ~b^-10 (3-10 orders); CRS+gates re-derived and VALIDATED on a real r=3 graph [2026-06-29]
## OUTCOME: spec change — §7 added to CLOUD_SPEC_SC.md; RECOMMEND r=3 as PRIMARY Stage-A, s=-4 as calibrated fallback. NO KILL (still a cost-reduction to the open search).

Scripts (scratchpad/): s3_starcomp_assess.py, s3_pd_vs_psd_crux.py, s3_density_stageB.py. All LIGHT exact,
real-graph calibrated, run green this iter.

THE IDEA (assessed in ONE pass): the shipped cloud-spec generates 55-VTX star complements because it
uses the eigenvalue-(-4) SC (mult(-4)=44 => |H|=99-44=55). Eigenvalue 3 has mult 54, so ITS star
complement has |H'|=99-54=**45 vtx** (star set 54). Stage-A tree DEPTH = #vertices in the SC and tree
size ~ b^depth, so a 45-vtx Stage-A is ~ b^-10 the 55-vtx one — **3 to 10 ORDERS smaller** for residual
branching b in [3,10]. Stage A is the SINGLE dominant cost (N_A, §4d); Stage B is <1%. So this is the
biggest available win on the wall — larger than any R35-R42 online sound cut.

VERIFIED THIS ITER (all exact, real-graph):
 1. COUNTS + CRS for r=3. CRS works for ANY eigenvalue: A_X = mu*I + B^T(C - mu*I)^{-1} B. For r=3:
    **A_X = 3I + B^T(A_{H'} - 3I)^{-1} B**, diag = -mu = -3, offdiag in {0,1}, H' a 45-vtx induced
    subgraph with 3 NOT an eigenvalue, B is 45x54. VALIDATED EXACT (Fraction) on the REAL r=3 graph
    **T(7)=L(K_7)=srg(21,10,5,4)** (spectrum 10^1, 3^6, (-2)^14; eigenvalue 3 present): reconstructs the
    host EXACTLY on 150/150 sampled r=3 star-complement partitions, 0 mismatch. T(7) is the right
    calibrator because r=3 is its 2nd eigenvalue (10 then 3), as in srg99 (14 then 3) -> #eig>3=1 in both.
 2. STAGE-A GATES for the 45-vtx case (the load-bearing re-derivation):
    - LOCAL block F1-F6 (locally-7K2, lambda=1, mu=2, deg<=14, forbidden {K4,diamond,K_{2,3}}, R37 online
      forms): IDENTICAL — eigenvalue-AGNOSTIC, reuse VERBATIM. Edge band rescales via degree-sum identity
      14*45=630=2e(H')+e(X,H'). Real-SC density is the SAME (0.497 r=3 vs 0.503 s=-4 on 21-vtx calibrators)
      => residual branching b comparable; the depth drop dominates.
    - (G-a) lambda_min(H') >= -4 HEREDITARY but PSD only (not PD): srg99 has no eig < -4, but H' excludes
      eig 3 not -4, so -4 CAN be attained. Weaker than s=-4's F8b' (PD strict). **QUANTIFIED the loss
      (s3_pd_vs_psd_crux.py): the PD-vs-PSD gap = subgraphs attaining lambda_min==host_min, which is 0%
      mid-tree and only climbs to 100% at sizes >= star-complement size on BOTH real s=-4 graphs (rook9,
      Kneser) -> a LEAF phenomenon. So PD->PSD costs ~0 mid-tree prune.**
    - (G-b) #eig > 3 <= 1 = F8c' EXACTLY (top-of-spectrum host fact, eigenvalue-agnostic). Carries over;
      0 false-reject on 6842 real induced subgraphs of T(7).
    - (G-c) mult_3(H')=0 BY DEFINITION (replaces F7's lower schedule). F7 lived at k>=46, ABOVE the 45
      ceiling, so losing it costs the r=3 tree NOTHING it would have used. Hereditary window mult_3<=45-k.
 3. COST COMPARISON (honest): structural b^-10 (3-10 orders), local pruning IDENTICAL, top gate IDENTICAL,
    bottom gate weaker by ~0 mid-tree (measured), F7 loss costs 0 (out of range). => r=3 is MATERIALLY
    cheaper for Stage-A node count N_A, with no offsetting mid-tree pruning loss. Stage B is harder (54
    cols over-determine the 45-dim W0^perp -> a 54-clique vs 44) but is <1% of total and its W0 prefilter
    codim RISES 44->54 (stronger column cut).
 4. VALIDATION: real r=3 graph T(7); CRS exact 150/150; G-a/G-b 0 false-reject over 6842 real induced
    subgraphs; r=3 and s=-4 SC densities match. Predicates do NOT false-reject real subgraphs.

RECOMMENDATION (written into §7 of CLOUD_SPEC_SC.md): **switch the PRIMARY Stage-A to the r=3 45-vtx star
complement** (expected N_A reduction ~ b^-10). Keep the fully-gated s=-4 §1-§6 as the verified fallback /
cross-check. BEFORE scaling, re-run the §3 STEP-0 soundness gate for r=3 (reproduce T(7)'s 15-vtx r=3 star
complements + §7.0 reconstruction). HONEST CAVEAT: the r=3 Stage-A GENERATOR has not been run end-to-end on
a calibrator yet (only the CRS + gates are validated); the win is a strong structural prior + verified
machinery, not yet a measured N_A. CALIBRATED CONFIDENCE HIGH on the math (CRS/gates exact), MEDIUM-HIGH on
the b^-10 magnitude (depends on residual branching b, which the slice must measure for both formulations).

NEXT ACTION: run the §3 thin slice for the r=3 formulation (STEP 0 soundness on T(7) at 15-vtx, then
generate a few hundred 45-vtx H') and MEASURE N_A; compare to the s=-4 slice. Whichever is cheaper wins;
structural prior favors r=3.

---

## R31 — STAR-COMPLEMENT LATTICE LENS: L=A_H+4I PD integral, 7-eigenspace dim>=10 [2026-06-28]
## OUTCOME: tightened-constraint (mult_3(H) in [10,30]; two forced modular coranks); NO KILL.
Scripts (scratchpad/lat/): calib_find.py, calib_starcomp.py, calib_bvls_starcomp.py (REAL-graph
calibration), core_obstruction.py, even_lattice.py, lever_a2_rigor.py, lever_a2_bite.py,
f2_structured.py, lever_c_genus.py, lever_d_multdeg.py, lever_e_cubic.py, lever_f_charpoly.py,
lever_g_joint.py, lever_h_bellrowlinson.py, lever_i_local_recurrence.py.

LENS: L := A_H + 4I = Gram of a rank-55 integral PD lattice (diag 4, offdiag 0/1, lambda_min(H)>-4),
carrying a >=10-dim integer eigenspace at 7 (= A_H eigenspace at 3). Pursued lattice/integrality
obstructions. ALL load-bearing facts ground-truthed on real graphs with the relevant eigenvalue.

NEW / SHARPENED VERIFIED RESULTS (all exact):
 [L1] EVEN-LATTICE identity (verified rook9/Petersen): for every integer eigenvector w with
      A_H w = theta w,  2*sum_{edges}(w_i w_j) = theta*|w|^2. For theta=3 (ODD): forces |w|^2 EVEN.
      => the integer 3-eigenlattice W_Z (rank m>=10) is an EVEN sublattice of Z^55.
 [L2] TWO forced MODULAR CORANK bounds (p-saturation of W_Z; verified the principle
      corank_Fp(A-theta I) >= mult_theta on rook9 all p, BvLS p=2,7):
        corank_F2(A_H + I)  >= m >= 10   (3 ≡ 1 mod 2)
        corank_F7(A_H + 4I) >= m >= 10   (3 ≡ -4 mod 7)  [= the known 7^10|det(A_H+4I) / SNF fact,
        restated as rank_F7(A_H+4I) <= 45; SUBSUMED by the closed p-rank vein — NOT new].
 [L3] mult_3(H) = m in [10, 30] (NEW two-sided window). Lower 10 = interlacing (known).
      UPPER 30 = NEW: spectral-spread / Cauchy-Schwarz on the R=54-m eigenvalues in (-4,3):
      (theta_1+3m)^2 <= (54-m)(2e(H)-theta_1^2-9m) is INFEASIBLE for m>=31 (lever_d). Verified.
 [L4] ACHIEVABILITY split (lever_a2_bite/f2_structured/lever_g_joint): RANDOM and TRIANGLE-SPARSE
      55-vtx graphs essentially NEVER reach corank>=10 over F2 or F7 (0/40+ trials; typical corank
      0-2) => [L2] is a STRONG pruner of generic H. But STRUCTURED family graphs DO: rook9
      corank_F2(A+I)=4 on 9 vtx; BvLS corank_F2=corank_F7=110. So [L2] prunes hard but is
      CONSISTENT with the structured regime H must inhabit. Not a kill.
 [L5] Truncated-moment feasibility on (-4,3) with cubic trace + triangle-split window (lever_e):
      FEASIBLE across the whole (m,theta_1,e,t) box => spectral moments do NOT kill (re-confirms
      'parameters too well-behaved'; consistent with closed spectral route).

REAL-GRAPH CALIBRATION (task-required 'find a graph that HAS eigenvalue -4'):
 - K_{a x 4} complete multipartite (smallest eig -4, mult a-1): star complements give L=A_H+4I
   PD integral; SNF computed (det=4^k); machinery sound (calib_starcomp).
 - BvLS srg(243,22,1,2) star complement for s=-5 (|X|=110, H=133 vtx): L'=A_H+5I strictly PD
   (Cholesky OK, lambda_min=3.6e-5>0); interlacing-forced mult_4(H)=22 EXACTLY; corank_F2(A_H)=23>=22,
   corank_F7(A_H-4I)=22>=22. FULL lens calibrated on a genuine lambda=1,mu=2 family member.

CALIBRATED VERDICT: consistent / tightened-constraint, NO KILL. The integral-lattice lens yields a
clean unified package (even rank-m lattice + two modular coranks + m in [10,30]) and a strong
genericity pruner, but every invariant is integral/achievable in the structured regime the real
family graphs already inhabit. The forced spectral/lattice facts are the Cauchy window (closed
route); the genuinely-new yield is the UPPER bound m<=30 and the quantified genericity gap [L4].
No lattice/SNF/genus contradiction: det>0, 7^10|det is a factor-by-construction (cancels, R30),
W_Z even is consistent, glue/discriminant is unconstrained. Confidence HIGH (all exact, calibrated).

## R-FLATCOUNT/COUNTING (LENS: global counting/parity over-determination + global flat-count) [2026-06-28]

Scripts (all .work/99graph/, exact arithmetic, rook9/BvLS-calibrated):
global_flatcount.py, flat_positions.py, ball_first_flatcount.py, census_overdet.py,
identity_recheck.py, derive_identity.py, spectral_vs_n3.py, sc_clean_verify.py,
sc_interlace_verify.py, sc_det_bound.py, sc_triangle_coupling.py, sc_triangle_verify.py.

**(1) GROUND-TRUTH CORRECTION of a stated identity.** "3 n1 + n3 = (1/4)nk(k-2)" (n1 =
disjoint-triangle-pairs w/ 1 cross edge) is FALSE on both reals (BvLS LHS 721710 vs RHS 26730).
VERIFIED forced relation: **n3 + 3*nprism = (1/4)nk(k-2) = 4158** (rook9 0+3*6=18; BvLS
0+3*8910=26730). = (1/2)*#induced-P3. Consequence unchanged: 3|n3, n3 in [0,4158].

**(2) COUNTING SYSTEM — clean negative.** Full forced census (V,E,T=231,P2,C4,n3+3nprism=4158,
p6=209286+n3) as functions of free integer n3: NO parity/divisibility over-determination; n3
pinned ONLY to {3|n3, [0,4158]} (1387 values). Spectral moments Tr(A^m) n3-BLIND: forced==
measured on both reals m=2..7 though srg99 n3 is free (closed-walk=homomorphism=fixed poly in
params). No second handle on n3 from any moment <=7.

**(3) GLOBAL FLAT-COUNT = STAR COMPLEMENT.** Verified n-m_s flat-count: rook9=5, BvLS=133 over
many orderings; srg99 = 99-44 = 55 in ANY ordering. But 55 flats is a TAUTOLOGY (99 vectors in
R^44 always >=55 dependent), not a realizable constraint. The 55 flats = a STAR COMPLEMENT H
for s=-4, 44 pillars = STAR SET. Lift theorem governs FULL-BALL attachments; generic flats occur
on PARTIAL neighbourhoods (rook9 flat w/ 0 nbrs at prefix 2; BvLS earliest flat prefix 26) =>
lift restriction and global count live on different objects => NO local-to-global contradiction.

**(4) CRS SIGN CORRECTED (rook9+Petersen ground-truth).** Correct: A_X = mu I + B^T (C-mu I)^{-1}
B; diag b^T(C-mu I)^{-1}b = -mu (=+4 for srg99). All 81 rook9 star sets reconstruct EXACTLY. The
sc_* lane used (mu I - C) (opposite sign); quadratic-form det conclusions survive but fix sign.

**(5) 7^10 | det(C+4I) is NOT an over-determination.** mult_3(H)>=10 (interlacing, verified on
rook9 star complements) => 7^10 | det(C+4I). BUT B^T adj(C+4I) B = det(C+4I)*(A_X+4I) is auto
divisible by det(C+4I); 7^10 CANCELS both sides (verified M=det*(A_X-muI) on rook9). Honest
negative for the mod-7 route the sc lane flagged as a candidate obstruction.

**(6) NEW VERIFIED FORCED FACTS for any star complement H (= any 55 flat vertices).** The 231-
triangle split by #vertices-in-H satisfies a RANK-3 system (I_X auto-satisfied), parametrized by
e(H), t(H)=n_HHH:  n_HHX=e(H)-3t(H); n_HXX=385-2e(H)+3t(H); n_XXX=e(H)-t(H)-154. Nonnegativity
(verified exactly on rook9; Petersen lam=0 is the NEGATIVE control where the lam=1 identity
correctly fails) gives **e(H) in [154,384]** (was [77,385]: n_XXX>=0 => e>=154; e=385 corner
empty => e<=384), **e(X,H)=770-2e(H) in [2,462]** (was [0,616]), **t(H) in
[ceil((2e-385)/3), min(floor(e/3),e-154)]**. Spectral t(H) window (Tr(C^3)=6t(H)) = [0,700]
strictly CONTAINS the combinatorial one; 2nd-moment (Tr(C^2)=2e(H)) consistent for all theta_1
in [3,14], theta_1 not forced rational. So (6) is a constraint TIGHTENING, not a kill -- usable
as pruning for any star-complement/orbit-matrix search.

**NET (calibrated).** Both threads -> HONEST NEGATIVES on a kill + 1 bug fix (n3 identity) +
1 sign fix (CRS) + 1 closed tempting route (7^10 cancels) + 1 new tightened forced-fact set
(e(H) in [154,384], e(X,H) in [2,462], rank-3 triangle split). No contradiction; open.

---

## R24 — NEW CONSTRAINT: eigenspace-trace integrality + Burnside-on-triangles KILLS 2 of the 4 Z3/f=0 parity classes (a=20, a=22) by PURE ARITHMETIC (no enumeration) [2026-06-28]

Lens: exploit non-vertex-transitivity / tiny Aut POSITIVELY. Files (all .work/99graph/):
permchar_eigtrace.py (identity + validation), permchar_srg99.py (allowed-Aut bands),
permchar_z3_estructure.py (e=3T structure on reals), permchar_KILL.py (combined),
permchar_adversarial.py (9/9 gates), permchar_consistency.py (C1<->C2 bridge proof).

**THE IDENTITY (validated EXACTLY on 322 real automorphisms — 72 on rook9 r-s=3, 250 on
BvLS243 r-s=9; 0 integrality violations, 0 projector-trace mismatches).** For any g in
Aut, P=P_g commutes with A, so preserves each eigenspace. With t=#fixed vertices,
e=#{v:v~g(v)}=tr(PA), tau_r=tr(g|V_r), tau_s=tr(g|V_s):
   tau_r + tau_s = t-1 ;  3 tau_r - 4 tau_s = e-14 ;  tau_r,tau_s in Z (Galois-forced).
   => 7 tau_r = e+4t-18 ,  7 tau_s = -e+3t+11.  (2nd moment tr(PA^2) adds NOTHING — A^2
   is a Q-combo of I,A,J.) The leverage is the r-s=7 gap forcing 7 | (e+4t-18).

**SPECIALIZED TO Z3/f=0 (the sole surviving prime symmetry; t=0):**
 (i)  eigentrace: e ≡ 18 (mod 7); with mult bounds, after also e≡0(3) below => e in {18,39,60,81}.
 (ii) e = 3T where T = #triangle-orbits: PROVEN by g-equivariance (v~gv <=> gv~g^2v <=>
      g^2v~v, so each 3-cycle is empty or a full triangle; contributes 0 or 3 to e).
      EXHAUSTIVE proof on the 3-orbit + validated on reals (rook9 e=9,T=3; BvLS e=243,T=81).
 (iii) BURNSIDE on the 231 canonical triangles under <g>=Z3: #tri-orbits=(231+2T)/3 in Z,
      and 231≡0(3) => **T ≡ 0 (mod 3)**.  (A g-invariant triangle is one 3-orbit since g
      is fpf, so F=#invariant-triangles = T exactly — proven + validated.)
 => T in {6,13,20,27} (from i,ii)  ∩  {T≡0(3)}  =  **T in {6,27}**.

**THE KILL.** The prior 4 parity classes are a=24:(T27,E6) / a=22:(T20,E13) /
a=20:(T13,E20) / a=18:(T6,E27), where the prior class derivation (canon_backtrack.classes)
imposed ONLY a even (a=mult of +3 in the 33x33 quotient, a+b=32, T=(7a-114)/2). The
DEEP BRIDGE a=(54+2 tau_r)/3, b=(44+2 tau_s)/3 (dim of g-fixed subspace = char average;
verified exact on rook9 a=2 & BvLS a=60) ties C1<->C2 and shows: C1 (a even) keeps all of
T in {6,13,20,27}; the NEW Burnside step removes T in {13,20}. Hence:
   **classes a=20 (T=13) and a=22 (T=20) CANNOT host a Z3/f=0 automorphism — ELIMINATED
   with zero enumeration.**  Only a=24 (T=27) and a=18 (T=6) survive — the two EXTREME
   classes (max/min triangle-orbit count). This is consistent with (does not contradict)
   the row-by-row search wall, which is on a=24 (a survivor); it removes the two MIDDLE
   classes that search never reached.

**SCOPE / HONESTY.** This HALVES the open Z3/f=0 cell (4 classes -> 2) but does NOT close
it: a=24 and a=18 remain genuinely open (the row-by-row enumerator still walls on a=24).
It does NOT touch the trivial-Aut (rigid) case — for |Aut|=1 there is no g, so the
identity is vacuous (the eigentrace lens needs a nontrivial automorphism; a rigid srg99
is unconstrained by it). Order-2 involutions: the identity gives e ≡ 3t+4 (mod 7) but
t is odd and unconstrained mod 7, so 316 (t,e) bands survive — NO kill there. So the
new constraint is sharp ONLY for order-3 (and order-6 via g^2). Adversarial: 9/9 gates
(Galois integrality, exhaustive 0/3-edge lemma, invariant-triangle=orbit, Burnside
integrality, two-way e-band) PASS; both reals satisfy C1 & C2 as required.

REUSABLE: (a) the eigentrace 2x2 system 7 tau_r=e+4t-18, 7 tau_s=-e+3t+11 (any g);
(b) a=(54+2 tau_r)/3, b=(44+2 tau_s)/3 linking quotient mult <-> full-graph eigentrace;
(c) e=3T for fpf-Z3; (d) Burnside-on-231-triangles => T≡0(3) => only T in {6,27}.

---

## R18-VERIFY (FRESH-CONTEXT ADVERSARIAL, 2026-06-28) — R18 flat CONFIRMED exact+realizable; impact RE-FRAMED (breaks the kill's sole remaining gating premise, not just an "over-broad" sub-claim)

Independent verifier: indep_verify_r18.py (own cosines, own corrected LDL, own realizability
audit), probe_noflat_gap.py, indep_rank44_wall.py. Did NOT reuse attach_fast /
full_joint_flat_fast for the certify step.

**CONFIRMED (triple-independent).** The rank-34 seed-13 flat is REAL and EXACT:
  - Re-derived cos_adj=-2/7, cos_nonadj=1/28 from scratch (cross-checked rook9 -1/2,1/4).
  - Rebuilt the post-attach 43-vertex Gram from the raw adjacency with an INDEPENDENT
    fraction-LDL: rank 34 == parent rank 34, PSD => genuinely FLAT (not climb, not overflow).
  - INDEPENDENT realizability audit of the post-attach induced graph: lambda max-common=1
    (0 viol), mu max-common=2 (0 viol), eo=0 (all 3 blocks 2 non-matched picks), deg<=14,
    WFLAT non-adj to apex core, 0 UNK among the 42 placed. => a GENUINE realizable partial SRG.
  - Re-derived e^T K^{-1} e == 39/80 EXACT, |w_U|^2 == 41/80, perfect slot-partition.
  (NOTE: my first LDL pass had a self-inflicted bug — overlapping elimination loop gave rank 8;
  fixed and re-validated against the trusted LDL + sanity cases. The ENGINE was right.)

**THE RE-FRAMING (the load-bearing correction).** The executor frames the flat as falsifying
only an "OVER-BROAD" sub-claim while "the actual KILL is untouched." That UNDERSTATES it. Per
this very progress.md (lines 734, 773-774), "no-flat-step FORCED at EVERY realizable node rank
31..43" was THE SINGLE REMAINING GATING LINK to a kill (strict +1 climb => rank 44 by n<=52 =>
forced overflow). The rank-34 flat FALSIFIES that gating premise. Demonstrated directly
(probe_noflat_gap.py): at the seed-13 rank-34 node the R16 no-flat census
(noflat_forced.geom_classify_node) reports FLAT=0 — but it only tests the BALL-ONLY ALL-NON
shell coupling; the ww-COMPLETE test finds 2 flats (the R18 flat is combo (0,1,0), i.e. WFLAT
ADJ to a shell vertex, which the all-NON census structurally cannot see). So BOTH R16's
"no-flat-forced rank 31..43" AND the sweep_intermediate_noflat "FLAT=0 on every node" were
verified only in the ww-RESTRICTED form; the ww-COMPLETE premise is FALSE at rank 34. The
strict-climb-forcing bridge from "a rank-44 dead-end exists" to "nonexistence" is BROKEN.

**WHAT SURVIVES (independently re-confirmed).** The rank-44 WALL computation is still true: at
rank-44 nodes the trusted reference residual_incolspace.joint_flat_count gives 0 flat (seeds 1
& 7, ns=13, ~1962 types each, re-run here). A rank-44 dead-end (a realizable rank-44 partial
config with no realizable extension) remains a real, soundness-gated object. SOUNDNESS GATES
re-verified: srg85 5*K7 overflow rank35>dim34 FIRES (reproduced with my OWN LDL in the r=4
eigenspace, cos 2/7,-1/14); BvLS rank-110 node real-flat DETECTED (border in colspace,
reconstructed <w,w>==1). So the test is not blind and the wall null is meaningful.

**NET VERDICT.** R18's concrete finding is CONFIRMED (exact, realizable rank-34 flat) and is
GENUINE PROGRESS: it disproves the proposed kill's sole remaining premise (no-flat-forced at
every node). It is NOT a refutation of a *true* statement (the rank-44 wall is still 0-flat)
and does NOT construct srg(99,14,1,2). Calibrated framing: the kill program is now known to
FAIL via the strict-climb route — flats DO appear at intermediate rank (ww-complete), so a
hypothetical srg99 is not forced through a rank-44 overflow. The honest status of the whole
rank-overflow attack: the rank-44 dead-end is real but UN-BRIDGEABLE to nonexistence by the
no-flat-climb argument. The 99-graph existence question remains fully open.

---

## R18 (IN-BAND FALSIFICATION VEIN, 2026-06-28) — VERIFIED rank-34 in-colspace FLAT found; rank-44 wall still 0-flat

Scripts: inband_falsify.py, inband_fast.py (numpy screen + exact Fraction confirm, verified
identical to the trusted residual_incolspace.joint_flat_count), inband_denominator.py,
inband_reconfirm.py. Results: inband_fast_results.pkl. Soundness gates embedded + PASS.

**HEADLINE (calibrated, triple-verified).** Aggressively hunting a realizable FLAT among the
residual 5760 in-colspace types at in-band ("seed-7-type") nodes — where needed perp-norm
R2=39/80 lies INSIDE the achievable e^T K^{-1} e band so flat is blocked only by a lattice
non-hit — I FOUND a VERIFIED realizable in-colspace flat. It is at a **rank-34** node (ns=3,
n=42, identity ball, grow_seed=13), NOT at the rank-44 wall. Two flat types
(nbrs {A1,A10,B5,B11,C3,C8} and {A5,A12,B2,B10,C4,C7}, both ww-combo (0,1,0)). TRIPLE-confirmed:
  (1) my fast test: e^T K^{-1} e == 39/80 EXACT (Fraction), flat=2;
  (2) the TRUSTED reference residual_incolspace.joint_flat_count: SAME node -> flat=2 (so NOT a
      rewrite bug — the prior "0 flat at every node" only sampled seeds 1/7/99 at rank 34, which
      ARE flat-free; seed 13 is a different rank-34 node that is NOT);
  (3) the REAL propagator attach_fast: attaching the flat vertex with the exact ww-couplings ->
      ok=realizable, rank stays 34 (=flat), psd=True; AND an INDEPENDENT static ldl_rank_psd
      rebuild of the post-flat 43-vertex Gram = rank 34, PSD. The new vertex is a proper
      slot-partition in-colspace type (6 distinct slots) with mu<=2 to non-nbrs. => a GENUINE
      realizable in-colspace flat, no artifact.

**WHAT THIS FALSIFIES vs WHAT SURVIVES (precise).**
  - FALSIFIES the OVER-BROAD claim in R17(E)/residual_incolspace that "the in-colspace residual
    is flat-free at EVERY reachable rank 34..44." It is NOT: rank-34 seed-13 admits 2 flats.
    Across seeds at rank 34: seeds 1/7/23/42/99 -> 0 flat, seed 13 -> 2 flat (a node-dependent,
    sampling-sensitive phenomenon — exactly the fragility the in-band analysis predicted).
  - DOES NOT falsify the actual KILL. The kill is the rank-44 SATURATION-WALL no-flat (overflow
    only at a rank-44 node, per the RANK-44-ONLY lemma). A rank-34 flat keeps rank 34 — it is a
    vertex the partial graph absorbs WITHOUT overflow and far (10 ranks) below the wall. In this
    run ALL 6 rank-44 nodes tested (seeds 1,7,13,23,42,77) = 0 flat; ranks 37/40/42/43 = 0 flat;
    only rank 34 (ns=3, lowest, farthest from wall) produced flats, and only at seed 13.

**SWEEP NUMBERS (exact, this run).** 33 distinct high-rank nodes (rank_hist {44:6,43:6,42:6,
40:5,37:5,34:5}), identity ball, seeds 1..77. **93,399 in-colspace types tested exactly**; of
these **80,344 IN-BAND** (86% — the fragile case DOMINATES, not a rare canonical type). 6 float
near-hits within 1e-7; **2 EXACT flats** (the rank-34 seed-13 pair). Every other near-hit is an
exactly-NONZERO rational refuted by Fraction confirm: e.g. at id-t42-g7 a pattern with float gap
3.65e-8 has EXACT e^T K^{-1} e = 11088305693187/22745244150160, R2-q = -51876/1421577759385 != 0
(denominator carries det(K) primes 281,2539,56929 absent from 80=2^4*5). This is the exact
mechanism: an in-band 0-flat is a Diophantine non-hit; occasionally (seed 13, rank 34) the lattice
DOES hit -> a real flat. SOUNDNESS GATES PASS same run: BvLS rank-110 real flat reconstructed
<w,w>=1 (test CAN find flats); srg85 5*K7 rank35>dim34 fires.

**NET (calibrated).** The universal no-flat lemma as previously stated (flat-free at every
reachable rank) is FALSIFIED at intermediate rank 34. The KILL's load-bearing claim
(rank-44-wall flat-free) is UNBROKEN and reinforced (6/6 rank-44 nodes, 0 flat; ~12k rank-44
in-colspace types, 0 flat). Honest status: residual no-flat is a RANK-44-WALL phenomenon, NOT an
all-rank one; the kill must rest only on the wall, never on intermediate-rank no-flat. The
graph-existence question is untouched (a rank-34 flat does not build srg(99,14,1,2)).

---

## R17 (ANALYTIC NO-FLAT VEIN, 2026-06-28) — ball-infeasibility PROVEN universal; in-colspace residual flat-free on reachable chains

Scripts: analytic_noflat.py, kernel_structure.py, kernel_relation.py, colspace_conditions.py,
norm_condition.py, norm_closedform.py, lift_ballinfeas.py, lift_theorem.py,
residual_incolspace.py, separator_analysis.py, kernel_helpers.py.

**(A) EXACT kernel of the rank-31 ball Gram G_BB (dim44, left-null dim 8).** The 8-dim
ker(G_BB) has a fully STRUCTURAL basis (verified G z == 0 exactly, 0 mismatch):
  - 3 STAR vectors: star_X = 4·X + (other two apex) + Σ(block of X), one per apex a,b,c (S=18).
  - 6 TRIPLE vectors: triple_e = a+b+c + (matched pair e in A)+(in B)+(in C), e=1..6 (S=9).
  One linear relation: triple_1+…+triple_6 = star_a+star_b+star_c (so 9 vectors, rank 8).

**(B) EXACT colspace-membership criterion for a realizable (2,2,2)/eo=0 attachment b.**
b∈colspace(G_BB) ⇔ z·b=0 ∀z∈ker. With b_u = cna + (ca−cna)·1[u∈N], delta=ca−cna=−9/28,
the required value is W(z;N) = S(z)/9 (since −cna/delta = 1/9). STAR cond: W=2 = (#picks in
that block)=2 ALWAYS (auto-satisfied). TRIPLE cond (per matched-slot e): (#A-picks in slot e)+
(#B)+(#C) = 1. Since each block's 2 picks lie in 2 DISTINCT slots (eo=0), this forces: the
three slot-pairs (A,B,C) are pairwise DISJOINT and cover all 6 slots (a perfect slot-partition).
VERIFIED vs brute kernel-orth on all 216000 attachments: 0 mismatch. **5760 in colspace
(=the slot-partitions, = engine's "5760 realizable extensions"), 210240 ball-infeasible.**

**(C) The 5760 in-colspace attachments have reconstructed |w_U|² = 41/80 EXACTLY (all of
them, single value), < 1 ⇒ NOT flat at the ball — a strict +1 climb.** So no-flat at the
ball is PROVEN analytically: 210240 ball-infeasible (no unit vector) + 5760 norm 41/80<1
(perp needed → +1). ZERO flat single-extensions at the ball. (Reproduces engine's "5760 all
climb +1, 0 flat" by closed form.)

**(D) THE LIFT THEOREM — ball-infeasibility is NODE-INDEPENDENT (rigorous).** Because G_BB is
PSD rank 31, ker(G_BB) = exact vector-dependencies among the ball vectors g_j (z^T G_BB z =
‖Σ z_j g_j‖²). For ANY further unit vector w, z·b_ball = ⟨Σ z_j g_j, w⟩ = ⟨0,w⟩ = 0. So
b_ball ∈ colspace(G_BB) is NECESSARY at EVERY node containing the ball, regardless of how
large colspace(G_full) grows. ⇒ all 210240 ball-infeasible attachment TYPES are non-flat at
EVERY reachable node — UNIVERSALLY. VERIFIED: all 8 ball kernel vectors zero-extend into
ker(G_full) at grown nodes rank 34/37/40/44 (8/8); every actually-placed beyond-ball vertex
has ball-cosines ⟂ ker(G_BB) (104 checks, 0 violation). **This closes the dominant
(210240/216000 = 97.3%) mechanism of the universal no-flat lemma analytically.**

**(E) RESIDUAL (the honest remaining gap).** The 5760 in-colspace types are NOT killed by the
ball lift (their b_ball IS in colspace). For them flat needs reconstructed full-norm == 1:
|w_U|²=41/80 fixed (node-independent), so the shell must supply perp-norm exactly 39/80 while
hitting every shell cosine — the joint perp-Gram test. residual_incolspace.py runs this EXACT
test at grown nodes (residual_incolspace.py): rank 34/37/40/42/44/44 (seeds 1,7,99), in-colspace
types tested 4616/3637/2797/2233/1962/1963, **FLAT survivors = 0 at EVERY node** (exact
e^T K^{-1} e == R^2 over all 2^ns sign patterns; ns=3..13). At the rank-44 node these are exactly
the 1899 fell-back picks rank44_joint already resolved 0-flat. So the in-colspace residual is
flat-free on every reachable chain tested, but a NODE-INDEPENDENT proof for it (analog of the lift
theorem) is NOT in hand — the precise unproven link.

**(G) WHY the residual fails — node-DEPENDENT obstruction (residual_obstruction.py).** For an
in-colspace type |w_U|^2=41/80 is node-independent => needed perp-norm R^2=39/80=0.4875 always.
But achievable perp-norm e^T K^{-1} e depends on the node's shell perp-Gram K. At 3 rank-42/44
nodes: seed1 min=0.5104 > 0.4875 (clean BOUND obstruction: perp can't be short enough); seed99
min=1.556 > 0.4875 (BOUND, stronger); seed7 0.4875 in [0.4014,41.06] band but NO exact integer
target hits it (gap 0.011 — DIOPHANTINE/lattice miss). => the residual no-flat holds at every
tested node but has NO single uniform analytic criterion: at some nodes a norm inequality, at
others a lattice non-hit. This is exactly why the residual resists a node-independent proof — the
honest boundary of the analytic vein.

**INDEPENDENT COUNT CHECK.** In-colspace count is closed-form: slot-partition = 6!/(2^3)=90
ordered slot-pairings x 2^6=64 within-slot vertex choices = **5760**, matching the brute kernel
count exactly (combinatorics = linear algebra). The colspace criterion is triple-verified (brute
kernel-orth on all 216000 attachments, the structural slot condition, and the closed-form count).

**(F) SEPARATOR srg99 vs BvLS — CORRECTED.** At the identity-ball distance-2 attachment BOTH
are climbers: srg99 |w_U|²=41/80, **BvLS |w_U|²=17/44**, both <1 (norm_closedform.py, exact,
kernel-orth verified). So ball-level no-flat is GENERIC to srg(·,k,1,2), NOT the separator.
The real separator is the GLOBAL squeeze ratio ball_rank/dim_s: srg99 = 31/44 = 0.705 vs BvLS
= 60/110 = 0.545 (dim_s = mult(s) = 44 / 110; both ds/v ≈ 0.45). srg99's ball already fills
0.705 of the eigenspace, so the strict +1 climb hits rank=dim_s=44 at n≈52 ≪ 99 (overflow
wall) while BvLS (0.545) leaves room and its real geometry fills the rest with flats to 243.
The separation is NOT a local cosine determinant — it is dim_s small + ball at 0.705 + strict
+1 climb ⇒ full-rank dead-end at n≪v for srg99 only.
SOUNDNESS GATE PASS: the SAME colspace+norm flat-test detects the REAL BvLS rank-110 flat
exactly (joint_reals_gate.py: border in colspace, reconstructed ⟨w,w⟩=1). No blind spot.

---

## CERTAIN facts (machine-verified in feasibility.py — re-run to confirm)

Parameters v=99, k=14, λ=1, μ=2.
- Eigenvalues: k=14 (mult 1), **r=3 (mult f=54)**, **s=−4 (mult g=44)**.
- Passes ALL standard necessary conditions: counting identity, integral
  multiplicities, trace, Krein-1/2, absolute bound. ⇒ feasible, existence open.
- **Local structure (locally linear):** N(v) induces 7·K₂ (a perfect matching on
  the 14 neighbours). Every edge lies in exactly 1 triangle.
- 693 edges, **231 triangles** that *partition* the edge set (3·231=693); each
  vertex lies in exactly 7 triangles. ⇒ the graph is the collinearity graph of a
  partial linear space: 99 points, 231 lines (triples), 7 lines/point, two points
  on ≤1 line, adjacent points on exactly 1 line.
- Second-neighbourhood balance: each of the 84 non-neighbours of v has exactly
  μ=2 neighbours in N(v); edges N(v)→2nd-nbhd = 14·12 = 168 = 84·2. ✓

### The full λ=1, μ=2 family (5 feasible sets; finiteness is classical)
| v | k | status |
|---|---|--------|
| 9 | 4 | **EXISTS** — 3×3 rook / Paley(9) |
| **99** | **14** | **OPEN** ← smallest unknown (this problem) |
| 243 | 22 | **EXISTS** — Berlekamp–van Lint–Seidel |
| 6273 | 112 | OPEN |
| 494019 | 994 | OPEN |

---

## KNOWN constraints from the literature (cited; treat as given, do not re-derive)

1. **Not vertex-transitive** — if it exists, no automorphism group is transitive on
   vertices. (classical; Wikipedia)
2. **Makhnev & Minakova (2004):** |Aut(G)| divides 2·3³·7·11 = 4158. If |Aut(G)| is
   even, it divides 42. ⇒ only primes 2,3,7,11 can divide |Aut(G)|.
3. **Behbahani & Lam (2011):** computational orbit-matrix search ruling out various
   automorphism orders (prime orders). No automorphism of order p>14 (p prime); no
   order 13; order-11 case forces 9 orbits of size 11 (fixed-point-free).
4. **Cesarz & Woldar (2023, Algebraic Combinatorics / arXiv:2308.02978):**
   divisibility by 7 ⇒ G ≅ ℤ₇; consequently divisibility by 2 ⇒ |G| divides 6, so
   G ∈ {ℤ₂, ℤ₆, S₃}. ⇒ a putative 99-graph is *nearly rigid*.

**Implication for strategy:** because Aut is so constrained, the classic
"assume a large automorphism + orbit-matrix" attack space is mostly exhausted; any
remaining symmetric search is order ∈ {3, 11, small}. A graph with trivial/tiny
Aut cannot be found by symmetry reduction — this is *why* the problem is hard.

---

## Attack vectors (research program — to be expanded by /scamper, pursued by subagents)

Each vector must end in either (a) a machine-checked computation, or (b) an
adversarially-verified combinatorial argument. Idea-only output is not progress.

- **V1 — Local/counting constraints.** Push the partial-linear-space view: count
  configurations (pentagons, hexagons, 4-cycles), Higman-style local eigenvalue
  interlacing on the 84-vertex second subconstituent, μ-graph structure. (Recent:
  arXiv:2409.10620 hexagon lower bounds; arXiv:2409.00268 shared-neighbourhood.)
- **V2 — Spectral / interlacing / Hoffman bounds.** Subconstituents of an SRG are
  regular two-graphs / have known spectra; interlacing on induced subgraphs and on
  the 7K₂ neighbourhood may force contradictions for specific local extensions.
- **V3 — Orbit-matrix search for the *surviving* automorphism orders** (3, 11, and
  combinations under |Aut| | 4158). Reproduce Behbahani–Lam machinery, then probe
  whether anything was left open. Concrete + verifiable, but heavy infrastructure.
- **V4 — SAT / CP exact encoding of small fragments.** Encode "extend this forced
  local configuration" as SAT; show local non-extendability lemmas. Feasible at the
  fragment scale even though the full graph is far out of reach.
- **V5 — Two-graph / switching-class angle.** Relation to regular two-graphs on
  the descendant structure; Seidel switching invariants.
- **V6 — Reframe via the 231-triangle Steiner-like packing.** It is a resolvable
  edge-decomposition into triangles with extra μ=2 global condition; map to design
  theory (group-divisible / packing) nonexistence tools.

---

## VERIFIED results (each validated against the real graphs rook(9) / BvLS(243))

These are machine-checked or adversarially-verified. battery.py reproduces the
spectral ones; the cross-pair bijection is verified true on rook(9).

**R1 — Cross-pair bijection (CERTAIN).** The 84 non-neighbours of v are in a
*forced* bijection with the 84 = C(14,2)−7 "cross-pairs": each non-neighbour's two
common neighbours with v are two neighbours lying in *distinct* matched edges of
the 7K₂ (they cannot be a matched edge, else λ=1 is violated since v is already
that edge's unique triangle-apex). Coordinates: label the 7 pairs, signs {+,−};
non-nbrs ↔ {(i,εᵢ),(j,εⱼ)}, i<j. Verified on rook(9).

**R2 — Forced derived spectra (CERTAIN, from battery.py).**
- Triangle incidence N (99×231): NNᵀ = 7I + A, eigenvalues 21¹,10⁵⁴,3⁴⁴; rank N = 99.
- Block graph of the 231 triangles (adj = share a point): 18-regular on 231,
  eigenvalues 18¹,7⁵⁴,0⁴⁴,(−3)¹³² → **4 distinct ⇒ NOT strongly regular** (so the
  "block graph is an infeasible SRG" attack is dead — no contradiction there).
- Subconstituents: Γ₁(v)=7K₂ (spectrum 1⁷,(−1)⁷); Γ₂(v) is **12-regular on 84**.
- Classical bounds all pass with slack: Delsarte clique ≤4 (local structure ⇒ =3),
  Hoffman coclique ≤22, Krein & absolute bound pass. **No cheap kill.**

**R3 — Subconstituent / interlacing analysis is EXHAUSTED (no contradiction).**
Master identity (verified on 20000 real pairs of BvLS(243)):
NᵀN = (k−μ)I + (λ−μ)A₂ − A₂² + μJ, PSD ⇒ q(θ)=−(θ−r)(θ−s) = −(θ−3)(θ+4) ≥ 0
⇔ s ≤ θ ≤ r. PSD window = Cauchy window (no extra force). Sharper: rank(NᵀN)=rank(N)
≤ k ⇒ **≥ m−k = 70 of the 83 non-Perron Γ₂-eigenvalues are pinned at {3,−4}; ≤13
extras lie strictly inside (−4,3)**, in {1,0,−1,−2} with integer mults (26 feasible
integer spectra). Met with equality on both real graphs. **Γ₂ is NOT an SRG**
(BvLS(243)'s Γ₂ has 5 distinct eigenvalues, walk-regular) — refutes any "Γ₂ must be
infeasible SRG" argument. Spectral/interlacing methods are silent here.

**R4 — Z₇-automorphism case is OPEN; the obvious local kill FAILS (CERTAIN).**
Cesarz–Woldar proved 7 | |Aut| ⇒ Aut ≅ Z₇ (Frob(21) eliminated by computer) but did
NOT rule out / construct. A Z₇ fixes exactly 1 vertex x (99≡1 mod 7) + fourteen
7-orbits; degree forces x adjacent to exactly **two** full orbits ⇒ Γ₁=7K₂ is two
7-orbits. **Decisive finite check: 7K₂ DOES admit a fixed-point-free Z₇ action**
(46080 order-7 autos of 7K₂, all f.p.f. — rotate the 7 edges in a 7-cycle), so the
tempting "a perfect matching can't be Z₇-invariant" contradiction is FALSE. Full
orbit enumeration is ~10¹⁹² — not brute-forceable. Machinery validated on Paley(29)
(a real Z₇-symmetric SRG). No nonexistence proved; no novelty claimed.

**META-FINDING:** the difficulty is now precisely located. All *linear/spectral*
feasibility (eigenvalues, Krein, absolute bound, interlacing, subconstituent rank)
is EXHAUSTED and consistent. The entire residual is a **non-linear combinatorial
completion**: choosing Γ₂'s "disjoint-pair" adjacency (each non-nbr picks 10 of ~40
candidate edges so the amply-regular codegree identity codeg_{Γ₂}=(1 or 2)−t holds).
That is a design/Latin-square/exact-cover existence question — the right target for
SAT/CP on bounded fragments, not for more spectral arguments.

**R5 — Geometric tools are closed off (CERTAIN, gates.py).** G is NOT
pseudo-geometric (pg parameters S=7/2, A=1/2 non-integer). The complement
(99,84,71,72) HAS integer pseudo-geometric parameters pg(21,3,18), but α=18 exceeds
the partial-geometry bound min(s,t)+1 = 4, so no genuine partial geometry exists.
⇒ neither G nor Ḡ is the point graph of a partial geometry; geometric/pg
classification gives no leverage. 4th-moment census Tr(A⁴)=54054 consistent.

**R6 — Local-fragment SAT is structurally INCAPABLE of a kill (CERTAIN).** Built a
validated pysat encoder (validated by recovering rook(9)'s exact 5040 = 9!/72
labeled completions; negative controls flip-edge→UNSAT, pin→1 sol; BvLS(243)
constructed and validated). On srg(99,14,1,2): the edge fragment (27 vtx),
two-star fragment, and radius-2 balls for **every n = 4..83 are SAT** (extendable),
each in ≤2 s; a 99-ball negative control (force a λ=1 violation)→UNSAT, so the SATs
are genuine. **KEY:** the graph has diameter 2, so the full radius-2 ball IS the
whole graph — n=84 is the open problem restated, and no PROPER fragment can be
non-extendable. Completion counts grow 2→5→19→336 at n=2,3,4,6 (residual freedom
real, not collapsing). ⇒ local non-extendability cannot resolve a diameter-2 SRG;
only global isomorph-free generation or new theory can. No kill; none possible here.

**R7 — SOS/Lasserre route CLOSED at all in-reach levels (CERTAIN, validated SDP).**
Built a validated cvxpy/SCS moment-SDP pipeline (validates correctly: existing
graphs srg(5,2,0,1)/(9,4,1,2)/(10,3,0,1) → feasible; srg(28,9,0,4) caught by Krein
q222=−8, srg(50,21,4,12) caught by absolute bound → infeasible). **Degree-2
relaxation of (99,14,1,2) is FEASIBLE** (= Krein passes; both literal SDP and
Bose–Mesner module agree) ⇒ no degree-2 certificate. A certificate needs level ≥3;
exact moment-matrix sizes: level-2 is ~1.18×10⁷ per side (~1 PB to store), level-3
~1.9×10¹⁰, level-4 ~2.3×10¹³ — astronomically out of reach. Full S₉₉ symmetry
reduction collapses level-2 to the 2-class scheme = the feasible degree-2 object,
so no tractable reduced SDP certifies. ⇒ SOS yields no in-reach nonexistence proof.

**R8 — eo=0 coordinatization of Γ₂(v) (CERTAIN; verified rook(9)+BvLS(243)).** In
cross-pair coordinates, Γ₂(v) of any srg(n,k,1,2) splits as a FORCED within-fiber
4-cycle bundle (C(m,2) fibers, m=k/2=7) PLUS a (k−4)-regular "free graph" F whose
edges occur **only between edge-disjoint fibers** ("eo=0", a signed bundle over the
Kneser graph K(7,2)); every Γ₂-triangle is all-free, count (n−1−k)(k−4)/6. For
n=99: **F is 10-regular, eo=0-only, 140 all-free triangles; each vertex picks 10 of
40 candidates (=10 disjoint fibers × 4)**. Follows from elementary λ=1/μ=2 counting
(not a new theorem) but is the key SEARCH-SHRINKING coordinatization — it removes
most branching freedom in the residual. [scratchpad final_constraint.py]

**R9 — automorphism cases (verified, mostly reproductions).** Order-11 RULED OUT
(independently reconfirmed: FPF, 9 orbits of 11, quotient N²+N=12I₉+22J₉,
diagonal-sum∈{10,24}, exhaustive even-diagonal search = 0 solutions, engine
positive-controlled). **Order-3 is NOT eliminated and REMAINS LIVE**: f∈{0,3} fixed
points (f=3 ⇒ the 3 form a K₃, partition 3+36+60; f=0 ⇒ 33×33 orbit matrix with
(B−3I)(B+4I)=6J). So a Z₃-symmetric Conway graph is still possible — an open
sub-case worth a deeper dedicated search. (Reproduces Behbahani–Lam/Makhnev–Minakova.)

**R10 — two methodological "do-not-bother" results (CERTAIN).** (a) The Seidel
two-graph attack is VOID for this family: S=J−I−2A has 3 eigenvalues {70¹,7⁴⁴,(−7)⁵⁴}
(not a regular two-graph; the descent needs n=2(2k−λ−μ)=50≠99); descendant bidegrees
are a deterministic closed form, prune nothing. (b) Metaheuristic CONSTRUCTION is
structurally incapable here — the landscape is a verified "golf-hole" (on the REAL
BvLS(243), one 2-swap from a solution, 0/50000 sampled swaps improve); best near-miss
1865 violated constraints (all degrees=14). ⇒ "no solution found" is ZERO evidence
of nonexistence. Subgraph-census forced counts all consistent (the "new hexagon
upper bound" was a verified TAUTOLOGY on the feasibility curve — no obstruction).

**R11 — Shpectorov–Zhao rank-overflow method ported & validated; 39-ball CONSISTENT
(CERTAIN, exact arithmetic, adversarially verified).** The 2025 method that killed
srg(85,14,3,2): represent vertices as unit vectors in the chosen eigenspace (Gram =
idempotent E_θ); any induced subset's Gram is PSD of rank ≤ dim, so a FORCED config
whose Gram overflows rank dim is a contradiction. Ported to srg99 in the s=−4
eigenspace (dim 44), **exact cosines cos_adj=−2/7, cos_nonadj=1/28** (validated on
rook(9): −1/2,1/4; BvLS(243): −5/22,1/55). **Positive control reproduced**: srg85
5·K₇ (35 vtx) has exact rank 35 > 34 (overflow fires). srg99 forced 39-vertex
triangle-ball: PSD, exact rank 31–36 ≤ 44 — **no overflow** (matches the 39<44 count;
growth needed). No FORCED overflow found growing into the shell (backtracking PSD to
depth ≥8). **KEY (the soundness trap):** local λ=1/μ=2 admissibility ≠ realizability —
naive greedy growth manufactures unrealizable configs that spuriously fail PSD (proven
by the identical procedure also "failing" on the EXISTING BvLS(243)). A genuine
overflow proof needs the μ=2 new-vertex constraints propagated RIGOROUSLY +
exhaustive shell enumeration. **Structural lever discovered:** λ=1 ⇒ the local graph
is a perfect matching 7K₂ — a far smaller enumeration space than srg85's cubic graphs
(540→39 good), making the exhaustive analog more tractable here than for srg85.

## Iteration ledger

- **Iter 1:** deep-research grounding; feasibility.py (whole λ=1,μ=2 family);
  constraint compendium with citations; certain local structure.
- **Iter 2:** /scamper fan-out (6 brainstormers → ~55 ideas, convergent shortlist).
  Ran battery.py (R1,R2). Dispatched 2 executor subagents → R3 (subconstituent
  exhausted) and R4 (Z₇ case open, local kill fails). META-FINDING: spectral
  toolkit exhausted; residual is combinatorial completion of Γ₂. Landscape in
  scamper_landscape.md.
- **Iter 3:** gates.py (R5: not geometric) + SAT subagent (R6: local fragments all
  SAT, diameter-2 makes local non-extendability impossible). Three independent
  families of method (spectral, geometric, local-combinatorial) now all exhausted
  & CONSISTENT. The residual is provably the GLOBAL completion = the open problem.
- **Iter 4:** SOS/Lasserre subagent (R7: degree-2 = Krein = feasible, validated;
  higher levels 10⁷–10¹³ intractable). FIFTH in-reach STANDARD family closed.
  Wrote SUMMARY.md.
- **Iter 5 (ultracode):** 14-agent Workflow over 7 unexploited veins, each
  adversarially verified vs rook(9)+BvLS(243). Yield R8 (eo=0 coordinatization),
  R9 (order-11 out / order-3 LIVE), R10 (two-graph void + golf-hole). Adversarial
  layer caught a tautological "new bound", re-scored near-miss 2044→1865, proved a
  "cascade" axiom-forced. **Identified the one untried frontier technique:** the
  Shpectorov–Zhao Euclidean-representation rank-overflow proof that killed the
  SIBLING srg(85,14,3,2) in 2025 (arXiv:2504.02449), never ported to 99.
- **Iter 6 (ultracode):** 4-agent Workflow ported + validated the Shpectorov–Zhao
  rank-overflow method (R11). srg85 positive control fires (35>34); srg99 39-ball
  consistent (rank 31–36≤44); no forced overflow yet; identified the realizability
  trap and the 7K₂-local-graph lever. Verdict consistency-confirmed (adversarial).
- **Iter 7 (ultracode):** 4-agent Workflow built the rigorous realizability propagator
  + exact forced-structure spec, both soundness-gated on real graphs (R12, R13).
  Findings: the **39-ball is FORCED RIGID** ("tricapped": apex triangle + 3 six-edge
  matched fans + 12 transversal triangles; 31 triangles, 93 edges); the **60-vertex
  shell** has exact forced regularities (each shell vtx (2,2,2)/eo=0/induced-deg-8;
  block-vtx shell-deg 10; per-fiber load 20); the **new-new coexistence table** with
  the hard prune *ball_common ≥ 3 IMPOSSIBLE* (validated on BvLS, 16110 pairs, 0 exc).
  Deep DFS reached realizable depth 11 (n=50), rank +1/vertex to 42, PSD, NO overflow.
  Verdict consistency-confirmed, genuine-progress=true (independent grower reproduced).

## STATUS ASSESSMENT (after iter 7) — sound engine; depth-bounded, no kill yet
The rank-overflow attack is now a fully rigorous, soundness-gated engine
(realizability propagator + exact forced spec + full-Gram W-W' branching certificate;
never false-overflows the real graphs, fires on srg85, boundary-calibrated at rank 44).
The forced local structure is pinned exactly (rigid 39-ball, 60-shell regularities,
coexistence table). The srg99 realizable growth is PSD-CONSISTENT to depth 11 (n=50,
rank 42); a kill needs an all-branch overflow at depth ~14 (n≈53, rank 45), gated only
by the exact-LDL O(n³)/node cost × W-W' branching — the same global-completion wall
every prior family hit, but now approached by a sound, calibrated certificate that
WOULD fire on a real overflow. Genuine incremental progress; not a one-shot kill.

## R12 — Realizability-respecting partial-SRG propagator BUILT, soundness-gated,
## srg99 39-ball grows PSD-consistent with NO forced overflow (CERTAIN; iter 7).
Built a rigorous constraint propagator (.work/99graph/: srg_core.py, propagator.py,
srg99_ball.py, growth_search.py, extend_shell.py, enumerate_fillings.py, multi_growth.py;
gates soundness_gate.py/gate_shell.py/gate_no_overprune.py/gate_filling.py; run_all.py).
State = partial graph with rel∈{ADJ,NON,UNK}; enforces on EVERY pair-type:
  old-old: λ=1 (ADJ ≤1 common, =1 once closed), μ=2 (NON ≤2 common, =2 once closed),
           7K₂ matching at each vertex, degree≤k; old-new + new-new: same closure +
           eo=0 (a dist-2 vertex's 2 picks per block are never a matched pair).
Propagation = deduce-to-fixpoint (R-deg, R-lam-close, R-mu-cap/close, R-match);
certificate = exact LDL^T over ℚ (rank=#nonzero pivots; any negative pivot ⇒ not PSD)
on the s=−4 eigenspace Gram (cos_adj=−2/7, cos_nonadj=1/28), overflow ⇔ rank>44 or
not-PSD.
SOUNDNESS GATE (the load-bearing deliverable) PASSES on BOTH real graphs:
  • rook(9): ALL 492 induced subsets PSD, rank≤4=dim_s (full graph rank exactly 4).
  • BvLS(243) [built as the verified coset graph of the [11,6,5] ternary Golay code,
    self-checked to params (243,22,1,2)]: star, triangle-ball(63, rank 60), random
    induced subsets to n=100 — all PSD, rank≤110. The SHELL-EXTENSION code path (the
    exact engine the srg99 search uses) replays 40 real dist-2 vertices with ZERO
    false-reject; the OVER-PRUNING gate confirms the engine ACCEPTS all 180 real
    dist-2 vertices; the bijection model (each block-vertex ~ exactly one vertex of
    each other block) is CONFIRMED on the real graph. Never false-overflows.
POSITIVE control genuine: srg85 5·K₇ overflows in the r=4 eigenspace (rank 35>dim 34,
PSD) — reproduces the Shpectorov–Zhao kill exactly. NEGATIVE control: srg99 coclique
of 45 fires (rank 45>44) ⇒ the srg99 certificate is non-vacuous.
srg99 RESULT (no contradiction; growth is consistent):
  • forced 39-ball: PSD, rank 31–36 ≤44 (filling-dependent), NO overflow (reproduced).
  • single dist-2 extension of a filled (identity) 39-ball: of 216 000 (=60³) eo=0
    pick-triples, exactly 5 760 are REALIZABLE (survive full propagation+certificate);
    210 240 pruned by genuine λ/μ contradictions; 0 pruned by overflow/non-PSD. EVERY
    realizable n=40 config has rank exactly 32 (= +1 over the n=39 rank 31), identical
    to the real-graph behaviour (BvLS rank climbs +1 per added dist-2 vertex).
  • of 121 sampled fillings (A-B fixed=id WLOG): 51 consistent, 70 inconsistent
    (correctly rejected), and ALL 51 consistent fillings admit ≥1 realizable extension
    (no dead-end). No forced single-vertex overflow exists.
VERDICT: the rank-overflow engine is now rigorous + soundness-gated, and the srg99
39-ball + first shell is PSD-CONSISTENT with no forced overflow — the open-problem
signature (every in-reach realizable extension stays representable). A nonexistence
proof needs exhaustive realizable growth to depth ≳52 (rank must climb 31→45), which
is the same astronomically-large global completion all five prior method-families hit;
the engine is the right tool but the bounded search finds no kill (none expected).

## R13 — DEEP bounded-exhaustive realizable growth w/ FULL-Gram certificate + W-W'
## branching; soundness-gated in-execution. CONSISTENCY-TO-DEPTH-11 (n=50), NO KILL.
New engine (deep_enum.py) fixes the load-bearing weakness of R12's multi_growth: that
search left NEW-NEW (W-W') pairs UNK, so known_clique_subset() DROPPED W vertices and
the certified rank UNDER-counted (could never reach 44 even if the true config would).
deep_enum BRANCHES on every W-W' adjacency via the exact BvLS-validated coexistence
table (ball_common>=3 impossible; ==2 forces non-adj; in{0,1} branch ADJ/NON), so the
FULL (39+t)-vertex induced Gram is certified at every node — no UNK, no undercount.

Two key forced facts re-derived + used:
  • a distance-2 vertex's 6 ball-neighbours form an INDEPENDENT set in the ball
    (verified: 0/180 real BvLS shell vtx violate). Picks hitting a ball-edge are
    pruned by lambda=1. -> 62,880 ball-independent picks, of which EXACTLY 5,760 are
    realizable single extensions (reproduces R12's 5,760; all rank exactly 32).
  • independent hand-audit of a built chain: 0 lambda>1, 0 mu>2, 0 7K2, all (2,2,2)/eo=0
    -> the propagator emits only genuine partial induced subgraphs.

SOUNDNESS GATE (same execution, same code path) — ALL PASS:
  • deep_cert_sanity.py: certificate NON-VACUOUS + calibrated — srg99 coclique-45 fires
    (rank45>44), coclique-44 QUIET (rank44==44, boundary correct), srg85 5*K7 fires
    (rank35>34), 39-ball quiet (rank31).
  • deep_gate.py: srg85 positive control overflows; BvLS243 static growth never false-fails.
  • deep_gate_engine.py: the IDENTICAL attach+full-Gram-certify ENGINE replays 45 REAL
    BvLS(243) shell vertices (n 63->108, rank 60->86, all PSD, all<=110): ZERO false-fail,
    ZERO false-contradiction. Engine is sound on realizable real growth.
  • proof-detector liveness: deep_enum's full_gram_certify rejects the 45-coclique
    (rank45) and accepts the 44-coclique (rank44) -> it WOULD detect a real overflow.

RESULT (two independent backtracking DFS runs agree): realizable growth reaches
DEPTH 11 = n=50, rank EXACTLY 42, climbing strictly +1 per added vertex
(32,33,...,42), PSD-consistent throughout; survivors at EVERY node; FORCED all-branch
overflow = NONE. (certfail prunes are SINGLE-branch non-PSD/over-rank of unrealizable
W-W' coupling choices — every such node still had surviving realizable branches; this
is healthy pruning, NOT a proof.) Note BvLS's real rank climbs SUB-linearly (flat +0
steps, e.g. 62->62), so on the real graph rank need not hit dim; the srg99 high-rank
greedy chain is the WORST case for overflow and still only reaches 42 at n=50 in budget.
Extrapolating +1/depth: rank 44 at ~depth13 (n=52), overflow(45) at ~depth14 (n=53) —
the same astronomically-large global completion every prior method hit. CAVEAT: this is
consistency-to-depth-11, NOT nonexistence (no all-branch certificate obtained; bounded
by exact-LDL O(n^3)/node x W-W' branching). Calibrated: CONSISTENT, no kill (expected
for a genuine open problem). Artifacts: deep_enum.py, deep_gate.py, deep_gate_engine.py,
deep_cert_sanity.py, rank_hunt.py, run_deep_all.py.
RANK-HUNT CALIBRATION NOTE: rank_hunt.py's greedy beam "stalled" at n=42 — VERIFIED an
artifact of its scan-budget truncation (the n=42 rank-34 config has >=5 realizable
extensions on full scan); the backtracking deep_enum DFS (n=50) is the reliable depth.

## R14 — OPTIMIZED rank-overflow engine (incremental bordered-LDL + index-backed
## propagator); reached DEPTH 12 (n=51, rank 43); EXACT exhaustive FORCED-RANK-CLIMB at
## the 39-ball; flat-impossibility is GEOMETRIC; WLOG nuance (iter 8; CERTAIN).
Artifacts (.work/99graph/): incldl.py, test_incldl.py, deep_enum_fast.py, perf_gate.py,
forced_climb.py, forced_climb_exhaustive.py, forced_climb_highrank.py, flat_geometry.py,
flat_geometry_deep.py, wlog_filling.py, wlog_filling2.py, frontier_highfill.py.

ENGINE OPTIMIZATION (validated exact-equivalent, soundness-gated):
  • incldl.IncLDL: exact rational BORDERED LDL. The placed-vertex Gram is a PURE BORDER of
    the parent node's (machine-verified border-stability: attaching a dist-2 vertex with
    fixed W-W' couplings NEVER flips a prior known pair / never turns prior UNK known, 0
    events over a depth-10 chain). So O(n^2) push + restore on backtrack replaces O(n^3)
    refactor. test_incldl.py: psd ALWAYS agrees with ldl_rank_psd; rank agrees whenever
    PSD; reproduces coclique-44(rank44)/coclique-45(rank45)/srg85-5K7(rank35) + 320 real
    induced subsets + 800 random matrices. EXACT.
  • propagator.py now carries an incremental _adj/_unk index (set_rel/add_vertex maintain
    it) so common_known_adj/possible_common use set-intersection not O(|V|) scans; get()
    inlines key(). perf_gate.py PROVES index==scan exactly on srg99 growth + 20 real BvLS
    shell vtx. ~2x throughput (deep_enum reaches depth 11 in 60s vs 120s prior).
  • ALL soundness gates still PASS unchanged: deep_cert_sanity (coclique45 fires/coclique44
    quiet/srg85 fires/39-ball quiet), deep_gate_engine (BvLS ball rank60->86 at n=108, ZERO
    false-fail).

RESULT — DEPTH 12 (n=51, RANK 43), one past the prior depth-11 wall. The high-rank chain
climbs strictly 31,32,...,43 (rank by depth d1..d12 = 32..43), PSD throughout, dim_s=44.
Rank 43 = 0.98 of dim; the frontier is rank 44 (depth 13) / overflow 45 (depth 14). Still
NO all-branch overflow node (no kill) — expected.

NEW STRUCTURAL RESULT (the real yield) — FORCED RANK CLIMB, and it is GEOMETRIC:
  • EXHAUSTIVE depth-0 certificate (forced_climb_exhaustive.py): of ALL 62880
    ball-independent 6-picks, exactly 5760 are realizable (reproduces R12/R13 exactly) and
    the rank-delta histogram is {+1: 5760} — ZERO flat, ZERO jump. Every realizable
    extension of the 39-ball RAISES rank by exactly 1.
  • WHY (flat_geometry.py, exhaustive cross-tab): of the 62880 picks, 57120 give a
    NON-PSD Gram border (geometrically impossible) and 5760 give a PSD border that climbs
    +1; **FLAT borders = 0 (both realizable and pruned).** So the cosine GEOMETRY ALONE
    forbids a rank-preserving extension at the 39-ball — flatness is geometrically
    impossible, not merely unrealizable. (Also: the 5760 PSD picks == the 5760 realizable
    picks exactly; geometry and lambda/mu realizability COINCIDE at depth 0.)
  • PERSISTS to high rank: at multiple distinct rank-37/40/42 nodes, every enumerated
    realizable extension still climbs +1 (forced_climb_highrank / flat_geometry_deep); at a
    rank-42 node all tested borders are non-PSD or climb, ZERO flat. (Evidence at the
    frontier, NOT a full all-config proof.)
  • CONTRAST WITH THE REAL GRAPHS (the significance): on BvLS(243), realizable extensions
    have rank-delta pattern [1,1,0,1,1,0,...] — flat (+0) steps appear from rank 62 (=0.564
    of dim 110) and keep the real rank SUB-linear so it never hits dim. srg99's forced ball
    starts ALREADY at 0.705 of dim (rank31/44) — higher than where BvLS's flat steps begin
    — and admits NO flat step. The real BvLS triangle-ball sits at rank/dim=0.545; srg99 is
    forced to 0.705. This is the precise structural reason the rank-overflow squeeze is
    much tighter for srg99 than for the family's real members.

WLOG of the identity filling (wlog_filling2.py — nuanced, honest):
  • Block-relabel orbit of identity: EXACTLY invariant (ball rank 31, 5760 ext, {+1:5760}).
  • NON-orbit consistent fillings EXIST and are genuinely different: random consistent
    cross-permutation fillings reach ball rank 36 (not 31) — so identity is NOT the unique
    iso-class; a full overflow proof would need to enumerate filling classes. BUT the
    FORCED +1 CLIMB is filling-INVARIANT: all 32 tested consistent fillings have
    delta-hist {+1} only. The structural phenomenon is robust; the absolute rank is not.
  • CAVEAT (must be stated): a rank-36 filling reaches the frontier in ~8 steps, but whether
    a rank-36 filling is itself extendable to a real srg99 is unverified — it may be a
    higher-rank filling that simply does not occur in any srg99. The rank-31 identity ball
    (the canonical forced structure from a real triangle) is the trustworthy anchor.

FRONTIER PROBES + a CAUGHT FALSE SIGNAL (adversarial discipline, CERTAIN):
  • A greedy high-rank chain from a rank-36 filling reached rank 43 (n=46) by depth 7, then
    a CAPPED scan (8000 picks) found no extension -> the driver auto-flagged "all-branch
    overflow". ADVERSARIAL RECHECK with an EXHAUSTIVE scan (recheck_overflow.py) found the
    SAME node HAS 4 realizable rank-44 extensions (delta {+1:4}) hiding past the cap
    (4 survivors per 327668 branches). => FALSE SIGNAL, a capped-scan artifact, NO kill.
    Lesson now hard-coded: a "zero survivors" from any capped/time-bounded scan is NEVER a
    proof signal; the auto-flag was removed from the drivers.
  • DECISIVE ARITHMETIC: at a rank-r node a +1 extension has rank r+1; only r+1 > dim_s=44
    (i.e. r>=44) is a rank OVERFLOW. So rank-43 dead-ends are combinatorial(lambda/mu) or
    non-PSD, NEVER a rank-overflow kill. A genuine overflow signal REQUIRES reaching an
    actual RANK-44 node and showing every extension is rank 45.
  • RANK-44 NODE TEST (rank44_node.py): reaching a rank-44 node needs a realizable rank-43
    -> rank-44 step, but those survivors are ULTRA-sparse (the identity seed-1 rank-43 node
    scanned 46419 picks / 163440 branches in 300s -> 0 rank-44 children, certfail=8 vs
    contra=163432, TIMED OUT -> INCONCLUSIVE, not a kill). Exhaustively reaching AND
    certifying a rank-44 node exceeds the per-run compute budget here. (Different rank-43
    nodes differ: the high-fill one had >=4 rank-44 children, the identity seed-1 one found
    0 in budget -- both consistent with "rank-43 extends", neither a proof.)

HONEST VERDICT (R14): the engine is faster (depth 11->12, ~2x/node) and EXACT-equivalent
(every optimization soundness-gated; a capped-scan false overflow was caught and retracted
by adversarial recheck). The genuine NEW result is the GEOMETRIC forced rank-climb at the
39-ball (exhaustive, exact: no flat extension exists, by cosine geometry alone) and its
persistence to rank 42 across many distinct nodes — a sharp qualitative difference from the
real family members (which rely on flat steps from 0.56 of dim to stay sub-linear; srg99's
ball is forced to 0.705 of dim with NO flat relief). This is consistency-to-greater-depth
(rank 43, depth 12) + a structural mechanism, NOT a kill: a kill needs an EXHAUSTIVELY
certified all-overflow rank-44 node across ALL filling classes, still gated by the global-
completion blow-up (frontier survivors ~4 per 3e5 branches). Calibrated: NO nonexistence
proof; verified structural findings + a faster, still-sound engine.

---

## R15 — MAKHNEV n3=0 NONEXISTENCE PATH: verified map (CERTAIN where machine-checked)

**Vein:** verify the literature's actual nonexistence path for srg(99,14,1,2).
Scripts: verify_n3_hexagon.py, verify_bvls_counts.py, verify_bvls_n3_hex.py,
verify_c6_and_n3types.py, reconstruct_n3.py (all exact arithmetic, all validated on
the real graphs rook9 + BvLS243).

**(1) The Makhnev reference is now pinned exactly.**
A.A. Makhnev (1988), "Strongly regular graphs with λ=1", Mat. Zametki 44(5) 667-672;
Eng. transl. Math. Notes 44(5) 847-850. MR980587, Zbl 0737.05078; mathnet paperid
mzm4220. Cited as ref [7]/[4] by Reimbayev 2024 (arXiv:2409.10620) and 2025
(arXiv:2508.03377). FULL TEXT NOT OBTAINED (mathnet gates it; no secondary source
quotes its theorem). The "[Makhnev] proved n3=0 ⇒ no srg(99,14,1,2)" claim exists ONLY
as a bare citation in Reimbayev's two preprints; the argument is NOT reproduced anywhere
accessible. NOTE: the authoritative 2023 Conway-99 paper (Cesarz-Woldar, arXiv:2308.02978)
cites Makhnev ONLY for automorphism bounds and never invokes any n3=0 nonexistence — a
strong signal the keystone is not part of the mainstream record.

**(2) p6 = 209286 + n3 identity: VERIFIED exactly on both real graphs.** It is the n=99
instance of Reimbayev Thm 2: n12 = (1/12)nk(k-2)(2k^2-21k+53) + n3, where n12 = #induced
hexagons (induced C6) and n3 = #{two vertex-disjoint triangles joined by exactly 2 edges}.
  - rook9:   formula const = 6;        real induced-C6 = 6;        n3 = 0.  ✓ (6 = 6+0)
  - BvLS243: formula const = 4980690;  real induced-C6 = 4980690;  n3 = 0.  ✓
  - srg99:   const = 209286, so p6 = 209286 + n3.
  Harness calibrated: p3=891, p4(C4)=13365, p5(C5)=384912 on BvLS all match exactly.
  c6 (char-poly coeff) independently verified from eigenvalue e6 AND Reimbayev's closed
  form for (9,4),(99,14),(243,22): c6 = -168, -47288703, -2975686065 (Table 3) all match.

**(3) n3 config disambiguated + n3=0 is structurally real.** Under λ=1, the "2 cross edges
sharing an endpoint" config is FORBIDDEN (a vertex would be a 2nd apex of an edge); the
only admissible n3 config is 2 *independent* (matching) cross edges. On BOTH real graphs,
disjoint-triangle pairs have ONLY 0, 1, or 3 cross edges — NEVER 2 (rook9: 6 prism pairs;
BvLS243: 240570 one-edge + 8910 prism pairs; n3=0 exactly). So "two triangles joined by 2
edges ⇒ joined by the 3rd" (the prism property) genuinely holds in the family's known
members. n3=0 is a real, non-vacuous structural rigidity — not an artifact.

**(4) "n3=0 ⇒ nonexistence" reconstruction: NOT reproduced; not locally forced.**
  - n3=0 is NOT forced by local (6-vertex) λ=1/μ=2 constraints: the config (2 cross edges,
    3rd absent) is locally admissible — it only requires c,z to find their 2 common
    neighbours outside the 6 vertices. Any forcing is GLOBAL.
  - n3 is a genuinely FREE variable in the order-six census; nonnegativity of all counts
    gives only n3 ∈ [0, 4158] (tightest bound n1 = 1386 - n3/3 ≥ 0), and integrality forces
    only 3 | n3. Nothing in the counting machinery forces OR excludes n3=0; n3=0 is merely
    the hexagon-minimising endpoint. So Reimbayev's own papers do NOT contain a proof; the
    nonexistence step is entirely outsourced to the un-recovered Makhnev 1988.
    VERDICT: could not reconstruct n3=0 ⇒ nonexistence; status = unverified literature claim.

**(5) "symmetry ⇒ n3=0": FOLKLORE / inapplicable to the open case (this is the key gap).**
  Reimbayev states it as a CONJECTURE ("we conjecture the lower bound is the true value due
  to many symmetries broken otherwise") and as "all arguments of symmetry tell that n3=0" —
  i.e. an expectation, never a proof. Both real witnesses (rook9 = Paley(9), |Aut|=72,
  vertex-transitive; BvLS243, vertex-transitive Cayley graph — both VERIFIED computationally)
  have n3=0 BECAUSE they are rank-3 / vertex-transitive: homogeneity collapses the count.
  But a Conway 99-graph is provably NOT vertex-transitive (Aut ∈ {1,Z2,Z3,Z6,S3} per
  Cesarz-Woldar 2023). So the very symmetry that yields n3=0 in the known graphs is ABSENT
  at n=99 — the heuristic runs exactly backwards for the open case. "symmetry ⇒ n3=0" is
  FOLKLORE for n=99: plausible-looking, witnessed in transitive examples, but with no
  mechanism that applies to the asymmetric 99-graph.

**Bottom line of the literature's nonexistence path:** it is a TWO-keystone chain
  [A] symmetry ⇒ n3=0   and   [B] n3=0 ⇒ no srg(99,14,1,2) (Makhnev 1988).
  [A] is explicitly a CONJECTURE (folklore; inapplicable to the asymmetric target).
  [B] is an un-recovered 1988 citation, absent from the authoritative 99-graph literature.
  Neither keystone is verified. The p6=209286+n3 IDENTITY underneath them, however, is now
  machine-checked exact on both real graphs. The honest verdict: the literature's
  "nonexistence path" is NOT a proof — it is a verified identity wrapped in two unproven
  (one conjectural, one unretrievable) steps.

---

## Ledger (cont.) + STATUS after iter 8
- **Iter 8 (ultracode):** 5-agent Workflow. Engine vein → R14: ~2× faster sound
  incremental-LDL engine, reached depth 12 (n=51, rank 43); **GEOMETRIC forced
  rank-climb at the 39-ball** (exhaustive: of 62880 picks, 5760 realizable, ALL +1,
  ZERO flat — flatness is geometrically impossible by the cosine system alone), vs
  real BvLS which relies on flat steps to stay sub-linear; the **rank-44-only lemma**
  (a +1 border changes rank by exactly 0 or 1, so an overflow can occur ONLY at a
  rank-44 node — rank-43 dead-ends are never kills); caught + retracted a capped-scan
  FALSE overflow signal (adversarial discipline). Makhnev vein → R15: the literature's
  nonexistence path is a verified identity (p6=209286+n3) wrapped in TWO unproven
  keystones — "symmetry⇒n3=0" is folklore that runs BACKWARDS for the asymmetric
  99-graph, "n3=0⇒nonexistence" is an unrecovered 1988 citation. Both veins
  consistency/negative-confirmed; no kill.

**STATUS:** The rank-overflow program has produced a sharp picture. A nonexistence
kill can live in EXACTLY ONE place: a rank-44 node forced by the rigid 39-ball that
admits zero realizable +1 extensions (the rank-44-only lemma). srg99 is uniquely
squeezed — its forced ball sits at rank/dim=0.705 with NO flat relief, where its real
siblings have flat steps from 0.55. But reaching AND exhaustively certifying a rank-44
node (depth ~13–14, n≈52–53) is compute-bounded: frontier survivors are ~4 per 3×10⁵
branches, and a full proof must cover all 39-ball filling classes. Symmetry reduction
is the one untried enabler. The literature's n3 path is now known NOT to be a usable
shortcut. Verified incremental progress; no kill; honest open frontier.

## R16 — RANK-44 NODE REACHED + zero-survivor signal (general-engine vein, iter 9)
## A TRUE rank-44 node with NO realizable extension; soundness-gated; HONEST scope stated.
Artifacts (.work/99graph/): rank44_drive.py, rank44_recheck.py, rank44_checkA.py,
rank44_flatfast.py, rank44_flatdirect.py, rank44_joint.py (the COMPLETE exact ww-exhaustive
certificate), joint_reals_gate.py, reals_flat_at_dim.py, noflat_forced.py, filling_census.py
(+ rank44_flatclosed.py, rank44_overcap.py). Saved node: scratchpad/rank44_node.pkl.

ENGINE ACCELERATION (the enabler): GEOMETRY/REALIZABILITY DECOUPLING. The rank-delta of a
new vertex is decided by its border column (one incldl push, O(n^2), no deepcopy/propagate),
so a CHEAP geometric pre-filter runs first and the expensive realizability runs only on
geometric climbers. This let the search reach a rank-44 node + exhaustively scan it (the
prior rank44_node.py TIMED OUT on the rank-43->44 step). At the rank-43 node the ball-only
geometric (rank,psd) class was verified WW-INVARIANT (40 picks, full 2^11 ww-space, 0 class
changes), justifying the ball-only pre-filter THERE.

RESULT (rank44_drive): reached 4 TRUE rank-44 nodes (n=52, rank 44 = dim_s). At EACH, an
EXHAUSTIVE (uncapped, completed) ball-only scan of all 62880 picks: FLAT@44 = 0, every PSD
extension geometrically OVERFLOWS to rank 45 > 44; ZERO realizable survivors.

ADVERSARIAL VERIFICATION (the load-bearing layer):
  • CHECK C (independent static-Gram, non-incldl path, srg_core.ldl_rank_psd): the rank-44
    node is rank 44, PSD — NOT an incremental-LDL artifact. left-null dim = 52-44 = 8 (exact).
  • REALS-DO-NOT-FALSE-FIRE (reals_flat_at_dim.py): on REAL BvLS(243) (dim_s=110), all 243
    vectors push to rank exactly 110, PSD throughout (NEVER overflow); at the first rank-110
    node ALL 52 remaining real vertices extend FLAT (0 overflow, 0 non-PSD). The mechanism is
    sound: a representable graph's rank-at-dim node is ALL-FLAT; srg99's is ALL-OVERFLOW —
    the OPPOSITE. The overflow is a genuine geometric over-constraint, not an engine bug.
  • NO-FLAT-FORCED census (noflat_forced.py): EXHAUSTIVE per-node geometric classification of
    all 62880 picks at every node rank 31..43: FLAT = 0 at EVERY node (5760->5704 climbers,
    rest non-PSD). So along the chain rank climbs strictly +1 with NO flat relief; it MUST
    reach 44 by n<=52 then overflow. (BvLS by contrast has flat steps from rank 62/110.)
  • CHECK B caught the soundness TRAP: the ball-only class is NOT ww-invariant AT a rank-44
    node (1/20 picks ww-dependent, classes {(44,nonPSD),(45,PSD)} — but NEITHER is a (44,PSD)
    flat). So the ball-only pre-filter is UNSOUND at rank 44 and the drive's "flat@44=0" needed
    a ww-COMPLETE recheck.
  • WW-COMPLETE FLAT TEST — the rank-44 node is a COMPLETE, EXACT, ww-exhaustive DEAD-END
    (rank44_flatdirect.py + rank44_joint.py). A survivor at a rank-44 node must be geometrically
    FLAT (rank 44 PSD; rank 45 overflows, non-PSD dead); flat <=> the new unit vector w lies in
    V (dim 44) with the prescribed cosines. Over ALL 62880 picks at a TRUE rank-44 node:
      - 37253 ww-impossible (ball_common>=3).
      - 23728 BALL-INFEASIBLE: b_ball NOT in colspace(G_BB) (ball sub-Gram rank 31) -> NO unit
        vector has those 6 ball-cosines -> no flat for ANY shell coupling. PROVEN exactly.
        (== the same 23728 the independent closed-form colspace test found flat-free.)
      - 1899 ball-feasible (|w_U|^2<1): resolved EXACTLY by the joint test. The 13 shell perp-
        vectors span the 13-dim perp space V\U (perp-Gram K rank 13, PSD, invertible), so each
        {ca,cna}^13 target pattern fixes a UNIQUE w_perp; flat <=> e^T K^{-1} e == R^2. Over
        EVERY pick x EVERY 2^13 pattern: **0 flat**.
    => ZERO geometric-flat ww over EVERY pick x EVERY shell coupling => the rank-44 node has
    ZERO realizable extensions: a COMPLETE, EXACT, ww-EXHAUSTIVE all-branch dead-end at a TRUE
    rank-44 node. (rank44_drive saw this at 4 distinct rank-44 nodes via the ball-only scan;
    flatdirect+joint CERTIFY one exactly, ww-complete, closing the CHECK-B gap.)
  • JOINT-TEST REALS GATE (joint_reals_gate.py): the SAME colspace+norm flat-test on a REAL
    BvLS(243) rank-110 node DETECTS the real flat extension exactly (border in colspace,
    reconstructed <w,w>=1). The test FINDS flats where they exist -> srg99 zero-flat is a
    genuine geometric over-constraint, NOT a method blind spot.

HONEST SCOPE (stated, not hidden):
  • FILLING CLASSES (filling_census.py): consistent 39-ball fillings (ab=id,ac=id, residual
    tau=bc) span ball-ranks 31..36 — rank31:1 (the IDENTITY = canonical real-triangle anchor),
    rank36:2132 (majority). The rank-44 signal is on the IDENTITY (rank-31) chain. Higher-rank
    fillings reach rank 44 in FEWER steps (MORE squeezed); no-flat census shows flat=0 at rank
    32..36 nodes too. So no-flat-forced, IF universal, covers ALL classes (identity is the
    slowest/hardest case). block-relabel WLOG fixes 2 of 3 cross-fillings -> tau reps.
  • THE GATING UNPROVEN LINK: a KILL needs no-flat-step FORCED at EVERY realizable node (all
    branches), not just the (exhaustive-at-each) nodes on the chains tested. Shown exhaustively
    at the ball + every node of sampled chains (rank 31..43) + the rank-44 node's flat-test;
    NOT shown for all reachable nodes. Also: a single rank-44 dead-end config is only a kill if
    a real srg99 is FORCED to contain such a node (the global-completion wall). LOGIC that IS
    sound: the rank-44 node we built does NOT embed in any srg99 (else it would extend to 99).
VERDICT: the FIRST genuine, COMPLETE zero-survivor certificate at a TRUE rank-44 node (the
unique place the rank-44-only lemma allows a kill). EXACT + ww-EXHAUSTIVE (all 62880 picks x
all 2^13 shell couplings accounted: 0 flat), soundness-gated every way (srg85 fires rank35>34;
coclique45/44 calibrated; BvLS rank-110 node all-flat & the flat-test DETECTS real flats —
no false-fire/no blind spot; static-Gram independent of incldl; node hand-audited clean
lambda=1/mu=2/deg14/0-UNK). So: this realizable rank-44 partial config does NOT embed in any
srg99 (else it extends to 99). NOT YET A KILL — the two remaining links are the global-
completion wall, now sharply localized: (1) no-flat-step FORCED at EVERY realizable node (shown
exhaustively at the ball + all chain nodes rank 31..43 + an independent rank-36 filling +
the rank-44 node, but not ALL reachable nodes); (2) a real srg99 is FORCED to grow its rank-31
ball through such a rank-44 dead-end (no-flat-forced would give this since rank then climbs
31->44 by n=52 with no relief). Calibrated: strongest signal to date — a complete exact dead-end
at the lemma's unique kill-locus — but not a full nonexistence proof.

## R20 — Z₃/f=0 CELL EXHAUSTION: 0/4 cells closed; GENUINE COMPUTE FRONTIER; bottleneck
## DIAGNOSED (iter 13). Artifacts (.work/99graph/): canon_backtrack.py, canon_validate.py,
## canon_drive2.py, sat_lexleader.py, smt_lexleader.py, canon_lift.py, CANON_FINDINGS.md.
Three MUTUALLY-INDEPENDENT engines built (canonical-labeling backtracker + Z3 SMT + CaDiCaL
SAT), ALL proven SOUND: recover the real rook(9) 3×3 and BvLS(243) 81×81 fixed-point-free-Z₃
quotients; lex-leader exhaustively sound (exactly 1 rep/orbit); close UNDERSIZED t≠33
sub-instances with COMPLETED UNSAT in <2.5s. But ALL stall at the SAME wall on the smallest
real cell a=24 (T27,E6). **0 of 4 spectral classes certified-exhausted; 0 liftable models.**
NO timeout relabeled as infeasible (adversarially verified: the only INFEASIBLE strings refer
to f=3 / order-11 / undersized sub-instances). **DIAGNOSIS (measured):** canonical
symmetry-breaking removes BETWEEN-row isomorph redundancy but does NOT shrink the ~10⁷
bilinear-consistent completions of a SINGLE empty row — the engine cannot even finish row 2
of 33. The symmetry quotient is the WRONG lever; the bottleneck is WITHIN-row A1-fill width.
Net: a validated reusable isomorph-free generator + a precisely characterized boundary; NOT
progress on existence. Behbahani's "?" confirmed a genuine compute wall. Conway's problem OPEN.

## R21 — WITHIN-ROW LEVER WORKS (a=24 row-2 wall BROKEN); bottleneck MIGRATES; 0 cells
## exhausted; program CONSOLIDATED (iter 14). Artifacts: incut_backtrack.py, rowdb_assembly.py,
## FINAL_REPORT.md.
The diagnosed within-row lever is REAL: row 2 of a=24 ct=(6,) (the prior wall — 3 engines
stalled at max_row=2) now COMPLETES. incut (intersection cut + leading-row canonicalization
L=2) → max_row=4; rowdb (residual-interval propagator) closes row 2 at node 362 → max_row=4.
Independently reproduced from scratch; non-vacuity verified element-by-element (genuine
bilinear-consistent quotient rows, IPs = 6−R_ij); row-2 width 586,575 confirmed by TWO
independent counts; the DECISIVE lever is leadsym L=2 (the cut is exact but insufficient alone).
BUT exhaustion is still far: the bottleneck MIGRATES (row 2→4→8 with the A2-lemma); deep pushes
a=24 ct=(6,) 120M nodes/639s → max_row=4, ct=(3,3) 80M/900s → max_row=8. **0 of 4 cells
certified-exhausted; 0 SAT models; honest timeouts throughout (no INFEASIBLE relabeled).**
This is the genuine compute frontier of orbit-matrix backtracking. CONSOLIDATION written:
FINAL_REPORT.md (full program R1–R21). Weakest link flagged: only rook(9) exercises empty-rows
as a real fpf-Z₃ control (BvLS has E=0); the empty-row cut's exactness rests on a synthetic
cut==brute@t=33 check + the 586,575 double-count.

## STATUS after iter 15 (R22 ×2): a=24 NOT closed (McKay full-canonical is sound but weaker
at leading rows than leadsym; the two are PROVABLY NON-COMPOSABLE — closes an unsound shortcut).
Global vein: mu-quad involution + line-meet spectrum {18,7,0,−3} reusable but elementary; CGSS
line-graph classification PROVABLY VOID (λ_min=−3<−2); no kill. END-STATE: genuine frontier.
The single live lever needs a SINGLE canonical form that is BOTH leading-row-strong AND
full-depth-sound — pure-Python cannot supply it; this requires nauty/Traces (C).

## R23 — TERMINAL: single-machine attack surface EXHAUSTED (iter 16). nauty UNAVAILABLE here
(no C toolchain: no gcc/cc/clang/cl/make/cmake; no pynauty/igraph/sage; only networkx). The
diagnosed missing canonical form WAS built in pure Python (ir_canon.py) and PROVEN EXACT
(V0 canon==brute lex-min over Aut_empty×S_T; C3 survivors=orbit reps, incl. S₆ 70→2) — leading
rows collapse to 1 — yet a=24 STILL walls at row-2 canonical width (re-run 120k nodes: budget
abort, models=0, max_row 2/3, NOT infeasible). 0/4 cells closed; 0 SAT models. Caveat: ir_canon
overflows on the dense BvLS t=81 quotient (idempotence not asserted there; the a=24 regime
converges, canon_overflows=0). LITERATURE (live re-fetch): Brouwer marks (99,14,1,2) "?" with NO
nonexistence ref; the active Reimbayev program's punchline rests on the n3=0/Makhnev-1988 step
already shown NOT-A-PROOF here; srg(19,6,1,2) proof explicitly does NOT extend to k=14; nothing
new portable 2024–2026. ⇒ every single-machine route closed/exhausted. EXTERNAL levers only:
(a) C-level nauty/Traces or distributed compute → could close a=24 (ir engine ready to drive);
(b) obtain/translate Makhnev-1988 → test the conditional n3=0⇒nonexistence.

## R24 — MAKHNEV 1988 RECOVERED + VERIFIED; n3 ≥ 3 PROVEN (new constraint); narrative fully
## characterized; TERMINAL: single-machine + literature levers EXHAUSTED (iter 17).
- **[B] VERIFIED:** Makhnev 1988 (Mat. Zametki 44(5):667-672) Theorem 2 recovered (valid PDF,
  internally consistent) + proof chain independently reconstructed: condition (*) = n3=0 forces a
  subconstellation **srg(33,12,1,6)** whose eigenvalue multiplicities **180/7 & 44/7 are
  NON-INTEGRAL ⇒ infeasible**. It is **(99,14,1,2)-SPECIFIC** (pivot Lemma 7 needs k=6μ+2=14 —
  only the 99-graph; BvLS has 5 disjoint triangles/outside-vertex, not 1) — resolving the
  "reals have n3=0 yet exist" paradox.
- **[A] FALSE-as-stated:** n3 = 4158 − 3·nprism; n3 provably NON-SPECTRAL (cospectral Rook₄ₓ₄ vs
  Shrikhande: identical char-polys, prism counts 48 vs 0) ⇒ no spectral/p-rank/scheme invariant
  pins n3; only 3∣n3, n3∈[0,4158]. "symmetry⇒n3=0" runs backwards for an asymmetric graph.
- **NEW PROVEN CONSTRAINT: any srg(99,14,1,2), if it exists, has n3 ≥ 3** (contains a disjoint
  triangle-pair joined by exactly 2 edges) — structurally UNLIKE both known family members.
  [A]∧[B] do NOT chain into a proof. Validated on both reals (makhnev1988.pdf/.txt, n3_VERDICT.py).

## R25 — EXTERNAL RESOURCES PROVIDED (iter 18): user gave local compute (RTX 5090, Ryzen
## 9950X3D 16C/32T, 64GB) + tool-install permission. TOOLKIT UNBLOCKED (no C compiler needed):
## igraph 1.0.0 BLISS canonical labeling (= the C-level partition refinement R20/R23 said was
## the missing ingredient); pysat with **kissat404** (Kissat 4.0.4) + cadical300 (strongest
## modern SAT, never used before here); numba 0.65.1 JIT; 32 logical CPUs for multiprocessing.
## ⇒ the Z3/f=0 cell-closure wall is now ATTACKABLE. Loop RESUMED (both computational + creative
## tracks, per user). [Previous TERMINAL STATUS below was pre-resource; superseded by R25.]

## R26 — NEW VERIFIED CONSTRAINT (creative track, iter 18): Z3/f=0 triangle-orbit kill
## T≡0 mod 3 eliminates parity classes a=20, a=22; + forced Δ2 spectrum; one false claim refuted.
- **A [STRONGEST, NEW, verified]:** for an order-3/6 fixed-point-free automorphism, Burnside on
  the 231 triangles forces **T ≡ 0 mod 3** (T = #triangle-orbits). With e=3T (each 3-cycle has 0
  or 3 internal edges) and the eigentrace identity 7τ_r=e+4t−18, this selects T∈{6,27} from
  {6,13,20,27}, **ELIMINATING a=20 (T=13) and a=22 (T=20)** — strictly stronger than the prior
  "a even". Reproduced exactly (rook9: 72 autos integral traces; e=9=3·3). ⇒ the Z3/f=0 search now
  only needs **a=18 and a=24** (both still open; a=24 is the BLISS+Kissat target). Conditional on an
  order-3/6 automorphism existing. (Caveat: eigentrace ALONE gives e≡4 mod 7, 14 values; the e=3T
  step is the separate load-bearing piece — code correct, attribution imprecise.)
- **B [NEW, consistent]:** forced second-subconstituent Δ2 spectrum {12, 3⁴⁰, 0⁷, −2⁶, −4³⁰}
  (12-regular, 84 vtx); λ=1-specific (rook4/Shrikhande have different Δ2 ⇒ not param-forced in
  general); a smaller fully-specified realizability sub-target. No kill.
- **C [modest, partly dual]:** triangle-block-graph N Nᵀ=(k/2)I+A_G ⇒ spectrum {18,7⁵⁴,0⁴⁴,−3¹³²},
  edge-regular λ_B=5, locally-3K6; mostly dual to the rank-44/τ=−4 content.
- **REFUTED (discard):** the "μ-balance #(μ=2)−#(μ=0)=462" claim is FALSE (B not SRG; 0 on rook9,
  −133650 on BvLS). Caught by the adversarial layer.
- No kill. All validated on rook(9)/BvLS(243). Cross-track: feed T≡0 mod 3 into the BLISS+Kissat
  enumerator as a-priori pruning; only a=18, a=24 remain in the symmetric subcase.

## R27 — BLISS BREAKS THE WALL (computational track, iter 18): frontier row 2-4 → row 11;
## a=24 ct=(6,) ~60% certified nonexistent; uncapped 32-core run is the path to closure.
BLISS canonical-augmentation (igraph, C-level) is the diagnosed missing ingredient and DELIVERS:
simultaneously leading-row-strong (row-1: >438k completions → ~5 canonical partials; row-2 ~17;
row-3 ~41) AND full-depth-sound. **max_row 11 (parallel) / 9 (single)** vs prior walls
(leadsym 4, McKay 2, ir_canon 2). a=24 ct=(6,): of 497 canonical subtrees, **300 COMPLETED with
0 orbit matrices** (individually certified nonexistent), 155 walled at the 107k-node cap (deep
tail), 42 unprocessed ⇒ cell ~60% certified, NOT closed (honest TIMEOUT, not relabeled). 0 SAT
models, 0 liftable. SAT (CaDiCaL) only CONFIRMS the wall (2M-conflict ct=(3,3)→UNKNOWN; kissat404
segfaults rc=139 on Windows; the "10M" portfolio log was a WinError-5 spawn crash = not evidence).
Engines fully validated (BLISS V0–V6 PASS, recovers rook9 + BvLS 81×81 quotients, exhaustion
control count=0). **PATH TO A PUBLISHED-GRADE INCREMENT:** with R26 (only a=18, a=24 remain),
run bliss_a24_unbounded.py UNCAPPED on 32 cores to certify the deep tail → close a=24 (0 survivors
= INFEASIBLE beyond Behbahani, or a found orbit matrix = lift to a construction). Plausibly reachable
for ct=(6,) in multi-hour-to-overnight; a=18 (E=27, 191 cycle-types) is much harder. NOW RUNNING
as a background process. Report any closure ONLY as a completed canonical tree with 0 survivors.

## R28 — RECURSIVE-SUBDIVISION ENGINE solves the deep-tail blocking; a=24 certification RUNNING,
## guaranteed to complete, 0 orbits so far (iter 18, in progress).
The flat-prefix-4 uncapped run STALLED on a deep subtree (>1.14M nodes blocking a worker; froze at
~219/497). FIX (bliss_a24_recursive.py, engine bliss_canon.py unchanged): per-worker NODE CAP
(tuned 300k→3M after watching the queue explode at 300k) + RECURSIVE SUBDIVISION — a worker that
hits the cap does NOT count; the master re-seeds that subtree one row deeper and re-queues the
children, so every contributing leaf completes uncapped (true certificate) with GUARANTEED progress
(no blocking). VALIDATED D1–D3: recovers rook(9) genuine quotient THROUGH the recursive driver under
a tiny cap (subdivision forced); exact count+cert-set under subdivision on the real a=24 cell;
ct=(6,)/ct=(3,3) partitions exact. (Fixed a JSON-resume unhashable-cert bug.) STATUS: a=24 ct=(6,)
RUNNING (PID 47408, 26 procs) — leaves=236, queue=445, subdiv depth 4, **0 orbit matrices, 0 SAT**,
7M+ nodes, no blocked worker; ct=(3,3) also running (PID 66392). Completion GUARANTEED but
multi-hour-to-multi-day (total tree plausibly billions of nodes). Monitor: `python monitor_a24.py`;
resume after any kill: `powershell -File launch_a24_recursive.ps1 -Ct "6" -Cap 3000000 -Procs 26`.
**VERDICT PENDING** — "a=24 ct=(6,) CLOSED" requires bliss_result_rec_a24_ct6.json with orbits=0
(completed tree, 0 survivors) — that would be an increment beyond Behbahani's open "?" cell.
SAFETY (learned): the machine also runs the user's LIVE trading system (copy-trader API :8800,
trader.py) — NEVER blanket-kill python; target only the specific bliss PIDs.

## R29 — DIRECTIVE PIVOT (iter 19): local compute STOPPED; loop → NEW MATH for the ASYMMETRIC case.
User directive: stop local BLISS (done — killed only the bliss PIDs 47408/66392; the 4 live-trading
python procs untouched; checkpoints bliss_rec_a24_ct6/ct3_3.jsonl preserved & resumable). Compute is
now CLOUD-ONLY — spec heavy jobs, never run them locally. The Z3/f=0 a=24/a=18 certification is PAUSED
(resumable on cloud via the R28 engine; was at leaves≈236+, 0 orbits, on track but multi-day).
NEW LOOP FOCUS: genuinely new mathematics for the **asymmetric (trivial-Aut) case** — the real crux,
untouched by ALL the symmetry/orbit-matrix work (which only addresses Z3/f=0 etc.; a real srg99 is
almost surely (near-)rigid). Build on the NEW verified results: **n3≥3** (every srg99 has an H3 = two
disjoint triangles + exactly 2 edges), the **lift theorem** (97.3% non-flat), the **Δ2 forced
spectrum** {12,3⁴⁰,0⁷,−2⁶,−4³⁰}, the rank-44 global Euclidean structure, the verified Makhnev
conditional. Don't re-tread closed routes (FINAL_REPORT §2). Verify every claim (light checks OK;
CLOUD-SPEC anything heavy); no bluffing; self-paced.

## R30 — NEW MATH, asymmetric case (iter 19): leverage migrated counting → s=−4 GEOMETRY;
## triangle-split polytope (new, scope-limited); identities corrected; no kill.
- **NEW constraint (scope-limited): TRIANGLE-SPLIT POLYTOPE.** For any s=−4 star complement H
  (|H|=55): classify the 231 triangles by |T∩H|∈{0,1,2,3}; the rank-3 system (forced by λ=1 +
  local-7K2) gives bHHX=e−3t, cHXX=385−2e+3t, dXXX=e−t−154, so nonnegativity forces
  **e(H)∈[154,384]** (tighter than the interlacing window [77,385]), e(X,H)=770−2e(H)∈[2,462],
  t(H)∈[⌈(2e−385)/3⌉, min(⌊e/3⌋, e−154)]. A NECESSARY condition on a hypothetical star complement
  (search-pruner), NOT an exclusion; untestable on the reals (neither has eigenvalue −4; BvLS min
  eig −5). Independently reproduced.
- **NO KILL** — all four lenses consistent. COUNTING IS PROVABLY EXHAUSTED: everything reduces to
  the {DTP, X1, X2} span with n3 free; n3/nprism/M provably NON-SPECTRAL (Rook4×4 vs Shrikhande:
  M=216 vs 192, (n3,nprism)=(144,144) vs (96,96)). The transient "n3≥1386" candidate kill was a
  FALSE ALARM (wrong DTP=21714 from ×T=231; correct DTP=24486 ⇒ bound dissolves; n3 stays free).
- **CORRECTED reusable identities:** n3 + 3·nprism = ¼·n·k(k−2) = 4158 (verified rook9=18,
  BvLS=26730 — the earlier "3n1+n3" form was FALSE); DTP=C(231,2)−99·C(7,2)=24486; CRS sign
  A_X = sI + Bᵀ(C−sI)⁻¹B (diag = −s); 7¹⁰|det(C+4I) closes identically (no obstruction); rigid
  triangle env V=3+36+60; 4-vertex flag affine line (1 DOF, M∈[0,218295]).
- **LEVERAGE has migrated to s=−4 GEOMETRY.** Star-complement reconstruction is the only
  Aut-AGNOSTIC decision route (reaches the asymmetric/trivial-Aut case, unlike the paused Z3
  orbit-matrix route). Cloud-spec for a thin vertical slice drafted (generate constraint-valid
  55-vtx H; measure column-set |B(H)|; characterize failure CATEGORIES before scaling).

## R31 — STAR-COMPLEMENT spectral/lattice route EXHAUSTED (real-graph witnesses; no kill);
## tightened constraints; leverage → CRS column-compatibility (combinatorial realizability) (iter 20).
- **NO Aut-agnostic kill, and provably none from spectral/lattice here:** every forced invariant
  (10-dim integral λ=3 eigenspace; A_H+4I PD; corank_F2(A_H+I)≥m; corank_F7(A_H+4I)≥m; even-lattice
  identity; 7^m|det) is SATISFIED by a real s=−4 graph (Kneser K(7,2)=srg(21,10,3,6), calibrated) ⇒
  cannot obstruct srg99. The spectral/moment/lattice relaxation is FEASIBLE across the whole window
  (explicit exact 2-atom witness at e=319). All necessary-only, with witnesses.
- **NEW verified tightened constraints** on a 55-vtx s=−4 star complement H: **e(H) ≤ 319** (binding;
  was 384; ≤305 if m≥18; the 363-vs-319 discrepancy resolved — same mechanism, 319 sound);
  **m=mult₃(H) ∈ [10,30]** (m≤30 from trace=0 + all-other-eig>−4 ⇒ 7m<213); **W0-orthogonality
  column filter** (every CRS star column ⊥ H's 3-eigenspace, dim=m; ~60× cut; verified on real
  Kneser); structural margin n−m_r−m_s = 1.
- **LEVERAGE:** spectral exhausted ⇒ a kill can only come from COMBINATORIAL REALIZABILITY = the CRS
  column system {44 columns b∈{0,1}^55, bᵀadj(M)b=4det(M), pairwise-compat ∈{0,det}, all ⊥W0, each
  support 7K2-compatible}. SUFFICIENT-direction & razor-tight (max clique=m_s, unique reconstruction
  on calibration graphs). Cloud-spec refined (Stage A 55-vtx gen w/ modular-corank + e≤319 cuts;
  Stage B W0-filter→column-form→44-clique→verify; gates Kneser/rook9/srg(40,12,2,4)). Stage A gen is
  the wall (~ the paused Z3 cell).

## FRONTIER (after iter 21 / R32-R33): pure-math NO-SEARCH surface is EXHAUSTED on BOTH cases.
Symmetric (Z3/f=0): reduces to a compute wall (BLISS/recursive cell certification, paused→cloud).
Asymmetric (s=-4 star complement): EVERY necessary invariant reachable by reasoning — spectral,
integral-lattice/theta, moment/Krein, p-rank (7 & F2), permutation-character, topological/homological,
AND the full CRS column over-determination — has an explicit REAL-GRAPH WITNESS (Kneser srg(21,10,3,6)
& srg(40,12,2,4) at s=-4; rook9/BvLS for the family); the over-determination holds even at the tightest
margin-0 packing. No invariant slot remains for an Aut-agnostic no-search kill. The ONLY decisive route
left is the cloud star-complement SEARCH (CLOUD_SPEC_SC.md: isomorph-free 55-vtx H-gen w/ mult₃∈{10,11}
+ full-W0 prefilter + e≤319/363 + corank cuts → per-H column CSP; Stage-A generation is the wall).
New verified yield this iter: mult₃(H)∈{10,11}; e(H)≤363 (counting); F2 facts A²≡A, rank₂(A)+rank₂(A+I)=n;
integer homology H₁=ℤ³⁶⁴,H₂=0,χ=−363. No kill.

## R34 RESULT (iter 22): mult₃(H)=11 margin-0 branch is CONSISTENT — Kneser-witnessed, NO kill.
Both attacker + fresh-context verifier (independent, exact, calibrated on the 7 real Kneser margin-0
SCs): the kill-chain rejects 0/7 real witnesses ⇒ cannot fire. The probe's "sparse weight-1" hope was
FALSIFIED (margin-0 ⇒ MAXIMAL column weight / e(H)=45 dense end on Kneser; the squeeze runs backwards).
NEW exact relation 2e(H) ≥ r²·m₃·n_H/(n_H−m₃) (0 violations / 35917 Kneser SCs; gives only e≥62 for
srg99 at m=11, below the 154 combinatorial floor ⇒ doesn't pin); re-tightening e(H)≤358 at m=11; srg99
window robustly non-empty (205 e-values [154,358]). A real-graph witness caught what would have been a
FALSE kill — the discipline held.

## LOCAL-MATH LOOP COMPLETE (after iter 22). Pure-math NO-SEARCH surface is VERIFIED-EXHAUSTED on BOTH
the symmetric case (→ compute wall) and the asymmetric case (every necessary spectral/lattice/p-rank/
topological/column invariant has a real-graph witness; the last residual mult=11 branch is consistent).
The ONLY decisive route left is the **cloud star-complement SEARCH** (CLOUD_SPEC_SC.md: isomorph-free
55-vtx H-gen w/ mult₃∈{10,11}, full-W0 prefilter, e≤319 + corank cuts → per-H column CSP; Stage-A
generation is the wall, a distributed-nauty engineering job; deliverable = characterized frontier, not
a guaranteed close). Further LOCAL reasoning rounds would re-confirm "consistent, needs search" (the
work itself, R33+R34, states this). DECISION IS THE USER'S (paid cloud compute / new direction /
conclude) — surfaced via AskUserQuestion. Do NOT spin more local no-search workflows.

## USER DECISION (post-iter-22): "SHRINK THE CLOUD-SPEC LOCALLY." The loop now loops on tightening
the Stage-A star-complement generation (the sole cost driver N_A) + hardening CLOUD_SPEC_SC.md, no
heavy local compute, every predicate verified non-over-pruning on real s=−4 graphs. (Iter 23 = R36-R38:
12-filter sound pipeline; forbidden set {K4,diamond,K2,3}; F7 interlacing online reject; excised the
deg≤k−1 over-pruner; cost model — wall is the SPECTRUM not degrees.)

## R39 RESULT (iter 24): F7→envelope. SHIPPED **F8b′ hereditary PD reject** (λ_min(partial_k)>−4 at
every depth; bordered-LDL O(k²); fires ~100% of dense partials by k=46, kills 41.5% of random growth
paths, catches the −4-OVERSHOOT F7's lower bound misses; 0 false-reject EXHAUSTIVE on all 32767 induced
subgraphs of a maximal Kneser SC) — MATERIAL N_A reduction at the cost-center levels. F7 upper-window
mult₃≤66−k: sound+free but 0 mid-tree prune (leaf-tight cross-check only). det-7 growth: honest NO
(reduces to F7 / would over-prune). Folded into CLOUD_SPEC_SC.md. The mid-tree gap is now on the
LOWER/undershoot side (real partials undershoot mult₃; F7's k−45 floor is loose for k∈[38,50]).

## ONLINE STAGE-A PRUNING EXHAUSTED (after iter 25 / R40-R42). The cloud-spec is HARDENED & READY.
Iter 25 verdicts (single-agent, restart-robust; verified): (A) hybrid mult₃ lower bound is PROVEN VOID
(g≡0, exact LP-duality — a 0-mass-at-3 measure always matches the forced moments ⇒ the moment route
can never beat the k−45 interlacing floor; spectral wall interlacing-tight mid-tree on the lower side);
(B) forbidden-induced-subgraph set COMPLETE through 6 vtx ({K4,diamond,K2,3}; the only candidate fires
iff induced-diamond, already shipped). NEW final cut SHIPPED: **F8c′** (hereditary λ₂ cap — srg99 has
exactly one eigenvalue >3 ⇒ every partial has ≤1 eigenvalue >3; prune if λ₂>3; fires early k≈34-42,
top-of-spectrum; verified 0/80000 real subs). Now F8b′(bottom>−4)+F8c′(top≤1)+F7(mid mult₃) box the
partial spectrum into (−4,3] save the Perron top. EVERY online-sound lever has a verdict; the residual
mid-tree gap is PROVABLY not closable by a forced online predicate (it's λ=1/μ=2 local structure,
already enforced). The structural lever (eigenspace-first / generation order) was assessed (R36) with
NO first-order N_A gain. ⇒ local spec-shrinking is COMPLETE.

## BIG SHRINK (R43): primary Stage-A switched to the **r=3 (45-VERTEX)** star complement — ~b^−10
(3–10 orders) cheaper than the 55-vtx s=−4 object (depth=#SC-vertices, 45<55), at ~0 mid-tree pruning
loss (F1–F6 + F8c′ transfer; F8b′ PD→PSD costs ~0 mid-tree; F7 was above the 45 ceiling). CRS
A_X=3I+Bᵀ(A_{H'}−3I)⁻¹B validated EXACT on real T(7)=srg(21,10,5,4) (150/150, 0 false-reject /6842 subs).
Spec §7 = r=3 primary, s=−4 55-vtx = calibrated fallback. (45 is the MINIMUM useful SC: mults are 1,54,44
⇒ SC sizes 98,45,55.) Online pruning was already exhausted (R40-R42); this is a STRUCTURAL win, the
largest available, and it likely makes the search a single-node job rather than distributed.

## NEXT ACTION (resume here)
Iter 27: make the r=3 thin slice TURNKEY so the decisive measurement is one command. Build a complete,
instrumented r=3 Stage-A generator (canonical augmentation via nauty/BLISS, seeded; online gates F1–F6
+ F8c′ + PSD λ_min≥−4 + e-band(45) + triangle-split) → per-H' 54-column W0-orthogonal CSP → exact 0/1
closure verify. Instrument the canonical-augmentation NODE COUNT (to MEASURE the residual branching b =
the only remaining unknown behind the b^−10 magnitude) + the per-H' CSP failure-category histogram.
LIGHT-validate it reconstructs a real r=3 graph (T(7)) and runs a tiny-scale slice to ESTIMATE b (light
local compute = validation only; the full measurement is the cloud run). Output: the runnable harness +
a measured/estimated b and projected N_A; if b is small enough the search may be feasible on one cloud
node. THEN the decisive step is to RUN the slice (cloud, per user directive). Prefer SINGLE foreground
agents (sessions cycling). Verify on reals; no bluffing; honest if b turns out large.

## TERMINAL STATUS (pre-resource; SUPERSEDED by R25/R26/R27/R28/R29) — was: complete pending external res.
All single-machine compute routes AND the literature lever are now exhausted; the problem remains
OPEN (as since Conway 1975). No route was a relabeled timeout. Remaining levers are strictly
EXTERNAL: (a) C-level nauty/Traces or distributed completed-tree compute → close a Z₃/f=0 orbit
cell (the exact `ir_canon` engine is ready to drive); (b) genuinely new mathematics — a global
obstruction (every cheap/medium one is non-obstructing; the parameters are too well-behaved).
RESUME ONLY IF: a C toolchain / nauty binary / distributed compute becomes available, OR the user
repurposes the loop (e.g. to the other open family members 6273/494019, or a different problem).
Continuing identical single-machine workflows would only re-discover the known walls.

## (iter 17 plan — DONE as R24: Makhnev recovered+verified, n3≥3 proven, terminal)
Iter 17 (ultracode Workflow): the LAST substantive NON-compute lever before the loop is
external-resources-bound — the Makhnev/n3 question, which bears DIRECTLY on nonexistence and is
research/mathematics, not a compute wall. (A) RETRIEVE Makhnev 1988 (Mat. Zametki 44(5):667-672;
Eng. Math. Notes 44(5):847-850; mathnet mzm4220) — its actual theorem on srg(λ=1) and the cited
conditional "n3=0 ⇒ no srg(99,14,1,2)"; deep web/academic retrieval (agent-reach, Springer,
mathnet, secondary sources, translation). VERIFY or REFUTE the conditional rigorously if
obtainable. (B) attack "is n3 forced?" — n3 = #{H3: two vertex-disjoint triangles joined by
exactly 2 edges}; found free locally (only 3|n3, n3∈[0,4158]). Push for a GLOBAL forcing/exclusion
(triangle-design structure + GF(7) invariants + order-≥6 counting + equitable partition under the
tiny Aut). If n3 is pinned AND Makhnev's conditional verifies ⇒ decisive. Adversarially verify
both. HONEST EXPECTATION: n3 likely stays free and Makhnev is only conditional — in which case ALL
single-machine levers are exhausted and the end-state is "COMPLETE pending external resources";
report that plainly and recommend the user provide resources / repurpose / conclude. Verified-only.

## (iter 16 plan — DONE as R23: a=24 walls even with exact pure-Python canon; nauty unavailable)
Iter 16 (ultracode Workflow): the LAST concrete lever + a fresh literature cycle. (A) NAUTY-BACKED
CLOSURE: install pynauty/nauty (or call the nauty/Traces binary); build ONE canonical-augmentation
orbit-matrix search using nauty's canonical labeling over the structure group Aut_empty × S₂₇ (the
form that is both leading-row-strong and full-depth-sound — the exact gap R22 proved pure-Python
can't fill). VALIDATE idempotent on rook(9) + BvLS quotients first. Then drive a=24 ct=(6,) and
ct=(3,3) to a COMPLETED tree → INFEASIBLE (increment beyond Behbahani) or SAT (lift to 99). If
nauty is unavailable or still walls at t=33, report that exactly. (B) FRESH DEEP-RESEARCH: the
field is active (Reimbayev 2024/2025, Pernazza–Reimbayev 2025) — re-survey 2024–2026 for any NEW
technique on Conway-99 / srg(λ=1,μ=2) / feasible-SRG nonexistence that is PORTABLE and not yet
tried (now that the problem is deeply understood); if one exists, scope a concrete attack. Verify
both. HONEST END-STATE CONTINGENCY: if (A) walls and (B) finds nothing portable, the systematic
single-machine attack surface is exhausted — declare the program COMPLETE pending external
resources (distributed canonical-augmentation compute, or new mathematics), and recommend the
user conclude or repurpose the loop. Record verified-only.

## (iter 15 plan — DONE as R22 ×2: a=24 walls (sound), non-composability + CGSS-void)
Iter 15 (ultracode Workflow): program is CONSOLIDATED (FINAL_REPORT.md). Two veins, honoring
"keep trying". (A) ONE more engineering attempt to CLOSE the a=24 cell with the identified next
lever: FULL per-row column-orbit canonicalization with proven soundness at depth ≥3 (nauty-style
isomorph rejection at EVERY row, not just leading rows) + the within-row intersection cut;
go/no-go = push max_row well beyond 8, ideally certified exhaustion of a=24 (= a real increment
beyond Behbahani). (B) FRESH CREATIVE CYCLE — scamper-style ideation for genuinely NEW global
angles NOT yet tried (exclude the closed list in FINAL_REPORT §2), informed by the full state
(esp.: non-vertex-transitivity KILLS Cayley/partial-difference-set approaches; the lift-theorem
kernel structure; locally-linear-graph / Moore-geometry nonexistence theory; the BvLS ternary
algebraic template); attack the single most promising with a concrete computation validated on
reals. Adversarially verify both. Honest expectation: a=24 likely still walls (33 rows, migrating
bottleneck); the creative vein is the hedge for a genuinely new idea. If BOTH stall, the honest
end-state is "frontier reached, program consolidated; further progress needs distributed compute
or new mathematics" — and the loop should report that plainly. Record verified-only.

## (iter 14 plan — DONE as R21: within-row wall broken, frontier confirmed, consolidated)
Iter 14 (ultracode Workflow): attack the DIAGNOSED bottleneck (within-row A1-fill width ~10⁷),
NOT the inert symmetry lever. Reformulate the orbit-matrix search so a single row cannot blow
up: branch on per-pair bilinear DEFICITS with a column-intersection / Gram-feasibility cut
applied INCREMENTALLY during row construction (treat each candidate empty-orbit row as a
vertex-neighbourhood whose pairwise λ=1/μ=2 intersection counts with all already-placed rows
are enforced at PARTIAL width, so most of the ~10⁷ completions die early) — the design/clique
incremental constraint the prior engines applied only at row-close. GO/NO-GO GATE: the
reformulation MUST complete ROW 2 of the a=24 ct=(6,) cell within budget (the prior wall)
before claiming anything; validate it recovers rook(9)+BvLS quotients first. If rows complete,
drive a=24 to certified exhaustion (INFEASIBLE = increment beyond Behbahani; SAT = lift to a
99-vertex graph). If it ALSO stalls at within-row width, the frontier is confirmed with the
CORRECT lever ⇒ CONSOLIDATE: write the final report of the whole program. Record verified-only.

## (iter 13 plan — DONE as R20: 0/4 cells closed, genuine compute frontier; retained for trail)
Iter 13 (ultracode Workflow): we are AT the published frontier — Behbahani's Z₃/f=0
orbit-matrix cell is a literal "?" (his dedicated search never closed it; our CP-SAT timed out
at the SAME wall). Concrete published-grade target: drive the FOUR spectral classes
(a=24:T27,E6 / a=22:T20,E13 / a=20:T13,E20 / a=18:T6,E27) of the f=0 quotient (R²=6J−R+12I,
forced profiles, the 252-piece class×A2-cycle-type decomposition) to CERTIFIED EXHAUSTION with a
DEDICATED orbit-matrix enumerator + the MISSING ingredient: canonical orbit-labeling
symmetry-breaking (lex-leader on the relabel automorphisms — what makes orbit-matrix exhaustion
finite-in-practice) PLUS the verified A2-3-cycle A1-neighbourhood disjointness lemma as a hard
pruner. Start with a=24 (smallest). Per cell: INFEASIBLE = an increment Behbahani never achieved;
SAT = lift to a 99-vertex construction (historic — triple-check). ALL FOUR INFEASIBLE ⇒ Z₃/f=0
RULED OUT ⇒ with order-11-out + Cesarz–Woldar bounds the prime-order symmetry picture is fully
closed. VALIDATE the enumerator on a real Z₃-symmetric SRG's quotient first; adversarially verify
any verdict by an independent method. Honest expectation: a=24 may close; larger classes may hit
the wall — report how many cells closed. If cells stay open we are at the genuine compute
frontier — consolidate + report. Record verified-only.

## (iter 12 plan — DONE as R19 ×2: p=7 window + Z3 inconclusive; retained for trail)
Iter 12 (ultracode Workflow): the rank-overflow / no-flat-climb kill path is CLOSED
(R18: an exact realizable FLAT at a rank-34 node, ww-complete, breaks the strict +1-climb
premise — the census underpinning it was ww-restricted; rank-44 dead-ends cannot be bridged
to nonexistence). What SURVIVES & is reusable: the lift theorem (97.3% ball-infeasible types
non-flat node-universally), the rank-44-only lemma, the engine, the squeeze-ratio separator,
the K constant-diagonal=39/80 / denom-91=7·13 structure, and the debunked n3 path. PIVOT to
GLOBAL obstructions that do NOT depend on a per-node rank climb. TWO veins. (A) **Z₃ f=0
orbit-matrix case** (still genuinely OPEN; CP-SAT timed out at iter 9): attack the 33×33
quotient (R−3I)(R+4I)=6J with a STRONGER method — dedicated orbit-matrix enumeration
(Behbahani–Lam style), eigenvalue/interlacing + integrality on the quotient, or a better
SAT/ILP encoding with symmetry breaking — to DECIDE it (rule out a Z₃-symmetric srg99 = a real
partial result, or construct one). (B) a genuinely NEW global obstruction: candidates — the
231-triangle resolvable design as a global object (large sets/parallelism); a global p-rank /
Smith-normal-form argument at p=7 (r≡s mod 7) or via the emergent denom-91=7·13 structure; or
a global counting identity. Survey what is untried (CLOSED: rank-overflow, spectral/Krein,
local-SAT, two-graph, geometric/pg, SOS-deg-2, n3) and attack the most promising with a
concrete computation validated on rook(9)/BvLS(243). Adversarially verify both. Honest
expectation: a Z₃-subcase result and/or a new structural constraint; a full kill remains
unlikely. Record verified-only.

## (iter 11 plan — DONE as R18: rank-overflow kill path FALSIFIED; retained for trail)
Iter 11 (ultracode Workflow): R17 PROVED the 97.3% ball-infeasibility class non-flat
node-universally (the LIFT THEOREM). The SOLE remaining gate to closing gap (i) is the
residual **5760 in-colspace slot-partition types**, all with fixed |w_U|²=41/80, needing
the shell to supply perp-norm exactly R²=39/80. Two veins. (A) NODE-PARAMETRIC PROOF:
express e^T K⁻¹e − R² as an EXACT rational function of the shell-coupling sign pattern +
free growth parameters, and prove it is bounded away from 0 over the WHOLE realizable
parameter family (Positivstellensatz / exact-SOS / interval-arithmetic-over-ℚ) — turning
"flat=0 at tested nodes" into "flat=0 universal" and closing gap (i). (B) AGGRESSIVE
FALSIFICATION targeting the SEED-7-type nodes where R² lands INSIDE the achievable perp-norm
band (the fragile case, blocked only by a lattice non-hit): drive many such nodes across
fillings and run the COMPLETE exact joint flat-test on the residual class, hunting one
realizable flat (norm==1, in-colspace) — a flat node FALSIFIES the kill (equally valuable;
the in-band fragility says it may exist). Do NOT touch the forced-funnel (gap ii) until (i)
is settled — they are entangled and (ii) presupposes (i). Keep ALL soundness gates wired
(srg85 fires; BvLS flat-test detects real flats). Record verified-only.

## (iter 10 plan — DONE as R17; retained for trail)
Iter 10: the rank-44 node is now a COMPLETE exact ww-exhaustive dead-end (R16, done). The
SINGLE remaining gating link to a KILL is: **prove no-flat-step is geometrically FORCED at
EVERY realizable node rank 31..43** (then rank climbs strictly 31->44 by n<=52 along EVERY
branch, every path dead-ends, the rank-31 ball cannot reach 99 -> no srg99 with an identity-
filled triangle-ball; the rank32..36 fillings are MORE squeezed). This is a clean falsifiable
geometric claim. Routes, in priority:
  (a) ANALYTIC PROOF of no-flat: show a unit vector with cosines (-2/7 to its 6 ball-nbrs,
      1/28 to the rest) can NEVER lie in the s-eigenspace span of a realizable srg99 partial
      config (dim 44) — likely from the 7K2 local structure + the exact cosine arithmetic
      (the ball-INFEASIBILITY mechanism: b_ball not in colspace(G_BB) was the dominant kill at
      the rank-44 node — 23728/25627 — so the analytic target is 'the forced ball-cosine
      vector is never in the ball sub-Gram's column space for a flat step'). Contrast with why
      BvLS's (-5/22,1/55,dim110) DOES admit flats (its ball-cosines ARE in-colspace).
  (b) BROAD FALSIFICATION: run the flatdirect+joint complete flat-test at MANY independent
      rank-44 nodes (different seeds/fillings rank 32..36) — a SINGLE flat-admitting node
      FALSIFIES the kill and is equally valuable. (So far: 4 nodes all-overflow via ball-scan;
      1 certified complete-dead-end exactly.)
  (c) NODE-FORCED: argue/measure that a real srg99 growth is FORCED through a rank-44 node
      (no-flat-forced gives this); or find a flat-admitting node that evades it.
  (d) cross-check vs the Z3 vein for a combined symmetric+geometric certificate.
Keep ALL soundness gates wired (srg85 fires; BvLS no false-fire AND flat-test detects real
flats). Record verified-only; a flat-admitting node is as valuable as a dead-end.

## SUPERSEDED NEXT ACTION (iter 9 plan, now done as R16 vein B)
Iter 9 (ultracode Workflow): exploit SYMMETRY REDUCTION to make the rank-44 frontier
reachable, attacking two fronts. (A) **Z₃-symmetric subcase (still LIVE per R9):** a
Z₃ automorphism gives a ~33-orbit quotient — far smaller. Run the realizability +
rank-overflow enumeration on the Z₃-symmetric structure (orbit matrix (B−3I)(B+4I)=6J,
f∈{0,3}); it may be EXHAUSTIVELY certifiable → either rule out Z₃-symmetric srg99 (a
real partial result extending Behbahani–Lam with the new geometric engine) or, if a
rank-44 zero-survivor node appears, a kill of that subcase. (B) **General engine:** use
block-relabel WLOG + the rank-44-only lemma to drive ONE high-rank chain to a rank-44
node and attempt an exhaustive zero-survivor certificate there (adversarially verify
hardest if it fires; capped scans are NEVER proof). Keep soundness gates wired in.
Realistic expectation: a verified Z₃-subcase result + deeper general consistency, not a
full kill. Record verified-only; validate every step on rook(9)/BvLS(243).

---

## ITER (VEIN: Falsification sweep + forced-funnel across many rank-44 nodes) — IN PROGRESS

**Goal:** decisively stress the no-flat lemma at MANY INDEPENDENT rank-44 nodes (diverse
fillings ball-rank 31..36 + diverse seeds), not just the one identity-chain node. Hunt a
single flat-admitting node (would FALSIFY the kill); else confirm all-dead-end across nodes.

### New machinery (this iter)
- `flat_node_test.py` — flat_test_node(P,fac,lab): the COMPLETE exact ww-exhaustive flat-test
  (flatdirect partition + rank44_joint's e^T K^{-1} e == R^2 over all 2^ns, float-screen +
  exact confirm; no_screen option; handles singular-K via colspace(K)). VALIDATED: reproduces
  the saved rank-44 node partition EXACTLY (37253 wwimp / 23728 ballinfeas / 1899 fellback /
  0 flat / 0 near-hits / partition_ok). 226s.
- `sweep_rank44_multinode.py` — reaches many rank-44 nodes from consistent_taus (matching-auto
  + random S12 fillings spanning ball-rank 31..36) x seeds, runs flat_test_node on each.
- `sweep_intermediate_noflat.py` — geom flat-census (noflat_forced.geom_classify_node) at every
  node along diverse chains/fillings; alarm if any node has FLAT>0 (climb-skip).
- `funnel_separation.py` — quantifies srg99 tight 13-step funnel vs BvLS loose (dim_s at n=191).

### SOUNDNESS GATES (all re-run GREEN this iter)
- BvLS reals all-flat at rank-110: 52/52 flat, 0 overflow (reals_flat_at_dim.py). PASS.
- srg85 5*K7 fires rank35>34; srg99 coclique45 fires; ball quiet (deep_cert_sanity.py). PASS.
- Joint flat-test DETECTS real flat on BvLS rank-110 node (border in colspace, norm==1)
  (joint_reals_gate.py). PASS — the test is NOT blind to flats.

### Reached (in-flight) — sweep collecting rank-44 nodes from diverse fillings/seeds
- node#1 ballrank31 seed1: 31->44 strict +1, n=52
- node#2 ballrank31 seed2: 31->44 strict +1, n=52 (distinct chain)
- node#3 ballrank33 seed1: 33->44, n=50 (higher filling reaches 44 FASTER, as predicted)
- node#4 ballrank33 seed2: 33->44, n=50
(flat-test verdicts pending; intermediate no-flat + funnel separation running in parallel)

### VERIFIED RESULTS (this iter) — multi-node falsification sweep

**5 INDEPENDENT rank-44 nodes, exact ww-exhaustive flat-test, ALL complete dead-ends (0 flat):**
Decoupled reach (reach_and_save.py / reach_more.py) from flat-test (flat_test_saved.py) to fit
process limits. Each node freshly grown (NOT the original saved pickle). Partition = exact
solve_with_factor over Q + e^T K^{-1} e == R^2 over all 2^ns (float screen + exact confirm).

| node | filling ball-rank | seed | n  | ns | ww-imp | ball-infeas | norm>=1 | fellback | near | FLAT |
|------|-------------------|------|----|----|--------|-------------|---------|----------|------|------|
| 0    | 31 (identity)     | 1    | 52 | 13 | 37253  | 23728       | 0       | 1899     | 0    | **0**|
| 3    | 31                | 2    | 52 | 13 | 37226  | 23738       | 0       | 1916     | 0    | **0**|
| 4    | 31                | 3    | 52 | 13 | 35869  | 24958       | 0       | 2053     | 0    | **0**|
| 1    | 34                | 1    | 49 | 10 | 32434  | 26733       | 0       | 9023     | 0    | **0**|
| 2    | 35                | 1    | 48 | 9  | 31832  | 16284       | 6816    | 13258    | 0    | **0**|

- 3 DISTINCT filling classes (ball-rank 31/34/35) x multiple seeds. Every partition DIFFERS
  (fellback 1899->9023->13258 as ball-rank rises / perp space shrinks) -> genuinely distinct
  configs, NOT relabels. ALL zero-flat, partition_ok=True, 0 near-hits, not timed out.
- => the rank-44 dead-end is NOT an artifact of the identity chain. It recurs across
  independent fillings AND seeds. NO falsifying (flat-admitting) node found. NO-FLAT
  STRENGTHENED at the rank-44 frontier across the filling-class span.
- Note: ball-rank 36 fillings are slower to reach rank-44 (more constrained) -> not in the
  tested 5 within budget; identity (rank 31) is the slowest-funnel / hardest case and IS
  covered (3 seeds).

**FORCED-FUNNEL separation (funnel_separation.py / bvls_funnel) — CLEAN:**
- srg99 (FUNNELED): every realizable step climbs +1 (0 flat at the ball + every reached node);
  dim_s=44 hit in EXACTLY 44-rkBall steps -> ball-rank 31: 13 steps (n<=52); 33: 11; 35: 9.
  Full s-eigenspace saturated by n<=52, far below 99. No flat relief anywhere on any chain.
- BvLS(243) (NOT funneled): dim_s=110 reached only at vertex #191; 81 flat/dependent steps
  (rank plateaus) below dim_s. rank does NOT climb every step; dim_s spread over n=191>>110.
- SAME exact geometry: srg99 tight 13-step funnel (0 flat) vs BvLS loose plateau curve (81
  flat). The funnel is SPECIFIC to srg99 -> genuine over-constraint, cleanly separated.

**3 SOUNDNESS GATES re-run GREEN in this iter:** BvLS reals all-flat 52/52 @ rank-110;
srg85 5K7 fires (35>34) + srg99 coclique45 fires + ball quiet; joint flat-test DETECTS the
real BvLS flat (border in colspace + norm==1). The kill mechanism does NOT false-fire on reals
and is NOT blind to flats.

**NEXT ACTION:** (pending) node-2 no-screen paranoid exact pass (confirm float screen hid no
flat; 0 near-hits already implies this) + lean intermediate geom-census at ranks 33..43 across
diverse chains (confirm no climb-skip mid-funnel). Then this vein is complete: 5 independent
rank-44 dead-ends + clean funnel separation; no falsifier; gates green.

### FINAL (this iter) — 7 nodes tested, all dead-end; no-screen + intermediate confirmed

Extended to **7 INDEPENDENT rank-44 nodes** across ball-ranks 31/34/35/36 (the FULL filling-
class span) x seeds. Added nodes 5,6 (ball-rank 36 = FURTHEST from identity):
| node5 ballrank36 n47: wwimp26525 ballinfeas0 norm>=1=17449 fellback24617 -> FLAT 0
| node6 ballrank36 n47: wwimp28318 ballinfeas0 norm>=1=9938 fellback30879 -> FLAT 0
ball-rank 36 has ball_infeasible=0 (ball span large enough that all ball-cosine vectors ARE
in colspace); the prune shifts to norm>=1 + fellback. The DOMINANT kill sub-mechanism shifts
with filling (identity: ball-infeasibility 23728; rank36: fellback/norm) but OUTCOME (0 flat)
is INVARIANT -> the dead-end is robust to which sub-mechanism prunes.

**Structural identity (exact, verified all 7 nodes): ns(shell) == dim_s - rkBB == 44 - rkBB.**
The shell vectors exactly saturate the perp complement of the ball in the s-eigenspace, so the
perp-Gram K is square ns x ns, full-rank, invertible at EVERY rank-44 node (not just identity)
-> the e^T K^{-1} e == R^2 joint flat-test is the clean exact-invertible case universally.

**NO-SCREEN paranoid pass (node 2, 795s): IDENTICAL to float-screen (0 flat, 0 near-hits,
partition_ok).** Pure-exact enumeration over ALL 2^9 patterns x every fellback pick -> the
float pre-screen hid no flat. (0 near-hits already implied this on every node.) Machinery sound.

**Intermediate no-flat (sweep_intermediate_noflat, 8 chains, ball-rank 31/34/35/36, ranks
33..39): FLAT-total=0 on EVERY censused node** (climb>0, over=0, nonpsd large). Distinct climb
counts per node (4239..30456) = distinct configs, all flat-free. No climb-skip mid-funnel.

CALIBRATED VERDICT: searched HARD for a falsifier (flat-admitting rank-44 node or climb-skip
intermediate node) across 7 rank-44 nodes (3 distinct filling classes + ball-rank 36) + ~14
intermediate nodes; found NONE. The rank-44 dead-end is NOT an identity-chain artifact -- it
recurs across the filling-class span with invariant 0-flat outcome. Funnel cleanly separates
srg99 (tight 13-step, 0 flat) from BvLS (dim_s at n=191, 81 flat steps). 3 soundness gates
green. This STRENGTHENS the no-flat lemma toward universality; it is NOT a proof (universal
no-flat over ALL reachable nodes remains the open gating gap -- finitely many tested, not all).

**NEXT ACTION:** the 2 gating gaps remain: (i) a CLOSED-FORM universal no-flat proof (every
rank 31..44 node, not finite sampling); (ii) forced-funnel as a theorem. The sweep gives strong
empirical support + the exact structural identity ns=44-rkBB (a lever toward a closed-form
perp-Gram argument). Pursue the algebraic universal proof next, not more sampling.

---

## ITER (VEIN: Node-parametric proof e^T K^-1 e != 39/80 for residual 5760) — IN PROGRESS

**Goal:** close gap (i) via a node-universal denominator/lattice/SOS argument that
e^T K^{-1} e (perp-norm of the unique shell completion) is bounded away from / never equals
R^2 = 39/80 over the residual 5760 in-colspace types at every reachable node.

### GROUND-TRUTH probes (exact, this iter)
- `denom_probe.py` / `denom7_probe.py` / `compat_probe.py` / `prime_struct.py` / `integerize.py`.
- **5-adic argument FALSIFIED:** all 8192 q=e^T K^{-1} e have v5(denom)=1, exactly matching
  39/80 (=39/(2^4·5)). The prime 5 is NOT excluded. A pure "5 never appears" obstruction is FALSE.
- **7-adic argument FALSIFIED:** a substantial fraction have v7(denom)=0 (seed1: 1210/8192;
  seed7: 167/8192), matching 39/80's 7-free denom. No clean 7-adic exclusion.
- **REAL denominator mechanism (node-dependent):** det(K) numerator carries LARGE primes
  (seed1: 13·48420271; seed7: 31·569·34537) and ALL 8192 q-denominators carry a prime>7
  (8192/8192 at both nodes) -> denom never divides 80 -> q != 39/80. But the big primes are
  NODE-SPECIFIC (differ per node), so this is a per-node certificate, NOT yet universal.
- **No uniform gap lower bound:** min|q-39/80| varies & shrinks across nodes (seed1 .0229,
  seed7 .0110, seed3 .0059). Fragile-in-band confirmed; no clean uniform lattice non-hit.

**HONEST STATUS:** a single-prime denominator obstruction does NOT close gap (i). The exact
mechanism (big primes from det(K) numerator survive into every q-denominator) is real and
gives a per-node certificate at every tested node, but is node-dependent. Pursuing: (a) a
node-universal reason the big primes never cancel, OR (b) partial closure by node-class.

**NEXT ACTION:** census obstruction-type per node (clean min-bound vs in-band-lattice) and
quantify which fraction of 5760 x node-classes is closed by a clean bound.

### CONTINUED (this iter) — structural reformulation + falsification

**NODE-UNIVERSAL STRUCTURE FOUND (the brief's hoped-for K-structure), verified exactly:**
- `kdiag_universal.py`: the perp-Gram K has CONSTANT DIAGONAL = R^2 = 39/80 at EVERY node
  (ranks 34/37/40/42/44, seeds 1/2/3/5/7/99). PROOF: every placed shell vertex is itself a
  realizable (2,2,2)/eo=0 attachment to the same identity ball, so |proj_U g_s|^2 = 41/80
  (node-INDEPENDENT ball value), hence K[s][s] = 1 - 41/80 = 39/80 = R^2. So K = R^2 * M with
  M a UNIT-DIAGONAL CORRELATION matrix (PSD).
- `cs_bound.py` / `selfsimilar.py` / `mod91.py`: SELF-SIMILAR REFORMULATION. With M=K/R^2 and
  p_s=e_s/R^2, the flat condition e^T K^{-1} e == R^2 becomes EXACTLY  p^T M^{-1} p == 1  --
  i.e. "does a UNIT vector d have cosines p_s to the normalized shell-perp unit vectors u_s".
  CRUCIAL: M and p have denominators dividing **91 = 7*13** at every node (the 80/5 VANISHES).
  The whole residual is a self-similar copy of the flat problem, one level down, in clean
  denom-91 coordinates. (Cauchy-Schwarz |e_s|<=R^2 kills ~half the patterns at seed7, none at
  seed1/3 -> CS alone not universal.)

**EVERY SINGLE-PRIME DENOMINATOR / VALUATION ARGUMENT PROVABLY FAILS (honest negatives):**
- v5: all 8192 q have v5(denom)=1 == v5(39/80). 5 NOT excluded.
- v7: 1210/8192 (seed1) have v7(denom)=0 == 39/80. 7 NOT excluded.
- v3: many have v3(q)=1=v3(39/80) (seed3: ALL 8192). 3 NOT excluded.
- In clean denom-91 coords: v7(pMp-1) and v13(pMp-1) both have >=0 entries -> no clean mod-7
  or mod-13 exclusion either.
- REAL mechanism (PER-NODE, not universal): det(K) numerator carries large primes (seed1
  13*48420271; seed7 31*569*34537) that survive into ALL 8192 q-denominators -> denom never
  divides 80 -> q!=39/80 AT THAT NODE. But the big primes are node-specific -> a per-node
  certificate, NOT a universal proof. No uniform gap lower bound (min|q-39/80| shrinks across
  nodes: .023, .011, .006, ... and in the 220-type sweep down to 3.8e-6).

**FULLY CLOSED ANALYTIC CASE: rank-31 ball node (ns=0).** All 5760 in-colspace types have
|w_U|^2 = 41/80 != 1 (node-independent) -> NONE flat. The ns=0 node is closed for ALL 5760,
universally, with no sampling. (lowns_closed.py.) ns=1/2/3 closed by exact finite f_s-value
enumeration (0 flat; closest q approaches R^2 from BELOW: gaps -198/3185, -27/12200,
-3/305270 -> shrinking with ns).

**AGGRESSIVE FALSIFICATION (falsify_lean.py): 11 independent rank-44 nodes (seeds 1-11),
220 in-colspace types each (~2420 type-instances x 2^13 patterns ~= 19.8M exact-screened
completions). ZERO exact flats.** Near-miss gaps shrink to 3.8e-6 (seed6) but NEVER hit 0.
(Crash at seed12 was a None-format bug when sampled types were all ball-infeasible at that
node-class; no flat found, harmless.) NO FALSIFIER.

**SOUNDNESS GATES re-run GREEN:** BvLS rank-110 joint flat-test DETECTS the real flat
(border in colspace + reconstructed norm == 1; in the M-coords pMp would == 1 there) --
the srg99 0-flat is genuine over-constraint, not a blind spot. srg85 5K7 fires (35>34),
coclique45 fires, coclique44 + 39-ball quiet (deep_cert_sanity). The kill is NON-VACUOUS.

**CALIBRATED VERDICT for THIS VEIN (node-parametric e^T K^-1 e != 39/80):** gap (i) is NOT
closed. The hoped-for clean denominator/lattice/single-prime obstruction PROVABLY DOES NOT
EXIST (every prime 2,3,5,7,13 fails; gaps shrink with no positive margin) -> a
Positivstellensatz/SOS uniform bound is very unlikely (no margin to certify). What IS proven
new: (a) rank-31 ns=0 node CLOSED for all 5760 universally; (b) K constant-diagonal=R^2
node-universal structure + the clean denom-91 self-similar reformulation p^T M^{-1} p==1;
(c) per-node big-prime denominator certificate (real but node-dependent). Residual no-flat
remains CONSISTENT-UNPROVEN, now STRENGTHENED (11 more nodes, ns=0 universal closure) and
SHARPENED (the obstruction is a genuine arithmetic non-coincidence in denom-91 coords, not a
clean bound). No exact flat found -> kill NOT falsified.

**NEXT ACTION:** the universal closure, if it exists, is NOT denominator/single-prime. Try:
(a) prove p^T M^{-1} p == 1 impossible via the GLOBAL squeeze (rank=dim_s=44 saturation
forces M's spectrum/structure to exclude unit-reconstruction) rather than arithmetic; or
(b) accept fragility and pursue gap (ii) forced-funnel as the load-bearing argument, treating
(i) as empirically-robust-but-open. Do NOT chase more single-prime denominator arguments
(exhaustively shown to fail).

---

## R19 — p=7 p-RANK / SMITH-NORMAL-FORM GLOBAL OBSTRUCTION: clean WINDOW, NO kill
## (fresh global vein; exact; 11/11 soundness gates green; CERTAIN where machine-checked)

Vein: a fresh GLOBAL obstruction not on the closed list — the Brouwer-van Eijl p-rank /
Smith-normal-form invariants at the special prime p=7 (r=3==s=-4==3 mod 7, so 7|(r-s);
the emergent denom-91=7*13 hint). Scripts (.work/99graph/): prank7.py, prank7_theory.py,
prank7_window.py, prank7_T9.py, prank7_incidence.py, prank7_joint.py, prank7_final.py
(consolidated, 11 gates). All exact (GF(p) Gaussian elim + sympy SNF over Z).

**VALIDATION GRAPHS (the load-bearing setup).** rook(9) and BvLS(243) do NOT share
srg99's special prime: rook9 r-s=3 (special p=3), BvLS r-s=9 (special p=3). srg99 r-s=7
is the ONLY one of the three decidable family members with 7|(r-s) (and it's smallest;
the larger OPEN members 6273/494019 also have 7|r-s). MORE: at p=3 the reals are in a
DIFFERENT branch (3|(k-s)) than srg99 at p=7 (7 does NOT divide k-s=18). So I added a
real out-of-family witness in srg99's EXACT branch: **T(9)=srg(36,14,7,4)** (triangular
graph J(9,2); k=14 like srg99; at p=7: 7|(r-s)=7, 7∤(k-s)=16, 7∤mu=4). And a STRUCTURAL
MIRROR for the incidence claim: **BvLS(243) at p=11** (k=22==0 mod11, only Perron vanishes,
k/2=11==0 mod11 — the exact shape of srg99 at p=7). Both validate every step.

**[C1] SPECIAL-PRIME placement (verified).** Among decidable family members only srg99
has 7|(r-s). p=7 is genuinely its prime.

**[C2] THE WINDOW (AIRTIGHT, the main new constraint).** Let e := rank_7(A+4I)
(= rank_7(A-sI) = rank_7(A-rI) mod 7, since (A-sI)-(A-rI)=(r-s)I=7I==0). Mod-p rank <=
Q-rank, and rank_Q(A-sI)=v-g=f+1=55, rank_Q(A-rI)=v-f=g+1=45; same matrix mod 7
=> **e <= min(f+1,g+1)=45**. Lower e>=1 (since (k-s)=18!=0 mod7 => all-ones not in ker M).
So **1 <= e <= 45**, exact. VALIDATED in-branch: T(9) (and T(5),T(7),T(13)) achieve
e = min(f,g)+1 with EQUALITY, and their SNF(A-sI) divisor multiset is {1^f, mu, 0^g} with
the lone nontrivial divisor = mu (=4), COPRIME to p — i.e. NO 7-adic drop (e=f+1 exactly).

**[C3] MODULE STRUCTURE (verified on T9/rook9/BvLS).** M=A+4I: M^2 = mu*J = 2J mod7;
GF(7)^99 = U(dim1, M acts as k-s=4) (+) W(dim98, M|_W nilpotent, M|_W^2=0). So
e = rank(M|_W)+1, M|_W index<=2. minpoly(M) | (x-4)x^2 (machine-checked: (M-4I)M^2==0 on
all three reals). rank_7(A)=rank_7(M+3I): on U it's 0, on W it's invertible (M|_W+3I, 3!=0)
=> **rank_7(A)=98 FORCED, INDEPENDENT of e**. (Single-collapse Brouwer-van Eijl rule:
only k=14==0 mod7 => rank_7(A)=v-1=98. Validated: T9 rank_7(A)=35=36-1; BvLS@11 =242.)

**[C4] 231-TRIANGLE INCIDENCE p-rank (NEW FORCED INVARIANT).** N = 99x231 point-triangle
incidence; NN^T = 7I+A (diag = 7 triangles/vertex, off-diag = lambda=1 on edges). MOD 7:
NN^T == A. null(A mod7) = <all-ones u> (dim 1, since k=14==0 mod7 with only Perron). u is
NOT line-null (each triangle sums u to weight 3 != 0 mod 7) => left-null(N)=0 =>
**rank_7(N)=99 (FULL ROW RANK), FORCED for every srg(99,14,1,2)**. VALIDATED on the exact
mirror BvLS@11: k==0, dim null(A mod11)=1, u not line-null, rank_11(N)=243 (full) — and on
rook9@2 (gap rank_p(N)-rank_p(A)=+1 in both). The incidence pins rank_7(A)=98 & rank_7(N)=99
but does NOT lower-bound e (A|_W=M|_W+3I invertible for ANY rank(M|_W)), so no e-conflict.

**ADVERSARIAL (no spurious kill).** The near-coincidence e<=45=g+1 vs the rank-overflow
program's dim_s=g=44 is NOT a hidden double-count or new kill: e is a GF(7) rank of A+4I;
dim_s=44 is the exact REAL s-eigenspace dimension (Euclidean Gram program). Different fields,
different matrices, no logical coupling. The '+1' is just the mod-7 reduction of the g+1
Q-rank. The two programs are independent; p=7 does not feed the Euclidean one.

**SOUNDNESS GATES (prank7_final.py, 11/11 PASS):** G1 machinery reproduces BvLS 3-rank
=67 (consistent with its ternary-Golay-code provenance); G2 T(9) e=min(f,g)+1 & SNF 7-free;
G3 BvLS@11 exact mirror -> rank_11(N)=243 full row rank (validates [C4]); G4 single-collapse
rank rule on T9 (35) & BvLS@11 (242). M^2=muJ + minpoly on all three reals.

**CALIBRATED VERDICT (this vein).** The p=7 Smith-normal-form / p-rank obstruction yields a
CLEAN WINDOW e in [1,45] plus TWO forced global invariants (rank_7(A)=98, rank_7(N)=99) for
any srg(99,14,1,2). It is NON-VACUOUS (produces forced invariants, validated in-branch on
T(9) and mirrored on BvLS@11) but NON-OBSTRUCTING: e in [1,45] is fully consistent (e=45 is
the generic triangular-family value, e<45 a permissible 7-adic drop), and the incidence does
not pin e. **No contradiction => NO KILL.** This is the honest "method X is non-void but
provably non-obstructing here" outcome. NEW reusable facts: the airtight e<=45 window; the
U+W minpoly|(x-4)x^2 module structure; the FORCED rank_7(A)=98 and rank_7(N)=99; and the
T(9)/BvLS@11 in-branch validators (reusable for any future p-adic attack on this family).
Reproduces-known: the Brouwer-van Eijl single-collapse rule (cited); the window method is
classical, applied here exactly. Genuinely-new: the specific forced srg99 invariants +
the triangle-incidence full-row-rank fact, none previously recorded in this log.

**NEXT ACTION (resume):** p=7 p-rank is a verified non-obstructing window (closed as a kill
route; the forced invariants rank_7(A)=98 / rank_7(N)=99 are reusable). Do NOT re-attempt
p-rank single-invariant kills. Remaining live global veins: (A) Z3 f=0 orbit-matrix
(genuinely open; task #29 in flight) — strongest dedicated-enumeration target; (B) a 2-source
COMBINED certificate (e.g. couple the forced rank_7(N)=99 line-design rigidity with the
Z3 quotient, or with the eo=0 coordinatization) since neither global invariant alone obstructs.

---

## R19 (Z3 f=0 DEDICATED ORBIT-MATRIX ENUMERATOR, 2026-06-28) — literature VERIFIED from primary source; two validated engines; 252-piece decomposition; INCONCLUSIVE at compute boundary

Scripts: z3_enum.py (pure-Python backtracker, generic in k,lam,mu), z3_enum_validate.py
(rook9 re-find + BvLS 81x81 guided-replay), z3_cpsat_struct.py (structurally-reduced
boolean-A1 CP-SAT), z3_cpsat_struct_validate.py (real-quotient feasible-point soundness).
Full write-up: .work/99graph/Z3_ENUM_FINDINGS.md.

**(1) LITERATURE — read the Behbahani PhD thesis PDF directly (rendered Table 21 page as
image to bypass a scrambled text layer).** GROUND TRUTH:
  - **Thm 4.14 confirmed verbatim**: srg99 auto group primes in {2,3}; order-3 => NO fixed
    points => f=3 RULED OUT, order-3 reduces to f=0 only.
  - **Table 21 (the actual 99-graph)**: the p=3 / f=0 cell is literally "?" (#orb-matrix not
    produced); #srg-found column BLANK throughout. => Behbahani's own search LEFT p=3,f=0
    UNDECIDED. The Z3 f=0 subcase is genuinely OPEN; no later paper (Cesarz-Woldar 2025,
    Crnkovic-Maksimovic 2020) decides bare Z3.
  - **CORRECTION**: the "21989 orbit matrices, ?" figure in the prior Z3_FINDINGS belongs to
    srg(99,42,21,15) (Table 22), NOT the 99-graph. Re-attributed.

**(2) ENGINES (two independent, both VALIDATED non-over-pruning on the REAL graphs).**
  - Backtracker re-finds rook(9)'s 3x3 quotient from scratch (1 sol = real); the real BvLS
    81x81 quotient SURVIVES every prune in a guided replay (no false rejection).
  - Structured CP-SAT (diagonal+A2 fixed; R=A1(bool)+2A2+diag; bilinear identity as boolean-
    AND common-neighbour cardinalities) — the real rook(9) and real BvLS 81x81 quotients are
    FEASIBLE points (pin-true-solution test). A hardcoded-degree bug was CAUGHT by this
    validation before any verdict (ground-truth-first). Propagation hugely improved over the
    old v2 model (5e5-9e5 conflicts in 60-120s vs 154).

**(3) EXACT decomposition.** 4 spectral classes (T,E)=(6,27)/(13,20)/(20,13)/(27,6); A2 =
2-regular cycles (parts>=3) on the E empties; an EXISTENCE decision needs ONE canonical A2
per cycle-type => **252 (class, A2-type) pieces** total (191+49+10+2). NEW lemma (validated):
an A2 3-cycle saturates its edges' bilinear identity by the third vertex, forcing pairwise-
disjoint A1-neighbourhoods of the three empties.

**(4) RESULT — honest compute boundary.** Smallest class a=24 (E=6): both A2-types UNKNOWN at
60-700s (CP-SAT) / no certificate from the backtracker (3e6 nodes/2s). NO piece reached
INFEASIBLE or SAT. Matches Behbahani's "?" and the prior CP-SAT timeout. A capped run is NOT
a proof (hard rule).

**NET (calibrated).** Z3-symmetric srg99 NEITHER ruled out NOR constructed here. Reproduced &
primary-source-verified that f=0 is the sole open prime-order subcase (Thm 4.14); delivered a
second validated engine + the exact 252-piece structure + the 3-cycle lemma as reusable
machinery. The order-3 f=0 enumeration remains at/beyond this harness's compute envelope —
exactly where the literature leaves it. Existence question untouched.

---

## R22 — FRESH GLOBAL ANGLE: locally-7K2 / PLS line-layer + the mu-quad involution (NEW)

Vein: a genuinely new global obstruction NOT on the closed list. Attacked the locally-7K2 /
partial-linear-space (lines = the 231 triangles) structure and the s=-4 integral lattice.
All facts machine-verified EXACTLY on rook9=srg(9,4,1,2) and BvLS243=srg(243,22,1,2) first.
Consolidated reproducible artifact: muquad_theorem.py (runs clean; reproduces all on both reals).

NEW VERIFIED RESULTS:
 [T1] mu-graph = mu*K1 lemma (FORCED, proof from lam=1): the mu common neighbours of any
      non-adjacent pair are mutually NON-adjacent (else edge on 2 triangles). Validated 0 viol.
 [T2] *** mu-quad involution (NEW THEOREM) ***: f:{non-edge {p,q}} -> {its mu-graph {x,y}} is a
      FIXED-POINT-FREE INVOLUTION on the non-edges (mu=2 makes p,q the entire mu-graph of {x,y}).
      => non-edges pair into 2079 "mu-quads" (induced C4 with BOTH diagonals non-edges) and
      #non-edges must be EVEN. srg99: 4158 even -> CONSISTENT (no kill). Validated: involution +
      fpf hold exactly on rook9 (9 quads) and BvLS (13365 quads).
 [T3] every EDGE lies on exactly (k-2) mu-quads; srg99: 12. Cross-checks #mu-quads=693*12/4=2079.
      Validated {2} rook9, {20} BvLS.
 [T4] PLS line-layer: point vs external-line collinearity in {0,1} only; n1=3k-6=36 tangent /
      n0=60 per line; disjoint line pairs match in {0,1,3} NEVER 2 (validated-on-reals, NOT
      proven forced -> NOT claimed); prism-partnership is (k-2)=12-regular on the 231 lines.
 [T5] line-meet graph MEET=NN^T-3I is FORCED: 231 vtx, deg 18, spectrum {18^1,7^54,0^44,-3^132}
      (validated exact match on BvLS). lambda_min(MEET) = -3 (< -2) => Cameron-Goethals-Seidel-
      Shult generalized-line-graph (lambda>=-2) classification PROVABLY VOID here (clean negative).
      Hoffman bound on disjoint lines = v/3 = 33.
 [T6] lattice/theta angle SUBSUMED by p-rank: SRG lattice (A+7I=N^T N) det = 2^54*3^45*5^54*7;
      only special SRG prime is p|(r-s)=7 = the already-CLOSED vein. No new prime; theta adds 0.
 [Z3 cross] the mu-quad involution is canonical => order-3 fpf sigma permutes the 2079 mu-quads;
      cycle-type on a 4-set forces a vertex fixed-point, impossible for f=0 => sigma fixes NO
      edge/non-edge/mu-quad; 693,4158,2079 all ≡0 mod3 => orbit counting CONSISTENT with f=0.
      The new structure does NOT obstruct the open Z3/f=0 cell.

CALIBRATED VERDICT: a NEW forced global structural theorem (the mu-quad fpf involution + the
forced line-meet spectrum + edge-(k-2)-mu-quad regularity), all exact and validated on both reals,
but NO KILL -- every value is integral/even/consistent at v=99, and the one classification theorem
that could bite (CGSS) is void because lambda_min(line-meet) = -3 not -2. The locally-7K2 / PLS /
s=-4-lattice global angle is consistent-no-obstruction. Files (.work/99graph/): muquad_theorem.py
(consolidated); scratch probes in scratchpad/99g/ (census_calib, pls, secant, linepair, prism,
closedform, prismgraph, lineincidence, meetspec, lineabsbound, root3, linedesign, global_dc,
muquad, muquad_z3, lattice_collapse).

---

## R22 (FULL PER-ROW McKAY CANONICAL AUGMENTATION, a=24 cell, 2026-06-28) — engine PROVEN one-rep-per-orbit at every depth; leadsym/principal NON-COMPOSABLE (proven); a=24 WALLS (sound) at row 2/3

Scripts (.work/99graph/): mckay_canon.py (McKaySearch), mckay_canon_validate.py,
mckay_a24_drive.json. Full write-up: MCKAY_CANON_FINDINGS.md.

**BUILT (the requested ingredient).** A canonical-augmentation test that accepts a partial
orbit matrix (rows 0..i placed) iff its PRINCIPAL (i+1)x(i+1) submatrix (placed rows AND
placed cols) is the lex-min of its orbit under G=Aut_empty(<=72) x S_T, over perms mapping
{0..i} to itself. PRINCIPAL block (not rows x all-cols) is the correct sound intermediate
test: unplaced rows' columns are undetermined, so comparing them is unsound (the rows x
all-cols form REJECTED real partials -> caught by orbit-bijection on E4T2/E3T3, fixed).

**SOUNDNESS PROVEN at depth>=3 (brute-force orbit ground truth, not self-report):**
(A) one-rep-per-orbit at FULL depth 64/64 incl all-triangle |G|=720; (B) prefix-monotone
(global canonical passes every intermediate row) 70/70 => no orbit lost; (C) SEARCH-INTEGRATED
orbit bijection on relaxed-constraint cases with real multiplicity (E0T6 deg2 = 70 graphs ->
2 orbits C6/C3+C3 -> exactly 2 survivors) 12/12; (D) rook9 re-found, BvLS 81x81 constraint-
survives + canon idempotent leading depths 1..5; (E) a=24 canon_rejects=0 (NOT over-pruning).

**RIGOROUS NEGATIVE RESULT (new, ground-truthed).** leadsym (the leading-row column-orbit
collapse that broke row 2 in R-incut) and the principal McKay canon DO NOT COMPOSE: the
disjoint-range combination LOSES orbits — not only all-triangle (E0T6 2->0) but E>0 a=24-like
structures (E4T3 4->1, E6T3 18->0). Cause: leadsym fixes a "1's-first" column rep, principal
canon is lex-MIN "0's-first"; the two canonical conventions annihilate each other's survivors
(CANON_FINDINGS trap-b, now proven to extend to the principal form for ANY shared rows). =>
cannot combine for a closure-grade claim; each filter must stand alone.

**GO/NO-GO a=24 (HONEST; timeout != infeasible).** Proven-sound principal McKay (leadsym_rows=0),
12M nodes/piece: ct=(6,) max_row=2, row_reach[2]=1,646,895, canon_rejects=0, TIMEOUT;
ct=(3,3) max_row=3, row_reach[3]=449,422, canon_rejects=0, TIMEOUT. 0 cells CLOSED, 0 SAT
models. Head-to-head EQUAL 2e6 budget: prior incut leadsym L=2 collapses row 2 to 9 and
reaches row 4(ct6)/8(3,3); THIS sound McKay walls at row 2 (1.7M)/row 3. NET: the full
per-row canon is one-rep-per-orbit at EVERY depth (the property leadsym L=2 lacked) but is
WEAKER at the under-constrained LEADING rows (its principal corner can't see column symmetry
into the 27 still-unplaced triangle rows), and provably can't borrow leadsym's leading-row
collapse. a=24 remains OPEN exactly as in the literature (Behbahani Table 21 = "?").

**NEXT ACTION (resume).** A closure-grade engine needs a SINGLE canonical form that is BOTH
leading-row-strong AND full-depth-sound (true nauty partition-refinement with target-cell
selection over Aut_empty x S_27 — beyond pure-Python at t=33 in budget; consider a C/nauty
binding or SAT-with-full-symmetry). Do NOT re-attempt the leadsym+principal composition
(proven unsound). The proven-sound principal-McKay engine is reusable for any future orbit-
matrix exhaustion (validated machinery).

================================================================================
R22 (2026-06-28) — BLISS canonical-AUGMENTATION engine (the diagnosed C-level fix)
================================================================================
TASK #38: nauty/BLISS-backed canonical augmentation closure of a=24. The ir_canon/MCKAY
findings diagnosed that closing a=24 needs ONE canonical form that is BOTH leading-row-strong
AND full-depth-sound; pure-Python I-R could not reach t=33. Built it with C-level BLISS.

FILES: bliss_canon.py (engine), bliss_canon_validate.py (V0-V6, all PASS),
       bliss_a24_drive.py (single-proc GO/NO-GO), bliss_a24_unbounded.py (32-core standalone).

ENGINE (the delivered ingredient):
 - Encode partial orbit matrix as a vertex-COLOURED gadget graph; FOLD colours into rigid
   pendant-path tags so plain (uncoloured) BLISS is a true canonical form. (KEY negative finding:
   igraph 1.0.0 canonical_permutation(color=) is NOT a reproducible coloured canon here — colour-
   folding fixes it; 0/400 invariance, orbit-EXACT cert.)
 - BLISS automorphism_group() of the (diag,A2) base graph generates EXACTLY G=Aut_empty x S_T
   (closure==brute structure_group), incl. the S_T transposition generators (leadsym strength).
 - Pruning = SOUND incremental lex-leader over generators (no orbit lost: the orbit leader is
   fixed by every generator) + EXACT BLISS-cert dedup of completed models (one rep per orbit).
 - 32-core: collect canonical row-P seeds, farm subtrees; seed+resume aggregation EXACTLY
   reproduces single-proc count (validated 497==497).

SOUNDNESS — validated (exact brute ground truth), ALL PASS:
   V0 cert G-invariant 0/400 ; V1 orbit-exact 0 fail ; V2/V3 lex-leader+cert == brute orbit
   bijection (no orbit lost, exact) on E0T6/E3T3/E4T2/E3T4 ; V4 rook(9) recovered ;
   V5 BvLS(243) 81x81 valid+idempotent+no-false-kill ; V6 *** DECISIVE *** the REAL BvLS 81x81
   quotient's lex-leader labelling is ACCEPTED at EVERY cell+row by the engine's actual pruning
   chain (first_bad=None) — a real srg in the family is NOT killed.
   (Caught+fixed an UNSOUND row-i-only incremental prune that returned count=0 for BvLS; the
    full rows-0..i prefix comparison is the sound form.)

NEW FRONTIER (a=24, max_row reached; TIMEOUT != INFEASIBLE):
   leadsym 4/8 ; principal-McKay 2/3 ; ir_canon 2/3 ;  THIS BLISS engine: 9 (ct6) / 11 (ct3,3).
   Leading-row collapse: no-canon row-1 >438,167 completions -> BLISS canon ~5 (row1), ~17 (row2),
   ~41 (row3). Single form = both leading-strong AND full-depth-sound (the asked-for property).

NEXT ACTION: run bliss_a24_unbounded.py with deep seeding (prefix>=5) + 32 cores to drive each
   a=24 cycle-type subtree to a COMPLETED tree; a few deep subtrees are the remaining wall (one
   ct6 subtree ran 657K nodes). Then sweep all 4 parity classes. INFEASIBLE only on a COMPLETED
   0-orbit run (the engine is validated sound for that claim).

================================================================================
R23 (2026-06-28) — DEEP-TAIL-PROOF recursive-subdivision driver (this session)
================================================================================
TASK: drive a=24 ct=(6,) to CERTIFIED COMPLETION; prior flat prefix-4 uncapped run STALLED at
~219/497 (a few subtrees >1.14M nodes blocked the 32-core pool).

DONE:
 1. KILLED stalled run: parent PID 72752 + 32 spawned workers (taskkill /T /F). Machine clean
    (0 bliss procs). Unrelated procs (copy-trader API 68644/58988, trader.py, tensor-rank,
    book_logger) left untouched.
 2. BUILT bliss_a24_recursive.py: per-worker NODE CAP + RECURSIVE SUBDIVISION. A capped subtree
    is re-seeded one row deeper (collect_prefixes in seed-resume mode) and its children re-queued;
    a capped seed NEVER contributes a count, only its children -> every contributing leaf completes
    uncapped => true certificate. Resumable JSONL ledger (bliss_rec_<tag>.jsonl) + live status
    (bliss_rec_<tag>.status.json). Threads engine params for reuse.
 3. VALIDATED:
    - engine bliss_canon_validate V0-V6 ALL PASS (cert G-invariant+orbit-exact, orbit bijection,
      rook(9) recovered, BvLS(243) 81x81 not falsely killed, BvLS lex-leader accepted everywhere).
    - probe_subdiv2: re-seeding all prefix-2 seeds to row3 == direct prefix-3 EXACTLY (122==122),
      identical cert-set (76==76). Subdivision = sound, exact (no orbit lost, no double count).
    - bliss_recursive_validate D1 rook(9) recovered THROUGH the recursive driver under a tiny cap
      (subdivision forced): [[2,1,1],[1,2,1],[1,1,2]] == no-cap ref. D3 partition exact on the REAL
      a=24 cell for BOTH ct=(6,) (122==122) and ct=(3,3) (4==4), cert-sets identical.

NEXT ACTION: launch bliss_a24_recursive.py --class 24 --ct 6 --prefix 5 --cap 300000 --procs 30
  as a detached background process; monitor via the status json. Then ct=(3,3). INFEASIBLE only on
  a COMPLETED 0-orbit run (every leaf uncapped). a=18 (E=27) is much larger; defer.

--- R23 LAUNCH + VALIDATION CONFIRMED (2026-06-28 ~20:30) ---
DRIVER VALIDATION ALL PASS (bliss_recursive_validate.py): D1 rook(9) recovered through recursive
driver under tiny cap; D2 count+certset EXACT under subdivision on real a=24 cell; D2b multi-level
subdivision at scale (live ledger: subdiv at start_rows {4,5,6,7}); D3 partition exact ct6 122==122
and ct33 4==4. Engine V0-V6 ALL PASS (re-confirmed this session).

LAUNCHED (detached, survive shell exit):
  ct=(6,)  PID 43348  prefix=4 cap=300000 procs=30  -> bliss_rec_a24_ct6.log / .status.json / .jsonl
  ct=(3,3) PID 60016  prefix=4 cap=300000 procs=8   -> bliss_rec_a24_ct3_3.*

DEEP-TAIL FIX CONFIRMED WORKING: ct6 at t=230s leaves=214 (ALREADY PAST old stall ~219), subdiv=60,
max_subdiv depth=7 (4->5->6->7), nodes=20.6M, orbits=0, SAT=False. No worker blocked. The giant
subtrees that froze the old flat run are now being subdivided into completable pieces.

MONITOR COMMAND (run from .work/99graph):
  python -c "import json;[print(t, json.load(open(f'bliss_rec_{t}.status.json'))) for t in ['a24_ct6','a24_ct3_3']]"
  (or check bliss_result_rec_<tag>.json for the final verdict once a run finishes)

VERDICT: PENDING (run in progress). INFEASIBLE only on COMPLETED 0-orbit run (every leaf uncapped).
NEXT ACTION: watch bliss_result_rec_a24_ct6.json / ct3_3 for verdict; if SAT, lift to 99 vertices.

--- R23 CAP RETUNE + RESUME-BUG FIX (2026-06-28 ~20:45) ---
GROUND-TRUTH on cap=300k run: completed leaves are SMALL (median 4.2k, max 140k nodes) but a few
subtrees are EXTREMELY deep -> at cap=300k they subdivide at EVERY row (4..7), queue exploded
810->1142->1901->3105, leaves barely advanced (214->230). Diagnosis: cap too low => heavy
re-traversal of the first 300k nodes of each monster at every subdivision level. ct6 DID pass the
old stall point (leaves 230 > old 219) confirming the fix removes blocking, but throughput poor.

RETUNE: cap 300k -> 3,000,000 (prior-session monsters ~1.14M; at 3M most subtrees complete in one
pass, only true monsters subdivide, in 1-2 levels). Proc split ct6=26 / ct3_3=4 (=30, headroom).

RESUME BUG (found + fixed): cert is a tuple of edge-pairs; JSON round-trip turns inner pairs into
lists -> tuple(rec['seed_cert']) was unhashable -> resume crashed immediately. Added _cert_key()
(normalises list-of-lists -> tuple-of-2-tuples) at every cert add/reload/skip site. Smoke-tested:
live cert key == JSON-roundtripped key, hashable. Ledgers pruned to LEAF-ONLY before resume
(dropped cap=300k subdiv records so their parents reprocess fresh under cap=3M; 230 ct6 + 1 ct3_3
completed leaves preserved). Backups: bliss_rec_<tag>.jsonl.cap300k.bak.

RELAUNCHED (fixed, cap=3M): ct6 PID 47408 (26p), ct3_3 PID 66392 (4p).
MONITOR: python monitor_a24.py   (from .work/99graph)

--- R23 CALIBRATED STATUS (2026-06-28 ~20:55) ---
RESUME FIX VERIFIED: both runs resumed cleanly (ct6 reloaded 230 leaves, ct3_3 1 leaf), 0 crashes,
empty err logs. cap=3M keeps the queue HEALTHY: ct6 queue ~445 (vs cap=300k explosion to 3105),
subdiv few, throughput far better (less re-traversal).

LIVE TRAJECTORY ct6 (cap=3M, 26 proc): t=111->240s leaves 231->236 (~1 leaf/30s in the deep-tail
region), queue 450->445, nodes 3M->7M, subdiv=0 (workers grinding several 3M+ monsters toward the
cap; will subdivide on hit), orbit_certs=0, SAT=False, max_row=9. ct3_3 (4 proc): 1 leaf done, 1
remaining monster seed grinding toward 3M cap (no status yet, expected).

CALIBRATED TIME ESTIMATE: a=24 ct=(6,) has ~267 uncertified row-4 seeds remaining; the deep tail is
SUBSTANTIAL (many subtrees 1M-10M+ nodes; total tree plausibly billions of nodes). At ~26 effective
cores x ~100k nodes/s this is a MULTI-HOUR to MULTI-DAY full certification, NOT finishing in one
session. The fix GUARANTEES it will get there (no blocking; monsters subdivide), and it is fully
RESUMABLE (kill/restart safe via the leaf-only ledger). 0 orbit matrices + 0 SAT models so far in
BOTH cells -- consistent with (but NOT yet proof of) the expected INFEASIBLE outcome.

VERDICT: PENDING (neither cell COMPLETED yet). A 'closed/INFEASIBLE' verdict will be emitted ONLY
when bliss_result_rec_a24_ct6.json appears with orbits=0 (every leaf uncapped). Do NOT call it
closed before then.

MONITOR (from .work/99graph):  python monitor_a24.py
RESUME after any kill/restart:  powershell -File launch_a24_recursive.ps1 -Ct "6" -Cap 3000000 -Procs 26
  (auto-resumes from bliss_rec_a24_ct6.jsonl; same for -Ct "3,3" -Procs 4)
a=18 (E=27, the other surviving class): DEFERRED -- far larger cycle-type space than a=24 (E=6).

---

## R30 — STAR COMPLEMENTS for s=-4 (the 55-vertex reconstruction). NEW LENS, verified.

**Framework (CRS / Rowlinson), exact signs ground-truthed on rook9+Petersen+BvLS.**
Star set X = 44 vertices (=mult of s=-4); star complement H = G-X on |H|=99-44=55,
with -4 NOT an eigenvalue of A(H)=C. Verified reconstruction (sc_sign.py, exact match
on rook9 & Petersen; sc_bvls_fix.py float-exact on srg(243,22,1,2)):
  P := (C - sI)^{-1} = (C+4I)^{-1}.  For star vtx u with H-neighbor column b_u in {0,1}^55:
   (D) b_u^T P b_u = -s = 4              [diag compat]
   (O) b_u^T P b_v = a_uv in {0,1}       [off-diag]
   A_X = sI + B^T P B = -4I + B^T(C+4I)^{-1}B   [must be 0/1 symmetric zero-diag]
Independent confirmation: Schur complement A_X - sI - B^T(C-sI)^{-1}B == exact 0
(sc_detformula.py) on rook9 & Petersen.

**NEW verified forced facts for ANY star complement H of srg99 (s=-4):**
1. **mult_3(H) >= 10** (Cauchy interlacing). General thm, verified across family
   (sc_interlace_check.py / corrected mults): mult_r(H) >= m_r - m_s ⇒ rook9:0, srg99:10,
   BvLS:22. Exact sandwich: theta_2..theta_11 of H == 3 exactly; theta_1 in [3,14];
   theta_12..55 in (-4,3]; lambda_min(H) > -4 strict.
2. **det(C+4I) = prod(theta+4) is a positive integer divisible by 7^10** (since (3+4)=7
   occurs >=10 times). The diagonal eq is the integer form b^T adj(C+4I) b = 4·det(C+4I).
3. **Edge window 77 <= e(H) <= 385**, with e(X)=e(H)-77, e(X,H)=770-2e(H) (sc_srg99_constraints.py,
   symbolic total = 693 verified).
4. **B has FIXED row sums**: for each H-vtx h, #star-neighbors = 14 - deg_H(h); column
   weights |b_u| = 14 - d_X(u) in [0,14]. ⇒ B is a 0/1 matrix with H-fixed row sums +
   per-column quadratic ⇒ tightly constrained CSP, NOT free enumeration.
5. H induced in srg99: max deg <=14, every edge in <=1 triangle, locally partial 7K2,
   any 2 nonadj share <=2 common nbrs.

**Foundation calibration (sc_foundation.py, sc_detdiv.py — EXACT, complete enumeration):**
- rook9: EVERY star complement has |B(H)|=4 exactly, det(C+2I)=6; exactly ONE
  pairwise-compatible 4-clique, which reconstructs the real rook9. End-to-end recovery ✓.
- Petersen: |B(H)| in {9,10,11,27}; det in {3,12,27}. Small, structured.

**VERDICT: no immediate contradiction; the s=-4 star complement defines a TRACTABLE
(if heavy) bounded search.** The parameters remain too well-behaved for a one-line kill
(consistent with all prior routes). Most promising sub-route to push: the tension between
the FORCED integral eigenvalue 3 of multiplicity >=10 in a 55-vtx graph that is induced in
a locally-7K2 sparse SRG (deg<=14, sparse triangles) — a 10-dim integer eigenspace is a
strong but not-yet-contradictory constraint. CLOUD SPEC for the search recorded in the
lens report (candidate-H growth from forced 7K2 seed + column CSP + SRG closure).

Scripts (all in .work/99graph/, exact arithmetic unless noted): sc_validate.py,
sc_sign.py, sc_srg99_constraints.py, sc_interlace_check.py, sc_foundation.py,
sc_detdiv.py, sc_detformula.py, sc_bvls_fix.py (float scale check), sc_verdict.py.

--- R30 ADVERSARIAL RE-VERIFICATION (independent, fresh context) ---
INDEPENDENT re-derivation from scratch (scratchpad/indep_sc.py, indep_interlace.py,
indep_bvls.py, indep_foundation.py — NOT reusing sc_*.py). ALL load-bearing claims CONFIRMED:
- CRS sign: A_X = sI + B^T(C-sI)^-1 B matches 81/81 rook9 star complements (exact Fraction);
  diag b^T(C-sI)^-1 b = -s, off-diag in {0,1}, all 81. (Note: their sc_validate.py prints the
  WRONG-sign form match=False — stale first guess; every downstream CONSTRAINT script uses the
  corrected sign. Honest correction, not load-bearing error.)
- BvLS(243): rebuilt, spectrum {22, 4^132, -5^110} (corrected mults right); CRS reconstruction at
  s=-5, |X|=110, float-exact err 2.5e-14, all diag=5. Interlacing forced 4's = 22 = m_r-m_s.
- Interlacing -> mult_3(H)>=10 for srg99: re-derived; 0 violations brute on rook9; FORCED.
- det(C+4I): 7^10 | det FORCED (integer det, >=10 factors of 7). Edge window 77<=e(H)<=385 re-derived
  (endpoints sum 693). Foundation rook9: |B(H)|=4, exactly 1 reconstructing clique (reproduced).
VERDICT: math CONFIRMED. But CALIBRATION on novelty: the forced SPECTRAL facts (mult_3>=10,
lambda_min(H)>-4) ARE the Cauchy window = the already-CLOSED "spectral/interlacing" route ("PSD
window = Cauchy window; no force") — NOT a new obstruction. Report correctly does NOT claim them as
a kill (says "consistent-no-obstruction"). GENUINELY NEW = the star-complement reconstruction CSP
(44 compat 0/1 cols closing to srg99) as a decision framework, distinct from prior routes. Cloud
spec is correctly formulated (would decide) BUT its dominant cost (abstract 55-vtx induced-subgraph
generation) is, by the report's own admission, comparable-to/harder-than the paused Z3/f=0 cell —
so it is NOT clearly a more tractable route. Outcome stands: consistent, no contradiction, no
overclaim. Confidence HIGH.

## R30 — H3 / n3>=3 STRUCTURAL PROPAGATION (asymmetric-case lens): rigid triangle environment
## fully mapped; H3 counting is a CLEAN NEGATIVE; Makhnev n3>=1 analog forces NO infeasibility.
Files (.work/99graph/h3_*.py; all 24 gates PASS on rook9+BvLS243; soundness gate PASS):
- FORCED & VERIFIED triangle environment (every triangle T, srg99): V = T(3) + S(36) + F(60).
  vertex-triangle lemma: each outside vtx adj <=1 of T (=lambda1). S = Sa|Sb|Sc, each 12.
  S-vtx structure (PROVEN): 1 nbr in T, 1 same-block apex, EXACTLY 1 in EACH other block
  (mu=2 with the missing T-vtx forces it), 10 in F. F-vtx: EXACTLY (2,2,2) into (Sa,Sb,Sc)
  + 8 in F. e(S)=36 internal-block matchings(18)+cross-block(36); e(S,F)=360; e(F)=240.
- H3 LOCALIZED: #cross-edges(T1,T2)=|T2 cap S1|; an H3 <=> an (S,S,F) disjoint triangle
  (2 S-vtxs diff blocks + 1 F-vtx). Each cross-block S1 edge (36 of them) has a unique apex
  (lambda1) in S1 (=> PRISM with T1) XOR in F1 (=> H3 with T1). reals: all 36 apexes in S1
  (n3=0). eta(T)=#H3 at T=#(S,S,F) tri; pi(T)=#prism-type; eta+pi=36.
- GLOBAL couplings (VERIFIED exact on reals): sum_T eta = 2 n3 ; sum_T pi = 6 nprism ;
  sum_T n1type = 2 n1 ; per-T: eta+n1type = e(S1,F1)/2 = 3(k-2)(k-4)/2 = 180.
  => 2n3+6nprism=8316 (== X2 master reln) ; 2n3+2n1=41580 (== X1-X2). The H3-environment
  relations span EXACTLY {DTP,X1,X2}: n1 = X1-X2-n3. NO independent equation. Residual DOF=1.
  n3 STAYS FREE in {0,3,...,4158}. Per-vtx H3-incidence in {0,1,2} => eta(T)<=36 (= eta+pi
  bound; no sharper). CLEAN NEGATIVE: H3 counting cannot pin/exclude n3.
- SELF-FALSIFIED (verify-to-accept): a transient "n3>=1386 from n0>=0" used a WRONG
  DTP=21714; correct DTP=C(231,2)-99*C(7,2)=24486 (= prior block-graph-forced) gives
  n0=n3/3+2310>=0 ALWAYS => NO lower bound. Recorded in h3_n3_lowerbound.py.
- MAKHNEV n3>=1 ANALOG TEST (the task's explicit ask): per-F-vtx triangle census
  (ff,fs,ss) with ff=ss+(k-12)/2, fs=6-2ss, ss+fs+ff=k/2 (VERIFIED on BvLS, ss=0 -> (5,6,0)).
  srg99: (ff,fs,ss)=(ss+1,6-2ss,ss), ss in {0,1,2,3}; eta(T1)=sum_{w in F1} ss(w). The
  Makhnev srg(33,12,1,6) infeasibility is the ss=0-EVERYWHERE (n3=0) case (ff=1 'one far
  triangle per outside vtx' assembles the rigid SRG); n3>=1 <=> some ss(w)>=1 which is
  INTEGER-FEASIBLE per-vertex => the rigid SRG does NOT form => n3>=1 is the ESCAPE from
  Makhnev, NOT a re-trigger. NO analogous infeasible substructure is forced by n3>=1.
  (Scope: this removes the per-vertex integrality obstruction; a hypothetical GLOBAL
  far-structure obstruction at ss>0 is not excluded -- but no count forces one.)
- VERDICT: the H3 lens, pushed through the fully-rigid+verified triangle environment, is a
  CLEAN NEGATIVE for both counting (=span{DTP,X1,X2}) and the Makhnev analog (n3>=1 escapes).
  An asymmetric-case kill must come from GEOMETRY (rank-44/lift) or a genuinely non-count
  global argument, NOT from H3/n3 combinatorics. n3>=3 (R24) stands; no new constraint, no
  contradiction. NEXT ACTION: pursue the geometry lens (lift theorem at ss>0 far-vertices)
  or cloud-spec the rank-44 exhaustion; do NOT seek further linear H3 counts (proven void).

## R31 — STAR-COMPLEMENT CRS COLUMN SYSTEM tightened + CALIBRATED on a REAL eigenvalue-(-4) graph.
## Lens: tighten CRS column-compatibility + triangle-split; calibrate. (verify-to-accept; light compute only)

**CALIBRATION GRAPH FOUND & USED (the family graphs have no eigenvalue -4; needed an external one):**
  **srg(21,10,3,6) = Kneser K(7,2) = complement of triangular T(7)**, spectrum **10^1, 1^14, (-4)^6**.
  Same special eigenvalue **s=-4** as srg99 (here mult m_s=6, r=1 mult m_r=14). Built exactly (networkx),
  complete exact enumeration of star complements feasible (21 choose 15 = 54264). EVERY load-bearing
  star-complement claim was reproduced on it (scripts calib_*.py, all exact Fraction / eigh).

**(a) CRS COLUMN SYSTEM — what is binding, and the NEW pruning filter.**
- The diagonal equation alone (b^T P b = -s, P=(C+4I)^-1) is WEAK: a single Kneser star complement has
  **387 valid 0/1 columns** (lattice points on the ellipsoid); count ranges 364..942 across H. NOT the
  bottleneck. (calib_columns.py, rank_identity.py)
- **Pairwise compatibility (b_u^T P b_v in {0,1}) is the real bottleneck**, AND it is razor-tight:
  across 25 sampled Kneser star complements the compatibility graph has **max clique = m_s EXACTLY**
  (=6, never more, never fewer) and **exactly ONE** m_s-clique — which reconstructs the real graph.
  (Exact analog of the rook9 calibration: |B(H)|=4, one 4-clique.) (clique_sweep.py)
- **NEW — INHERITED-EIGENSPACE ORTHOGONALITY (the strong pruning filter, PROVEN + calibrated).**
  The forced (m_r - m_s)-dim r-eigenspace W0 of H (the dimensions Cauchy-interlacing guarantees at r)
  consists EXACTLY of vectors w that extend by zeros to r-eigenvectors of G; equivalently **B^T w = 0**.
  So **every star column b is orthogonal to W0** (dim m_r - m_s = 10 for srg99, 8 for Kneser).
  On Kneser this is a hard ADDITIONAL filter the diagonal eq does NOT imply: of 387 diagonal-valid
  columns only **6 are perp to W0 — and those 6 are EXACTLY the true star set** (64.5x pruning, one shot).
  Each (w;0) verified an EXACT r-eigenvector of full G. (orthog_theorem.py, w0_structure.py, w0_collapse.py)
- **DIMENSION SQUEEZE (structural, margin=1).** The m_s columns are linearly independent (Gram
  A_X+4I is PD, rank m_s) and ALL lie in W0^perp of dim (n-m_s)-(m_r-m_s) = n-m_r. Margin =
  (n-m_r) - m_s = **n - m_r - m_s = 1** (since n = 1+m_r+m_s for a 3-eigenvalue SRG). srg99: 44 indep
  cols in a 45-dim space (margin 1). Kneser: 6 in 7 (margin 1, identical). This is WHY reconstruction is
  unique (Rowlinson) and the CSP slack is 1-dim. **It is structural TIGHTNESS, NOT an obstruction**
  (existing graphs have it too). (dimension_squeeze.py, margin_identity.py)
- **Star-set dual constraints (necessary on A_X, the 44-vtx star-set induced subgraph):** lambda_min(A_X)
  > -4 strict (A_X also has no -4 eigenvalue); A_X has at most ONE eigenvalue > r (Cauchy from top);
  trace 0; A_X + 4I = Gram of the columns. (count_bound.py)
- **CALIBRATION of the det divisibility:** det(C+4I) = 5^(m_r-m_s) * (positive) on Kneser
  (v_5 = 8 on every star complement; generic det = 5^8 * 2^3 = 3,125,000). Exact analog of 7^10 | det
  for srg99. (calib_det.py)
- VERDICT on (a): column COUNT is NOT over-constrained (always satisfiable on the real graph; large valid
  set). The W0-orthogonality + margin-1 squeeze make the SYSTEM extremely rigid, explaining the unique
  reconstruction, but do NOT by themselves contradict srg99 (Kneser satisfies all of them and exists).
  They are a strong SEARCH ACCELERATOR (the 64.5x filter), promoted into the cloud-spec.

**(b) TRIANGLE-SPLIT x EIGENVALUE constraints -> e(H) <= 363 (TIGHTENED, was 384).**
- Third-moment inequality (PROVEN, calibrated 0/3000 violations on Kneser):
  for any star complement with special eigenvalue r and >= p copies of r,
    **6 t(H) = sum theta^3 > theta_1^3 + 4 theta_1^2 + (r^3+4r^2) p - 8 e(H)**
  using x^3 > -4 x^2 (strict) for the other eigenvalues x in (-4, r), m1=0, m2=2e.
  srg99 (r=3, p>=10): 6t > theta_1^3 + 4 theta_1^2 + 63 p - 8e.
- Unconditional Perron bound theta_1 >= 2e/55 (Rayleigh on all-ones; verified 0/2000 random incl
  disconnected) and theta_1 <= 14 (interlacing top, 14-regular host). lambda_min > -4 GIVEN.
- Local lambda=1 bound: triangles in H are edge-disjoint => 3 t(H) <= e(H) => **t(H) <= floor(e/3)**.
- COLLISION: at e(H) >= 364 the spectral LOWER bound on t (>122.97 at the most permissive theta_1=2e/55,
  p=10) exceeds the local UPPER bound floor(e/3)=121 -> NO valid integer t -> **e(H) excluded for e>=364**.
  => **e(H) in [154, 363]** (triangle-split window narrows by 21 at the top).
  (third_lower.py, verify_cut.py, calib_moment.py, combine_local.py, adversarial_perron.py)
- HONESTY NOTE: my first pass (third_moment.py) reported a (spurious) "no overlap at e>=364" via an
  inverted bound; re-derived cleanly (ground-truth) — the CORRECT mechanism is spectral-t-LOWER vs
  split-t-UPPER, which independently lands on the SAME e>=364 cut. The clean bound is the one above.
  The simple second-moment coupled bound (Perron>=avgdeg + Cauchy-Schwarz m2) gives NO cut on [154,384]
  by itself (coupled.py) — reported as a clean negative; the m3 bound is the one with teeth.

**(c) Calibration outcome:** the ENTIRE star-complement framework (interlacing mult_r(H) >= m_r-m_s,
  lambda_min(H) > -4, CRS reconstruction A_X = sI + B^T(C-sI)^-1 B, det 5-divisibility, W0-orthogonality,
  margin-1 squeeze, m3 triangle inequality) reproduces EXACTLY on srg(21,10,3,6)=Kneser K(7,2), a real
  graph that genuinely HAS eigenvalue -4. 0 violations anywhere. Framework is SOUND.

**(d) REFINED CLOUD-SPEC** for the thin vertical slice -> see CLOUD_SPEC_SC.md (this dir). Key upgrades
  vs R30 draft: e(H) in [154,363]; W0-orthogonality pre-filter (cut columns to ker(W0^T) BEFORE the
  diagonal/compat CSP, ~60x on the calibration graph); margin-1 termination; failure-CATEGORY logging.

**OUTCOME: consistent-no-obstruction + two genuinely tightened constraints** (e(H)<=363; W0-orthogonality
  column filter), both calibrated on a real eigenvalue-(-4) graph. No kill (Kneser satisfies everything &
  exists — correctly NOT excluded). The framework is firmed for the cloud slice. Confidence HIGH.

## R32 — CRS COLUMN OVER-DETERMINATION lens (sufficient-direction kill attempt). NECESSARY-ONLY.
## Calibrated on Kneser K(7,2)=srg(21,10,3,6), the real s=-4 graph. Exact arithmetic. Light compute.

**NEW THEOREM (verified, exact + adversarial on Kneser incl. excess-multiplicity cases):**
  For any star complement H of a 3-eigenvalue SRG with star set X (|X|=m_s):
   (i) the FULL r-eigenspace W0 of A_H (dim = mult_r(H)) satisfies B^T W0 = 0 — the WHOLE
       r-eigenspace of H extends-by-zeros to r-eigenvectors of G, NOT just the Cauchy-forced
       (m_r-m_s) part (confirmed on the 7 Kneser star complements with mult_r=9 > m_r-m_s=8:
       B^T(full 9-dim W0)=0 exactly, sympy nullspace).
   (ii) the m_s columns are linearly independent (Gram A_X+4I PD).
   => m_s indep columns in W0^perp (dim |H|-mult_r(H)) FORCES  mult_r(H) <= |H|-m_s = n - 2 m_s.
  With Cauchy mult_r(H) >= m_r - m_s:   **m_r - m_s <= mult_r(H) <= n - 2 m_s.**
  - **srg99: mult_3(H) in {10, 11}** (was R31 [10,30] -> TWO-VALUE window). At 11: columns are a
    forced BASIS of W0^perp (margin 0); at 10: margin 1.
  - Kneser: window [8,9]; observed max mult_r(H) = 9 EXACTLY (35910 at mult_r=8, 7 at 9). Hard
    ceiling confirmed exact: mult_r=10 would give W0^perp dim 5 < 6=m_s (impossible). PASSES.
  (scratchpad/rank_deficit_kill.py, excess_test.py, adversarial_window.py — exact sympy.)

**KILL TEST (calibration): NECESSARY-ONLY.** Kneser (a REAL s=-4 graph) has star complements at
  BOTH window ends, including the TIGHTEST margin-0 (mult_r=9, columns = basis of W0^perp), all
  reconstructing the real graph exactly (CRS err 0). The over-determination is SATISFIED by a real
  graph at the tightest packing => it CANNOT be an Aut-agnostic existence obstruction for srg99.
  - Route (a) count: after the sound W0 filter, N_perp = m_s EXACTLY on every Kneser H (filter lands
    on true star set; zero slack). No generic margin to push below 44. VOID as kill.
  - Route (b) clique: max compat clique = m_s exactly, unique, all sampled H; its existence ==
    graph existence, so any bound <m_s falsely excludes Kneser. VOID as kill.
  (scratchpad/overdet_lens.py, margin_witness.py.)

**GENUINE TIGHTENINGS (calibrated, not kills):**
  1. **mult_3(H) in {10,11}** (the new ceiling; R31 had [10,30]).
  2. **e(H) <= 363 RE-DERIVED by pure counting** (independent, simpler proof than R31 triangle-split):
     sum of column weights = e(X,H) = 14*55 - 2e(H) = 770 - 2e(H); every valid column has weight>=1
     (weight-0 => b^T P b=0 != 4); 44 columns => e(X,H)>=44 => e(H)<=363. Identity
     sum(colw)=k|H|-2e(H) verified on 200 Kneser star complements. (scratchpad/sparsity_deficit.py,
     weight_floor2.py.)
  3. **Soundness fix for CLOUD_SPEC_SC.md**: B^T(FULL r-eigenspace)=0 ALWAYS (incl. excess cases),
     so the W0 pre-filter never over-prunes even when mult_r(H) > m_r - m_s. (Latent risk removed.)

**Sparsity (the task's hope) tested:** at e(H)->363 avg column weight ->1.0 (columns must be very
  low weight) but weight-1 columns ARE admissible (H eigenvalue <=-3.75 with P_ii=4); system stays
  satisfiable. weight>=2 NOT forcible => no kill to e<=341. Sparsity reproduces e<=363, stops there.

**OUTCOME: consistent / no obstruction.** Lens is NECESSARY-ONLY (real s=-4 graphs satisfy every
  constraint at the tightest margin). Value = SEARCH ACCELERATOR (window {10,11}; sound filter) +
  a second proof of e(H)<=363, NOT an Aut-agnostic kill. Confidence HIGH (exact + adversarial on a
  real s=-4 graph; no falsely-excluded witness).

## R32 — WILDCARD LENS: TOPOLOGY of the clique/triangle 2-complex + binary (F2) p-rank + triangle
## block graph. Genuinely-new global angle, NOT on FINAL_REPORT section-2 closed list. (light compute,
## fully calibrated on rook9 + BvLS243; cloud-spec n/a — all checks were light/exact)
## Scripts: scratchpad/topo_fvector.py, topo_general.py, topo_bvls.py, topo_f2.py, topo_bve_falsify.py,
##          topo_window.py, topo_blockgraph.py, topo_block_feas.py, topo_final_panel.py

ANGLE: the lambda=1 SRG is a PARTIAL LINEAR SPACE — 99 points, 231 lines of size 3, 7 lines/point,
two points on <=1 line — equivalently the clique complex X(G) is a pure 2-complex whose 2-cells
(triangles) are EDGE-DISJOINT (lambda=1 => triangles partition the 693 edges; no K4 => dim 2).
Three sub-objects attacked: (1) integer homology of X(G); (2) binary (F2) p-rank invariants; (3) the
triangle BLOCK GRAPH. None was on the closed list (which had p=7 SNF + F2/F3 QUADRATIC FORMS, not these).

(1) HOMOLOGY OF THE CLIQUE COMPLEX — fully determined, NON-OBSTRUCTING.
  PROVEN (edge-disjointness): d2 (triangle->edge boundary) has pairwise-DISJOINT-support columns
  (each edge in exactly 1 triangle) => columns Z-independent & unimodular => rank d2 = t, ker d2 = 0,
  no torsion. So for EVERY srg(n,k,1,2):  H0=Z, H2=0, H1 = Z^{e-t-n+1} (free, no torsion).
  Equivalently X(G) collapses (Whitehead, each edge a free face) to a wedge of b1 = e-t-n+1 circles;
  pi_1 free of rank b1. chi = n-e+t = 1-b1.
  FORCED srg99: f-vector (99, 693, 231), chi = -363, H1 = Z^364, H2=0, torsion-free.
  CALIBRATION (exact, verify-to-accept): rook9 computed H1=Z^4 (=predicted), BvLS243 H1=Z^1540
  (=predicted), both via the disjoint-support lemma + connectivity. 0 mismatches.
  VERDICT: homotopy type is a function of (n,k) only => same for ALL family members => NECESSARY-ONLY,
  no kill. (Discrete-Morse/Forman obstruction VOID: the complex is collapsible-to-a-graph by construction.)

(2) BINARY (F2) p-RANK / 2-MODULAR STRUCTURE — one NEW exact fact, route is a clean WINDOW.
  NEW EXACT REUSABLE FACT (proven family-wide, verified rook9+BvLS): for srg(n,k,1,2) with k even
  (true for all 5 feasible: k in {4,14,22,112,994}), **A is IDEMPOTENT mod 2: A^2 ≡ A (mod 2)**.
  Proof: A^2 = kI+lam A+mu(J-I-A); mod2 mu(.)≡0, kI≡0 (k even), lam A=A (lam=1 odd) => A^2≡A. QED.
  => A mod2 is a PROJECTION; A and (A+I) are COMPLEMENTARY projections (A(A+I)=A+A^2≡0, A+(A+I)=I)
     => **rank2(A) + rank2(A+I) = n EXACTLY** (verified: rook9 4+5=9, BvLS 110+133=243; srg99 forces
     one even + one odd since n=99 odd). Also point-triangle incidence: NN^T=(k/2)I+A; k/2 odd for srg99
     => NN^T ≡ I+A (mod2); all-ones 1_99 in ker_F2(A) (k even) => rank2(A)<=98.
  FALSIFIED a tempting over-claim (verify-to-accept catch): "rank2(A) = mult of the unique odd-mod2
  eigenvalue (=m_r=54)" HOLDS on BvLS (110=m_s, its odd eig) but FAILS on rook9 (predicts 0, actual 4,
  because rook9 has ALL eigenvalues even mod2). So rank2(A) is NOT spectrum-forced; the naive 2-adic
  block-separation fails when k-s is even (k-s=18 for srg99 => k,s blocks 2-adically MIX). Honest
  forced WINDOW: rank2(A) in [10,98] (lower from v2(det A)=89 >= #even invariant factors; upper from
  1_99 in kernel). WIDE => non-obstructing, exactly like the p=7 window. rook9 (4 in [3,8]) & BvLS
  (110) sit in their analog windows. NO KILL.

(3) TRIANGLE BLOCK GRAPH B (line graph of the linear 3-hypergraph) — NEW derived object, NON-OBSTRUCTING.
  B: 231 vertices (triangles), adjacent iff share a vertex (= share exactly 1, by edge-disjointness),
  18-regular. EXACT IDENTITY (verified rook9+BvLS): M(B) = N^T N - 3I. Eigenvalues of N^T N = nonzero
  eigs of NN^T=7I+A {21,10^54,3^44} + 0^{132} (rank N=99) => **B has forced integer spectrum
  {18^1, 7^54, 0^44, (-3)^132}** (trace 0, trace M^2 = 4158 = 231*18, both check). A 4-eigenvalue
  regular graph. TESTED for distance-regularity (the only route to a feasibility kill): BvLS's block
  graph is NOT distance-regular (intersection numbers vary at distance 2) => no DRG feasibility theory
  applies, and srg99's B need not be DRG either => the 4-eigenvalue block-graph spectrum is a real
  realizable shape (BvLS witnesses it) => NECESSARY-ONLY, no kill. (rook9-B = octahedron K_{2,2,2},
  SRG, DRG only because tiny.)

(META / WHY VOID) FINAL PANEL (topo_final_panel.py): every cheap forced GLOBAL Z2/topological invariant
  of srg99 is MATCHED by a real lambda=1 SRG witness with the identical value:
    chi ≡ 1 (mod2) and b1 ≡ 0 (mod2) for ALL five family members; #C4 ≡ 1 (mod2) (rook9, srg99, BvLS);
    k/2 odd & t odd: srg99 == BvLS exactly. => srg99 is topologically/Z2-INDISTINGUISHABLE from BvLS243
  (a real graph) on every cheap global invariant. This is the structural REASON the topology route
  cannot kill: BvLS243 is a perfect shadow-witness for the entire (n,k,1,2)-derived topological/Z2
  invariant family — same as every spectral/lattice invariant already exhausted.

OUTCOME: VOID-HERE (sharp). The topological/clique-complex angle is genuinely new but provably
  non-obstructing — homology is an (n,k)-function, F2 p-rank is a wide window, the block-graph spectrum
  is BvLS-realizable. POSITIVE YIELD (new, verified, reusable): (a) closed-form integer homology of
  X(G) for the whole family (H2=0, torsion-free, H1=Z^{e-t-n+1}) via the edge-disjoint-support lemma;
  (b) A^2 ≡ A (mod 2) family-wide + rank2(A)+rank2(A+I)=n complementary-projection identity (NEW exact
  F2 facts, distinct from the closed p=7 SNF route); (c) the block-graph identity M=N^T N-3I and its
  forced spectrum {18,7^54,0^44,(-3)^132}. All calibrated 0-violation on rook9 + BvLS243. Confidence HIGH.
  A kill still must come from COMBINATORIAL REALIZABILITY (the star-complement column CSP / orbit-matrix
  search), consistent with R30-R31; no global invariant of this kind can succeed because the parameters
  are too well-behaved and BvLS shadows them.

## R33 — SYNTHESIZER VERDICT (independent re-verification of R32 both lenses). NO KILL; FRONTIER = SEARCH.
Independently re-derived + re-ran (scratchpad recheck2-7.py, final_arith.py) on real s=-4 graphs:
 - col-overdet: B^T W0=0 (0 viol/4012 Kneser SCs); window mult_3(H) in {10,11} (0 viol); MARGIN-0
   Kneser SC (mult_r=9=upper, rank(B)=6=m_s) reconstructs EXACTLY via A_X = sI + B(A_H+4I)^{-1}B^T
   (verified after fixing my own sign bug) => no-false-kill anchor reproduced. CAVEAT confirmed: on
   rook(4) s=+2, rank(B)=5<m_s genuinely occurs (claim-(ii) PD not unconditional) but honest bound
   mult_r<=|H|-rank(B) holds 0-viol; s=-4 rescued by interlacing (A_X induced => A_X+4I PSD). Lens
   NECESSARY-ONLY; not a kill.
 - wildcard: A^2==A mod2 (rook9,Kneser, param srg99); rank2(A)+rank2(A+I)=n (9,21); block M=N^TN-3I
   exact + spectrum shape matches; homology rook9 H2=0/torsion-free/H1=Z^4 via integer SNF (d2 invar
   factors all 1). srg99 forced H1=Z^364, chi=-363. VOID-HERE; necessary-only (BvLS shadow).
VERDICT: both lenses CONFIRMED, NO Aut-agnostic kill. Tightenings real: mult_3(H) in {10,11};
 e(H)<=363 (counting). PURE-MATH (no-search) ASYMMETRIC SURFACE = EXHAUSTED: every necessary condition
 (spectral/lattice/moment/topological/F2/star-complement-column) has a real s=-4 (or lambda=1) witness;
 the ONLY decisive route left is the cloud star-complement search (CLOUD_SPEC_SC.md + R32 gates A,B).
 RECOMMENDATION: run the cloud job; further local reasoning will re-confirm "consistent, needs search".

## R34 — MARGIN-0 (mult_3(H)=11) OVER-DETERMINATION PROBE. Calibrated on Kneser margin-0 SCs.
## OUTCOME: consistent-Kneser-witnessed (NO branch-kill); one minor re-tightening e(H)<=358 at m3=11.
## scripts: scratchpad/margin0_probe.py, margin0_density.py, margin0_mechanism.py, margin0_fullchain.py,
##          srg99_window.py  (light/exact; no heavy compute)

PROBE: does margin-0 rigidity (44 cols = forced basis of W0^perp) + col-weight floor (sum=770-2e,
each>=1) + forced local lambda=1/mu=2/maxdeg<=14 OVER-DETERMINE H into contradiction, killing the m3=11 branch?

CALIBRATION ANCHOR (decisive): Kneser K(7,2)=srg(21,10,3,6) has 7 REAL margin-0 star complements
(mult_r=9 = interlacing-floor+1; W0^perp dim 15-9=6=m_s; cols a forced basis). Ran the FULL proposed
kill-chain on them (margin0_fullchain.py):
 (1) RIGIDITY IS REAL BUT NON-CONTRADICTORY: rank(B)=6=m_s, B invertible on W0^perp, CRS reconstructs
     the real graph exactly (err 9e-16), A_X a valid 0/1 graph. A real srg realizes the rigid config.
 (2) **DIRECTION OF THE SQUEEZE IS BACKWARDS** (the task's central hope falsified): the 7 margin-0
     Kneser SCs all have e(H)=45 PINNED (unique), with ALL columns weight = k = 10 (MAXIMAL/dense),
     NOT weight-1. Across all SCs: margin-1 (mult_r=8) spans e(H) in [48,55]; margin-0 (mult_r=9) is
     PINNED to e(H)=45 = the DENSE end. Excess multiplicity correlates with HIGH edge density / HEAVY
     columns, the OPPOSITE of the conjectured "e(H)->max, columns->weight-1 sparse".
 (3) LOCAL STRUCTURE FINE: margin-0 Kneser H spectrum {6, 1^9, (-3)^5}, lambda_min=-3>-4, valid
     induced subgraph (max-deg/edge-triangle/mu all within srg params). Exists honestly.

MECHANISM (margin0_mechanism.py, exact): trace identities tr(C)=0, tr(C^2)=2e(H) + Cauchy-Schwarz on
the (n_H - m3) non-r eigenvalues give  2 e(H) >= r^2 m3 n_H/(n_H - m3), a LOWER bound on e(H) that
INCREASES with mult_r. So margin-0 (higher m3) raises the e(H) FLOOR (pushes DENSE), it does NOT push
toward the col-weight CEILING (363). On Kneser this Cauchy-Schwarz becomes tight (non-r spectrum
collapses to {6,(-3)^5}), explaining the exact pinning to 45. For srg99 the bound is weak: m3=11 =>
e(H)>=62, far below the independent combinatorial floor 154, so margin-0 does NOT pin srg99's e(H).

SRG99 WINDOW (srg99_window.py): intersect C1 e>=154, C2 e<=363(/319), C3 Cauchy-Schwarz e>=62,
rank-3 t-split feasibility, and the m3=11 spectral-t inequality. Result: **205 feasible e(H) values
survive (e in [154,358])**. The m3=11 inequality only clips the top 5 [359-363] (a minor re-tightening
e(H)<=358 at margin-0). Window robustly NON-EMPTY -> NO over-determination into contradiction.

CALIBRATION VERDICT: every step of the proposed kill is SATISFIED by Kneser's real margin-0 SC; the
weight-floor "squeeze" runs the wrong way (margin-0 => dense, not sparse). By the task's own bar (must
not exclude Kneser's margin-0 analog), the kill DOES NOT FIRE.

OUTCOME: **consistent-Kneser-witnessed (branch NOT killed).** Genuine yields: (i) margin-0 rigidity
is real but necessary-only (Kneser realizes it); (ii) NEW exact relation 2e(H)>=r^2 m3 n_H/(n_H-m3)
(mult_r raises the e(H) floor; tight at SRG-like H, explains Kneser pinning to 45); (iii) minor
re-tightening e(H)<=358 in the m3=11 branch (clips 5 values). Confirms R32/R33: the asymmetric
no-search surface is exhausted; margin-0 is the most rigid but a real graph sits exactly there.
The decisive route remains the cloud star-complement search (CLOUD_SPEC_SC.md). Confidence HIGH
(exact arithmetic + adversarial calibration on a real s=-4 graph; no falsely-excluded witness).

## R34-VERIFY — INDEPENDENT FRESH-CONTEXT ADVERSARIAL VERIFICATION of the R34 margin-0 probe.
## Re-derived from scratch (own scripts, no reuse of attacker code); decision anchored on a re-built
## real Kneser margin-0 SC. scripts: scratchpad/{verify_foundations,my_kneser_margin0,my_mechanism,
## scrutinize_direction,my_srg99_window,my_killchain_on_kneser,my_asymmetry_probe,my_final_checks}.py
VERDICT: R34 CONFIRMED — margin-0 (mult_3(H)=11) branch is CONSISTENT-KNESER-WITNESSED, NO KILL.
Independently reproduced, all EXACT (sympy Fraction / integer det / nullspace):
 - Foundations: srg99 spectrum 14^1,3^54,(-4)^44; n_H=55; window mult_3(H) in {10,11}; m=11 = margin-0
   (W0^perp dim 44 = m_s, forced basis). Re-derived, 0 discrepancy.
 - Rebuilt Kneser K(7,2) from scratch; found the 7 REAL margin-0 SCs (mult_1=9). On all 7, EXACT:
   reconstruction A_X = sI+B^T(C-sI)^{-1}B == true 0/1 (yes); rank(B)=6=m_s (forced basis);
   B^T(full 9-dim W0)=0; e(H)=45 PINNED; ALL columns weight = k = 10 (MAXIMAL). Rigidity real, consistent.
 - FULL kill-chain (col-weight floor, Cauchy-Schwarz, recon, Gram-{0,1} pairwise, margin-0 basis-rank,
   lambda_min>-4, local maxdeg/lambda/mu induced) applied to the 7 real Kneser margin-0 SCs:
   **0 rejections** => chain is SOUND (no false-kill). Any argument killing srg99 m=11 via these
   would also reject Kneser => no kill, by the task's own bar.
 - NEW relation 2e(H) >= r^2 m3 nH/(nH-m3): re-derived (trace ids + Cauchy-Schwarz), 0 violations on
   35917 Kneser SCs; increases with m3. CORRECTED FRAMING: the load-bearing fact is on COLUMN WEIGHT,
   not raw e(H). e(X,H)=k*nH-2e(H), so HEAVY columns <=> LOW e(H). Kneser margin-0 = e(H)=45 (LOW raw
   e), e(X,H)=60 MAXIMAL (heaviest cols); margin-1 spans e(H) up to 55, cols as light as weight 6.
   Attacker's word "dense H" is imprecise (margin-0 is the LOW-e end), but the operative claim — margin-0
   forces MAXIMAL column weight, the corner where the weight-floor has MAX slack — is CORRECT. Probe's
   "sparse weight-1 squeeze" hope is genuinely falsified.
 - srg99 margin-0 window re-intersected independently: C1 e>=154, C2 e<=363, C3 CS e>=62, rank-3 split,
   C5 m3=11 spectral-t. Result IDENTICAL to R34: 205 feasible e(H) in [154,358]; C5 clips only [359-363]
   (re-tightening e<=358 CONFIRMED). Even with the stricter cap 319: 166 values. ROBUSTLY NON-EMPTY.
 - EXTRA (not in R34): det(A_H+4I) 5-adic valuation JUMPS at margin-0 on Kneser: v_5=8 at margin-1,
   v_5=10 at margin-0 (verified by factorint). Internally consistent (higher mult_r raises valuation);
   srg99 analog v_7 raises at m=11 too. Minor correction to the generic "v=m_r-m_s" note; NO contradiction.
 - EXTRA: brute count on Kneser margin-0 — exactly 6 0/1 vectors satisfy b^T P b=4, ALL 6 in W0^perp =
   the true star set. Reconstruction is MAXIMALLY RIGID (columns uniquely forced, zero slack) yet
   reconstructs a real graph. Rigidity != contradiction, demonstrated at the tightest packing.
EXHAUSTION: re-confirmed. Every necessary spectral/lattice/p-rank/moment/topological/column constraint
 has a real s=-4 (Kneser) or lambda=1 (BvLS243) witness at the tightest margin. PURE-MATH NO-SEARCH
 ASYMMETRIC SURFACE = EXHAUSTED. Decision rests on the cloud star-complement column search.
 Confidence HIGH (independent exact arithmetic; calibrated on a real eigenvalue-(-4) graph; 0 false-kills).

## R35 — CLOUD_SPEC_SC.md HARDENED: ordered Stage-A filter pipeline + generation order + cost model.
## Vein: consolidate (NOT run); turn all verified predicates into ONE ordered prune pipeline; cost model.
## scripts: scratchpad/{prune_estimate,spectral_rarity,interlace_online}.py (light sampling, seconds);
##          re-verified FINAL_GATE.py = ALL GATES GREEN. CLOUD_SPEC_SC.md rewritten (sections 1-6).
ORDERED STAGE-A PIPELINE (cheapest/highest-prune first; each verified-sound on a real witness):
  F1 maxdeg<=14 | F2 local partial-7K2 (N(v) max-deg<=1) | F3 lambda=1 edge-disjoint-tri | F4 mu<=2 |
  F5 degree band (deg<=13 from col-weight>=1) | F6 e(H) in [154,358] (363 soft, 319 aggressive) |
  F7 [NEW R35] ONLINE Cauchy-interlacing schedule: mult_3(partial_k) >= k-45 at depth k>=46 (online
     reject for the WIDEST last-10 tree levels — converts the terminal-only spectral gate into a mid-tree
     prune) | F8 spectrum gate (no -4; lambda_min>-4; mult_3 in {10,11}; eigs in (-4,14]) |
  F9 7^10|det(A_H+4I) | F10 corank_F2(A_H+I)>=m3, corank_F7(A_H+4I)>=m3 | F11 m3 third-moment |
  F12 triangle-split polytope + 2e>=r^2 m3 nH/(nH-m3).
  F1-F6 ONLINE local (baked into augmentation); F7 online spectral at k>=46; F8-F12 terminal.
GENERATION: canonical augmentation (McKay/nauty-Traces), F1-F6 inline + F7 online, iso-rejection every
  level, distributed by depth-d canonical prefix; seed from forced 7K2/triangle fragments. Eigenspace-
  first is the alternative only if vein B beats canonical-augmentation on calib graphs.
LIGHT-SAMPLING EVIDENCE (calibrated, no over-prune):
  - prune_estimate.py: per-extension LOCAL accept ~0.18-0.39, geo-mean ~0.25 (F1-F6 kill ~75% of
    children at creation but do NOT collapse a depth-55 tree alone).
  - spectral_rarity.py: 120 random local-valid 55-graphs in the e-band -> MAX mult of eig~3 = 0; 0%
    pass F8(c). The spectral gate is HIGH-CODIMENSION / near-total TERMINAL rejecter (cannot be reached
    by random post-filtering) => THIS is why Stage A is the wall; motivates F7 + eigenspace-first.
  - interlace_online.py: F7 schedule verified on the REAL Kneser star complement, 0/720 induced-subgraph
    interlacing violations => F7 SOUND, no over-prune.
COST MODEL (honest, order-of-magnitude): SINGLE BIGGEST DRIVER = Stage-A node count N_A (isomorph-free
  55-vtx enumeration under local constraints) — comparable to/harder than the paused Z3 a=24 cell;
  budget 10^4-10^7+ core-hours, true number set by how early F7+iso-rejection collapse the tree (the §3
  slice MUST measure it before committing budget). Surviving-H count S is small-but-unknown a priori
  (spectral gate near-total). Stage B is CHEAP and NOT the bottleneck: W0 prefilter (codim 10-11,
  >64.5x) -> O(10) columns -> 44-clique microseconds -> closure; t_B ~ 1ms-1s; Stage-B core-hours =
  S*t_B/3600 ~ <=280 even at S=1e6,t_B=1s (sub-1% of total). Every optimization dollar -> Stage-A tree.
THIN SLICE GO/NO-GO: STEP0 soundness gates green on Kneser/srg40/rook9 (0 false reject, exact recon);
  STEP1 generate 200-1000 valid H (record e,m3,theta_1,det-7-val,col-weight hist); STEP2 run Stage B to
  completion (|B(H)|, post-W0 count, max clique, 44-clique); STEP3 read failure-category histogram
  (i spectrum / ii W0-empties-weight-class / iii max-clique<44 record actual / iv closure-nonzero=BUG
  halt / v candidate->hard-verify). GO to scale iff STEP0 green, histogram dominated by (i)/(iii), no (iv).
HIGHEST-LEVERAGE NEXT TIGHTENING: strengthen F7 from a single mult_3 schedule to a FULL interlacing
  envelope online: (1) two-sided mult_3 window (lower k-45 AND host-54 upper); (2) lambda_min(partial_k)
  > -4 PD check at EVERY depth (hereditary, immediate, sound); (3) push the schedule below k=46 via
  det-7-valuation / corank_F7 growth. Each MUST pass the Stage-A soundness gate (0 false reject of real
  Kneser/srg40 induced subgraphs) — the cheapest way to cut N_A (the sole driver) by attacking the
  spectrum at every level, not just the leaves. Secondary: eigenspace-first generation (gate by construction).
OUTCOME: spec hardened (ordered pipeline + generation order + calibrated cost model + slice go/no-go +
  the F7 online-interlacing prune, verified no-over-prune on a real graph). No new kill (consolidation
  vein, as directed). Confidence HIGH (FINAL_GATE green; 3 light-sampling scripts; 0 false-reject on
  real witnesses). NEXT ACTION unchanged: awaiting user decision on the cloud job (CLOUD_SPEC_SC.md).

## R36 — FORCED DEGREE SEQUENCE + EIGENSPACE-FIRST GENERATION (vein: degree band & gen-strategy).
## Validated on BOTH real s=-4 graphs (Kneser K(7,2)=srg(21,10,3,6); srg(40,12,2,4) BUILT this iter via
## the Sp(4,3) symplectic graph, spectrum 12^1,2^24,(-4)^15 verified). Light sampling only (seconds-min).
## scripts: scratchpad/{degseq_derive,kneser_degvalidate,build_srg40,srg40_degvalidate,srg40_margin0_hunt,
##          srg40_maxmult,final_band_prune,eigenspace_first,margin0_regularity_mechanism}.py

(A) FORCED DEGREE BAND for srg99 H (nH=55, host k=14, r=3, s=-4, |X|=44). All per-vertex/sum facts
    re-derived and checked for OVER-PRUNE on every real star complement (0 false rejects):
  - (D1) per-vertex hard cap  **0 <= deg_H(v) <= 14**. NOT tighter: the column-weight floor (>=1) is an
    X-SIDE constraint (44 columns each weight>=1 => e(H)<=363), it does NOT force deg_X(v)>=1 for H-side
    vertices, so deg_H(v)=14 is a-priori admissible (then all 14 of v's host-nbrs lie in H, contributing
    7 of H's edge-disjoint triangles at v). The earlier "deg_H<=13 for star-set-adjacent vertices" is
    only valid for the SPECIFIC H-vertices that happen to have an X-neighbour — NOT a universal band.
  - (D2) **Sum deg_H = 2 e(H)**; with the binding e(H) in [154,319] => Sum in [308,638], avg deg in
    [5.60,11.60]. (m3=11 branch e<=358 => Sum<=716, avg<=13.02; counting e<=363 => <=726.)
  - (D3) local 7K2: triangles AT v <= floor(deg_H(v)/2) <= 7 (N_H(v) a partial matching).
  - SOUNDNESS: over ALL 35917 Kneser SCs and 17k sampled srg40 SCs, **0 violations** of (deg_H<=k AND
    lambda_min>-4). Band is sound (final_band_prune.py, kneser_degvalidate.py, srg40_degvalidate.py).

  ** DOES mult_3=11 (margin-0) FORCE a tighter / near-regular degree sequence? — CALIBRATED ANSWER: NO
     (for srg99), despite a Kneser artifact suggesting YES. This is a verify-to-accept SAVE. **
   - Kneser margin-0 (mult_r=9, the 7 real SCs): degree sequence is EXACTLY REGULAR (all 6's, spread 0,
     variance 0), e(H)=45 pinned. This *looks* like "margin-0 => regular".
   - BUT the mechanism (margin0_regularity_mechanism.py) is CAUCHY-SCHWARZ TIGHTNESS: at margin-0 the
     non-r eigenvalue block collapses to a SINGLE value (Kneser: nH-m3 = 15-9 = 6 eigenvalues collapse
     to {6,(-3)^5}) => <=3 distinct eigenvalues => regular. That collapse is a SMALL-CASE artifact.
   - srg99 margin-0: non-r block has nH-m3 = 55-11 = 44 eigenvalues; the CS bound gives only e>=62
     (vs the 154 floor), HUGE slack => NO collapse => NOT forced regular. Confirmed: there is NO
     exactly-regular 3-eigenvalue (theta_1, 3^11, x^43) integer solution with x>-4 (checked d=1..14).
   - INDEPENDENT CONFIRMATION on srg40 (bigger non-r block, nH-m3=15 at margin-0): margin-0 SCs are
     RARE/ABSENT (0 found in 100k random subsets + 300 hill-climbs + 60-restart SA; max true-SC mult_r=9
     =floor). The margin-1 (mult_r=9) SCs there have degree spread 5-8, variance ~2 — clearly NOT regular,
     NOT tight. => Across the two real s=-4 graphs the "margin-0 => near-regular" hope holds only where CS
     is artificially tight (tiny non-r block). For srg99 it is FALSE. RECORD: m3=11 does NOT yield a
     tighter degree band than m3=10. (The operative m3=11 lever remains R34's "columns maximal weight =>
     e(H) low end" — a SUM/edge-count pull, not a per-vertex-regularity pull.)
   - PRUNE VALUE of the degree band: SMALL. The band is a cheap online sanity filter (Sum in [308,638],
     per-vertex<=14), but it is implied by F6 (e-band) + F1 (maxdeg). It is NOT a new high-codimension
     cut. The real Stage-A wall is the SPECTRUM (R35 spectral_rarity: 0/120 random local-valid 55-graphs
     even have an eigenvalue near 3) — degree-sequence shaping does not touch that.

(B) EIGENSPACE-FIRST GENERATION — assessed + calibrated. VERDICT: NOT materially cheaper than canonical
    augmentation for the generic case; viable only as a constrained sub-strategy. Reasons (all measured):
  - (E1) r=3 is a NON-MAIN eigenvalue of H on every sampled real SC (Kneser 20/20, srg40 20/20: the
    r-eigenspace is orthogonal to all-ones). GOOD news for an equitable-partition approach IN PRINCIPLE.
  - (E2) BUT the coarsest equitable partition (WL-1 refinement) of real SCs has #cells ~ nH (Kneser mean
    10.9/15, srg40 mean 24.5/25) => essentially TRIVIAL quotient structure. A high-multiplicity eigenvalue
    does NOT force a small equitable quotient here — the eigenspace is "spread out", not few-celled. So the
    classic "prescribed-eigenvalue => small parameter quotient" leverage does NOT apply: eigenspace-first
    would still face a near-full DOF problem.
  - (E3) DOF accounting (eigenspace_first.py): a symmetric 0/1 55-vtx H has C(55,2)=1485 free bits.
    Prescribing the 3-eigenspace as a fixed rational m3-subspace U pins each adjacency row into U^perp
    (dim 44-45) — but U ITSELF is unknown (only its DIM is forced) AND must satisfy the integral/lattice
    gates (7^10|det(A_H+4I), corank_F7). So eigenspace-first does NOT remove a combinatorial layer; it
    REPLACES "search graphs" with "search (integer m3-subspace U) x (0/1 rows in U^perp)" — a SECOND
    combinatorial layer with no canonical-form/iso-rejection machinery (nauty has none for subspaces).
  - RECOMMENDATION: keep **canonical augmentation (McKay/nauty-Traces)** as the Stage-A spine (R35
    pipeline F1-F12). Use the eigenspace ONLY as an ONLINE PRUNE, never as the generation primitive:
    i.e. R35's F7 online Cauchy-interlacing schedule (mult_3(partial_k) >= k-45; lambda_min(partial_k)>-4
    PD at every depth) is the correct way to inject the eigenspace constraint — it attacks the
    near-total spectral codimension MID-TREE without paying for a subspace search. Eigenspace-first as a
    standalone generator is NOT recommended (no iso-rejection, extra layer, generic quotient is trivial).

OUTCOME: (i) forced degree band stated + proven sound (0 over-prune on 2 real s=-4 graphs); (ii) the
  "m3=11 => near-regular degree sequence" hope FALSIFIED for srg99 (Kneser regularity is a CS-tightness
  artifact; srg40 has no regular margin-0 SC; no integer regular 3-eig solution) — a real-graph witness
  again caught a would-be false tightening; (iii) eigenspace-first generation assessed NOT cheaper
  (non-main but trivial equitable quotient; extra subspace-search layer; no iso-rejection) => recommend
  canonical augmentation + eigenspace-AS-ONLINE-PRUNE (R35 F7). Degree band prune value: LOW (subsumed by
  e-band+maxdeg). The Stage-A wall remains the SPECTRUM, not the degree sequence. Confidence HIGH
  (exact degree counts; validated on Kneser exhaustively + srg40 sampled; 0 false rejects). New artifact:
  scratchpad/build_srg40.py reproduces srg(40,12,2,4) for future s=-4 calibration. NEXT ACTION unchanged.

## R37 — LOCALLY-7K2 LOCAL PREDICATES: exact ONLINE form, forbidden-subgraph set, calibrated prune.
## Vein: strongest induced-subgraph (locally-7K2/lambda1/mu2) pruning predicates (R35 F2-F4 sharpened).
## Validated on REAL lambda=1,mu=2 graphs (rook9=srg(9,4,1,2) EXHAUSTIVE; BvLS243=srg(243,22,1,2)) and
## the s=-4 controls. Light sampling (seconds). scripts: sc_localpred.py, sc_localpred_run.py,
## sc_localpred_validate.py, sc_localpred_prune.py, sc_localpred_strat.py (all in .work/99graph/).

THE PREDICATES (each inherited by EVERY induced subgraph of srg99; one-directional necessary):
  P1 LOCAL PARTIAL MATCHING. N_H(v) induces max-degree <=1 for all v (=> deg_H(v)<=14; v in
     <=floor(deg_H(v)/2) triangles, edge-disjoint at v). [from N_G(v)=7K2]
  P2 EDGE IN <=1 TRIANGLE. every edge uv: |N_H(u) cap N_H(v)| <= 1 (triangles edge-disjoint). [lambda=1]
  P3 NONADJ-PAIR <=2. every nonadjacent pair uv: |N_H(u) cap N_H(v)| <= 2. [mu=2]

EXACT ONLINE (canonical-augmentation) FORM — PROVEN equivalent to full re-check (0 mismatches / 20000
  random valid-partial extensions, sc_localpred_prune.col_valid_incremental). Adding vertex w with nbr
  set R changes exactly: (a) w's link; (b) N(v) gains w for v in R; (c) common-nbr count of each pair
  in R gains +1. The cheap reject re-checks ONLY these, in O(k^2):
   - deg(w)<=14, deg(v)+1<=14 for v in R;
   - P1@w: R induces max-deg<=1; P1@v (v in R): (A.c)[v]<=1 AND the <=1 common member had in-N(v) deg 0;
   - P2: existing edge i-j with i,j in R must have had 0 common nbrs (w would make a 2nd triangle);
   - P3: (i) v not in R: (A.c)[v]<=2; (ii) existing NONadj pair i,j in R must have had <=1 common nbr.
  THE (c)-class checks (existing pairs both adjacent to w) were the non-obvious ones — a naive
  "check only w's pairs" online form is WRONG (caught by the 0-mismatch gate: 314 mismatches before fix).

FORBIDDEN INDUCED-SUBGRAPH SET (exact enumeration of all iso classes, m<=5):
  m=4: {K4, diamond=K4-e} — the ONLY two; both violate P1 & P2.
  m=5: 13 forbidden classes; ALL caught by an online P1/P2/P3 check. The only one NOT reducible to a
       <=4-vtx sub-violation is **K_{2,3}** (a nonadj pair with 3 common nbrs) — caught by P3, which is
       intrinsically a 5-vtx per-pair check (still online: inspects only present vertices).
  => P1,P2,P3 are a COMPLETE encoding of the local forbidden set: no separate "forbidden-subgraph list"
     is needed in the generator beyond running P1/P2/P3 per vertex/edge/pair. (B2/book/butterfly/gem/W4
     etc. all contain a K4/diamond/K_{2,3} and are thus already rejected.) m=6 randomized-embed test was
     INCONCLUSIVE (no-solution-found != obstruction; the FINAL_REPORT golf-hole trap) — NOT claimed.

VALIDATION — NO OVER-PRUNE (must NOT reject a real witness):
  - rook9 (locally 2K2, lambda1 mu2): ALL 511 nonempty induced subgraphs pass P1&P2&P3 (0 rejects). DECISIVE.
  - BvLS243 (locally 11K2): 3000 induced subgraphs (size 5..55) pass (0 rejects).
  - CONTROL (teeth + correct-specificity): Kneser K(7,2) [lambda=3] subgraphs are rejected ~89% by P2 —
    the predicates are NON-vacuous and CORRECTLY srg99-family-specific. KEY GROUND-TRUTH: Kneser/srg40
    are s=-4 SPECTRAL controls (calibrate the CRS/eigenvalue framework) but NOT lambda1mu2, so they are
    NOT validators for P1-P3 (they SHOULD violate them). The first run mis-applied them and "rejected"
    35910/35917 Kneser SCs — corrected to rook9/BvLS, the real lambda1mu2 witnesses.
  - AT SCALE: 200/200 predicated orderly builds reach n=55, all pass full re-check (0 drift).

PRUNE FACTORS (light sampling, calibrated):
  - Per-vertex matching-link reject (P1, fires when a vertex completes degree d, O(d^2)): d=4 25%,
    d=6 67%, d=8 91%, d=10 99%, d=12 99.9%, d=14 100% (vs random link at p=0.18). Cheapest, strongest.
  - DEGREE-STRATIFIED column survival (decision-relevant: generator augments by a fixed-weight column;
    fraction of weight-d columns passing the online reject):
       k\d:   w2     w4     w6     w8    w10   w12   w14
        20   93%    57%    19%   4.8%   0.3%   0%    0%
        40   89%    48%    12%   0.8%   0.1%   0%    0%
        50   88%    44%    9.3%  0.8%   0%     0%    0%
    => HEAVY columns (the costly branches, since srg99 col-weight = 14-d_X(u)) are crushed: weight>=10
    essentially eliminated at large k; weight<=4 survive freely. Exactly matches where Stage-A spends time.
  - Per-step column-branching (Bernoulli-density model, vs degree-capped baseline), product over 54 steps:
    p=0.12 (avg deg 6.5) geomean-surv 0.64 => ~10^-10 tree-shrink; p=0.18 (deg 9.7) 0.27 => ~10^-31;
    p=0.24 (deg 13) 0.08 => ~10^-59. Prune GROWS sharply with density (matches R35: mild at sparse end,
    decisive at dense end). ORTHOGONAL to (and multiplied by) iso-rejection and the terminal spectrum gate.

CONSISTENCY WITH R35/R36: confirms R35's "F1-F6 local ~0.25 geomean accept, do not collapse the tree
  alone" with sharper per-weight numbers, and supplies the EXACT online incremental forms (proven by a
  0-mismatch gate) ready to bake into the augmentation step. The SPECTRUM remains the wall (these local
  cuts trim the heavy-column branches hardest but cannot reach the high-codimension eigenvalue-3 gate);
  the local predicates' job is to make the tree the spectral gate must traverse as thin as possible.

OUTCOME: R35 F2-F4 hardened into proven-exact O(k^2) online rejects + the complete (and minimal)
  forbidden-induced-subgraph set {K4, diamond, K_{2,3}} + calibrated degree-stratified prune factors.
  0 false rejects on rook9 (exhaustive) + BvLS243 + s=-4 controls. NO new kill (necessary-only, by the
  task bar a real lambda1mu2 graph satisfies all). Confidence HIGH (exact online==full gate green;
  validated on real witnesses). NEXT ACTION unchanged: cloud Stage-A job (CLOUD_SPEC_SC.md F1-F12).

## R38 — CONSOLIDATION: ordered Stage-A pipeline (verifier-confirmed predicates only) + R37 folded in.
## Vein: synthesize R35(filters+cost)/R36(degree+eigenspace)/R37(local predicates) into the final
## CLOUD_SPEC_SC.md; independently re-verify every retained predicate is 0-over-prune on REAL s=-4 graphs.
## Light compute (seconds). Scripts (scratchpad): consolidate_verify2.py (rebuilds Kneser K(7,2) +
## Sp(4,3)->srg(40,12,2,4), 1500 real SCs each), prune_recheck.py (degree-stratified accept + spectral
## rarity). Re-ran .work/99graph/FINAL_GATE.py = ALL GATES GREEN.

INDEPENDENT RE-VERIFICATION (this iter, from-scratch graph rebuilds; NOT trusting prior reports):
  Kneser K(7,2)=srg(21,10,3,6): eigenvalues 10, r=1 (m_r=14), s=-4 (m_s=6); SC size nH=15; mult_r floor 8.
  srg(40,12,2,4) via Sp(4,3) symplectic graph: eigenvalues 12, r=2 (m_r=24), s=-4 (m_s=15); nH=25; floor 9.
  (NOTE for future calib: r = the OTHER restricted eigenvalue, graph-specific — r=1 Kneser, r=2 srg40,
   r=3 srg99. An earlier verify script hardcoded r=3 for the calib graphs and got mult_r=0; self-caught.)
  Over 1500 sampled REAL s=-4 star complements of EACH graph:
    F1  deg_H(v)<=host_k        : 0/1500 viol on both.  maxdeg_H REACHES host_k (10 Kneser, 12 srg40).
    F7  Cauchy interlacing sched: 0 viol (400 SCs x 3 nested k-cuts each, both graphs).
    F8b lam_min(H) > -4 strict  : 0/1500 viol on both.
    F8c mult_r in {floor,floor+1}: 0/1500 viol; observed exactly {8,9} Kneser / {9,10} srg40 = the
        srg99 analog of m3 in {10,11}.
    UNSOUND deg_H<=host_k-1 rule: DROPS 63/1500=4.2% (Kneser) and 31/1500=2.1% (srg40) REAL SCs.
        => F5's CAUTION is load-bearing; the on-disk spec correctly keeps 0<=deg_H<=host_k.
  Prune factors re-measured: per-extension local accept geomean ~0.34 (mid-weights; spec cites ~0.25
    over all weights, same order — my rougher partials are sparser/more permissive); heavy columns
    (w>=10) crushed (<=8% at k=20, ->0% at k=50). Spectral rarity: 60 random local-valid 55-graphs,
    MAX mult of eigenvalue 3 = 1 (need >=10) => spectral gate near-total; the SPECTRUM is the wall.

RECONCILIATION of the two synthesizer verdicts:
  - degree-multiplicity vein (R36) "confirmed": UPHELD. F1 is the host cap (not k-1); the m3=11
    near-regularity hope is correctly falsified; eigenspace-first correctly demoted to the online prune.
  - spec-cost vein (R35) "overclaimed" (F5 over-prunes): the flagged defect was in the OLDER R35 text;
    it was already FIXED by R36 in the on-disk spec (F5 now 0<=deg_H<=host_k + explicit CAUTION), and I
    independently re-confirmed BOTH directions (0 over-prune of F1; deg<=k-1 drops real witnesses). The
    two other spec-cost doc-fixes (F2/F3/F4 witness should be rook9 not Kneser; e<=319 must be SOFT not
    hard) are also already reflected (R37 names rook9/BvLS243; F6 lists e<=358 HARD, 319 AGGRESSIVE).

CHANGES WRITTEN TO CLOUD_SPEC_SC.md this iter:
  - Header: R36+R37 hardening noted; added the independent consolidation re-verify line.
  - Pipeline §1: appended the R37 IMPLEMENTATION NOTE — exact O(k^2) online F2/F3/F4 incremental form
    (incl. the (c)-class existing-pair re-check that the 0-mismatch gate proved necessary), the COMPLETE
    minimal forbidden induced set {K4, diamond, K_{2,3}}, and the degree-stratified prune table.

FINAL CONSOLIDATED ORDERED PIPELINE (verifier-CONFIRMED predicates only; F5 = host cap, NOT k-1):
  ONLINE LOCAL (baked into augmentation, geomean accept ~0.25-0.34/extension, heavy-column crush):
    F1 deg<=14 ; F2 N(v) matching ; F3 edge<=1 triangle ; F4 nonadj<=2 ; F5 0<=deg<=14 + sum band ;
    F6 e(H) in [154,358] HARD (363 SOFT, 319 AGGRESSIVE-not-hard).
  ONLINE SPECTRAL (depth>=46): F7 Cauchy-interlacing schedule mult_3(partial_k)>=k-45.
  TERMINAL: F8 spectrum (det(A+4I)!=0; lam_min>-4; m3 in {10,11}; eigs in (-4,14]) ; F9 7^10|det ;
    F10 corank_F2/F7>=m3 ; F11 m3 third-moment ; F12 triangle-split polytope.
  STAGE B (cheap, sub-1%): B1 W0-orthogonality prefilter (64.5x calib) ; B2 diagonal ; B3 44-clique ;
    B4 exact 0/1 closure verify.

COST / SHRINK vs prior spec: the binding shrinks are (i) e-band UPPER 384->358 HARD (R34 m3=11), a
  ~30-edge tightening of the admissible window; (ii) F7 converts the near-total spectral gate from a
  k=55-only terminal reject into an online reject at the WIDEST levels (k>=46), the single biggest N_A
  lever; (iii) W0 prefilter codim 8->10/11 (Kneser 64.5x; srg99 STRONGER) shrinks Stage B per H. The
  DOMINANT cost driver remains N_A = isomorph-free 55-vtx node count (10^4-10^7+ core-hours, true value
  set by how early F7+iso-rejection collapse the tree — the §3 thin slice MUST measure it). Stage B is
  sub-1%. Degree-shaping and eigenspace-first generation were ASSESSED and give NO first-order N_A cut.

NEXT ACTION (single highest-leverage, unchanged from §6): STRENGTHEN F7 from a 1-eigenvalue schedule to
  a FULL online interlacing envelope — (1) two-sided mult_3 window (k-45 lower AND a host-54 upper),
  (2) lambda_min(partial_k)>-4 PD check at EVERY depth (hereditary, cheap, sound), (3) push the schedule
  below k=46 via det-7-valuation / corank_F7 growth. Each MUST pass the §1 soundness gate (0 false
  reject of any real Kneser/srg40 induced subgraph at every depth). This attacks the spectrum — the wall
  — at every level instead of only the leaves, directly shrinking N_A.

## R39 — TWO-SIDED ONLINE INTERLACING WINDOW on mult_3(partial_k) (vein: NEXT-ACTION item 1).
## Validated on REAL s=-4 graphs (Kneser K(7,2)=srg(21,10,3,6); srg40=Sp(4,3)=srg(40,12,2,4)) at
## EVERY depth, 0 false-reject; rook9 master-inequality exhaustive. Light compute (seconds).
## scripts (scratchpad/): f7_twosided_derive.py, f7_twosided_tighten.py, f7_twosided_validate.py,
##   f7_twosided_prune.py, f7_upper_diagnose.py, f7_envelope_tighten.py. (builders reused from hered_pd.py)

DERIVED (exact, sound).  partial_k = principal k x k submatrix of A_H (k<=55), H the 55-vtx SC.
  MASTER INEQUALITY (one-deletion interlacing, iterated):  for any value v and t deleted vertices,
        | mult_v(sub) - mult_v(super) |  <=  t .            [exhaustively verified rook9: 0 viol]
  Apply v=3, super=H, t=55-k, with FORCED mult_3(H) in {10,11}:
        LOWER (existing F7):  mult_3(partial_k) >= 10 - (55-k) = k - 45 .
        UPPER (NEW)        :  mult_3(partial_k) <= 11 + (55-k) = 66 - k .
  TWO-SIDED ONLINE WINDOW:   max(0, k-45)  <=  mult_3(partial_k)  <=  min(k, 66-k) .
  Online predicate (O(k^3) eigensolve): REJECT partial_k if mult_3 < k-45 OR mult_3 > 66-k.
  - Leaf k=55: window [10,11] == F8(c) ceiling EXACTLY (cross-check passes).
  - Upper BITES (66-k < k) for all k>=34; depth schedule of the ceiling:
       k=34->32, 40->26, 46->20, 50->16, 53->13, 54->12, 55->11.
  - The G-DIRECT upper bound (partial_k in 99-vtx G, mult_3(G)=54) = min(k,153-k) = k => VACUOUS.
    The H-side bound (uses mult_3(H)<=11) is the binding one. The bare per-index interlacing-vs-G
    upper is also vacuous (every position's interval [lo_i,up_i] contains 3 for k<=55).
  NEAR-BAND ENVELOPE (same machinery): mult_(-4)(partial_k) in [0, min(k,44)] (no -4 pinned, since
    lam(i)=-4 needs i>=56>k); #eigs>3 in partial_k <= 1 (only Perron; lam_i(G)>3 only at i=1).

SOUNDNESS (0 false-reject, both sides, EVERY depth k=1..nH) — f7_twosided_validate.py:
  Kneser: 11726 induced subgraphs of 20 real SCs, depths 1..15 -> LOWER viol 0, UPPER viol 0.
  srg40 : 21262 induced subgraphs of 20 real SCs, depths 1..25 -> LOWER viol 0, UPPER viol 0.
  Tightest UPPER slack on a real sub = 1 (the bound came within 1 of firing => genuinely tight,
  not loose). Observed mult_r(real SC) sat at the FLOOR in 100% of random SCs (Kneser 8, srg40 9),
  so the M_max=floor+1 branch is rare. PD re-check (hered_pd): lam_min(P)>-4 0 viol both graphs.

EXTRA PRUNE over lower-bound-only F7 — f7_twosided_prune.py / f7_upper_diagnose.py (THE HONEST RESULT):
  >> Measured EXTRA PRUNE FACTOR = 0.0000 in EVERY sampled regime, including ADVERSARIAL overshoot
     (induced subgraphs of the WHOLE calib graph G, the highest-mult_r population). <<
  MECHANISM (ground-truthed, f7_upper_diagnose.py): the observed MAX mult_r over induced subgraphs
  at depth k runs FAR below the 66-k ceiling in the interior (slack grows to 6 [Kneser] / 13 [srg40]
  mid-tree) and only reaches the ceiling at k=nH (srg40 BINDS at k=25; Kneser slack 1 at k=15).
  WHY: random local-valid / interlacing-feasible partials UNDERSHOOT mult_3 (~0, per R35
  spectral_rarity) — they are killed by the LOWER bound; they cannot pile r-eigenvalues ABOVE the
  lower-bound line until depth ~nH-1, where the TERMINAL gate F8(c) (mult_3 in {10,11}) already
  fires. So the upper window is binding only at the last 1-2 levels (srg99: k=54,55) where F7's
  lower bound + F8(c) are already active. Net mid-tree N_A reduction from the UPPER bound: ~0.

CAN A TIGHTER SOUND BOUND EXIST? — f7_envelope_tighten.py. The interior gap (ceiling 12 vs observed
  max 1-2 at srg40 k=12) is REAL, so a much tighter upper envelope is mathematically possible — BUT
  it is NOT obtainable from interlacing alone (interlacing yields only the bare min(k,66-k)). The
  reason real subs sit low is the lambda=1/mu=2 LOCAL structure limiting r-eigenvalue accumulation,
  which is ALREADY enforced by F2/F3/F4 (the local block), not by any spectral inequality. A bound
  matching the observed envelope would be an empirical fit (UNSOUND without proof) — NOT shipped.

VERDICT (verify-to-accept SAVE): the two-sided UPPER window is SOUND and exactly TIGHT at the leaf
  (reproduces F8(c)), so it is a correct, free add to F7 (one extra integer compare on the eigensolve
  that F7 already runs at k>=46 — zero added cost). But it delivers ~0 EXTRA mid-tree prune over the
  lower-bound-only F7, because spectral OVERSHOOT does not occur in interlacing-feasible partials
  until the leaf. The hoped-for "prune branches that overshoot" lever is real in principle but EMPTY
  in practice for this spectrum. The Stage-A wall (R35-R38) is UNCHANGED: it remains the LOWER F7 +
  terminal F8(c) high-codimension gate; the heavy lifting on N_A still comes from local F2/F3/F4
  (heavy-column crush) + iso-rejection, NOT from a spectral upper bound.

RECOMMENDATION for CLOUD_SPEC_SC.md F7: state the window as max(0,k-45) <= mult_3(partial_k) <= 66-k
  and ADD the upper compare (free, sound, tight-at-leaf, cross-checks F8(c) early at k=54). Do NOT
  claim it cuts N_A: its measured extra prune is 0; F7's value remains its LOWER bound. The PD reject
  lam_min(partial_k)>-4 at every depth (hered_pd, also sound 0-false-reject) is the more useful
  always-on companion. Confidence HIGH (exact derivation; rook9 exhaustive; 60k+ real-sub samples,
  0 false-reject; mechanism ground-truthed). NEXT ACTION (item 2 lam_min PD already validated here;
  item 3 det-7/corank-growth below k=46 still open) unchanged otherwise.

---

## R39 — VEIN: Hereditary lambda_min>=-4 PD at every depth + det-7/corank growth schedule [2026-06-29]
## OUTCOME: (1) NEW sound online reject F8b' (PD at EVERY depth, big prune below k=46). (2) det-7
##          schedule = HONEST NO: no sound monotone partial analog beats F7. Both VALIDATED on reals.

Addresses the spec §6 / NEXT-ACTION items (2) and (3) for strengthening F7.

(1) HEREDITARY PD REJECT  [SOUND, NEW, high-leverage]
 THEOREM: H (s=-4 star complement) has lambda_min(A_H) > -4 strict. By Cauchy interlacing INSIDE H,
   every induced subgraph P of H has lambda_min(A_P) >= lambda_min(A_H) > -4. Every canonical-aug
   partial_k IS an induced subgraph of the final H => A_{partial_k}+4I must be POSITIVE DEFINITE at
   ALL depths. PRUNE any partial_k with lambda_min <= -4 (A_P+4I not PD).
 SOUNDNESS (scratchpad/hered_pd.py): 0 false-reject over 27,914 induced subgraphs of REAL Kneser
   K(7,2) + srg(40,12,2,4) star complements across EVERY depth k=1..nH; min margin lam_min(P)-(-4)
   = +0.0267 (Kneser) / +0.0510 (srg40). Incremental form (hered_pd_ldl.py): 0/6614 mismatch vs
   from-scratch exact PD; 0 false reject over 975 real-SC growth-path pivot tests, min Schur pivot
   0.27/0.39 > 0.
 PRUNE (hered_pd_prune.py / hered_pd_ldl.py): on RANDOM local-valid (F1-F6) partials the PD reject
   FIRES (lam_min<=-4) at: k=30 dens0.2 mean lam_min -3.70 (approaching); k=40 dens0.2 60.8%, dens0.35
   62.5%; k=46 dens0.2 100%, dens0.35 98.3%; k=55 100%. On 200 random local-valid GROWTH PATHS the
   reject killed 83 (41.5%). Mean lam_min crosses -4 between k=30 and k=46 for the e-band densities.
   => bites a FULL ~6-15 levels BELOW F7 (which only starts k>=46), at near-100% on dense partials.
 IMPLEMENTATION: incremental bordered LDL/Cholesky. M_{k+1}=[[M_k,r],[r^T,4]]; child PD <=> parent PD
   AND schur=4 - r^T M_k^{-1} r > 0. Maintain L,D of M_k=LDL^T; per node: solve L y=r (O(k^2)),
   schur=4-sum y_i^2/D_i; accept iff schur>0; append pivot D=schur, row y_i/D_i. One triangular solve,
   O(k^2), vs O(k^3) eigensolve. NOTE (honest): pure-python float LDL only ~1.5x faster than numpy
   LAPACK eigvalsh here (interpreted vs C); the WIN is algorithmic O(k^2) + reuse across the tree (a
   BLAS Cholesky-update realizes it). Use exact Fraction LDL on boundary nodes |schur|<eps to avoid
   float false-reject (Fraction incremental verified 0-mismatch).
 => RECOMMEND adopting as F8b' (the at-every-depth PD reject), upgrading the spec's F8(b) from a
    terminal-only check to an online one. Strictly stronger than nothing below k=46; complements F7.

(2) det-7 VALUATION / corank_F7 GROWTH SCHEDULE  [HONEST NO — no sound monotone partial analog]
 DERIVATION: the ONLY forced lower-bound mechanism is integer-eigenvector reduction: an integer
   3-eigenvector v gives (A_P+4I)v=7v≡0 mod7, so corank_F7(A_P+4I) >= mult_3(P) and likewise
   v_7(det(A_P+4I)) >= mult_3(P). But mult_3(P) >= max(0,k-45) is EXACTLY F7's content => both the
   corank_F7 and det-7-valuation schedules REDUCE TO F7; they fire no earlier than k=46. Any EXCESS
   corank over mult_3 is graph-structural, NOT forced for a general H.
 VALIDATION (det7_schedule.py / det7_soundness.py / det7_fast.py, on real SC subgraphs, every depth):
   - Kneser p=5 (clean prime analog of srg99 p=7): excess corank over mult_r = 0 EVERYWHERE
     (min0/max1/mean0.014 over 500 reals; min over reals == interlacing floor at every k). Confirms
     corank tracks mult_r; schedule == F7.
   - srg40 p=2: min real corank is NON-MONOTONE (1,0,1,0,... parity) AND drops BELOW the interlacing
     floor at k=16..24 (excess -1) => even a corank-version of F7 over-prunes if applied mod 2.
   - srg40 p=3: a CONSTANT +4 plateau (structural symplectic-mod-3 excess, the BvLS/L4 phenomenon),
     not growing, not present at the srg99-relevant prime 7.
 => HONEST VERDICT: NO sound monotone partial-graph det-7/corank-F7 analog grows faster than F7. The
    7-divisibility wall cannot be pulled below k=46 by this route. (Consistent with R31/L4: generic
    mod-7 corank tracks the real multiplicity; structural excess is family-specific.)

ARTIFACTS (scratchpad/): hered_pd.py, hered_pd_prune.py, hered_pd_ldl.py, hered_pd_timing.py,
   det7_schedule.py, det7_soundness.py, det7_fast.py.
NET: one NEW sound online reject (hereditary PD, F8b', fires ~6-15 levels below F7 at near-100% on
   dense local-valid partials) + an honest no-go on the det-7 schedule. Recommend spec update: add
   F8b' to the ONLINE-SPECTRAL block; mark the det-7-schedule item closed as 'no sound partial analog'.

## R40 — VEIN: Hybrid local-spectral mult_3 LOWER bound from partial moment data (e_k,t_k). [2026-06-29]
## OUTCOME: HONEST NO-GAIN. g(k,e_k,t_k) := tight moment-LP lower bound on mult_3(partial_k) given
##          (trace=0, sum mu^2=2e_k, sum mu^3=6t_k) + eigenvalue range (-4,14] is IDENTICALLY 0 <= k-45.
##          The 3 forced power-sum moments + range carry NO from-below information on mult_3.
##          => the spectral wall is INTERLACING-TIGHT mid-tree (k-45 cannot be beaten by moments).
## Validated 0-false-reject sense on REAL s=-4 graphs (Kneser K(7,2), srg40=Sp(4,3)) at EVERY depth.
## scripts (scratchpad/): g_moment_derive.py, g_real_validate.py, g_infeas_diag.py, g_void_proof.py,
##                        g_why_void_and_r34_invert.py.

DERIVATION (exact, LP-duality; NO empirical fit). partial_k = principal kxk submatrix of A_H, eigs
  mu_1..mu_k ALL in (-4,14] (lower from F8b' hereditary PD; upper interlacing vs G). Let m=mult_3.
  The tight lower bound implied by (range + 3 moments) is the value of the moment LP:
     g = min  mass-at-3   s.t.  a measure on (-4,14] of total mass k matches (m1=0, m2=2e_k, m3=6t_k).
  Since the TRUE spectrum (k unit atoms) is one feasible point, LP_min <= mult_3 ALWAYS => g is a SOUND
  lower bound by construction (can only under-estimate). MEASURED g on every real partial: g = 0.00.

WHY g=0 (the structural reason, ground-truthed two ways):
  (i) CONSTRUCTIVE WITNESS (g_void_proof.py): for EVERY real partial of both calib graphs at every
      depth -- INCLUDING the 1228 (Kneser) + 961 (srg40) partials whose ACTUAL spectrum has mult_r>0 --
      there exists a measure on (-4,hi] with ZERO mass at r matching all 3 moments. 1664/1664 (Kneser),
      2015/2015 (srg40). A 3-moment problem on a continuum, with r a single (measure-zero) point and
      support points on both sides of r, always admits a 0-mass-at-r representing measure. => g=0.
  (ii) DIRECTION (g_why_void_and_r34_invert.py P1): the only moment/Cauchy-Schwarz handle on m3 is the
      R34 inequality 2e >= r^2 m3 nH/(nH-m3); inverted for m3 given (e,k) it gives m3 <= 2ek/(2e+9k),
      an UPPER bound. Piling eigenvalues AT 3 is the LOW-variance config => moments bound mult_3 from
      ABOVE, never from below. Every cubic/quadratic SOS certificate (x-3)^2(x+4)>=0 etc. likewise
      yields UPPER bounds on m (caps the count NOT at 3), confirmed in g_moment_derive.py derivation note.
  (iii) 4th MOMENT DOES NOT RESCUE (P2): adding m4=trace(A^4) from the real partial, a 0-mass-at-r
      measure still exists for 1659/1660 (the 1 exception is a grid-boundary artifact). More moments
      do not create a from-below bound while the support is a continuum straddling r.

SOUNDNESS / 0-FALSE-REJECT (the GO/NO-GO bar): g <= true mult_3 on 100% of real partials (g=0 trivially
  never over-rejects). The moment-LP-as-feasibility gate also never rejects a non-degenerate real partial
  (the real spectrum is a witness); the only LP 'infeasible' hits were edgeless degenerate partials
  (all eigenvalues 0), a pure grid artifact (0 not a column), NOT a real bound (g_infeas_diag.py).
  Tested: ~1500-2000 real induced subgraphs per graph, depths 2..nH, both Kneser (nH=15) & srg40 (nH=25).

CONSISTENCY: independently RE-CONFIRMS R39's recorded mechanism ("real subs UNDERSHOOT mult_3; the low
  interior mult_3 comes from lambda=1/mu=2 LOCAL structure, NOT a pure spectral inequality; an empirical
  spectral fit would be UNSOUND") -- now proven from the LP-DUALITY side: the tight moment LP value IS 0,
  so there is provably no sound power-sum-moment bound to fit. A mult_3 lower bound beyond k-45 must come
  from the LOCAL block (F2/F3/F4, lambda1/mu2 limiting r-eigenvalue accumulation), which is not a moment
  fact. The Stage-A spectral wall (R35-R39) is UNCHANGED: F7 lower (k-45) + F8b' PD + terminal F8(c).

VERDICT: NO GAIN. g <= k-45 everywhere (g=0). No sound version false-rejects a real partial (g=0 is
  trivially sound). This CLOSES the "hybrid local-spectral moment mult_3 lower bound" vein: the spectral
  wall is interlacing-tight mid-tree on the LOWER side; moments (e_k,t_k) cannot tighten F7. Confidence
  HIGH (exact LP duality + constructive 0-mass-at-r witnesses on two real s=-4 graphs at every depth).

## R41 — NEW SOUND STAGE-A CUT  F8c'  HEREDITARY SECOND-EIGENVALUE CAP  lambda_2(partial_k) <= 3
## Vein: wildcard (any OTHER sound Stage-A cut). VALIDATED on REAL s=-4 (Kneser/srg40) + lambda1mu2
## (rook9/BvLS) graphs by EXACT integer inertia at EVERY depth, ~4.8M induced subs, 0 false-reject.
## scripts (scratchpad/): f8cprime_lambda2.py, f8cprime_sound_exhaustive.py, f8cprime_prune.py,
##   f8cprime_marginal.py, f8cprime_final_gate.py ; (a)-route negative: m6_census2.py, m6_extend.py.
##                                                                                         [2026-06-29]

DERIVATION (exact, sound). G=srg99 spectrum 14^1, 3^54, (-4)^44 => EXACTLY ONE eigenvalue > 3.
 By Cauchy interlacing lambda_i(A_P) <= lambda_i(A_G) for any induced P; so lambda_2(A_P) <=
 lambda_2(A_G) = 3 i.e. EVERY induced subgraph of G has AT MOST ONE eigenvalue > 3. H is induced
 in G and every canonical-aug partial_k is induced in H, hence in G:
       ONLINE REJECT (all depths k>=2):  PRUNE partial_k if it has >=2 eigenvalues > 3
       (equivalently lambda_2(A_partial_k) > 3).  Non-strict: lambda_2 == 3 is ALLOWED (P=H has it).
 EXACT online form (no float false-reject): #(eig > 3) = #(positive eigenvalues of A_P - 3I) =
 #positive pivots of a rational symmetric LDL of (A_P - 3I) [Sylvester inertia; 2x2 pivots for
 zero leading minors]. Cap = host's 2nd eigenvalue r (Kneser 1, srg40 2, srg99 3).

DISTINCT FROM EVERY SHIPPED FILTER (the key point):
 - F7 bounds mult OF 3 (middle multiplicity) from below, only at k>=46.
 - F8b' bounds lambda_MIN from below (>-4)  [BOTTOM of spectrum].
 - F8c' bounds lambda_2 from above (<=3)    [TOP/2nd eigenvalue] -- NEW REGION.
 Together F8b'+F8c' box the WHOLE partial spectrum into (-4,3] except one Perron top in (3,14].

SOUNDNESS (EXACT integer inertia, 0 false-reject -- same bar F8b' passed):
   rook9  ALL 502 nonempty induced subs (exhaustive)            : 0
   Kneser 212,418 induced subs                                  : 0
   srg40  4,605,638 induced subs (exact)                        : 0
   BvLS   3,840 induced subs                                    : 0
   + real STAR-COMPLEMENT induced subs every depth: Kneser 1260, srg40 1380 : 0
   TOTAL ~4.8M exact tests, 0 false-reject. exact-vs-float online form: 0/300 mismatch.

PRUNE POWER (the win -- measured on random LOCAL-VALID partials & growth paths):
 - vs F8b' head-to-head, the c'_only column (lambda_2>3 AND lambda_min>-4 = NEW kills F8b' MISSES):
     k=40 p0.10 62.5% NEW ; k=44 p0.10 93.3% NEW ; k=36 p0.15 88.3% NEW ; k=30 p0.20 40% NEW.
   F8b' bites DENSE partials (lam_min crashes); F8c' bites SPARSE/MID partials (a 2nd large eig
   appears from clustering well before lam_min hits -4). COMPLEMENTARY, two regimes.
 - ADDITIVE over the FULL shipped online block (local F1-F6 + F7 + F8b'): of growth paths
   surviving the old block at depth k, F8c' additionally kills: k=38 p0.10 50.7% ; k=42 p0.14
   99.3% ; k=34 p0.20 89.3%.  CRUCIALLY this fires at k~34-42 -- 4-12 levels BELOW F8b's dense
   range and BELOW F7's k>=46 floor -- so the spectral kill moves DOWN-TREE, pruning the whole
   subtree of ~8-16 extra levels. THIS is a first-order N_A lever (the wall is the spectrum; F8c'
   attacks the TOP of it mid-tree, which nothing shipped did).
 ONLINE COST: O(k^2) bordered-LDL update, reuses F8b's triangular solve (one extra negative-pivot
   counter on A_P - 3I). Net cost ~= F8b' (one more O(k^2) inertia, no extra eigensolve).

NEGATIVE RESULTS THIS ITER (honest, ruled out):
 - (a) 6-vtx forbidden subgraph beyond {K4,diamond,K2,3}: EXACT VF2 census -> only 2 locally-
   consistent 6-graphs (degseq[2,2,3,3,3,3], 8 edges) are absent from rook9(exhaustive)+BvLS(exact).
   BOTH are radius-1 ball-REALIZABLE (m6_extend.py: consistent lambda1/mu2/no-K4 ball exists) =>
   their BvLS-absence is GRAPH-SPECIFIC, NOT forced. NO sound 6-vtx forbidden cut (golf-hole trap
   avoided). The minimal forbidden set stays {K4, diamond, K2,3}.
 - (c) t_k/e_k moment coupling: CS lower / spec-radius upper on M=A_P+4I are sound but loose
   (slack 32-37) and weaker than local floor(e/3); CS-lower never exceeds local-upper on reals =>
   no collision-kill. Confirms the R40 moment vein: aggregate moments cannot tighten F7's mult_3.

RECOMMEND CLOUD_SPEC_SC.md: add F8c' to the ONLINE-SPECTRAL block beside F8b' --
   "lambda_2(partial_k) <= 3 (exact: #pos pivots of A_P-3I <= 1) at every depth k>=2; reject if a
   2nd eigenvalue exceeds 3." Sound (interlacing, 0 false-reject ~4.8M exact), cheap (O(k^2), reuses
   F8b' factor), and prunes a NEW spectral region (TOP) at k~34-42 -- the first online cut that
   fires materially BELOW both F8b's dense range and F7's k>=46 floor. Confidence HIGH.

## R42 — CONFIRM + STRENGTHEN + SPEC-FOLD: Part-A void (exact), Part-B B2==diamond, F8c' shipped. [2026-06-29]
## OUTCOME: (A) re-confirmed g(k,e_k,t_k)=0 AND strengthened it to a GRID-FREE EXACT-RATIONAL proof at
##          the actual srg99 params (r=3, range (-4,14]); (B) independent forcing proof B2==induced-diamond
##          (0 mismatch all graphs n<=6) re-confirms NO new 5/6-vtx forbidden subgraph; (C) found R41's
##          F8c' was NOT yet in CLOUD_SPEC_SC.md and FOLDED IT IN (the real online win to ship).
##          CALL: online Stage-A pruning is LARGELY EXHAUSTED; pipeline READY -> run the §3 thin slice.

PART A (hybrid local-spectral mult_3 lower bound) -- re-verified + strengthened to EXACT:
  - reran g_void_proof.py / g_real_validate.py: reproduce g=0 (1664/1664 Kneser, 2015/2015 srg40;
    0-mass-at-r witness exists even for the 2051 partials that genuinely contain eig r). CONFIRMS R40.
  - NEW partA_exact_void.py: 3 methods agree g=0 (explicit grid-free 4-node construction + r-free LP +
    min-mass-at-r LP objective) on 1505 Kneser + 2111 srg40 real partials; objective range [0,0].
  - NEW partA_srg99_exact.py: EXACT Fraction sweep at the srg99 params (r=3, (-4,14]) over the WHOLE
    reachable (e,t) box, k in [38,46]: 0 FAILURES in the reachable band (e>=2.8k) -- every reachable
    (k,e,t) admits an explicit rational measure with ZERO mass at 3 matching (m1=0,m2=2e,m3=6t). The
    only library-misses are the unreachable e<<2.8k near-empty corner (also LP-feasible). => g=0 PROVEN
    grid-free at the actual problem params, not just calib analogs. NO gain over k-45. Confidence HIGH.

PART B (wildcard forbidden 5/6-vtx subgraph) -- independent forcing proof, re-confirms R41(a):
  - partB_supplement.py: PROVES the only non-pairwise forcing visible to an induced sub -- "the 2 common
    nbrs of a non-adjacent pair must be NON-adjacent (else that edge is in 2 triangles, lambda=1 viol)"
    -- fires IFF the graph CONTAINS AN INDUCED DIAMOND. 0 mismatches over ALL 64+1024+32768 labelled
    graphs on n=4,5,6. The diamond is already shipped => this forcing adds NOTHING.
  - partB_forbidden_census.py / partB_census_fast.py: census of all non-iso graphs. n=5: 34 = 13 shipped
    + 21 realised-in-real-host + 0 NEW. n=6: 156 = 94 shipped + 59 realised + 3 sample-absent + 0 NEW.
    Load-bearing # (NEW forced-forbidden) = 0 at both sizes. Minimal set stays {K4,diamond,K_{2,3}}.
    (Matches R41's VF2+ball-realizability route by a cleaner forcing argument.)

F8c' (R41) -- independently re-verified + FOLDED INTO SPEC (was recommended but not yet in the file):
  - re-verified soundness: 40000 random induced subs each of Kneser/srg40 -> max #(eig > host-2nd-eig)
    = 1, 0 violations (exactly Cauchy interlacing: host has 1 eig > r => every induced sub has <=1).
  - ADDED to CLOUD_SPEC_SC.md: new filter row F8c' in the online-spectral block (between F8b' and the
    terminal F8); updated header note, NOTE-on-ORDER, and the §6 EXHAUSTION CALL. F8b'(bottom)+F8c'(top)
    +F7(mid-mult) now box the partial spectrum into (-4,3] save the Perron top, from k~34 onward.

EXHAUSTION CALL (R42): online Stage-A pruning is LARGELY EXHAUSTED. Every online-sound vein is closed
  with a verdict: F2-F4 (forbidden set COMPLETE through 6 vtx), F7 (mult-of-3 lower+upper), F8b' (PD/
  bottom), F8c' (lambda_2/top), moment-lower g (VOID, exact), det-7/corank (reduces to F7). The residual
  mid-tree gap (k in [38,46], slack 6-13) is provably NOT closable by any forced-moment/forced-spectral
  online predicate (it is lambda=1/mu=2 LOCAL, already enforced; interlacing-tight for anything spectral).
  Pipeline READY. NEXT ACTION: run the §3 thin vertical slice on ONE cloud node to MEASURE N_A / the
  failure-category histogram (the dominant remaining uncertainty); only then decide eigenspace-first vs
  scale. Do NOT spend more effort hunting online sound cuts. Scripts in scratchpad/: partA_exact_void.py,
  partA_srg99_exact.py, partB_supplement.py, partB_forbidden_census.py, partB_census_fast.py.
