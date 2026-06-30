"""
root_cell_triangle_orbit_audit.py -- matching-triple block orbit audit.

The rooted fiber model has a large residual symmetry from the fixed 7K2 local
neighbourhood: swap endpoints inside any local edge and permute the seven local
edges.  For a fixed matching of three disjoint fibers

    A=(0,1), B=(2,3), C=(4,5)

this script enumerates the induced action on the three direct S4 blocks
P_AB, P_AC, P_BC.  It independently compares that action against the abstract
D8^3 semidirect S3 action on the three square fibers.

The result is an exhaustive, symmetry-sound case split for rooted SAT/CP runs:
every solution can be moved into exactly one of the reported representative
classes for the chosen matching triple.
"""
import argparse
import json
from collections import Counter, deque
from itertools import product
from pathlib import Path

from root_cell_cpsat import labels_by_fiber, make_labels
from root_cell_permutation_csp import (
    PERM_ID,
    PERMS,
    SQUARE_ORBIT,
    compose_perm,
    invert_perm,
)


TRIANGLE_FIBERS = ((0, 1), (2, 3), (4, 5))


def transform_local(triple, actions):
    p01, p02, p12 = triple
    h0, h1, h2 = actions
    return (
        compose_perm(h1, compose_perm(p01, invert_perm(h0))),
        compose_perm(h2, compose_perm(p02, invert_perm(h0))),
        compose_perm(h2, compose_perm(p12, invert_perm(h1))),
    )


def permute_fibers(triple, sigma):
    p01, p02, p12 = triple
    directed = {
        (0, 1): p01,
        (1, 0): invert_perm(p01),
        (0, 2): p02,
        (2, 0): invert_perm(p02),
        (1, 2): p12,
        (2, 1): invert_perm(p12),
    }
    return (
        directed[(sigma[0], sigma[1])],
        directed[(sigma[0], sigma[2])],
        directed[(sigma[1], sigma[2])],
    )


def local_vertex_map(pair_perm, flips):
    mapping = {}
    for pair in range(7):
        for bit in (0, 1):
            image_pair = pair_perm[pair]
            image_bit = bit ^ flips[pair]
            mapping[2 * pair + bit] = 2 * image_pair + image_bit
    return mapping


def mapped_label(label, vertex_map):
    return tuple(sorted((vertex_map[label[0]], vertex_map[label[1]])))


def triple_edge_lookup(triple):
    p01, p02, p12 = triple
    directed = {
        (0, 1): p01,
        (1, 0): invert_perm(p01),
        (0, 2): p02,
        (2, 0): invert_perm(p02),
        (1, 2): p12,
        (2, 1): invert_perm(p12),
    }
    return directed


def apply_actual_symmetry(triple, pair_perm, flips, labels, by_fiber, label_to_index):
    vertex_map = local_vertex_map(pair_perm, flips)
    image_to_preimage = {}
    for fiber_idx, fiber in enumerate(TRIANGLE_FIBERS):
        for pos, label_idx in enumerate(by_fiber[fiber]):
            image_label = mapped_label(labels[label_idx], vertex_map)
            image_idx = label_to_index[image_label]
            image_fiber = next(i for i, f in enumerate(TRIANGLE_FIBERS) if image_idx in by_fiber[f])
            image_pos = by_fiber[TRIANGLE_FIBERS[image_fiber]].index(image_idx)
            image_to_preimage[image_fiber, image_pos] = (fiber_idx, pos)

    directed = triple_edge_lookup(triple)
    out = []
    for left_fiber, right_fiber in ((0, 1), (0, 2), (1, 2)):
        perm = []
        for left_pos in range(4):
            old_left_fiber, old_left_pos = image_to_preimage[left_fiber, left_pos]
            ones = []
            for right_pos in range(4):
                old_right_fiber, old_right_pos = image_to_preimage[right_fiber, right_pos]
                old_perm = directed[(old_left_fiber, old_right_fiber)]
                if old_perm[old_left_pos] == old_right_pos:
                    ones.append(right_pos)
            if len(ones) != 1:
                raise AssertionError((triple, pair_perm, flips, left_fiber, right_fiber, left_pos, ones))
            perm.append(ones[0])
        out.append(tuple(perm))
    return tuple(out)


def swap_perm(a, b):
    out = list(range(7))
    out[a], out[b] = out[b], out[a]
    return tuple(out)


def edge_swap_perm(edge_a, edge_b):
    out = list(range(7))
    a0, a1 = edge_a
    b0, b1 = edge_b
    out[a0], out[b0] = out[b0], out[a0]
    out[a1], out[b1] = out[b1], out[a1]
    return tuple(out)


def flip_vector(pair):
    flips = [0] * 7
    flips[pair] = 1
    return tuple(flips)


def actual_generators():
    labels = make_labels(14)
    by_fiber = {fiber: sorted(indices) for fiber, indices in labels_by_fiber(labels).items()}
    label_to_index = {label: idx for idx, label in enumerate(labels)}
    identity_perm = tuple(range(7))
    zero_flips = (0,) * 7

    raw = []
    for pair in range(6):
        raw.append((identity_perm, flip_vector(pair)))
    raw.extend(
        [
            (swap_perm(0, 1), zero_flips),
            (swap_perm(2, 3), zero_flips),
            (swap_perm(4, 5), zero_flips),
            (edge_swap_perm((0, 1), (2, 3)), zero_flips),
            (edge_swap_perm((2, 3), (4, 5)), zero_flips),
        ]
    )

    def make_generator(pair_perm, flips):
        def gen(key):
            triple = tuple(PERMS[idx] for idx in key)
            moved = apply_actual_symmetry(triple, pair_perm, flips, labels, by_fiber, label_to_index)
            return tuple(PERM_ID[p] for p in moved)

        return gen

    return [make_generator(pair_perm, flips) for pair_perm, flips in raw]


def abstract_generators():
    identity = (0, 1, 2, 3)
    gens = []
    for fiber_idx in range(3):
        for h in SQUARE_ORBIT:
            if h == identity:
                continue

            def make_local(idx, action):
                def gen(key):
                    triple = tuple(PERMS[i] for i in key)
                    actions = [identity, identity, identity]
                    actions[idx] = action
                    return tuple(PERM_ID[p] for p in transform_local(triple, tuple(actions)))

                return gen

            gens.append(make_local(fiber_idx, h))
    for sigma in ((1, 0, 2), (0, 2, 1)):

        def make_swap(sig):
            def gen(key):
                triple = tuple(PERMS[i] for i in key)
                return tuple(PERM_ID[p] for p in permute_fibers(triple, sig))

            return gen

        gens.append(make_swap(sigma))
    return gens


def orbit_table_from_generators(generators):
    all_keys = {tuple(ids) for ids in product(range(len(PERMS)), repeat=3)}
    orbits = {}
    key_to_orbit = {}
    while all_keys:
        start = min(all_keys)
        queue = deque([start])
        orbit = {start}
        all_keys.remove(start)
        while queue:
            key = queue.popleft()
            for gen in generators:
                moved = gen(key)
                if moved not in orbit:
                    orbit.add(moved)
                    queue.append(moved)
                    all_keys.discard(moved)
        rep = min(orbit)
        orbits[rep] = len(orbit)
        for key in orbit:
            key_to_orbit[key] = rep
    return dict(sorted(orbits.items())), key_to_orbit


def main():
    ap = argparse.ArgumentParser(description="Audit matching-triple S4 block orbits")
    ap.add_argument("--json-out")
    args = ap.parse_args()

    abstract_orbits, _abstract_key_to_orbit = orbit_table_from_generators(abstract_generators())
    actual_orbits, _actual_key_to_orbit = orbit_table_from_generators(actual_generators())
    mismatch = abstract_orbits != actual_orbits
    reps = [
        {"index": idx, "rep": list(rep), "size": size}
        for idx, (rep, size) in enumerate(actual_orbits.items())
    ]
    result = {
        "type": "root_cell_triangle_orbit_audit_v1",
        "ok": not mismatch,
        "triple_fibers": [list(f) for f in TRIANGLE_FIBERS],
        "ambient_triples": len(PERMS) ** 3,
        "orbit_count": len(actual_orbits),
        "orbit_size_histogram": dict(sorted(Counter(actual_orbits.values()).items())),
        "actual_equals_abstract_d8_s3": not mismatch,
        "representatives": reps,
    }
    if mismatch:
        result["abstract_only"] = [list(key) for key in sorted(set(abstract_orbits) - set(actual_orbits))[:10]]
        result["actual_only"] = [list(key) for key in sorted(set(actual_orbits) - set(abstract_orbits))[:10]]

    print(json.dumps(result, indent=2, sort_keys=True))
    if args.json_out:
        path = Path(args.json_out)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"WROTE {path}")
    if not result["ok"]:
        raise SystemExit("triangle orbit audit failed")


if __name__ == "__main__":
    main()
