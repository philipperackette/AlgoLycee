# tests_rapides.py

from Factorielle import factorielle
from MultipleDiviseurNombrePremier import est_premier
from PremierePuissanceSuperieure import (
    puissance_superieure,
    puissance_inferieure,
)
from ifactor import decomposition_facteurs_premiers

def test_factorielle():
    assert factorielle(0) == 1
    assert factorielle(1) == 1
    assert factorielle(5) == 120
    print("✓ Test factorielle réussi")

def test_est_premier():
    assert est_premier(2)
    assert est_premier(3)
    assert est_premier(17)
    assert not est_premier(1)
    assert not est_premier(9)
    assert not est_premier(15)
    print("✓ Test nombres premiers réussi")

def test_puissances():
    assert puissance_superieure(2, 5) == 8
    assert puissance_inferieure(2, 5) == 4
    assert puissance_superieure(2, 8) == 8
    assert puissance_inferieure(2, 8) == 8
    print("✓ Test puissances réussi")

def test_facteurs_premiers():
    resultat = decomposition_facteurs_premiers(360)
    # 360 = 2^3 * 3^2 * 5
    assert resultat == {2: 3, 3: 2, 5: 1}
    print("✓ Test facteurs premiers réussi")

if __name__ == "__main__":
    test_factorielle()
    test_est_premier()
    test_puissances()
    test_facteurs_premiers()
    print("\n🎉 Tous les tests passent avec succès !")