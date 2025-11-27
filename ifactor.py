# https://www.mathweb.fr/euclide/2022/06/14/creer-une-fonction-ifactors-en-python/
from __future__ import annotations
from typing import Dict


def ifactors(n: int, decomp: bool = False):
    """
    Décomposition en facteurs premiers de n >= 2.

    - Si decomp=False : renvoie un dictionnaire {prime: exposant}.
    - Si decomp=True  : renvoie une chaîne "2² × 3³ × ...".
    """
    if n < 2:
        return {} if not decomp else ""

    D: Dict[int, int] = {}
    i = 2

    # Décomposition naïve (suffisant pour les entiers "lycée")
    while i * i <= n:
        exposant = 0
        while n % i == 0:
            exposant += 1
            n //= i
        if exposant != 0:
            D[i] = exposant
        i += 1

    # S'il reste un facteur premier > sqrt(n)
    if n > 1:
        D[n] = 1

    if not decomp:
        return D

    L_exp = [
        0x2070,  # ⁰
        0x00B9,  # ¹
        0x00B2,  # ²
        0x00B3,  # ³
        0x2074,  # ⁴
        0x2075,  # ⁵
        0x2076,  # ⁶
        0x2077,  # ⁷
        0x2078,  # ⁸
        0x2079,  # ⁹
    ]

    def expo_to_superscript(e: int) -> str:
        s = ""
        for ch in str(e):
            s += chr(L_exp[int(ch)])
        return s

    morceaux = []
    for prime in sorted(D):
        e = D[prime]
        morceaux.append(f"{prime}{expo_to_superscript(e)}")

    return " × ".join(morceaux)


if __name__ == "__main__":
    print(ifactors(360))
    print(ifactors(360, decomp=True))