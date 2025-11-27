def sont_alignes(A, B, C):
    """
    Teste si 3 points A, B, C sont alignés
    en utilisant le déterminant des vecteurs AB et AC
    """
    # Vecteur AB
    AB_x = B[0] - A[0]
    AB_y = B[1] - A[1]
    
    # Vecteur AC  
    AC_x = C[0] - A[0]
    AC_y = C[1] - A[1]
    
    # Déterminant
    determinant = AB_x * AC_y - AB_y * AC_x
    
    # Si le déterminant est proche de 0, les points sont alignés
    return abs(determinant) < 1e-9

# Programme principal
print("Test d'alignement de 3 points")
xA = float(input("x_A = "))
yA = float(input("y_A = "))
xB = float(input("x_B = "))
yB = float(input("y_B = "))
xC = float(input("x_C = "))
yC = float(input("y_C = "))

A = (xA, yA)
B = (xB, yB)
C = (xC, yC)

if sont_alignes(A, B, C):
    print("✓ A, B et C sont alignés")
else:
    print("✗ A, B et C ne sont pas alignés")