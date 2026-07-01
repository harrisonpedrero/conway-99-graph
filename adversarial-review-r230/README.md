# R230 Adversarial Review Bundle

## Claim Under Review

The repository-local R230 certificate proves, computationally, that no strongly
regular graph `srg(99,14,1,2)` exists within the exact rooted proof-SAT reduction
implemented here.

This bundle is organized for adversarial review: it separates the mathematical
reduction, the SAT encoding, the independent proof-check evidence, and the
large artifacts that must be regenerated or supplied outside normal Git history.

## Contents

- `latex/` - LaTeX writeup of the reduction and certificate.
- `reports/` - consolidated result reports and the historical superseded notes.
- `source/` - the Python scripts needed for the R204/R220/R229/R230 audits and
  CNF generation.
- `artifacts/audit_json/` - audit summaries, the all-24 proof summary, and the
  manifest from the original run.
- `artifacts/proof_logs/` - copied CaDiCaL and `drat-trim` logs for all 24
  representatives.
- `artifacts/large_artifacts_manifest.csv` - CNF/DRAT paths, sizes, and hashes.
- `scratchpad/root_cell_triangle_rep_cloud_r229_seq_intercoset/` - the 24 CNF
  bodies and 24 ASCII DRAT proof bodies, stored via Git LFS.
- `scripts/` - lightweight bundle checks and full replay helpers.

The most important human entry point is
`reports/R204_HUMAN_CHECKABLE_REDUCTION.md`.  It spells out the rooted
fiber/permutation reduction and points to the clean-room symbolic audit that
checks it exactly.

## Fast Bundle Check

From this folder:

```powershell
python scripts/verify_bundle_metadata.py
```

This does not re-run SAT or DRAT verification.  It checks that the pushed bundle
is internally consistent: 24 representatives, 24 UNSAT records, 24 verified
records, all reduction audits green, and all copied solve/check logs contain the
expected markers.

## Clean-Room Replay

From this folder:

```powershell
python scripts/clean_room_replay.py
```

This runs the clean-room R204 symbolic audit, the compact metadata/log check,
and the full hash/log certificate audit against the included CNF/DRAT bodies.
It does not need CaDiCaL, `drat-trim`, PySAT, or OR-Tools because it rechecks
the already included certificate and the R204 symbolic reduction.

## Full Adversarial Replay

The large CNF and DRAT files are included via Git LFS.  After cloning, run
`git lfs pull` if the files are present only as small pointer files.  To replay
the certificate fully:

1. Install Python dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

2. Optional independent rebuild of all 24 R229 CNFs:

   ```powershell
   powershell -ExecutionPolicy Bypass -File scripts/rebuild_all24_cnf.ps1
   ```

3. Build or provide CaDiCaL and `drat-trim` executables.  The original checked
   run used:

   - `scratchpad\tools\cadical\cadical.exe` version `3.0.0`, with `--no-binary`
   - `scratchpad\tools\drat-trim\drat-trim.exe`

4. Re-run SAT proof generation and DRAT checking:

   ```powershell
   powershell -ExecutionPolicy Bypass -File scripts/recheck_all24_with_cadical.ps1
   ```

5. Run the full certificate audit after the CNF/DRAT files are present:

   ```powershell
   python source/root_cell_r229_certificate_audit.py `
     --json-out scratchpad/root_cell_r229_certificate_audit_replay.json
   ```

The final command should report `ok=true`, `unsatCount=24`,
`verifiedCount=24`, and `failures=[]`.

## Review Checklist

1. Read `reports/R204_HUMAN_CHECKABLE_REDUCTION.md`.
2. Run `python scripts/clean_room_replay.py`.
3. Inspect the R204 root-cell reduction in `source/root_cell_permutation_sat.py`
   and `source/root_cell_cpsat.py`.
4. Re-run the reduction-chain audits listed in
   `reports/FINAL_REPORT_R230_NONEXISTENCE.md`.
5. Confirm the R220 orbit split covers all `24^3=13824` triangle assignments.
6. Confirm the R229 D8-coset projection audit has no orientation failures and
   matches the CP-SAT source projection.
7. Pull or rebuild CNFs and compare their SHA-256 hashes against
   `artifacts/large_artifacts_manifest.csv`.
8. Re-run CaDiCaL with ASCII DRAT output and independently check every proof
   with `drat-trim`.

## Caveat

This bundle is not a journal article and not an independent third-party replay.
It is a compact handoff for adversarial review.  The most important next step is
an independent clean-machine replay of the CNF generation and DRAT checking.
