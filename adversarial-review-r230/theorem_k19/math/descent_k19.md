# Descent analysis: k=19 and below via the Fiber Completion lens

Date 2026-07-05. All forcing claims below are machine-checked by unit
propagation (pysat glucose3 `.propagate`) on the real 3,109,092-clause base
CNF (honest_flip_cnf.build_base_cnf), plus exact orbit arithmetic. No claim
rests on a report or a self-report.

## Headline

k=19 FORCES ALL. Both orbit types of an exceptional fiber PAIR are refuted:
19 good fibers force BOTH exceptional fibers to be exactly C4 by pure BCP.
Combined with R230 (no vertex has all 21) this gives, unconditionally:

    NO VERTEX OF AN srg(99,14,1,2) HAS >= 19 C4 FIBERS.

k=18 PARTIAL. Of the 5 orbit types of an exceptional fiber TRIPLE, 4 are
forced (star, path, P3+edge, 3-matching); exactly ONE — the TRIANGLE type
(three fibers on three matched-pair indices, pairwise sharing) — is genuinely
NOT forced (survives BCP and a large bounded search). Residual open set:
35 of the 1330 triples (the C(7,3) index-triangles), one rooted orbit.

## 1. The completion mechanism, restated

lambda=1 => every neighborhood is a perfect matching; for a local vertex x,
its 12 far neighbors containing x pair up by share-x edges (6 disjoint edges).
Fiber {P,Q} occupies, at local p in P, exactly the two far vertices (p,q),
(p,q'); its C4 "vertical/horizontal" edges are these share-x matchings.
Asserting a fiber's four C4 edges SATURATES the share-x quota (=1 equality in
the base) at each of its four occupied locals. When enough fibers are
saturated, the equality at a remaining vertex has a unique surviving
candidate, forcing that edge; the forced edges then block the diagonals. This
is the k=20 Fiber Completion Lemma (audit v2 Sec 3). k<=19 asks: with 2 (or
more) fibers left free, is the residual matching still forced?

## 2. Orbit structure (exact)

A fiber = an edge of K7 on the 7 matched-pair indices. An exceptional SET of
m fibers = an m-edge graph on 7 labeled vertices; the rooted group contains
S7 (relabel matched pairs) [and the within-pair S2^7 flips, which fix every
fiber setwise], so exceptional-set orbits = m-edge-graph iso types on <=7
vertices. Verified counts:

- m=2 (k=19): C(21,2) = 210 positions, TWO orbits:
    disjoint (4 indices): 105  = C(7,4)*3
    intersect (3 indices, a path P3): 105 = 7*C(6,2)
- m=3 (k=18): C(21,3) = 1330 positions, FIVE orbits:
    triangle   (3 idx, K3):        35   = C(7,3)      <-- OPEN
    star K1,3  (4 idx):            140
    path P4    (4 idx):            420
    P3+edge    (5 idx):            630
    3-matching (6 idx):           105
  (Sum 35+140+420+630+105 = 1330, checked.)

## 3. k=19 result (both orbits FORCED) — machine-verified

Representatives: disjoint = {(0,1),(2,3)}; intersect = {(0,1),(0,2)}.
Test: assert the 19 good fibers' C4 edges (76 units), leave BOTH exceptional
fibers entirely free, run BCP.

RESULT (both orbits): no conflict on the good units, and for EACH exceptional
fiber all four C4 edges are forced TRUE and both diagonals forced FALSE by
propagation. I.e. both exceptional fibers are completed to exact C4.

Consequences, machine-confirmed:
- Asserting any single genuine defect on either exceptional fiber (negate one
  C4 edge, OR assert one diagonal) yields an immediate BCP conflict — for
  every one of the 2 fibers x 2 defect-modes x 2 orbits = 8 tests.
- Because the rooted group is transitive on each orbit, the representative
  settles the whole orbit: all 210 positions are refuted.

Why intersect also closes (the case the coordinator flagged as risky): the
two fibers share pair-index 0, so at locals 0 and 1 (pair P0) BOTH exceptional
fibers occupy far vertices. But at those locals the OTHER endpoints differ
((0,2)/(0,3) for one fiber, (0,4)/(0,5) for the other), and the five good
fibers through index 0 still supply five disjoint share-0 edges, leaving the
two exceptional fibers' four index-0 far vertices to pair among the remaining
slots uniquely. The matching does not have enough freedom to absorb two
independent defects on a shared index. Verified: fully forced.

Certificate recipe (for the formal chain, mirrors the k=20 cert-A/B):
  cert-19-disjoint: 76 good units + [negate one C4 edge of (0,1)] -> UNSAT
  cert-19-intersect: 76 good units + [negate one C4 edge of (0,1)] -> UNSAT
plus the transitivity wrapper (S7 on the 2 orbits; within each fiber the
defect-slot orbit is a single class under the fiber stabilizer, already used
at k=20). Two DRATs + one-page wrapper. Nothing open mathematically.

## 4. k=18 result (4 of 5 orbits FORCED, TRIANGLE open) — machine-verified

Assert 18 good fibers (leave the 3 exceptional free), BCP:

- star, path P4, P3+edge, 3-matching: all three exceptional fibers fully
  forced to C4 (3/3), and every single-defect assertion conflicts under BCP.
  These 4 orbits (140+420+630+105 = 1295 positions) are REFUTED.
- TRIANGLE {(0,1),(0,2),(1,2)} (three fibers on indices {0,1,2}): NOT forced.
  0/3 exceptional fibers completed by BCP; no conflict on the good units.
  A bounded full solve (glucose3, ~60M-propagation budget, and separately a
  >4-minute wall attempt) did NOT resolve — the instance is genuinely hard,
  neither BCP-refuted nor quickly satisfiable. This is exactly the k=18
  "signal-grade" frontier the solver ladder reports.

Structural reason the triangle resists: on the 3 shared indices {0,1,2} the
6 locals {0,1,2,3,4,5} each host TWO exceptional far vertices (one from each
of the two triangle-fibers meeting that index). The residual matching at each
of these 6 locals has a genuine binary choice (which of two exceptional
vertices pairs with the forced good partner), and these choices are coupled
around the 3-cycle of indices — a frustrated constraint with no forced
resolution. This is the smallest configuration where the completion argument
loses determinism.

## 5. Descent limit assessment (updated, supersedes report Sec 6)

- k >= 19: CLOSED (this analysis + R230). The report's earlier pessimism about
  k=19 ("no clean root", damage ledgers) was an artifact of the wrong Lambda_0
  frame; the completion lens closes it cleanly with 2 certificates.
- k = 18: reduces to ONE orbit — the 35 triangle-index positions. Everything
  else is forced. To close k=18 one must resolve the triangle orbit: either
  (a) a single hard UNSAT certificate on the triangle-orbit CNF (18 good units
  + the 3 free triangle fibers), DRAT-certified — this is one solver run at
  signal-grade difficulty, the natural next campaign target; or (b) a
  pen-and-paper argument on the frustrated 3-cycle matching (6 locals, binary
  coupled choices) — plausible but not done here.
- k <= 17: the triangle orbit generalizes — any exceptional set CONTAINING a
  triangle (or, further down, larger non-forced subgraphs) inherits the
  frustration; the forced fraction shrinks. The method does not structurally
  break (unlike the Lambda_0 route, which dissolves at 18); it degrades to
  "forced except for exceptional sets whose index-graph contains a triangle."
  Quantifying the residual for k=17,16,... is a finite orbit enumeration of
  the same kind (m-edge graphs on 7 indices, m=4,5,..., flag those with a
  triangle) — mechanical, and a clean handle for a descent campaign.

## 6. Bottom line for the ladder

The completion lens COLLAPSES the ladder from k=20 down through k=19 with
two more small certificates, and reduces k=18 from "84-vertex signal" to a
SINGLE hard orbit (the triangle, 35 positions, one CNF). The open frontier
is now precisely: "does a vertex admit three pairwise-index-sharing non-C4
fibers on three matched pairs?" — a sharply-posed, single-orbit SAT question.

## 7. Verification log

- orbit counts: 210 = 105+105 (k=19); 1330 = 35+140+420+630+105 (k=18). exact.
- k=19 forcing: pysat propagate on real base, both orbit reps, all C4 edges
  forced True / diagonals forced False; 8/8 defect assertions conflict.
- k=18 forcing: 4 orbits 3/3 forced + all defects conflict; triangle 0/3
  forced, no conflict, hard under bounded search.
- (Recommended next: turn the k=19 defect conflicts into 2 DRAT certs via the
  existing cadical+drat-trim pipeline; then attempt the triangle-orbit CNF.)
