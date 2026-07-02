"""
root_cell_triangle_orbit_audit.py -- matching-triple block orbit audit.

The rooted fiber model has a large residual symmetry from the fixed 7K2 local
neighbourhood: swap endpoints inside any local edge and permute the seven local
edges.  For a fixed matching of three disjoint fibers

    A=(0,2), B=(1,4), C=(3,6)

this script enumerates the induced action on the three direct S4 blocks
P_AB, P_AC, P_BC.  It independently compares that action against the abstract
D8^3 semidirect S3 action on the three square fibers.

The result is an exhaustive, symmetry-sound case split for rooted SAT/CP runs:
every solution can be moved into exactly one of the reported representative
classes for the chosen matching triple.
"""
import argparse
import json
import sys
from collections import Counter, deque
from itertools import product
from pathlib import Path

SOURCE_DIR = Path(__file__).resolve().parents[2] / "source"
if str(SOURCE_DIR) not in sys.path:
    sys.path.insert(0, str(SOURCE_DIR))

from root_cell_cpsat import labels_by_fiber, make_labels
from root_cell_permutation_csp import (
    PERM_ID,
    PERMS,
    SQUARE_ORBIT,
    compose_perm,
    invert_perm,
)


DEFAULT_TRIANGLE_FIBERS = ((0, 2), (1, 4), (3, 6))


def normalize_triangle_fibers(triangle_fibers):
    normalized = tuple(tuple(sorted(fiber)) for fiber in triangle_fibers)
    if len(normalized) != 3:
        raise ValueError("expected exactly three fibers")
    for fiber in normalized:
        if len(fiber) != 2 or len(set(fiber)) != 2:
            raise ValueError(f"invalid 2-subset fiber: {fiber}")
        if any(pair < 0 or pair > 6 for pair in fiber):
            raise ValueError(f"fiber index outside 0..6: {fiber}")
    used_pairs = [pair for fiber in normalized for pair in fiber]
    if len(set(used_pairs)) != len(used_pairs):
        raise ValueError(f"fibers are not pairwise disjoint: {normalized}")
    return normalized


def parse_triangle_fibers(text):
    fibers = []
    for chunk in text.split(";"):
        cleaned = chunk.strip().strip("()")
        if not cleaned:
            continue
        parts = [part.strip() for part in cleaned.split(",") if part.strip()]
        if len(parts) != 2:
            raise ValueError(f"expected two comma-separated indices in {chunk!r}")
        fibers.append(tuple(int(part) for part in parts))
    return normalize_triangle_fibers(fibers)


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


def apply_actual_symmetry(triple, triangle_fibers, pair_perm, flips, labels, by_fiber, label_to_index):
    vertex_map = local_vertex_map(pair_perm, flips)
    image_to_preimage = {}
    for fiber_idx, fiber in enumerate(triangle_fibers):
        for pos, label_idx in enumerate(by_fiber[fiber]):
            image_label = mapped_label(labels[label_idx], vertex_map)
            image_idx = label_to_index[image_label]
            image_fiber = next(i for i, f in enumerate(triangle_fibers) if image_idx in by_fiber[f])
            image_pos = by_fiber[triangle_fibers[image_fiber]].index(image_idx)
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


def actual_generators(triangle_fibers):
    labels = make_labels(14)
    by_fiber = {fiber: sorted(indices) for fiber, indices in labels_by_fiber(labels).items()}
    label_to_index = {label: idx for idx, label in enumerate(labels)}
    identity_perm = tuple(range(7))
    zero_flips = (0,) * 7

    raw = []
    for pair in sorted(pair for fiber in triangle_fibers for pair in fiber):
        raw.append((identity_perm, flip_vector(pair)))
    for fiber in triangle_fibers:
        raw.append((swap_perm(fiber[0], fiber[1]), zero_flips))
    raw.extend(
        [
            (edge_swap_perm(triangle_fibers[0], triangle_fibers[1]), zero_flips),
            (edge_swap_perm(triangle_fibers[1], triangle_fibers[2]), zero_flips),
        ]
    )

    def make_generator(pair_perm, flips):
        def gen(key):
            triple = tuple(PERMS[idx] for idx in key)
            moved = apply_actual_symmetry(
                triple, triangle_fibers, pair_perm, flips, labels, by_fiber, label_to_index
            )
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


def json_safe(value):
    if isinstance(value, tuple):
        return [json_safe(item) for item in value]
    if isinstance(value, list):
        return [json_safe(item) for item in value]
    if isinstance(value, dict):
        return {str(key): json_safe(item) for key, item in value.items()}
    return value


def write_result(result, json_out):
    print(json.dumps(result, indent=2, sort_keys=True))
    if json_out:
        path = Path(json_out)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"WROTE {path}")


def main():
    ap = argparse.ArgumentParser(description="Audit matching-triple S4 block orbits")
    ap.add_argument("--json-out")
    ap.add_argument(
        "--triple",
        default="0,2;1,4;3,6",
        help="semicolon-separated matching triple, e.g. '0,2;1,4;3,6'",
    )
    args = ap.parse_args()

    triangle_fibers = parse_triangle_fibers(args.triple)
    abstract_orbits, _abstract_key_to_orbit = orbit_table_from_generators(abstract_generators())
    try:
        actual_orbits, _actual_key_to_orbit = orbit_table_from_generators(
            actual_generators(triangle_fibers)
        )
    except AssertionError as exc:
        result = {
            "type": "root_cell_triangle_orbit_audit_v1",
            "ok": False,
            "triple_fibers": [list(f) for f in triangle_fibers],
            "ambient_triples": len(PERMS) ** 3,
            "orbit_count": 0,
            "orbit_size_histogram": {},
            "actual_equals_abstract_d8_s3": False,
            "representatives": [],
            "actual_generator_assertion": json_safe(exc.args[0] if len(exc.args) == 1 else exc.args),
        }
        write_result(result, args.json_out)
        raise SystemExit("actual generator assertion failed") from exc
    mismatch = abstract_orbits != actual_orbits
    reps = [
        {"index": idx, "rep": list(rep), "size": size}
        for idx, (rep, size) in enumerate(actual_orbits.items())
    ]
    result = {
        "type": "root_cell_triangle_orbit_audit_v1",
        "ok": not mismatch,
        "triple_fibers": [list(f) for f in triangle_fibers],
        "ambient_triples": len(PERMS) ** 3,
        "orbit_count": len(actual_orbits),
        "orbit_size_histogram": dict(sorted(Counter(actual_orbits.values()).items())),
        "actual_equals_abstract_d8_s3": not mismatch,
        "representatives": reps,
    }
    if mismatch:
        result["abstract_only"] = [list(key) for key in sorted(set(abstract_orbits) - set(actual_orbits))[:10]]
        result["actual_only"] = [list(key) for key in sorted(set(actual_orbits) - set(abstract_orbits))[:10]]

    write_result(result, args.json_out)
    if not result["ok"]:
        raise SystemExit("triangle orbit audit failed")


if __name__ == "__main__":
    main()
