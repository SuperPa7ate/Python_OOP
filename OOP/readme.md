# Classe Texte

Vous trouverez ci-joint les dossiers/fichiers concernant la classe texte. 

C'est une classe [Python](https://www.python.org/) qui utilise [Spacy](https://spacy.io/) et [pandas](https://pandas.pydata.org/) pour faire divers traitements sur un fichier texte au format .txt (tokenisation, POS-tagging) et les interroger (combien de noms dans le texte ? quels sont les noms ?).

Le tout peut ensuite être exporté au format excel (".xlsx").

## Prérequis

L'execution de ce script nécessite plusieurs librairies :
- [Spacy 3.5.0](https://spacy.io/) : librairie de NLP
    - les modèles de langue **en-core-web-sm** et **fr-core-news-md** 
- [pandas 1.5.3](https://pandas.pydata.org/) : librairie de visualisation de données
- [openpyxl 3.1.0](https://openpyxl.readthedocs.io/en/stable/) : librairie pour écrire un fichier excel
- [pip](https://pypi.org/project/pip/) ou [pipenv](https://pypi.org/project/pipenv/)
- bien entendu, un éditeur capable de lancer le script ([VSCode](https://code.visualstudio.com/), [PyCharm](https://www.jetbrains.com/pycharm/)...)

## Installation

Si j'ai bien fait mon travail (ce qui sera évidemment le cas, n'est-ce pas ?... n'est-ce pas ?...), il suffit de lancer la ligne de commande suivante à l'endroit où se trouve le dossier racine.

    pip install -r requirements.txt

Toutes les librairies et dépendances décrites plus haut s'y trouvent, et s'installeront d'elles-mêmes.

## Arborescence des fichiers
```
📦OOP
 ┣ 📂input_files
 ┃ ┣ 📜a.txt
 ┃ ┗ 📜text.txt
 ┣ 📂output_files
 ┃ ┗ 📜results_text.xlsx
 ┣ 📜class_text.py
 ┣ 📜readme.md
 ┗ 📜requirements.txt
 ```

### 📦OOP

Le dossier racine, qui contient un certain nombre de fichiers importants.

#### 📜class_text.py
L'endroit où se trouve tout le code et où il faudra l'executer.

Il contient 7 fonctions applicables à l'objet texte :

- .read() : ouvrir le fichier cible en format .txt
- .tokenize() : permet de tokeniser le texte
- .pos() : pos-tagging
- .pos_request(tag) : sort tous les mots taggés par le tag recherché
- .pos_stats() : sort les stats des POS
- .text_compare(texte2) : comparer texte 1 et texte 2 (comparaison sémantique de Spacy)
- .export_excel() : permet d'exporter les résultats dans un type de fichier donné

Chaque fonction contient une docstring normalement claire qui permet de s'y retrouver un peu.

#### 📜requirements.txt

Le fichier qui permet d'installer toutes les libraires et les dépendances nécessaires au bon fonctionnement du script.


#### 📜readme.md

Le fichier sous vos yeux actuellement. Il est beau hein ? (et normalement complet !)

### 📂input_files

C'est l'endroit où mettre les fichiers texte à traiter au format .txt.

### 📂output_files

L'endroit où est stocké le fichier de sortie généré par la fonction .export_excel().


## Pour utiliser le script

### Exemple d'utilisation de la classe texte

```python
test=Text("text.txt")
test.read()
test.tokenize()
test.pos()
test.pos_request("NOUN","ADJ")
```
    sortie de .pos_request() :

                    NOUN         ADJ
        0        élevage    intensif
        1       hors-sol     majeure
        2           type     porcins
```python
    test.text_compare("a.txt")
```
    sortie de .text_compare(text2.txt) :

        les deux textes sont similaires à : 0.6928972506883008 %
```python
    test.export_excel()
```

Exemple du fichier de sortie  :

![](https://i.imgur.com/Ck1ylZF.gif)

## Remerciements

COULANGE Sylvain pour avoir jeté un oeil à mon readme et avoir pointé quelques faiblesses.

Vous-mêmes, qui avez survécu jusqu'à la fin.