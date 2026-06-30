# Large Proof Artifacts

The checked R230 run produced:

- 24 CNF files totaling `273647640` bytes.
- 24 ASCII DRAT proof files totaling `986182510` bytes.

Those bodies are not committed here because several individual DRAT proofs are
larger than GitHub's normal 100 MB file limit:

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

To recreate the missing bodies, use:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/rebuild_all24_cnf.ps1
powershell -ExecutionPolicy Bypass -File scripts/recheck_all24_with_cadical.ps1
```

Then run:

```powershell
python source/root_cell_r229_certificate_audit.py `
  --summary artifacts/audit_json/r229_all24_ascii_drat_checked_summary.json `
  --json-out scratchpad/root_cell_r229_certificate_audit_replay.json
```

The replay audit should report `ok=true`, `unsatCount=24`, `verifiedCount=24`,
and no failures.
