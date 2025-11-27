def racine2_balayage(precision):
    """
    Approximation de √2 par balayage
    """
    pas = 10 ** -precision
    x = 1.0
    
    while x * x < 2:
        x += pas
    
    return x - pas/2  # milieu de l'intervalle

def racine2_dichotomie(precision):
    """
    Approximation de √2 par dichotomie
    """
    a, b = 1.0, 2.0
    
    for i in range(precision * 10):  # suffisamment d'itérations
        milieu = (a + b) / 2
        if milieu * milieu < 2:
            a = milieu
        else:
            b = milieu
    
    return (a + b) / 2

print("Approximations de √2:")
print(f"Par balayage (précision 6): {racine2_balayage(6):.8f}")
print(f"Par dichotomie (précision 10): {racine2_dichotomie(10):.8f}")
print(f"Valeur réelle: {2**0.5:.8f}")