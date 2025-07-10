# Python - Abstract Base Classes (ABC)

Ce projet explore les concepts avancés de la programmation orientée objet en Python, en particulier l'utilisation des classes abstraites (ABC), du duck typing, des mixins et de l'héritage multiple.

## Description

Ce projet fait partie du curriculum Holberton School et vise à approfondir la compréhension des concepts suivants :
- Classes abstraites et méthodes abstraites
- Duck typing et polymorphisme
- Héritage multiple et résolution d'ordre de méthodes (MRO)
- Mixins et composition
- Itérateurs personnalisés
- Surcharge de méthodes

## Fichiers

| Fichier | Description |
|---------|-------------|
| `task_00_abc.py` | Implémentation de classes abstraites avec ABC |
| `task_01_duck_typing.py` | Démonstration du duck typing avec des formes géométriques |
| `task_02_verboselist.py` | Création d'une liste verbose qui hérite de la classe `list` |
| `task_03_countediterator.py` | Implémentation d'un itérateur qui compte les éléments |
| `task_04_flyingfish.py` | Exemple d'héritage multiple avec un poisson volant |
| `task_05_dragon.py` | Utilisation de mixins pour créer un dragon |
| `main_*.py` | Fichiers de test pour chaque tâche |

## Concepts abordés

### 1. Classes abstraites (ABC)

Les classes abstraites définissent une interface commune que les sous-classes doivent implémenter :

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
```

### 2. Duck Typing

Le duck typing permet de traiter les objets en fonction de leurs méthodes plutôt que de leur type :

```python
def shape_info(obj):
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
```

### 3. Héritage multiple

Python supporte l'héritage multiple avec une résolution d'ordre des méthodes (MRO) :

```python
class FlyingFish(Fish, Bird):
    def habitat(self):
        print("The flying fish lives both in water and the sky!")
```

### 4. Mixins

Les mixins fournissent des fonctionnalités réutilisables :

```python
class SwimMixin:
    def swim(self):
        print("The creature swims!")

class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
```

### 5. Itérateurs personnalisés

Création d'itérateurs avec des fonctionnalités supplémentaires :

```python
class CountedIterator:
    def __next__(self):
        # Logique d'itération avec comptage
        pass
```

## Utilisation

Chaque fichier peut être testé avec son fichier main correspondant :

```bash
# Test des classes abstraites
python3 main_00_abc.py

# Test du duck typing
python3 main_01_duck_typing.py

# Test de la liste verbose
python3 main_02_verboselist.py

# Test de l'itérateur compteur
python3 main_03_countediterator.py

# Test de l'héritage multiple
python3 main_04_flyingfish.py

# Test des mixins
python3 main_05_dragon.py
```

## Exemples d'exécution

### Task 00 - Classes abstraites
```bash
$ python3 main_00_abc.py
Bark
Meow
```

### Task 01 - Duck typing
```bash
$ python3 main_01_duck_typing.py
Area: 78.53981633974483
Perimeter: 31.41592653589793
Area: 28
Perimeter: 22
```

### Task 02 - Liste verbose
```bash
$ python3 main_02_verboselist.py
Added 4 to the list.
Extended the list with 2 items.
Removed 2 from the list.
Popped 6 from the list.
Popped 1 from the list.
```

### Task 03 - Itérateur compteur
```bash
$ python3 main_03_countediterator.py
Got 1, total 1 items iterated.
Got 2, total 2 items iterated.
Got 3, total 3 items iterated.
Got 4, total 4 items iterated.
No more items.
```

### Task 04 - Héritage multiple
```bash
$ python3 main_04_flyingfish.py
The flying fish is swimming!
The flying fish is soaring!
The flying fish lives both in water and the sky!
```

### Task 05 - Mixins
```bash
$ python3 main_05_dragon.py
The creature swims!
The creature flies!
The dragon roars!
```

## Structure du projet

```
python-abc/
├── task_00_abc.py              # Classes abstraites
├── task_01_duck_typing.py      # Duck typing
├── task_02_verboselist.py      # Liste verbose
├── task_03_countediterator.py  # Itérateur compteur
├── task_04_flyingfish.py       # Héritage multiple
├── task_05_dragon.py           # Mixins
├── main_00_abc.py              # Test classe abstraite
├── main_01_duck_typing.py      # Test duck typing
├── main_02_verboselist.py      # Test liste verbose
├── main_03_countediterator.py  # Test itérateur
├── main_04_flyingfish.py       # Test héritage multiple
├── main_05_dragon.py           # Test mixins
└── README.md                   # Ce fichier
```

## Concepts Python utilisés

- **ABC (Abstract Base Classes)** : `from abc import ABC, abstractmethod`
- **Décorateurs** : `@abstractmethod`
- **Héritage** : `class Child(Parent)`
- **Héritage multiple** : `class Child(Parent1, Parent2)`
- **Super()** : Appel des méthodes parentes
- **Méthodes magiques** : `__init__`, `__next__`, `__iter__`
- **Gestion des exceptions** : `try/except StopIteration`
- **F-strings** : `f"Text {variable}"`
- **Polymorphisme** : Même interface, comportements différents

## Prérequis

- Python 3.8 ou supérieur
- Compréhension de base de la POO en Python
- Connaissance des concepts d'héritage et de polymorphisme

## Installation

```bash
# Cloner le projet
git clone <repository-url>

# Aller dans le répertoire
cd python-abc

# Rendre les fichiers exécutables
chmod +x *.py

# Tester tous les fichiers
python3 -m pytest  # Si pytest est installé
```

## Bonnes pratiques

1. **Utiliser des classes abstraites** pour définir des interfaces
2. **Préférer la composition à l'héritage** quand possible
3. **Documenter les classes et méthodes** avec des docstrings
4. **Suivre le principe DRY** (Don't Repeat Yourself)
5. **Respecter le MRO** (Method Resolution Order) en héritage multiple
6. **Utiliser des mixins** pour partager des fonctionnalités
7. **Implémenter correctement** les protocoles d'itérateurs

## Debugging

```bash
# Vérifier le MRO d'une classe
print(MyClass.__mro__)

# Vérifier les méthodes disponibles
print(dir(my_object))

# Debugger avec pdb
import pdb; pdb.set_trace()
```

## Tests

```bash
# Tester individuellement
python3 task_00_abc.py

# Tester avec doctest
python3 -m doctest task_*.py

# Vérifier le style de code
python3 -m pycodestyle task_*.py
```

## Ressources

- [Documentation officielle Python ABC](https://docs.python.org/3/library/abc.html)
- [Duck Typing en Python](https://realpython.com/lessons/duck-typing/)
- [Héritage multiple en Python](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)
- [Mixins en Python](https://realpython.com/inheritance-composition-python/)
- [Itérateurs et générateurs](https://docs.python.org/3/tutorial/classes.html#iterators)

## Auteur

Krosenvag

## Licence

Ce projet est à des fins éducative 

---

*Dernière mise à jour : 2025*