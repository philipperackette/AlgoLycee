from __future__ import annotations
from typing import Tuple
import math

Point = Tuple[float, float]
Vector = Tuple[float, float]


def vecteur(A: Point, B: Point) -> Vector:
    """Retourne le vecteur AB."""
    return B[0] - A[0], B[1] - A[1]


def determinant(u: Vector, v: Vector) -> float:
    """Déterminant de (u, v)."""
    return u[0] * v[1] - u[1] * v[0]


def sont_alignes(A: Point, B: Point, C: Point, tol: float = 1e-9) -> bool:
    """
    Teste l'alignement des 3 points avec une tolérance flottante.
    """
    AB = vecteur(A, B)
    AC = vecteur(A, C)
    det = determinant(AB, AC)
    return math.isclose(det, 0.0, rel_tol=0.0, abs_tol=tol)


def main() -> None:
    xA = float(input("x_A = ? "))
    yA = float(input("y_A = ? "))
    xB = float(input("x_B = ? "))
    yB = float(input("y_B = ? "))
    xC = float(input("x_C = ? "))
    yC = float(input("y_C = ? "))

    if sont_alignes((xA, yA), (xB, yB), (xC, yC)):
        print("Une droite passe par A, B et C.")
    else:
        print("A, B et C ne sont pas alignés.")


if __name__ == "__main__":
    main()