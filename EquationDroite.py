def equation_droite(A, B):
    """
    Trouve l'équation de la droite passant par A et B
    """
    xA, yA = A
    xB, yB = B
    
    if xA == xB:  # droite verticale
        return f"x = {xA}"
    
    # Coefficient directeur
    a = (yB - yA) / (xB - xA)
    
    # Ordonnée à l'origine
    b = yA - a * xA
    
    if b == 0:
        return f"y = {a:.2f}x"
    elif b > 0:
        return f"y = {a:.2f}x + {b:.2f}"
    else:
        return f"y = {a:.2f}x - {abs(b):.2f}"

# Programme principal
print("Équation d'une droite passant par 2 points")
xA = float(input("x_A = "))
yA = float(input("y_A = "))
xB = float(input("x_B = "))
yB = float(input("y_B = "))

A = (xA, yA)
B = (xB, yB)

print(f"Équation: {equation_droite(A, B)}")