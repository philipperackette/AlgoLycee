def carre(x):
    return(x**2)

def balayage(n):
    x1=1.0
    x2=1+10**(-n)
    while((carre(x1)-2.0)*(carre(x2)-2.0)>0):
        x1=x1+10**(-n)
        x2=x2+10**(-n)
    print(round(x1,n+1),"^2 = ", carre(x1))
    print(round(x2,n+1),"^2 = ", carre(x2))

def dichotomie(n):
    x1=0.0
    x2=2.0
    while(x2-x1>10**(-n)):
        m=(x1+x2)/2.0
        if(carre(m)-2<0):
            x1=m
        else:
            x2=m
    print(round(x1,n+1),"^2 = ", carre(x1))
    print(round(x2,n+1),"^2 = ", carre(x2))

from decimal import * #Augmentation du nombre de décimales
D=Decimal
getcontext().prec=1005
def cent_decimales():
    X1=D(0)
    X2=D(2)
    while(X2-X1>10**(-100)):
        M=D((X1+X2)/D(2.0))
        if(carre(M)-2<0):
            X1=M
        else:
            X2=M
    print(round(X1,100))

def newton(n):
    X1=D(1)
    X2=D(0.5)*(X1+2/X1)
    while(abs(X2-X1)>10**(-n)):
        X1=X2
        X2=D(0.5)*(X2+2/X2)
    print(round(X1,n))

print("-------------------------")
print("Balayage à 10^-7 :")
balayage(7)
print("-------------------------")
print("Dichotomie à 10^-12 :")
dichotomie(12)
print("-------------------------")
print("Cent premières décimales par dichotomie :")
cent_decimales()
print("-------------------------")
print("Mille premières décimales par méthode de Newton :")
newton(1000)