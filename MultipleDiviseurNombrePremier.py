from __future__ import annotations


def aEstMultipleDeb(a: int, b: int) -> bool:
    """
    Retourne True si a est un multiple de b.

    Convention :
    - Si b == 0 : seul 0 est multiple de 0.
    - Sinon : a est multiple de b s'il existe un entier k tel que a = k*b.
    """
    if b == 0:
        return a == 0
    return a % b == 0


def plusGrandMultipleDeaInferieurAb(a: int, b: int) -> int:
    """
    Plus grand multiple de a inférieur ou égal à b.

    Utilise la division entière : le quotient q = b // a donne le plus grand
    entier tel que q*a <= b, donc q*a est le plus grand multiple recherché.
    """
    if a == 0:
        raise ValueError("a ne doit pas être nul")

    q = b // a
    return q * a


def estPremier(n: int) -> bool:
    """
    Teste si n est un nombre premier (n >= 2).
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    d = 3
    while d * d <= n:
        if aEstMultipleDeb(n, d):
            return False
        d += 2
    return True


if __name__ == "__main__":
    for k in range(1, 20):
        print(k, "premier ?" , estPremier(k))