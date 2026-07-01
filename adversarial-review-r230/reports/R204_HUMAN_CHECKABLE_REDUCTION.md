# R204 Human-Checkable Reduction Note

## Purpose

This note isolates the load-bearing R204 step in the R230 certificate:

> after rooting a hypothetical `srg(99,14,1,2)`, the 84 far vertices can be
> represented by 105 permutation blocks in `S4`, and the compact R204
> equality-count equations are exactly the rooted far-pair SRG equations.

The original sampled regression check is no longer the primary evidence.  The
primary evidence is now the clean-room symbolic audit:

```powershell
python source\root_cell_r204_cleanroom_symbolic_audit.py `
  --json-out artifacts\audit_json\root_cell_r204_cleanroom_symbolic_audit.json
```

Recorded result: `ok=true`, `symbolicPairEquationsChecked=3360`,
`symbolicMismatches=[]`.

## Rooted Far Labels

Root a hypothetical graph at a vertex `r`.  Its neighborhood is `7K2`; write the
14 local vertices as matched pairs

```text
{0,1}, {2,3}, ..., {12,13}.
```

A far vertex is adjacent to exactly two local vertices, and not to both ends of
one matched pair.  Thus the far labels are

```text
(a,b), 0 <= a < b < 14, b != a^1.
```

Here is the bijection, explicitly.  If `x` is far from `r`, then `r,x` are a
nonedge, so `x` has exactly `mu=2` neighbors in `N(r)`.  Those two local
neighbors cannot be a matched pair: otherwise that local edge would have both
`r` and `x` as common neighbors, contradicting `lambda=1`.  Conversely, any
non-matched local pair `{a,b}` is a nonedge with common neighbor `r`.  Since
`N(r)` is a matching, no local vertex is adjacent to both `a` and `b`; `mu=2`
therefore gives a unique second common neighbor, and it is a far vertex with
label `(a,b)`.
Thus the 84 far vertices are in bijection with the `C(14,2)-7 = 84` allowed
labels.

Group labels into fibers by the two matched-pair indices appearing in the
label.  There are `C(7,2)=21` fibers, and each fiber has four vertices.

## Forced Edges Inside and Between Fibers

For two far labels `x,y`, let `ov=|label(x) cap label(y)|`.

- Same fiber: the two labels either share one local vertex or are opposite in
  the fiber square.
  - If `ov=1`, the far edge is forced present.
  - If `ov=0`, the far edge is forced absent.
  So each fiber is a forced `C4`.
- Two fibers sharing one matched-pair index: the far edge is forced absent.
- Two disjoint fibers: the edge is a genuine free variable.

These are the only free edges in the rooted far graph.

Equivalently, for a fiber on matched pairs `{P,Q}`, with endpoints
`P={p0,p1}` and `Q={q0,q1}`, the four labels are `(pi,qj)`.  The forced
same-fiber graph is the square on these four labels, joining labels with one
equal endpoint and not joining opposite corners.  If two fibers share exactly
one matched-pair index, every cross-pair between them is a forced nonedge.  If
the two fiber indices are disjoint, the rooted equations leave the cross-edge
unfixed.  This is exactly the table used by the clean-room audit's
`forced_far_edge`: same fiber returns `1` for `ov=1` and `0` for `ov=0`;
disjoint fibers return `None`; all other distinct-fiber pairs return `0`.

## Why Disjoint Fiber Blocks Are Permutation Matrices

Fix one fiber `F`.  Its four vertices each have total far degree `k-2=12`.
Inside `F`, each vertex has two forced `C4` neighbors.  Vertices in fibers that
intersect `F` are forced nonneighbors.  Therefore each vertex in `F` has exactly

```text
12 - 2 = 10
```

free neighbors, all lying in the ten fibers disjoint from `F`.

Now take two distinct vertices `x,y` in the same fiber `F`.

- If `x,y` are adjacent in the `C4`, the SRG far-pair equation gives
  `common_F(x,y)=0`.
- If `x,y` are opposite in the `C4`, the two other vertices of `F` already give
  the required two far common neighbors, so again `x,y` share no free neighbor.

Thus the four free-neighbor sets of the four vertices of `F` are pairwise
disjoint.  Their total size is `4*10=40`.  The candidate free-neighbor universe
outside `F` is exactly ten disjoint fibers times four vertices, also `10*4=40`.
So every candidate vertex in every disjoint fiber is adjacent to exactly one
vertex of `F`.

Applying the same argument with a disjoint target fiber `G` fixed shows every
vertex of `F` is adjacent to exactly one vertex of `G`.  Hence each disjoint
`4x4` block has every row and every column equal to one: it is a permutation
matrix.  With 105 disjoint fiber pairs, the free surface is a `105`-block
`S4` assignment.

The clean-room audit checks this finite certificate as:

```json
"permutationBlockCertificate": {
  "forcedDegreeInsideFiber": [2],
  "freeDegreePerVertex": 10,
  "disjointFibersPerFiber": [10],
  "candidateVerticesPerFiber": 40,
  "coveredByFourDisjointFreeNeighbourSets": 40,
  "ok": true
}
```

## Why the Compact Pair Equation Is Exact

For any two far vertices `x=(F,u)` and `y=(G,v)` in distinct fibers, the rooted
far-pair equation is

```text
common_F(x,y) + edge_F(x,y) = 2 - |label(x) cap label(y)|.
```

R204 expands the left side using the permutation blocks:

- For every fiber `H` disjoint from both endpoint fibers, the common-neighbor
  contribution is one exactly when the image of position `u` in block `F-H`
  equals the image of position `v` in block `G-H`.
- If `F` and `G` are disjoint, the endpoint edge `edge_F(x,y)` is the direct
  block entry.
- If `F` and `G` are disjoint, common neighbors may also lie inside the endpoint
  fibers.  Those are exactly the forced `C4` neighbors of `x` reached by `y`'s
  inverse block, and symmetrically for `y`.
- If `F` and `G` intersect, the endpoint edge is forced zero and there are no
  endpoint-fiber free terms.

The clean-room audit independently expands the full far-pair equation as a
symbolic multiset of Boolean terms, expands the compact R204 equation as a
second symbolic multiset, and compares them for every distinct-fiber far pair.
It checks:

```json
"symbolicPairEquationsChecked": 3360,
"pairTypeHistogram": {
  "disjoint_fibers": 1680,
  "intersecting_fibers": 1680
},
"rhsHistogram": {
  "1": 840,
  "2": 2520
},
"symbolicMismatches": []
```

This is finite and exact.  It does not sample permutation assignments.

## What This Does Not Prove Alone

R204 does not by itself prove nonexistence.  It proves that the rooted search
surface is exactly the 105-block `S4` permutation CSP with the compact far-pair
equations.  The later R220/R229/R230 artifacts then split, strengthen, encode,
and proof-check every case.
