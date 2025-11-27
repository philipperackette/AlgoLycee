def factorielle(n):
    """
    Calcule n! de manière itérative
    """
    if n < 0:
        return "Erreur: n doit être positif"
    
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    return resultat

# Table des factorielles
print("Table des factorielles:")
for i in range(8):
    print(f"{i}! = {factorielle(i)}")