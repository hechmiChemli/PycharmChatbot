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
                matrice[i].append(tf[fichier][mots]*idf[mots])
            else:
                matrice[i].append(0.0)#les mots ne sont pas dans le premier fichier
        i += 1 #aller a la ligne suivante de la matrice donc de
    return matrice





def liste_moins_importants(tf_idf: object, tf_score: object) -> object:
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







def mots_repetes_chirac(dossier,tf_idf):
    liste_mots_non_importants = liste_moins_importants(tf_idf, tf_score)
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
dossier="cleaned"






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
dossier="cleaned"
question="Quelle est votre nom aujourd'hui"
resulat_mots_commun=indentification_termes(question)
print(resulat_mots_commun)


#3
def tf_idf_question(question, tf_score, idf_scores):
    # Tokenisation de la question
    mots_question = tokenisation(question)

    # Initialisation du vecteur TF-IDF de la question
    vecteur_tfidf_question = []

    # Calcul du score TF pour chaque mot de la question
    for mot in mots_question:
        # Fréquence du mot dans la question
        tf_score_mot = mots_question.count(mot)
        condition = False

        # Vérification de la présence du mot dans les fichiers du corpus
        for fichier_tf in tf_score:
            if mot in fichier_tf:
                condition = True
                break

        # Ajouter le score TF du mot dans chaque fichier
        if condition:
            tfidf_score = tf_score_mot * idf_scores.get(mot, 0)
        else:
            tfidf_score = 0
        vecteur_tfidf_question.append(tfidf_score)

    return vecteur_tfidf_question
dossier="cleaned"
question="Quelle est votre nom aujourd'hui"
tf_score=tf_score(dossier)
idf_scores=idf(dossier)
resultat=tf_idf_question(question, tf_score, idf_scores)
print(resultat)


#4
def produit_scalaire(vecteur_a, vecteur_b):
    return sum(a * b for a, b in zip(vecteur_a, vecteur_b))


def norme_vecteur(vecteur):
    return math.sqrt(sum(a**2 for a in vecteur))

def similarite_cosinus(vecteur_a, vecteur_b):
    produit = produit_scalaire(vecteur_a, vecteur_b)
    norme_a = norme_vecteur(vecteur_a)
    norme_b = norme_vecteur(vecteur_b)

    if norme_a == 0 or norme_b == 0:
        return 0  # Éviter une division par zéro

    return produit / (norme_a * norme_b)
#5
def document_pertinent(tf_idf_corpus, vecteur_tfidf_question, noms_fichiers):
    nom_document_pertinent = None
    similarite_max = -1  # Initialisation avec une valeur minimale car le cos est entre -1 et 1

    for i, vecteur_tfidf_corpus in enumerate(tf_idf_corpus):#La boucle for i, vecteur_tfidf_corpus in enumerate(tf_idf_corpus) parcourt chaque vecteur du corpus, où i est l'indice du vecteur dans la liste tf_idf_corpus.
        # On calcule la similarité de cosinus pour chaque mot
        sim = similarite_cosinus(vecteur_tfidf_question, vecteur_tfidf_corpus)#calculer la similarité entre les vecteurs tf_idf de la question et vecteur tf_idf du corpus
#La similarité de cosinus mesure l'angle entre deux vecteurs dans un espace vectoriel. Plus l'angle est petit, plus la similarité de cosinus est élevée, ce qui indique une plus grande similarité entre les deux vecteurs.
        # On garde le nom du document ayant la plus grande similarité
        #chercher la similarité maximum
        if sim > similarite_max:
            similarite_max = sim
            nom_document_pertinent = noms_fichiers[i]#chercher le document le plus pertinent .i représente l'indice du vecteur dans la liste des noms des fichiers (noms_fichiers).Ainsi ,noms_fichiers[i] récupère le nom du fichier associé au vecteur du corpus actuellement traité

    return nom_document_pertinent
#6
#Dans le vecteur TF-IDF de la question, repérer le mot ayant le score TF-IDF le plus élevé et le retourner.
#essayons de trouver le vocabulaire de tf_idf_questions,cest a dire la liste
def obtenir_vocabulaire_mot(tf_idf_question, mots_question):
    # Créer un dictionnaire pour stocker le vocabulaire de la question avec les scores TF-IDF
    vocabulaire = {}

    # Parcourir chaque mot dans la question et associer le score TF-IDF
    if len(mots_question)==len(tf_idf_question):#il faut sassurer que la longueur de mots_question correspond à la longueur de tf_idf_question
        for i, mot in enumerate(mots_question):
            vocabulaire[mot] = tf_idf_question[i]#chaque mot de vocabulaire contiendra son tf_idf_questions

    return vocabulaire
# Exemple d'utilisation
question = "Votre question ici"
tf_idf_question = tf_idf_question(question, tf_score, idf_scores)
mots_question = tokenisation(question)

vocabulaire_question = obtenir_vocabulaire_mot(tf_idf_question, mots_question)
print(vocabulaire_question)

def obtenir_mot_remarquable(tf_idf_question):
    # Obtenez le vocabulaire de la question
    vocabulaire =obtenir_vocabulaire_mot(tf_idf_question,question)

    # Obtenez le mot ayant le score TF-IDF le plus élevé
    mot_remarquable = max(vocabulaire, key=tf_idf_question.get)

    return mot_remarquable




dossier = "cleaned"
tf_scores = tf_score(dossier)
idf_scores = idf(dossier)
question = "Votre question ici"
resultat = tf_idf_question(question, tf_scores, idf_scores)
mot_remarquable_question = obtenir_mot_remarquable(resultat)
print(mot_remarquable_question)

def generer_reponse(question):
    question = question.lower()  # Convertir la question en minuscules pour faciliter la comparaison

    if "comment" in question:
        reponse = "Après analyse, votre réponse ici."
    elif "pourquoi" in question:
        reponse = "Car, votre réponse ici."
    elif "peux-tu" in question:
        reponse = "Oui, bien sûr! Votre réponse ici."
    else:
        reponse = "Je ne suis pas sûr de comprendre la question. Pouvez-vous reformuler?"

    # Mise en forme de la réponse
    reponse = reponse.capitalize()  # Mettre en majuscule la première lettre
    reponse += " Merci de poser cette question."

    return reponse

# Exemple d'utilisation
question_posee = "Pourquoi le ciel est-il bleu?"
reponse_generee = generer_reponse(question_posee)
print(reponse_generee)











