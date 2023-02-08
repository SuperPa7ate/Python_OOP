import spacy
import pandas as pd
import pathlib 
from pathlib import Path
import os

class Text :
    
    """classe texte :

    - read() : ouvrir le fichier cible en format .txt
    - tokenize() : permet de tokeniser le texte
    - pos() : pos-tagging
    - pos_request(tag) : sort tous les mots taggés par le tag recherché
    - pos_stats()) : sort les stats des POS  
    - text_compare(texte2) : comparer texte 1 et texte 2 (comparaison sémantique de Spacy)
    - export_excel() : permet d'exporter les résultats dans un type de fichier donné
    """

    BASE_DIR=Path("t.py").resolve().parent

    def __init__ (self, fileName, directory=BASE_DIR, encoding="UTF-8", language="fr"):
        self.directory=directory    #chemin d'accès du fichier/arborescence
        self.fileName=fileName      #nom du fichier à traiter (ex : "text.txt")
        self.encoding=encoding      #encodage par défaut
        self.content=""             #contenu textuel du fichier lu une fois .read() utilisé
        self.tokenized=[]           #structure qui contiendra les token du texte (.tokenize())
        self.language=language      #langue du texte, utilisée pour charger le modèle de langue de Spacy (fr : français, en : anglais)
        
        #crée la variable modèle de langue Spacy de l'objet, et charge le modèle de langue
        if self.language=="fr":
            self.nlp=spacy.load('fr_core_news_md')
        elif self.language=="eng":
            self.nlp=spacy.load("en_core_web_sm")

    def read(self, directory=os.path.join(BASE_DIR,"input_files"), encoding="UTF-8"):
        """Ouvre un fichier texte au format .txt et en stocke le contenu."""
        try: 
            with open(directory+'/'+self.fileName, mode="r", encoding=encoding) as f:
                self.content=f.read()
        except OSError as err:
            print("OS error : {0}".format(err))

    def tokenize(self):
        """Tokenise le texte et stocke les tokens dans un tableau indicé, retourne le tableau (self.tokenized)."""
        doc=self.nlp(self.content)

        for token in doc:
            self.tokenized.append(token)
        return self.tokenized
    
    def pos(self):
        """Effectue le pos-tagging du texte (self.content), retourne un dictionnaire (clé=pos, valeur=token(s))."""

        #gestion de l'erreur si .tokenize() n'a pas été utilisé avant
        try:
            self.content
        except AttributeError:
            self.tokenize()

        doc=self.nlp(self.content)
        self.dictPOS={}                               #initialisation du dictionnaire retourné (appartenant aux variables de l'objet)

        for token in doc:
            if token.pos_ in self.dictPOS.keys():     #si le POS existe déjà en clé, on fait rien
                pass
            else:
                self.dictPOS[token.pos_]=[]           #sinon on crée un tableau et on ajoute le token
            self.dictPOS[token.pos_].append(token)

        return self.dictPOS
    
    def pos_request(self, *pos_name, display_all=False):
        """Permet d'interroger le dictionnaire obtenu par .pos(), print les tokens associés.
        Liste des POS :
         
            -ADJ: adjective
            -ADP: adposition
            -ADV: adverb
            -AUX: auxiliary
            -CCONJ: coordinating conjunction
            -DET: determiner
            -INTJ: interjection
            -NOUN: noun
            -NUM: numeral
            -PART: particle
            -PRON: pronoun
            -PROPN: proper noun
            -PUNCT: punctuation
            -SCONJ: subordinating conjunction
            -SYM: symbol
            -VERB: verb
            -X: other
        
        Pour afficher tous les tokens et leur POS, display_all=True.
        """

        #vérification que la fonction .pos() dictPOS été utilisée avant, si non on l'applique (pour pouvoir itérer sur self.dictPOS)
        try:
            self.dictPOS
        except AttributeError:
            self.pos()

        #utilisation de pandas pour faire un affichage correct et formaté (en enlevant les valeurs manquantes pour la lisibilité)
        if display_all:
            df=pd.DataFrame.from_dict(test.dictPOS, orient="index")
            df=df.transpose()
            pm = df.apply(sorted, key=pd.isnull)
            new = pm[~pd.isnull(pm).all(1)].fillna("")
            print(new)
            
        else:
            #initialisation du dictionnaire qui va servir à garder en mémoire les POS demandés + un flag pour arrêter la fonction après le traitement de l'erreur
            selected_pos={}  
            flag=False

            #parcours du tuple donné par *pos_name
            for pos in pos_name:
                try:
                    selected_pos[pos]=self.dictPOS[pos]

                except KeyError:
                    flag=True
                    print("\n Le POS","\""+pos+"\"","demandé n'existe pas pour ce texte, la liste des POS disponible est : ")
                    print(self.dictPOS.keys(),"\n")
            
            #si flag, on affiche pas selected_pos, si non on l'affiche
            if flag:
                return
            else:
            #affichage du tableau selected_pos, qui regroupe les POS demandés
                df=pd.DataFrame.from_dict(selected_pos, orient="index")
                df=df.transpose()
                pm = df.apply(sorted, key=pd.isnull)
                new = pm[~pd.isnull(pm).all(1)].fillna("")
                print(new)

    def pos_stats(self, *pos_name, display_all=False):
        """Permet d'interroger le nombre de tokens appartenant à un POS, retourne le tout sous forme de dictionnaire. 
        
         Liste des POS :
         
            -ADJ: adjective
            -ADP: adposition
            -ADV: adverb
            -AUX: auxiliary
            -CCONJ: coordinating conjunction
            -DET: determiner
            -INTJ: interjection
            -NOUN: noun
            -NUM: numeral
            -PART: particle
            -PRON: pronoun
            -PROPN: proper noun
            -PUNCT: punctuation
            -SCONJ: subordinating conjunction
            -SYM: symbol
            -VERB: verb
            -X: other

        Pour tout afficher, display_all=True.
        """

        #vérification que la fonction .pos() dictPOS été utilisée avant, si non on l'applique (pour pouvoir itérer sur self.dictPOS)
        try:
            self.dictPOS
        except AttributeError:
            self.pos()

        self.pos_stats={}                        #intialisation du dictionnaire qui va contenir les "stats" du texte

        if display_all:  
            for key in self.dictPOS:              #parcours des POS en clé du dictionnaire donné par .pos()
                self.pos_stats[key]=0
                for value in self.dictPOS[key]:   #pour chaque token associé au POS on incrémente
                    self.pos_stats[key]+=1

            df=pd.DataFrame.from_dict(self.pos_stats, orient="index")
            print(df.transpose())

            return self.pos_stats

        else:                               #la même chose mais pour un POS spécifique avec une gestion de l'erreur
            flag=False

            #parcours du tuple donné par *pos_name
            for pos in pos_name:

                #vérification que le POS demandé existe, sinon gestion de l'erreur
                try:
                    self.pos_stats[pos]=0

                    #on compte le nombre de token dans le POS demandé
                    for value in self.dictPOS[pos]:
                        self.pos_stats[pos]+=1

                except KeyError:
                    flag=True
                    print("\n Le POS","\""+pos+"\"","demandé n'existe pas pour ce texte, la liste des POS disponible est : ")
                    print(self.dictPOS.keys(),"\n")
        
            if flag:
                return
            else:
                df=pd.DataFrame.from_dict(self.pos_stats, orient="index")
                print(df.transpose())

            return self.pos_stats

    def text_compare(self, text_2="FileName"):
        """Cette fonction sert à comparer le sens de deux textes (sorte de comparaison de similarité, basée sur la vectorisation du texte par le module Spacy).
        Retourne la valeur obtenue en %tage de similarité. (float)"""

        #ouverture du second fichier
        text2=Text(text_2)
        text2.read()
       
        #chargement des docs pour pouvoir appliquer la fonction similarity
        doc1=self.nlp(self.content)
        doc2=text2.nlp(text2.content)

        similariteSemantique=doc1.similarity(doc2)
        print("les deux textes sont similaires à :",similariteSemantique,"%")

        return similariteSemantique

    def export_excel(self, fileName="results.xlsx", directory=os.path.join(BASE_DIR,"output_files")):
        """Exporte tous les dictionnaires, listes et strings concernant le texte stockés en variables d'objet dans un fichier excel."""

        #ouverture du writer pandas pour écrire un fichier excel (pour avoir plusieurs pages)
        with pd.ExcelWriter(directory+'\\'+fileName, mode="w") as writer:

            #dictionnaire qui sert à stocker les informations str et path
            misc_dict={}

            #on parcourt toutes les variables de l'objet
            for key in vars(self):

                #si c'est une liste on le traite comme pandas traite les listes
                if isinstance(vars(self)[key], list):
                    df=pd.DataFrame(vars(self)[key])
                    df.to_excel(writer, sheet_name=key)

                #si c'est un dictionnaire on fait pareil
                elif isinstance(vars(self)[key], dict):
                    df=pd.DataFrame.from_dict(vars(self)[key], orient="index")
                    df=df.transpose()
                    df.to_excel(writer, sheet_name=key)

                #si c'est une variable string ou path, on le stock dans le dictionnaire misc_dict
                elif isinstance(vars(self)[key], str) or isinstance(vars(self)[key], pathlib.PurePath):
                    misc_dict[key]=vars(self)[key]

            #à la fin du parcours on écrit dans une nouvelle page excel le contenu de misc_dict
            df=pd.DataFrame.from_dict(misc_dict, orient="index")
            df=df.transpose()
            df.to_excel(writer, sheet_name="misc")

test=Text("text.txt")
test.read()
test.tokenize()
test.pos()
test.pos_request("NOUN","ADJ")
test.text_compare("a.txt")
test.export_excel()

