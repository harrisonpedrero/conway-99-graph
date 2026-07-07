# cake_lpr — formally-verified LRAT proof checker

The k=15 K_{2,3} residual (`certificates/k15/`, res3) has an UNSAT proof (22.4 GB
LRAT) too large for `drat-trim`'s backward-mode checker to verify locally (it
timed out at 3.9 h). It is instead verified by **cake_lpr**, a LRAT/LPR proof
checker whose checking core is **formally verified in HOL4/CakeML** (Tan, Heule,
Myreen, "Verified Propagation Redundancy and Compositional UNSAT Checking in
CakeML"). cake_lpr is a *stronger* guarantee than drat-trim: its soundness is a
machine-checked theorem, not just extensive testing.

## Why not the bundled `lrat-check`?

An earlier revision used `scratchpad/drat-trim/lrat-check.exe` (the standard
Heule `lrat-check`). An adversarial audit found — and we reproduced — that it
prints `c VERIFIED` on a hand-crafted **bogus** empty-clause proof of a
*satisfiable* formula (`p cnf 2 2 / 1 0 / 2 0` with proof `3 0 1 2 0`), because
its "no-conflict ⇒ FAILED" guard (lrat-check.c line 161) is commented out. It
verifies genuine solver output correctly but trusts the hints, so it does not
meet this project's "never trust the solver" bar. All lrat-check corroboration
claims were retracted; cake_lpr replaces it for large proofs.

## Source and provenance

- Upstream: `https://github.com/tanyongkiam/cake_lpr` (ships a pre-compiled,
  CakeML-generated `cake_lpr.S`; no CakeML compiler needed to build).
- `cake_lpr.S` sha256 (upstream, verified checking core, unmodified logic):
  `c5e6f9f60ea674c3...` (full value in this repo's build log; also in upstream
  `cake_lpr.sha256`).
- Two **build-shim-only** tweaks were required to build on Windows with
  llvm-mingw. NEITHER changes the verified checking core:
  1. Stripped the `.func`/`.endfunc` assembler directives from `cake_lpr.S`
     (debugger metadata only, emit no code; the LLVM integrated assembler
     rejects them). Result: `cake_lpr_clean.S`.
  2. Patched `basis_ffi.c` (the untrusted C FFI/runtime shim, NOT the verified
     CakeML core): `unsigned long` → `unsigned long long` and `strtoul` →
     `strtoull` for the heap/stack byte-size arithmetic. On Windows (LLP64)
     `unsigned long` is 32-bit, so a requested heap > 4 GB overflowed to 0.
     See `basis_ffi_llp64.patch` (against upstream `basis_ffi.c`).
     patched sha256: `cbcd8ed9f42b6174...`.

## Build

    git clone https://github.com/tanyongkiam/cake_lpr
    cd cake_lpr
    sed -E '/^\s*\.(func|endfunc)/d' cake_lpr.S > cake_lpr_clean.S
    # apply basis_ffi_llp64.patch  (or use the basis_ffi_patched.c here)
    gcc -O2 basis_ffi_patched.c cake_lpr_clean.S -o cake_lpr_sound.exe -std=c99

## Validation performed

- `cake_lpr_sound.exe example.cnf example.lpr` → `s VERIFIED UNSAT` (bundled
  UNSAT example accepted).
- `cake_lpr_sound.exe` on the bogus SAT proof above → **rejected** (NOT
  verified) — the exact proof the unsound `lrat-check` accepted.
- Heap/stack are set at runtime, in MB: `CML_HEAP_SIZE`, `CML_STACK_SIZE`.
  The k15 res3 check used `CML_HEAP_SIZE=24576 CML_STACK_SIZE=4096`.

## Use for res3 (k=15 K_{2,3})

    cadical --chrono=0 --unsat --restartint=50 --lrat --no-binary \
            k15_res3.cnf k15_res3.lrat        # emit LRAT proof
    CML_HEAP_SIZE=24576 CML_STACK_SIZE=4096 \
            cake_lpr_sound.exe k15_res3.cnf k15_res3.lrat   # → s VERIFIED UNSAT
