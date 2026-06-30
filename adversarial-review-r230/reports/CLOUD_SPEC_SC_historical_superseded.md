# CLOUD-SPEC — star-complement s=-4 thin vertical slice (srg(99,14,1,2))
# DO NOT RUN LOCALLY. This is a specification for cloud / distributed compute.
# R230 FINAL UPDATE (2026-06-30): the cloud measurement route is now superseded
# as the decisive line by the rooted proof-SAT certificate.  The R43/R199/R218
# r=3 / 45-vertex Stage-A harness remains one-command runnable and validated as
# a fallback/cross-check, but the current proof bundle is:
#   python root_cell_r229_certificate_audit.py --json-out scratchpad\root_cell_r229_certificate_audit_current.json
# using
#   scratchpad\root_cell_triangle_rep_cloud_r229_seq_intercoset\r229_all24_ascii_drat_checked_summary.json
# which records all 24 R220 triangle representatives as UNSAT and independently
# drat-trim VERIFIED against the exact R229 CNFs.  Do not spend cloud budget on
# r=3 measurement unless the R230 certificate bundle is being independently
# challenged or reproduced.
# HARDENED at R35 (ordered filters + generation order + cost model), R36 (F5 over-prune FIX +
# eigenspace-first/degree-shaping verdicts), R37 (exact O(k^2) online F2/F3/F4 + complete minimal
# forbidden set {K4,diamond,K_{2,3}} + degree-stratified prune). Supersedes R31/R32/R34 drafts;
# folds every verified Stage-A predicate (R30-R37) into ONE ordered pipeline, plus generation strategy,
# calibrated cost model, thin-slice go/no-go, soundness gates, and the verified online Cauchy-interlacing
# prune (F7).
# All numeric constraints are calibrated on REAL eigenvalue-(-4) graphs (srg(21,10,3,6)=Kneser K(7,2),
# srg(40,12,2,4)) and the lambda=1 family (rook9=srg(9,4,1,2), BvLS243); framework reproduces 0 violations.
# CONSOLIDATION RE-VERIFY (this iter, independent rebuilds of Kneser K(7,2) and Sp(4,3)->srg(40,12,2,4)):
#   F1 (deg_H<=host_k), F7 (Cauchy interlacing), F8b (lam_min>-4), F8c (mult_r in {floor,floor+1}=
#   {10,11} for srg99) = 0/1500 over-prune on EACH real s=-4 graph; the UNSOUND deg_H<=host_k-1 rule
#   WOULD drop 4.2% (Kneser) / 2.1% (srg40) of REAL star complements — confirming F5's CAUTION.
#   R39 ADD: F8b' = hereditary-PD reject (lam_min(partial_k)>-4) at EVERY depth, and F7 upper-window
#   (mult_3<=66-k). Both SOUND: 0 false-reject over EXHAUSTIVE 32767 Kneser + 262143 srg40 induced
#   subgraphs (exact Sylvester minors) + ~35k sampled real-SC subs. F8b' has real mid-tree prune
#   (fires k>=40 dense, ~100% by k=46); the upper-window has 0 measured extra prune (leaf-tight only).
#   det-7/corank growth schedule: HONEST NO (reduces to F7; a corank schedule would over-prune srg40).
#   R41 ADD: F8c' = hereditary SECOND-EIGENVALUE cap (lambda_2(partial_k) <= 3) at EVERY depth k>=2:
#   srg99 has exactly ONE eig > 3, so by interlacing every induced subgraph has <=1 eig > 3 -> reject
#   any partial with >=2 eigs > 3.  SOUND (exact integer inertia, 0 false-reject over ~4.8M induced
#   subs: rook9 502 exh + Kneser 212418 + srg40 4.6M + BvLS 3840 + real-SC subs).  REAL mid-tree prune
#   at the TOP of the spectrum, fires k~34-42 (BELOW F8b's dense range and F7's k>=46 floor) -- the
#   first online cut to bite the spectral TOP; F8b'(bottom)+F8c'(top) box the partial spectrum into
#   (-4,3] save one Perron eig.  THE R41 ONLINE WIN (now shipped to the §1 pipeline).
#   R40 ADD (this iter, see §6): (a) forced-moment INTERIOR mult_3 LOWER bound g(k,e,t) -- HONEST NO,
#   structurally VOID (g=0 identically; proven grid-free with EXACT rational measures at the srg99
#   params over the whole reachable (k,e,t) box, k in [38,46]; r=3 is a single interior point so a
#   0-mass-at-3 measure always exists -- LP-duality dual of the known m3-from-ABOVE bound).  (b) NEW
#   5/6-vtx forbidden subgraph beyond {K4,diamond,K_{2,3}} -- HONEST NONE (the mu/lambda adjacency
#   forcing == "contains an induced diamond", 0 mismatch over all graphs n<=6; census 0 NEW at n=5,6).
#   CALL: online Stage-A pruning is LARGELY EXHAUSTED; residual mid-tree N_A is interlacing-tight /
#   structural.  Pipeline is READY -> run the §3 thin slice to MEASURE N_A; next lever is eigenspace-
#   first (structural), not a new online sound cut.
# Verified live: FINAL_GATE.py = ALL GATES GREEN (W0 64.5x, m3 cut e<=363, interlacing floor=8, margin=1).
# R43 ADD (§7, NEW): the r=3 (45-VERTEX) star-complement ALTERNATIVE — assessed + validated this iter.
#   Eigenvalue 3 has mult 54 => its star complement is 45 vtx (vs 55 for s=-4) => Stage-A tree depth 45
#   vs 55 => ~b^-10 (3-10 ORDERS) fewer nodes.  Local block F1-F6 IDENTICAL (eigenvalue-agnostic); top
#   gate G-b == F8c' IDENTICAL; bottom gate weakens PD->PSD but the PD/PSD gap is LEAF-only (0% mid-tree,
#   measured on rook9+Kneser) so costs ~0; lost F7 lived ABOVE the 45 ceiling so costs nothing.  CRS for
#   r=3 (A_X=3I+B^T(C-3I)^-1 B) verified EXACT 150/150 on real r=3 graph T(7)=srg(21,10,5,4); G-a/G-b
#   0 false-reject on 6842 real induced subgraphs.  RECOMMENDATION: run r=3 as PRIMARY Stage-A (biggest
#   N_A win available, > any R35-R42 online cut); keep s=-4 as the calibrated fallback/cross-check.  See §7.

# R186 ADD: current r=3 Stage-A includes three proof-checked completion closures:
#   R184 pair lower-closure, R185 neighbourhood matching-completion, and R186 outside-degree moment.
#   R186 double-counts outside degrees to a partial P:
#     S=sum_{p in P}(14-deg_P(p)), D=sum_{a<b in P}(tau-common_P(a,b));
#   D must fit the min/max possible sum binom(s_x,2) over 99-|P| outside vertices with total S and
#   cap min(14,|P|).  Validated on rook9 exhaustive 0/512, T(7) sampled 0/1000, BvLS sampled 0/500,
#   synthetic control fires, and `s3_slice_harness.py --gate` remains ALL GREEN.  Exact regenerated
#   prefix: R185 N10=42425 -> R186 N10=42423.  Old R90 d11 direct scans show R185 29, R186 27,
#   overlap 0, either 56; available d12 files show 141/1174677 direct R186 violations.  IMPORTANT:
#   R186 is sound as a prefix predicate but not monotone as a later-depth row statistic, so exact
#   refreshed N11 must be rerun from `scratchpad/r3_frontier_d10_r186_outside_moment.jsonl` using
#   `s3_cloud_r3_d11_r186.py`; do not quote the old-R90 direct union count as exact.
# R187 ADD: exact outside-degree histogram feasibility was tested as a possible strengthening of R186.
#   It is sound and stricter in abstract, but measured no extra rows over R186 on current evidence:
#   R186 d10 0/42423, pre-R186 d10 2/42425 with extra 0, old R90 d11 27/463636 with extra 0,
#   known d12 141/1174677 with extra 0; rook9/T(7)/BvLS no-overprune checks passed.  Do NOT add this
#   DP to the hot path for the current cloud run.  Reconsider only if deeper frontiers land in exact
#   histogram gaps after passing the R186 interval test.
# R188 ADD: actual R186 d10->d11 pilot shards 0..1/64 completed through `s3_cloud_r3_d11_r186.py`.
#   Loaded 1326/42423 parents (3.1257%), produced 14832 depth-11 children, diagnostic scaled
#   N11~474523.3, no budget/time/sample flags, and both fresh shard frontiers scan clean under R185/R186.
#   This proves the one-command path writes compatible stats/frontiers.  It is diagnostic only; exact
#   R186 N11 still requires all 64 shards and strict aggregation without `--allow-incomplete`.
# R189 ADD: near-full subset outside-degree moment closure is now in Stage-A.  It applies the R186
#   double-count to U=P\{u} and U=P\{u,v}, with the outside set still V\P.  Soundness controls:
#   synthetic R186-clean row fires; rook9 exhaustive 0/512, T(7) sampled 0/1000, BvLS sampled 0/500;
#   `s3_slice_harness.py --gate` remains ALL GREEN.  Measured extra hits beyond global R186:
#   clean R186 d10 +1 row -> exact regenerated N10=42422; old R90 d11 +10 direct rows; known d12
#   +87 direct rows.  Current primary d10->d11 refresh is `s3_cloud_r3_d11_r189.py` from
#   `scratchpad/r3_frontier_d10_r189_nearfull_subset_moment.jsonl`.  Old d11/d12 direct scans remain
#   diagnostic only; exact R189 N11 requires all 64 d10->d11 shards under the R189 prefix.
# R190 ADD: actual R189 d10->d11 shard 0/64 completed.  Loaded 663/42422 parents, produced 7336
#   depth-11 children, diagnostic scaled N11~469393.4, no budget/time/sample flags, fresh frontier
#   scans clean under R189/R186.  The comparable R188/R186 shard-0 pilot produced 7403 children, so
#   R189 removes 67 children on this shard.  Still diagnostic; exact N11 requires all 64 shards.
# R191 ADD: R189 shards 0..1/64 aggregate completed.  Loaded 1326/42422 parents, produced 14824
#   depth-11 children, diagnostic scaled N11~474256.2, no budget/time/sample flags; shard-1 frontier
#   scans clean under R189/R186.  R188/R186 two-shard diagnostic was 14832 children, scaled
#   N11~474523.3.  This comparison is sizing-only because R189's removed d10 row shifts modulo shard
#   membership after that row.  Exact R189 N11 still requires all 64 shards.
# R192 ADD: tested remove<=3 version of the near-full subset moment check.  It is sound but no-gain:
#   clean R189 d10 0/42422, old R90 d11 14/463636 exactly same as remove<=2, and a 200k-row d12 sample
#   had remove<=2=31, remove<=3=31, extra=0.  Probe supports `--max-remove 3`, but the hot path should
#   stay at R189 remove<=2 unless deeper refreshed frontiers show remove-3-only rows.
# R193 ADD: tested matching-aware adjacent-edge split of outside pair demand: feasibility of `(S,D,A)`
#   where `A` is residual adjacent-edge demand and each outside vertex can contribute at most
#   floor(s/2) adjacent pairs among s placed neighbours.  No-gain: per-vertex incident bound 0 hits on
#   clean d10/old d11; global `(S,D,A)` clean R189 d10 0/42422 and old R90 d11 only the 27 global R186
#   rows; near-full `(S,D,A)` clean R189 d10 0/42422.  Do not add this DP to the hot path.
# R194 ADD: tested exact outside-column incidence shadow MILP.  For each unplaced vertex x, its support
#   `B_x=N(x) cap P` must realize every residual placed-vertex degree and placed-pair common-neighbour
#   demand exactly; lambda=1 supports also must be matching-completable.  Soundness controls passed:
#   rook9 exhaustive 0/512, T(7) sampled 0/200 under generic SRG rules, BvLS sampled 0/100, with actual
#   outside-column reconstruction checked before MILP feasibility.  Measurements: clean R189 d10
#   0/42422 infeasible and 0 limit rows; R189 d11 pilot shard samples 0/10000; old R90 d11 first 5000
#   had 3 infeasible rows all already R185; known d12 sample first 8000 had 2 infeasible rows already
#   R186/R189, with the 2 short-limit rows rerun feasible under a longer cap.  Verdict: useful
#   diagnostic, no current prune, too expensive for `PartialGraph.can_add()`.  Do not add to hot path
#   unless deeper refreshed frontiers show extra failures or a cheap Farkas-style certificate is derived.
# R195 ADD: actual R189 d10->d11 shards 2..3/64 completed.  Shard2 `663 -> 7351`, shard3 `663 -> 7394`;
#   together `1326 -> 14745`, no budget/time/sample flags, fresh frontier scans clean under R184/R185/
#   R186/R189.  Shards 0..3 now cover `2652/42422` d10 parents (6.2515%) and produce `29569` d11
#   children; diagnostic scaled `N11 ~= 472992.5`.  Still diagnostic only; exact R189 N11 requires all
#   64 shards and strict aggregation.  Next unmeasured foreground range is `4-5`.
# R196 ADD: actual R189 d10->d11 shards 4..5/64 completed.  Shard4 `663 -> 7672`, shard5 `663 -> 7016`;
#   together `1326 -> 14688`, no budget/time/sample flags, fresh frontier scans clean under R184/R185/
#   R186/R189.  Shards 0..5 now cover `3978/42422` d10 parents (9.3772%) and produce `44257` d11
#   children; diagnostic scaled `N11 ~= 471963.4`.  Still diagnostic only; exact R189 N11 requires all
#   64 shards and strict aggregation.  Next unmeasured foreground range is `6-7`.
# R197 ADD: actual R189 d10->d11 shards 6..7/64 completed.  Shard6 `663 -> 7489`, shard7 `663 -> 7648`;
#   together `1326 -> 15137`, no budget/time/sample flags, fresh frontier scans clean under R184/R185/
#   R186/R189.  Shards 0..7 now cover `5304/42422` d10 parents (12.5029%) and produce `59394` d11
#   children; diagnostic scaled `N11 ~= 475040.0`.  Still diagnostic only; exact R189 N11 requires all
#   64 shards and strict aggregation.  Next unmeasured foreground range is `8-9`.
# R198 ADD: actual R189 d10->d11 shards 8..9/64 completed.  Shard8 `663 -> 6609`, shard9 `663 -> 7234`;
#   together `1326 -> 13843`, no budget/time/sample flags, fresh frontier scans clean under R184/R185/
#   R186/R189.  Shards 0..9 now cover `6630/42422` d10 parents (15.6287%) and produce `73237` d11
#   children; diagnostic scaled `N11 ~= 468606.3`.  Still diagnostic only; exact R189 N11 requires all
#   64 shards and strict aggregation.  Next unmeasured foreground range is `10-11`.
# R199 ADD: primary r=3 / 45-vtx Stage-A cloud measurement now has a self-checking one-command wrapper:
#   `s3_cloud_r3_stagea.py`. It runs `s3_slice_harness.py --gate` first by default, then launches the
#   unseeded depth-45 measurement with stats/manifests; it intentionally never passes `--seed-triangle`.
#   Live validation: py_compile passed; `s3_slice_harness.py --gate` ALL GREEN (rook9 all 362880 orders,
#   rook9 spectral 0/511, T(7) exact CRS closure, T(7) Stage-A false rejects 0/5242); wrapper root smoke
#   exact `N1..N7=1,2,4,9,21,62,208`; wrapper two-shard continuation from the smoke d7 frontier
#   recombined exactly to `N8=916`. The deep spectral-collapse curve remains unmeasured; this is a
#   readiness repair, not a construction/nonexistence result.
# R200 ADD: integrated generic replay of the lambda=1,mu=2 predicate bundle against real witnesses:
#   `s3_integrated_predicate_replay.py` replays the same formulas with each witness's true parameters
#   rather than the srg99 constants. Live run passed: rook9 exhaustive `362880/362880` orders accepted;
#   BvLS(243) sampled induced-order replay `200` subsets/orders of size 0..30 had 0 violations; BvLS
#   sampled triangle-split identities `100/100` had 0 violations. Predicates covered together:
#   degree caps, lambda/mu caps, pair lower-closure, neighbourhood matching-completion, outside-degree
#   moment, R189 near-full subset moment remove<=2, and triangle counter/split identities.
# R201 ADD: actual R189 d10->d11 shards 10..11/64 completed. Shard10 `663 -> 7320`, shard11
#   `663 -> 7631`; together `1326 -> 14951`, no budget/time/sample flags, fresh frontier scans clean
#   under R184/R185/R186/R189. Shards 0..11 now cover `7956/42422` d10 parents (18.7544%) and produce
#   `88188` d11 children; diagnostic scaled `N11 ~= 470225.2`. Still diagnostic only; exact R189 N11
#   requires all 64 shards and strict aggregation. Next unmeasured foreground range is `12-13`.
# R202 ROOTED ADD: R8's forced/free `Gamma_2(root)` split has been ported into the R141 rooted CP-SAT
#   surface as `root_cell_cpsat.py --free-edge-vars` and validated by `root_cell_forced_free.py`.
#   For k=14 it replaces all `C(84,2)=3486` far-edge variables with `1680` genuine free-edge variables,
#   plus constants for `84` forced C4 edges and `1722` forced nonedges.  The full CP-SAT proto with
#   commutation shrinks from `289338` vars / `294084` constraints to `67201` vars / `73752` constraints.
#   Real-witness checks passed on rook9 all roots and BvLS roots 0,1,2; reduced k=4 reconstructs rook9.
#   Bounded k=14 CP-SAT remains UNKNOWN (60s: commutation branches 304020; no-commute 492979), so this is
#   an exact encoding reduction for a future SAT/SMS/free-graph model, not a nonexistence result.
# R203 ADD: actual R189 d10->d11 shards 12..13/64 completed. Shard12 `663 -> 6819`, shard13
#   `663 -> 7184`; together `1326 -> 14003`, no budget/time/sample flags, fresh frontier scans clean
#   under R184/R185/R186/R189. Shards 0..13 now cover `9282/42422` d10 parents (21.8802%) and produce
#   `102191` d11 children; diagnostic scaled `N11 ~= 467048.8`. Still diagnostic only; exact R189 N11
#   requires all 64 shards and strict aggregation. Next unmeasured foreground range is `14-15`.
# R204 ROOTED ADD: the R202 free-edge surface has a stronger k=14 fiber-block reduction.  In each
#   rooted far-cell fiber the four free-neighbour sets are pairwise disjoint; since `4*(14-4)=40`
#   equals the ten disjoint fibers times four vertices, every disjoint `4x4` fiber block is a
#   permutation matrix.  New scripts `root_cell_fiber_permutation.py`,
#   `root_cell_permutation_formula_audit.py`, and `root_cell_permutation_csp.py` validate and encode
#   this as a 105-block `S4` permutation CSP.  Real-witness checks passed for the general disjointness
#   lemma on rook9/BvLS; the k=14 covering step is parameter-specific.  Formula audit checked 30 random
#   permutation assignments / 104580 far pairs against direct common-neighbour counts.  Generic CP-SAT
#   remains UNKNOWN (permutation CSP: 840 int vars, 23520 bool vars, 50715 constraints, 60s UNKNOWN).
# R205 ROOTED SAT ADD: the R204 permutation CSP now has a bounded one-command CNF thin-slice:
#   `python .\root_cell_permutation_sat.py --time-cap 60 --solver cadical195 --json-out .\scratchpad\root_cell_permutation_sat_cadical_r205.json --solution-out .\scratchpad\root_cell_permutation_sat_solution_r205.json`.
#   Encoding size is 137760 vars / 384720 clauses with 1680 permutation block vars, 840 row/col
#   exactly-one equations, 15120 equality terms, 60480 AND terms, and 3360 pair equations.  Cadical195
#   60s result: UNKNOWN (440040 conflicts, 1285475 decisions, 548094919 propagations).  SAT reconstructs
#   and verifies the full graph before writing a solution; UNSAT is NOT proof-grade until proof logging
#   and independent checking are added.  A Glucose attempt exceeded the outer command budget and is not
#   evidence.
#   Treat this as the next exact structural encoding target, not as SAT/UNSAT evidence.
# R206 ROOTED SAT SPLIT ADD: `root_cell_permutation_sat.py` now supports the exhaustive two-case target
#   block representative split `--block-rep square|nonsquare`.  Finite audit
#   `root_cell_block_rep_audit.py` enumerates all 24 S4 block permutations under legal left/right D8
#   square actions and verifies exactly two double cosets: square rep (0,1,2,3), size 8; nonsquare rep
#   (0,1,3,2), size 16; covered_permutations=24.  Each slice adds four unit clauses (137760 vars /
#   384724 clauses).  Cadical195 60s results are both UNKNOWN: square 440053 conflicts / 1021023
#   decisions; nonsquare 450026 conflicts / 1016005 decisions.  This is a sound exhaustive CASE SPLIT
#   only when BOTH representatives are run; a single representative would over-prune.  Proof-grade
#   nonexistence would require independent UNSAT certificates for both slices.
# R207 SAT TOOLCHAIN ADD: local proof-grade SAT is NOT available.  `root_cell_sat_toolchain_audit.py`
#   found no standalone cadical/kissat/drat-trim/gratgen/lrat-check on PATH.  PySAT cadical153/195/300
#   support bounded solving and solve a toy UNSAT without proof, but proof-enabled child probes return
#   empty proof lists and abnormal child return code 3221226505.  Cadical300 R206 60s slices are both
#   UNKNOWN and worse than Cadical195 (square 480036 conflicts / 1088797 decisions; nonsquare 470041 /
#   1083032).  Cadical153 square 15s probe is UNKNOWN with no clear improvement.  Keep Cadical195 as
#   local default; proof-grade R206 needs cloud/toolchain support for proof logging + independent DRAT/LRAT
#   checking.
# R208 ENCODING ADD: `root_cell_permutation_sat.py --card-encoding direct` replaces seqcounter auxiliaries
#   for the small exactly-k equations (largest n=8).  Exhaustive translator audit
#   `root_cell_card_encoding_audit.py --max-n 8` passed: all n<=8, all bounds, all assignments,
#   assignments_checked=4097.  Per R206 representative slice, CNF changes from 137760 vars / 384724
#   clauses to 77280 vars / 405724 clauses.  Cadical195 60s remains UNKNOWN but improves locally:
#   square direct 390037 conflicts / 857171 decisions; nonsquare direct 410040 conflicts / 1003204
#   decisions.  Preferred cloud commands are now:
#     python .\root_cell_permutation_sat.py --time-cap <T> --solver cadical195 --block-rep square --card-encoding direct --json-out <square.json> --solution-out <square_solution.json>
#     python .\root_cell_permutation_sat.py --time-cap <T> --solver cadical195 --block-rep nonsquare --card-encoding direct --json-out <nonsquare.json> --solution-out <nonsquare_solution.json>
#   R219 proof-stack export commands:
#     python .\root_cell_permutation_sat.py --block-rep square --card-encoding direct --cnf-out square.cnf --no-solve --json-out square_export.json
#     python .\root_cell_permutation_sat.py --block-rep nonsquare --card-encoding direct --cnf-out nonsquare.cnf --no-solve --json-out nonsquare_export.json
# R209 CP-SAT TABLE ADD: disjoint-fiber common-neighbour equations have an exact residual-table
#   formulation over one direct block and three relative permutations.  Audit
#   `root_cell_disjoint_table_audit.py` checked all 24*24^3 combinations: ok=true, 456 table rows
#   (square direct blocks 9 triples each; nonsquare 24 each).  `root_cell_permutation_csp.py
#   --disjoint-tables` adds 210 permutation-id vars, 315 relative-permutation vars, and 630 table
#   constraints; unsplit 60s CP-SAT is still UNKNOWN but improves sharply vs R204 repaired CSP:
#   34799 conflicts / 756900 branches vs 187506 / 1299396.  Representative CP slices are also UNKNOWN
#   and did not beat the unsplit table model locally.  Repro command:
#     python .\root_cell_permutation_csp.py --time-cap <T> --workers <W> --disjoint-tables --json-out <tables.json> --out <tables_solution.json>
# R210 INTERSECTING TABLE CAUTION: the analogous intersecting-fiber relation is exact but too heavy as
#   a CP-SAT extensional table.  Audit: arity 6, 35280 rows per target, invalid ambient space 24^6,
#   ok=true.  Local `--intersecting-tables` probes are UNKNOWN with 0 conflicts / 0 branches after
#   38.6s (10s cap) and 63.0s (60s cap), i.e. budget is spent in table/presolve handling.  DO NOT put
#   `--intersecting-tables` in the hot path unless decomposed into smaller constraints or moved to a
#   solver suited to large table constraints.
# R211 ADD: actual R189 d10->d11 shards 14..15/64 completed. Shard14 `663 -> 7512`, shard15
#   `663 -> 7290`; together `1326 -> 14802`, no budget/time/sample flags, fresh frontier scans clean
#   under R184/R185/R186/R189. Shards 0..15 now cover `10608/42422` d10 parents (25.0059%) and produce
#   `116993` d11 children; diagnostic scaled `N11 ~= 467861.7`. Still diagnostic only; exact R189 N11
#   requires all 64 shards and strict aggregation. Next unmeasured foreground range is `16-17`.
# R212 ADD: actual R189 d10->d11 shards 16..17/64 completed. Shard16 `663 -> 6574`, shard17
#   `663 -> 6227`; together `1326 -> 12801`, no budget/time/sample flags, fresh frontier scans clean
#   under R184/R185/R186/R189. Shards 0..17 now cover `11934/42422` d10 parents (28.1316%) and produce
#   `129794` d11 children; diagnostic scaled `N11 ~= 461381.0`. Still diagnostic only; exact R189 N11
#   requires all 64 shards and strict aggregation. Next unmeasured foreground range is `18-19`.
# R213 ADD: Lou-Murin/Wilbrink order-9 motif audited.  In the specific `(99,14,1,2)` parameter set,
#   an induced `srg(9,4,1,2)-e` is forbidden: any subgraph copy forces the missing edge and induces the
#   3x3 rook graph.  Audit artifact `lou_murin_hminus_audit.py` recognizes the motif exactly and shows
#   it is NOT already killed by the current local/spectral gates.  Current measured hit rates are low:
#   depth9 `1/5311`, depth10 `8/42422`, R189 depth11 shards 0..17 `12/129794`.  Treat as a safe offline
#   audit / optional bounded shallow filter, not a hot-path all-9-subsets scan unless a cheap incremental
#   detector is derived.  The R43 r=3 / 45-vertex Stage-A route remains the primary cloud route.
# R214 ROOTED ADD: R209's disjoint residual table has a sound right-coset projection modulo the square
#   subgroup `D8<=S4`.  `root_cell_coset_csp.py` proves the finite projection: square direct block =>
#   all 3 common relative permutations square; nonsquare direct block => 0 or 2 square relatives.  The
#   standalone 3-colour macro CSP is SAT (and all three fixed-coset slices SAT), so no obstruction.
#   `root_cell_permutation_csp.py --coset-projection` is optional.  Alone it worsens R204 locally
#   (`319254` conflicts / `1519082` branches at 60s); with `--disjoint-tables` it remains UNKNOWN and
#   shifts R209 from `34799` conflicts / `756900` branches to `50442` conflicts / `617908` branches.
#   Use only as an experimental CP-SAT propagation layer; do not replace R209 or claim a verdict.
# R215 ROOTED ADD: the six-class refinement `(right D8 coset, parity)` was tested in
#   `root_cell_class_projection_csp.py`.  The projected arity-7 table has `10368/279936` allowed tuples,
#   but the unsliced projection is constructively SAT by assigning every directed block to class 0
#   (even square coset).  A nonzero fixed-class CP-SAT slice is table/presolve-heavy and UNKNOWN at 30s.
#   Verdict: coarse class projections alone are too weak; future rooted work must keep actual relative
#   permutations or derive true cycle/holonomy equations.
# R216 READINESS REFRESH: `READINESS_R216.md` is the current honest go/no-go note after R213-R215.
#   Compile check passed for the new audit/rooted scripts.  The r=3 wrapper dry-run emitted exactly the
#   intended one-command sequence (`s3_slice_harness.py --gate`, then unseeded `--slice`) and wrote
#   `scratchpad\r3_stagea_dry_r216_manifest.json`.  A bounded no-gate smoke to depth 7 reproduced
#   `N1..N7=1,2,4,9,21,62,208`, `expanded=307`, all prune counters 0, no budget/time/sample flags,
#   wall 0.53s.  CAVEAT: a fresh full `s3_slice_harness.py --gate` exceeded the local 124s command cap;
#   the escaped gate process was identified and stopped.  Therefore R216 does NOT supersede the R199/R200
#   full green gate transcript.  At R216 time the instruction was to rerun the full gate with a longer
#   cap before any paid/decisive cloud run; R218 below clears that caveat with a fresh 238.5s full local
#   gate.  Verdict:
#   runnable experiment, not proof; deep spectral-collapse curve and proof-grade rooted SAT/SMS remain
#   the decisive unknowns.
# R217 ROOTED ADD: a true matching-triangle relative-permutation holonomy parity law was audited:
#   for three pairwise-disjoint rooted fibers A,B,C,
#   `parity(q_AB^C)+parity(q_BC^A)+parity(q_AC^B)=0 mod 2`.  Finite enumeration over `S4^3`
#   checked all `24^3=13824` direct-block triples and proved the admissible relative triples are exactly
#   the `6912` even-parity triples; the K7-edge fiber geometry has `105` such matching triples.
#   Implemented as `root_cell_permutation_csp.py --matching-holonomy` (requires `--disjoint-tables`) and
#   audited by `root_cell_matching_holonomy_audit.py`.  Local CP-SAT at 60s remains UNKNOWN:
#   `34143` conflicts / `894736` branches versus R209 disjoint tables alone `34799` / `756900`.
#   Verdict: exact proof note and optional diagnostic flag, but not a default cloud path; parity-only
#   holonomy is now closed unless a later solver profile specifically benefits from it.
# R218 READINESS ADD: fresh full `python s3_slice_harness.py --gate` completed locally in 238.5s and ended
#   `SOUNDNESS GATE: ALL GREEN`.  Checks included rook9 all `9! = 362880` vertex orders, rook9 spectral
#   false rejects `0/511`, triangle-split identity on `512` subsets, exact T(7) r=3 reconstruction with
#   `det(A_H'-3I)=390625`, blind recovery of all 6 true star columns among `735` diagonal-valid columns,
#   cadical195 size-6 clique closure, and T(7) Stage-A false rejects `G-a=0`, `G-b=0` over `5242` real
#   induced subgraphs.  The primary r=3 cloud command is now backed by a fresh full gate transcript;
#   rerun the gate only if code/dependencies/environment change before launch, and archive the transcript
#   with the cloud artifacts.
# R219 SAT-PROOF ADD: `root_cell_permutation_sat.py` now supports `--cnf-out` and `--no-solve`, so the
#   R206/R208 representative rooted SAT slices can be exported as fixed DIMACS formulas for an external
#   proof-logging stack.  Generated direct-cardinality CNFs:
#     square    `scratchpad\root_cell_permutation_sat_direct_square_r219.cnf`
#       vars/clauses `77280/405724`, bytes `7714533`,
#       sha256 `d244fc73c930f3c679c08836001985c23a2d01b0b1c73a38bee61e975478fda0`
#     nonsquare `scratchpad\root_cell_permutation_sat_direct_nonsquare_r219.cnf`
#       vars/clauses `77280/405724`, bytes `7714533`,
#       sha256 `25891300867286ee445506491cd84688836f6c675eed691211e8e4a9d1f363b0`
#   PySAT read-back verified both DIMACS headers/counts match encoder stats.  Proof-grade acceptance:
#   solve BOTH CNFs, emit solver proof artifacts for UNSAT claims, independently check them against these
#   exact hashes, and reconstruct+verify a full SRG for any SAT model.  This is cloud readiness, not a
#   result.
# R220 SAT-PROOF ADD: R219's two one-block CNFs are superseded by a stronger matching-triangle
#   representative split.  Fix rooted fibers `(0,1),(2,3),(4,5)` and split on the three direct S4
#   blocks between them.  `root_cell_triangle_orbit_audit.py` proves that the actual rooted-label
#   stabilizer orbit table equals the abstract `D8^3 semidirect S3` table: `24^3=13824` ambient
#   triples collapse to 24 orbit representatives, histogram `{64:2,128:4,256:2,384:5,768:8,1536:3}`.
#   `root_cell_permutation_sat.py --triangle-rep-index <i> --card-encoding direct` fixes one
#   representative by 12 unit clauses; each such CNF has `77280` vars / `405732` clauses.
#   Independent BCP (`root_cell_triangle_rep_unit_audit.py`) kills 16 reps at level 0:
#     killed `[1,3,4,5,6,9,11,12,13,14,16,17,18,19,20,23]`
#     live   `[0,2,7,8,10,15,21,22]`
#   The killed set exactly matches the local 5s Cadical195 zero-decision UNSAT smoke set.  One-command
#   export for the current proof suite:
#     python .\root_cell_triangle_rep_cloud_suite.py --out-dir scratchpad\root_cell_triangle_rep_cloud_r220 --card-encoding direct
#   This rebuilds all 24 reps, reruns BCP, writes only the 8 live DIMACS files, and emits
#   `scratchpad\root_cell_triangle_rep_cloud_r220\manifest.json`
#   with hash `FA61BBF30CC7FEC972E909D3224B8DCD814A8E875BAAEE63629C56E60A87EBF6`.
#   Live survivor CNF hashes:
#     rep00 `(0,0,0)`  `6c3c01cf908defc4571ff9fb9f15b6610f332312832b6b0ebb18575db956176d`
#     rep02 `(0,0,2)`  `2eb94fb0029c73679b40d83c47601d1b2e9eeb91562ed805d856ffb9bfd0ed58`
#     rep07 `(0,0,23)` `26f0bbe7f1431aacabfa440b4aa9fc99167e976a4169b52ad8c9c2dd65e0bdc4`
#     rep08 `(0,1,1)`  `35b11a3b8a2d9d70862b5f3640f5d7be28e2f90b71a6588e4d768923a01b6d7a`
#     rep10 `(0,1,4)`  `0c192e6615fd5d499c4d87821a4ecef9b7ff1f0037fc0d17b227f2d47927e6ad`
#     rep15 `(0,1,17)` `180da713dddebb4875281174c55148e22f2e826f3ed5e5ca7d3e4e7ba47fcc77`
#     rep21 `(1,1,17)` `28bfe0f0b9eac7895e4a8224a9a04de28b19d397c8d849655853b80098d4d0cb`
#     rep22 `(1,4,5)`  `baf9a7305a2587766e97c71d6791472eda0b9ca7ce6e8183f41c255fa2c22557`
#   Proof-grade nonexistence from this SAT route now requires proof-logging UNSAT and independent proof
#   checking for these 8 live CNFs, plus the R220 orbit/BCP audits.  SAT still requires full graph
#   reconstruction.  Do not mix this proof-SAT track with the R43/R199/R218 r=3 Stage-A measurement:
#   r=3 remains the primary search-cost cloud route; R220 is the current rooted proof-SAT route.
# R221 ROOTED CAUTION: a residual one-block split after R220 was probed exactly with
#   `root_cell_triangle_next_block_probe.py`.  Residual group sizes matched the R220 orbit-stabilizer
#   check (`96,48,96,16,8,16,24,48` for reps `0,2,7,8,10,15,21,22`).  However, a second fixed block
#   gives no broad unit-propagation kill: reps `0,2,7,15,21` kill `0/24` assignment weight, and reps
#   `8,10,22` kill only `8/24` while increasing proof case count.  Do not make residual one-block
#   subcases the default proof route unless a concrete proof-solver benchmark justifies a targeted split.
# R222 SAT-PROOF ADD: globalized R220 into full matching-triangle forbidden-triple cuts.  The eight
#   R220 survivor orbits contain exactly `2176` allowed direct triples; the other `11648` triples are
#   forbidden on every matching of three pairwise-disjoint rooted fibers.  With 105 rooted matching
#   triples, `root_cell_permutation_sat.py --matching-triangle-cuts` adds `1223040` length-12 clauses
#   and no variables.  Audit:
#     python .\root_cell_matching_triangle_cut_audit.py --json-out scratchpad\root_cell_matching_triangle_cut_audit_r222.json
#   returned `ok=true`, `mismatch_count=0`, `allowed_triples=2176`, `forbidden_triples=11648`.
#   One build-only rep-0 direct cut CNF measured `77280` vars / `1628772` clauses in `8.98s`.
#   The suite exporter supports the cloud flag:
#     python .\root_cell_triangle_rep_cloud_suite.py --out-dir <DIR> --card-encoding direct --matching-triangle-cuts
#   Use `--no-export` for a sanity build without writing the large DIMACS files; local no-export over
#   all 24 reps took `231.0s` and preserved the same 16 killed / 8 survivor partition.  Local 5s
#   Cadical195 smoke on the 8 survivors remained UNKNOWN but improved to roughly `37k-62k` decisions
#   and `29M-42M` propagations, versus lean R220's `82k-122k` decisions and `58M-73M` propagations.
#   Tradeoff: lean R220 survivor CNF `77280/405732`; cut-heavy R222 survivor CNF `77280/1628772`.
#   Benchmark lean vs cut-heavy on the actual proof solver before committing large cloud proof runs.
# R223 CP-SAT ADD: the R222 allowed-triple relation is also available compactly in
#   `root_cell_permutation_csp.py --disjoint-tables --matching-triangle-tables`.  It adds 105
#   allowed-assignment tables over existing permutation-id variables, not the 1.2M SAT clauses.
#   Current 60s/8-worker measurement:
#     baseline `--disjoint-tables`: `40018` conflicts / `886008` branches;
#     `--matching-triangle-tables`: `30041` conflicts / `562026` branches;
#     plus old `--matching-holonomy`: `34357` conflicts / `615402` branches.
#   Verdict: use `--matching-triangle-tables` for CP-SAT diagnostics; leave parity holonomy off by
#   default once the full table is present.  Still UNKNOWN, not proof evidence.
# R224 ROOTED NEGATIVE: the pid-only global R222 triangle-table quotient was tested in
#   `root_cell_global_triangle_table_probe.py`.  It keeps the 105 direct block-ID variables and the 105
#   R222 matching-triangle tables, fixing each of the 24 R220 representatives in turn.  Result: exactly
#   the 16 already unit-dead reps are INFEASIBLE, and all 8 R220 survivors are globally feasible in
#   this quotient.  Do not expect the R222 table alone to prune further without permutation-entry or
#   intersecting-fiber structure.
# R225 CP-SAT ADD: R210's heavy arity-6 intersecting-fiber table has a useful decomposed substitute:
#   `root_cell_permutation_csp.py --intersecting-pair-tables`.  Audit
#   `root_cell_intersecting_pair_projection_audit.py` proves that all 15 binary projections of the
#   full 35280-row table have exactly 356 allowed pairs out of 576 and match the full table's
#   projections.  Current 60s/8-worker measurements:
#     baseline `--disjoint-tables`: `40018` conflicts / `886008` branches;
#     `--matching-triangle-tables`: `30041` / `562026`;
#     `--intersecting-pair-tables`: `12403` / `466352`;
#     both tables: `14788` / `400367`;
#     both + parity holonomy: `12223` / `445293`.
#   New rooted CP-SAT diagnostic default:
#     python .\root_cell_permutation_csp.py --time-cap <T> --workers <W> --disjoint-tables --matching-triangle-tables --intersecting-pair-tables ...
#   Still UNKNOWN, but it is the strongest compact rooted propagation profile so far.  Keep full
#   `--intersecting-tables` out of the hot path; keep parity holonomy off by default.
# R226 CP-SAT CAUTION: arity-3 projections of the R210 intersecting table are exact but locally too
#   heavy as CP-SAT tables.  Audit: 20 ternary projections, each 3252 rows out of 24^3, all exactly
#   induced by the full 35280-row table.  Probe with the R225 default plus `--intersecting-triple-tables`
#   returned UNKNOWN after `62.24s` with `0` conflicts / `0` branches.  Do NOT add ternary projections
#   to the default unless decomposed further or moved to a better table engine.
# R227 CP-SAT ADD: compact algebraic shadows of the R210 intersecting table were audited.  Parity
#   shadow has `52/64` allowed patterns; D8-coset shadow has `182/729`, both exactly induced by the
#   full 35280-row table.  Short 60s/8-worker CP-SAT profiles:
#     R225 default (`--matching-triangle-tables --intersecting-pair-tables`): `14788` conflicts / `400367` branches;
#     R225 + parity shadow: `8863` / `652149`;
#     R225 + coset shadow: `8016` / `234594`;
#     R225 + coset + parity: `8960` / `629971`;
#     matching-triangle + coset, no pair projections: `9236` / `173732`;
#     coset over disjoint tables only: `5` / `16507`.
#   A longer 180s run of `--disjoint-tables --intersecting-coset-table` remained UNKNOWN
#   (`83847` conflicts / `1852607` branches), so this is not proof evidence.  For short local rooted
#   CP-SAT diagnostics, prefer:
#     python .\root_cell_permutation_csp.py --time-cap <T> --workers <W> --disjoint-tables --intersecting-coset-table ...
#   Do not add parity by default; pair projections and matching-triangle tables are exact but worsened
#   this profile once the coset shadow was present.
# R228 ROOTED NEGATIVE: the pure D8-coset quotient is feasible.  Probe
#   `root_cell_coset_quotient_probe.py` keeps 210 directed block-coset vars and 945 relative-coset
#   vars, with projected inverse, relative-composition, R209 disjoint, R227 intersecting-coset, and
#   R222 matching-triangle constraints.  Unfixed quotient is OPTIMAL in `2.4s`.  Fixing the 24 R220
#   reps only at coset level kills `[1,3,5,9,11,14]`, but all exact R220 survivors
#   `[0,2,7,8,10,15,21,22]` remain feasible.  Do not retry the pure coset quotient as a standalone
#   obstruction; the remaining R220 kills need finer S4-entry structure.
# R229/R230 SAT-PROOF CERTIFICATE: the R227 intersecting D8-coset shadow has been moved into
#   `root_cell_permutation_sat.py --intersecting-coset-cuts` with relative-permutation literals tied
#   to the original S4 block entries.  Audit `root_cell_intersecting_coset_sat_audit.py` proves the SAT
#   duplicate matches the CP-SAT source projection: 105 intersecting pairs, 35280 full rows each,
#   182/729 allowed coset rows, and 0 orientation failures over all 24x24 block pairs.  R204 formula,
#   R220 orbit/unit, and block-rep audits were rerun and passed.
#   One-command local UNSAT suite:
#     python .\root_cell_triangle_rep_cloud_suite.py --out-dir scratchpad\root_cell_triangle_rep_cloud_r229_unsat_suite --card-encoding seqcounter --intersecting-coset-cuts --smoke-solve --solver cadical153 --time-cap 120 --no-export
#   completed in `516.6051s` and solved all eight R220 survivors UNSAT:
#     reps `[0,2,7,8,10,15,21,22]` with solve seconds `[22.8648,45.5025,88.0111,92.4448,11.9727,98.4614,70.0938,60.9130]`.
#   Export proof-input CNFs with:
#     python .\root_cell_triangle_rep_cloud_suite.py --out-dir scratchpad\root_cell_triangle_rep_cloud_r229_seq_intercoset --card-encoding seqcounter --intersecting-coset-cuts
#   R230 UPDATE: proof tooling was built locally under `scratchpad\tools`, and all 24 R220
#   representatives now have ASCII DRAT certificates independently checked by `drat-trim`.
#   Certificate summary:
#     scratchpad\root_cell_triangle_rep_cloud_r229_seq_intercoset\r229_all24_ascii_drat_checked_summary.json
#   reports `ok=true`, `unsatCount=24`, `verifiedCount=24`.  Local replay/audit command:
#     python .\root_cell_r229_certificate_audit.py --json-out scratchpad\root_cell_r229_certificate_audit_current.json
#   Therefore the rooted SAT route is the decisive verified nonexistence certificate in this repository.
#   R43/R199/R218 r=3 Stage-A measurement remains runnable only as a fallback/cross-check.

# R49 ADD: `--stats-out` JSON + `s3_aggregate_shards.py` strict combiner. Cloud workers now emit
#   auditable per-shard records with source-frontier SHA-256, canonical-parent metadata, exact/sampled
#   depth status, prune counters, and branching. The combiner refuses seeded diagnostic slices,
#   pre-R48 frontiers, mixed shard sets, missing shards unless explicitly diagnostic, or mixed source
#   hashes, and marks only fully covered unsampled depths as exact.
# R50 ADD: canonical-parent ownership is evaluated after child BLISS duplicate detection and cached by
#   child canonical key. This preserves the R48 exact ownership rule but avoids repeated vertex-deletion
#   BLISS work for isomorphic children. Verified unchanged counts through depth 8 and exact shard
#   recombination 5=21,6=62,7=208; small local wall times improved on d5->d7 shards.
# R52 ADD: full-scope resumed frontier outputs are chainable again. `frontier_complete=true` is now
#   preserved when a complete source frontier is resumed with `--shard-count 1` and the continuation has
#   no sampled levels; true shard outputs remain non-global. Exact depth 10 measured:
#   N10=42430 from the R50/R51 depth-9 frontier, aggregate-proven.
# R53 ADD: four deterministic 1/64 shards from depth 10 to 11 completed for sizing. They cover
#   2652/42430 parents, produce 29167 children, and give diagnostic scaled N11~4.67e5; this is NOT an
#   exact count until all 64 shards are aggregated without `--allow-incomplete`.
# R54 ADD: `s3_run_shards.py` wraps the verified harness+aggregator into a foreground resumable shard
#   range runner. Verified on shards 4-5; combined shards 0-5 cover 3978/42430 parents and give
#   diagnostic N11~4.70e5. Exact N11 still requires all 64 shards.
# R55 ADD: shards 6-7 completed; combined shards 0-7 cover 5304/42430 parents (12.5%) and give
#   diagnostic N11~4.692e5. No local/spectral/triangle pruning has fired in any d10->d11 pilot shard.
# R56 ADD: shards 8-9 completed after a fresh `--gate` proof pass. Combined shards 0-9 cover
#   6630/42430 parents (15.63%), produce 74059 depth-11 children, weighted branch 11.170, and give
#   diagnostic N11~4.740e5. Still incomplete/diagnostic; exact N11 requires shards 10..63 plus a final
#   aggregate without `--allow-incomplete`. No local/spectral/triangle pruning has fired.
# R57 ADD: shards 10-11 completed; combined shards 0-11 cover 7956/42430 parents (18.75%), produce
#   87955 depth-11 children, weighted branch 11.055, and give diagnostic N11~4.691e5. Still diagnostic;
#   exact N11 requires shards 12..63 plus a final aggregate without `--allow-incomplete`. No pruning has
#   fired and no shard has hit budget/time/sample caps.
# R58 ADD: `s3_run_shards.py --frontier-out-dir DIR` can now preserve one frontier JSONL per shard, and
#   `s3_merge_frontiers.py` strictly merges a complete compatible shard set into one chainable complete
#   frontier. Verified on the known d5->d6->d7 two-shard reconstruction: merged d6 frontier has 62 rows
#   and continues exactly to N7=208; incomplete merge is refused.
# R59 ADD: shards 12-13 completed with `--frontier-out-dir`; combined shards 0-13 cover 9282/42430
#   parents (21.88%), produce 101946 depth-11 children, weighted branch 10.983, diagnostic N11~4.660e5.
#   Shards 12-13 now also have per-shard depth-11 frontier JSONL rows (7196 and 6795). Shards 0-11 are
#   valid count evidence but still stats-only unless rerun with frontier output.
# R60 ADD: shards 14-15 completed with `--frontier-out-dir`; combined shards 0-15 cover 10608/42430
#   parents (25.00%), produce 116519 depth-11 children, weighted branch 10.984, diagnostic N11~4.661e5.
#   Shards 12-15 now have frontier JSONL rows; shards 0-11 remain stats-only.
# R61 ADD: shards 16-17 completed with `--frontier-out-dir`; combined shards 0-17 cover 11934/42430
#   parents (28.13%), produce 132166 depth-11 children, weighted branch 11.075, diagnostic N11~4.699e5.
#   Shards 12-17 now have frontier JSONL rows; shards 0-11 remain stats-only.
# R62 ADD: shards 18-19 completed with `--frontier-out-dir`; combined shards 0-19 cover 13260/42430
#   parents (31.25%), produce 144968 depth-11 children, weighted branch 10.933, diagnostic N11~4.639e5.
#   Shards 12-19 now have frontier JSONL rows; shards 0-11 remain stats-only.
# R63 ADD: shards 20-21 completed with `--frontier-out-dir`; combined shards 0-21 cover 14586/42430
#   parents (34.38%), produce 159115 depth-11 children, weighted branch 10.908, diagnostic N11~4.629e5.
#   Shards 12-21 now have frontier JSONL rows; shards 0-11 remain stats-only.
# R64 ADD: shards 22-23 completed with `--frontier-out-dir`; combined shards 0-23 cover 15912/42430
#   parents (37.50%), produce 171794 depth-11 children, weighted branch 10.797, diagnostic N11~4.581e5.
#   Shards 12-23 now have frontier JSONL rows; shards 0-11 remain stats-only.
# R65 ADD: shards 24-25 completed with `--frontier-out-dir`; combined shards 0-25 cover 17238/42430
#   parents (40.63%), produce 186429 depth-11 children, weighted branch 10.815, diagnostic N11~4.589e5.
#   Shards 12-25 now have frontier JSONL rows; shards 0-11 remain stats-only.
# R66 ADD: shards 26-27 completed with `--frontier-out-dir`; combined shards 0-27 cover 18564/42430
#   parents (43.75%), produce 201063 depth-11 children, weighted branch 10.831, diagnostic N11~4.596e5.
#   Shards 12-27 now have frontier JSONL rows; shards 0-11 remain stats-only.
# R67 ADD: shards 28-29 completed with `--frontier-out-dir`; combined shards 0-29 cover 19890/42430
#   parents (46.88%), produce 216440 depth-11 children, weighted branch 10.882, diagnostic N11~4.617e5.
#   Shards 12-29 now have frontier JSONL rows; shards 0-11 remain stats-only.
# R68 ADD: shards 30-31 completed with `--frontier-out-dir`; combined shards 0-31 cover 21216/42430
#   parents (50.00%), produce 229954 depth-11 children, weighted branch 10.838, diagnostic N11~4.599e5.
#   Shards 12-31 now have frontier JSONL rows; shards 0-11 remain stats-only.
# R69 ADD: shards 32-33 completed with `--frontier-out-dir`; combined shards 0-33 cover 22542/42430
#   parents (53.13%), produce 243860 depth-11 children, weighted branch 10.818, diagnostic N11~4.590e5.
#   Shards 12-33 now have frontier JSONL rows; shards 0-11 remain stats-only.
# R70 ADD: shards 34-35 completed with `--frontier-out-dir`; combined shards 0-35 cover 23868/42430
#   parents (56.25%), produce 257602 depth-11 children, weighted branch 10.793, diagnostic N11~4.579e5.
#   Shards 12-35 now have frontier JSONL rows; shards 0-11 remain stats-only.
# R71 ADD: shards 36-37 completed with `--frontier-out-dir`; combined shards 0-37 cover 25194/42430
#   parents (59.38%), produce 270666 depth-11 children, weighted branch 10.743, diagnostic N11~4.558e5.
#   Shards 12-37 now have frontier JSONL rows; shards 0-11 remain stats-only.
# R72 ADD: shards 38-39 completed with `--frontier-out-dir`; combined shards 0-39 cover 26520/42430
#   parents (62.50%), produce 285168 depth-11 children, weighted branch 10.753, diagnostic N11~4.562e5.
#   Shards 12-39 now have frontier JSONL rows; shards 0-11 remain stats-only.
# R73 ADD: shards 40-41 completed with `--frontier-out-dir`; combined shards 0-41 cover 27846/42430
#   parents (65.63%), produce 300052 depth-11 children, weighted branch 10.775, diagnostic N11~4.572e5.
#   Shards 12-41 now have frontier JSONL rows; shards 0-11 remain stats-only.
# R74 ADD: shards 42-43 completed with `--frontier-out-dir`; combined shards 0-43 cover 29172/42430
#   parents (68.75%), produce 314653 depth-11 children, weighted branch 10.786, diagnostic N11~4.577e5.
#   Shards 12-43 now have frontier JSONL rows; shards 0-11 remain stats-only.
# R75 ADD: shards 44-45 completed with `--frontier-out-dir`; combined shards 0-45 cover 30498/42430
#   parents (71.88%), produce 329214 depth-11 children, weighted branch 10.795, diagnostic N11~4.580e5.
#   Shards 12-45 now have frontier JSONL rows; shards 0-11 remain stats-only.
# R76 ADD: shards 46-47 completed with `--frontier-out-dir`; combined shards 0-47 cover 31824/42430
#   parents (75.00%), produce 344433 depth-11 children, weighted branch 10.823, diagnostic N11~4.592e5.
#   Shards 12-47 now have frontier JSONL rows; shards 0-11 remain stats-only.
# R77 ADD: shards 48-49 completed with `--frontier-out-dir`; combined shards 0-49 cover 33150/42430
#   parents (78.13%), produce 358670 depth-11 children, weighted branch 10.820, diagnostic N11~4.591e5.
#   Shards 12-49 now have frontier JSONL rows; shards 0-11 remain stats-only.
# R78 ADD: shards 50-51 completed with `--frontier-out-dir`; combined shards 0-51 cover 34476/42430
#   parents (81.25%), produce 373622 depth-11 children, weighted branch 10.837, diagnostic N11~4.598e5.
#   Shards 12-51 now have frontier JSONL rows; shards 0-11 remain stats-only.
# R79 ADD: shards 52-53 completed with `--frontier-out-dir`; combined shards 0-53 cover 35802/42430
#   parents (84.38%), produce 389619 depth-11 children, weighted branch 10.883, diagnostic N11~4.617e5.
#   Shards 12-53 now have frontier JSONL rows; shards 0-11 remain stats-only.
# R80 ADD: shards 54-55 completed with `--frontier-out-dir`; combined shards 0-55 cover 37128/42430
#   parents (87.50%), produce 405619 depth-11 children, weighted branch 10.925, diagnostic N11~4.635e5.
#   Shards 12-55 now have frontier JSONL rows; shards 0-11 remain stats-only.
# R81 ADD: shards 56-57 completed with `--frontier-out-dir`; combined shards 0-57 cover 38454/42430
#   parents (90.63%), produce 420629 depth-11 children, weighted branch 10.938, diagnostic N11~4.641e5.
#   Shards 12-57 now have frontier JSONL rows; shards 0-11 remain stats-only.
# R82 ADD: shards 58-59 completed with `--frontier-out-dir`; combined shards 0-59 cover 39780/42430
#   parents (93.75%), produce 434876 depth-11 children, weighted branch 10.932, diagnostic N11~4.638e5.
#   Shards 12-59 now have frontier JSONL rows; shards 0-11 remain stats-only.
# R83 ADD: shards 60-61 completed with `--frontier-out-dir`; combined shards 0-61 cover 41106/42430
#   parents (96.88%), produce 450105 depth-11 children, weighted branch 10.950, diagnostic N11~4.646e5.
#   Shards 12-61 now have frontier JSONL rows; shards 0-11 remain stats-only.
# R84 ADD: all 64 d10->d11 shards completed and strict-aggregated WITHOUT `--allow-incomplete`.
#   Exact r=3 counts through depth 11 are now certified: N10=42430, N11=463636, weighted branch
#   10.927. No budget/time/sample flags; no local/spectral/triangle prune has fired by depth 11.
#   Shards 12-63 have frontier JSONL rows; shards 0-11 remain stats-only and must be rerun with
#   `--frontier-out-dir` before merging a complete chainable depth-11 frontier.
# R85 ADD: frontier backfill started. Shards 0-1 were rerun with `--frontier-out-dir`, exactly
#   reproducing original counts (7818, 7260) and writing matching JSONL rows. Shards 2-11 remain
#   stats-only before a complete d11 frontier can be merged.
# R86 ADD: frontier backfill advanced through shards 2-3, exactly reproducing original counts
#   (6930, 7159) and writing matching JSONL rows. Shards 4-11 remain stats-only before merge.
# R87 ADD: frontier backfill advanced through shards 4-5, exactly reproducing original counts
#   (7392, 7473) and writing matching JSONL rows. Shards 6-11 remain stats-only before merge.
# R88 ADD: frontier backfill advanced through shards 6-7, exactly reproducing original counts
#   (6745, 7881) and writing matching JSONL rows. Shards 8-11 remain stats-only before merge.
# R90 ADD: backfilled shards 8-11, then strictly merged all 64 frontier-bearing shard stats into
#   `scratchpad\r3_frontier_d11_r90.jsonl`. Header and physical row count both certify 463636 depth-11
#   graph rows, `frontier_complete=true`, merged_from_shards 0..63. This is now the preferred exact
#   reusable prefix for d11->d12+ continuation; still not a construction/nonexistence proof.
# R91 ADD: validated continuation from `scratchpad\r3_frontier_d11_r90.jsonl` with d11->d12 shard
#   0/512. Loaded 906 parents, produced 11325 depth-12 children (branch 12.500), wrote matching
#   frontier rows; diagnostic scaled N12~5.795e6. This is a probe only, not exact.
# R92 ADD: d11->d12 shard 1/512 completed from `scratchpad\r3_frontier_d11_r90.jsonl`. Loaded
#   906 parents, produced 11943 depth-12 children (branch 13.182), wrote matching frontier rows.
#   Combined shards 0-1 cover 1812/463636 parents (0.3908%), produce 23268 depth-12 children,
#   and give diagnostic scaled N12~5.954e6. No budget/time/sample flags; no pruning has fired.
#   This remains a probe only, not exact.
# R93 ADD: d11->d12 shard 2/512 completed from the same exact d11 frontier. Loaded 906 parents,
#   produced 12012 depth-12 children (branch 13.258), wrote matching frontier rows. Combined
#   shards 0-2 cover 2718/463636 parents (0.5862%), produce 35280 depth-12 children, and give
#   diagnostic scaled N12~6.018e6. No budget/time/sample flags; no pruning has fired. Probe only.
# R94 ADD: d11->d12 shard 3/512 completed from the same exact d11 frontier. Loaded 906 parents,
#   produced 13692 depth-12 children (branch 15.113), wrote matching frontier rows. Combined
#   shards 0-3 cover 3624/463636 parents (0.7816%), produce 48972 depth-12 children, and give
#   diagnostic scaled N12~6.265e6. No budget/time/sample flags; no pruning has fired. Probe only.
# R95 ADD: `s3_cloud_r3_d12.py` is now the one-command exact d11->d12 cloud wrapper. It runs
#   the soundness gate by default, then calls `s3_run_shards.py` from `r3_frontier_d11_r90.jsonl`
#   over 512 shards. Full 0..512 runs are strict exact aggregates; worker/indices runs auto-pass
#   `--allow-incomplete` and are labelled diagnostic. Verified by py_compile, dry-run command
#   expansion, and a fresh `s3_slice_harness.py --gate` pass (rook9 + T(7), ALL GREEN).
# R96 ADD: first spaced d11->d12 probe completed: shard 128/512 loaded 906 parents and produced
#   12640 children (branch 13.951). Stratified aggregate over shards 0,1,2,3,128 covers
#   4530/463636 parents (0.9770%), produces 61612 depth-12 children, and gives diagnostic
#   scaled N12~6.306e6. No budget/time/sample flags; no pruning has fired. Probe only.
# R97 ADD: second spaced d11->d12 probe completed: shard 256/512 loaded 906 parents and produced
#   12061 children (branch 13.312). Stratified aggregate over shards 0,1,2,3,128,256 covers
#   5436/463636 parents (1.1724%), produces 73673 depth-12 children, and gives diagnostic
#   scaled N12~6.284e6. No budget/time/sample flags; no pruning has fired. Probe only.
# R98 ADD: third spaced d11->d12 probe completed: shard 384/512 loaded 905 parents and produced
#   13987 children (branch 15.455). Stratified aggregate over shards 0,1,2,3,128,256,384 covers
#   6341/463636 parents (1.3676%), produces 87660 depth-12 children, and gives diagnostic
#   scaled N12~6.409e6. No budget/time/sample flags; no pruning has fired. Probe only.
# R99 ADD: bounded vertical diagnostic from the R91 d12 shard-0 frontier to depth 13 completed.
#   Source frontier is globally incomplete and output remains diagnostic (`frontier_complete=false`,
#   loaded-scope complete only). Loaded 177/11325 local d12 parents (subshard 0/64), produced
#   4104 depth-13 children (branch 23.186), scaled local-shard N13~262586. No budget/time/sample
#   flags; no pruning has fired. Not a global d13 estimate.
# R100 ADD: second bounded d12->d13 diagnostic from the R98 shard-384 d12 frontier completed.
#   Source/output globally incomplete, loaded-scope complete only. Loaded 219/13987 local d12
#   parents (subshard 0/64), produced 4729 depth-13 children (branch 21.594), scaled local-shard
#   N13~302030. No budget/time/sample flags; no pruning has fired. Not a global d13 estimate.
# R101 ADD: `READINESS_R100.md` captures the current measured verdict. The harness is ready for
#   exact N12 cloud measurement from the R90 d11 frontier; it is NOT ready for existence/nonexistence,
#   global N13, or depth-45 feasibility claims. Next best move is exact N12, then d13 from a complete
#   d12 frontier.
# R102 ADD: third bounded d12->d13 diagnostic from the R97 shard-256 d12 frontier completed.
#   Source/output globally incomplete, loaded-scope complete only. Loaded 189/12061 local d12
#   parents (subshard 0/64), produced 4235 depth-13 children (branch 22.407), scaled local-shard
#   N13~270256. Across R99/R100/R102 local d13 diagnostics, branch range is 21.594..23.186 and
#   no pruning has fired. Not a global d13 estimate.
# R103 ADD: exact-contributing d11->d12 shards 4-7/512 completed from the R90 d11 frontier.
#   Counts: 14042, 13225, 11951, 12497 children from 906 parents each; all wrote matching frontier
#   rows. Known shard set 0,1,2,3,4,5,6,7,128,256,384 now covers 9965/463636 parents (2.1493%),
#   produces 139375 depth-12 children, and gives diagnostic scaled N12~6.485e6. No budget/time/sample
#   flags; no pruning has fired. Still diagnostic until all 512 shards are present.
# R104 ADD: exact-contributing d11->d12 shards 8-11/512 completed from the R90 d11 frontier.
#   Counts: 13142, 13017, 12116, 13222 children from 906 parents each; all wrote matching frontier
#   rows. Known shard set 0..11 plus 128,256,384 now covers 13589/463636 parents (2.9310%),
#   produces 190872 depth-12 children, and gives diagnostic scaled N12~6.512e6. No budget/time/sample
#   flags; no pruning has fired. Still diagnostic until all 512 shards are present.
# R105 ADD: exact-contributing d11->d12 shards 12-15/512 completed from the R90 d11 frontier.
#   Counts: 12285, 12393, 13009, 12545 children from 906 parents each; all wrote matching frontier
#   rows. Known shard set 0..15 plus 128,256,384 now covers 17213/463636 parents (3.7126%),
#   produces 241104 depth-12 children, and gives diagnostic scaled N12~6.494e6. No budget/time/sample
#   flags; no pruning has fired. Still diagnostic until all 512 shards are present.
# R106 ADD: exact-contributing d11->d12 shards 16-19/512 completed from the R90 d11 frontier.
#   Counts: 12510, 13507, 15324, 13615 children from 906 parents each; all wrote matching frontier
#   rows. Known shard set 0..19 plus 128,256,384 now covers 20837/463636 parents (4.4943%),
#   produces 296060 depth-12 children, and gives diagnostic scaled N12~6.588e6. No budget/time/sample
#   flags; no pruning has fired. Branch range now 12.500..16.914. Still diagnostic until all 512 shards
#   are present.
# R107 ADD: exact-contributing d11->d12 shards 20-23/512 completed from the R90 d11 frontier.
#   Counts: 12556, 13357, 13359, 14823 children from 906 parents each; all wrote matching frontier
#   rows. Known shard set 0..23 plus 128,256,384 now covers 24461/463636 parents (5.2759%),
#   produces 350155 depth-12 children, and gives diagnostic scaled N12~6.637e6. No budget/time/sample
#   flags; no pruning has fired. Branch range remains 12.500..16.914. Still diagnostic until all
#   512 shards are present.
# R108 ADD: graphify+SCAMPER source-mining pass produced `SCAMPER_BREAKTHROUGH_R108.md` and a cheap
#   frontier-strata experiment, `s3_frontier_strata.py`. On the R107 d12 frontiers it scanned 54095
#   rows: edge range 8..24, triangle range 0..7, max lambda2=2.646164<3, min lambda_min=-3.361325>-4,
#   and 0 spectral gate violations. Conclusion: do not spend local diagnostics on shallow R107
#   spectral-extreme rows; they are not near the deep gates yet. The provisional order-six/hexagon
#   next-lever note is superseded by R109's ledger check: the known n3 census route is already
#   characterized unless a new independent n3 handle appears.
# R109 ADD: exact-contributing d11->d12 shards 24-25/512 completed from the R90 d11 frontier.
#   Counts: 13717 and 14942 children from 906 parents each; both wrote matching frontier rows.
#   Known shard set 0..25 plus 128,256,384 now covers 26273/463636 parents (5.6667%),
#   produces 378814 depth-12 children, and gives diagnostic scaled N12~6.685e6. No budget/time/sample
#   flags; no pruning has fired. Branch range remains 12.500..16.914. The R109 soundness gate rerun
#   stayed ALL GREEN (rook9 local/spectral/triangle checks + T(7) CRS/CSP reconstruction, 0/5242
#   T(7) false rejects). Also corrected the R108 next-lever note: order-six/n3 was already characterized
#   in R15/R24/R30 (p6 identity, Makhnev conditional, n3>=3, n3 still free mod 3). Do not retread it
#   unless a new independent handle on n3/completion capacity appears. Active cloud lever remains exact
#   N12 via `s3_cloud_r3_d12.py` or continued shard filling.
# R110 ADD: exact-contributing d11->d12 shards 26-27/512 completed from the R90 d11 frontier.
#   Counts: 13886 and 13287 children from 906 parents each; both wrote matching frontier rows and
#   physical row recounts matched stats/header counts exactly. Known shard set 0..27 plus 128,256,384
#   now covers 28085/463636 parents (6.0576%), produces 405987 depth-12 children, and gives diagnostic
#   scaled N12~6.702e6. No budget/time/sample flags; no pruning has fired. Branch range remains
#   12.500..16.914. The soundness gate rerun stayed ALL GREEN (rook9 local/spectral/triangle checks
#   + T(7) CRS/CSP reconstruction, 0/5242 T(7) false rejects).
# R111 ADD: exact-contributing d11->d12 shards 28-29/512 completed from the R90 d11 frontier.
#   Counts: 13486 and 12229 children from 906 parents each; both wrote matching frontier rows and
#   physical row recounts matched stats/header counts exactly. Known shard set 0..29 plus 128,256,384
#   now covers 29897/463636 parents (6.4484%), produces 431702 depth-12 children, and gives diagnostic
#   scaled N12~6.695e6. No budget/time/sample flags; no pruning has fired. Branch range remains
#   12.500..16.914. The soundness gate rerun stayed ALL GREEN (rook9 local/spectral/triangle checks
#   + T(7) CRS/CSP reconstruction, 0/5242 T(7) false rejects).
# R112 ADD: exact-contributing d11->d12 shards 30-31/512 completed from the R90 d11 frontier.
#   Counts: 13908 and 12461 children from 906 parents each; both wrote matching frontier rows and
#   physical row recounts matched stats/header counts exactly. Known shard set 0..31 plus 128,256,384
#   now covers 31709/463636 parents (6.8392%), produces 458071 depth-12 children, and gives diagnostic
#   scaled N12~6.698e6. No budget/time/sample flags; no pruning has fired. Branch range remains
#   12.500..16.914. The soundness gate rerun stayed ALL GREEN (rook9 local/spectral/triangle checks
#   + T(7) CRS/CSP reconstruction, 0/5242 T(7) false rejects).
# R113 ADD: exact-contributing d11->d12 shards 32-33/512 completed from the R90 d11 frontier.
#   Counts: 13625 and 13963 children from 906 parents each; both wrote matching frontier rows and
#   physical row recounts matched stats/header counts exactly. Known shard set 0..33 plus 128,256,384
#   now covers 33521/463636 parents (7.2300%), produces 485659 depth-12 children, and gives diagnostic
#   scaled N12~6.717e6. No budget/time/sample flags; no pruning has fired. Branch range remains
#   12.500..16.914. The soundness gate rerun stayed ALL GREEN (rook9 local/spectral/triangle checks
#   + T(7) CRS/CSP reconstruction, 0/5242 T(7) false rejects).
# R114 ADD: exact-contributing d11->d12 shards 34-35/512 completed from the R90 d11 frontier.
#   Counts: 14660 and 13666 children from 906 parents each; both wrote matching frontier rows and
#   physical row recounts matched stats/header counts exactly. Known shard set 0..35 plus 128,256,384
#   now covers 35333/463636 parents (7.6208%), produces 513985 depth-12 children, and gives diagnostic
#   scaled N12~6.744e6. No budget/time/sample flags; no pruning has fired. Branch range remains
#   12.500..16.914. The soundness gate rerun stayed ALL GREEN (rook9 local/spectral/triangle checks
#   + T(7) CRS/CSP reconstruction, 0/5242 T(7) false rejects).
# R115 ADD: exact-contributing d11->d12 shards 36-37/512 completed from the R90 d11 frontier.
#   Counts: 13327 and 14599 children from 906 parents each; both wrote matching frontier rows and
#   physical row recounts matched stats/header counts exactly. Known shard set 0..37 plus 128,256,384
#   now covers 37145/463636 parents (8.0117%), produces 541911 depth-12 children, and gives diagnostic
#   scaled N12~6.764e6. No budget/time/sample flags; no pruning has fired. Branch range remains
#   12.500..16.914. The soundness gate rerun stayed ALL GREEN (rook9 local/spectral/triangle checks
#   + T(7) CRS/CSP reconstruction, 0/5242 T(7) false rejects).
# R116 ADD: exact-contributing d11->d12 shards 38-39/512 completed from the R90 d11 frontier.
#   Counts: 14775 and 13023 children from 906 parents each; both wrote matching frontier rows and
#   physical row recounts matched stats/header counts exactly. Known shard set 0..39 plus 128,256,384
#   now covers 38957/463636 parents (8.4025%), produces 569709 depth-12 children, and gives diagnostic
#   scaled N12~6.780e6. No budget/time/sample flags; no pruning has fired. Branch range remains
#   12.500..16.914. The soundness gate rerun stayed ALL GREEN (rook9 local/spectral/triangle checks
#   + T(7) CRS/CSP reconstruction, 0/5242 T(7) false rejects).
# R117 ADD: exact-contributing d11->d12 shards 40-41/512 completed from the R90 d11 frontier.
#   Counts: 13471 and 12750 children from 906 parents each; both wrote matching frontier rows and
#   physical row recounts matched stats/header counts exactly. Known shard set 0..41 plus 128,256,384
#   now covers 40769/463636 parents (8.7933%), produces 595930 depth-12 children, and gives diagnostic
#   scaled N12~6.777e6. No budget/time/sample flags; no pruning has fired. Branch range remains
#   12.500..16.914. The soundness gate rerun stayed ALL GREEN (rook9 local/spectral/triangle checks
#   + T(7) CRS/CSP reconstruction, 0/5242 T(7) false rejects).
# R118 ADD: exact-contributing d11->d12 shards 42-43/512 completed from the R90 d11 frontier.
#   Counts: 14049 and 13885 children from 906 parents each; both wrote matching frontier rows and
#   physical row recounts matched stats/header counts exactly. Known shard set 0..43 plus 128,256,384
#   now covers 42581/463636 parents (9.1841%), produces 623864 depth-12 children, and gives diagnostic
#   scaled N12~6.793e6. No budget/time/sample flags; no pruning has fired. Branch range remains
#   12.500..16.914. The soundness gate rerun stayed ALL GREEN (rook9 local/spectral/triangle checks
#   + T(7) CRS/CSP reconstruction, 0/5242 T(7) false rejects).
# R119 ADD: exact-contributing d11->d12 shards 44-45/512 completed from the R90 d11 frontier.
#   Counts: 13519 and 12526 children from 906 parents each; both wrote matching frontier rows and
#   physical row recounts matched stats/header counts exactly. Known shard set 0..45 plus 128,256,384
#   now covers 44393/463636 parents (9.5750%), produces 649909 depth-12 children, and gives diagnostic
#   scaled N12~6.788e6. No budget/time/sample flags; no pruning has fired. Branch range remains
#   12.500..16.914. The soundness gate rerun stayed ALL GREEN (rook9 local/spectral/triangle checks
#   + T(7) CRS/CSP reconstruction, 0/5242 T(7) false rejects). Per the active goal, do not launch
#   more shard batches until the graphify+SCAMPER breakthrough pass is complete.
# R121 ADD: graphify+SCAMPER breakthrough pass completed in `SCAMPER_BREAKTHROUGH_R121.md`.
#   Taylor's adjacent-pair 27-vertex local templates were rebuilt with current BLISS/local-gate tooling:
#   `s3_taylor_edge_templates.py --out scratchpad\taylor_edge_templates_r120.json` reproduces the
#   notebook count ladder exactly and yields 11 final representatives, all accepted by
#   `PartialGraph.can_add`. Each template is spectral-boundary tight: exact inertia of A-3I is
#   (1,25,1), with lambda2=3 and lambda_min=-4. Diagnostic continuation from these 11 depth-27
#   boundary seeds using current Stage-A gates measured 11 -> 11 -> 11 through depth 29, with
#   50784 spectral prunes, 0 local prunes, 0 triangle-split prunes, no time/budget/sample flags,
#   wall 420.31s. Added one-command reproducer `s3_taylor_seed_probe.py`.
#   IMPORTANT: this seeded line is not proof-complete for the r=3 star-complement search until a
#   containment/basis-extension lemma is proved: every hypothetical srg99 must have an r=3 star
#   complement containing one full Taylor adjacent-pair template. Next cloud/foreground action is
#   NOT ordinary d11 shard filling; it is either prove/falsify that lemma or run:
#     python s3_taylor_seed_probe.py --target-depth 30 --time-cap 3600 --out scratchpad\taylor_seed_probe_d30.json
#   If the containment lemma fails, build the sound full-host Taylor-template continuation instead.
# R122 ADD: containment lemma FAILED by exact supported-eigenvector proof.
#   `s3_taylor_supported_eigenvector.py --out scratchpad\taylor_supported_eigenvector_r122.json`
#   verifies that every Taylor 27-vertex template has the same supported 3-eigenvector:
#     [3,-3,0,1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1].
#   The vector remains a 3-eigenvector in any valid induced extension containing the full template:
#   outside vertices are nonadjacent to the saturated endpoints 0,1; mu=2 forces two neighbours in
#   each endpoint neighbourhood, and the common neighbour has weight 0, so +1 and -1 contributions
#   balance. Therefore no r=3 star complement can contain a full Taylor adjacent-pair template.
#   Do NOT scale the R121 Taylor-seeded r=3 H-search as a proof route. The Taylor lever remains sound
#   only as a full-host seeded search or as boundary-equation information. Next implementation target:
#   `s3_taylor_fullhost_probe.py` (local lambda/mu + hereditary spectral gates, no r=3 H edge-band,
#   no terminal mult_3(H)=0 assumption).
# R123 ADD: sound full-host Taylor-template probe implemented and measured.
#   `s3_taylor_fullhost_probe.py` grows from the 11 Taylor templates using only full-host local
#   lambda/mu constraints, saturated exact lambda/mu checks, hereditary spectral gates, and BLISS
#   deduplication. It has frontier save/load and parent sharding.
#   Complete d27->d28:
#     python s3_taylor_fullhost_probe.py --target-depth 28 --time-cap 600 \
#       --out scratchpad\taylor_fullhost_probe_d28_r123.json \
#       --frontier-out scratchpad\taylor_fullhost_frontier_d28_r123.jsonl
#     counts 11 -> 879, saturated-exact rejects 18496, spectral rejects 0, iso_dups 36571.
#   d28->d29 shard 0/64:
#     14 parents -> 46017 children, saturated-exact rejects 41837, spectral rejects 0,
#     iso_dups 32490, wall 303s.
#   VERDICT: full-host Taylor continuation is sound and runnable, but naive brute-force scaling is
#   not promising. Do not launch a large Taylor full-host cloud run until a new algebraic cut is
#   derived. Next lever: edge-local 3-eigenvector algebra `(A+4I)(e_a-e_b)` over the 693 edges.
# R124 ADD: simple edge-vector Gram PSD/rank gate tested on Taylor frontiers.
#   `s3_edge_vector_gram_probe.py` scans present-edge vectors `(A+4I)(e_a-e_b)` and checks that their
#   Gram matrix is PSD with rank <=54. Results:
#     d28 full frontier 879 rows: 0 PSD/rank rejects, max rank 26.
#     d29 shard64_000 46017 rows: 0 PSD/rank rejects, max rank 27.
#   Verdict: this basic principal Gram condition is a reusable certificate check but not an early
#   pruning gate. Stronger edge-vector relations are needed before spending cloud on this line.
# R125 ADD: edge-vector Gram checker now includes the full projector upper-spectrum certificate.
#   In the full graph, the nonzero eigenvalues of the present-edge Gram are all
#   `(r-s)^2(k-r)=539`, so every principal partial must also have largest eigenvalue <=539.
#   `python s3_edge_vector_gram_probe.py --self-test` validates the formula on real witnesses:
#   T(7) rank 6/6 with lambda_max=175=upper, rook9 rank 4/4 with lambda_max=27=upper.
#   Re-scans:
#     d28 full frontier 879 rows: 0 PSD/rank/upper rejects, max rank 26, max lambda 309.778.
#     d29 shard64_000 46017 rows: 0 PSD/rank/upper rejects, max rank 27, max lambda 316.570.
#   Verdict unchanged: useful certificate, no early Taylor prune. Do not rerun principal Gram spectra
#   at these depths without a new relation.
# R126 ADD: exact-contributing d11->d12 shards 46-47/512 completed from the R90 d11 frontier.
#   Counts: 13421 and 12437 children from 906 parents each; both wrote matching frontier rows and
#   physical row recounts matched stats/header counts exactly. Known shard set 0..47 plus 128,256,384
#   now covers 46205/463636 parents (9.9658%), produces 675767 depth-12 children, and gives diagnostic
#   scaled N12~6.781e6. No budget/time/sample flags; no pruning has fired. Branch range remains
#   12.500..16.914. Aggregate: scratchpad\r3_d11_to_d12_shard512_known51_aggregate_r126.json.
# R127 ADD: exact-contributing d11->d12 shards 48-49/512 completed from the R90 d11 frontier.
#   Counts: 11303 and 13335 children from 906 parents each; both wrote matching frontier rows and
#   physical row recounts matched stats/header counts exactly. Known shard set 0..49 plus 128,256,384
#   now covers 48017/463636 parents (10.3577%), produces 700405 depth-12 children, and gives diagnostic
#   scaled N12~6.763e6. No budget/time/sample flags; no pruning has fired. Branch range is now
#   12.476..16.914. Aggregate: scratchpad\r3_d11_to_d12_shard512_known53_aggregate_r127.json.
# R128 ADD: exact-contributing d11->d12 shards 50-51/512 completed from the R90 d11 frontier.
#   Counts: 13507 and 14565 children from 906 parents each; both wrote matching frontier rows and
#   physical row recounts matched stats/header counts exactly. Known shard set 0..51 plus 128,256,384
#   now covers 49829/463636 parents (10.7464%), produces 728477 depth-12 children, and gives diagnostic
#   scaled N12~6.778e6. No budget/time/sample flags; no pruning has fired. Branch range remains
#   12.476..16.914. Aggregate: scratchpad\r3_d11_to_d12_shard512_known55_aggregate_r128.json.
# R129 ADD: exact-contributing d11->d12 shards 52-53/512 completed from the R90 d11 frontier.
#   Counts: 12349 and 12433 children from 906 parents each; both wrote matching frontier rows and
#   physical row recounts matched stats/header counts exactly. Known shard set 0..53 plus 128,256,384
#   now covers 51641/463636 parents (11.1383%), produces 753259 depth-12 children, and gives diagnostic
#   scaled N12~6.763e6. No budget/time/sample flags; no pruning has fired. Branch range remains
#   12.476..16.914. Aggregate: scratchpad\r3_d11_to_d12_shard512_known57_aggregate_r129.json.
# R130 ADD: graphify reassessment before further shards found no better bounded lever. Hits route to
#   already-closed H3/n3 propagation (R30), older rank/lattice lines, or the R124/R125 edge-Gram branch.
#   Decision: resume exact N12 coverage as the validated cost/calibration experiment.
# R131 ADD: exact-contributing d11->d12 shards 54-55/512 completed from the R90 d11 frontier.
#   Counts: 13662 and 12676 children from 906 parents each; both wrote matching frontier rows and
#   physical row recounts matched stats/header counts exactly. Known shard set 0..55 plus 128,256,384
#   now covers 53453/463636 parents (11.5291%), produces 779597 depth-12 children, and gives diagnostic
#   scaled N12~6.762e6. No budget/time/sample flags; no pruning has fired. Branch range remains
#   12.476..16.914. Aggregate: scratchpad\r3_d11_to_d12_shard512_known59_aggregate_r131.json.
# R132 ADD: `s3_cloud_r3_d12.py --indices` was exercised directly on d11->d12 shards 56-57/512.
#   Counts: 13023 and 13073 children from 906 parents each; both wrote matching frontier rows and
#   physical row recounts matched stats/header counts exactly. Known shard set 0..57 plus 128,256,384
#   now covers 55265/463636 parents (11.9200%), produces 805693 depth-12 children, and gives diagnostic
#   scaled N12~6.759e6. No budget/time/sample flags; no pruning has fired. Branch range remains
#   12.476..16.914. Aggregate: scratchpad\r3_d11_to_d12_shard512_known61_aggregate_r132.json.
# R133 ADD: exact-contributing d11->d12 shards 58-59/512 completed through `s3_cloud_r3_d12.py`.
#   Counts: 13630 and 13268 children from 906 parents each; both wrote matching frontier rows and
#   physical row recounts matched stats/header counts exactly. Known shard set 0..59 plus 128,256,384
#   now covers 57077/463636 parents (12.3107%), produces 832591 depth-12 children, and gives diagnostic
#   scaled N12~6.763e6. No budget/time/sample flags; no pruning has fired. Branch range remains
#   12.476..16.914. Aggregate: scratchpad\r3_d11_to_d12_shard512_known63_aggregate_r133.json.
# R134 ADD: exact-contributing d11->d12 shards 60-61/512 completed through `s3_cloud_r3_d12.py`.
#   Counts: 12840 and 14152 children from 906 parents each; both wrote matching frontier rows and
#   physical row recounts matched stats/header counts exactly. Known shard set 0..61 plus 128,256,384
#   now covers 58889/463636 parents (12.7016%), produces 859583 depth-12 children, and gives diagnostic
#   scaled N12~6.768e6. No budget/time/sample flags; no pruning has fired. Branch range remains
#   12.476..16.914. Aggregate: scratchpad\r3_d11_to_d12_shard512_known65_aggregate_r134.json.
# R135 ADD: exact-contributing d11->d12 shards 62-63/512 completed through `s3_cloud_r3_d12.py`.
#   Counts: 12768 and 13176 children from 906 parents each; both wrote matching frontier rows and
#   physical row recounts matched stats/header counts exactly. Known shard set 0..63 plus 128,256,384
#   now covers 60701/463636 parents (13.0924%), produces 885527 depth-12 children, and gives diagnostic
#   scaled N12~6.764e6. No budget/time/sample flags; no pruning has fired. Branch range remains
#   12.476..16.914. Aggregate: scratchpad\r3_d11_to_d12_shard512_known67_aggregate_r135.json.
# R136 ADD: contiguous d11->d12 block aggregate for shards 0..63/512 written as
#   scratchpad\r3_d11_to_d12_shard512_000_063_aggregate_r136.json. It covers 57984/463636 parents
#   (12.5064%), produces 846839 depth-12 children, and gives diagnostic scaled N12~6.771e6.
#   Consistency: known67 minus this block equals spaced probes 128,256,384 (2717 parents, 38688
#   children). No flags; no pruning has fired.
# R137 ADD: exact-contributing d11->d12 shards 64-65/512 completed through `s3_cloud_r3_d12.py`.
#   Counts: 15913 and 13255 children from 906 parents each; both wrote matching frontier rows and
#   physical row recounts matched stats/header counts exactly. Shard 64 is the current measured
#   high branch at 17.564. Known shard set 0..65 plus 128,256,384 now covers 62513/463636 parents
#   (13.4832%), produces 914695 depth-12 children, and gives diagnostic scaled N12~6.784e6.
#   No budget/time/sample flags; no pruning has fired. Branch range is now 12.476..17.564.
#   Aggregate: scratchpad\r3_d11_to_d12_shard512_known69_aggregate_r137.json.
# R138 ADD: exact-contributing d11->d12 shards 66-67/512 completed through `s3_cloud_r3_d12.py`.
#   Counts: 12716 and 13557 children from 906 parents each; both wrote matching frontier rows and
#   physical row recounts matched stats/header counts exactly. Known shard set 0..67 plus
#   128,256,384 now covers 64325/463636 parents (13.8740%), produces 940968 depth-12 children,
#   and gives diagnostic scaled N12~6.782e6. No budget/time/sample flags; no pruning has fired.
#   Branch range remains 12.476..17.564. Aggregate:
#   scratchpad\r3_d11_to_d12_shard512_known71_aggregate_r138.json.
# R139 ADD: exact-contributing d11->d12 shards 68-69/512 completed through `s3_cloud_r3_d12.py`.
#   Counts: 13890 and 13574 children from 906 parents each; both wrote matching frontier rows and
#   physical row recounts matched stats/header counts exactly. Known shard set 0..69 plus
#   128,256,384 now covers 66137/463636 parents (14.2649%), produces 968432 depth-12 children,
#   and gives diagnostic scaled N12~6.789e6. No budget/time/sample flags; no pruning has fired.
#   Branch range remains 12.476..17.564. Aggregate:
#   scratchpad\r3_d11_to_d12_shard512_known73_aggregate_r139.json.
# R140 ADD: exact-contributing d11->d12 shards 70-71/512 completed through `s3_cloud_r3_d12.py`.
#   Counts: 13253 and 13621 children from 906 parents each; both wrote matching frontier rows and
#   physical row recounts matched stats/header counts exactly. Known shard set 0..71 plus
#   128,256,384 now covers 67949/463636 parents (14.6557%), produces 995306 depth-12 children,
#   and gives diagnostic scaled N12~6.791e6. No budget/time/sample flags; no pruning has fired.
#   Branch range remains 12.476..17.564. Aggregate:
#   scratchpad\r3_d11_to_d12_shard512_known75_aggregate_r140.json.
# R142 ADD: after R141 introduced the rooted 84-label formulation, `root_cell_linear_rank.py` audited
#   its linear layer. Exact algebra proves `AS=SA` and far-degree rows are redundant after
#   `AN = 2J - N(I+M)` plus symmetry (`NN^T=S+2I`), and the modular audit confirms no linear
#   obstruction: combined `degree+AN+commute` is consistent modulo 2,3,5,7,1000003, with odd/large-prime
#   rank 1085 on 3486 edge variables (affine dimension 2401). Therefore centralizer/block rank alone
#   is exhausted; rooted progress must attack the quadratic common-neighbour equations or add a new
#   validated structural constraint. The r=3 cloud measurement below remains one-command runnable for
#   exact N12 cost measurement, but it is not a solution proof.
# R143 ADD: the rooted first-row branch is now measured. Fix far label `(0,2)`: the raw one-row `AN`
#   neighbourhood count is 56,011,010, but Burnside over its stabilizer in `S_2 wr S_7`
#   (`2*2^5*5! = 7680`) gives exactly 8,105 row orbits. This is a genuine symmetry cost reduction for
#   a future rooted SAT/SMS branch. The representative list is not yet generated, so this is not yet a
#   runnable complete rooted search.
# R144 ADD: rooted row-local quadratic propagation lemma. For any far vertex `u`, its far-neighbour
#   set is forced to be `5K2 + 2I` in the srg99 rooted model: the two row vertices whose labels overlap
#   `u` are isolated inside the row, and the other ten form a perfect matching. Outside cross-degrees
#   into the row are also fixed (20 overlap-1 outside labels have cross-degree 1; 51 overlap-0 labels
#   have cross-degree 2). Validated on all rook(9) rooted far-neighbourhoods and sampled BvLS243 roots.
#   Add this before any rooted SAT/SMS cloud solve.
# R145 ADD: generated the actual rooted first-row representative list via CP-SAT lex leaders over the
#   7680-element fixed-label stabilizer. `scratchpad\root_cell_row_reps_k14_r145.json` contains exactly
#   8105 distinct representatives, matching the R143 Burnside count; verifier confirms all satisfy AN
#   and the R144 split. R144 matching existence is not a row filter: all rows admit matchings, with
#   2,944,568 total row+matching choices. Next rooted layer must combine row matchings with outside
#   cross-degree/common-neighbour equations.
# R146 ADD: residual quotient of R144 row matchings is measured and low-yield: 2,944,568 raw
#   row+matching choices reduce only to 2,677,638 orbits because most rows have trivial residual
#   stabilizer. Do not spend the next cloud/research cycle on matching quotient alone; attach outside
#   equations or run row-seeded SAT/CP-SAT slices.
# R147 ADD: row-seeded outside-to-row incidence CP-SAT layer is measured and permissive. The model
#   enforces R144 matching, outside cross-degrees, row-pair common-neighbour equations, exact row-side
#   AN, and outside row-demand upper bounds. It is SAT on rook control, on first-100 srg99 row reps
#   after one longer timeout rerun, and on a 128-row stratified sample. Next rooted layer must include
#   outside-outside residual AN/common-neighbour structure; row+matching+outside-to-row alone is too loose.
# R148 ADD: outside residual AN probes. Cheap local-column aggregate balance is too weak (rook SAT,
#   stratified 128 srg99 rows SAT). Direct outside-AN CP-SAT with outside-outside edge variables is not
#   a usable oracle yet (rook SAT; first five srg99 rows UNKNOWN at 20s; row 0 UNKNOWN at 120s even
#   after fixed decision strategy). Do not read UNKNOWN as evidence. Reformulate outside layer as
#   structured residual b-matching/SAT or derive a smaller obstruction before scaling.
# R149 ADD: exact outside-pair row-common cap `sum_r y[a,r]y[b,r] <= 2-overlap(a,b)` added and measured.
#   It is SAT on rook, first-5 srg99 rows, a 32-row stratified sample, and a 16-row sample combined with
#   outside-balance, so it is propagation but not a row filter. Fixed-y residual outside-AN was split
#   into its own oracle; CP-SAT and SciPy/HiGHS MILP both time out on representative 0. Hard subproblem
#   is now localized to the residual outside graph factor with exact label-demand equations.
# R150 ADD: fixed-y residual modular-rank audit. `root_cell_fixed_y_residual_rank.py` forms the exact
#   linear `degree+AN` system after a row-layer `y` witness is fixed. Rook control passes without
#   over-prune, and the R149 representative-0 fixed-y system is consistent modulo 2,3,5,7,1000003
#   (mod 2 rank=aug=889, dim=1596; odd/large rank=aug=903, dim=1582). Therefore modular linear
#   inconsistency is exhausted for this measured fixed-y witness; the next residual-rooted lever must
#   exploit Booleanity and quadratic outside pair/common-neighbour structure. `root_cell_fixed_y_residual_an.py`
#   now infers k from the source reps file and refuses old row-layer outputs without stored y.
# R151 ADD: saturated-pair neighbour-domain audit. For fixed y, tau(a,b)=0 forces x_ab=0 and forbids
#   any outside vertex from being adjacent to both a,b. `root_cell_fixed_y_neighbor_domains.py` checks
#   each outside vertex's residual AN row against this tau=0 independence graph. Rook control passes;
#   R149 representative 0 has pair targets tau=0:82, tau=1:1046, tau=2:1357 and all 71 outside vertex
#   domains are SAT in <0.006s each. Thus the one-vertex saturated-pair screen is exact but too local;
#   a useful fixed-y residual solver must enforce global edge symmetry and exact pair equations.
# R152 ADD: fixed-y row-outside pair equations are linear after the R144 row matching and y are fixed.
#   Added them to `root_cell_fixed_y_residual_rank.py` as `row_outside`. Rook control remains consistent.
#   On R149 representative 0, the combined AN+row_outside system is still consistent but shrinks the
#   odd/large-field affine dimension from 1582 to 1010 (rank 903 -> 1475). Any residual brancher should
#   enforce this R152 linear closure before branching on the quadratic outside-outside pair equations.
# R153 ADD: fixed-y Boolean row-outside layer now implemented in `root_cell_fixed_y_residual_an.py`.
#   Rook fixed-y controls pass under CP-SAT/full-pair and MILP/row-outside. The specific R149
#   representative-0 y witness is refuted exactly by Boolean `AN + row_outside`: CP-SAT INFEASIBLE
#   in 0.0149s and independent HiGHS MILP infeasible on the same 1917-row / 2485-variable system.
#   This kills only that y, not row representative 0. Next rooted row-layer model should choose y and
#   outside edges together with outside AN + row-outside constraints; only integrated UNSAT prunes rows.
# R154 ADD: `root_cell_row_layer_cpsat.py --row-outside` now lifts the row-outside equations into the
#   row-layer model, choosing row matching, y, and outside edges together; rook control SAT. Row 0 with
#   integrated row-outside+paircap is UNKNOWN at 60s, so no row prune. A lazy `--forbid-json` loop
#   generated five distinct row-0 paircap witnesses, and all 5 are killed by the R153 fixed-y Boolean
#   layer with CP-SAT infeasible in 0.014-0.028s and independent MILP infeasible. Treat this as a strong
#   fixed-y filter sample, not a row-level proof.
# R156 ADD: reusable fixed-y infeasibility cores. `root_cell_fixed_y_core.py` extracts CP-SAT assumption
#   cores over z/y truth values from killed fixed-y witnesses; `root_cell_row_layer_cpsat.py
#   --forbid-core-json` consumes them as row-layer nogoods with a source guard. Original R149 row-0
#   witness yields a 75-literal core out of 887 assumptions. A second core-forbidden witness yields a
#   329-literal core with 4 workers / 60s. Feeding one or two cores back still finds new row-0 paircap
#   witnesses, and those witnesses are killed by R153 fixed-y row-outside, so this is a reusable-clause
#   architecture improvement but not row pruning yet.
# R157 ADD: `root_cell_core_learning_loop.py` makes the R156 generate-kill-core cycle one-command and
#   bounded. Seeded with two cores, it generated a row-0 witness, killed it by fixed-y row_outside, and
#   extracted a third 659-literal core. Feeding all three cores back still finds a new row-0 paircap
#   witness in 5.78s, again killed by fixed-y row_outside. Conclusion: core learning is runnable, but
#   blind accumulation of bulky cores is not the next decisive lever; improve core quality or integrated
#   branching instead.
# R158 ADD: fixed-y row_outside kills are already continuous LP infeasible. `root_cell_fixed_y_residual_an.py
#   --backend lp` proves rook control feasible, original R149 row-0 `degree+AN` feasible, but row_outside
#   makes the continuous box LP infeasible; the same LP infeasibility holds for three later row-0
#   core-forbidden witnesses. Thus the obstruction is real linear equations + 0<=x<=1 bounds, not
#   integrality. HiGHS IIS access was probed but returned valid-empty IIS objects; broad group localization
#   was too slow and not accepted as evidence. Next lever: LP/Farkas/IIS-style row_outside cuts, not bulky
#   SAT core accumulation.
# R159 ADD: `root_cell_fixed_y_farkas.py` extracts and exactly checks box-bound Farkas certificates for
#   fixed-y row_outside LP infeasibility. Rook fixed-y control is feasible. The original R149 row-0 fixed-y
#   witness now has a compact exact certificate: 17 active rows all on outside label [8,12], with
#   `m^T b=-7` below the box lower `-5` (gap 2). Later core-forbidden witnesses remain LP-infeasible but
#   did not yield small integer certificates under the conservative extractor, and replaying the 17-row
#   template kills only the original witness. This is proof-grade for one fixed y, not a row prune.
# R160 ADD: fixed-y kills localize to one-outside-vertex residual LPs. `root_cell_fixed_y_farkas.py
#   --scan-outside` keeps only one outside vertex's AN, degree, and row_outside equations (27 rows over
#   the 70 star variables x_ow). Rook local scan has 0 nonoptimal vertices. All 8 measured killed row-0
#   fixed-y witnesses have local infeasible vertices: total 56 nonoptimal one-outside LPs, 35 accepted
#   exact local Farkas certificates. `root_cell_fixed_y_core.py --outside-index` extracts local CP-SAT
#   z/y cores; one R156 local core minimized from 374 to 88 literals and is consumed by the row-layer
#   `--forbid-core-json` path, but row 0 remains SAT under that single core. Next rooted lever is bounded
#   local-core learning or symbolic local-Farkas cuts; still no row prune.
# R161 ADD: `root_cell_core_learning_loop.py --local-core` makes the R160 generate-scan-local-core cycle
#   one-command and bounded. Seeded with the R160 88-literal local core, it generated a row-0 witness,
#   found 9 local LP failures / 7 exact certificates, and extracted a 26-literal minimized local core.
#   Seeded with both local cores, it generated another witness, found 3 local LP failures / 2 exact
#   certificates, and extracted a 172-literal minimized local core. Row 0 remains SAT after three local
#   cores; this is runnable infrastructure and measured steering, not a prune.
# R162 ADD: `root_cell_row_layer_cpsat.py --local-row-outside` now integrates the R160 one-outside
#   residual-star obstruction directly with directed local outside variables (exact AN, degree, and
#   row_outside equations per outside vertex, but no global edge symmetry). Rook control SAT; row 0 is
#   UNKNOWN at 60s, so the first monolithic encoding is not decisive. A bounded local-core continuation
#   learned three more local cores (76, 94, 22 literals); with all six local cores forbidden, row 0 is
#   still SAT in 10.433s and the resulting witness still has 4 local LP failures / 3 exact local Farkas
#   certificates. Next rooted lever: symbolic/semi-symbolic local-Farkas cuts or multi-core-per-witness
#   learning, not unbounded blind core accumulation.
# R163 ADD: `root_cell_fixed_y_farkas.py --rational-denominator-limit` recovers exact local Farkas
#   certificates from small-denominator dual rays.  On the 12-core row-0 witness, integer-only scan had
#   5 local LP failures but only 1 exact certificate; denominator 64 recovered 5/5 exact certificates,
#   while rook control stayed clean.  `root_cell_core_learning_loop.py --local-cores-per-iter` learned
#   nine more exact local cores across bounded runs (final 15), but row 0 still remained SAT in ~8s and
#   the regenerated witness stayed full-LP infeasible.  Verdict: keep rational certificate recovery;
#   de-prioritize blind local-core accumulation unless it becomes a symbolic row-layer inequality.
# R163 CLOUD ADD: the r=3 one-command d11->d12 wrapper advanced exact measured coverage with shards
#   72..73/512 after `s3_slice_harness.py --gate` stayed ALL GREEN.  Shard 72 produced 13098 depth-12
#   children; shard 73 produced 13376; no budget/time/sample flags, and frontier recounts matched.
#   Updated known-shard aggregate `scratchpad\r3_d11_to_d12_shard512_known77_aggregate_r163.json`
#   covers shards `0..73,128,256,384`: 69761/463636 depth-11 parents (15.05%), 1021780 measured
#   depth-12 children, diagnostic scaled N12 ~= 6.7908e6.  Next contiguous pair: 74..75.
# R164 CLOUD ADD: exact r=3 d11->d12 shards 74..75/512 completed with the same one-command wrapper.
#   Shard 74 produced 13341 depth-12 children; shard 75 produced 14089; no budget/time/sample flags,
#   prune counters remained zero, and frontier recounts matched.  Updated known aggregate
#   `scratchpad\r3_d11_to_d12_shard512_known79_aggregate_r164.json` covers shards
#   `0..75,128,256,384`: 71573/463636 depth-11 parents (15.44%), 1049210 measured depth-12 children,
#   diagnostic scaled N12 ~= 6.7966e6.  Next contiguous pair: 76..77.
# R165 CLOUD ADD: exact r=3 d11->d12 shards 76..77/512 completed.  Shard 76 produced 11519 depth-12
#   children; shard 77 produced 13440; no budget/time/sample flags, prune counters remained zero, and
#   frontier recounts matched.  Updated known aggregate
#   `scratchpad\r3_d11_to_d12_shard512_known81_aggregate_r165.json` covers shards
#   `0..77,128,256,384`: 73385/463636 depth-11 parents (15.83%), 1074169 measured depth-12 children,
#   diagnostic scaled N12 ~= 6.7864e6.  Next contiguous pair: 78..79.
# R166 CLOUD ADD: exact r=3 d11->d12 shards 78..79/512 completed.  Shard 78 produced 13908 depth-12
#   children; shard 79 produced 13661; no budget/time/sample flags, prune counters remained zero, and
#   frontier recounts matched.  Updated known aggregate
#   `scratchpad\r3_d11_to_d12_shard512_known83_aggregate_r166.json` covers shards
#   `0..79,128,256,384`: 75197/463636 depth-11 parents (16.22%), 1101738 measured depth-12 children,
#   diagnostic scaled N12 ~= 6.7929e6.  Next contiguous pair: 80..81.
# R167 CLOUD ADD: exact r=3 d11->d12 shards 80..81/512 completed.  Shard 80 produced 13402 depth-12
#   children; shard 81 produced 11488; no budget/time/sample flags, prune counters remained zero, and
#   frontier recounts matched.  Updated known aggregate
#   `scratchpad\r3_d11_to_d12_shard512_known85_aggregate_r167.json` covers shards
#   `0..81,128,256,384`: 77009/463636 depth-11 parents (16.61%), 1126628 measured depth-12 children,
#   diagnostic scaled N12 ~= 6.7829e6.  Next contiguous pair: 82..83.
# R168 ROOTED ADD: `root_cell_row_layer_cpsat.py --farkas-cut-json` now adds exact one-outside
#   Farkas/Benders cuts projected onto row-layer z/y variables.  Five cuts changed row-0 from quick SAT
#   to SAT only after 71.56s; nine cuts alone were UNKNOWN at 120s; fifteen cuts still found SAT in
#   85.66s.  Every regenerated witness remains killed by rational local Farkas and full fixed-y LP.
#   Verdict: real formulation improvement, no row prune.  Next local lever is certificate
#   minimization/canonicalization or pair-local symmetric Farkas, not blind raw-cut accumulation.
# R169 ROOTED ADD: `root_cell_fixed_y_farkas.py --minimize-rows` greedily zeros Farkas multipliers while
#   preserving exact contradictions.  It is sound, but weaker for row-layer pruning: the non-minimized
#   15-cut set found SAT in 85.66s, while the minimized 15-cut set found SAT in 33.35s; the witness was
#   still LP-dead with 7/7 rational local certificates.  Do not prefer naive minimized cuts; use raw
#   certificates unless a propagation-aware minimization objective is developed.
# R170 ROOTED ADD: `root_cell_fixed_y_farkas.py --scan-outside-pairs` found exact pair-local Farkas
#   certificates among outside vertices that are individually locally feasible.  `root_cell_row_layer_cpsat.py`
#   now projects pair/multi-outside Farkas certificates too.  On row 0, 15 one-outside cuts alone found
#   SAT in 85.66s; adding 2 pair-local cuts was UNKNOWN at 240s; adding 6 pair-local cuts was also
#   UNKNOWN at 240s.  This is the strongest rooted-residual pressure so far, but not a prune.
# R171 ROOTED ADD: `root_cell_farkas_orbits.py` canonicalizes pair-local certificates under the
#   fixed-label stabilizer.  Across five pair-scan files, 9 exact pair-only certificates collapse to
#   6 rooted-label orbits, with 3 orbits recurring twice.  This supports template mining, but is not
#   yet a finite obstruction library or a row prune.
# R172 ROOTED ADD: actual row-representative symmetry lifting was implemented and validated in
#   `root_cell_farkas_lift.py` / `root_cell_farkas_lift_single.py`.  Row representative 0 has only
#   16 sound automorphisms inside the 7,680 fixed-label stabilizer; every lifted image is rebuilt
#   against the transformed fixed-y witness and exact integer-checked before emission.  Pair sources:
#   13 exact certificates -> 208 exact lifted images -> 130 one-per-pair cuts.  Single sources:
#   accumulated exact certificates -> 560 exact lifted images -> 46 one-per-outside cuts.  Best row-0
#   bounded run still SAT (59.078s, 13,171 branches) but improves over R168's 194,733 branches.  The
#   residual witness still has 8 fresh exact one-outside certificates, so this is a sound propagation
#   aid/template dataset, NOT a row proof.  Cloud route unchanged: the R43 r=3 45-vtx star-complement
#   measurement remains the decisive one-command path.
# R173 CLOUD ADD: exact r=3 d11->d12 shards 82..83/512 completed through the one-command wrapper.
#   Shard 82 produced 10,532 children (branch 11.6247); shard 83 produced 11,201 children
#   (branch 12.3631).  No budget/time/sample flags, frontier recounts matched, and local/spectral/
#   triangle-split prune counters remain zero.  Updated known aggregate
#   `scratchpad\r3_d11_to_d12_shard512_known87_aggregate_r173.json` covers shards
#   `0..83,128,256,384`: 78,821/463,636 depth-11 parents (17.0006%), 1,148,361 measured depth-12
#   children, diagnostic scaled N12 ~= 6.7548e6.  Stage-B is still not a sound partial-frontier
#   predicate; it applies only to completed 45-vtx H candidates.  Next contiguous pair: 84..85.
# R174 DIAGNOSTIC ADD: `s3_edge_vector_gram_probe.py` now accepts current frontier rows keyed by `k`
#   (older code expected `depth`).  Real controls still pass (`T(7)` rank 6/6, rook9 rank 4/4).
#   On R173 d12 frontiers 82/83 it scans 21,733 rows with 0 negative/rank/upper Gram violations;
#   max ranks are 11 and max largest eigenvalues are 157.2921 / 154.5928 versus the srg99 bound 539.
#   Paired frontier strata have max lambda2 2.604789 and min lambda_min -3.309592.  Verdict: useful
#   diagnostic, far from a current depth-12 prune; do not promote to a gate without deeper evidence.
# R175 STAGE-B ADD: `s3_stageb_columns_cpsat.py` prototypes exact CP-SAT generation of diagonal-valid
#   r=3 CRS columns for `b^T(A_H-3I)^-1 b=-3`.  It matches brute force exactly on the real T(7)
#   control (`nH=15`, 735 columns, OPTIMAL, 0.5272s) and matches brute on current d12 frontier smoke
#   rows (0 columns; partial rows only, no prune).  This is a Stage-B building block, not a terminal
#   solver by itself.
# R176 STAGE-B ADD: the same prototype now adds exact compatibility, a CP-SAT target clique, exact
#   closure, and a real-witness SRG check.  On T(7), CP-SAT found the same 735 diagonal columns, recovered
#   the true six star columns, solved a target-6 compatibility clique in 3.218s, and the selected closed
#   graph verifies as `srg(21,10,5,4)`.  Use this as the current Stage-B readiness gate for terminal
#   45-vtx H' candidates; do NOT use partial d12 rows as Stage-B pruning evidence.
# R177 STAGE-B ADD: CP-SAT compatibility cliques can now enforce exact star-set degree equations:
#   selected column `b` must have reconstructed star-set degree `k-|b|`.  This is safe regularity,
#   not a Stage-A cut.  On T(7), the degree-aware model still closes to `srg(21,10,5,4)`, forces
#   61/735 diagonal-valid columns off, and reduces the target-6 clique solve from 3.218s to 1.6319s.
# R178 STAGE-B ADD: CP-SAT cliques can now also enforce exact X-X common-neighbour equations.  For a
#   selected pair of star columns, common neighbours from H' plus selected star columns must equal
#   lambda or mu according to the reconstructed star-set adjacency.  T(7) remains green; this forces
#   off 9,225 compatible column pairs on the 735-column control and closes to `srg(21,10,5,4)`.
# R179 STAGE-B ADD: CP-SAT now supports full SRG closure equations for terminal H': H-degree, H-H
#   common-neighbour, and H-X common-neighbour equations, in addition to diagonal/compatibility/X-X.
#   T(7) remains green and closes to `srg(21,10,5,4)`; final closure solve is OPTIMAL in 0.4966s
#   with 0 conflicts/branches on the 735-column control.  This is the current terminal Stage-B model
#   to wire into workers; still not valid on partial d12 frontiers.
# R180 STAGE-B INTEGRATION: `s3_slice_harness.py --stageb-demo --stageb-engine auto|cpsat|brute`
#   now routes terminal 45-vtx H' candidates to the R179 full-closure CP-SAT solver (falling back in
#   auto mode if OR-Tools is unavailable).  Partial generated H' candidates remain smoke-only and skip
#   terminal closure constraints.  Harness gate and CP-SAT T(7) self-test remain green.
# R181 STAGE-B VALIDATION: the R179/R180 full-closure model was validated on 12 distinct random r=3
#   star complements of real T(7): 12/12 matched brute diagonal enumeration, recovered true columns,
#   found a full-closure CP-SAT target-6 solution, and verified the selected closure as
#   `srg(21,10,5,4)`.  Diagonal column counts ranged 274..765.  This is strong real-witness gating
#   for Stage-B, not a result about partial srg99 frontiers.
# R182 TERMINAL PRECHECK ADD: `terminal_h_shadow_precheck()` derives cheap H-only necessary conditions
#   from the final closure equations (residual star degrees and H-H residual common-neighbour demands)
#   and is wired before terminal column generation in `s3_slice_harness.py`.  It passes 200/200 sampled
#   real T(7) r=3 star complements.  This is terminal-only unless a separate lookahead theorem is proved;
#   do not apply it to partial d12 frontiers.
# R183 CLOUD ADD: exact r=3 d11->d12 shards 84..85/512 completed through the one-command wrapper.
#   Shard 84 produced 12,969 children (branch 14.315); shard 85 produced 13,347 children
#   (branch 14.732).  No budget/time/sample flags, frontier recounts matched, and local/spectral/
#   triangle-split prune counters remain zero.  Updated known aggregate
#   `scratchpad\r3_d11_to_d12_shard512_known89_aggregate_r183.json` covers shards
#   `0..85,128,256,384`: 80,633/463,636 depth-11 parents (17.3914%), 1,174,677 measured depth-12
#   children, diagnostic scaled N12 ~= 6.7543e6.  Still diagnostic only; next contiguous pair 86..87.
# R184 STAGE-A ADD: pair lower-closure demand is now checked inside `PartialGraph.can_add()`:
#   for every placed pair u,v, `common_P(u,v)+min(14-deg_P(u),14-deg_P(v)) >= lambda_or_mu`.
#   Proof: each future common neighbour consumes one residual degree slot from both endpoints.
#   Validation: synthetic impossible partial fired; rook(9) exhaustive 0/512 violations; T(7) sampled
#   0/5000; BvLS sampled 0/5000; R183 shard-84 and shard-85 d12 frontiers had 0/12969 and 0/13347
#   violations; `s3_slice_harness.py --gate` stayed green; shallow exact d1..d9 counts unchanged.
#   Treat this as a late residual-degree guard, not a current d12 pruning breakthrough.
# R185 STAGE-A ADD: locally-7K2 matching-completion closure is now checked online.  For each placed
#   vertex v, if d=|N_P(v)| and m=current matching edges inside N_P(v), require d-2m <= 14-d; otherwise
#   the current unpaired neighbours cannot be paired using the remaining neighbour slots.  This is a
#   strict strengthening of R37's "N(v) is a partial matching" condition.  Witness validation passed
#   (rook9 exhaustive 0/512, BvLS sampled 0/5000, harness --gate ALL GREEN).  It is monotone under
#   extension.  Measured exact prefix change: old d9 5311 -> new d9 5310; old d10 42430 -> new d10
#   42425; old R90 d11 has 29 dead rows, so corrected N11 is 463607.  Available d12 scans find
#   57/1174677 dead rows across 89 frontier files.  Use R185 frontiers/counts for new exact work.

## 0. Goal / decision the slice would make
R43+ SUPERSESSION NOTE: the current primary route is the eigenvalue-3 star-complement search:
enumerate isomorph-free 45-vertex H' with 3 not an eigenvalue, then solve the 54-column CRS
Stage-B closure.  The older s=-4 / 55-vertex wording immediately below is retained as fallback
history/cross-check context, not the current primary cloud route.
Decide existence of srg(99,14,1,2) by the Aut-AGNOSTIC route: enumerate (isomorph-free) candidate
s=-4 star complements H (55-vtx induced subgraphs with -4 NOT an eigenvalue and the forced spectrum),
and for each H solve the CRS column CSP (find 44 pairwise-compatible 0/1 columns that close to an SRG).
- If some H yields a valid 44-column closure passing full SRG verification -> srg99 EXISTS (construct it).
- If ALL valid H are certified to admit NO valid 44-column set -> srg99 does NOT exist.
- Realistic expectation: PARTIAL — characterize failure categories, measure the true frontier.
  (R30/R33 adversarial note, RE-CONFIRMED at R35 by sampling §5: the dominant cost — abstract 55-vtx
   induced-subgraph generation under local constraints — is comparable to / harder than the paused
   Z3/f=0 cell. The value is the NEW pruning + a clean failure-category map, NOT a guaranteed close.)

================================================================================================
## 1. STAGE A — H-generation. THE ORDERED FILTER PIPELINE (cheapest / highest-prune first).
================================================================================================
A generator must ENFORCE the local (per-extension) predicates inline (kill children at creation),
and apply the global/spectral predicates as terminal or near-terminal rejects. Order = by cost-per-call
ascending AND by prune-power descending; both agree here. EACH filter below is verified-sound on a real
witness (the "calib" column): a real star complement of Kneser/srg40/rook9/BvLS passes it.

LEGEND: [L]=local, O(1)-O(deg) per extension, baked into the augmentation step (ONLINE reject).
        [P]=partial-spectral, O(k^3) eigensolve on the partial graph, ONLINE at depth k>=46 (R35 NEW).
        [G]=global, computed once per COMPLETED H (terminal reject).

 #  TAG  FILTER (predicate)                                          PRUNE (calib)         CALIB WITNESS
 -- ---  ---------------------------------------------------------   -------------------   -------------
 F1 [L]  max degree <= 14 (host is 14-regular)                       weak alone            all
 F2 [L]  locally partial-7K2: N_H(v) induces max degree <= 1         STRONG (see §5)       Kneser/srg40
          (a partial matching). |N_H(v)| <= 14.
 F3 [L]  lambda=1 LOCAL: every edge in <= 1 triangle                 STRONG (see §5)       all (lam=1)
          (<=> |N(u) cap N(v)| <= 1 for every edge uv)
          => triangles edge-disjoint => t(H) <= floor(e(H)/3).
 F4 [L]  mu=2 LOCAL: any two NON-adjacent vtxs share <= 2 common nbrs MODERATE             all (mu=2)
 F5 [L]  degree band (R36 CORRECTED — see CAUTION below):                LOW (subsumed by   all real SCs
          per-vertex  0 <= deg_H(v) <= 14  (hard host cap, = F1).         F1+F6)             (0 over-prune)
          sum band  Sum_v deg_H(v) = 2 e(H) in [308, 638] (e<=319) /
          [308,716] (e<=358, m3=11) / [308,726] (e<=363).  avg deg in
          [5.60, 11.60]..[5.60,13.2].  Cheap online running-sum sanity.
          ** CAUTION (R36, validated on Kneser+srg40): do NOT impose
          deg_H(v) <= 13.  The column-weight floor |b_u| >= 1 is an
          X-SIDE constraint on the 44 X-vertices (=> e(H) <= 363, that
          is F6's top), NOT a per-H-vertex floor.  An H-vertex with
          deg_X(v)=0 (all 14 host-nbrs inside H, deg_H(v)=14) is
          ADMISSIBLE.  A "deg_H<=13 for all v" rule WOULD over-prune a
          real witness — it is unsound.  Keep only 0<=deg_H(v)<=14. **
 F6 [L]  edge band e(H) in [154, 358]  (avg deg 2e/55 in [5.6,13.0]). hard endpoints       (window;
          (R30 triangle-split polytope LOWER 154; R34 m3=11 UPPER 358;                       Kneser e=45
          R31/R32 give 363, R31 strict-count 319 is BINDING if m>=18 —                       in its own
          carry e<=363 as SOFT, e<=319 as the AGGRESSIVE variant, e<=358 HARD.)              scaled band)
 ------ ----- end of ONLINE-CHEAP local block; everything below needs the spectrum --------------------
 F7 [P]  ONLINE CAUCHY-INTERLACING SCHEDULE (R35 NEW, verified §5):                          Kneser real H
          a partial induced subgraph on k vertices is induced in the final 55-vtx H, so       0/720 viol
          by Cauchy interlacing  mult_3(partial_k) >= mult_3(H) - (55 - k) >= 10 - (55-k).
          => at depth k>=46 PRUNE any branch with mult_3(partial_k) < k - 45.
          Schedule: k=46->mult_3>=1, 50->5, 53->8, 54->9, 55->10. Converts the otherwise
          terminal-only spectral gate into an ONLINE reject for the WIDEST last-10 tree levels.
          (Cost: one symmetric eigensolve per node at depth>=46; cheap vs the branching saved.)
          UPPER-WINDOW (R39, verified SOUND, free add): also mult_3(partial_k) <= 66 - k       Kneser/srg40
          [= mult_3(H)_max(=11) + (55-k), from the master 1-deletion interlacing               0 false-rej
          |mult_v(sub)-mult_v(super)|<=t]. Leaf k=55 -> [10,11] = F8(c) exactly. One extra      0 EXTRA prune
          integer compare on the count F7 already has; ZERO added eigensolves. HONEST: its      (both calib)
          MEASURED mid-tree extra prune over F7-lower is 0 in EVERY sampled regime incl.
          adversarial whole-G overshoot (0/37225 srg40, 0/20440 Kneser lower-survivors);
          interlacing-feasible partials undershoot mult_3 (killed by lower) and don't pile
          r-eigs above the lower line until k=nH-1 where F8(c) already fires. Keep as a free
          leaf-tight consistency cross-check, NOT as a wall-shrinker.
 F8b'[P] HEREDITARY PD REJECT (R39 NEW, verified SOUND, fires at EVERY depth k>=1):            Kneser+srg40
          A_H+4I is positive definite (F8(b)); PD is HEREDITARY to induced subgraphs, and       0 false-rej
          every partial_k is induced in the final H, so A_{partial_k}+4I must be PD at ALL      EXHAUSTIVE
          depths. PRUNE any partial_k with lambda_min <= -4 (i.e. A_partial_k+4I NOT PD).       (32767 Kneser
          This is the at-every-depth strengthening of the terminal-only F8(b).                  + 262143 srg40
          IMPL (cheap, online): bordered LDL/Cholesky update. M_{k+1}=[[M_k,r],[r^T,4]];        induced subs,
          solve L y = r (O(k^2) fwd-subst), schur = 4 - sum y_i^2/D_i; parent PD (tree          0 reject;
          invariant) => child PD iff schur > 0. One triangular solve/node, reuse L,D across     min margin
          the tree. Float LDL by default; fall back to exact Fraction LDL on boundary nodes     +0.027/+0.051)
          |schur| < eps (exact form 0-mismatch vs from-scratch PD).
          PRUNE POWER (the REAL lever, measured): on RANDOM local-valid (F1-F6) partials it
          fires k=40 dens.20 60.8% / dens.35 62.5%; k=46 dens.20 100% / dens.35 98.3%;
          k=55 100% all densities; killed 83/200 (41.5%) random local-valid growth paths
          before completion. So F8b' bites ~6-15 levels BELOW F7's k>=46 floor, at near-100%
          on the WIDEST/most-expensive dense levels -- it attacks the spectrum mid-tree, not
          only at the leaf. COMPLEMENTS F7 (does not replace it: F7 catches undershoot, F8b'
          catches the -4 overshoot). SOUNDNESS anchored exhaustively (see test column).
 F8c'[P] HEREDITARY SECOND-EIGENVALUE CAP (R41 NEW, verified SOUND, fires at EVERY depth k>=2):    Kneser+srg40
          srg99 spectrum 14^1, 3^54, (-4)^44 has EXACTLY ONE eigenvalue > 3.  By Cauchy             0 false-rej
          interlacing lambda_2(A_P) <= lambda_2(A_G) = 3 for every induced P, so EVERY induced       ~4.8M EXACT
          subgraph of G (hence every partial_k of H) has AT MOST ONE eigenvalue > 3.                 tests:
          ONLINE REJECT (all depths): PRUNE partial_k if it has >=2 eigenvalues > 3                  rook9 502 exh,
          (i.e. lambda_2(A_partial_k) > 3).  Non-strict: lambda_2 == 3 is ALLOWED (P=H attains it).  Kneser 212418,
          EXACT online form (no float false-reject): #(eig > 3) = #positive eigenvalues of           srg40 4.6M,
          A_P - 3I = #positive pivots of a rational symmetric LDL of (A_P - 3I) [Sylvester           BvLS 3840,
          inertia; 2x2 pivots for zero leading minors].  Cap = host 2nd eigenvalue r (Kneser 1,      + real-SC subs
          srg40 2, srg99 3); independently re-verified this iter (40000 random induced subs/         every depth;
          calibrator: max #(eig>r) = 1, 0 violations).                                               0 reject.
          DISTINCT SPECTRAL REGION (the point): F7 bounds mult OF 3 from below (k>=46); F8b'
          bounds lambda_MIN from below (>-4, BOTTOM); F8c' bounds lambda_2 from above (<=3, TOP/
          2nd eigenvalue) -- a region NOTHING shipped touched.  Together F8b'+F8c' box the whole
          partial spectrum into (-4,3] except the single Perron top in (3,14].
          PRUNE POWER (measured, the win): c'-only kills (lambda_2>3 while lambda_min still >-4,
          i.e. NEW over F8b'): k=40 dens.10 62.5% / k=44 dens.10 93.3% / k=36 dens.15 88.3%.
          ADDITIVE over the FULL shipped block (F1-F6 + F7 + F8b'): of growth paths surviving the
          old block at depth k, F8c' additionally kills k=38 p.10 50.7% / k=42 p.14 99.3% / k=34
          p.20 89.3%.  CRUCIALLY fires at k~34-42 -- 4-12 levels BELOW F8b's dense range and BELOW
          F7's k>=46 floor, moving the spectral kill DOWN-TREE (prunes ~8-16 extra subtree levels).
          The FIRST online cut to bite the TOP of the spectrum mid-tree; a first-order N_A lever.
          COST: O(k^2) bordered-LDL inertia on A_P - 3I, reuses F8b's triangular solve; ~= F8b' cost.
 F8 [G]  SPECTRUM GATE on COMPLETED H (exact integer char-poly, or high-prec eigh + integer-round):
          (a) -4 is NOT an eigenvalue: det(A_H + 4I) != 0          definition of SC          all real SCs
          (b) lambda_min(A_H) > -4 strict (A_H + 4I positive def)  GIVEN by interlacing       all real SCs
          (c) eigenvalue 3 with multiplicity m3 in {10, 11}        FORCED (R32 two-value)     Kneser->{8,9}
              [Cauchy floor 10; over-determination ceiling 11.]                                analog OK
          (d) theta_1 in [2e/55, 14]; ALL eigenvalues in (-4, 14]  Perron+interlace           all real SCs
 F9 [G]  DET DIVISIBILITY: det(A_H + 4I) is a positive integer with 7^10 | det               Kneser 5^8|det
          (>=10 factors of (3+4)=7). Cheap integer GCD check.                                  analog OK
 F10[G]  MODULAR CORANKS (cheap exact rank over a finite field):                              all real SCs
          corank_F2(A_H + I) >= m3 ;  corank_F7(A_H + 4I) >= m3.
 F11[G]  m3 CONSISTENCY (third-moment, the e<=363 mechanism, R31):                            Kneser 0/3000
          6 t(H) > theta_1^3 + 4 theta_1^2 + 63*m3 - 8 e(H).        (used to derive F6 top)    viol
 F12[G]  TRIANGLE-SPLIT POLYTOPE feasibility (R30): with t=t(H), e=e(H):                      (window check;
          b_HHX = e - 3t >= 0 ; c_HXX = 385 - 2e + 3t >= 0 ; d_XXX = e - t - 154 >= 0 ;        no real s=-4
          AND 2 e(H) >= r^2 * m3 * 55 / (55 - m3)  (R34 trace/Cauchy-Schwarz floor;            family witness;
          gives e>=62 at m3=11 — dominated by F6, kept for completeness/cross-check).          calib on synth)

NOTE on ORDER: F1-F6 are O(1)..O(deg) and kill the overwhelming majority of children at creation
(sampling §5: geometric-mean per-extension acceptance ~0.25, i.e. ~75% of naive children die LOCALLY).
F7 + F8b' + F8c' are the mid-depth spectral rejects. F7 (mult_3 lower schedule) bites k>=46; F8b'
(hereditary PD / lambda_min, R39) bites EARLIER (~k>=40 dense, near-100% by k=46); F8c' (hereditary
lambda_2<=3, R41) bites EARLIEST (~k>=34 on sparse/mid partials where a 2nd large eig appears before
lambda_min crashes) -- the three attack the BOTTOM (F8b'), TOP (F8c'), and MIDDLE-mult (F7) of the
partial spectrum, boxing it into (-4,3] save the Perron top, from the widest tree levels down to k~34;
without them the spectrum gate fires ONLY at k=55, after the full tree is built. The F7
upper-window (66-k) is sound+free but contributes 0 measured extra prune (leaf-tight only).
F8-F12 are terminal; F8(c) (m3 in {10,11}) is the dominant TERMINAL rejecter (sampling §5: a random
local-valid 55-graph has mult_3=0 essentially always — the gate is high-codimension and near-total).

------------------------------------------------------------------------------------------------------
R37 IMPLEMENTATION NOTE — EXACT ONLINE FORM of F2/F3/F4 + the COMPLETE minimal forbidden set.
  (Verified: online==full-recheck, 0/20000 mismatches; 0 over-prune on real lambda=1,mu=2 witnesses
   rook9=srg(9,4,1,2) EXHAUSTIVE 511 subgraphs + BvLS243=srg(243,22,1,2) 3000 subgraphs.)
  F2/F3/F4 are PRECISELY equivalent to forbidding three induced subgraphs — this is the WHOLE local set:
        {  K4 ,  diamond (K4 minus an edge) ,  K_{2,3}  }.
  (Every other small forbidden graph — book/butterfly/gem/W4/B2 etc. — already CONTAINS a K4, diamond,
   or K_{2,3}, so running F2+F3+F4 per-vertex/edge/pair is a COMPLETE encoding; no separate list needed.)
  EXACT O(k^2) ONLINE REJECT when augmenting partial H (size k) by vertex w with neighbour set R:
   - degree:  deg(w)=|R|<=14  AND  deg(v)+1<=14 for every v in R;
   - F2 @w :  R induces max-degree <=1 (w's neighbourhood is a partial matching);
   - F2 @v :  for v in R, the (already-present) common-neighbour count C[w-stub via R]<=1 and the single
              prior in-N(v) member had in-N(v) degree 0;
   - F3    :  any EXISTING edge i-j with i,j both in R must have had 0 common neighbours (else w makes a
              2nd triangle on i-j) ;
   - F4    :  (i) for v NOT in R, common(v,w)=|R cap N(v)| <= 2 ;
              (ii) any EXISTING NON-adjacent pair i,j both in R must have had <= 1 common neighbour.
   CAUTION (the non-obvious part, caught by the 0-mismatch gate — a naive "only check w's own pairs"
   online form is WRONG, it had 314 mismatches before the (c)-class existing-pair checks were added):
   adding w changes the common-neighbour count of EVERY pair already inside R, so F3/F4 must re-check
   those existing pairs, not just pairs incident to w.
  DEGREE-STRATIFIED PRUNE (R37, light sampling; fraction of weight-d columns passing the online reject):
        k \ d:   w2    w4    w6    w8   w10   w12  w14
          20    93%   57%   19%  4.8%  0.3%   0%   0%
          40    89%   48%   12%  0.8%  0.1%   0%   0%
          50    88%   44%  9.3%  0.8%   0%    0%   0%
   => HEAVY columns (weight>=10, the COSTLY high-branching extensions) are essentially eliminated at
      large k; light columns (weight<=4) survive freely. This is exactly where Stage-A spends its time,
      so the local block bites hardest on the most expensive branches. (Independent re-measure this iter,
      rougher partials: w8~0.20-0.46, w10~0.04-0.24, w12<=0.09 — same crush of heavy columns.)

GENERATION METHOD (recommend): CANONICAL AUGMENTATION (McKay orderly generation / nauty-Traces
`geng`-style) over 55-vtx graphs with F1-F6 baked into the extension step and F7 as an online reject
at depth >=46. Isomorph rejection at EVERY level (the engineering bar flagged in FINAL_REPORT §5).
DISTRIBUTE by leading-row / first-k-vertex canonical profile (each cloud worker owns a disjoint set of
depth-d canonical prefixes; no shared lease; embarrassingly parallel above the split depth).
  - SEEDING: seed the tree from forced 7K2 / edge-disjoint-triangle fragments (each closed nbhd in the
    HOST is 7K2; H inherits partial-7K2 nbhds). Start the augmentation from a canonical triangle or a
    7K2-fragment rather than the empty graph to cut the shallow levels.
  - EIGENSPACE-FIRST — ASSESSED (R36) and NOT RECOMMENDED as the generation primitive. Measured on the
    real s=-4 graphs: r=3 is a NON-MAIN eigenvalue of every sampled real H (eigenspace _|_ all-ones,
    Kneser 20/20 + srg40 20/20) — which would *suggest* an equitable-partition handle — BUT the coarsest
    equitable partition (WL-1) of real SCs has #cells ~ nH (Kneser 10.9/15, srg40 24.5/25), i.e. the
    high-multiplicity eigenspace does NOT force a small quotient; it is "spread out". And the integer
    m3-subspace U is itself unknown (only its DIM is forced) and must satisfy 7^10|det / corank_F7, so
    eigenspace-first REPLACES "search graphs" with "search subspace U  x  search 0/1 rows in U^perp" — a
    second combinatorial layer with NO canonical-form / iso-rejection machinery (nauty has none for
    subspaces). Net: not cheaper. CORRECT use of the eigenspace = the ONLINE PRUNE F7 (Cauchy schedule +
    lambda_min(partial_k) > -4 PD at every depth), NOT a standalone generator. Default = canonical augmentation.
  - DEGREE-SEQUENCE SHAPING — LOW value (R36). The forced degree band (F5) is subsumed by F1 + F6.
    Crucially, mult_3 = 11 (margin-0) does NOT force a tighter / near-regular degree sequence for srg99:
    Kneser's margin-0 SCs are exactly regular ONLY because their tiny non-r block (nH-m3 = 6) makes the
    trace Cauchy-Schwarz tight (collapse to a 3-eigenvalue/SRG H); srg99's non-r block (44) has huge CS
    slack (e >= 62 vs 154 floor) and admits NO regular 3-eigenvalue solution, and srg40 (non-r block 15)
    has no regular margin-0 SC at all. So degree-sequence regularity is NOT a Stage-A lever — the wall is
    the SPECTRUM (F8(c): 0/120 random local-valid 55-graphs even have an eigenvalue near 3, §5).

SOUNDNESS GATE for Stage A (MUST pass before any scale-up):
  run the SAME generator restricted to 15-vtx with the s=-4 local constraints and confirm it
  (re)produces the Kneser K(7,2) star complements; separately reproduce srg(40,12,2,4) star complements
  and the rook9/BvLS analogs. A generator that DROPS a real star complement is buggy. Mirror
  sc_foundation.py (exact enumeration). The R35 online interlacing schedule F7 was verified to NOT
  over-prune the real Kneser H (0/720 induced-subgraph violations, interlace_online.py).

================================================================================================
## 2. STAGE B — column CSP per accepted H (cheap relative to A; the R31/R32 pruning lives here).
================================================================================================
Inputs per accepted H: C = A_H, M = C + 4I, P = M^-1 (EXACT, via adjugate/det integer arithmetic;
  b^T P b = (b^T adj(M) b)/det(M) — keep integer, compare b^T adj(M) b vs 4*det(M)). W0 = the FULL
  eigenvalue-3 eigenspace of C (dim m3 in {10,11}); PROVEN (R32) B^T W0 = 0 for the WHOLE space (not just
  the Cauchy-forced part), so the prefilter never over-prunes even in the excess m3=11 case.
Steps (in THIS order — the W0 filter goes FIRST):
  (B1) W0-ORTHOGONALITY PRE-FILTER (calib 64.5x on Kneser, codim 8; srg99 codim 10-11 => STRONGER).
       A valid star column b must satisfy w^T b = 0 for every w in W0. Restrict the 0/1-column search to
       the integer points of the cube lying in ker(W0^T) (a subspace of codim m3 >= 10). On Kneser this
       cut alone took 387 diagonal-valid columns to EXACTLY the 6 true ones. Implement as lattice
       enumeration in the subspace, or ILP over {0,1}^55 intersect ker(W0^T).
  (B2) DIAGONAL equation (exact integer): b^T adj(M) b = 4*det(M)  (i.e. b^T P b = 4).
       Column weight |b| = 14 - d_X(u), a free per-column integer in [1,14]; enumerate by weight.
       Sum of all 44 weights = e(X,H) = 770 - 2 e(H)  (R32; verified on 200 Kneser SCs) — at e=358 the
       average column weight is ~1.2 (very sparse columns), at e=154 it is ~10.5 (dense). Use the weight
       histogram as a per-H pre-allocation.
  (B3) COMPATIBILITY clique: edge iff b_u^T P b_v in {0,1} (exact: b_u^T adj(M) b_v in {0, det(M)}).
       Seek a clique of size m_s = 44. MARGIN fact (R31/R32): the 44 columns are linearly independent
       and live in W0^perp of dim 55 - m3 in {44,45}. At m3=11 the columns are a FORCED BASIS (margin 0);
       at m3=10, margin 1. Any 45 mutually-compatible columns are over-determined -> early termination.
       Calib: on EVERY Kneser/rook9 H the max compatible clique = m_s EXACTLY and is UNIQUE.
  (B4) CLOSURE / FULL VERIFY: A_X = -4 I + B^T P B must be a 0/1 symmetric zero-diagonal matrix; assemble
       the full 99x99 A and verify srg(99,14,1,2) parameters EXACTLY (defeat false positives).
       If A_X has ANY non-{0,1} entry under EXACT arithmetic, that is an ARITHMETIC BUG, not a result.
SOUNDNESS GATE for Stage B: on Kneser K(7,2), B1->B4 must recover the unique reconstructing 6-clique;
  on rook9, the unique 4-clique; on srg(40,12,2,4) (a real s=-4 SRG), it MUST reconstruct. A Stage-B that
  fails to reconstruct a real graph is buggy. Mirror calib_crs.py / calib_columns.py / w0_collapse.py /
  sc_foundation.py. (Verified live: FINAL_GATE.py GATE 2/GATE 4 green.)

================================================================================================
## 3. MEASURE THE GOAL, not a proxy (operating-method rule 6) — THIN VERTICAL SLICE go/no-go.
================================================================================================
Hit the end-to-end oracle EARLY with a thin slice BEFORE scaling Stage A.
GO/NO-GO PROTOCOL (run on a SINGLE machine / one small cloud node first):
  STEP 0 (soundness, MUST be green first): run both Stage-A and Stage-B soundness gates (§1,§2) on
    Kneser K(7,2), srg(40,12,2,4), rook9. 0 false rejections, exact reconstruction. If red -> FIX, do
    not proceed.
  STEP 1 (generate a few HUNDRED valid H): produce 200-1000 accepted srg99 star complements H (first by
    canonical order from the seed, or random-restart canonical-augmentation), passing F1-F12. RECORD per
    H: e(H), m3, theta_1, det-7-valuation, column-weight histogram.
  STEP 2 (run Stage B to completion on each): measure |B(H)| (diagonal-valid column count), |B(H) cap
    ker W0^T| (post-prefilter), and the MAX compatible clique size; attempt the 44-clique.
  STEP 3 (READ THE FAILURE CATEGORIES — the deliverable):
     (i)   H rejected at spectrum gate — WHICH sub-gate (-4 present / m3 not in {10,11} / det-7 / corank).
     (ii)  H passes spectrum but the W0-filter EMPTIES some required column-weight class.
     (iii) max compatible clique < 44 — RECORD the actual max. Consistently 43 = a near-miss signal
           worth escalating; consistently << 44 = the CSP is generically infeasible (a soft nonexistence
           signal, NOT a proof).
     (iv)  clique = 44 but closure A_X not 0/1 under EXACT arithmetic — this is a BUG indicator (must be
           ZERO with exact arithmetic); halt and fix, do not log as a result.
     (v)   full closure passes -> CANDIDATE GRAPH -> escalate to hard verify IMMEDIATELY.
GO criterion to scale Stage A: STEP 0 green AND the STEP-3 histogram is dominated by (i)/(iii) with
  sane per-category rates AND no (iv) bugs. NO-GO (re-design before spending cloud budget): any (iv)
  bug; OR the generator is too slow to produce a few hundred H (Stage-A engineering not ready); OR a
  real calib graph is falsely rejected anywhere.
  Only AFTER the histogram is in hand do you scale Stage A. Do NOT optimize the generator before its
  output is characterized. One costly validation run at a time; stop by task id; never blunt-kill.

================================================================================================
## 4. COST MODEL (honest, calibrated; order-of-magnitude).
================================================================================================
DEFINITIONS: Let N_A = number of distinct (isomorph-free) local-valid 55-vtx graphs the generator must
  EXPAND (tree nodes), S = number that survive ALL Stage-A gates (the spectral gate is near-total).
  t_B = per-H Stage-B wall-time. Stage-B core-hours = S * t_B / 3600.

(a) STAGE-A SURVIVING-H COUNT S — the dominant uncertainty.
  - The spectrum gate F8(c) "eigenvalue 3 with multiplicity exactly 10 or 11" is a HIGH-CODIMENSION
    algebraic condition. SAMPLING (§5): across 120 randomly-built local-valid 55-vtx graphs in the
    e-band, the MAX multiplicity of eigenvalue ~3 was 0 — random local-valid graphs essentially NEVER
    satisfy the gate. => S is many orders of magnitude below N_A; S is small in ABSOLUTE terms but
    UNKNOWN without the run (could be 0, could be 10^3-10^6). The honest statement: S is bounded by
    the generated tree, not estimable a priori; the slice (§3) is what measures it.
  - The COST is dominated by N_A (the number of nodes you must walk to find the rare S survivors),
    NOT by S itself. This is the WALL.

(b) STAGE-A NODE COUNT N_A — the single biggest cost driver.
  - No exact count exists for local-valid 55-vtx graphs (avg degree ~5.6-13). Anchors:
    * canonical-augmentation per-extension LOCAL acceptance ~0.25 (geometric mean, §5) — i.e. F1-F6
      kill ~75% of children at creation, a strong but not tree-collapsing cut.
    * the residual branching (number of distinct canonical valid children per node) is what sets N_A;
      for a depth-55 search with even a modest residual branching of ~3-10 the tree is 10^25-10^50
      nodes BRUTE — astronomically infeasible without the spectral+iso pruning doing most of the work.
    * F7 (online interlacing) is the only lever that prunes mid-tree on the SPECTRUM; it bites at
      depth>=46 where the tree is widest, and is the highest-leverage single addition (R35).
  - HONEST ORDER-OF-MAGNITUDE: comparable to / harder than the paused Z3/f=0 a=24 cell (33-row orbit
    backtrack that walls at row 2-8 of 33). Budget Stage A as a REAL distributed-nauty engineering
    project measured in 10^4-10^7+ core-hours, with the true number set by how early F7 + iso-rejection
    collapse the tree — which the §3 slice MUST measure before committing budget. DO NOT quote a single
    number; quote the RANGE and the dependency on N_A.

(c) STAGE-B PER-H COST t_B — cheap; NOT the driver.
  - W0 prefilter (B1) takes diagonal-valid columns (Kneser ~387/H; srg99 expect O(10^2-10^3) before,
    O(10) after the codim-10/11 cut) to a handful; the 44-clique among O(10) compatible columns is
    microseconds; closure+verify is one 99x99 matrix build. t_B ~ 1ms-1s per H.
  - Stage-B core-hours = S * t_B / 3600: even at S=10^6 and t_B=1s this is ~280 core-hours — NEGLIGIBLE
    vs Stage A. Stage B is NOT the bottleneck; it is the cheap confirmer/rejecter.

(d) SINGLE BIGGEST COST DRIVER: STAGE-A generation node-count N_A (isomorph-free 55-vtx enumeration
    under the local constraints). Stage B is sub-1% of total in every scenario. Therefore EVERY further
    optimization dollar goes to (1) pruning the Stage-A tree earlier and (2) the iso-rejection engine.

================================================================================================
## 5. CALIBRATION / SAMPLING EVIDENCE (R35, light compute, this iter).
================================================================================================
  - FINAL_GATE.py (real Kneser K(7,2)): ALL GATES GREEN. GATE 3 interlacing min mult_r = m_r-m_s = 8;
    GATE 4 W0-filter 387 -> 6 = true set (64.5x); GATE 6 m3 edge cut first-excluded e=364 -> e<=363;
    GATE 7 m3 inequality 0 violations.
  - prune_estimate.py: per-extension LOCAL-filter acceptance (F2/F3/F4 on random degree-d additions)
    measured 0.18-0.39 across partial sizes |V|=10..50; geometric mean ~0.25. F1-F6 are real per-node
    cuts but do NOT collapse a depth-55 tree alone.
  - spectral_rarity.py: 120 random local-valid 55-vtx graphs in the e-band -> MAX mult of eigenvalue~3
    = 0; 0% satisfy the F8(c) gate. CONFIRMS the spectral gate is high-codimension / near-total terminal
    rejecter, and CANNOT be satisfied by random post-filtering -> motivates F7 (online interlacing) and
    structural/eigenspace-first generation. This is also WHY Stage A is the wall.
  - interlace_online.py: the F7 Cauchy-interlacing schedule verified on the REAL Kneser star complement
    (induced k-subgraphs, k=10..14): required mult_r(H_k) >= mult_r(H) - (15-k) holds with 0/720
    violations -> F7 is SOUND (no over-prune of a real witness).
  All scripts in scratchpad/ (prune_estimate.py, spectral_rarity.py, interlace_online.py) +
  .work/99graph/FINAL_GATE.py.

================================================================================================
## 6. SINGLE HIGHEST-LEVERAGE FURTHER-TIGHTENING TO CHASE NEXT.
================================================================================================
  ---- R39 STATUS of the three "full interlacing envelope" sub-items (all VERIFIED, see F7/F8b' above):
    (1) two-sided mult_3 window [k-45, 66-k]: DONE. SOUND (0 false-reject both sides, exhaustive on
        calib SCs) but 0 MEASURED extra prune over F7-lower (overshoot doesn't occur in interlacing-
        feasible partials until k=nH-1, where F8(c) already fires). Shipped as a free leaf-tight
        consistency cross-check; NOT a wall-shrinker. -- CLOSED.
    (2) hereditary lambda_min>-4 PD at every depth: DONE = F8b'. SOUND (0 false-reject, exhaustive
        32767 Kneser + 262143 srg40 induced subs, exact Sylvester minors) AND has REAL mid-tree prune
        (fires k>=40 dense, near-100% by k=46, 41.5% of random growth paths). This is the genuine
        win from this round. -- SHIPPED as F8b'.
    (3) det-7-valuation / corank_F7 growth schedule below k=46: HONEST NO. The only forced mechanism
        gives corank_F7(A_P+4I) >= mult_3(P) and v_7(det) >= mult_3(P), but mult_3(P) >= max(0,k-45)
        is EXACTLY F7 -> reduces to F7, fires no earlier. Any excess corank is graph-structural, not
        forced (verified: srg40 p=2 min real corank is non-monotone and DROPS BELOW the interlacing
        floor -> a corank schedule would OVER-PRUNE reals; srg40 p=3 is a constant +4 plateau, prime-
        specific, not growing). No sound monotone partial analog exists. -- CLOSED (no new predicate).

  ---- R40 RESOLUTION of the "hybrid local-spectral interior mult_3 lower bound" (was the #1 chase):
    (4) SOUND ONLINE INTERIOR mult_3 LOWER bound g(k, e_k, t_k) that beats k-45 for k in [38,46]:
        >>> HONEST NO -- the forced-moment route is STRUCTURALLY VOID.  g(k,e,t) = 0 identically. <<<
        WHAT WAS ASKED: given a k-vtx graph with e_k edges, t_k triangles, all eigenvalues in (-4,14],
        trace 0, how SMALL can mult of EXACTLY-3 be?  ANSWER (proven): it can be 0 for every reachable
        (k,e,t).  The three forced power-sum moments (p1=tr A=0, p2=tr A^2=2e, p3=tr A^3=6t) plus the
        eigenvalue range carry NO lower-bound information on mult_3, because r=3 is a single interior
        point and the support interval (-4,14] contains points on BOTH sides of 3, so a finite
        quadrature avoiding 3 can match any 3 moments -> a 0-mass-at-3 measure ALWAYS exists -> the
        moment-LP min-mass-at-3 = 0.  This is the LP-duality dual of the KNOWN fact (R34/F12) that the
        same Cauchy-Schwarz only bounds m3 from ABOVE (piling mass at r is low-variance):
        inverting 2e >= 9*m3*nH/(nH-m3) gives m3 <= 2e*k/(2e+9k), an UPPER bound, never a lower one.
        Adding the 4th moment m4 does NOT rescue it (a 0-mass-at-r measure still exists; tk_moment_*).
        PROOF STRENGTH: grid-free + EXACT.  partA_srg99_exact.py sweeps the ENTIRE reachable (k,e,t)
        box at the srg99 params (r=3, range (-4,14]) for k in [38,46] and exhibits, with EXACT
        rational arithmetic, an explicit nonneg rational measure with ZERO mass at 3 matching
        (m1,m2,m3) for 0 FAILURES in the reachable band (e>=2.8k; the only library-misses are the
        unreachable e<<2.8k near-empty corner, and those too are LP-feasible -- partA_exact_void.py).
        SOUNDNESS (the §1 gate): g=0 trivially never false-rejects; conversely g never EXCEEDS the
        true mult_3 of any real partial (g_real_validate.py: 0 over-rejects on 1664 Kneser + 2015 srg40
        induced subgraphs at every depth, incl. the 2051 that genuinely contain eigenvalue r).
        CONSEQUENCE: the mid-tree gap below k=46 is REAL but UNCLOSABLE by any forced-moment online
        predicate.  The low interior mult_3 of real partials is driven by the lambda=1/mu=2 LOCAL
        structure (already F2/F3/F4), which is NOT a power-sum-moment fact.  The spectral wall IS
        interlacing-tight mid-tree for everything online + sound.  -- CLOSED (no new predicate).
        Scripts: .work/99graph/scratchpad/{partA_exact_void.py, partA_srg99_exact.py, g_void_proof.py,
        g_real_validate.py, g_why_void_and_r34_invert.py, tk_moment_derive.py}.

  ---- R40 WILDCARD: any 5/6-vtx induced subgraph FORBIDDEN in srg99 beyond {K4, diamond, K_{2,3}}?
        >>> HONEST NONE.  The shipped local set is COMPLETE for 5- and 6-vertex forbidden subgraphs. <<<
        Method (forcing, not sampling): the ONLY forcing an induced subgraph can witness is the pairwise
        common-neighbour cap (<=lambda=1 on edges, <=mu=2 on non-edges) = F2/F3/F4, whose complete
        minimal set is {K4, diamond, K_{2,3}} (R37).  The next-order rule -- "the 2 common nbrs of a
        non-adjacent pair must be NON-adjacent" (else that edge lies in 2 triangles, violating lambda=1)
        -- was the candidate for something NEW.  PROVEN SUBSUMED: this rule (call it B2) fires IFF the
        graph CONTAINS AN INDUCED DIAMOND (partB_supplement.py: 0 mismatches between "B2 fires" and
        "has induced diamond" over ALL 64 + 1024 + 32768 labelled graphs on n=4,5,6).  The 2 adjacent
        common nbrs w1,w2 of a non-edge {u,v} together with u,v induce exactly a diamond -- already
        shipped.  The locally-7K2 neighbourhood constraint reduces to F2 (N(v) induces max-degree <=1).
        CENSUS CONFIRM (partB_forbidden_census.py / partB_census_fast.py): of all non-iso graphs --
        n=5: 34 = 13 shipped-forbidden + 21 realised in a real lambda=1/mu=2 or s=-4 host + 0 NEW;
        n=6: 156 = 94 shipped-forbidden + 59 realised + 3 sample-absent (no rule fires; NOT forbidden)
        + 0 NEW forced-forbidden.  The load-bearing number (NEW forced-forbidden) is 0 at both sizes.
        => DO NOT add any forbidden subgraph to F2-F4; the set is complete through 6 vertices.

  ---- R41 THE GENUINE NEW ONLINE WIN this round: F8c' (hereditary lambda_2 <= 3 cap, shipped above).
      It is the FIRST sound online cut to attack the TOP of the spectrum mid-tree (k~34-42), a region
      F7 (mult-of-3 lower) and F8b' (lambda_min lower) never touched.  With F8c' shipped, F8b'+F8c'
      now box the whole partial spectrum into (-4,3] save the single Perron top, at EVERY depth.

  >>> NEXT LEVER: the remaining mid-tree N_A is interlacing-tight / structural.  After F8c', no further
      reduction is available from a forced-moment or forced-spectral ONLINE predicate (all such veins
      closed -- see EXHAUSTION CALL).  Any further win must be STRUCTURAL: adopt eigenspace-first
      generation (build H from a candidate integer 10/11-dim 3-eigenspace lattice) so the spectral gate
      is satisfied BY CONSTRUCTION rather than by rejection -- only after a vein-B demonstration that it
      beats canonical augmentation on calib.  (R36 assessed eigenspace-first and did NOT recommend it as
      the primitive; it remains the only lever left now that F7/F8b'/F8c'/moment-lower/forbidden-census
      are all closed.)

  >>> EXHAUSTION CALL (R40/R41): online Stage-A pruning is now LARGELY EXHAUSTED.  Every online-sound
      vein has been driven to a verdict: F2-F4 (local; forbidden set {K4,diamond,K_{2,3}} proven
      COMPLETE through 6 vtx this round), F7 (interlacing mult-of-3 lower+upper window), F8b' (hereditary
      PD / lambda_min, the R39 mid-tree win), F8c' (hereditary lambda_2<=3 / TOP, the R41 NEW mid-tree
      win), moment-lower g (VOID -- proven grid-free exact at the srg99 params), det-7/corank schedule
      (reduces to F7).  The three spectral handles now cover BOTTOM (F8b'), TOP (F8c'), and MIDDLE-mult
      (F7) of the partial spectrum.  The residual mid-tree gap (k in [38,46], real interior mult_3 slack
      6-13 below the F7 floor) is provably NOT closable by any forced-moment / forced-spectral online
      predicate -- it is driven by lambda=1/mu=2 LOCAL structure already enforced, and is interlacing-
      tight for anything spectral.  RECOMMENDATION: the Stage-A online filter pipeline is READY -- ADD
      F8c' to the generator, then run the §3 thin vertical slice on one cloud node to MEASURE N_A / the
      failure-category histogram (the dominant remaining uncertainty), and only then decide eigenspace-
      first vs scale.  Do NOT spend more effort hunting online sound cuts.

================================================================================================
## 7. ALTERNATIVE / PRIMARY FORMULATION — the r=3 (45-VERTEX) STAR COMPLEMENT  [R43, this iter]
================================================================================================
PREMISE (verified this iter): the star-complement method (Cvetkovic-Rowlinson-Simic) works for ANY
eigenvalue, not just s=-4.  srg99 spectrum 14^1, 3^54, (-4)^44.  The SHIPPED §1-§6 spec uses the
eigenvalue-(-4) star complement => |H| = 99 - mult(-4) = 99 - 44 = 55 vtx, star set 44.  Eigenvalue 3
has multiplicity 54, so ITS star complement has |H'| = 99 - 54 = **45 vtx**, star set **54**.  Since the
Stage-A generation tree depth = #vertices in the star complement and tree size ~ b^depth (b = residual
canonical branching), a 45-vtx Stage-A is ~ b^-10 the size of the 55-vtx Stage-A -- 3 to 10 ORDERS OF
MAGNITUDE smaller for any plausible b in [3,10].  Stage-B grows (54 columns vs 44) but Stage-B is <1%
of total cost (§4d), and its W0-prefilter gets STRONGER (codim 54 vs 44).  => r=3 is the cheaper
Stage-A.  VALIDATED on real graphs; scripts in scratchpad/ (s3_starcomp_assess.py, s3_pd_vs_psd_crux.py,
s3_density_stageB.py).  This section is the r=3 Stage-A pipeline; run it as the PRIMARY Stage-A (or run
both and keep whichever the §3 slice shows cheaper -- they share the verified §1 local block verbatim).

--- 7.0  CRS RECONSTRUCTION for r=3 (CONFIRMED EXACT on a real r=3 graph).
  A star complement H' for eigenvalue mu=3 is a 45-vtx INDUCED subgraph of srg99 with 3 NOT an
  eigenvalue of A(H').  Reconstruct the star set X (54 vtx) by:
        A_X = 3 I + B^T (A_{H'} - 3 I)^{-1} B          [CRS general form, mu=3]
  where C = A_{H'} (45x45), B is 45 x 54 (H' rows, star-set columns, 0/1 adjacency).
  diag(B^T (C-3I)^{-1} B) = -mu = -3 ; off-diagonals in {0,1} (= A_X adjacency).
  VERIFIED EXACT (Fraction arithmetic) on the REAL r=3 graph T(7)=L(K_7)=srg(21,10,5,4), spectrum
  10^1, 3^6, (-2)^14 (eigenvalue 3 present, mult 6): A_X = 3I + B^T(C-3I)^{-1}B reconstructs the host
  EXACTLY on 150/150 sampled r=3 star-complement partitions (diag=-3, offdiag in {0,1}, 0 mismatch).
  [s3_starcomp_assess.py P1c.]  T(7) is the natural calibrator: r=3 is its SECOND eigenvalue (10 then 3),
  exactly as in srg99 (14 then 3), so #eig>3 = 1 in both -- the F8c' geometry transfers.

--- 7.1  STAGE-A LOCAL BLOCK (F1-F6) -- IDENTICAL, REUSED VERBATIM.
  H' is induced in srg99 exactly as H is, so the LOCAL structure is the SAME: locally-7K2, lambda=1,
  mu=2, max-deg<=14, complete minimal forbidden set {K4, diamond, K_{2,3}}, the R37 exact O(k^2) online
  F2/F3/F4 reject, the R37 degree-stratified heavy-column crush.  F1-F6 are EIGENVALUE-AGNOSTIC (they
  depend only on H' being an induced subgraph of srg99, not on which eigenvalue's SC it is).  COPY THEM
  UNCHANGED.  Only the edge-band ENDPOINTS rescale to 45 vtx (degree-sum identity below).

  EDGE BAND for H' (45 vtx, host 14-regular):  degree-sum identity  14*45 = 630 = 2 e(H') + e(X,H')
  => e(X,H') = 630 - 2 e(H') = SUM of the 54 column weights (>= 0 forces e(H') <= 315 = host cap 7*45).
  LOWER endpoint (R46, implemented): the R30 triangle-split nonneg polytope scaled to 45 vtx. If
  t=#HHH triangles, then T2=e-3t, T1=315-2e+3t, T0=e-t-84 are real triangle-class counts, hence all
  nonnegative. In particular e(H')>=84. Use the safe partial precheck "current e + max future edges
  can still reach a final e_f with t_f>=current_t, t_f<=e_f/3, and t_f<=e_f-84" and the exact terminal
  class-count gate at k=45. This precheck deliberately ignores upper bounds on future triangle creation,
  so it may under-prune but cannot over-prune.
  Real-SC density CHECK (s3_density_stageB.py): r=3 and s=-4 star complements have essentially the SAME
  density (0.497 vs 0.503 on the 21-vtx calibrators) -> residual branching b is COMPARABLE; the 55->45
  depth drop is the dominant cost lever, NOT offset by a denser tree.

--- 7.2  STAGE-A SPECTRAL GATES for r=3 (re-derived; the gates CHANGE -- this is the load-bearing part).
  srg99 eigenvalues sorted DESC: 14 (x1), 3 (x54), -4 (x44).  For an r=3 star complement:

  (G-a) lambda_min(H') >= -4  HEREDITARY, but only PSD not PD.  srg99 has NO eigenvalue < -4, so by
        Cauchy interlacing every induced subgraph (hence every partial of H') has lambda_min >= -4.
        H' EXCLUDES eigenvalue 3, NOT -4, so -4 CAN be an eigenvalue of H' => the bound is >= -4 and may
        be ATTAINED (A_{H'}+4I is PSD, possibly singular -- NOT necessarily PD).  ONLINE GATE: PRUNE any
        partial_k with lambda_min < -4 STRICT (bordered-LDL inertia on A_P+4I, reuse §1 F8b' machinery
        but accept the zero pivot).  This is WEAKER than the s=-4 F8b' (which is PD, lambda_min > -4
        strict, sound because the s=-4 H *by definition* has -4 not an eigenvalue).
        *** QUANTIFIED LOSS (the honest cost of switching, MEASURED s3_pd_vs_psd_crux.py): the gap
        between PD-reject and PSD-reject = induced subgraphs attaining lambda_min == host_min exactly.
        On BOTH real s=-4 graphs (rook9, Kneser) this fraction is 0% for ALL small/mid sizes and only
        climbs (8% -> 34% -> 100%) at sizes >= n - mult(s) + 1 = the STAR-COMPLEMENT SIZE band, i.e. it
        is a LEAF phenomenon.  => F8b's extra bite over PSD/interlacing is concentrated at the leaf, NOT
        mid-tree, so the PD->PSD weakening costs ~0 mid-tree prune.  The r=3 bottom gate is materially
        as strong as s=-4's mid-tree.  This is WHY the 10-fewer-levels saving is NOT eaten by the gate. ***

  (G-b) #eigenvalues > 3  <= 1   HEREDITARY (= F8c', IDENTICAL predicate).  srg99 has exactly ONE
        eigenvalue (14) > 3, so lambda_2(A_P) <= 3 for every induced P.  This is the SAME gate as the
        shipped F8c' and fires the SAME way regardless of which eigenvalue we star-complement (it is a
        TOP-of-spectrum fact about the host, not about the SC).  Online exact form: #(eig>3) = #positive
        pivots of rational LDL of (A_P - 3I).  VERIFIED 0 false-reject on 6842 real induced subgraphs of
        T(7) (s3_starcomp_assess.py P4).  CARRY OVER UNCHANGED.

  (G-c) mult_3(H') = 0  BY DEFINITION of an r=3 star complement (3 is NOT an eigenvalue of H').  This
        REPLACES the s=-4 F7 (mult_3 LOWER schedule that forced 3 UP to the leaf).  The hereditary
        interlacing window for mult_3 of a partial of H' is mult_3(partial_k) <= 0 + (45 - k) = 45 - k
        (UPPER side; lower side is 0, vacuous).  This bites only near the leaf (k close to 45).  NOTE the
        s=-4 F7 also only bit at k>=46 (the last ~9 of 55 levels) -- which the 45-vtx tree NEVER REACHES
        -- so LOSING F7 costs the r=3 search nothing it would have used (F7 lived above the 45 ceiling).
        TERMINAL form: at the completed H' verify mult_3(H')==0 (det(A_{H'}-3I) != 0), the DEFINING gate.

  (G-d) det / divisibility at the special prime: r=3 == s=-4 == 3 (mod 7) (srg99's special prime, r-s=7).
        For H' the analog of F9 is on det(A_{H'} - 3 I) (eigenvalue-3 SC) rather than det(A_H + 4I).
        Carry as a terminal exact-integer cross-check; not load-bearing for Stage A.

  ORDERED r=3 PIPELINE (cheapest/highest-prune first), depth-45 tree:
     F1-F6  [L]  IDENTICAL local block (deg<=14, locally-7K2, lambda=1/mu=2, forbidden {K4,diamond,
                 K_{2,3}}, edge band via 630 = 2e(H')+e(X,H')).  Kills ~75%/extension (§5, unchanged).
     G-b    [P]  hereditary lambda_2 <= 3 (= F8c', the shared TOP gate) -- fires EARLIEST (k~34-42),
                 the strongest mid-tree spectral cut, carries over verbatim.
     G-a    [P]  hereditary lambda_min >= -4 PSD (strict-undershoot reject) -- fires k>=40 dense, ~same
                 as s=-4's F8b' mid-tree (the PD/PSD gap is leaf-only, measured).
     G-c    [P]  mult_3(partial_k) <= 45 - k (leaf-tight UPPER window) + TERMINAL mult_3(H')==0.
     terminal: det(A_{H'}-3I)!=0 ; #eig>3 ==1 ; lambda_min in (-4 inclusive ..14] ; G-d 7-divisibility.

--- 7.3  STAGE-B for r=3 (54-column CSP; bigger but still <1% of cost, and the prefilter is STRONGER).
  Per accepted H': C = A_{H'}, M = C - 3I, P = M^{-1} (exact adjugate/det).  W0 = the eigenvalue-3
  eigenspace of C... NO: for an r=3 SC, 3 is NOT an eigenvalue of H'; the relevant orthogonality space
  is the host's 3-eigenspace restricted to X.  The Stage-B steps mirror §2 with mu=3:
    (B1) W0-ORTHOGONALITY PREFILTER: a valid star column b satisfies b^T P b = -mu = -3 and the 54
         columns span W0^perp of dim 99 - 54 = 45.  CODIM of the orthogonality cut is mult_3 = 54
         (vs 44 for s=-4) => the prefilter is STRONGER (higher codim removes more of the 0/1 cube).
    (B2) DIAGONAL: b^T adj(M) b = -3 * det(M)  (i.e. b^T P b = -3).  Enumerate columns by weight
         = #nbrs in H', sum of 54 weights = e(X,H') = 630 - 2 e(H').
    (B3) COMPATIBILITY clique of size m_s = 54: edge iff b_u^T P b_v in {0,1}.  At margin the 54 columns
         are linearly independent in W0^perp (dim 45)... NOTE 54 > 45, so the columns are NOT all
         independent -- this is the structural difference from s=-4 (44 cols in dim 44/45, a near-basis).
         The 54 columns over-determine the 45-dim space => MORE internal linear relations to exploit as
         early-termination, but ALSO a larger clique target.  (This is the one place r=3 Stage-B is
         genuinely harder; still microseconds-to-seconds per H', cf §4c, S * t_B negligible.)
    (B4) CLOSURE: A_X = 3I + B^T P B must be 0/1 symmetric zero-diagonal; assemble 99x99 A, verify SRG.
  SOUNDNESS GATE for r=3 Stage B: on T(7) (real r=3 graph) B1->B4 must recover the star set EXACTLY;
  the §7.0 CRS test already confirms the closure A_X = 3I + B^T(C-3I)^{-1}B reconstructs T(7) exactly.

--- 7.4  SWITCH RECOMMENDATION (honest, quantified).
  >>> RUN r=3 (45-vtx) AS THE PRIMARY Stage-A.  Expected N_A reduction ~ b^-10 (3-10 ORDERS of
      magnitude for residual branching b in [3,10]); the single biggest cost driver (§4d) is exactly
      this tree, so this is the largest available win on the dominant cost -- larger than any online
      sound cut found in R35-R42. <<<
  WHY it is (near-)free of downside, point by point (all MEASURED this iter):
    1. Depth 45 vs 55: tree ~ b^-10 smaller.  STRUCTURAL, certain.
    2. Local block F1-F6: IDENTICAL (eigenvalue-agnostic) -> zero re-derivation, reuse the verified
       R37 online forms verbatim.  Real-SC density is the same (0.497 vs 0.503) -> b comparable.
    3. Top spectral gate G-b == F8c': IDENTICAL, the strongest mid-tree cut, carries over.
    4. Bottom gate G-a: PD->PSD weakening costs ~0 mid-tree (the PD/PSD gap is a LEAF phenomenon,
       0% mid-tree on both real s=-4 graphs).
    5. Lost F7 (mult_3 lower schedule): lived at k>=46, ABOVE the 45-vtx ceiling -> never reachable
       by the r=3 tree -> losing it costs nothing.
    6. Stage-B: 54 cols vs 44, the over-determined clique (54 in dim 45) is the one harder piece, but
       Stage B is <1% of total (§4d) and the W0 prefilter codim RISES 44->54 (stronger).
  CAVEAT (honest): the SHIPPED s=-4 pipeline is fully soundness-gated on real graphs (R30-R42); the r=3
  spectral gates are re-derived and validated this iter (CRS exact 150/150 on T(7); G-a/G-b 0 false-
  reject on 6842 real induced subgraphs) but the r=3 STAGE-A GENERATOR has not yet been run end-to-end
  on a calibrator.  THEREFORE: keep the s=-4 §1-§6 as the verified fallback, and the §3 thin-slice STEP 0
  soundness gate MUST be re-run for r=3 (reproduce a real r=3 SRG's star complements at 15-vtx on T(7),
  and reconstruct via §7.0) BEFORE scaling.  Net: r=3 is the recommended PRIMARY for the N_A win; s=-4
  stays as the calibrated cross-check.  If the §3 slice is run for BOTH at small scale, keep whichever
  measures cheaper -- but the structural prior strongly favors r=3 (45 < 55).

================================================================================================
## 8. TURNKEY HARNESS + CLOUD RUN COMMAND  [R44 + R45 repair + R48/R49 distribution -- the r=3 thin-slice instrument]
================================================================================================
BUILT + VALIDATED + R45-REPAIRED: .work/99graph/s3_slice_harness.py  (numpy + python-igraph BLISS;
pysat/cadical optional for the column CSP; sympy for the exact soundness reconstruction).  ONE command.
IMPORTANT R45 CORRECTION: the decisive Stage-A measurement starts UNSEEDED from one vertex. A forced
triangle root is not proved sound for every possible r=3 star complement, so `--seed-triangle` is
diagnostic only and MUST NOT be used for the decisive cloud measurement.

WHAT IT IS (implements §7 end-to-end):
  - Stage-A: LEVEL-COMPLETE canonical-augmentation generator for 45-vtx induced-subgraph
    candidates H', with igraph BLISS canonical_permutation isomorph rejection at EVERY depth,
    the §1 local block F1-F6 baked into the extension step (EXACT R37 online K4/diamond/K_{2,3}
    reject, incl. the existing-pair re-check), and the §7.2 spectral gates online:
    G-b (#eig>3 <= 1, = F8c'), G-a (lambda_min >= -4 PSD), G-c (mult_3 window 45-k), edge band,
    the R184 pair lower-closure residual-degree demand, the R185 neighbourhood matching-completion
    closure, plus the R46 terminal triangle-split gate (e>=84 and T2/T1/T0 nonnegative at k=45).
    R48 ADD: exact frontier JSONL save/load and deterministic shard continuation via a canonical-parent
    ownership rule, so distributed prefix workers do not double-count isomorphic children across shards.
    R49 ADD: `--stats-out` writes machine-readable run records and `s3_aggregate_shards.py` combines
    shard sets only when their metadata proves they are compatible and exact.
    R50 ADD: canonical-parent ownership is cached by child canonical key and evaluated after the ordinary
    child BLISS duplicate check. This preserves exact shard ownership while avoiding repeated deletion
    BLISS work on isomorphic children.
    Spectral gates use float eigh online with an EXACT integer-inertia (rational LDL, 2x2 pivots
    for singular minors) fallback on small/boundary depths.  Instruments the iso-free NODE COUNT
    per depth => the residual branching b (the only unknown behind the b^-10 magnitude).
  - Stage-B: per completed H', the r=3 column CSP -- M=A_{H'}-3I, P=M^{-1} EXACT; diagonal
    eqn b^T P b = -3, compatibility b_u^T P b_v in {0,1}, clique target = star set, exact 0/1
    closure A_X = 3I + B^T P B.  Backtrack clique by default; cadical (pysat) SAT cross-check.
  - bounded by --node-budget / --time-cap / --level-cap.

SOUNDNESS GATE (the correctness proof, runs in seconds, ALL GREEN after R45 repair):
  first validates the ACTUAL local generation predicates on a real lambda=1,mu=2 witness:
    rook(9)=srg(9,4,1,2) replay through `PartialGraph.can_add` accepts all 9! vertex orders
    (362,880/362,880); the incremental triangle counter matches exact rook(9) t=6; the srg99 r=3
    spectral gates reject 0/511 nonempty rook(9) induced subgraphs; the triangle-split identities
    match the actual split on all 512 rook(9) vertex subsets. This is the no-overprune gate for F1-F6
    + the srg99-threshold spectral code and a real-witness check for the R46 triangle-split algebra.
    R184 ADD: the pair lower-closure probe separately validates this residual-degree demand on rook(9)
    exhaustive subsets, T(7) and BvLS sampled subsets, and current R183 d12 frontier rows before it is
    used inside `PartialGraph.can_add()`.
    R185 ADD: the neighbourhood matching-completion probe separately validates the stronger locally-7K2
    completion condition on rook(9) exhaustive subsets and BvLS samples, then `--gate` confirms the
    integrated online form still accepts every rook(9) insertion order.
  then reconstructs the REAL r=3 graph T(7)=L(K_7)=srg(21,10,5,4) end-to-end:
    DIAGONAL b^T P b=-3 (6/6 true cols) | COMPAT matches true A_X | CLOSURE A_X exact 0/1 |
    BLIND column search 735 diagonal-valid cols, all 6 true recovered | backtrack clique = 6
    (=star set) | SAT (cadical195) clique = 6 closes 0/1 | Stage-A gates 0 false-reject over
    5242 real induced subgraphs of T(7) (G-a, G-b both 0).  => the harness is CORRECT.

MEASURED AFTER R45/R47 REPAIR (bounded UNSEEDED local slices, srg99 r=3):
  best local command run:
    `python s3_slice_harness.py --slice --node-budget 150000 --time-cap 120 --target-depth 12 --level-cap 2000`
  complete iso-free counts through clean levels: depth 1..9 = 1,2,4,9,21,62,208,916,5311.
  Clean-level residual branching b=2.922; deepest clean children/node at depth 8->9 = 5.798.
  Level cap is applied after the complete depth-9 count; later levels are sampled-frontier counts,
  not full N_d. No spectral prune yet; `pruned_triangle_split=0` at shallow depth, as expected for
  a near-leaf/terminal gate.
  Shallow projection from depth 9 gives total Stage-A N_A ~ 4.68e20 (LARGE).  HONEST: this is still only
  the unpruned shallow regime and branching is still rising; G-a/G-b should bite only at k~34-46, so the
  decisive unknown remains the DEEP spectral prune. The older triangle-seeded b~3.7 was a diagnostic
  subslice only, not a sound decisive N_A measurement. Do NOT quote any shallow extrapolation as final
  feasibility. `--time-cap` is a soft between-level cap so complete level counts are not corrupted by
  mid-level interruption.

R48 DISTRIBUTED FRONTIER VALIDATION:
  naive modulo sharding was tested and found UNSAFE before the fix: two depth-5 shards produced 58+54
  depth-6 children versus the true 62, because different parents can generate isomorphic children.
  The harness now uses canonical-parent ownership (child accepted only from the lexicographically least
  BLISS key among its vertex-deleted parents). Verified:
    - direct complete depth 7 remains N1..N7 = 1,2,4,9,21,62,208;
    - full resume from a saved complete depth-5 frontier gives depth 6=62 and depth 7=208;
    - two shards recombine exactly: depth 6 -> 39+23=62, depth 7 -> 125+83=208.
  A complete depth-9 frontier was written locally with 5311 reps:
    `python s3_slice_harness.py --slice --target-depth 9 --node-budget 20000 --time-cap 60 --level-cap 10000 --frontier-out scratchpad\r3_frontier_d9_test.jsonl`
  Use only R48+ frontier files for exact distributed totals; older naive shard files are diagnostic only.

R49 JSON/AGGREGATE VALIDATION:
  `--stats-out PATH` writes `r3_slice_stats_v1` records for root or shard runs. The record carries
  parameters, source frontier SHA-256 and metadata, node counts by depth, sampled-level flags, branching,
  prune counters, and completed count.
  `s3_aggregate_shards.py` writes `r3_shard_aggregate_v1` and refuses unsafe aggregation: seeded
  diagnostic slices, duplicate/missing shards, mixed target depths, mixed source hashes, or a source
  frontier without `canonical_parent=true`.
  Verified locally:
    - root stats aggregate through depth 7 matched exactly 1,2,4,9,21,62,208;
    - two depth-5 shards aggregated from JSON to exact depth counts 5=21, 6=62, 7=208;
    - aggregate JSON marks all three depths exact and records the source frontier SHA-256
      `5f4ed0a21e05dc2fcf1a11104ea363be1b349f2ef2a91104ae4f57873ac07a4c`.

R50 OWNER-CACHE VALIDATION:
  The canonical-parent owner key is invariant over each child isomorphism class, so the generator now
  computes the child BLISS key first, skips already-accepted duplicates before ownership, and caches
  `child_key -> owner_key` per level. This changes only evaluation order, not the ownership predicate.
  Verified locally:
    - `--gate` still ALL GREEN after the change;
    - root aggregate through depth 8 matched exactly 1,2,4,9,21,62,208,916;
    - optimized depth-5 shards still aggregate exactly to 5=21, 6=62, 7=208.
  Small local timing evidence: root depth 7 went 0.59s -> 0.40s; depth-5 shard0 to d7 went
  0.37s -> 0.24s; shard1 went 0.21s -> 0.15s. Treat these as small-run evidence only, not a deep
  cloud scaling proof.

R51 CURRENT PREFIX ARTIFACT:
  R50-optimized complete depth-9 frontier regenerated:
    `python s3_slice_harness.py --slice --target-depth 9 --node-budget 20000 --time-cap 120 --level-cap 10000 --frontier-out scratchpad\r3_frontier_d9_r50.jsonl --stats-out scratchpad\r3_frontier_d9_stats_r50.json`
  Result: exact `N1..N9=1,2,4,9,21,62,208,916,5311`, wall=20.22s, frontier count 5311,
  `frontier_complete=True`, `canonical_parent_cache_hit=37055`. Aggregate proof:
  `scratchpad\r3_frontier_d9_aggregate_r50.json` marks depths 1..9 exact.
  Use `scratchpad\r3_frontier_d9_r50.jsonl` as the current local prefix artifact for shard smoke tests;
  on cloud, regenerate the same frontier in the run directory before launching workers.

R52 CHAINED DEPTH-10 ARTIFACT:
  Full-scope resume metadata fixed: when `--frontier-in` uses a complete source frontier with
  `--shard-count 1`, a complete continuation now writes `frontier_complete=true` and records
  `frontier_complete_for_loaded_scope` plus `source_frontier_complete`. True shard outputs remain
  non-global and must still be aggregated.
  Exact depth-10 continuation from the R51 frontier:
    `python s3_slice_harness.py --slice --frontier-in scratchpad\r3_frontier_d9_r50.jsonl --shard-count 1 --shard-index 0 --target-depth 10 --node-budget 100000 --time-cap 300 --level-cap 100000 --frontier-out scratchpad\r3_frontier_d10_r52.jsonl --stats-out scratchpad\r3_frontier_d10_stats_r52.json`
  Result: exact `N9=5311`, `N10=42430`, wall=181.47s, frontier count 42430,
  `canonical_parent_cache_hit=262936`, no local/spectral/triangle prunes. Aggregate proof:
  `scratchpad\r3_frontier_d10_aggregate_r52.json` marks depths 9 and 10 exact. The older ~41k local
  sampled note is not a certified full `N10`; use 42430.

R53 DEPTH-10 -> DEPTH-11 SHARD PILOT:
  Four deterministic 1/64 shards from `scratchpad\r3_frontier_d10_r52.jsonl` completed:
    shard0: 663 parents -> 7818 children, wall 53.56s;
    shard1: 663 -> 7260, wall 54.46s;
    shard2: 663 -> 6930, wall 53.87s;
    shard3: 663 -> 7159, wall 54.14s.
  Combined diagnostic aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_03_aggregate_r53.json`
  Coverage: 2652/42430 depth-10 parents = 6.2503%; depth-11 pilot children 29167; weighted branching
  10.997; diagnostic scaled estimate `N11 ~ 466650`. This is a sizing estimate only, not a certified
  full count. To certify exact `N11`, run all 64 shard indexes and aggregate without `--allow-incomplete`.
  No local/spectral/triangle prunes fired in the pilot.

R54 RESUMABLE SHARD RUNNER:
  `s3_run_shards.py` is a foreground wrapper around `s3_slice_harness.py` and `s3_aggregate_shards.py`.
  It runs finite shard index sets, writes one stats JSON per shard, skips completed shard JSON on rerun,
  and aggregates the selected stats. It does not implement graph generation or pruning.
  Verified:
    `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 4-5 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --tag r3_d10_to_d11_shard64_runner_r54 --aggregate-out scratchpad\r3_d10_to_d11_shard64_04_05_runner_aggregate_r54.json --allow-incomplete`
  ran shards 4 and 5, then a rerun skipped both existing stats files and regenerated only the aggregate.
  New shard results: shard4 663->7392, shard5 663->7473. Combined shards 0..5 now cover 3978/42430
  parents, produce 44032 depth-11 children, weighted branching 11.069, diagnostic scaled `N11 ~ 469653`.

R55 CURRENT D10->D11 CERTIFICATION PROGRESS:
  Additional runner shards completed: shard6 663->6745, wall 56.26s; shard7 663->7881, wall 54.82s.
  Combined diagnostic aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_07_aggregate_r55.json`
  Coverage: 5304/42430 depth-10 parents = 12.5006%; depth-11 pilot children 58658; weighted branching
  11.059; diagnostic scaled `N11 ~ 469242`. Rows are still diagnostic, not exact. Prune counters across
  all 8 shards remain zero.

R56 CURRENT D10->D11 CERTIFICATION PROGRESS:
  Fresh validation before extending: `python -m py_compile s3_slice_harness.py s3_aggregate_shards.py
  s3_run_shards.py` passed and `python s3_slice_harness.py --gate` was ALL GREEN.
  Additional runner shards completed: shard8 663->7680, wall 54.47s; shard9 663->7721, wall 53.85s.
  Combined diagnostic aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_09_aggregate_r56.json`
  Coverage: 6630/42430 depth-10 parents = 15.6257%; depth-11 pilot children 74059; weighted branching
  11.170; diagnostic scaled `N11 ~ 473955`. Rows are still diagnostic, not exact. No budget/time/sample
  flags; prune counters across all 10 shards remain zero. Exact N11 still requires shards 10..63 and an
  aggregate without `--allow-incomplete`.

R57 CURRENT D10->D11 CERTIFICATION PROGRESS:
  Additional runner shards completed: shard10 663->6632, wall 54.45s; shard11 663->7264, wall 52.70s.
  Combined diagnostic aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_11_aggregate_r57.json`
  Coverage: 7956/42430 depth-10 parents = 18.7509%; depth-11 pilot children 87955; weighted branching
  11.055; diagnostic scaled `N11 ~ 469071`. Rows are still diagnostic, not exact. No budget/time/sample
  flags; prune counters across all 12 shards remain zero. Exact N11 still requires shards 12..63 and an
  aggregate without `--allow-incomplete`.

R58 CHAINABLE FRONTIER WORKFLOW:
  `s3_run_shards.py --frontier-out-dir DIR` now passes `--frontier-out` to each shard and skips a shard
  only when both the stats JSON and requested frontier JSONL are present. `s3_merge_frontiers.py` consumes
  the stats JSON files, reuses the strict aggregate compatibility checks, verifies each frontier header
  and graph-row count/depth, and writes a merged `frontier_complete=true` JSONL only when the full target
  depth is exact. Validation on the known depth-5 two-shard split:
    runner with `--frontier-out-dir scratchpad\merge_test` reproduced exact 5=21,6=62;
    `python s3_merge_frontiers.py ... --out scratchpad\merge_test\r3_frontier_d6_merged.jsonl` wrote
    62 rows at depth 6;
    continuing from the merged frontier reproduced exact 6=62,7=208;
    a one-shard merge was refused as incomplete.
  For future d10->d11 runs, prefer writing frontiers from the start; the existing R53-R57 stats-only
  shard results are valid count evidence but do not by themselves form a chainable depth-11 frontier.

R59 CURRENT D10->D11 CERTIFICATION PROGRESS WITH FRONTIER OUTPUT:
  Additional chainable runner shards completed:
    `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 12-13 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r59 --aggregate-out scratchpad\r3_d10_to_d11_shard64_12_13_chain_aggregate_r59.json --allow-incomplete`
  Shard12: 663->7196, wall 56.32s; shard13: 663->6795, wall 54.47s. Both wrote depth-11 frontier
  JSONL files whose headers are local-scope complete (`frontier_complete_for_loaded_scope=true`) but
  globally incomplete (`frontier_complete=false`, as expected for 64-way shards), with row counts
  matching stats.
  Combined diagnostic aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_13_aggregate_r59.json`
  Coverage: 9282/42430 depth-10 parents = 21.8760%; depth-11 pilot children 101946; weighted branching
  10.983; diagnostic scaled `N11 ~ 466017`. Rows are still diagnostic, not exact. No budget/time/sample
  flags; prune counters across all 14 counted shards remain zero. Exact N11 still requires shards 14..63
  for counts, and a chainable merged d11 frontier also requires frontier outputs for every shard
  (including rerunning or regenerating shards 0..11 with `--frontier-out-dir`).

R60 CURRENT D10->D11 CERTIFICATION PROGRESS WITH FRONTIER OUTPUT:
  Additional chainable runner shards completed:
    `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 14-15 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r60 --aggregate-out scratchpad\r3_d10_to_d11_shard64_14_15_chain_aggregate_r60.json --allow-incomplete`
  Shard14: 663->7706, wall 54.59s; shard15: 663->6867, wall 59.81s. Both wrote depth-11 frontier
  JSONL files with row counts matching stats.
  Combined diagnostic aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_15_aggregate_r60.json`
  Coverage: 10608/42430 depth-10 parents = 25.0012%; depth-11 pilot children 116519; weighted branching
  10.984; diagnostic scaled `N11 ~ 466054`. Rows are still diagnostic, not exact. No budget/time/sample
  flags; prune counters across all 16 counted shards remain zero. Exact N11 still requires shards 16..63
  for counts, and a chainable merged d11 frontier still requires frontier outputs for shards 0..11 as
  well as 16..63.

R61 CURRENT D10->D11 CERTIFICATION PROGRESS WITH FRONTIER OUTPUT:
  Additional chainable runner shards completed:
    `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 16-17 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r61 --aggregate-out scratchpad\r3_d10_to_d11_shard64_16_17_chain_aggregate_r61.json --allow-incomplete`
  Shard16: 663->7738, wall 56.00s; shard17: 663->7909, wall 57.31s. Both wrote depth-11 frontier
  JSONL files with row counts matching stats.
  Combined diagnostic aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_17_aggregate_r61.json`
  Coverage: 11934/42430 depth-10 parents = 28.1263%; depth-11 pilot children 132166; weighted branching
  11.075; diagnostic scaled `N11 ~ 469901`. Rows are still diagnostic, not exact. No budget/time/sample
  flags; prune counters across all 18 counted shards remain zero. Exact N11 still requires shards 18..63
  for counts, and a chainable merged d11 frontier still requires frontier outputs for shards 0..11 as
  well as 18..63.

R62 CURRENT D10->D11 CERTIFICATION PROGRESS WITH FRONTIER OUTPUT:
  Additional chainable runner shards completed:
    `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 18-19 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r62 --aggregate-out scratchpad\r3_d10_to_d11_shard64_18_19_chain_aggregate_r62.json --allow-incomplete`
  Shard18: 663->6027, wall 57.30s; shard19: 663->6775, wall 56.32s. Both wrote depth-11 frontier
  JSONL files with row counts matching stats.
  Combined diagnostic aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_19_aggregate_r62.json`
  Coverage: 13260/42430 depth-10 parents = 31.2515%; depth-11 pilot children 144968; weighted branching
  10.933; diagnostic scaled `N11 ~ 463876`. Rows are still diagnostic, not exact. No budget/time/sample
  flags; prune counters across all 20 counted shards remain zero. Exact N11 still requires shards 20..63
  for counts, and a chainable merged d11 frontier still requires frontier outputs for shards 0..11 as
  well as 20..63.

R63 CURRENT D10->D11 CERTIFICATION PROGRESS WITH FRONTIER OUTPUT:
  Additional chainable runner shards completed:
    `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 20-21 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r63 --aggregate-out scratchpad\r3_d10_to_d11_shard64_20_21_chain_aggregate_r63.json --allow-incomplete`
  Shard20: 663->6815, wall 54.84s; shard21: 663->7332, wall 55.12s. Both wrote depth-11 frontier
  JSONL files with row counts matching stats.
  Combined diagnostic aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_21_aggregate_r63.json`
  Coverage: 14586/42430 depth-10 parents = 34.3766%; depth-11 pilot children 159115; weighted branching
  10.908; diagnostic scaled `N11 ~ 462858`. Rows are still diagnostic, not exact. No budget/time/sample
  flags; prune counters across all 22 counted shards remain zero. Exact N11 still requires shards 22..63
  for counts, and a chainable merged d11 frontier still requires frontier outputs for shards 0..11 as
  well as 22..63.

R64 CURRENT D10->D11 CERTIFICATION PROGRESS WITH FRONTIER OUTPUT:
  Additional chainable runner shards completed:
    `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 22-23 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r64 --aggregate-out scratchpad\r3_d10_to_d11_shard64_22_23_chain_aggregate_r64.json --allow-incomplete`
  Shard22: 663->6441, wall 67.33s; shard23: 663->6238, wall 67.54s. Both wrote depth-11 frontier
  JSONL files with row counts matching stats.
  Combined diagnostic aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_23_aggregate_r64.json`
  Coverage: 15912/42430 depth-10 parents = 37.5018%; depth-11 pilot children 171794; weighted branching
  10.797; diagnostic scaled `N11 ~ 458096`. Rows are still diagnostic, not exact. No budget/time/sample
  flags; prune counters across all 24 counted shards remain zero. Exact N11 still requires shards 24..63
  for counts, and a chainable merged d11 frontier still requires frontier outputs for shards 0..11 as
  well as 24..63.

R65 CURRENT D10->D11 CERTIFICATION PROGRESS WITH FRONTIER OUTPUT:
  Additional chainable runner shards completed:
    `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 24-25 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r65 --aggregate-out scratchpad\r3_d10_to_d11_shard64_24_25_chain_aggregate_r65.json --allow-incomplete`
  Shard24: 663->6628, wall 68.17s; shard25: 663->8007, wall 57.49s. Both wrote depth-11 frontier
  JSONL files with row counts matching stats.
  Combined diagnostic aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_25_aggregate_r65.json`
  Coverage: 17238/42430 depth-10 parents = 40.6269%; depth-11 pilot children 186429; weighted branching
  10.815; diagnostic scaled `N11 ~ 458881`. Rows are still diagnostic, not exact. No budget/time/sample
  flags; prune counters across all 26 counted shards remain zero. Exact N11 still requires shards 26..63
  for counts, and a chainable merged d11 frontier still requires frontier outputs for shards 0..11 as
  well as 26..63.

R66 CURRENT D10->D11 CERTIFICATION PROGRESS WITH FRONTIER OUTPUT:
  Additional chainable runner shards completed:
    `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 26-27 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r66 --aggregate-out scratchpad\r3_d10_to_d11_shard64_26_27_chain_aggregate_r66.json --allow-incomplete`
  Shard26: 663->7374, wall 54.92s; shard27: 663->7260, wall 54.08s. Both wrote depth-11 frontier
  JSONL files with row counts matching stats.
  Combined diagnostic aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_27_aggregate_r66.json`
  Coverage: 18564/42430 depth-10 parents = 43.7521%; depth-11 pilot children 201063; weighted branching
  10.831; diagnostic scaled `N11 ~ 459551`. Rows are still diagnostic, not exact. No budget/time/sample
  flags; prune counters across all 28 counted shards remain zero. Exact N11 still requires shards 28..63
  for counts, and a chainable merged d11 frontier still requires frontier outputs for shards 0..11 as
  well as 28..63.

R67 CURRENT D10->D11 CERTIFICATION PROGRESS WITH FRONTIER OUTPUT:
  Additional chainable runner shards completed:
    `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 28-29 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r67 --aggregate-out scratchpad\r3_d10_to_d11_shard64_28_29_chain_aggregate_r67.json --allow-incomplete`
  Shard28: 663->7632, wall 54.09s; shard29: 663->7745, wall 54.48s. Both wrote depth-11 frontier
  JSONL files with row counts matching stats.
  Combined diagnostic aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_29_aggregate_r67.json`
  Coverage: 19890/42430 depth-10 parents = 46.8772%; depth-11 pilot children 216440; weighted branching
  10.882; diagnostic scaled `N11 ~ 461717`. Rows are still diagnostic, not exact. No budget/time/sample
  flags; prune counters across all 30 counted shards remain zero. Exact N11 still requires shards 30..63
  for counts, and a chainable merged d11 frontier still requires frontier outputs for shards 0..11 as
  well as 30..63.

R68 CURRENT D10->D11 CERTIFICATION PROGRESS WITH FRONTIER OUTPUT:
  Additional chainable runner shards completed:
    `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 30-31 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r68 --aggregate-out scratchpad\r3_d10_to_d11_shard64_30_31_chain_aggregate_r68.json --allow-incomplete`
  Shard30: 663->6689, wall 53.93s; shard31: 663->6825, wall 54.19s. Both wrote depth-11 frontier
  JSONL files with row counts matching stats.
  Combined diagnostic aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_31_aggregate_r68.json`
  Coverage: 21216/42430 depth-10 parents = 50.0024%; depth-11 pilot children 229954; weighted branching
  10.838; diagnostic scaled `N11 ~ 459886`. Rows are still diagnostic, not exact. No budget/time/sample
  flags; prune counters across all 32 counted shards remain zero. Exact N11 still requires shards 32..63
  for counts, and a chainable merged d11 frontier still requires frontier outputs for shards 0..11 as
  well as 32..63.

R69 CURRENT D10->D11 CERTIFICATION PROGRESS WITH FRONTIER OUTPUT:
  Additional chainable runner shards completed:
    `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 32-33 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r69 --aggregate-out scratchpad\r3_d10_to_d11_shard64_32_33_chain_aggregate_r69.json --allow-incomplete`
  Shard32: 663->6725, wall 54.58s; shard33: 663->7181, wall 53.49s. Both wrote depth-11 frontier
  JSONL files with row counts matching stats.
  Combined diagnostic aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_33_aggregate_r69.json`
  Coverage: 22542/42430 depth-10 parents = 53.1275%; depth-11 pilot children 243860; weighted branching
  10.818; diagnostic scaled `N11 ~ 459009`. Rows are still diagnostic, not exact. No budget/time/sample
  flags; prune counters across all 34 counted shards remain zero. Exact N11 still requires shards 34..63
  for counts, and a chainable merged d11 frontier still requires frontier outputs for shards 0..11 as
  well as 34..63.

R70 CURRENT D10->D11 CERTIFICATION PROGRESS WITH FRONTIER OUTPUT:
  Additional chainable runner shards completed:
    `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 34-35 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r70 --aggregate-out scratchpad\r3_d10_to_d11_shard64_34_35_chain_aggregate_r70.json --allow-incomplete`
  Shard34: 663->7051, wall 53.35s; shard35: 663->6691, wall 53.57s. Both wrote depth-11 frontier
  JSONL files with row counts matching stats.
  Combined diagnostic aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_35_aggregate_r70.json`
  Coverage: 23868/42430 depth-10 parents = 56.2527%; depth-11 pilot children 257602; weighted branching
  10.793; diagnostic scaled `N11 ~ 457938`. Rows are still diagnostic, not exact. No budget/time/sample
  flags; prune counters across all 36 counted shards remain zero. Exact N11 still requires shards 36..63
  for counts, and a chainable merged d11 frontier still requires frontier outputs for shards 0..11 as
  well as 36..63.

R71 CURRENT D10->D11 CERTIFICATION PROGRESS WITH FRONTIER OUTPUT:
  Additional chainable runner shards completed:
    `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 36-37 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r71 --aggregate-out scratchpad\r3_d10_to_d11_shard64_36_37_chain_aggregate_r71.json --allow-incomplete`
  Shard36: 663->6665, wall 54.92s; shard37: 663->6399, wall 54.64s. Both wrote depth-11 frontier
  JSONL files with row counts matching stats.
  Combined diagnostic aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r71_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_37_aggregate_r71.json`
  Coverage: 25194/42430 depth-10 parents = 59.3778%; depth-11 pilot children 270666; weighted branching
  10.743; diagnostic scaled `N11 ~ 455837`. Rows are still diagnostic, not exact. No budget/time/sample
  flags; prune counters across all 38 counted shards remain zero. Exact N11 still requires shards 38..63
  for counts, and a chainable merged d11 frontier still requires frontier outputs for shards 0..11 as
  well as 38..63.

R72 CURRENT D10->D11 CERTIFICATION PROGRESS WITH FRONTIER OUTPUT:
  Additional chainable runner shards completed:
    `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 38-39 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r72 --aggregate-out scratchpad\r3_d10_to_d11_shard64_38_39_chain_aggregate_r72.json --allow-incomplete`
  Shard38: 663->6589, wall 53.44s; shard39: 663->7913, wall 54.14s. Both wrote depth-11 frontier
  JSONL files with row counts matching stats.
  Combined diagnostic aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r71_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r72_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_39_aggregate_r72.json`
  Coverage: 26520/42430 depth-10 parents = 62.5029%; depth-11 pilot children 285168; weighted branching
  10.753; diagnostic scaled `N11 ~ 456247`. Rows are still diagnostic, not exact. No budget/time/sample
  flags; prune counters across all 40 counted shards remain zero. Exact N11 still requires shards 40..63
  for counts, and a chainable merged d11 frontier still requires frontier outputs for shards 0..11 as
  well as 40..63.

R73 CURRENT D10->D11 CERTIFICATION PROGRESS WITH FRONTIER OUTPUT:
  Additional chainable runner shards completed:
    `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 40-41 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r73 --aggregate-out scratchpad\r3_d10_to_d11_shard64_40_41_chain_aggregate_r73.json --allow-incomplete`
  Shard40: 663->7075, wall 54.50s; shard41: 663->7809, wall 54.65s. Both wrote depth-11 frontier
  JSONL files with row counts matching stats.
  Combined diagnostic aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r71_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r72_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r73_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_41_aggregate_r73.json`
  Coverage: 27846/42430 depth-10 parents = 65.6281%; depth-11 pilot children 300052; weighted branching
  10.775; diagnostic scaled `N11 ~ 457201`. Rows are still diagnostic, not exact. No budget/time/sample
  flags; prune counters across all 42 counted shards remain zero. Exact N11 still requires shards 42..63
  for counts, and a chainable merged d11 frontier still requires frontier outputs for shards 0..11 as
  well as 42..63.

R74 CURRENT D10->D11 CERTIFICATION PROGRESS WITH FRONTIER OUTPUT:
  Additional chainable runner shards completed:
    `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 42-43 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r74 --aggregate-out scratchpad\r3_d10_to_d11_shard64_42_43_chain_aggregate_r74.json --allow-incomplete`
  Shard42: 663->7519, wall 55.64s; shard43: 663->7082, wall 54.91s. Both wrote depth-11 frontier
  JSONL files with row counts matching stats.
  Combined diagnostic aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r71_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r72_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r73_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r74_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_43_aggregate_r74.json`
  Coverage: 29172/42430 depth-10 parents = 68.7532%; depth-11 pilot children 314653; weighted branching
  10.786; diagnostic scaled `N11 ~ 457656`. Rows are still diagnostic, not exact. No budget/time/sample
  flags; prune counters across all 44 counted shards remain zero. Exact N11 still requires shards 44..63
  for counts, and a chainable merged d11 frontier still requires frontier outputs for shards 0..11 as
  well as 44..63.

R75 CURRENT D10->D11 CERTIFICATION PROGRESS WITH FRONTIER OUTPUT:
  Additional chainable runner shards completed:
    `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 44-45 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r75 --aggregate-out scratchpad\r3_d10_to_d11_shard64_44_45_chain_aggregate_r75.json --allow-incomplete`
  Shard44: 663->6840, wall 54.55s; shard45: 663->7721, wall 54.29s. Both wrote depth-11 frontier
  JSONL files with row counts matching stats.
  Combined diagnostic aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r71_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r72_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r73_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r74_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r75_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_45_aggregate_r75.json`
  Coverage: 30498/42430 depth-10 parents = 71.8784%; depth-11 pilot children 329214; weighted branching
  10.795; diagnostic scaled `N11 ~ 458015`. Rows are still diagnostic, not exact. No budget/time/sample
  flags; prune counters across all 46 counted shards remain zero. Exact N11 still requires shards 46..63
  for counts, and a chainable merged d11 frontier still requires frontier outputs for shards 0..11 as
  well as 46..63.

R76 CURRENT D10->D11 CERTIFICATION PROGRESS WITH FRONTIER OUTPUT:
  Additional chainable runner shards completed:
    `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 46-47 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r76 --aggregate-out scratchpad\r3_d10_to_d11_shard64_46_47_chain_aggregate_r76.json --allow-incomplete`
  Shard46: 663->7894, wall 54.79s; shard47: 663->7325, wall 54.75s. Both wrote depth-11 frontier
  JSONL files with row counts matching stats.
  Combined diagnostic aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r71_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r72_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r73_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r74_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r75_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r76_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_47_aggregate_r76.json`
  Coverage: 31824/42430 depth-10 parents = 75.0035%; depth-11 pilot children 344433; weighted branching
  10.823; diagnostic scaled `N11 ~ 459222`. Rows are still diagnostic, not exact. No budget/time/sample
  flags; prune counters across all 48 counted shards remain zero. Exact N11 still requires shards 48..63
  for counts, and a chainable merged d11 frontier still requires frontier outputs for shards 0..11 as
  well as 48..63.

R77 CURRENT D10->D11 CERTIFICATION PROGRESS WITH FRONTIER OUTPUT:
  Additional chainable runner shards completed:
    `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 48-49 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r77 --aggregate-out scratchpad\r3_d10_to_d11_shard64_48_49_chain_aggregate_r77.json --allow-incomplete`
  Shard48: 663->6635, wall 53.45s; shard49: 663->7602, wall 54.73s. Both wrote depth-11 frontier
  JSONL files with row counts matching stats.
  Combined diagnostic aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r71_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r72_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r73_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r74_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r75_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r76_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r77_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_49_aggregate_r77.json`
  Coverage: 33150/42430 depth-10 parents = 78.1287%; depth-11 pilot children 358670; weighted branching
  10.820; diagnostic scaled `N11 ~ 459076`. Rows are still diagnostic, not exact. No budget/time/sample
  flags; prune counters across all 50 counted shards remain zero. Exact N11 still requires shards 50..63
  for counts, and a chainable merged d11 frontier still requires frontier outputs for shards 0..11 as
  well as 50..63.

R78 CURRENT D10->D11 CERTIFICATION PROGRESS WITH FRONTIER OUTPUT:
  Additional chainable runner shards completed:
    `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 50-51 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r78 --aggregate-out scratchpad\r3_d10_to_d11_shard64_50_51_chain_aggregate_r78.json --allow-incomplete`
  Shard50: 663->7969, wall 56.36s; shard51: 663->6983, wall 55.96s. Both wrote depth-11 frontier
  JSONL files with row counts matching stats.
  Combined diagnostic aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r71_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r72_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r73_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r74_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r75_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r76_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r77_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r78_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_51_aggregate_r78.json`
  Coverage: 34476/42430 depth-10 parents = 81.2538%; depth-11 pilot children 373622; weighted branching
  10.837; diagnostic scaled `N11 ~ 459821`. Rows are still diagnostic, not exact. No budget/time/sample
  flags; prune counters across all 52 counted shards remain zero. Exact N11 still requires shards 52..63
  for counts, and a chainable merged d11 frontier still requires frontier outputs for shards 0..11 as
  well as 52..63.

R79 CURRENT D10->D11 CERTIFICATION PROGRESS WITH FRONTIER OUTPUT:
  Additional chainable runner shards completed:
    `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 52-53 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r79 --aggregate-out scratchpad\r3_d10_to_d11_shard64_52_53_chain_aggregate_r79.json --allow-incomplete`
  Shard52: 663->8216, wall 54.96s; shard53: 663->7781, wall 54.24s. Both wrote depth-11 frontier
  JSONL files with row counts matching stats.
  Combined diagnostic aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r71_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r72_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r73_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r74_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r75_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r76_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r77_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r78_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r79_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_53_aggregate_r79.json`
  Coverage: 35802/42430 depth-10 parents = 84.3790%; depth-11 pilot children 389619; weighted branching
  10.883; diagnostic scaled `N11 ~ 461749`. Rows are still diagnostic, not exact. No budget/time/sample
  flags; prune counters across all 54 counted shards remain zero. Exact N11 still requires shards 54..63
  for counts, and a chainable merged d11 frontier still requires frontier outputs for shards 0..11 as
  well as 54..63.

R80 CURRENT D10->D11 CERTIFICATION PROGRESS WITH FRONTIER OUTPUT:
  Additional chainable runner shards completed:
    `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 54-55 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r80 --aggregate-out scratchpad\r3_d10_to_d11_shard64_54_55_chain_aggregate_r80.json --allow-incomplete`
  Shard54: 663->7990, wall 54.63s; shard55: 663->8010, wall 53.45s. Both wrote depth-11 frontier
  JSONL files with row counts matching stats.
  Combined diagnostic aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r71_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r72_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r73_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r74_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r75_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r76_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r77_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r78_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r79_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r80_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_55_aggregate_r80.json`
  Coverage: 37128/42430 depth-10 parents = 87.5041%; depth-11 pilot children 405619; weighted branching
  10.925; diagnostic scaled `N11 ~ 463543`. Rows are still diagnostic, not exact. No budget/time/sample
  flags; prune counters across all 56 counted shards remain zero. Exact N11 still requires shards 56..63
  for counts, and a chainable merged d11 frontier still requires frontier outputs for shards 0..11 as
  well as 56..63.

R81 CURRENT D10->D11 CERTIFICATION PROGRESS WITH FRONTIER OUTPUT:
  Additional chainable runner shards completed:
    `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 56-57 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r81 --aggregate-out scratchpad\r3_d10_to_d11_shard64_56_57_chain_aggregate_r81.json --allow-incomplete`
  Shard56: 663->7978, wall 54.91s; shard57: 663->7032, wall 55.66s. Both wrote depth-11 frontier
  JSONL files with row counts matching stats.
  Combined diagnostic aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r71_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r72_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r73_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r74_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r75_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r76_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r77_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r78_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r79_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r80_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r81_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_57_aggregate_r81.json`
  Coverage: 38454/42430 depth-10 parents = 90.6293%; depth-11 pilot children 420629; weighted branching
  10.938; diagnostic scaled `N11 ~ 464120`. Rows are still diagnostic, not exact. No budget/time/sample
  flags; prune counters across all 58 counted shards remain zero. Exact N11 still requires shards 58..63
  for counts, and a chainable merged d11 frontier still requires frontier outputs for shards 0..11 as
  well as 58..63.

R82 CURRENT D10->D11 CERTIFICATION PROGRESS WITH FRONTIER OUTPUT:
  Additional chainable runner shards completed:
    `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 58-59 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r82 --aggregate-out scratchpad\r3_d10_to_d11_shard64_58_59_chain_aggregate_r82.json --allow-incomplete`
  Shard58: 663->7095, wall 53.09s; shard59: 663->7152, wall 55.49s. Both wrote depth-11 frontier
  JSONL files with row counts matching stats.
  Combined diagnostic aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r71_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r72_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r73_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r74_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r75_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r76_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r77_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r78_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r79_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r80_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r81_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r82_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_59_aggregate_r82.json`
  Coverage: 39780/42430 depth-10 parents = 93.7544%; depth-11 pilot children 434876; weighted branching
  10.932; diagnostic scaled `N11 ~ 463846`. Rows are still diagnostic, not exact. No budget/time/sample
  flags; prune counters across all 60 counted shards remain zero. Exact N11 still requires shards 60..63
  for counts, and a chainable merged d11 frontier still requires frontier outputs for shards 0..11 as
  well as 60..63.

R83 CURRENT D10->D11 CERTIFICATION PROGRESS WITH FRONTIER OUTPUT:
  Additional chainable runner shards completed:
    `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 60-61 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r83 --aggregate-out scratchpad\r3_d10_to_d11_shard64_60_61_chain_aggregate_r83.json --allow-incomplete`
  Shard60: 663->7730, wall 54.65s; shard61: 663->7499, wall 54.62s. Both wrote depth-11 frontier
  JSONL files with row counts matching stats.
  Combined diagnostic aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r71_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r72_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r73_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r74_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r75_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r76_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r77_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r78_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r79_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r80_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r81_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r82_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r83_*.json" --allow-incomplete --out scratchpad\r3_d10_to_d11_shard64_00_61_aggregate_r83.json`
  Coverage: 41106/42430 depth-10 parents = 96.8796%; depth-11 pilot children 450105; weighted branching
  10.950; diagnostic scaled `N11 ~ 464603`. Rows are still diagnostic, not exact. No budget/time/sample
  flags; prune counters across all 62 counted shards remain zero. Exact N11 still requires shards 62..63
  for counts, and a chainable merged d11 frontier still requires frontier outputs for shards 0..11 as
  well as 62..63.

R84 EXACT D10->D11 CERTIFICATION:
  Final chainable runner shards completed:
    `python s3_run_shards.py --frontier-in scratchpad\r3_frontier_d10_r52.jsonl --shard-count 64 --indices 62-63 --target-depth 11 --node-budget 100000 --time-cap 300 --level-cap 100000 --out-dir scratchpad --frontier-out-dir scratchpad\r3_d10_to_d11_frontiers --tag r3_d10_to_d11_shard64_chain_r84 --aggregate-out scratchpad\r3_d10_to_d11_shard64_62_63_chain_aggregate_r84.json --allow-incomplete`
  Shard62: 662->6848, wall 53.33s; shard63: 662->6683, wall 52.43s. Both wrote depth-11 frontier
  JSONL files with row counts matching stats.
  Strict all-shard aggregate:
    `python s3_aggregate_shards.py --glob "scratchpad\r3_d10_to_d11_shard64_0*_stats_r53.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r54_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r55_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r56_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_runner_r57_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r59_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r60_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r61_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r62_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r63_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r64_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r65_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r66_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r67_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r68_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r69_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r70_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r71_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r72_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r73_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r74_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r75_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r76_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r77_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r78_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r79_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r80_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r81_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r82_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r83_*.json" --glob "scratchpad\r3_d10_to_d11_shard64_chain_r84_*.json" --out scratchpad\r3_d10_to_d11_shard64_00_63_EXACT_aggregate_r84.json`
  Exact counts: N10=42430, N11=463636, weighted branching 10.927. No budget/time/sample flags;
  prune counters across all 64 shards remain zero. This is an exact depth-11 measurement, not a
  construction or nonexistence proof. To make d11 chainable, rerun shards 0..11 with frontier output,
  then merge all 64 shard frontier files.

CLOUD RUN COMMAND (R189 exact d10->d11 refresh; run before refreshed d11->d12 work):
    # Starts from the regenerated R189 d10 frontier:
    #   scratchpad/r3_frontier_d10_r189_nearfull_subset_moment.jsonl
    # Full run over 64 shards is strict/exact; worker subsets are diagnostic until aggregated.
    python .work/99graph/s3_cloud_r3_d11_r189.py \
        --frontier-in scratchpad/r3_frontier_d10_r189_nearfull_subset_moment.jsonl \
        --out-dir d10_d11_r189_stats --frontier-out-dir d10_d11_r189_frontiers \
        --aggregate-out r3_d10_to_d11_r189_shard64_EXACT_aggregate.json
    python .work/99graph/s3_merge_frontiers.py \
        --glob "d10_d11_r189_stats/r3_d10_to_d11_r189_shard64_exact_*.json" \
        --out r3_frontier_d11_r189.jsonl
    # R189 N10 is exactly 42422. Exact R189 N11 is NOT known until this shard refresh finishes;
    # old R90/R186 direct scans are diagnostic only because these completion predicates are prefix
    # predicates, not monotone later-depth row statistics.

CLOUD RUN COMMAND (pre-R189 exact d11->d12 measurement from the R90 frontier; use only with corrections):
    # Copy or keep the exact R90 frontier at one of:
    #   scratchpad/r3_frontier_d11_r90.jsonl
    #   r3_frontier_d11_r90.jsonl
    # Then run the one-command wrapper. It runs --gate first unless --skip-gate is passed.
    python .work/99graph/s3_cloud_r3_d12.py --frontier-in r3_frontier_d11_r90.jsonl
    # R184 note: current code includes the pair lower-closure Stage-A demand. Existing R90/R183
    # frontiers scanned clean at d12, so the old measured prefix remains compatible; this is expected
    # to matter, if at all, only near later degree-saturation levels.
    # R185 note: current code also includes neighbourhood matching-completion closure. This DOES change
    # shallow exact counts. R185 alone gives N9=5310 and N10=42425, and old d11 has 29 monotone dead rows.
    # R186 note: current code also includes outside-degree moment closure. Prefer
    # scratchpad/r3_frontier_d10_r186_outside_moment.jsonl for historical R186 continuations. R186 gives
    # N10=42423; old R90/R183 artifacts have direct violations (old d11 27, available d12 141/1,174,677).
    # R189 note: current code also includes near-full subset outside-degree moment closure. Prefer
    # scratchpad/r3_frontier_d10_r189_nearfull_subset_moment.jsonl for all new d10 continuations. R189
    # gives N10=42422; old direct scans show extra rows (old d11 +10 beyond R186, available d12 +87
    # beyond R186), but exact refreshed N11/N12 require regeneration from the R189 prefix, not subtraction.
    # The exact all-shard command expands to a strict aggregate over shards 0..511 and MUST NOT
    # pass --allow-incomplete. Expected single-process wall from local probes is roughly
    # 512 * 130-140s = 18-20h; use workers below to shorten elapsed time.

    # Distributed workers, example 16-way split. Worker aggregates are diagnostic by design;
    # the final strict aggregate below is the exact proof artifact once all 512 stats exist.
    python .work/99graph/s3_cloud_r3_d12.py \
        --frontier-in r3_frontier_d11_r90.jsonl --worker-count 16 --worker-index WORKER_ID \
        --out-dir d11_d12_stats --frontier-out-dir d11_d12_frontiers \
        --aggregate-out d11_d12_worker_WORKER_ID_aggregate.json --skip-gate
    python .work/99graph/s3_aggregate_shards.py \
        --glob "d11_d12_stats/r3_d11_to_d12_shard512_exact_*.json" \
        --out r3_d11_to_d12_shard512_EXACT_aggregate.json
    python .work/99graph/s3_merge_frontiers.py \
        --glob "d11_d12_stats/r3_d11_to_d12_shard512_exact_*.json" \
        --out r3_frontier_d12.jsonl
    # Exact acceptance criteria: aggregate has complete_shard_set=true, exact=true at depth 12,
    # source SHA ce3f25d95d2c102eb00d53b23fcd38a449758b55392e51cf0804104db03cfb7b, no
    # budget/time/sample flags, and merge writes a complete depth-12 frontier whose physical
    # graph-row count equals the exact N12 aggregate.

CLOUD RUN COMMAND (primary R199 root/depth-45 r=3 Stage-A measurement):
    # 0) deps (no compiler needed): pip install igraph numpy sympy python-sat ortools
    # 1) self-checking one-command root measurement. It runs --gate first unless --skip-gate is passed.
    #    R218: a fresh full local gate passed in 238.5s.  Archive that transcript with the cloud run;
    #    rerun the gate if code/dependencies/environment changed before launch.
    python .work/99graph/s3_cloud_r3_stagea.py \
        --node-budget 200000000 --time-cap 86400 --target-depth 45 --level-cap 2000000 \
        --out-dir r3_stagea_cloud
    #    IMPORTANT: the wrapper never passes --seed-triangle. Stats JSON and manifest files are written
    #    under r3_stagea_cloud/ by default. Rows after a sampled level are diagnostic only.
    #    Dry-run/smoke reproduce command from R216:
    python .work/99graph/s3_cloud_r3_stagea.py --dry-run \
        --target-depth 12 --node-budget 4000 --time-cap 20 --level-cap 200 \
        --out-dir scratchpad\r3_stagea_dry_r216 --manifest-out scratchpad\r3_stagea_dry_r216_manifest.json
    # 1b) Optional Stage-B CP-SAT readiness gate (R176; T(7) real-witness diagonal+clique+closure):
    python .work/99graph/s3_stageb_columns_cpsat.py --self-test --time-cap 30 \
        --json-out r3_stageb_cpsat_t7_selftest.json
    # 2) lower-level equivalent, for manual control/debug only:
    python .work/99graph/s3_slice_harness.py --gate
    python .work/99graph/s3_slice_harness.py --slice \
        --node-budget 200000000 --time-cap 86400 --target-depth 45 --level-cap 2000000 \
        --stats-out r3_single_node_stats.json
    #    --time-cap is soft between complete levels; stop/distribute by prefix if a level is too wide.
    #    (reads off: per-depth iso-free N_d, where the spectral gates START to bite mid-tree, the
    #     true b(depth) curve, and the projected/measured N_A.  This is the §3 STEP-1/STEP-2 slice.)
    # 3) Stage-B smoke on generated candidates:
    python .work/99graph/s3_slice_harness.py --stageb-demo --target-depth 14 --node-budget 200000 \
        --stageb-engine auto
  EXACT DISTRIBUTED PREFIX WORKFLOW (R48/R49, preferred once a complete prefix frontier is available):
    # A) write a complete prefix frontier (depth 10 verified locally; depth 9 is the faster fallback)
    python .work/99graph/s3_slice_harness.py --slice \
        --target-depth 10 --node-budget 100000 --time-cap 3600 --level-cap 100000 \
        --frontier-out r3_frontier_d10.jsonl --stats-out r3_frontier_d10_stats.json
    # Optional shallow certification: run all 64 shards to certify exact N11 before going deeper.
    python .work/99graph/s3_run_shards.py \
        --frontier-in r3_frontier_d10.jsonl --shard-count 64 --start 0 --stop 64 \
        --target-depth 11 --node-budget 100000 --time-cap 3600 --level-cap 100000 \
        --out-dir . --frontier-out-dir d10_d11_frontiers --tag d10_d11_shard \
        --aggregate-out d10_d11_aggregate.json
    # If all 64 shards are complete and exact, merge their frontier rows to continue without rerunning.
    python .work/99graph/s3_merge_frontiers.py --glob "d10_d11_shard_*.json" \
        --out r3_frontier_d11.jsonl
    # B) launch worker i=0..N-1; canonical-parent ownership makes shards disjoint
    python .work/99graph/s3_slice_harness.py --slice \
        --frontier-in r3_frontier_d10.jsonl --shard-count N --shard-index i \
        --node-budget 200000000 --time-cap 86400 --target-depth 45 --level-cap 2000000 \
        --stats-out shard_i.json
    # Equivalent R199 worker wrapper. Use --skip-gate on workers after one gate transcript has been
    # archived for the run.
    python .work/99graph/s3_cloud_r3_stagea.py --skip-gate \
        --frontier-in r3_frontier_d10.jsonl --shard-count N --shard-index i \
        --node-budget 200000000 --time-cap 86400 --target-depth 45 --level-cap 2000000 \
        --out-dir r3_stagea_worker_i
    # C) combine only R48+ canonical-parent runs; read only depths marked exact.
    python .work/99graph/s3_aggregate_shards.py --glob "shard_*.json" --out aggregate.json
  DISTRIBUTION (when single-node N_A is too wide): each worker owns a shard of a saved complete
  depth-d frontier, and the R48 canonical-parent rule assigns every child to exactly one parent shard.
  Do NOT sum outputs from naive pre-R48 modulo shards.  Stage B is <1% of cost (§4d) -- run it inline
  on each completed H'.
  R49 aggregate rule: do NOT read sampled/diagnostic aggregate rows as measured `N_d`; only rows with
  `"exact": true` are decisive.
  PORT NOTE (honest): the python generator is the MEASUREMENT instrument, not the production engine.
  For the full depth-45 search at scale, port the inner extension+BLISS loop to nauty/Traces `geng`
  + the C inertia update (the python LDL is exact but ~ms/node).  The harness defines the gates and
  the soundness oracle the C port must reproduce (re-run --gate against the C port).
