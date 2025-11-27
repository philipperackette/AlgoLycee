def puissance_superieure(a, b):
    """
    Plus petite puissance de a supérieure ou égale à b
    """
    if a <= 1:
        return "a doit être > 1"
    
    puissance = 1
    while puissance < b:
        puissance *= a
    
    return puissance

def puissance_inferieure(a, b):
    """
    Plus grande puissance de a inférieure ou égale à b
    """
    if a <= 1:
        return "a doit être > 1"
    
    puissance = 1
    while puissance * a <= b:
        puissance *= a
    
    return puissance

# Tests
a = 2
valeurs_b = [1, 5, 10, 20]

print(f"Puissances de {a}:")
for b in valeurs_b:
    sup = puissance_superieure(a, b)
    inf = puissance_inferieure(a, b)
    print(f"b={b:2d} → puissance ≥ b: {sup:2d}, puissance ≤ b: {inf:2d}")