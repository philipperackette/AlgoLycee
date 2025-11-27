def permutations_simples(elements):
    """
    Génère les permutations d'une liste (version simplifiée)
    """
    if len(elements) <= 1:
        return [elements]
    
    resultat = []
    for i in range(len(elements)):
        element_courant = elements[i]
        elements_restants = elements[:i] + elements[i+1:]
        
        for perm in permutations_simples(elements_restants):
            resultat.append([element_courant] + perm)
    
    return resultat

# Test avec 3 éléments
elements = ['A', 'B', 'C']
print(f"Permutations de {elements}:")
for perm in permutations_simples(elements):
    print(perm)