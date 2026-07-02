#!/usr/bin/env python3
"""Audit S2 wr S7 orbits on unordered far-label pairs."""

from __future__ import annotations

import json
from collections import deque
from pathlib import Path


CLASS_ORDER = ("SF1", "SF0", "IF1", "IF0", "DJ")
EXPECTED_CLASS_SIZES = {
    "SF1": 84,
    "SF0": 42,
    "IF1": 840,
    "IF0": 840,
    "DJ": 1680,
}
EXPECTED_PAIR_COUNT = 3486


def local_mate(i: int) -> int:
    return i ^ 1


def make_labels(k: int) -> list[tuple[int, int]]:
    labels = []
    for a in range(k):
        for b in range(a + 1, k):
            if local_mate(a) != b:
                labels.append((a, b))
    return labels


def overlap(labels: list[tuple[int, int]], i: int, j: int) -> int:
    return len(set(labels[i]) & set(labels[j]))


def label_pair_ids(label: tuple[int, int]) -> tuple[int, int]:
    return tuple(sorted((label[0] // 2, label[1] // 2)))


def local_vertex_map(
    pair_perm: tuple[int, ...],
    flips: tuple[int, ...],
) -> dict[int, int]:
    mapping = {}
    for pair in range(7):
        for bit in (0, 1):
            image_pair = pair_perm[pair]
            image_bit = bit ^ flips[pair]
            mapping[2 * pair + bit] = 2 * image_pair + image_bit
    return mapping


def mapped_label(
    label: tuple[int, int],
    vertex_map: dict[int, int],
) -> tuple[int, int]:
    return tuple(sorted((vertex_map[label[0]], vertex_map[label[1]])))


def generator_specs() -> list[tuple[str, tuple[int, ...], tuple[int, ...]]]:
    identity_perm = tuple(range(7))
    zero_flips = (0,) * 7
    specs = []
    for pair in range(7):
        flips = [0] * 7
        flips[pair] = 1
        specs.append((f"flip_{pair}", identity_perm, tuple(flips)))
    for pair in range(6):
        pair_perm = list(range(7))
        pair_perm[pair], pair_perm[pair + 1] = pair_perm[pair + 1], pair_perm[pair]
        specs.append((f"swap_pair_{pair}_{pair + 1}", tuple(pair_perm), zero_flips))
    return specs


def classify_pair(labels: list[tuple[int, int]], i: int, j: int) -> str:
    fiber_i = label_pair_ids(labels[i])
    fiber_j = label_pair_ids(labels[j])
    ov = overlap(labels, i, j)
    if fiber_i == fiber_j:
        if ov == 1:
            return "SF1"
        if ov == 0:
            return "SF0"
    elif set(fiber_i).isdisjoint(fiber_j):
        return "DJ"
    elif len(set(fiber_i) & set(fiber_j)) == 1:
        if ov == 1:
            return "IF1"
        if ov == 0:
            return "IF0"
    raise AssertionError((labels[i], labels[j], fiber_i, fiber_j, ov))


def label_permutation(
    labels: list[tuple[int, int]],
    label_to_index: dict[tuple[int, int], int],
    pair_perm: tuple[int, ...],
    flips: tuple[int, ...],
) -> tuple[int, ...]:
    vertex_map = local_vertex_map(pair_perm, flips)
    return tuple(label_to_index[mapped_label(label, vertex_map)] for label in labels)


def apply_to_pair(pair: tuple[int, int], perm: tuple[int, ...]) -> tuple[int, int]:
    image = (perm[pair[0]], perm[pair[1]])
    return tuple(sorted(image))


def representative_payload(
    pair: tuple[int, int],
    labels: list[tuple[int, int]],
    orbit_size: int,
) -> dict[str, object]:
    return {
        "pair_indices": list(pair),
        "labels": [list(labels[pair[0]]), list(labels[pair[1]])],
        "size": orbit_size,
    }


def main() -> int:
    labels = make_labels(14)
    if len(labels) != 84:
        raise AssertionError(f"expected 84 labels, got {len(labels)}")

    label_to_index = {label: idx for idx, label in enumerate(labels)}
    if len(label_to_index) != len(labels):
        raise AssertionError("labels are not unique")

    pairs = [(i, j) for i in range(len(labels)) for j in range(i + 1, len(labels))]
    if len(pairs) != EXPECTED_PAIR_COUNT:
        raise AssertionError(f"expected {EXPECTED_PAIR_COUNT} pairs, got {len(pairs)}")

    class_sizes = {name: 0 for name in CLASS_ORDER}
    pair_class = {}
    for pair in pairs:
        class_name = classify_pair(labels, *pair)
        pair_class[pair] = class_name
        class_sizes[class_name] += 1

    if sum(class_sizes.values()) != EXPECTED_PAIR_COUNT:
        raise AssertionError(class_sizes)
    if class_sizes != EXPECTED_CLASS_SIZES:
        raise AssertionError({"expected": EXPECTED_CLASS_SIZES, "actual": class_sizes})

    generators = [
        label_permutation(labels, label_to_index, pair_perm, flips)
        for _, pair_perm, flips in generator_specs()
    ]
    if len(generators) != 13:
        raise AssertionError(f"expected 13 generators, got {len(generators)}")
    expected_perm_image = set(range(len(labels)))
    for perm in generators:
        if set(perm) != expected_perm_image:
            raise AssertionError("generator is not a permutation of the far labels")

    unvisited = set(pairs)
    orbit_counts_per_class = {name: 0 for name in CLASS_ORDER}
    representatives = {name: [] for name in CLASS_ORDER}
    mixed_orbits = []

    while unvisited:
        start = min(unvisited)
        queue = deque([start])
        unvisited.remove(start)
        orbit = {start}

        while queue:
            pair = queue.popleft()
            for perm in generators:
                image = apply_to_pair(pair, perm)
                if image not in orbit:
                    orbit.add(image)
                    queue.append(image)
                    unvisited.discard(image)

        classes = sorted({pair_class[pair] for pair in orbit}, key=CLASS_ORDER.index)
        rep_pair = min(orbit)
        payload = representative_payload(rep_pair, labels, len(orbit))
        if len(classes) == 1:
            class_name = classes[0]
            orbit_counts_per_class[class_name] += 1
            representatives[class_name].append(payload)
        else:
            payload["classes"] = classes
            mixed_orbits.append(payload)

    for class_name in CLASS_ORDER:
        representatives[class_name].sort(key=lambda item: item["pair_indices"])

    covered_sizes = {
        class_name: sum(item["size"] for item in representatives[class_name])
        for class_name in CLASS_ORDER
    }
    orbits_match_classes = (
        not mixed_orbits
        and covered_sizes == class_sizes
        and all(orbit_counts_per_class[class_name] == 1 for class_name in CLASS_ORDER)
    )

    result = {
        "class_sizes": class_sizes,
        "orbit_counts_per_class": orbit_counts_per_class,
        "orbits_match_classes": orbits_match_classes,
        "representatives": representatives,
    }
    if mixed_orbits:
        result["mixed_orbits"] = mixed_orbits

    output_path = Path(__file__).with_suffix(".json")
    output_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"orbit_counts_per_class": orbit_counts_per_class}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
