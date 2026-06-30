$ErrorActionPreference = "Stop"

$root = Resolve-Path (Join-Path $PSScriptRoot "..")
$source = Join-Path $root "source"
$outDir = Join-Path $root "scratchpad\root_cell_triangle_rep_cloud_r229_seq_intercoset"
New-Item -ItemType Directory -Force -Path $outDir | Out-Null

$env:PYTHONPATH = $source

for ($idx = 0; $idx -lt 24; $idx++) {
  $cnf = Join-Path $outDir ("root_cell_triangle_rep_{0:D2}_seqcounter_intercoset.cnf" -f $idx)
  $json = Join-Path $outDir ("root_cell_triangle_rep_{0:D2}_seqcounter_intercoset_export.json" -f $idx)
  python (Join-Path $source "root_cell_permutation_sat.py") `
    --no-solve `
    --card-encoding seqcounter `
    --triangle-rep-index $idx `
    --intersecting-coset-cuts `
    --cnf-out $cnf `
    --json-out $json
}

Write-Host "Wrote all 24 CNFs under $outDir"
