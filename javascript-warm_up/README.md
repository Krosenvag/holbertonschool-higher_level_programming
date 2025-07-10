# JavaScript - Warm up

Ce projet est une introduction aux concepts de base de JavaScript. Il couvre les fondamentaux du langage, la manipulation des arguments de ligne de commande, les fonctions, les objets, et les modules.

## Description

Ce projet fait partie du curriculum Holberton School et vise à familiariser les étudiants avec JavaScript à travers des exercices pratiques. Chaque fichier aborde un concept spécifique du langage.

## Fichiers

| Fichier | Description |
|---------|-------------|
| `0-javascript_is_amazing.js` | Affiche "JavaScript is amazing" en utilisant une constante |
| `1-multi_languages.js` | Affiche trois lignes de texte sur différents langages |
| `2-arguments.js` | Gère les arguments de ligne de commande et affiche leur statut |
| `3-value_argument.js` | Affiche la valeur du premier argument ou "No argument" |
| `4-concat.js` | Concatène deux arguments avec le format "X is Y" |
| `5-to_integer.js` | Convertit un argument en entier et l'affiche |
| `6-multi_languages_loop.js` | Utilise une boucle pour afficher des messages sur les langages |
| `7-multi_c.js` | Affiche "C is fun" X fois selon l'argument fourni |
| `8-square.js` | Dessine un carré avec le caractère 'X' |
| `9-add.js` | Additionne deux nombres passés en arguments |
| `10-factorial.js` | Calcule le factoriel d'un nombre de manière récursive |
| `11-second_biggest.js` | Trouve le deuxième plus grand nombre dans une liste |
| `12-object.js` | Démonstration de manipulation d'objets JavaScript |
| `13-add.js` | Exporte une fonction d'addition (module) |

## Utilisation

Chaque fichier peut être exécuté avec Node.js :

```bash
node nom_du_fichier.js [arguments]
```

### Exemples d'utilisation

```bash
# Afficher "JavaScript is amazing"
node 0-javascript_is_amazing.js

# Afficher des messages multi-langages
node 1-multi_languages.js

# Tester avec des arguments
node 2-arguments.js hello world
# Sortie: "arguments found"

node 2-arguments.js
# Sortie: "No argument"

# Afficher la valeur d'un argument
node 3-value_argument.js "Hello"
# Sortie: "Hello"

# Concaténer deux arguments
node 4-concat.js "Hello" "World"
# Sortie: "Hello is World"

# Convertir en entier
node 5-to_integer.js 42
# Sortie: "My number: 42"

# Utiliser une boucle pour afficher des langages
node 6-multi_languages_loop.js

# Répéter "C is fun"
node 7-multi_c.js 3
# Sortie: "C is fun" (3 fois)

# Dessiner un carré
node 8-square.js 4
# Dessine un carré 4x4 avec des 'X'

# Additionner deux nombres
node 9-add.js 3 5
# Sortie: "8"

# Calculer le factoriel
node 10-factorial.js 5
# Sortie: "120"

# Trouver le deuxième plus grand nombre
node 11-second_biggest.js 1 4 2 3 5
# Sortie: "4"

# Démonstration d'objets
node 12-object.js
```

## Concepts JavaScript abordés

### Variables et constantes
- Utilisation de `const` et `let`
- Portée des variables
- Différence entre `var`, `let`, et `const`

### Fonctions
- Déclaration de fonctions
- Fonctions anonymes
- Récursion
- Paramètres et arguments

### Structures de contrôle
- Conditions `if/else`
- Boucles `for` et `while`
- Opérateurs de comparaison

### Objets et tableaux
- Création et manipulation d'objets
- Propriétés et méthodes
- Parcours d'objets

### Modules
- `exports` et `require`
- Importation et exportation de fonctions
- Organisation du code en modules

### Arguments de ligne de commande
- Utilisation de `process.argv`
- Parsing des arguments
- Gestion des cas d'erreur

### Conversion de types
- `parseInt()` et `parseFloat()`
- `isNaN()` pour valider les nombres
- Conversion implicite et explicite

### Méthodes utiles
- `Math.max()`, `Math.min()`
- Méthodes de manipulation de chaînes
- Méthodes de tableaux

## Prérequis

- **Node.js** (version 14 ou supérieure)
- Terminal/ligne de commande
- Éditeur de texte

### Installation de Node.js

```bash
# Sur Ubuntu/Debian
sudo apt update
sudo apt install nodejs npm

# Vérifier l'installation
node --version
npm --version
```

## Style de code

Le code suit les conventions JavaScript standards :

- **Indentation** : 2 espaces
- **Noms de variables** : camelCase
- **Constantes** : `const` pour les valeurs non modifiées
- **Variables** : `let` pour les valeurs modifiables
- **Fonctions** : déclaration explicite avec `function` ou fléchées
- **Points-virgules** : optionnels mais cohérents dans le projet

## Debugging

Pour déboguer les scripts :

```bash
# Utiliser node avec des options de debug
node --inspect nom_du_fichier.js

# Afficher des informations détaillées
node --trace-warnings nom_du_fichier.js
```

## Tests

Pour tester manuellement les scripts :

```bash
# Tester tous les fichiers avec différents arguments
./test_all.sh

# Ou tester individuellement
node 0-javascript_is_amazing.js
node 1-multi_languages.js
# etc.
```

## Ressources utiles

- [Documentation officielle Node.js](https://nodejs.org/docs/)
- [Guide JavaScript MDN](https://developer.mozilla.org/fr/docs/Web/JavaScript)
- [Holberton School Curriculum](https://www.holbertonschool.com/)

## Auteur

Projet réalisé dans le cadre du curriculum **Holberton School**.

## Licence

Ce projet est à des fins éducatives uniquement dans le cadre du programme Holberton school