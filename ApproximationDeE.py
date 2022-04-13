from math import *
def Exp(x,n):
    E=1
    for k in range(1,n+1):
        E=E+(x**k)/factorial(k)
    return(E)
print("e =", Exp(1,17))