# Python - Classes et Objets

Ce projet explore les concepts fondamentaux de la programmation orientée objet (POO) en Python, en se concentrant sur les classes, les objets, les propriétés, et l'encapsulation.

## Description

Ce projet fait partie du curriculum Holberton School et vise à approfondir la compréhension des concepts suivants :
- Définition et utilisation des classes
- Encapsulation et attributs privés
- Propriétés (getters et setters)
- Méthodes d'instance
- Structures de données personnalisées

## Fichiers

| Fichier | Description |
|---------|-------------|
| `0-square.py` | Définition d'une classe Square vide |
| `1-square.py` | Classe Square avec attribut privé size |
| `2-square.py` | Classe Square avec validation de l'attribut size |
| `3-square.py` | Classe Square avec méthode area() |
| `4-square.py` | Classe Square avec propriété size (getter/setter) |
| `5-square.py` | Classe Square avec méthode my_print() |
| `6-square.py` | Classe Square avec position et impression formatée |
| `100-singly_linked_list.py` | Implémentation d'une liste chaînée |
| `*-main.py` | Fichiers de test pour chaque classe |

## Concepts abordés

### 1. Classe de base

```python
class Square:
    """Represent a square."""
    pass
```

### 2. Attributs privés

```python
class Square:
    def __init__(self, size):
        self.__size = size  # Attribut privé
```

### 3. Validation des données

```python
def __init__(self, size=0):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size
```

### 4. Propriétés (Properties)

```python
@property
def size(self):
    """Get/set the current size of the square."""
    return self.__size

@size.setter
def size(self, value):
    if not isinstance(value, int):
        raise TypeError("size must be an integer")
    elif value < 0:
        raise ValueError("size must be >= 0")
    self.__size = value
```

### 5. Méthodes d'instance

```python
def area(self):
    """Return the current area of the square."""
    return self.__size * self.__size

def my_print(self):
    """Print the square with the # character."""
    for i in range(self.__size):
        print("#" * self.__size)
```

## Utilisation

### Exemples d'utilisation des classes Square

```python
# Classe de base
from 0-square import Square
my_square = Square()

# Avec taille
from 1-square import Square
my_square = Square(3)

# Avec validation
from 2-square import Square
try:
    my_square = Square("invalid")
except TypeError as e:
    print(e)  # size must be an integer

# Calcul d'aire
from 3-square import Square
my_square = Square(3)
print(my_square.area())  # 9

# Avec propriétés
from 4-square import Square
my_square = Square(3)
print(my_square.size)  # 3
my_square.size = 5
print(my_square.area())  # 25

# Impression du carré
from 5-square import Square
my_square = Square(3)
my_square.my_print()
# ###
# ###
# ###

# Avec position
from 6-square import Square
my_square = Square(3, (1, 1))
my_square.my_print()
#
#  ###
#  ###
#  ###
```

### Liste chaînée

```python
from 100-singly_linked_list import SinglyLinkedList

sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
print(sll)
# 2
# 3
# 5
```

## Évolution du projet

### Étape 0 : Classe vide
- Définition d'une classe Square basique

### Étape 1 : Attribut privé
- Ajout d'un attribut privé `__size`
- Constructeur avec paramètre size

### Étape 2 : Validation
- Validation du type et de la valeur de size
- Gestion des exceptions TypeError et ValueError

### Étape 3 : Méthode area
- Ajout d'une méthode pour calculer l'aire
- Accès aux attributs privés depuis les méthodes

### Étape 4 : Propriétés
- Implémentation des getters et setters
- Encapsulation avec validation

### Étape 5 : Impression
- Méthode my_print() pour afficher le carré
- Utilisation de caractères pour la représentation visuelle

### Étape 6 : Position
- Ajout d'un attribut position
- Gestion de l'espacement et du positionnement

### Étape 100 : Structure de données avancée
- Implémentation d'une liste chaînée
- Classes Node et SinglyLinkedList
- Insertion triée automatique

## Tests

Chaque fichier peut être testé avec son fichier main correspondant :

```bash
# Test de la classe de base
python3 0-main.py

# Test avec attribut privé
python3 1-main.py

# Test avec validation
python3 2-main.py

# Test avec méthode area
python3 3-main.py

# Test avec propriétés
python3 4-main.py

# Test avec impression
python3 5-main.py

# Test avec position
python3 6-main.py

# Test de la liste chaînée
python3 100-main.py
```

## Exemples d'exécution

### Square avec position
```bash
$ python3 6-main.py
###
###
###
--
 
 ###
 ###
 ###
--
   ###
   ###
   ###
--
```

### Liste chaînée triée
```bash
$ python3 100-main.py
-4
-3
1
2
3
3
4
5
5
10
12
```

## Concepts Python utilisés

- **Classes et objets** : `class`, `__init__`
- **Encapsulation** : attributs privés avec `__`
- **Propriétés** : `@property`, `@setter`
- **Gestion d'exceptions** : `raise TypeError`, `raise ValueError`
- **Validation de types** : `isinstance()`
- **Méthodes magiques** : `__str__`, `__init__`
- **Structures de données** : listes chaînées
- **Algorithmes** : insertion triée

## Bonnes pratiques

1. **Encapsulation** : Utiliser des attributs privés
2. **Validation** : Vérifier les types et valeurs
3. **Documentation** : Docstrings pour classes et méthodes
4. **Propriétés** : Getters/setters pour l'accès contrôlé
5. **Gestion d'erreurs** : Exceptions appropriées
6. **Lisibilité** : Code clair et bien structuré

## Structure du projet

```
python-classes/
├── 0-square.py              # Classe Square vide
├── 1-square.py              # Square avec attribut privé
├── 2-square.py              # Square avec validation
├── 3-square.py              # Square avec méthode area
├── 4-square.py              # Square avec propriétés
├── 5-square.py              # Square avec impression
├── 6-square.py              # Square avec position
├── 100-singly_linked_list.py # Liste chaînée
├── *-main.py                # Fichiers de test
├── __pycache__/             # Fichiers compilés Python
└── README.md                # Ce fichier
```

## Prérequis

- Python 3.8 ou supérieur
- Compréhension des concepts de base de Python
- Notions de programmation orientée objet

## Installation et utilisation

```bash
# Cloner le répertoire
git clone <repository-url>

# Naviguer dans le dossier
cd python-classes

# Rendre les fichiers exécutables
chmod +x *.py

# Tester un fichier spécifique
python3 0-main.py
```

## Debugging

```bash
# Vérifier les attributs d'un objet
print(my_square.__dict__)

# Vérifier le type d'un objet
print(type(my_square))

# Debugger avec les exceptions
try:
    my_square = Square(-1)
except ValueError as e:
    print(f"Erreur: {e}")
```

## Validation du code

```bash
# Vérifier le style avec pycodestyle
pycodestyle *.py

# Vérifier avec flake8
flake8 *.py

# Tester avec doctest
python3 -m doctest *.py
```

## Ressources

- [Documentation Python - Classes](https://docs.python.org/3/tutorial/classes.html)
- [Python Properties](https://docs.python.org/3/library/functions.html#property)
- [Python Data Model](https://docs.python.org/3/reference/datamodel.html)
- [OOP en Python](https://realpython.com/python3-object-oriented-programming/)
- [Python Encapsulation](https://docs.python.org/3/tutorial/classes.html#private-variables)

## Auteur

Krosenvag

## Licence

Ce projet est à des fins éducatives uniquement.
