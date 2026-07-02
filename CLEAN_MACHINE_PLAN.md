# Clean-Machine Replay Plan (Ticket B)

Goal: an independent, clean-machine certification run that (i) re-solves all 24 R229
certificate CNFs with a pinned CaDiCaL + drat-trim, and (ii) solves the new
**flip-certificate CNFs** (the kernel-lemma certificates that make the proof
unconditional) with DRAT logging and verification. One provisioning covers both.

## What you need to provision (one item)

A single Linux VM. Recommended spec:

| Item | Value | Why |
|---|---|---|
| Instance | 32 vCPU / 128 GB RAM (e.g. AWS `c7a.8xlarge`, GCP `c3-standard-44`, or a Hetzner AX102 dedicated) | 24 re-solves batch nicely at ~8-way; flip certs are memory-hungry single-thread runs |
| Disk | ≥ 1 TB NVMe | ASCII DRAT for flip certificates can reach tens of GB per case before completion |
| OS | Ubuntu 24.04 LTS | apt toolchain, no Windows shims needed |
| Runtime budget | up to 7 days | 24 re-solves ≈ hours; flip certificates are the unknown — budget 48h/case × 4 cases with parallel slots |

Estimated cost: AWS on-demand ≈ $1.7/h (≈ $280/week), spot ≈ 40% of that;
Hetzner dedicated ≈ €60–110/month (cheapest for a week-long run).

## What I need from you

Either of:
1. **SSH access**: create the VM, then give me `user@ip` + private key path (put the
   key somewhere local and tell me the path — do not paste key contents into chat).
2. **Provider API key** (simplest for you): an AWS access key pair scoped to EC2, or a
   Hetzner Cloud API token. I provision, run, harvest, and tear down myself.
   Store it in a local file (e.g. `C:\Users\Hpedr\.keys\...`) and tell me the path.

Also: the repo must be reachable from the VM — either push it to a private GitHub
remote with LFS (preferred; LFS bodies ≈ 1.2 GB), or I'll rsync it over SSH.

## What runs on the VM (I supply the script; outline)

1. `apt install build-essential git git-lfs python3-pip; pip install python-sat ortools`
2. Build **pinned** solvers from exact commits (recorded in the run manifest):
   - CaDiCaL: the commit whose version string matches the original run (`3.0.0`);
     `./configure && make` (no Windows shims needed on Linux).
   - drat-trim: current upstream master commit, recorded.
3. **Independent CNF rebuild**: regenerate all 24 representative CNFs from
   `source/root_cell_permutation_sat.py`; `sha256sum -c` against
   `artifacts/large_artifacts_manifest.csv`. Abort loudly on any mismatch.
4. **Re-solve layer**: for each rep 0..23: `cadical --no-binary rep.cnf rep.drat`,
   then `drat-trim rep.cnf rep.drat`; require `s UNSATISFIABLE` + `s VERIFIED`.
   8 parallel slots; expected wall: a day at most (original survivors took ≤ hours each).
5. **Flip-certificate layer** (the decisive new work): solve the symmetry-broken
   flip CNFs from `scratchpad/flip_certs/` (up to 4 cases; IF1 and IF0 are the
   load-bearing two), `--no-binary` DRAT + drat-trim verify, 48h cap each, 4 parallel.
6. Emit `clean_machine_replay_summary.json`: per-instance verdict, wall time, CNF and
   DRAT SHA-256, tool commits, hardware fingerprint. Pull the small artifacts back;
   keep DRATs compressed on the VM until verified, then archive the flip-cert DRATs
   (they are the publishable kernel-lemma certificates).

## Acceptance criteria

- 24/24 re-solves: `s UNSATISFIABLE` + `s VERIFIED`, CNF hashes matching the manifest.
- Flip certificates: `s UNSATISFIABLE` + `s VERIFIED` for at least IF1 and IF0
  (with SF1/SF0 as belt-and-braces), archived with hashes.
- Any `SATISFIABLE` on a flip CNF = countermodel to the forced-edge table → the
  certificate story changes fundamentally (this would be a major finding, not a bug).

## Current status upstream of this plan

- Flip CNF generation with stabilizer symmetry breaking (|Stab| = 768/case) is running
  locally (ticket A2b). Local solve attempts will start as soon as CNFs exist — if the
  symmetry-broken instances resolve locally, the flip layer of this plan shrinks to
  "verify the already-produced DRATs on the clean machine", which is cheap.
- The 24-re-solve layer is fully specified and independent of A2b.
