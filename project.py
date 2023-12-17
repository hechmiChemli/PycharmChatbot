import os
import math



def list_of_files(directory, extension):
    # Création d'une liste pour stocker les noms de fichiers avec l'extension spécifiée
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


# Appel de la fonction
directory = "speeches"
files_names = list_of_files(directory, "txt")

# Affichage de la liste des fichiers


def nom_president(files_names):
    # Liste pour stocker les noms de présidents extraits des noms de fichiers
    president = []
    for filename in files_names:
        filename = filename.replace('Nomination_', '')
        filename = filename.replace('.txt', '')
        for caractere in filename:
            if (caractere < 'a' or caractere > 'z') and (caractere < 'A' or caractere > 'Z'):
                filename = filename.replace(caractere, '')
        president.append(filename)
    return president


# Appel de la fonction nom_president
files_names = list_of_files(directory, "txt")
nom_president(files_names)


# Ajout de cette ligne pour afficher la liste des présidents

def prenom(president_names):
    # Dictionnaire associant les noms de président à leurs prénoms respectifs
    president_f_name = {
        'Chirac': 'Jacques',
        'GiscarddEstaing': 'Valéry',
        'Mitterrand': 'François',
        'Macron': 'Emmanuel',
        'Sarkozy': 'Nicolas',
        'Hollande':'François'

    }
    # Utilisation d'une compréhension de liste pour créer une liste des prénoms complets
    for name in president_names:
        print(name + ' ' + president_f_name[name])


# Appel de la fonction prenom avec la liste des noms de présidents
p=nom_president(files_names)
president_first_names = prenom(p)



def minuscule(dossier_entree, dossier_sortie):
    # Parcourir tous les fichiers dans le dossier d'entrée (speeches)
    for fichier in os.listdir(dossier_entree):
        # Création du chemin complet pour le fichier d'entrée
        fichier_entree = os.path.join(dossier_entree, fichier)
        with open(fichier_entree, 'r') as file:
            contenu = file.read()
            contenu_min = ""
            for caractere in contenu:
                if 65 <= ord(caractere) <= 90:
                    contenu_min += chr(ord(caractere) + 32)
                else:
                    contenu_min += caractere
            # Création du chemin complet pour le fichier de sortie
            fichier_sortie = os.path.join(dossier_sortie, fichier)
            with open(fichier_sortie, 'w') as file:
                file.write(contenu_min)


# Appel de la fonction minuscule
dossier_entree = "speeches"
dossier_sortie = "cleaned"
minuscule(dossier_entree, dossier_sortie)


def cleaned(dossier):
    # Parcourir tous les fichiers dans le dossier spécifié
    for fichier in os.listdir(dossier):
        # Création du chemin complet pour le fichier d'entrée
        fichier_entree = os.path.join(dossier, fichier)
        with open(fichier_entree, 'r') as file:
            contenu = file.read()
            new_content = ""
            for caractere in contenu:
                if caractere in [',', ';', '.', ':', '?', '!','-']:
                    new_content += ''
                elif caractere in ['', '.', "'",]:
                    new_content += ' '
                else:
                    new_content += caractere
            # Réécrire le fichier avec le contenu nettoyé
            with open(fichier_entree, 'w') as file:
                file.write(new_content)


# Appel de la fonction cleaned
dossier = "cleaned"
#cleaned(dossier)


def tf_score(dossier):
    # Liste pour stocker les dictionnaires de scores TF pour chaque fichier
    liste_tf = []
    for fichier in os.listdir(dossier):
        fichier_entree = os.path.join(dossier, fichier)
        dico = {}
        with open(fichier_entree, 'r') as file:
            contenu = file.read()
            contenu = contenu.split()
            for mot in contenu:
                if mot not in dico:
                    dico[mot] = 0
                else:
                    dico[mot] += 1
            liste_tf.append(dico)
    return liste_tf


# Appel de la fonction tf_score
dossier_tf = "cleaned"  # Modification du dossier selon vos commentaires
resultat_tf = tf_score(dossier_tf)
print(resultat_tf)


def idf(dossier):
    dico = {}
    total_doc = len(os.listdir(dossier))
    for fichier in os.listdir(dossier):
        with open(os.path.join(dossier, fichier), 'r') as file:
            contenu = file.read()
            mots = set(contenu.split())
            for mot in mots:
                if mot not in dico:
                    dico[mot] = 0
                else:
                    dico[mot] += 1
    dico_idf = {}
    for mot, valeur in dico.items():
        dico_idf[mot] = math.log(total_doc / (valeur+1))
    return dico_idf


# Appel de la fonction idf
dossier_idf = "cleaned"
resultat_idf = idf(dossier_idf)
print(resultat_idf)


def tf_idf(tf,idf):
    matrice=[]
    i = 0
    for mots in idf:#parcour les mots(ligne) dans le dico,car on doit parcourir pour chaque fichier le mot du fichier donc pour chaque colonne la ligne.Le nombre de lignes de la matrice résultante doit être égal au nombre de mots uniques dans tous les
#fichiers
        matrice.append([])
        for fichier in range(len(tf)):#t le nombre de colonnes doit être égal au nombre de fichiers se trouvant dans le répertoire .Parcourir tout les fichier du mot correspondant
            if mots in tf[fichier]:#si le mot correspond au tf du fichier cest a dire si il se trouve dans le dico tf on lappend a la matrice
                matrice[i].append(tf[fichier][mots.value]*idf[mots.value])
            else:
                matrice[i].append(0.0)#les mots ne sont pas dans le premier fichier
        i += 1 #aller a la ligne suivante de la matrice donc de
    return matrice

tf_idf_score = (tf_idf(resultat_tf,resultat_idf))




def liste_moins_importants(tf_idf,tf_score):
    liste=[]
    i=0

    for ligne in tf_idf:


        compteur = 0

        for score in ligne:
            if tf_idf[ligne][score]==0.0:
                compteur+=1
        #reprensente le nombre de mots

        if compteur==len(ligne):#si la longuer de la ligne est egale au compteur du mot
            liste.append((tf_score[i].key()))#i reprensente la ligne donc le mot quon doit ajouter a la liste
        i = i + 1#reprensente le nombre de mots
    return liste
def mot_max_tf(tf,tf_idf):
    mots_max_tf = []
    for fichier_tf in tf:
        mots = list(fichier_tf.keys())
        mot_max = mots[0]  # Initialisation avec le premier mot
        score_max = tf_idf[mot_max]

        for mot in mots:
            if tf_idf[mot] > score_max:
                mot_max = mot
                score_max = tf_idf[mot]

        mots_max_tf.append((mot_max, score_max))

    return mots_max_tf
def mot_max_tf(tf_score,tf_idf):
    mots_max_tf = []

    for i,fichier_tf in enumerate(tf_score):
        somme = 0

        mot=list(fichier_tf.keys())
        mots_max=mot[0]
        score_max = tf_idf[i][0]

        for score in tf_idf[i]:
            somme=somme + score
            if somme > score_max:
                score_max = somme
                mot_max = mot[tf_idf[i].index(score)]

        mots_max_tf.append((mot_max))

    return mots_max_tf







def mots_repetes_chirac(dossier,resultat_tf_idf):
    liste_mots_non_importants = liste_moins_importants(tf_idf, tf_score(dossier))
    mots_repetes = []

    for fichier in os.listdir(dossier):
        if fichier == nom_president('Chirac'):
            fichier_entree = os.path.join(dossier, fichier)
            with open(fichier_entree, 'r') as file:
                contenu = file.read().split()  # Sépare le contenu en mots
                word_count = tf_score(fichier_entree)#prendre le tf des mots du fichier

                mot_max = max(word_count, key=word_count.get)

                if mot_max not in liste_mots_non_importants:
                    mots_repetes.append(mot_max)

    return mots_repetes

# Exemple d'utilisation
dossier = "cleaned"


resultat_tf = tf_score(dossier_tf)
resultat_idf = idf(dossier_idf)
resultat_tf_idf = tf_idf(resultat_tf, resultat_idf)
resultat_mots_repetes_chirac = mots_repetes_chirac(dossier_tf, resultat_tf_idf)
print(resultat_mots_repetes_chirac)


#####################        ###############################PARTIE II

def tokenisation(question):
    liste = []
    contenu = question.split()

    for mot in contenu:
        mot_traite = ""
        for char in mot:
            if char.isalpha() or char == "'":
                mot_traite += char.lower()

        if mot_traite:
            liste.append(mot_traite)

    return liste

# Exemple d'utilisation
question = "Quelle est votre nom aujourd'hui"
resultat_tokenisation = tokenisation(question)

print("Question originale:", question)
print("Liste des mots tokenisés:", resultat_tokenisation)


def indentification_termes(question):
    mots_questions=set(tokenisation(question))#cree un enesemble avec les mots de la questions separer
    mots_corpus=set()#initialisation dun esemble vide des mots du corpus

    for fichier in os.listdir(dossier):#parcourir les fichiers dans le corpus
        chemin_fichier=os.path.join(dossier,fichier)#rejoindre le fichier au chemin
        with open(chemin_fichier,'r') as file:
            contenu_doc=file.read()
            mots_corpus.update(tokenisation(contenu_doc))#permettre de mettre a jour la variable mot_corpus avec tout les mots du fichiers

    mots_commun=mots_questions.intersection(mots_corpus)

    return mots_commun
# Exemple d'utilisation
question = "Quelle est votre nom aujourd'hui"
dossier= "cleaned"

resultat_intersection = indentification_termes(question, dossier)

print("Question originale:", question)
print("Termes communs avec le corpus:", resultat_intersection)

#3

