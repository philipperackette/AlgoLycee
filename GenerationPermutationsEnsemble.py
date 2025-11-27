from __future__ import annotations
from typing import List, Sequence, Any


def permutations(E: Sequence[Any]) -> List[List[Any]]:
    """
    Génère récursivement toutes les permutations de la séquence E.
    """
    if len(E) == 0:
        return []
    if len(E) == 1:
        return [list(E)]

    perm: List[List[Any]] = []
    for i, e in enumerate(E):
        sousE = E[:i] + E[i + 1:]  # E privé de e
        for p in permutations(sousE):
            perm.append([e] + p)
    return perm


def main() -> None:
    for p in permutations(['A', 'B', 'C', 'D']):
        print(p)


if __name__ == "__main__":
    main()