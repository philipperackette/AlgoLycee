def archimede_pi(n_iterations):
    """
    Approximation de π par la méthode d'Archimède
    avec des polygones réguliers
    """
    # On part d'un hexagone (6 côtés)
    n_cotes = 6
    cote = 1.0  # polygone inscrit dans un cercle de rayon 1
    
    for i in range(n_iterations):
        # Doublage du nombre de côtés
        n_cotes *= 2
        
        # Nouvelle longueur du côté
        cote_nouveau = (2 - (4 - cote**2)**0.5)**0.5
        
        # Périmètre du polygone inscrit
        perimetre_inscrit = n_cotes * cote_nouveau
        
        # Approximation de π (périmètre / diamètre)
        pi_approx = perimetre_inscrit / 2
        
        cote = cote_nouveau
    
    return pi_approx

print("Approximation de π par Archimède:")
for n in [3, 4, 5]:
    approx = archimede_pi(n)
    print(f"Après {2**(n+1)} côtés: π ≈ {approx:.10f}")
