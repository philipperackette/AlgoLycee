def factorielle(n: int) -> int:
    """
    Calcule n! pour n entier >= 0.

    Version itérative (évite les problèmes de récursion pour n grand).
    """
    if n < 0:
        raise ValueError("n doit être >= 0")

    resultat = 1
    for k in range(2, n + 1):
        resultat *= k
    return resultat


if __name__ == "__main__":
    # Petit test rapide
    for i in range(6):
        print(f"{i}! = {factorielle(i)}")