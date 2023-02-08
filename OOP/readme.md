# Classe Texte

Vous trouverez ci-joint les dossiers/fichiers concernant la classe texte. C'est une classe python qui utilise *Spacy* et *pandas* pour faire divers traitement sur un texte. Le tout peut ensuite être exporté au format excel (".xlsx").

# Arborescence des fichiers

📦OOP
┣ 📂input_files
┃ ┣ 📜a.txt
┃ ┗ 📜text.txt
┣ 📂output_files
┃ ┗ 📜results.xlsx
┣ 📜.env
┣ 📜class_text.py
┣ 📜Pipfile
┣ 📜Pipfile.lock
┗ 📜readme.md

## 📦OOP

Le dossier racine, qui contient un certain nombre de fichiers importants.
### 📜class_text.py
L'endroit où se trouve tout le code. Il contient 7 fonctions applicables à l'objet texte :

- read() : ouvrir le fichier cible en format .txt
- tokenize() : permet de tokeniser le texte
- pos() : pos-tagging
- pos_request(tag) : sort tous les mots taggés par le tag recherché
- pos_stats()) : sort les stats des POS
- text_compare(texte2) : comparer texte 1 et texte 2 (comparaison sémantique de Spacy)
- export_excel() : permet d'exporter les résultats dans un type de fichier donné

Chaque fonction contient une docstring normalement claire qui permet de s'y retrouver un peu.

### 📜Pipfile & 📜Pipfile.lock

Ce sont les fichiers de l'environnement virtuel créé par pipenv. Les fichiers pip permettent d'installer toutes les libraires et les dépendances nécessaires au bon fonctionnement du script.

### 📜.env

Chemin d'accès des librairies de l'environnement virtuel Python indiqué pour Windows. Pas certain que ce soit très utile outre mesure, c'était le cas pour moi alors je le mets quand même au cas où.

    PYTHONPATH="C:\Users\Raphael\.virtualenvs\python_oop--uNTNCoH\Lib"

### 📜readme.md

Le fichier sous vos yeux actuellement. Il est beau hein ? (et normalement complet !)

## 📂input_files

C'est l'endroit où mettre les fichiers texte à traiter au format .txt.

## 📂output_files

L'endroit où est stocké le fichier de sortie généré par la fonction .export_excel().



# Pour utiliser le script

## Charger le fichier Pipfile

En ligne de commande (via Pipenv) sur Windows (je sais pas pour les autres distributions) :

    pipenv sync

Permet d'installer toutes les dépendances nécessaires

## Exemple d'utilisation de la classe texte

    test=Text("text.txt")									#construit un objet texte
    test.read()
    test.tokenize()
    test.pos()
    test.pos_request("NOUN","ADJ")
    test.text_compare("a.txt")
    test.export_excel()
