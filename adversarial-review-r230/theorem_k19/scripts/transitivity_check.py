import json
from itertools import permutations, product
from pathlib import Path


PAIR_COUNT = 7
LOCAL_COUNT = 14
F0 = (0, 1)
F0_LABELS = ((0, 2), (0, 3), (1, 2), (1, 3))

C4_EDGES = (
    ("ce1", ((0, 2), (0, 3))),
    ("ce2", ((1, 2), (1, 3))),
    ("ce3", ((0, 2), (1, 2))),
    ("ce4", ((0, 3), (1, 3))),
)

DIAGONALS = (
    ("cd1", ((0, 2), (1, 3))),
    ("cd2", ((0, 3), (1, 2))),
)


def local_mate(vertex):
    return vertex ^ 1


def make_labels(k=LOCAL_COUNT):
    labels = []
    for a in range(k):
        for b in range(a + 1, k):
            if local_mate(a) != b:
                labels.append((a, b))
    return labels


def pair_ids(label):
    return tuple(sorted((label[0] // 2, label[1] // 2)))


def local_vertex_map(pair_perm, flips):
    """Same S2 wr S7 local-label action as root_cell_triangle_orbit_audit.py."""
    mapping = {}
    for pair in range(PAIR_COUNT):
        for bit in (0, 1):
            image_pair = pair_perm[pair]
            image_bit = bit ^ flips[pair]
            mapping[2 * pair + bit] = 2 * image_pair + image_bit
    return mapping


def mapped_label(label, vertex_map):
    return tuple(sorted((vertex_map[label[0]], vertex_map[label[1]])))


def image_fiber(fiber, pair_perm):
    return tuple(sorted((pair_perm[fiber[0]], pair_perm[fiber[1]])))


def canonical_edge(edge):
    left, right = edge
    return tuple(sorted((tuple(left), tuple(right))))


def mapped_edge(edge, vertex_map):
    return canonical_edge(tuple(mapped_label(label, vertex_map) for label in edge))


def orbit_partition(items, moves):
    remaining = set(items)
    orbits = []
    while remaining:
        start = min(remaining)
        orbit = {move(start) for move in moves}
        if start not in orbit:
            raise AssertionError(f"orbit did not contain start item {start}")
        orbits.append(sorted(orbit))
        remaining -= orbit
    return orbits


def named_edge(name, edge):
    canonical = canonical_edge(edge)
    return {
        "name": name,
        "labels": [list(canonical[0]), list(canonical[1])],
        "pair_ids": [list(pair_ids(canonical[0])), list(pair_ids(canonical[1]))],
    }


def edge_orbits_to_json(orbits, names_by_edge):
    out = []
    for orbit in orbits:
        entries = [named_edge(names_by_edge[edge], edge) for edge in orbit]
        entries.sort(key=lambda item: item["name"])
        out.append({"size": len(entries), "edges": entries})
    out.sort(key=lambda item: [entry["name"] for entry in item["edges"]])
    return out


def main():
    labels = make_labels()
    label_set = set(labels)
    if len(labels) != 84:
        raise AssertionError(f"expected 84 far labels, got {len(labels)}")
    if set(F0_LABELS) - label_set:
        raise AssertionError("F0 labels are not in the canonical far-label list")

    fibers = tuple((a, b) for a in range(PAIR_COUNT) for b in range(a + 1, PAIR_COUNT))
    if len(fibers) != 21:
        raise AssertionError(f"expected 21 fibers, got {len(fibers)}")

    pair_perms = list(permutations(range(PAIR_COUNT)))
    flip_vectors = list(product((0, 1), repeat=PAIR_COUNT))
    fiber_moves = [lambda fiber, perm=perm: image_fiber(fiber, perm) for perm in pair_perms]
    fiber_orbits = orbit_partition(fibers, fiber_moves)

    c4_edges = tuple(canonical_edge(edge) for _, edge in C4_EDGES)
    diagonal_edges = tuple(canonical_edge(edge) for _, edge in DIAGONALS)
    c4_names = {canonical_edge(edge): name for name, edge in C4_EDGES}
    diagonal_names = {canonical_edge(edge): name for name, edge in DIAGONALS}

    c4_moves = []
    diagonal_moves = []
    stab_size = 0
    for pair_perm in pair_perms:
        if image_fiber(F0, pair_perm) != F0:
            continue
        for flips in flip_vectors:
            stab_size += 1
            vertex_map = local_vertex_map(pair_perm, flips)
            if {mapped_label(label, vertex_map) for label in F0_LABELS} != set(F0_LABELS):
                raise AssertionError("setwise F0 stabilizer did not preserve the F0 labels")

            def make_edge_move(vmap):
                return lambda edge: mapped_edge(edge, vmap)

            move = make_edge_move(vertex_map)
            for edge in c4_edges:
                image = move(edge)
                if image not in c4_names:
                    raise AssertionError(f"C4 edge mapped outside C4 slots: {edge} -> {image}")
            for edge in diagonal_edges:
                image = move(edge)
                if image not in diagonal_names:
                    raise AssertionError(f"diagonal mapped outside diagonal slots: {edge} -> {image}")
            c4_moves.append(move)
            diagonal_moves.append(move)

    c4_orbits = orbit_partition(c4_edges, c4_moves)
    diagonal_orbits = orbit_partition(diagonal_edges, diagonal_moves)

    report = {
        "type": "g2prime_f0_transitivity_report_v1",
        "group": {
            "pair_permutation_count": len(pair_perms),
            "flip_vector_count": len(flip_vectors),
            "wreath_product_size": len(pair_perms) * len(flip_vectors),
        },
        "far_label_count": len(labels),
        "fiber_count": len(fibers),
        "fiber_orbit_count": len(fiber_orbits),
        "fiber_orbits": [
            {"size": len(orbit), "fibers": [list(fiber) for fiber in orbit]}
            for orbit in fiber_orbits
        ],
        "f0": {
            "fiber": list(F0),
            "labels": [list(label) for label in F0_LABELS],
        },
        "stab_size": stab_size,
        "c4edge_orbits": edge_orbits_to_json(c4_orbits, c4_names),
        "diagonal_orbits": edge_orbits_to_json(diagonal_orbits, diagonal_names),
    }

    out_path = Path(__file__).with_name("transitivity_report.json")
    out_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(f"fiber_orbit_count: {report['fiber_orbit_count']}")
    print(f"stab_size: {report['stab_size']}")
    print(f"c4edge_orbits: {[orbit['size'] for orbit in report['c4edge_orbits']]}")
    print(f"diagonal_orbits: {[orbit['size'] for orbit in report['diagonal_orbits']]}")
    print(f"WROTE {out_path}")


if __name__ == "__main__":
    main()
