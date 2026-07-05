# Makhnev 1988, Lemmas 6-9: dependency on (*) and the k=20 question

**Verdict (one paragraph).** Makhnev's Lemmas 6-9 use the FULL strength of (*) at
*every* vertex of Gamma, and they use it in two structurally different ways: (a)
locally at the three vertices of the root triangle Delta (Lemma 6: k_Lambda = 12,
lambda_Lambda = 1) and at every far vertex X (Lemma 7: the 6 mu-neighbors of X in
Gamma(Delta) are pairwise non-adjacent — this is exactly "the fiber of X over each
of A,B,C is C4-compatible"); and (b) globally through Lemma 8, which needs (*) at
vertices of triangles Delta_1 at distance 1 from Delta in Lambda. A single non-C4
fiber at a single vertex breaks the regularity of Lambda_0 = {Delta} u Lambda_1 u
Lambda_2 (33 triangles) only in a bounded, countable way: each failed fiber
perturbs at most O(1) edges of Lambda_0. The k=20 rung does NOT fall by a soft
counting repair alone — Lemma 9's divisibility argument (12*10/20 = 6) has slack
when one fiber fails — but a finite case analysis is well-posed and small (the
failed fiber interacts with the (33,12,1,6) machinery through <= 24 explicitly
enumerable triangle-pairs). I give below the exact perturbation ledger, a partial
repaired argument that rules out most failure configurations, and a precise
statement of the remaining gap. Descent below k=20 by this method degrades
quickly: at k=19 the perturbation is no longer localized to one fiber per root
choice, and at k<=18 the (33,12,1,6) skeleton itself is no longer forced.

## [v3 ADDENDUM — SUPERSEDES THE k=20 STATUS BELOW] (audit v2)

The six v2 CNFs were solved and drat-trim VERIFIED (all UNSAT). The M5/M6
refutations are genuine, not vacuous, and reveal the FIBER COMPLETION LEMMA:
in the honest rooted system, asserting only the 80 C4 edges of 20 fibers
forces (by unit propagation alone) the 21st fiber to be exactly C4 — machine
verified this session at BCP level with minimal premises. Hence no vertex has
exactly 20 C4 fibers; with R230's certificate (no vertex has 21):
NO VERTEX OF AN srg(99,14,1,2) HAS >= 20 C4 FIBERS. THE k=20 RUNG FALLS,
bypassing the Lambda_0 machinery entirely. Gaps G-A/G-B/G-C below are moot at
k=20 (they existed only to manage a single bad fiber, which cannot exist).
Remaining housekeeping: two minimal orbit-canonical certificates (cert-A,
cert-B) + a one-page symmetry wrapper — see .work/g2prime_audit_v2.md
Sections 3-4. The k=19 outlook is rewritten by the same lens: two bad fibers
at a vertex must share a matched pair, with defects confined to crossed
share-p pairings (audit v2 Section 5). Sections 4-6 below stand as v2
history, but their "M5/M6 not locally refutable" claims are RETRACTED.

## [CORRECTED v2] Status banner (post g2prime audit)

The g2prime audit (.work/g2prime_audit.md) found an error in this report's
original Section 2 (Lambda_1 geometry) that propagated into Sections 3-6.
Corrected passages below are marked [CORRECTED v2]. Headline changes:
(1) Lambda_1 triangles are vertex-DISJOINT from Delta (12 x 3 = 36 partition),
    not vertex-sharing as originally written.
(2) The original "6 slot types, 3 closed by hand" taxonomy is RETRACTED. The
    corrected damage taxonomy is M1-M6 (Section 4 v2). M1-M4 close at radius 1
    by quota arithmetic (machine-verified 2026-07-05); M5 (mate-loss) and M6
    (vertical-loss) are the genuine residual damage modes and are NOT
    refutable at the bad-fiber vertex alone.
(3) The k=20 proof burden moves to: clean-root existence in the corrected
    frame, L9 damage arithmetic for M5/M6, and the previously unmapped
    requirement that condition (*) hold inside Lambda_0 for the Theorem-1
    application.
(4) Machine-readable representatives: ladder/g2prime/rep_table_v2.json. The
    three g2prime_slot*.cnf/.drat artifacts are RETIRED as evidence (audit:
    vacuous refutations).
The verdict paragraph above remains directionally correct (k=20 partial, not
proved) but its mechanism description is superseded by the v2 text.

## Contents
1. Setup and notation (modern English)
2. Reconstruction of Lemmas 6-9 (with corrected OCR readings)
3. Exact dependency map on (*)
4. Perturbation analysis: one vertex with 20-of-21 C4 fibers
5. The repaired argument for k=20: what is proved, what remains
6. Descent limit assessment (k=19, k=18)
7. Arithmetic verification log

## 1. Setup and notation

Gamma = hypothetical srg(99,14,1,2). lambda=1: every edge lies in a unique
triangle; 99*14/2 = 693 edges, 693/3 = 231 triangles. For adjacent A,B write
A.B for the third vertex of the unique triangle on AB.

Fiber language vs Makhnev's (*): root at v. N(v) is a perfect matching of 7
pairs (lambda=1). Each far vertex X (84 of them) is adjacent to exactly mu=2
vertices of N(v), necessarily from DIFFERENT matched pairs (else a triangle on
a matched edge would repeat), so X carries a label = an unordered pair of
matched pairs... more precisely a pair {a,b} with a,b in N(v) non-adjacent.
There are 21 = C(7,2) pair-classes; each class contains 4 labels and the fiber
of a class has 4 far vertices (Sec. 7). The fiber is "C4" iff the 4 vertices
induce a 4-cycle matching the label-sharing pattern. Equivalence: (*) holds for
all triangle pairs through v iff all 21 fibers at v are C4.

Lambda = triangle graph: vertices = 231 triangles; Delta_1 ~ Delta_2 in Lambda
iff joined by exactly 3 edges of Gamma. (*) says: joined by >=2 edges implies
joined by exactly 3, i.e., there are no "2-bridges".

## 2. Reconstruction of Lemmas 6-9 (OCR corrected)

Fix Delta = ABC. Gamma(Delta) = [A] u [B] u [C]; |Gamma(Delta)| = 39 = 3*(14-1)
since [A],[B],[C] pairwise intersect exactly in Delta's vertices (mu=2,
lambda=1). Outside: 99 - 39 = 60 vertices.

L6 [CORRECTED v2]. "k_Lambda(Delta) = 12 and lambda_Lambda = 1 near Delta."
Makhnev's text: the 36 points of Gamma(Delta)-Delta lie in 12 triangles of
[Delta]_Lambda. Since 12 x 3 = 36, these triangles are vertex-DISJOINT from
Delta, 3-joined to it (a perfect matching of edges onto A, B, C), and they
PARTITION the 36 points. Explicit form, rooted at A (labels = A-frame far
labels): for each x in N(A)-{B,C},
    T_x = { x, {B,x}, {C,x} },
where {B,x} is the unique far vertex adjacent to B and x. T_x is 3-joined to
Delta via x-A, {B,x}-B, {C,x}-C (all label-forced). T_x EXISTS as a triangle
iff the single edge {B,x}~{C,x} holds — the "vertical" of fiber
{pair(B,C), pair(x)} at A. The Lambda-triangle {Delta, T_x, T_x'} (x' = mate
of x) needs additionally the "horizontals" {B,x}~{B,x'} and {C,x}~{C,x'}.
Enumeration is complete: any triangle 3-joined to Delta has this form.
Hence L6-clean(Delta) <=> the 6 fibers at A containing pair(B,C) are fully C4
(12 verticals + 12 horizontals; the fiber chords are then auto-blocked by
mu-quotas at radius 1). lambda_Lambda is then exactly 1 (T_x's unique common
neighbor with Delta is T_x').

L7. "Every X outside Gamma(Delta) lies in a UNIQUE triangle disjoint from
Gamma(Delta)." X has exactly 2 neighbors in each of [A],[B],[C] (mu=2), 6
points total; by (*) these 6 are pairwise non-adjacent; X lies on 7 = 14/2
triangles; 6 of them meet Gamma(Delta) (one per mu-neighbor), leaving exactly
1 disjoint. Hence the 60 outside points partition into 20 disjoint-from-
Gamma(Delta) triangles: Lambda_2. Put Lambda_1 = [Delta]_Lambda (12 triangles),
Lambda_0 = {Delta} u Lambda_1 u Lambda_2, |Lambda_0| = 33.

L8 [CORRECTED v2]. "If Delta_1 in Lambda_1 then [Delta_1]_Lambda subset
Lambda_0." Delta_1 = T_x is DISJOINT from Delta. Root at w := x (any vertex of
T_x; the other two are then a matched pair of N(w), canonically (2,3), and in
w's frame Delta = {0, (0,2), (0,3)} with A = 0 in N(w), T_w = {w,2,3},
Delta_2-mate = {1, (1,2), (1,3)}). Complete enumeration (verified):
    [T_w]_Lambda = { S_a = {a, (2,a), (3,a)} : a in N(w)-{2,3},
                     with the vertical (2,a)~(3,a) present }.
S_0 = Delta, S_1 = Delta_2. For a >= 4, S_a's local vertex a is never in
Gamma(Delta); S_a meets Gamma(Delta) only through far-far adjacencies of
(2,a) or (3,a) to B = (0,2) or C = (0,3). Makhnev's mu=2 argument = under
(*) none of those adjacencies exist, so S_a lands in Lambda_2 by L7.

L9. "Each Delta_2 in Lambda_2 has exactly 6 Lambda-neighbors in Lambda_1 and 6
in Lambda_2." Upper bound: each vertex of Delta_2 has 6 neighbors in
Gamma(Delta) (2 per root vertex), and (*) groups them so Delta_2 is 3-joined to
at most 6 members of Lambda_1... cap = 6. Count: by L8 each of the 12 Delta_1
sends 12 - 1 (Delta) - 1 (its Lambda_1-mate, from lambda_Lambda=1) = 10 edges
to Lambda_2; e(Lambda_1,Lambda_2) = 12*10 = 120 = 6*20: cap+average forces
exactly 6 each. The other 12 - 6 = 6 neighbors of Delta_2 avoid Gamma(Delta):
in Lambda_2.

Conclusion: Lambda_0 is an srg(33,12,1,6) subgraph of Lambda satisfying (*),
contradicting Theorem 1 (mu <= 3 or (27,10,1,5)). QED Theorem 2 (99-case).

## 3. Exact dependency map on (*)  [CORRECTED v2]

Which structure each lemma consumes, for root triangle Delta = ABC:

- L6: exactly the full C4-ness of the SIX fibers at A containing pair(B,C)
  (24 Gamma-edges: 12 verticals for T_x existence, 12 horizontals for the
  mate structure; chords auto-blocked at radius 1 given the verticals). This
  is a condition at ONE vertex per root choice — much narrower than the
  original v1 claim ("fibers at A, B, C"). Note the same 24 edges can be
  described from B's or C's frame; the fiber-internal description lives at A.
- L7: FOLLOWS from L6-clean at radius 1 (new v2 result, quota-verified). All
  five adjacency channels among an outside X's 6 mu-neighbors are blocked:
  [A]x[A] by the N(A)-matching; [B]x[B], [C]x[C] by lambda=1 (an edge there
  would lie in two triangles); [A]x[B], [A]x[C] because the share-y quota of
  {B,y} is consumed by the vertical {C,y}; [B]x[C] because {B,y}'s share-C
  quota is consumed by {C,y}. So L7 costs NOTHING beyond L6-clean.
- L8: for each T_x and each of its vertices w, the leak channels are governed
  by the fiber F0(w) = {pair(A-slot), pair(T_x-slot)} at w and by the
  S_a-fibers {pair(T_x-slot), pair(a)} at w. See Section 4 v2 (M1-M6).
  L6-clean at A propagates: the A-side horizontals/verticals ARE the F0(w)
  C4 edges (E1-E4) for every w in the 36 points (frame translation verified).
- L9: no new (*); counting from L6 + L8 exactness. 120 = 6*20 with cap 6.
  Deficits cannot cancel (cap is one-sided) — repair lever AND fragility.
- Theorem-1 invocation: needs (*) INSIDE Lambda_0 as a graph in its own
  right. This is an additional consumer of full (*), unmapped in v1, and an
  open item for any k<21 repair.

## 4. Damage taxonomy M1-M6  [CORRECTED v2 — supersedes the v1 D1-D4 ledger]

Setting: w-rooted frame of Section 2 v2 L8: Delta = {0,(0,2),(0,3)},
T_w = {w,2,3}, F0 = fiber {(0,1),(2,3)} at w with C4 edges
E1 = (0,2)-(0,3), E2 = (1,2)-(1,3), E3 = (0,2)-(1,2), E4 = (0,3)-(1,3).
Canonical leak candidate S_4 = {4, (2,4), (3,4)}. All claims below were
verified by exact quota arithmetic (script run 2026-07-05; see Sec. 7 v2).

- M1 (cross leak, alpha): (2,4)~(0,3). IMPOSSIBLE given E1 alone: (0,3)'s
  share-2 quota (=1) is consumed by (0,2). Radius-1 theorem. So this channel
  is closed for ANY Delta that exists as a triangle — regardless of fibers.
- M2 (cross leak, beta): (3,4)~(0,2). Mirror of M1 (share-3 quota at (0,2)
  consumed by (0,3) via E1). Closed unconditionally.
- M3 (share leak, alpha): (2,4)~(0,2). Requires BOTH (i) not-E3 — i.e. F0
  bad at w ((0,2)'s share-2 quota) — and (ii) fiber {(2,3),(4,5)} at w bad
  ((2,4)'s share-2 quota vs its horizontal (2,4)-(2,5)). TWO bad fibers at w:
  contradicts H20 directly. Closed under H20. (Mirror: (3,4)~(0,3).)
- M4 = M3's mirror (share leak, beta). Same two-defect forcing. Closed.
- M5 (mate-loss): F0 bad at w with E1, E2 present but E3 (or E4) missing.
  Then Delta_2 = {1,(1,2),(1,3)} exists, is 3-joined to T_w (label-forced),
  but is NOT 3-joined to Delta (needs E3 and E4) — so Delta_2 is in
  [T_w]_Lambda but outside Lambda_0: a genuine leak costing only ONE bad
  fiber at w. NOT closed by the budget at w. It IS closed whenever Delta is
  L6-clean (clean => E1-E4 hold at every w among the 36 points).
- M6 (vertical-loss): bad fiber {(2,3),pair(a)} at w kills the vertical
  (2,a)~(3,a): S_a does not exist, k_Lambda(T_w) drops (<= 2 losses per bad
  fiber). One bad fiber at w suffices; damages the L9 count 120 = 6*20.
  Bonus fact (verified): the same missing vertical also renders one fiber at
  vertex 2 AND one at vertex 3 non-C4 (the defect triple-charges T_w's other
  two vertices' budgets), which sharpens any global counting.

Consequence: the ONLY damage modes surviving H20 at the single-vertex level
are M5 and M6, and both are visible purely in w's rooted frame. The v1
interaction-bound paragraph (<= 24 incidences) is RETRACTED as frame-flawed.

## 5. The k=20 argument: proved pieces and precise gaps  [CORRECTED v2]

The v1 text of this section (slot taxonomy, "3 of 6 closed by hand",
Step-1 count 2+2+2<7, leak bound t<=24) is RETRACTED — it was derived in the
flawed frame. Corrected structure:

Hypothesis H20: every vertex of Gamma has >= 20 C4 fibers (with R230: each
vertex has exactly one bad fiber or none).

PROVED (radius-1, machine-verified quota arithmetic):
(P1) M1/M2 cross leaks are impossible for any existing Delta (Sec. 4 v2).
(P2) M3/M4 share leaks force two bad fibers at one vertex — impossible under
     H20.
(P3) If Delta is L6-clean then L7 holds verbatim (Sec. 3 v2) and — via the
     frame translation A-side horizontals/verticals => E1-E4 at each w — all
     M5 mate-losses are excluded, and Lambda_0 has exactly 33 members.

OPEN GAPS (the honest k=20 frontier):
(G-A) Clean-root existence: does H20 guarantee some triangle Delta with the
      6 pair(B,C)-fibers at A fully C4 AND with no M6 vertical-losses among
      its 12 T_x? Per vertex A, a bad fiber at A rules out at most 2 of the
      7 pair-choices (those whose 6-fiber set contains it), leaving >= 5
      L6-clean choices at A — but M6 damage lives at the 36 OTHER vertices
      and is not re-choosable from A. The M6 triple-charge fact (Sec. 4 v2)
      is the natural lever: each vertical-loss consumes the whole bad-fiber
      budget of THREE vertices; a global count over the 231 triangles vs the
      <= 99 bad fibers looks favorable but has NOT been completed rigorously.
(G-B) L9 damage arithmetic when some k_Lambda(T_x) < 12 (M6): with t lost
      verticals, e(Lambda_1,Lambda_2) = 120 - t and cap-6 counting alone no
      longer forces the (33,12,1,6) srg. Needs either G-A to force t = 0, or
      a discharging argument using the triple-charge.
(G-C) Theorem-1 application requires (*) INSIDE Lambda_0; under H20 this is
      not automatic and has no analysis yet.

STATUS: k=20 does NOT yet fall analytically. What is genuinely settled: every
leak mode except M6 vertical-loss is excluded under H20 once a clean root
exists; and all exclusion steps are radius-1 quota facts, individually
certifiable as trivial CNF/DRAT lemmas (see rep_table_v2.json, reps 1-4).
The two SAT-open probes (reps 5-6) encode M5 and M6 at a single vertex and
are conjectured SAT — i.e., not refutable locally; the remaining work is the
global counting (G-A, G-B) plus (G-C).

## 6. Descent limit  [CORRECTED v2]

- k=20: gaps G-A, G-B, G-C (Sec. 5 v2). The radius-1 closure of M1-M5 under
  a clean root is a genuine structural advance; the plausible finishing move
  is a discharging count using the M6 triple-charge. Assessment: reachable,
  not yet reached. (v1's "gap = 3 SAT-sized slot types" is retracted.)
- k=19 (up to 2 bad fibers per vertex): per-vertex clean pair-choices drop
  to >= 3 of 7 (2 bad fibers exclude <= 4), so L6-clean roots still exist at
  every vertex — BETTER than the v1 claim — but M3/M4 exclusion breaks (two
  bad fibers at one w are now allowed), reopening share leaks, and the M6
  budget doubles. The case tree grows but stays frame-local; machine-assisted
  progress plausible, analytic closure doubtful.
- k=18 and below: share leaks and vertical losses compound; the 33-triangle
  skeleton is no longer determined. The Makhnev route structurally ends
  here — consistent with the empirical hardness jump at 18.

## 7. Arithmetic verification log (exact, python)

- 99*14/2 = 693 edges; 693/3 = 231 triangles. OK
- |Gamma(Delta)| = 3 + 3*12 = 39; 99 - 39 = 60; 60/3 = 20. OK
- fibers: 84 far vertices, 21 = C(7,2) pair-classes, 84/21 = 4 per fiber. OK
- L9: 12*(12-2) = 120 = 6*20. OK
- Step 1: 6 = 2*3 < 7. OK   - Step 2: 2*12 = 24 < 120. OK
- k=19: 4*3 = 12 >= 7 (no clean root). OK
- (33,12,1,6) feasibility as srg: 6*(33-12-1) = 120 = 12*(12-1-1) = 120. OK —
  parameter-feasible, which is why Makhnev needs Theorem 1, not parameters.

[v1 flag, resolved in v2] The v1 constants and slot taxonomy were audited and
retracted; see the v2 sections above.

## 7b. Arithmetic verification log — v2 additions (exact, python, run 2026-07-05)

- Quota formula: for far vertex i, local x: #(far neighbors of i with x in
  label) = 2 - [x in label(i)] - [mate(x) in label(i)]. Source:
  honest_flip_cnf.py::build_base_cnf; re-derived by hand from lambda/mu.
- M1: E1 + (2,4)~(0,3) violates (0,3)'s share-2 quota (2 > 1). VERIFIED.
- M2: E1 + (3,4)~(0,2) violates (0,2)'s share-3 quota. VERIFIED.
- M3(i): E3 + (2,4)~(0,2) violates (0,2)'s share-2 quota. VERIFIED.
- M3(ii): (2,4)~(2,5) + (2,4)~(0,2) violates (2,4)'s share-2 quota. VERIFIED.
- Vertical + cross-leak conflict: (2,4)~(3,4) + (2,4)~(0,3) violates (2,4)'s
  share-3 quota. VERIFIED.
- M5 probe (20 fibers C4 + E1 + E2 + not-E3, 82 asserted edges): passes ALL
  radius-1 quota checks and pairwise common-neighbor caps. VERIFIED.
- M6 probe (20 fibers C4 + partial F_bad minus one vertical, 83 edges):
  passes all radius-1 checks. VERIFIED.
- Sanity: all-21-fibers-C4 assertion passes radius-1 (as expected: the R230
  kernel configuration is locally consistent). VERIFIED.
- L6-clean choices per vertex under H20: a bad fiber {P,Q} at A excludes the
  pair-choices p0 in {P,Q}: 7 - 2 = 5 >= 1. VERIFIED (trivial).
- k=19: 7 - 4 = 3 >= 1 clean pair-choices per vertex. VERIFIED (trivial).
