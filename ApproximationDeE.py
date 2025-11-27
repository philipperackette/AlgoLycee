def approximation_e(n):
    """
    Approximation de e par la série 1 + 1/1! + 1/2! + ... + 1/n!
    """
    somme = 1.0
    fact = 1.0
    
    for i in range(1, n + 1):
        fact *= i  # calcul de i!
        somme += 1.0 / fact
    
    return somme

# Tests
print("Approximations de e:")
print(f"Avec 5 termes: {approximation_e(5):.6f}")
print(f"Avec 10 termes: {approximation_e(10):.6f}")
print(f"Avec 20 termes: {approximation_e(20):.6f}")
