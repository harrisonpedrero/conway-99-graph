# Audit v2: the six g2v2 refutations — validity, content, and k=20 consequences

Date: 2026-07-05. Auditor: this session. All checks below were re-run locally
(exact arithmetic + pysat BCP on the real base CNF + drat-trim); nothing is
taken from the coordinator's report on trust.

## Executive verdict

- M1, M2, M3a, M3b: VALID. Each is exactly the designed radius-1 quota lemma.
- M5, M6: NOT VACUOUS. They are locally consistent (pass full radius-1 scans),
  encode exactly the rep_table_v2 units, and are GENUINELY UNSAT. My
  "expected SAT" prediction was wrong. The refutation content is a new,
  load-bearing fact — the FIBER COMPLETION LEMMA — which, combined with the
  certified R230 result, CLOSES THE k=20 RUNG. See Section 4.

## 1. M5 / M6 vacuity check (coordinator task 1)

Unit fidelity: for all six reps, manifest_v2.json unit_literals were recomputed
from rep_table_v2.json label pairs via the canonical edge-var order and match
EXACTLY (polarity included; M5 = 82 pos + literal -12 = not-E3; M6 = 83 pos +
literal -1726 = not-(2,4)-(3,4)). manifest validation blocks (sha256, p-line,
trailing units) all true.

Radius-1 scan on the manifest's actual units: M5, M6 have NO violation (all
per-(far,local) counts within quota; pairwise common-neighbor caps ok). So the
earlier slot1-3 vacuity mode (units contradicting one quota by OVERCOUNT) is
absent. NOT vacuous.

Why they are UNSAT anyway (the mechanism my radius-1 checker cannot see):
the base encodes quota EQUALITIES. Asserted C4 edges of the 20 good fibers
SATURATE the share-x quotas of their endpoints, which BCP turns into forced
NON-edges elsewhere; the equality at the remaining vertex then has all its
candidates false except one, forcing that edge TRUE. Concretely for M5: at
local 2, the five good fibers {(2,3),R} (R != (0,1)) pair up (2,4)-(2,5),
(2,6)-(2,7), (2,8)-(2,9), (2,10)-(2,11), (2,12)-(2,13); each (2,y) has
share-2 quota exactly 1, now saturated; so (0,2)'s share-2 equality (=1) has
sole surviving candidate (1,2): edge E3 = (0,2)-(1,2) is FORCED TRUE. M5
asserts not-E3: contradiction. For M6: at local 4, good fibers pair
(0,4)-(1,4), (4,6)-(4,7), (4,8)-(4,9), (4,10)-(4,11), (4,12)-(4,13); the
share-4 equality at (2,4) then forces (2,4)-(3,4) TRUE; M6 negates it.

Machine confirmation (pysat glucose3 on the 3,109,092-clause base):
- propagate(M5 units) and propagate(M6 units): conflict at PURE unit
  propagation (no search) — consistent with the 2s solves and with the DRAT
  sizes (3.49MB, dominated by propagation-chain lemmas over the seqcounter
  encodings).
- propagate(M5 positives only, without -12): no conflict, and +12 (E3) IS in
  the propagated set — E3 forced true, exactly the mechanism above.
- propagate(M6 positives only): +1726 ((2,4)-(3,4)) forced true. Same.

drat-trim verification (local, this session): all six certificates
"s VERIFIED" against their CNFs.

## 2. M1-M3b content audit (coordinator task 2)

Three independent confirmations each:
(a) Units match the table exactly (see Sec. 1).
(b) Radius-1 scan on the actual units finds EXACTLY ONE violated quota per
    rep, and it is the designed one:
      M1: far (0,3), local 2 (count 2 > quota 1)   [design: (0,3) share-2]
      M2: far (0,2), local 3                        [design: (0,2) share-3]
      M3a: far (0,2), local 2                       [design: (0,2) share-2]
      M3b: far (2,4), local 2                       [design: (2,4) share-2]
    No accidental second violation anywhere.
(c) Isolated-constraint refutation: for each rep I rebuilt ONLY the single
    designed cardinality equation (CardEnc.equals over the share-x candidate
    edges of the designated far vertex, rhs = quota) plus the rep's two unit
    clauses: UNSAT in isolation. So the designed constraint alone refutes the
    units; the full-base refutation is that content, not an accident.
Also: full-base BCP-only conflict confirmed for all four; DRATs verified.
VERDICT: M1 VALID, M2 VALID, M3a VALID, M3b VALID — as designed radius-1
lemma certificates (they certify analytic steps, not deep search results).

## 3. What the refutations reveal: the Fiber Completion Lemma

LEMMA (fiber completion; machine-verified at BCP level, minimal premises).
In the honest rooted system for srg(99,14,1,2) (base CNF, no extra
assumptions), assert ONLY the 80 C4 edges of the 20 fibers other than
F0 = {(0,1),(2,3)}. Then unit propagation alone forces:
  (0,2)-(0,3), (1,2)-(1,3), (0,2)-(1,2), (0,3)-(1,3)  all TRUE, and
  (0,2)-(1,3), (0,3)-(1,2)  (the diagonals) both FALSE.
I.e., THE 21st FIBER IS FORCED TO BE EXACTLY C4. (Verified this session via
solver.propagate on the real base: all six polarities confirmed; no conflict.)

Proof sketch (pen-and-paper, radius 2): lambda=1 makes every neighborhood
induce a perfect matching. For local vertex x in a pair X of F0's class pair
{P,Q}: the 12 far vertices containing x must pair up via share-x edges; the
five good fibers {pair(x)^c ...} containing x's pair contribute five disjoint
share-x edges covering 10 of them; the two leftover are F0's vertices, forced
to pair with each other. Doing this at each of the four locals 0,1,2,3 forces
all four C4 edges of F0; the forced edges saturate the cross quotas, blocking
both diagonals. QED. (Same argument as the M5/M6 forcing; the CNF facts above
are its machine check.)

COROLLARY: no vertex of an srg(99,14,1,2) has exactly 20 C4 fibers.
With R230 (certified: no vertex has all 21): NO VERTEX HAS >= 20 C4 FIBERS.

## 4. Coverage of G2' and the k=20 status (coordinator task 3)

- The four valid certificates close leak modes M1-M4 (cross leaks blocked by
  Delta's existence; share leaks force two bad fibers).
- M5/M6 do better than close their damage modes: their UNSAT shows the
  premise "exactly one bad fiber at a vertex" is itself contradictory —
  which SUPERSEDES the entire G2'/leak analysis and Makhnev's Lambda_0
  machinery for the k=20 rung. Gaps G-A (clean root), G-B (L9 damage
  arithmetic), G-C (Lambda_0-(*)) from the report are MOOT at k=20: they
  were only needed to handle a vertex with one bad fiber, which cannot exist.
- k=20 STATUS: FALLS. Chain: [six v2 DRATs, verified] + [fiber completion
  minimal-premise check] + [R230 certificate] + elementary lemmas
  (neighborhood matching from lambda=1; fiber partition from mu=2; symmetry).

Remaining work for a clean, publishable certificate chain (small):
(1) Two MINIMAL orbit-canonical CNFs + DRATs, replacing M5/M6's slightly
    over-premised versions:
    cert-A: 80 good-fiber units + unit not-(0,2)-(1,2)      -> UNSAT
    cert-B: 80 good-fiber units + unit +(0,2)-(1,3)         -> UNSAT
    (M5 also asserted E1,E2; M6 also asserted 3 edges of F_bad. Harmless but
    inelegant. cert-A/B need no F0 assertions at all.)
(2) The one-page symmetry wrapper: the stabilizer of F0 in S2 wr S7 acts
    transitively on F0's four C4-edge slots and on its two diagonals, so
    cert-A and cert-B cover every non-C4 defect pattern of the 21st fiber.
(3) Cite R230's existing certificate for the 21-fiber case.
Items (1)-(2) are an afternoon of existing pipeline work; nothing open
mathematically.

## 5. Descent outlook (k=19), from the same lens

The completion argument constrains k=19 sharply: two bad fibers at a vertex
must SHARE a matched pair (if their classes are disjoint, each is completed
to C4 by its five good partners — contradiction). For bad fibers {P,Q} and
{P,R}: all Q-slot and R-slot edges are still forced (their five partners are
good), diagonals blocked, so the only possible defects are CROSSED share-p /
share-p' pairings at the two locals of P: e.g. (p,q)-(p,r) instead of
(p,q)-(p,q'). Small orbit space (crossing patterns at p and p', a few
label-symmetry classes). The k=19 rung is plausibly certifiable by the same
[good-fiber units + crossing units] -> CNF recipe, and this matches the
solver ladder's observation that 19 is genuinely harder but solver-provable.

## 6. Corrections to my own prior outputs

- rep_table_v2.json's expected_verdict for M5/M6 ("SAT conjectured") is
  WRONG; the configurations are impossible. The table's unit lists and
  consistency certifications remain correct as stated (they claim only
  radius-1 consistency, which holds).
- makhnev_k20_report.md v2 Sections 4-6 statements that "M5/M6 are the
  genuine residual damage modes, not locally refutable" are RETRACTED by
  this audit; a v3 addendum note has been added to the report.
- The report's k=19 analysis should be redone from the completion lens
  (Sec. 5 above) rather than the M5/M6 damage ledger.
