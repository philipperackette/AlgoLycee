def est_multiple(a, b):
    """Teste si a est multiple de b"""
    if b == 0:
        return a == 0
    return a % b == 0

def est_premier(n):
    """Teste si n est premier"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Test des diviseurs impairs
    d = 3
    while d * d <= n:
        if est_multiple(n, d):
            return False
        d += 2
    
    return True

# Tests
print("Nombres premiers jusqu'à 30:")
for i in range(2, 31):
    if est_premier(i):
        print(f"{i} est premier")