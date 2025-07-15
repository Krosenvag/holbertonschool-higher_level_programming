# JavaScript - DOM Manipulation

Ce projet explore les concepts fondamentaux de la manipulation du DOM (Document Object Model) en JavaScript. Il couvre les interactions avec les éléments HTML, la gestion d'événements, les appels API, et la modification dynamique du contenu web.

## Description

Ce projet fait partie du curriculum Holberton School et vise à approfondir la compréhension des concepts suivants :
- Sélection et manipulation d'éléments DOM
- Gestion d'événements JavaScript
- Modification de styles et classes CSS
- Création dynamique d'éléments HTML
- Appels API avec fetch()
- Manipulation de contenu textuel

## Fichiers

| Fichier | Description |
|---------|-------------|
| `0-script.js` / `0-main.html` | Change automatiquement la couleur du header en rouge |
| `1-script.js` / `1-main.html` | Change la couleur du header en rouge lors du clic |
| `2-script.js` / `2-main.html` | Ajoute une classe CSS rouge au header lors du clic |
| `3-script.js` / `3-main.html` | Alterne entre les classes rouge et verte du header |
| `4-script.js` / `4-main.html` | Ajoute un élément à une liste lors du clic |
| `5-script.js` / `5-main.html` | Met à jour le texte du header lors du clic |
| `6-script.js` / `6-main.html` | Affiche un personnage Star Wars via API |
| `7-script.js` / `7-main.html` | Affiche une liste de films Star Wars via API |
| `8-script.js` / `8-main.html` | Affiche une salutation en français via API |

## Concepts abordés

### 1. Sélection d'éléments DOM

```javascript
// Sélection par ID
const element = document.getElementById("mon-id");

// Sélection par sélecteur CSS
const header = document.querySelector("header");

// Sélection par classe
const elements = document.querySelectorAll(".ma-classe");
```

### 2. Modification de styles

```javascript
// Modification directe du style
element.style.color = "#FF0000";

// Ajout/suppression de classes CSS
element.classList.add("rouge");
element.classList.remove("vert");
element.classList.toggle("actif");
```

### 3. Gestion d'événements

```javascript
// Événement au chargement du DOM
document.addEventListener("DOMContentLoaded", function() {
    // Code à exécuter
});

// Événement de clic
element.addEventListener("click", function() {
    // Action à effectuer
});
```

### 4. Création d'éléments

```javascript
// Création d'un nouvel élément
const nouvelElement = document.createElement("li");
nouvelElement.textContent = "Nouveau texte";

// Ajout à un parent
parentElement.appendChild(nouvelElement);
```

### 5. Appels API avec fetch()

```javascript
fetch("https://api.exemple.com/data")
    .then(response => response.json())
    .then(data => {
        // Traitement des données
        element.textContent = data.propriete;
    })
    .catch(error => console.error('Erreur:', error));
```

## Utilisation

### Tests en navigateur

Chaque paire de fichiers HTML/JS peut être testée directement dans un navigateur :

```bash
# Ouvrir dans le navigateur
firefox 0-main.html
# ou
google-chrome 1-main.html
# ou
xdg-open 2-main.html
```

### Serveur HTTP local (pour les API)

Pour les fichiers utilisant des API (6, 7, 8), utilisez un serveur HTTP :

```bash
# Serveur Python
python3 -m http.server 8000

# Puis ouvrir dans le navigateur
firefox http://localhost:8000/6-main.html
```

## Exemples d'exécution

### Task 0 - Changement automatique de couleur
```
Ouvrir 0-main.html → Le header devient rouge automatiquement
```

### Task 1 - Changement de couleur au clic
```
Ouvrir 1-main.html → Cliquer sur "Red header" → Le header devient rouge
```

### Task 2 - Ajout de classe CSS
```
Ouvrir 2-main.html → Cliquer sur "Red header" → Classe "red" ajoutée au header
```

### Task 3 - Toggle entre couleurs
```
Ouvrir 3-main.html → Cliquer sur "Toggle header" → Alterne entre rouge et vert
```

### Task 4 - Ajout d'élément à une liste
```
Ouvrir 4-main.html → Cliquer sur "Add item" → Nouvel "Item" ajouté à la liste
```

### Task 5 - Mise à jour du texte
```
Ouvrir 5-main.html → Cliquer sur "Update the header" → Texte change pour "New Header!!!"
```

### Task 6 - Affichage de personnage Star Wars
```
Ouvrir 6-main.html → Affiche automatiquement "Leia Organa"
```

### Task 7 - Liste de films Star Wars
```
Ouvrir 7-main.html → Affiche automatiquement la liste des films
```

### Task 8 - Salutation en français
```
Ouvrir 8-main.html → Affiche automatiquement "Bonjour"
```

## APIs utilisées

- **Star Wars API** : `https://swapi-api.hbtn.io/api/`
  - Personnages : `/people/5/`
  - Films : `/films/`

- **Hello Salut API** : `https://hellosalut.stefanbohacek.dev/`
  - Salutations multilingues : `?lang=fr`

## Structure du projet

```
javascript-dom_manipulation/
├── 0-main.html              # HTML pour changement automatique
├── 0-script.js              # Script pour changement automatique
├── 1-main.html              # HTML pour changement au clic
├── 1-script.js              # Script pour changement au clic
├── 2-main.html              # HTML pour ajout de classe
├── 2-script.js              # Script pour ajout de classe
├── 3-main.html              # HTML pour toggle de couleur
├── 3-script.js              # Script pour toggle de couleur
├── 4-main.html              # HTML pour ajout d'élément
├── 4-script.js              # Script pour ajout d'élément
├── 5-main.html              # HTML pour mise à jour texte
├── 5-script.js              # Script pour mise à jour texte
├── 6-main.html              # HTML pour personnage Star Wars
├── 6-script.js              # Script pour personnage Star Wars
├── 7-main.html              # HTML pour films Star Wars
├── 7-script.js              # Script pour films Star Wars
├── 8-main.html              # HTML pour salutation
├── 8-script.js              # Script pour salutation
└── README.md                # Ce fichier
```

## Concepts JavaScript utilisés

- **DOM API** : `document`, `querySelector`, `getElementById`
- **Événements** : `addEventListener`, `DOMContentLoaded`, `click`
- **Styles** : `style.property`, `classList.add/remove/toggle`
- **Création d'éléments** : `createElement`, `appendChild`
- **Contenu** : `textContent`, `innerHTML`
- **Fetch API** : `fetch()`, `then()`, `catch()`
- **Promesses** : Gestion asynchrone avec `.then()`
- **JSON** : `response.json()`

## Debugging

### Outils de développement du navigateur

```javascript
// Console pour debugging
console.log("Valeur:", variable);
console.error("Erreur:", error);

// Vérifier les éléments DOM
console.log(document.getElementById("mon-id"));

// Vérifier les événements
element.addEventListener("click", function(event) {
    console.log("Clic détecté:", event);
});
```

### Vérification des erreurs communes

```javascript
// Vérifier si l'élément existe
const element = document.getElementById("mon-id");
if (element) {
    element.textContent = "Texte";
} else {
    console.error("Élément non trouvé");
}

// Gestion d'erreurs pour les API
fetch("url-api")
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .catch(error => console.error('Erreur API:', error));
```

## Bonnes pratiques

1. **Attendre le chargement du DOM** : Utiliser `DOMContentLoaded`
2. **Gestion d'erreurs** : Toujours inclure `.catch()` pour les appels API
3. **Sélecteurs efficaces** : Utiliser `getElementById` quand possible
4. **Validation des éléments** : Vérifier l'existence avant manipulation
5. **Code réutilisable** : Organiser le code en fonctions
6. **Console pour debugging** : Utiliser `console.log` pour le développement

## Prérequis

- Navigateur web moderne (Chrome, Firefox, Safari, Edge)
- Serveur HTTP local pour les tests API
- Connaissances de base en HTML, CSS et JavaScript

## Tests manuels

Pour chaque fichier, vérifiez :

1. **Fonctionnalité** : L'action attendue se produit-elle ?
2. **Erreurs console** : Aucune erreur JavaScript ?
3. **Responsive** : Fonctionne sur différentes tailles d'écran ?
4. **API** : Les données sont-elles récupérées correctement ?

## Ressources

- [MDN - DOM API](https://developer.mozilla.org/fr/docs/Web/API/Document_Object_Model)
- [MDN - Fetch API](https://developer.mozilla.org/fr/docs/Web/API/Fetch_API)
- [MDN - EventTarget.addEventListener](https://developer.mozilla.org/fr/docs/Web/API/EventTarget/addEventListener)
- [JavaScript.info - DOM](https://javascript.info/document)
- [Star Wars API Documentation](https://swapi.dev/)

## Auteur

Krosenvag

## Licence
Ce projet est à des fins éducatives uniquement.