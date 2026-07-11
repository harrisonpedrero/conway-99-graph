# Exact Gram / Euclidean-Representation Certificates

A second, independent certification method for the same ladder theorem the SAT
work targets ("no vertex of a hypothetical `srg(99,14,1,2)` has many C4
fibers"). Where the SAT ladder proves each residual case by a solver plus a
DRAT/LRAT proof checker — with proof bodies up to 28 GB — this method proves
the same cases with **kilobyte-scale exact rational certificates checkable in
exact arithmetic**, and shows that a large part of the ladder needs no SAT
search at all.

This note states precisely what the method proves, what it rests on, and what
it does **not** prove. As with the rest of this repository, the headline
constraint is honesty: **Conway's problem remains open.**

## The method in one paragraph

A hypothetical `srg(99,14,1,2)` has adjacency eigenvalues `14, 3, -4` with
multiplicities `1, 54, 44`. Represent its vertices as unit vectors in the
`theta = -4` eigenspace `E` (dimension 44). Inner products depend only on
adjacency (the cosine sequence; Godsil, *Algebraic Combinatorics*, Ch. 13;
Brouwer–Cohen–Neumaier §4.1B):

```text
w0 = 1,   w1 = theta/k = -2/7  (adjacent),   w2 = 1/28  (non-adjacent).
```

For **any** set of vertices whose pairwise adjacencies are known, the Gram
matrix (1 on the diagonal, `w1` on edges, `w2` on non-edges) is completely
determined and **must be positive semidefinite**. Rooted around a vertex,
unknown far–far adjacencies become variables `x in [0,1]` (each Gram entry is
affine in `x`), constrained by exact rooted counting rows. If no completion of
`x` — not even a fractional one — makes the Gram matrix PSD, then that rooted
configuration is impossible. The infeasibility is witnessed by an **exact
rational certificate**: a PSD matrix `Z` and nonnegative rational multipliers
whose weak-duality combination is a strictly negative constant. No solver and
no floating point enter the accepted proof; a standalone checker re-derives
every row and checks `Z` PSD by exact `LDL^T`.

## What is proved

**1. A four-core exclusion theorem (exact, certificate-backed).**
Fix a root and index its seven matched local pairs `0..6`; let `F_ij` be the
four far vertices whose two local neighbours have indices `i,j`. For each of
the exceptional-index graphs

```text
C3 (triangle), C5 (5-cycle), C7 (7-cycle), K4-e ("K4ish"),
```

if every fiber outside the graph is a good C4 fiber and every fiber inside it
is genuinely non-C4, then no such rooted configuration exists — for every
matching state and every `S7`-labelled copy. Each core has one exact rational
certificate (`kappa < 0`, ranks 27/35/43/39). A hardened standalone verifier
accepts all four and rejects a suite of adversarial mutations (float-forging,
cross-core substitution, duplicate keys, non-canonical rationals).

**2. A ladder-wide screen (this bundle's `scratchpad/ladder/psd_screen/`).**
Every residual orbit of the certificate ladder was run through the same
one-shot test. Across the historical rungs k18–k14, **14 of the 20 dense-core
residuals** carry exact Gram certificates, and **the entire forcing (Part-A)
layer — all 122 orbit types across k18–k14 — is reproduced by exact rooted
propagation alone**, with no SAT search: coordinate-balance counting forces the
designated fiber to be C4, contradicting the all-non-C4 hypothesis. The six
residuals that resist are exactly the even/degree-heavy cores:

```text
k17 C4-cycle,  k15 K4,  k15 K2,3,  k15 C6,  k14 res1,  k14 res6.
```

These six still rest on their verified SAT/LRAT certificates. The SAT ladder
itself has since reached k=13 (all 22 dense-core residuals UNSAT, 450 forcing
certificates, no floor; one residual's proof is being re-verified — see
`../theorem_k19/README_theorem_k19.md`). The Gram screen has been run over the
residual orbits of k13 down through k8 as well, with exact certificates for the
kills recorded in the working area; that descent is ongoing.

**3. A global first-moment survivor contains no graph.**
An exact rational point survives the uncoupled 99-vertex first-moment Fantope
model (`G = (27I - 9A + J)/28` inside `0 <= G <= 9I/4`). It is a genuine
integrality-gap artifact, not a near-graph: its Gram rank is 84 (a graph needs
44) and its defect is `4800/7` (a graph has 0). Its selector marginal pins the
expected number of exceptional fibers at exactly 7. But every rooted
configuration with 7 or fewer exceptional fibers is impossible — this is exactly
the "no vertex with ≥14 C4 fibers" ladder theorem, established by the SAT ladder
and reproved here for every case except the six excepted cores. So a real vertex
has at least 8 exceptional fibers, no mixture of real vertices can average 7,
and the survivor contains no graph. This matches the internal finding that the
next model must carry joint support–adjacency moments.

## What it rests on (and what it does not)

The accepted proof base is:

- the rooted `srg(99,14,1,2)` counting model — that a hypothetical graph
  induces the rooted far-degree, local–far quota, and far–far common-neighbour
  equations (the **same** modelling bridge the SAT ladder assumes);
- the standard `theta = -4` Euclidean representation of a strongly regular
  graph;
- two proved rooted counting lemmas — **Coordinate-Balance** (an exact per-
  coordinate far-neighbour demand) and **Side-Complete-Means-C4** (four present
  side edges force a C4 fiber); the coordinate-balance rows are load-bearing
  (the pure Gram/box relaxation is feasible without them);
- exact rational weak-duality / `LDL^T` verification.

It does **not** rest on a SAT solver, on a DRAT/LRAT proof checker's soundness,
on the R204 forced-edge "kernel," or on any trust in a CNF encoding beyond the
counting model. Relative to the SAT ladder it removes the solver-and-checker
trust and the multi-gigabyte artifacts, replacing them with certificates a
person can re-check in exact arithmetic.

## What it does NOT prove

- Nonexistence of `srg(99,14,1,2)`. Conway's problem stays open.
- Anything about vertices with 12 or fewer C4 fibers (the SAT ladder reached
  k=13; the descent below that is ongoing, not complete).
- The six resisting cores by this method — they remain SAT/LRAT-certified only.
- Realizability: a PSD-feasible or fractional survivor is not a graph.
- Independence from the counting model, or a third-party replay. The exact
  certificates and their standalone checker have been re-implemented and
  exact-arithmetic verified **within the project**; they have not yet been
  replayed by an outside party.

## Relation to the SAT ladder

The two methods target the same fiber-completion statement and agree wherever
both run. The odd-cycle and small-core residuals (C3, C5, C7, K4-e, and
several dense k14/k15 cores) that the SAT ladder proved with large DRAT/LRAT
proofs now also have small exact Gram certificates. The forcing layer that the
SAT ladder proved with hundreds of per-fiber defect certificates is reproduced
by exact propagation. The six even/degree-heavy cores are where the SAT ladder
remains the only certification and where the method's own analysis explains the
resistance (odd cycles die; even cycles, `K4`, and `K2,3` do not, under these
relaxations).

## Where the artifacts are, and how to check them

The exact certificates, the generator, and the standalone exact-arithmetic
verifier live in this bundle's ignored working area,
`adversarial-review-r230/scratchpad/ladder/psd_screen/` (kept out of Git along
with the large solver bodies). A curated, self-contained subset can be promoted
into the tracked tree on request. The verifier re-derives, for each
certificate: the rooted state and its known/unknown far pairs, every
coordinate-balance and side-sum row, the PSD property of `Z` by exact `LDL^T`,
exact multiplier nonnegativity, exact stationarity, and the strictly negative
constant — using only Python's `fractions`, with no solver, no numpy, and no
floating point in the acceptance path.
