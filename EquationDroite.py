from sympy import *
x,y=symbols('x y')
init_printing(use_unicode=True)

xA=float(input('x_A = ? '))
yA=float(input('y_A = ? '))
xB=float(input('x_B = ? '))
yB=float(input('y_B = ? '))

print(simplify((x-xA)*(yB-yA)-(y-yA)*(xB-xA)),'= 0')
