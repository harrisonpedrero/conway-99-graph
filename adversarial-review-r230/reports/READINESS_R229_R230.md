# R229/R230 Readiness Verdict

## Status

A checked computational nonexistence certificate has been completed for
`srg(99,14,1,2)` inside this repository's rooted proof-SAT framework.

The earlier R229 readiness note said proof tooling was missing.  R230 closes
that gap: all 24 R220 triangle representatives have exact R229 CNFs, CaDiCaL
ASCII DRAT proofs, and independent `drat-trim` verification logs.

## Evidence In Hand

Reduction-chain audits passed:

- R204 formula audit: `ok=true`, `pairs_checked=69720`.
- R220 triangle-orbit audit: `ok=true`, 24 orbits over `24^3=13824` triples.
- R220 unit audit: `ok=true`, 16 unit-dead reps and 8 survivor reps.
- R229 coset-SAT audit: `ok=true`, 105 intersecting pairs, 35280 full rows per
  target, 182 allowed coset rows out of 729, and no orientation failures.

Proof certificate summary:

```powershell
scratchpad\root_cell_triangle_rep_cloud_r229_seq_intercoset\r229_all24_ascii_drat_checked_summary.json
```

Summary fields:

- `ok=true`
- `reps=24`
- `unsatCount=24`
- `verifiedCount=24`
- solver: `scratchpad\tools\cadical\cadical.exe 3.0.0 --no-binary`
- checker: `scratchpad\tools\drat-trim\drat-trim.exe`
- CNF bytes checked: `273647640`
- ASCII DRAT bytes checked: `986182510`

Every representative `0..23` has a solve log with `s UNSATISFIABLE` and a
checker log with `s VERIFIED`.  The eight previously live R220 reps
`[0,2,7,8,10,15,21,22]` are included in this all-24 certificate.

## One-Command Local Audit

Run:

```powershell
python root_cell_r229_certificate_audit.py --json-out scratchpad\root_cell_r229_certificate_audit_current.json
```

This rechecks the certificate summary, all CNF/DRAT hashes, the solve/check log
markers, and the reduction-chain audit JSON files.

## Verdict

Ready to stop search locally: the rooted proof-SAT route covers all cases and
every case is independently proof-checked UNSAT.  Further work should be
replication and archival, not more heuristic search: rerun the certificate audit
on a clean machine, preserve the CNF/DRAT bundle and hashes, and write the
R204/R220/R229 reductions as a publication-grade proof note.
