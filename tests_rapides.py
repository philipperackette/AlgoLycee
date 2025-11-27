# tests_rapides.py

from Factorielle import factorielle
from MultipleDiviseurNombrePremier import estPremier
from PremierePuissanceSuperieure import (
    premierePuissanceDeaSuperieureAb,
    premierePuissanceDeaInferieureAb,
)
from ifactor import ifactors

def test_factorielle():
    assert factorielle(0) == 1
    assert factorielle(1) == 1
    assert factorielle(5) == 120

def test_estPremier():
    assert estPremier(2)
    assert estPremier(3)
    assert not estPremier(1)
    assert not estPremier(9)

def test_puissances():
    assert premierePuissanceDeaSuperieureAb(2, 5) == 8
    assert premierePuissanceDeaInferieureAb(2, 5) == 4

def test_ifactor():
    d = ifactors(360, decomp=False)
    # 360 = 2^3 * 3^2 * 5
    assert d == {2: 3, 3: 2, 5: 1}

if __name__ == "__main__":
    test_factorielle()
    test_estPremier()
    test_puissances()
    test_ifactor()
    print("Tous les tests passent ✔️")