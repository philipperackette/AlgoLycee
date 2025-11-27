# AlgoLycee

Quelques scripts Python pour illustrer des notions d'algorithmique et de mathématiques au lycée.

## Contenu des scripts

- **AlignementTroisPoints.py**  
  Test de l'alignement de trois points dans le plan via le déterminant de deux vecteurs.

- **ApproximationDeE.py**  
  Approximation de \( e \) par la série de Taylor :
  - version flottante,
  - version haute précision avec `decimal`.

- **ApproximationPiArchimede.py**  
  Encadrement de \( \pi \) par la méthode d'Archimède à l'aide de polygones réguliers inscrits/circonscrits dans le cercle unité.

- **ApproximationRacineDeDeux.py**  
  Approximations de \( \sqrt{2} \) par :
  - balayage,
  - dichotomie en flottant,
  - dichotomie décimale (`decimal`),
  - méthode de Newton en haute précision.

- **EquationDroite.py**  
  Équation d'une droite passant par deux points, simplifiée à l'aide de `sympy`.

- **Factorielle.py**  
  Calcul de la factorielle \( n! \) (version itérative, sans récursion).

- **GenerationPermutationsEnsemble.py**  
  Génération récursive de toutes les permutations d'un ensemble fini.

- **ifactor.py**  
  Décomposition en facteurs premiers d'un entier :
  - sous forme de dictionnaire `{prime: exposant}`,
  - ou sous forme d'affichage “joli” avec exposants (², ³, etc.).

- **MultipleDiviseurNombrePremier.py**  
  Fonctions pour :
  - tester si un entier est multiple d'un autre,
  - trouver le plus grand multiple de `a` inférieur ou égal à `b`,
  - tester si un entier est premier.

- **PremierePuissanceSuperieure.py**  
  Recherche de :
  - la plus petite puissance de `a` supérieure ou égale à `b`,
  - la plus grande puissance de `a` inférieure ou égale à `b`, pour \(|a| > 1\).

## Exécution

Les scripts sont pensés pour être exécutés individuellement :

```bash
python AlignementTroisPoints.py
python ApproximationDeE.py
python ApproximationPiArchimede.py
python ApproximationRacineDeDeux.py
python EquationDroite.py
python Factorielle.py
python GenerationPermutationsEnsemble.py
python ifactor.py
python MultipleDiviseurNombrePremier.py
python PremierePuissanceSuperieure.py
