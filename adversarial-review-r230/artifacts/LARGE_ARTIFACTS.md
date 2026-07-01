# Large Proof Artifacts

The checked R230 run produced:

- 24 CNF files totaling `273647640` bytes.
- 24 ASCII DRAT proof files totaling `986182510` bytes.

Those bodies are included in this repository via Git LFS under:

```text
scratchpad/root_cell_triangle_rep_cloud_r229_seq_intercoset/
```

Several individual DRAT proofs are larger than GitHub's normal 100 MB file
limit, so they cannot live in ordinary Git blobs:

- rep 15: `171402353` bytes
- rep 8: `160661493` bytes
- rep 21: `146836080` bytes
- rep 10: `121864895` bytes
- rep 22: `110709987` bytes
- rep 2: `106367502` bytes

The exact paths, sizes, and SHA-256 hashes are in:

```text
artifacts/large_artifacts_manifest.csv
```

If a checkout contains only LFS pointer files, run:

```powershell
git lfs pull
```

To independently recreate the bodies, use:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/rebuild_all24_cnf.ps1
powershell -ExecutionPolicy Bypass -File scripts/recheck_all24_with_cadical.ps1
```

Then run:

```powershell
python source/root_cell_r229_certificate_audit.py `
  --json-out scratchpad/root_cell_r229_certificate_audit_replay.json
```

The replay audit should report `ok=true`, `unsatCount=24`, `verifiedCount=24`,
and no failures.
