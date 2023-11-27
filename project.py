import math
import os



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
print(files_names)


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
        'Giscard': 'Valéry',
        'Mitterrand': 'François',
        'Macron': 'Emmanuel',
        'Sarkozy': 'Nicolas'
    }
    # Utilisation d'une compréhension de liste pour créer une liste des prénoms complets
    return [name + ' ' + president_f_name[name] for name in president_names]


# Appel de la fonction prenom avec la liste des noms de présidents
president_first_names = prenom(nom_president())
print(president_first_names)


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
                if caractere in [',', ';', '.', ':', '?', '!']:
                    new_content += ''
                elif caractere in ['\n', '.', "'"]:
                    new_content += ' '
                else:
                    new_content += caractere
            # Réécrire le fichier avec le contenu nettoyé
            with open(fichier_entree, 'w') as file:
                file.write(new_content)


# Appel de la fonction cleaned
dossier = "cleaned"
cleaned(dossier)


def tf_score(dossier):
    # Liste pour stocker les dictionnaires de scores TF pour chaque fichier
    liste_tf = []
    for fichier in os.listdir(dossier):
        fichier_entree = os.path.join(dossier, fichier)
        with open(fichier_entree, 'r') as file:
            contenu = file.read()
            contenu = contenu.split()
            dico = {}
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
        dico_idf[mot] = math.log10(total_doc / (valeur + 1))
    print(dico_idf)
    return dico_idf


# Appel de la fonction idf
dossier_idf = "cleaned"
resultat_idf = idf(dossier_idf)
print(resultat_idf)


def tf_idf(dossier, filepath=None, idf=None):
    idf_score = idf(dossier)
    tf_idf = {}
    for filename in os.listdir(dossier):
        filepatn = os.path.join(directory, filename)
        with open(filepath, 'r', enconding='utf-8') as file:
            contenu = file.read()
        tf_s = tf_score(contenu)
        tf_idf[filename] = {}
        for mot, tf in tf_s.items():
            idf = idf_score.get(mot, 1)
            tfidf = tf * math.log(len(tf_idf) / idf)
            tf_idf[filename][mot] = tfidf
    return tf_idf


def least_important_words(tf_idf_scores):
    # Créer un ensemble pour stocker les mots qui ont TF-IDF = 0 dans tous les fichiers
    zero_tfidf_words = set(tf_idf_scores[tf_idf_scores.columns[0]].index)

    # Itérez sur les scores TF-IDF de chaque fichier
    for column in tf_idf_scores.columns[1:]:
        # Mettez à jour l’ensemble avec les mots dont TF-IDF = 0 dans le fichier actuel
        zero_tfidf_words &= set(tf_idf_scores[column][tf_idf_scores[column] == 0].index)

    return zero_tfidf_words


# appel de la fonction:
tf_idf_scores = tf_idf("cleaned", idf=resultat_idf)
least_important_words_list = least_important_words(tf_idf_scores)
print("Least Important Words:", least_important_words_list)


def mot_repete_Chirac(tf_scores, president_name):
    # Filtrer TF scores pour les presidents specifiques
    president_tf_scores = tf_scores[tf_scores.index.str.contains(president_name, case=False)]

    # Trouvez les mots avec le score TF le plus élevé pour la présidente spécifiée
    most_repeated_words = president_tf_scores.idxmax(axis=0)

    return most_repeated_words


# Appel de la fonction:
chirac= mot_repete_Chirac(tf_score, "Chirac")
print("Les mots les plus repetes de Chirac sont", chirac)
