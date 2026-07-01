"""Clean-room replay entry point for the R230 review bundle.

This replay avoids the solver stack.  It checks the parts a reviewer can verify
from the repository bundle alone:

1. R204 clean-room symbolic reduction audit;
2. compact bundle metadata and proof-log markers;
3. full certificate audit against the included CNF/DRAT bodies and hashes.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_step(name: str, command: list[str]) -> dict:
    proc = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    shown_command = ["python" if part == sys.executable else part for part in command]
    return {
        "name": name,
        "command": shown_command,
        "returncode": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
        "ok": proc.returncode == 0,
    }


def main() -> int:
    scratchpad = ROOT / "scratchpad"
    scratchpad.mkdir(exist_ok=True)
    steps = [
        (
            "r204_cleanroom_symbolic_audit",
            [
                sys.executable,
                "source/root_cell_r204_cleanroom_symbolic_audit.py",
                "--json-out",
                "scratchpad/root_cell_r204_cleanroom_symbolic_audit_replay.json",
            ],
        ),
        (
            "bundle_metadata",
            [sys.executable, "scripts/verify_bundle_metadata.py"],
        ),
        (
            "certificate_with_bodies",
            [
                sys.executable,
                "source/root_cell_r229_certificate_audit.py",
                "--json-out",
                "scratchpad/root_cell_r229_certificate_audit_replay.json",
            ],
        ),
    ]

    results = [run_step(name, command) for name, command in steps]
    payload = {
        "type": "r230_clean_room_replay_v1",
        "ok": all(result["ok"] for result in results),
        "steps": results,
    }
    out = scratchpad / "clean_room_replay_summary.json"
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"ok": payload["ok"], "summary": str(out), "steps": [
        {"name": item["name"], "returncode": item["returncode"], "ok": item["ok"]}
        for item in results
    ]}, indent=2, sort_keys=True))
    return 0 if payload["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
