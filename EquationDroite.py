from __future__ import annotations
from typing import Tuple
from sympy import symbols, simplify, init_printing

x, y = symbols("x y")
init_printing(use_unicode=True)

Point = Tuple[float, float]


def equation_droite_par_deux_points(A: Point, B: Point):
    """
    Équation d'une droite passant par A(xA, yA) et B(xB, yB) :
    (x - xA)(yB - yA) - (y - yA)(xB - xA) = 0
    """
    xA, yA = A
    xB, yB = B

    if xA == xB and yA == yB:
        raise ValueError("Les deux points doivent être distincts.")

    expr = (x - xA) * (yB - yA) - (y - yA) * (xB - xA)
    return simplify(expr)


def main() -> None:
    xA = float(input("x_A = ? "))
    yA = float(input("y_A = ? "))
    xB = float(input("x_B = ? "))
    yB = float(input("y_B = ? "))

    expr = equation_droite_par_deux_points((xA, yA), (xB, yB))
    print(expr, "= 0")


if __name__ == "__main__":
    main()