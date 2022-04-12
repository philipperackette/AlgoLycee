def premierePuissanceDeaSuperieureAb(a,b):
    if a!=0 and a!=1:
        if b<=0:
            return(1)
        else:
            m=1
            while(m<b):
                m=m*a
            return(m)
    elif b==1:
        return(1)

def premierePuissanceDeaInferieureAb(a,b):
    if a>0 and a!=1 and b!=0:
        if b<=0:
            return(1)
        else:
            m=1
            while(m*a<=b):
                m=m*a
            return(m)
    elif b==1 and a>0:
        return(1)