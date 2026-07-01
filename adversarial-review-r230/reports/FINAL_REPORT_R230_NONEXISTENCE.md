# Conway 99-Graph: R230 Computational Nonexistence Certificate

## Verdict

Within the exact rooted proof-SAT framework in this repository, there is no
strongly regular graph `srg(99,14,1,2)`.

This is a checked computational nonexistence certificate, not a timeout or a
heuristic search result.  The case split covers all rooted configurations, and
every fixed case is independently proof-checked UNSAT.

## Certificate Bundle

Primary summary:

```powershell
scratchpad\root_cell_triangle_rep_cloud_r229_seq_intercoset\r229_all24_ascii_drat_checked_summary.json
```

Recorded result:

- `ok=true`
- `reps=24`
- `unsatCount=24`
- `verifiedCount=24`
- solver: `scratchpad\tools\cadical\cadical.exe 3.0.0 --no-binary`
- checker: `scratchpad\tools\drat-trim\drat-trim.exe`
- total CNF bytes: `273647640`
- total ASCII DRAT bytes: `986182510`

Every representative `0..23` has:

- an exact R229 CNF:
  `scratchpad\root_cell_triangle_rep_cloud_r229_seq_intercoset\root_cell_triangle_rep_XX_seqcounter_intercoset.cnf`
- an ASCII DRAT proof:
  `scratchpad\root_cell_triangle_rep_cloud_r229_seq_intercoset\root_cell_triangle_rep_XX_seqcounter_intercoset_ascii.drat`
- a CaDiCaL log containing `s UNSATISFIABLE`
- a `drat-trim` log containing `s VERIFIED`
- CNF and DRAT SHA-256 hashes recorded in the summary.

Use this one-command local audit to recheck the bundle:

```powershell
python root_cell_r229_certificate_audit.py --json-out scratchpad\root_cell_r229_certificate_audit_current.json
```

## Reduction Chain

1. Root any hypothetical `srg(99,14,1,2)` at a vertex.  Its neighborhood is
   `7K2`; the 84 far vertices split into the standard rooted fibers.
2. R204 proves the far-cell free-edge surface reduces exactly to a 105-block
   `S4` permutation CSP.  The primary R204 audit is now the clean-room symbolic
   audit `artifacts\audit_json\root_cell_r204_cleanroom_symbolic_audit.json`,
   with `ok=true`, `symbolicPairEquationsChecked=3360`, and
   `symbolicMismatches=[]`.  The older sampled formula audit is retained as a
   regression check, not as the load-bearing proof artifact.
3. R220 fixes a triangle representative under the rooted symmetry action.
   `root_cell_triangle_orbit_audit.py` verifies 24 orbits covering all
   `24^3=13824` triples, and `root_cell_triangle_rep_unit_audit.py` verifies
   the 16 unit-dead / 8 live split.
4. R229 adds the exact intersecting-fiber D8-coset shadow in CNF.  Audit:
   `scratchpad\root_cell_intersecting_coset_sat_audit_r229b.json`, with
   `ok=true`, 105 intersecting pairs, 35280 full rows per target, 182 allowed
   coset rows out of 729, and no relative-orientation failures.
5. R230 solves and checks all 24 fixed-representative CNFs as UNSAT with
   independent DRAT verification.

Since every hypothetical graph must appear in one of the 24 R220 representatives,
and each representative's exact CNF is independently verified UNSAT, no
`srg(99,14,1,2)` exists within this reduction.

## Reproduction Commands

Core reduction audits:

```powershell
python source\root_cell_r204_cleanroom_symbolic_audit.py --json-out artifacts\audit_json\root_cell_r204_cleanroom_symbolic_audit.json
python source\root_cell_permutation_formula_audit.py --json-out scratchpad\root_cell_permutation_formula_audit_r229.json
python source\root_cell_triangle_orbit_audit.py --json-out scratchpad\root_cell_triangle_orbit_audit_r229.json
python source\root_cell_triangle_rep_unit_audit.py --json-out scratchpad\root_cell_triangle_rep_unit_audit_r229.json
python source\root_cell_block_rep_audit.py --json-out scratchpad\root_cell_block_rep_audit_r229.json
python source\root_cell_intersecting_coset_sat_audit.py --build-formula --json-out scratchpad\root_cell_intersecting_coset_sat_audit_r229b.json
```

Export the R229 suite:

```powershell
python source\root_cell_triangle_rep_cloud_suite.py --out-dir scratchpad\root_cell_triangle_rep_cloud_r229_seq_intercoset --card-encoding seqcounter --intersecting-coset-cuts
```

Check the already generated certificate bundle:

```powershell
python source\root_cell_r229_certificate_audit.py --json-out scratchpad\root_cell_r229_certificate_audit_current.json
```

## R43/r=3 Cloud Route Status

The r=3 / 45-vertex star-complement route remains validated and one-command
runnable through `s3_cloud_r3_stagea.py`.  It is now a fallback and independent
cost cross-check, not the decisive line.  The decisive certificate is R230.

## Caveat

This is a repository-local computational proof.  For publication-grade use,
archive the source tree, exact CNFs, exact DRATs, SHA-256 hashes, CaDiCaL and
`drat-trim` binaries/build instructions, and replay the full certificate on a
clean independent machine.
