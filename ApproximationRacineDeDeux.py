from __future__ import annotations
from decimal import Decimal, getcontext


def carre(x: float) -> float:
    """Renvoie x² (version flottante)."""
    return x * x


def balayage(n: int) -> None:
    """
    Balayage de l'intervalle [1, 2] avec un pas 10^-n.
    Affiche un encadrement de √2.
    """
    pas = 10 ** (-n)
    x1 = 1.0
    x2 = 1.0 + pas

    while (carre(x1) - 2.0) * (carre(x2) - 2.0) > 0:
        x1 += pas
        x2 += pas

    print(f"{x1:.{n+1}f}^2 = {carre(x1)}")
    print(f"{x2:.{n+1}f}^2 = {carre(x2)}")


def dichotomie(n: int) -> float:
    """
    Dichotomie sur [1, 2] jusqu'à une largeur d'intervalle < 10^-n.
    Renvoie une approximation flottante de √2.
    """
    a, b = 1.0, 2.0
    eps = 10 ** (-n)

    while b - a > eps:
        m = 0.5 * (a + b)
        if carre(m) < 2.0:
            a = m
        else:
            b = m

    approx = 0.5 * (a + b)
    print(f"sqrt(2) ≈ {approx:.{n+1}f}")
    return approx


def sqrt2_decimal_dichotomie(digits: int) -> Decimal:
    """
    Approximation décimale de √2 par dichotomie avec 'digits' décimales.
    """
    getcontext().prec = digits + 5  # marge
    a = Decimal(1)
    b = Decimal(2)
    deux = Decimal(2)
    eps = Decimal(10) ** (-(digits + 2))

    while b - a > eps:
        m = (a + b) / 2
        if m * m < deux:
            a = m
        else:
            b = m

    approx = (a + b) / 2
    getcontext().prec = digits
    return +approx  # arrondi à la précision courante


def sqrt2_decimal_newton(digits: int) -> Decimal:
    """
    Approximation décimale de √2 par la méthode de Newton.
    """
    getcontext().prec = digits + 5
    deux = Decimal(2)
    x = Decimal(1)

    # nombre d'itérations suffisant pour converger avec marge
    for _ in range(digits + 10):
        x = (x + deux / x) / 2

    getcontext().prec = digits
    return +x


def main() -> None:
    print("-------------------------")
    print("Balayage à 10^-7 :")
    balayage(7)

    print("-------------------------")
    print("Dichotomie à 10^-12 :")
    dichotomie(12)

    print("-------------------------")
    print("Cent premières décimales par dichotomie décimale :")
    print(sqrt2_decimal_dichotomie(100))

    print("-------------------------")
    print("Mille premières décimales par méthode de Newton :")
    print(sqrt2_decimal_newton(1000))


if __name__ == "__main__":
    main()