"""
root_cell_block_rep_audit.py -- finite audit for R206 block-rep SAT slices.

For the target disjoint fiber block (0,1)x(2,3), endpoint flips and swapping the
two groups inside either fiber act on the four positions as the square symmetry
group D8.  Therefore a block permutation is only meaningful up to left/right D8
action.  This script enumerates all 24 permutations of S4 and verifies that the
two representatives used by root_cell_permutation_sat.py cover exactly the two
double cosets.
"""
import argparse
import json
from itertools import permutations, product
from pathlib import Path


def compose(p, q):
    return tuple(p[i] for i in q)


def inverse(p):
    out = [0] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


def square_group():
    group = set()
    for flip_a, flip_b, swap in product([0, 1], [0, 1], [0, 1]):
        perm = []
        for pos in range(4):
            a = pos // 2
            b = pos % 2
            a ^= flip_a
            b ^= flip_b
            if swap:
                a, b = b, a
            perm.append(2 * a + b)
        group.add(tuple(perm))
    return sorted(group)


def double_coset(rep, group):
    rep_inv_domain = []
    for left in group:
        for right in group:
            rep_inv_domain.append(compose(left, compose(rep, inverse(right))))
    return sorted(set(rep_inv_domain))


def orbit_partition():
    group = square_group()
    unseen = set(permutations(range(4)))
    orbits = []
    while unseen:
        rep = min(unseen)
        orbit = double_coset(rep, group)
        orbits.append(orbit)
        unseen -= set(orbit)
    return group, sorted(orbits, key=lambda orbit: (len(orbit), orbit[0]))


def main():
    ap = argparse.ArgumentParser(description="Audit D8 double-cosets of S4 block permutations")
    ap.add_argument("--json-out")
    args = ap.parse_args()

    group, orbits = orbit_partition()
    reps = [orbit[0] for orbit in orbits]
    sizes = [len(orbit) for orbit in orbits]
    ok = len(group) == 8 and len(orbits) == 2 and sizes == [8, 16] and reps == [
        (0, 1, 2, 3),
        (0, 1, 3, 2),
    ]

    result = {
        "type": "root_cell_block_rep_audit_v1",
        "ok": ok,
        "square_group_size": len(group),
        "square_group": [list(p) for p in group],
        "orbit_count": len(orbits),
        "orbit_sizes": sizes,
        "representatives": {
            "square": list(reps[0]),
            "nonsquare": list(reps[1]),
        },
        "covered_permutations": sum(sizes),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if args.json_out:
        path = Path(args.json_out)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"WROTE {path}")
    if not ok:
        raise SystemExit("block representative audit failed")


if __name__ == "__main__":
    main()
