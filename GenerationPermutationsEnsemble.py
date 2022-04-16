def permutations(E):
    if len(E)==0:
        return([])
    elif len(E)==1:
        return([E])
    else:
        perm=[]
        for i in range(len(E)):
            e=E[i]
            sousE=E[:i] + E[i+1:] #E privé de e
            for p in permutations(sousE): #récursivité
                perm.append([e] + p)
    return(perm)

for p in permutations(['A','B','C','D']):
    print(p)