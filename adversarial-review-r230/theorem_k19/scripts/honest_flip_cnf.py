import json
import sys
import time
from pathlib import Path

from pysat.card import CardEnc, EncType
from pysat.formula import CNF, IDPool


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from source.root_cell_cpsat import local_mate, make_labels, overlap  # noqa: E402


K = 14
OUT_DIR = ROOT / "scratchpad" / "honest_flip_probe"


def add_card_equals(cnf, lits, bound, vpool):
    enc = CardEnc.equals(
        lits=list(lits),
        bound=bound,
        vpool=vpool,
        encoding=EncType.seqcounter,
    )
    cnf.extend(enc.clauses)


def build_base_cnf():
    labels = make_labels(K)
    n = len(labels)
    cnf = CNF()
    vpool = IDPool()

    edge_vars = {}
    for i in range(n):
        for j in range(i + 1, n):
            edge_vars[i, j] = vpool.id(f"e_{i}_{j}")

    def edge(i, j):
        if i == j:
            raise ValueError("diagonal edge requested")
        return edge_vars[(i, j) if i < j else (j, i)]

    # Far graph degree: each far vertex has 12 far neighbours.
    for i in range(n):
        add_card_equals(
            cnf,
            [edge(i, j) for j in range(n) if j != i],
            K - 2,
            vpool,
        )

    # Local-far lambda/mu equations.
    label_sets = [set(label) for label in labels]
    for i, lab_set in enumerate(label_sets):
        for local in range(K):
            rhs = 2 - int(local in lab_set) - int(local_mate(local) in lab_set)
            lits = [
                edge(i, j)
                for j, other in enumerate(label_sets)
                if j != i and local in other
            ]
            add_card_equals(cnf, lits, rhs, vpool)

    # Far-far lambda/mu equations:
    # common_F(i,j) + e_ij + overlap(i,j) = 2.
    product_vars = []
    for i in range(n):
        for j in range(i + 1, n):
            common_lits = []
            for z in range(n):
                if z == i or z == j:
                    continue
                p = vpool.id(f"p_{i}_{j}_{z}")
                e_iz = edge(i, z)
                e_jz = edge(j, z)
                cnf.append([-p, e_iz])
                cnf.append([-p, e_jz])
                cnf.append([p, -e_iz, -e_jz])
                common_lits.append(p)
                product_vars.append(p)
            add_card_equals(
                cnf,
                common_lits + [edge(i, j)],
                2 - overlap(labels, i, j),
                vpool,
            )

    cnf.nv = vpool.top
    return cnf, labels, edge_vars, len(product_vars)


def write_dimacs(path, clauses, nv, unit):
    with path.open("w", encoding="ascii", newline="\n") as fh:
        fh.write(f"p cnf {nv} {len(clauses) + 1}\n")
        for clause in clauses:
            fh.write(" ".join(str(lit) for lit in clause))
            fh.write(" 0\n")
        fh.write(f"{unit} 0\n")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    started = time.perf_counter()
    cnf, labels, edge_vars, product_var_count = build_base_cnf()
    base_seconds = time.perf_counter() - started

    def edge_by_label(left, right):
        i = labels.index(left)
        j = labels.index(right)
        return edge_vars[(i, j) if i < j else (j, i)]

    cases = {
        "T1": -edge_by_label((0, 2), (0, 3)),
        "T2": edge_by_label((0, 2), (1, 3)),
        "T3": edge_by_label((0, 2), (0, 4)),
    }

    metadata = {
        "type": "honest_flip_cnf_metadata_v1",
        "k": K,
        "far_vertices": len(labels),
        "edge_var_count": len(edge_vars),
        "product_var_count": product_var_count,
        "cnf_vars": cnf.nv,
        "base_clauses": len(cnf.clauses),
        "case_clauses": len(cnf.clauses) + 1,
        "build_seconds": base_seconds,
        "labels": [list(label) for label in labels],
        "edge_vars": [[i, j, var] for (i, j), var in sorted(edge_vars.items())],
        "cases": cases,
    }
    (OUT_DIR / "metadata.json").write_text(
        json.dumps(metadata, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    for case, unit in cases.items():
        path = OUT_DIR / f"flip_{case}.cnf"
        write_dimacs(path, cnf.clauses, cnf.nv, unit)
        print(
            f"{case}: wrote {path} vars={cnf.nv} clauses={len(cnf.clauses) + 1} "
            f"unit={unit}",
            flush=True,
        )

    print(
        f"base build seconds={base_seconds:.2f} "
        f"edge_vars={len(edge_vars)} product_vars={product_var_count}",
        flush=True,
    )


if __name__ == "__main__":
    main()
