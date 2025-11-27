from __future__ import annotations


def premierePuissanceDeaSuperieureAb(a: int, b: int) -> int:
    """
    Plus petite puissance de a supérieure ou égale à b.
    On travaille avec a > 1 (sinon la notion n'a pas trop de sens).
    """
    if a in (0, 1, -1):
        raise ValueError("On suppose |a| > 1.")

    if b <= 1:
        return 1

    m = 1
    while m < b:
        m *= a
    return m


def premierePuissanceDeaInferieureAb(a: int, b: int) -> int:
    """
    Plus grande puissance de a inférieure ou égale à b, pour |a| > 1.
    """
    if a in (0, 1, -1):
        raise ValueError("On suppose |a| > 1.")

    if b <= 1:
        return 1

    m = 1
    while m * a <= b:
        m *= a
    return m


if __name__ == "__main__":
    a = 2
    for b in [1, 2, 3, 5, 9, 17]:
        print(f"a = {a}, b = {b} :")
        print("  première puissance de a ≥ b :", premierePuissanceDeaSuperieureAb(a, b))
        print("  première puissance de a ≤ b :", premierePuissanceDeaInferieureAb(a, b))