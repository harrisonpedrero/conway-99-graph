# Literature Index (primary sources for the corrected R230 claim)

PDFs are kept locally (not committed - publisher/arXiv licensing). Fetch from the
links below; the load-bearing quotes were verified against the actual texts on
2026-07-01 during the adversarial review.

1. **A. A. Makhnev**, "O silno regulyarnykh grafakh s lambda=1" [On strongly
   regular graphs with lambda=1], *Mat. Zametki* **44**:5 (1988) 667-672;
   English transl. *Math. Notes* **44** (1988) 847-850.
   Free Russian original: mathnet.ru, ID mzm4220.
   - Defines condition (*): any pair of triangles joined by at least two edges
     is joined by exactly three.
   - Proves (p. 669) that under (*) every quadrilateral generates an induced
     srg(9,4,1,2).
   - **Theorem 2** (verified verbatim in the OCR text): "Ne sushchestvuet
     sil'no regulyarnykh grafov s parametrami (99,14,1,2) i (115,18,1,3),
     udovletvoryayushchikh usloviyu (*)" - no srg(99,14,1,2) satisfying (*)
     exists. Framed as a partial answer to Seidel's question.

2. **A. Keramatipour**, "Approaching the Conway-99 problem using SAT solvers",
   MPhil thesis, University of Cambridge, June 2023; arXiv:2604.23037.
   - Definition 12: the "Paley(9) pattern" == the fiber-C4 forced-edge table at
     every vertex.
   - **Theorem 3.4.2** (verified): "If a (99,14,1,2) strongly regular graph
     exists, it cannot follow the Paley(9) pattern."
   - Theorem 3.4.3: no 11 independent Paley(9) subgraphs.
   - **Conjecture 3.4.4**: no Paley(9) subgraph occurs at all.

3. **P. G. Cesarz, A. J. Woldar**, "On the automorphism group of a putative
   Conway 99-graph", *Algebraic Combinatorics* (doi 10.5802/alco.418);
   arXiv:2308.02978.
   - Lemma 4.8 (unconditional): coordinate balance of the 12 far neighbors.
   - **Remark 5.6** (verified verbatim): "It is currently unclear to us if a
     Conway 9-graph QR(9) (aka Paley graph of order 9) exists inside a putative
     Conway 99-graph."

4. **S. Lou, M. Murin**, "On the strongly regular graph of parameters
   (99,14,1,2)", MIT PRIMES-USA, 2014.
   - Theorem 2.1: Paley(9)-minus-an-edge closure.

5. **R. Reimbayev**, "The Subgraphs of Order Six...", arXiv:2508.03377 (2025).
   - Six-vertex census linear in n3; n3=0 is equivalent to the global
     Paley-pattern hypothesis; cites Makhnev for the fatal consequence.

6. **H. A. Wilbrink, A. E. Brouwer**, "A (57,14,1) strongly regular graph does
   not exist", Math. Centrum ZW 121/78 (1978) = *Indag. Math.* **45** (1983)
   117-121. Rooted 7K2 local analysis for the mu=4 sibling parameters.

7. **H. A. Wilbrink**, "On the (99,14,1,2) strongly regular graph", in *Papers
   dedicated to J. J. Seidel*, EUT Report 84-WSK-03 (1984) 342-355.
   No automorphism of order 11; orbit-matrix method.
