# Supersession Notice (R230, 2026-06-30)

This report is historical.  It was correct when written, but it predates the
R229/R230 rooted proof-SAT certificate.  The current repository verdict is the
checked computational nonexistence certificate documented in
`FINAL_REPORT_R230_NONEXISTENCE.md`, backed by
`scratchpad\root_cell_triangle_rep_cloud_r229_seq_intercoset\r229_all24_ascii_drat_checked_summary.json`.

---

# Conway's 99-graph problem — consolidated report of an autonomous research loop

**Question (OPEN; Conway's $1000 problem).** Does a strongly regular graph
**srg(99,14,1,2)** exist? — 99 vertices, 14-regular, every edge in exactly one
triangle (λ=1), every non-adjacent pair with exactly two common neighbours (μ=2).

**Outcome of this work.** The problem **remains open** — as it has since Biggs
(1969) / Conway (1975). No graph was constructed and no nonexistence proof was
found. What this loop produced is a body of **machine-verified, adversarially-checked
incremental results**: several closed attack-routes (with the exact reasons they
close), one genuinely-new proven structural theorem, new GF(7) invariants, an
honest debunking of a folklore "near-proof", a reproduction of the published
automorphism constraints, and an engineering advance that pushes one published-open
subcase one step past the prior compute wall. Every quantitative claim was validated
against the two real graphs in the family — rook(9)=srg(9,4,1,2) and the
Berlekamp–van Lint–Seidel graph srg(243,22,1,2) — so a method that would misclassify
a real graph was caught.

---

## 1. Frame: the problem is reduced to one open published cell

The λ=1,μ=2 family has exactly 5 feasible parameter sets; two exist (9, 243), three
are open (99, 6273, 494019), and **99 is the smallest open one**. Eigenvalues
14, **r=3 (mult 54)**, **s=−4 (mult 44)**; all classical feasibility conditions
(integrality, Krein, absolute bound) pass with slack. Local structure is forced:
N(v) ≅ 7K₂, the 231 triangles partition the 693 edges (7 per vertex).

Automorphism constraints (literature, reproduced): not vertex-transitive;
|Aut| divides 4158 = 2·3³·7·11; even ⇒ |Aut| divides 6 (Cesarz–Woldar 2023);
**order-11 ruled out**, **order-3 with fixed points (f=3) ruled out** (Behbahani
Thm 4.14). ⇒ the **sole surviving prime-order symmetry is order-3, fixed-point-free
(f=0)** — and that subcase is a literal "?" in Behbahani's Table 21 (his dedicated
orbit-matrix search never closed it). This is the one open cell the loop attacks.

## 2. Closed / exhausted attack routes (with the reason)

| Route | Result |
|---|---|
| Spectral / interlacing / subconstituent | EXHAUSTED, consistent. Γ₂(v) is walk-regular not SRG (refuted via BvLS); PSD window = Cauchy window; no force. |
| Geometric / partial-geometry | CLOSED. Neither G nor Ḡ is pseudo-geometric with a valid (s,t,α). |
| Local-fragment SAT | STRUCTURALLY VOID. Diameter 2 ⇒ the radius-2 ball *is* the whole graph; every proper fragment is SAT. |
| SOS / Lasserre SDP | CLOSED in-reach. Degree-2 = Krein = feasible; level ≥3 is 10⁷–10¹³ per side. |
| Two-graph / Seidel descent | VOID for the family (needs n=2(2k−λ−μ)=50≠99). |
| Metaheuristic construction | STRUCTURALLY HOPELESS ("golf-hole"; verified on BvLS). "No solution found" ⇒ no information. |
| n3=0 literature path | FULLY CHARACTERIZED — not a proof. [B] "n3=0⇒no srg(99,14,1,2)" is now RECOVERED + VERIFIED (Makhnev 1988 Thm 2; n3=0 forces a subconstellation srg(33,12,1,6) with non-integral multiplicities 180/7, 44/7; (99,14,1,2)-specific via k=6μ+2). But [A] "n3=0 is forced" is FALSE-as-stated: n3 is provably non-spectral (cospectral Rook₄ₓ₄ vs Shrikhande: prism counts 48 vs 0) and free (only 3∣n3). So [A]∧[B] do NOT chain into a proof. |
| **Rank-overflow (Shpectorov–Zhao port)** | **CLOSED by self-falsification.** Ported the 2025 method that killed srg(85,14,3,2); built a sound engine; but found an EXACT realizable flat step at a rank-34 node, breaking the strict-climb premise that bridged "rank-44 dead-end" → nonexistence. The kill path is dead. |

## 3. Genuinely new, verified results (the positive yield)

- **n3 ≥ 3 for any srg(99,14,1,2) (NEW, verified).** Combining the recovered+verified
  Makhnev 1988 Theorem 2 (n3=0 ⇒ nonexistence, parameter-specific) with the proof that
  n3 is NOT forced to 0 (n3 = 4158 − 3·nprism; provably non-spectral via the cospectral
  Rook₄ₓ₄/Shrikhande witness, prism counts 48 vs 0): **any srg(99,14,1,2), if it exists,
  must contain a disjoint triangle-pair joined by exactly 2 edges (n3 ≥ 3, 3∣n3)** — so it
  is structurally *unlike* both known members of its family (both have n3=0). The two-step
  literature narrative [A] symmetry⇒n3=0 ∧ [B] n3=0⇒nonexistence is now fully mapped: [B]
  is true & 99-specific, [A] is false-as-stated, so they do not chain into a proof.
- **The lift theorem (PROVEN, node-universal).** In the s=−4 Euclidean
  representation (dim 44, cos_adj=−2/7, cos_nonadj=1/28), the rigid 39-vertex
  triangle-ball Gram has an exact 8-dim kernel with a structural basis (3 "star" +
  6 "triple" vectors). This gives a closed-form colspace criterion proving that
  **97.3% of attachment types (210240/216000) can never extend "flat" at any node** —
  airtight linear algebra, not sampling.
- **The rank-44-only lemma (PROVEN):** a unit-vector border changes Gram rank by
  exactly 0 or 1, so a rank overflow can occur *only* at a rank-44 node.
- **The squeeze-ratio separator:** the real distinction between srg99 and its
  realizable siblings is global — forced ball rank/dim = 31/44 = 0.705 (srg99) vs
  60/110 = 0.545 (BvLS) — not a cosine criterion (a corrected earlier claim).
- **GF(7) p-rank invariants (new):** rank₇(A)=98, rank₇(N)=99 (the 231-triangle
  incidence is full row-rank over GF(7)), and the window rank₇(A+4I) ∈ [1,45] —
  all forced; provably non-obstructing (clean negative).
- **Orbit-matrix infrastructure:** a validated isomorph-free Z₃/f=0 orbit-matrix
  generator (R²=6J−R+12I; the (a,b)→(T,E) parity classes; forced row profiles; the
  A2-3-cycle disjointness lemma) and the within-row intersection-cut + leading-row
  canonicalization that breaks the prior row-2 wall on the a=24 cell.

## 4. The open subcase, precisely scoped

Z₃/f=0: a 33×33 orbit matrix in four parity classes
(a=24→(T,E)=(27,6); 22→(20,13); 20→(13,20); 18→(6,27)). **0 of 4 classes
certified-exhausted; 0 SAT orbit matrices found.** Measured frontier: with the
within-row lever, the smallest cell (a=24) now completes row 2 (prior wall) and
reaches max-row 4–8 of 33 before the node/time budget; the within-row width recurs
each row. This is the genuine compute frontier of orbit-matrix backtracking.

## 5. What it would take to go further (honest)

(a) Close a Z₃/f=0 cell: full per-row column-orbit canonicalization with proven
soundness at depth ≥3 (nauty-style isomorph rejection at every row), and/or
distributed completed-tree runs — a real engineering project, not a one-shot. (b) A
genuinely new global obstruction: every cheap/medium one tried is non-obstructing
because the parameters are too well-behaved; a kill likely needs a new idea, not a
new computation.

## 6. Honesty notes / weakest links
- The only real fpf-Z₃ control with *empty rows* is rook(9) (tiny); BvLS has E=0, so
  the empty-row cut's exactness rests on a synthetic cut==brute@t=33 check + an
  independent 586,575 double-count, not a large real graph with empty rows.
- Every "INFEASIBLE/UNSAT" in the artifacts refers to f=3 / order-11 / undersized
  sub-instances — NO srg99 class was certified infeasible; no timeout was relabeled.

Full per-result audit trail with scripts: progress.md (R1–R21). Reproduce core facts:
`python feasibility.py | battery.py | gates.py`; subcase engines in the same dir.
