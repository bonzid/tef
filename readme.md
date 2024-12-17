# Transducteur à États Finis (TEF)  
Doria BONZI - 01/11/2024

## Objectifs

Dans le cadre d'un travail étudiant autour de la programmation orientée objet, nous avons développé un projet autour des transducteurs à états finis dont l'objectif était de : 
- Programmer une classe **TEF** (Transducteur à États Finis) qui prend en entrée la définition d’un transducteur à états finis simplifié.
- Instancier deux objets de type TEF permettant de réaliser les tâches :
  - De **tokenisation** simplifiée d'un texte.
  - De **transformation** d'un fichier au format CSV en format TSV.


## Fonctionnement de la classe TEF

### 1. Définition du Transducteur à États Finis

Lors de l'instanciation d'un objet TEF, la définition du transducteur est fournie sous forme d'un état initial et d'un dictionnaire d'états. Ce dictionnaire **"etats"** associe chaque état aux transitions possibles depuis cet état. La définition du transducteur se fait lors de l'instanciation de l'objet en paramètres.

Objets : 
Entrée : soit un fichier, soit une chaîne de caractères
Sortie : chaîne de caractères à la console


### 2. Fonctionnalités

- **`__len__()`** : retourne le nombre d'états dans le transducteur
  
- **`ajout_transition()`** : permet d'ajouter une transition au transducteur. Cette transition est définie par :
  - L'état de départ,
  - La chaîne d'entrée,
  - La chaîne de sortie,
  - L'état suivant la transition

- **`__add__()` et `__sub__()`** : permettent respectivement d'ajouter ou de supprimer des transitions à partir des informations fournies

- **`analyse()`** : prend une chaîne de caractères en entrée, applique les transitions définies dans le transducteur, et renvoie la chaîne de sortie générée

- **`read()`** : si l'entrée à analyser est un fichier, cette fonction permet de lire et renvoyer son contenu


### 3. Fonctionnement du convertisseur CSV vers TSV

La classe TEF est utilisée dans une fonction **`csv_to_tsv()`**, permettant de convertir un fichier CSV en fichier TSV. Cette fonction prend en entrée le chemin d'un fichier CSV et génère un fichier TSV en sortie.



---

### Structure du Projet

Le projet contient les fichiers suivants :
- **TEF.py** : le fichier contenant la classe TEF et ses méthodes
- **csv_to_tsv.py** : le script permettant de convertir des fichiers CSV en TSV
- **tests.py** : un script d'instanciation d'une machine à rires dans la classe TEF à titre de test, ainsi que l'instanciation d'un tokeniseur simpliste.
- **tests/** : un répertoire contenant des exemples de fichiers à utiliser
- **outputs/** : un répertoire pour les fichiers de sortie

---

### Limites

- La conversion CSV en TSV n'est pas encore capable de traiter des cas complexes tels que les virgules au sein des cellules.
- La fonction `csv_to_tsv()` utilise la classe TEF pour produire un fichier TSV, mais cette fonctionnalité de sortie de type fichier n'est pas disponible dans la classe TEF seule.
- Il serait intéressant de pouvoir mettre les paramètres du transducteur dans un fichier pour instnacier un nouvel objet.
