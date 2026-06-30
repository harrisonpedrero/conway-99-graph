$ErrorActionPreference = "Stop"

$root = Resolve-Path (Join-Path $PSScriptRoot "..")
$outDir = Join-Path $root "scratchpad\root_cell_triangle_rep_cloud_r229_seq_intercoset"
$cadical = Join-Path $root "scratchpad\tools\cadical\cadical.exe"
$dratTrim = Join-Path $root "scratchpad\tools\drat-trim\drat-trim.exe"

if (-not (Test-Path $cadical)) {
  throw "Missing CaDiCaL executable: $cadical"
}
if (-not (Test-Path $dratTrim)) {
  throw "Missing drat-trim executable: $dratTrim"
}

for ($idx = 0; $idx -lt 24; $idx++) {
  $cnf = Join-Path $outDir ("root_cell_triangle_rep_{0:D2}_seqcounter_intercoset.cnf" -f $idx)
  $drat = Join-Path $outDir ("root_cell_triangle_rep_{0:D2}_seqcounter_intercoset_ascii.drat" -f $idx)
  $solveLog = Join-Path $outDir ("root_cell_triangle_rep_{0:D2}_cadical_ascii_proof.log" -f $idx)
  $checkLog = Join-Path $outDir ("root_cell_triangle_rep_{0:D2}_drat_trim_ascii.log" -f $idx)

  if (-not (Test-Path $cnf)) {
    throw "Missing CNF for representative $idx`: $cnf"
  }

  & $cadical --no-binary $cnf $drat | Out-File -FilePath $solveLog -Encoding utf8
  & $dratTrim $cnf $drat | Out-File -FilePath $checkLog -Encoding utf8

  if (-not (Select-String -Path $solveLog -Pattern "s UNSATISFIABLE" -Quiet)) {
    throw "CaDiCaL did not report UNSAT for representative $idx"
  }
  if (-not (Select-String -Path $checkLog -Pattern "s VERIFIED" -Quiet)) {
    throw "drat-trim did not verify representative $idx"
  }
}

Write-Host "All 24 representatives solved UNSAT and verified."
