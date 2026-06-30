"""
root_cell_triangle_rep_unit_audit.py -- independent BCP audit for R220 reps.

The SAT solver reports that many matching-triangle representatives are UNSAT
with zero decisions.  This script verifies that claim without trusting a solver:
it builds each direct-cardinality CNF and runs plain Boolean unit propagation.
Any representative killed here is contradicted by level-0 clauses alone.
"""
import argparse
import json
from collections import deque
from pathlib import Path

from root_cell_permutation_sat import PermutationSat, TRIANGLE_REP_IDS


def unit_propagate(cnf):
    clauses = cnf.clauses
    occurrence = {}
    assignment = {}
    queue = deque()
    propagation_steps = 0

    for idx, clause in enumerate(clauses):
        if not clause:
            return {
                "conflict": True,
                "conflict_clause_index": idx,
                "conflict_clause": [],
                "assigned": 0,
                "propagation_steps": 0,
            }
        for lit in clause:
            occurrence.setdefault(-lit, []).append(idx)
        if len(clause) == 1:
            queue.append((clause[0], idx))

    while queue:
        lit, reason = queue.popleft()
        var = abs(lit)
        value = lit > 0
        old = assignment.get(var)
        if old is not None:
            if old != value:
                return {
                    "conflict": True,
                    "conflict_clause_index": reason,
                    "conflict_clause": clauses[reason],
                    "assigned": len(assignment),
                    "propagation_steps": propagation_steps,
                    "conflict_literal": lit,
                }
            continue
        assignment[var] = value
        propagation_steps += 1

        for clause_idx in occurrence.get(lit, []):
            clause = clauses[clause_idx]
            satisfied = False
            unassigned = []
            for term in clause:
                assigned = assignment.get(abs(term))
                if assigned is None:
                    unassigned.append(term)
                elif assigned == (term > 0):
                    satisfied = True
                    break
            if satisfied:
                continue
            if not unassigned:
                return {
                    "conflict": True,
                    "conflict_clause_index": clause_idx,
                    "conflict_clause": clause,
                    "assigned": len(assignment),
                    "propagation_steps": propagation_steps,
                }
            if len(unassigned) == 1:
                queue.append((unassigned[0], clause_idx))

    return {
        "conflict": False,
        "assigned": len(assignment),
        "propagation_steps": propagation_steps,
    }


def main():
    ap = argparse.ArgumentParser(description="BCP-audit triangle representative CNFs")
    ap.add_argument("--card-encoding", choices=["direct", "seqcounter"], default="direct")
    ap.add_argument("--json-out")
    args = ap.parse_args()

    records = []
    for idx, rep in enumerate(TRIANGLE_REP_IDS):
        enc = PermutationSat(card_encoding=args.card_encoding, triangle_rep_index=idx).build()
        bcp = unit_propagate(enc.cnf)
        records.append(
            {
                "index": idx,
                "rep": list(rep),
                "unit_conflict": bcp["conflict"],
                "assigned": bcp["assigned"],
                "propagation_steps": bcp["propagation_steps"],
                "conflict_clause_index": bcp.get("conflict_clause_index"),
                "conflict_clause": bcp.get("conflict_clause"),
                "cnf_vars": enc.stats["cnf_vars"],
                "cnf_clauses": enc.stats["cnf_clauses"],
            }
        )

    killed = [r["index"] for r in records if r["unit_conflict"]]
    survivors = [r["index"] for r in records if not r["unit_conflict"]]
    result = {
        "type": "root_cell_triangle_rep_unit_audit_v1",
        "ok": True,
        "card_encoding": args.card_encoding,
        "representatives": len(records),
        "unit_conflict_count": len(killed),
        "survivor_count": len(survivors),
        "unit_conflict_indices": killed,
        "survivor_indices": survivors,
        "records": records,
    }

    print(json.dumps(result, indent=2, sort_keys=True))
    if args.json_out:
        path = Path(args.json_out)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"WROTE {path}")


if __name__ == "__main__":
    main()
