from __future__ import annotations
from decimal import Decimal, getcontext
from typing import Tuple


def archimede(nb_iterations: int, precision: int) -> Tuple[Decimal, Decimal]:
    """
    Calcule un encadrement de π par la méthode d'Archimède.

    On part du cercle unité et de polygones réguliers inscrit / circonscrit.
    Retourne (pi_gauche, pi_droite) tels que pi_gauche < π < pi_droite.
    """
    # petite marge pour les calculs internes
    getcontext().prec = precision + 5

    # Périmètres du carré circonscrit (T) et inscrit (S) à un cercle de rayon 1.
    T = Decimal(8)                            # 4 côtés de longueur 2
    S = Decimal(4) * Decimal(2).sqrt()        # 4 côtés de longueur √2

    for _ in range(nb_iterations):
        # Formules classiques d'Archimède
        T = 2 * (S * T) / (S + T)             # polygone circonscrit
        S = (S * T).sqrt()                    # polygone inscrit

    # Périmètres / 2 = approximation de π
    return T / 2, S / 2


def main() -> None:
    digits = 1000
    iterations = 1700

    pi_gauche, pi_droite = archimede(iterations, digits)

    # On se remet à la précision souhaitée pour l'affichage
    getcontext().prec = digits
    print(f"{pi_gauche} < π < {pi_droite}")


if __name__ == "__main__":
    main()