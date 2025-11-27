# AlgoLycee

Quelques scripts Python pour illustrer des notions d'algorithmique et de mathématiques au lycée.

Les fichiers sont indépendants : chaque script peut être exécuté seul, pour travailler une notion précise (alignement, factorielle, approximation de π, etc.).

---

## Prérequis

- Python 3 (version 3.8 ou plus récente recommandée)
- Les scripts utilisent uniquement la bibliothèque standard de Python, **sauf** :

  - [`sympy`](https://www.sympy.org/) pour `EquationDroite.py`

---

## Installation des bibliothèques nécessaires

### Avec `pip` (installation classique)

Assurez-vous d’avoir Python installé, puis dans un terminal :

```bash
python3 -m pip install --upgrade pip
python3 -m pip install sympy
```

Selon la configuration du système, la commande peut être `python` au lieu de `python3` :

```bash
python -m pip install sympy
```

### Avec `conda` (Anaconda / Miniconda)

Si vous utilisez un environnement `conda` :

```bash
conda install sympy
```

Une fois cette dépendance installée, tous les scripts du dépôt doivent pouvoir s’exécuter sans erreur d’import.

---

## Contenu des scripts

### `AlignementTroisPoints.py`

Test de l'alignement de trois points dans le plan via le déterminant de deux vecteurs.

- Entrée : coordonnées \((x_A, y_A)\), \((x_B, y_B)\), \((x_C, y_C)\).
- Sortie : message indiquant si les trois points sont alignés ou non.
- Utilise une tolérance numérique (`math.isclose`) pour éviter les erreurs d’arrondi.

---

### `ApproximationDeE.py`

Approximation de \( e^x \) par la série de Taylor.

- Version flottante : somme des \( x^k / k! \) pour \( k = 0 \ldots n \).
- Version haute précision : utilisation du module `decimal` pour calculer \( e \) avec de nombreuses décimales.

---

### `ApproximationPiArchimede.py`

Encadrement de \( \pi \) par la méthode d'Archimède :

- Polygones réguliers inscrits et circonscrits dans le cercle unité.
- À chaque itération, on augmente le nombre de côtés et on améliore l’encadrement.
- Utilise `decimal` pour obtenir un grand nombre de décimales si souhaité.

---

### `ApproximationRacineDeDeux.py`

Approximations de \( \sqrt{2} \) par plusieurs méthodes :

- Balayage (recherche par pas de \(10^{-n}\) dans \([1, 2]\)).
- Dichotomie en flottant sur \([1, 2]\).
- Dichotomie avec `decimal` (haute précision).
- Méthode de Newton avec `decimal` (très efficace pour beaucoup de décimales).

---

### `EquationDroite.py`

Équation d'une droite passant par deux points, simplifiée avec `sympy`.

- Entrée : deux points \(A(x_A, y_A)\), \(B(x_B, y_B)\) (distincts).
- Sortie : une équation de droite sous forme symbolique, par exemple  
  \((y - y_A)(x_B - x_A) - (x - x_A)(y_B - y_A) = 0\) simplifiée.

---

### `Factorielle.py`

Calcul de la factorielle \( n! \) pour un entier \( n \geq 0 \).

- Version itérative (pas de récursion) pour éviter les problèmes de profondeur de pile.
- Le fichier contient un petit test si on l’exécute directement.

---

### `GenerationPermutationsEnsemble.py`

Génération récursive de toutes les permutations d’un ensemble fini.

- Exemple fourni : permutations de `['A', 'B', 'C', 'D']`.
- Peut être réutilisé pour n’importe quelle liste ou séquence.

---

### `ifactor.py`

Décomposition en facteurs premiers d’un entier \( n \geq 2 \).

- Si `decomp=False` (par défaut) : renvoie un dictionnaire `{prime: exposant}`.
- Si `decomp=True` : renvoie une chaîne de la forme  
  `2³ × 3² × 5` avec de jolis exposants (², ³, …).
- Basé sur une méthode de division successive, suffisante pour des entiers de taille “lycée”.

---

### `MultipleDiviseurNombrePremier.py`

Regroupe plusieurs fonctions arithmétiques :

- `aEstMultipleDeb(a, b)` : teste si `a` est un multiple de `b`  
  (avec un traitement explicite du cas `b = 0` : seul `0` est multiple de `0`).
- `plusGrandMultipleDeaInferieurAb(a, b)` : plus grand multiple de `a` inférieur ou égal à `b`.
- `estPremier(n)` : test de primalité naïf mais efficace pour les valeurs courantes en classe.

---

### `PremierePuissanceSuperieure.py`

Recherche de puissances de `a` encadrant `b` (pour \(|a| > 1\)) :

- `premierePuissanceDeaSuperieureAb(a, b)` : plus petite puissance de `a` supérieure ou égale à `b`.
- `premierePuissanceDeaInferieureAb(a, b)` : plus grande puissance de `a` inférieure ou égale à `b`.

---

### `tests_rapides.py`

Petit fichier de tests “à la main” pour vérifier le bon fonctionnement de quelques fonctions importantes :

- Teste :
  - `factorielle` (`Factorielle.py`)
  - `estPremier` (`MultipleDiviseurNombrePremier.py`)
  - les fonctions de puissances (`PremierePuissanceSuperieure.py`)
  - `ifactors` (`ifactor.py`)

Exécution :

```bash
python tests_rapides.py
```

Si tout va bien, le script affiche :

```text
Tous les tests passent ✔️
```

---

## Exécution des scripts

Les scripts sont pensés pour être exécutés individuellement depuis un terminal, par exemple :

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
```

Chaque fichier contient un bloc :

```python
if __name__ == "__main__":
    ...
```

ce qui permet :
- une exécution directe en ligne de commande (mode “programme principal”),
- mais aussi l’import dans un autre script Python (mode “bibliothèque”) sans effet de bord.
