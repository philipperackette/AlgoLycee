def aEstMultipleDeb(a,b):
    r=a
    if b != 0:
        while(r>0):
            r=r-b
        if r==0:
            return(True)
        else:
            return(False)
    elif a==0:
        return(True)
    else:
        return(False)

def plusGrandMultipleDeaInferieurAb(a,b):
    if b>=0:
        m=0
        while(m+abs(a)<=b):
            m=m+abs(a)
        return(m)
    else:
        return(-plusGrandMultipleDeaInferieurAb(a,-b)-abs(a))

def estPremier(n):
    if n>1:
        d=2
        while(d*d<=n):
            if aEstMultipleDeb(n,d):
                return(False)
            d=d+1
        return(True)
    return(False)

