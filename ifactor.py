def decomposition_facteurs_premiers(n):
    """
    Décomposition en facteurs premiers
    """
    if n < 2:
        return {}
    
    facteurs = {}
    d = 2
    
    while d * d <= n:
        while n % d == 0:
            if d in facteurs:
                facteurs[d] += 1
            else:
                facteurs[d] = 1
            n //= d
        d += 1
    
    if n > 1:
        facteurs[n] = 1
    
    return facteurs

def afficher_decomposition(n):
    """
    Affiche la décomposition de manière lisible
    """
    facteurs = decomposition_facteurs_premiers(n)
    
    if not facteurs:
        return f"{n} n'a pas de décomposition"
    
    termes = []
    for facteur, exposant in sorted(facteurs.items()):
        if exposant == 1:
            termes.append(str(facteur))
        else:
            termes.append(f"{facteur}^{exposant}")
    
    return f"{n} = " + " × ".join(termes)

# Tests
nombres = [12, 36, 100, 97]
for n in nombres:
    print(afficher_decomposition(n))