from math import sqrt
from decimal import *
D=Decimal
getcontext().prec=1100
def archimede(n):
    T=D(8)
    S=D(4*Decimal.sqrt(D(2)))
    for k in range(n):
        T=D(2*(S*T)/(S+T))
        S=D(Decimal.sqrt(S*T))
    #affichage des périmètres des polygone inscrits et circonscrits
    #print("T =", T, "S =",S)
    #encadrement de π
    print(format(T/2,'.1001g'), "< π <",format(S/2,'.1001g'))
print("1000 décimales de π")
archimede(1700)