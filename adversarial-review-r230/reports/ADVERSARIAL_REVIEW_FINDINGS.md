# Adversarial Review — R230 Nonexistence Certificate for srg(99,14,1,2)

Reviewed 2026-07-01. Reviewer: independent adversarial pass (Claude Code session).

## 1. Verdict

**Potential fatal flaw.**

The bundle's artifact layer is fully sound — verified here end-to-end, independently of the
bundle's own logs. But the mathematical reduction rests on one **unproven load-bearing
assumption**: the R204 forced-edge table. The bundle contains no proof of it, the
"clean-room" audit assumes it rather than deriving it, and ~19 CPU-hours of targeted
computation in this review could neither certify nor refute it. Until that lemma is proven
(or certified per-class), the bundle establishes only the conditional statement:

> No srg(99,14,1,2) exists **whose rooted far graph satisfies the R204 forced-edge table.**

The unconditional headline claim ("no srg(99,14,1,2) exists") is not established.

## 2. Confidence

- **Artifact correctness: HIGH (~0.95).** Every checkable artifact claim reproduced:
  all 24 CNFs rebuild byte-identical to manifest SHA-256s directly from the encoder;
  all 24 DRAT proofs verified `s VERIFIED` with a drat-trim built from upstream source
  with a local compiler; all audit JSONs reproduce exactly on rerun; orbit coverage exact.
- **Mathematical reduction (unconditional claim): MEDIUM-LOW (~0.5–0.6).** Everything
  downstream of the forced-edge table was verified sound (several parts re-derived by hand
  in this review). The table itself is plausibly true but is unproven in the bundle and
  resisted heavy computational certification.

## 3. Findings (by severity)

### F1 — POTENTIAL FATAL: forced-edge table asserted, never proven
- `source/root_cell_cpsat.py:55-64` (`forced_free_edge_value`) — the axiom everything uses.
- `source/root_cell_r204_cleanroom_symbolic_audit.py:63-71` (`forced_far_edge`) — the
  "clean-room" audit re-asserts the identical table; its 3360 symbolic equation checks prove
  compact-equation ≡ full-equation *given* the table, not the table itself. Its
  `permutationBlockCertificate` checks arithmetic (2 forced + 10 free, 40=40), not entailment.
- `reports/R204_HUMAN_CHECKABLE_REDUCTION.md` §"Forced Edges Inside and Between Fibers" —
  states the table with no derivation. (The label bijection above it IS correctly proven.)

Reviewer analysis: λ=1 implies every neighborhood induces a perfect matching; from this the
same-fiber C4 rules (forced edges for ov=1, forced nonedge for opposite corners) **follow**
from the intersecting-fiber rule. The single unproven kernel is:

> **Kernel lemma.** Two far vertices lying in fibers that share exactly one matched-pair
> index are never adjacent (both ov=1 and ov=0 flavors).

Local counting does not force this (violating configurations are locally count-consistent:
a far vertex has exactly one far neighbor per endpoint-mate family and two per outside
local — both sides of the flip satisfy all root/local λ/μ counts). If some hypothetical
graph violates the kernel, the 24 CNFs exclude it and their UNSAT results say nothing
about it — that would make the certificate vacuous as a nonexistence proof.

Computational attack (all inconclusive):
- Sparse/dense LP over degree + local-far + commutation equations: flip variables NOT
  linearly pinned (range [0,1] for all three representative pairs).
- CP-SAT (honest model, 294k constraints): 3 flips × 2h × 10 workers → UNKNOWN ×3.
- CaDiCaL 3.0.0 (honest CNF, 1,375,458 vars / 3,109,093 clauses): 3 flips × 4h → timeout ×3
  (~11 GB partial DRAT each).
- k=4 sanity (rook's graph): flips are INFEASIBLE (harness validates); k=6/k=8: honest model
  itself infeasible (vacuous for entailment testing).

**Required fix**: a mathematical proof of the kernel lemma, or checkable per-class flip
UNSAT certificates (one per orbit of the rooted relabeling group S2≀S7 on intersecting
pairs — likely 2 classes) plus the transitivity argument.

### F2 — CLARIFICATION: "clean-room" framing overstates what is machine-checked
`latex/conway_99_r230_nonexistence.tex:60-71` says the clean-room audit "independently
rebuilds the rooted labels and checks the symbolic reduction". True only downstream of the
assumed table. A reader will conclude the reduction is machine-verified end-to-end; it is not.
Same overstatement risk in `reports/FINAL_REPORT_R230_NONEXISTENCE.md` step 2.

### F3 — CLARIFICATION: bundled "audits" are marker/hash checks, not re-verification
`source/root_cell_r229_certificate_audit.py:99-104` greps copied logs for
`s UNSATISFIABLE` / `s VERIFIED`; `scripts/clean_room_replay.py` runs no solver or checker
(docstring admits this). Internally honest, but the replay's green result must not be read
as proof-checking. **Mitigated in this review**: all 24 DRATs re-verified with an
independently built drat-trim; all 24 CNFs rebuilt byte-identical.

### F4 — VERIFIED SOUND (no action): R220 orbit split
24 orbits; sizes {64×2,128×4,256×2,384×5,768×8,1536×3} sum to exactly 13824=24³;
abstract D8³⋊S3 action verified equal to genuine rooted relabelings
(`root_cell_triangle_orbit_audit.py` cross-check design is good); encoder
`TRIANGLE_REP_IDS` order-identical to audit representatives. Sound *given* F1's framework.

### F5 — VERIFIED SOUND (no action): R229 coset shadow
Relative-orientation identity checked exhaustively over 24×24; S4 partitions into 3 right
D8-cosets of size 8; SAT projection == CP-SAT projection == full-row projection for all 105
intersecting pairs; `intersecting_residual_rows` is a genuine necessary condition given
F1+permutation blocks. No over-pruning found beyond F1. The endpoint-fiber common-neighbor
terms for disjoint pairs ARE present (`root_cell_permutation_sat.py:496-500`) and verified
symbolically — that attack fails.

### F6 — POLISH
- Same-fiber pair equations and local-far equations are not encoded in the CNFs; omission is
  in the sound (relaxation) direction for UNSAT-based nonexistence, but worth documenting.
- Solver/checker binaries not pinned to commits; this review had to build both from upstream
  (Windows builds need `-Dgetc_unlocked=getc`/`-Dputc_unlocked=putc`).
- `verify_bundle_metadata.py` accepts UTF-16LE markers (Windows PowerShell logs) — fine, fragile.

## 4. Reproduction (this review)

All from `adversarial-review-r230/`, Python 3.12, ortools 9.15, pysat, scipy 1.18:

- `python scripts/verify_bundle_metadata.py` → ok=true, 24/24/24.
- `python scripts/clean_room_replay.py` → 3 steps ok.
- `python source/root_cell_r204_cleanroom_symbolic_audit.py` → ok, 3360 eqs, 0 mismatches
  (matches bundled JSON field-for-field).
- `python source/root_cell_triangle_orbit_audit.py` → 24 orbits, coverage 13824 exact.
- `python source/root_cell_intersecting_coset_sat_audit.py` → ok, 105 pairs, 0 orientation failures.
- Rebuild all 24 CNFs via `PermutationSat(card_encoding='seqcounter', triangle_rep_index=i,
  intersecting_coset_cuts=True)` → 24/24 SHA-256 match `artifacts/large_artifacts_manifest.csv`.
- drat-trim built from github.com/marijnheule/drat-trim (`gcc -O2 -Dgetc_unlocked=getc`) →
  24/24 proofs `s VERIFIED` (survivor core stats consistent with bundled logs, e.g. rep 00:
  3263 RAT lemmas both runs).
- Forced-edge flip probes: see F1 (CP-SAT UNKNOWN ×3 at 2h; CaDiCaL timeout ×3 at 4h; LP unpinned ×3).

Could not run: full clean-machine re-solve of the 24 certificate CNFs with proof logging
(pysat's in-process CaDiCaL segfaults on the survivor instances; the standalone CaDiCaL
re-solve was not attempted after the probe campaign consumed the compute budget).

## 5. Attack plan (next 3 checks before domain experts)

1. **Certify the kernel lemma** (decisive): mathematical proof, or per-orbit flip UNSAT
   certificates with DRAT + a transitivity proof for the S2≀S7 action on intersecting pairs.
   Budget days of CaDiCaL time per class, or find the human proof (likely known folklore for
   λ=1 SRGs — check literature: Wilbrink/Brouwer local analysis, Makhnev-style arguments).
2. **Independent re-solve of the 24 certificate CNFs** with a pinned CaDiCaL on a clean
   machine, regenerating DRATs and comparing verdicts (not hashes — proofs are
   nondeterministic) — closes the "solver bug" residual.
3. **Second triangle probe**: rerun the orbit machinery on a different fixed matching triple
   (e.g. fibers (0,2),(1,3),(4,6) after relabeling) and confirm 24 orbits again — a cheap
   independence check on the quotient step.
