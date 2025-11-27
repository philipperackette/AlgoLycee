import math
from decimal import Decimal, getcontext


def exp_serie(x: float, n: int) -> float:
    """
    Approximation de e^x par la série de Taylor (version flottante).

    Somme_{k=0..n} x^k / k!
    """
    terme = 1.0  # k = 0
    somme = terme
    for k in range(1, n + 1):
        terme *= x / k  # évite de recalculer x**k à chaque fois
        somme += terme
    return somme


def exp_decimal(x: str, n: int, precision: int) -> Decimal:
    """
    Version haute précision décimale de e^x.

    x est passé en chaîne pour éviter les conversions flottantes.
    """
    getcontext().prec = precision
    x_dec = Decimal(x)
    terme = Decimal(1)
    somme = terme
    for k in range(1, n + 1):
        terme *= x_dec / k
        somme += terme
    return somme


def main() -> None:
    approx_float = exp_serie(1.0, 20)
    print("Approximation flottante de e :", approx_float)
    print("Valeur math.e                 :", math.e)

    approx_dec = exp_decimal("1", n=120, precision=80)
    print("Approximation décimale de e  :", approx_dec)


if __name__ == "__main__":
    main()