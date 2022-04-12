def vecteur(A,B):
   return([B[0]-A[0],B[1]-A[1]])

def determinant(u,v):
    return(u[0]*v[1]-u[1]*v[0])

xA=float(input("x_A = ? "))
yA=float(input("y_A = ? "))
xB=float(input("x_B = ? "))
yB=float(input("y_B = ? "))
xC=float(input("x_C = ? "))
yC=float(input("y_C = ? "))

AB=vecteur([xA,yA],[xB,yB])
AC=vecteur([xA,yA],[xC,yC])

if determinant(AB,AC)==0:
    print("Une droite passe par A, B et C.")
else :
    print("A, B et C ne sont pas alignés.")