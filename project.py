import os


def list_of_files(directory, extension):
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
    president = []
    for filename in files_names:
        filename = filename.replace('Nomination_', '')
        filename = filename.replace('.txt', '')
        for caractere in filename:
            if (caractere < 'a' or caractere > 'z') and (caractere < 'A' or caractere > 'Z'):
                filename = filename.replace(caractere, '')
    president.append(filename)


def prenom(president_names):
    president_f_name = {
        'Chirac': 'Jacques',
        'Giscard': 'Valéry',
        'Mitterrand': 'François',
        'Macron': 'Emmanuel',
        'Sarkozy': 'Nicolas'
    }
    return [name + ' ' + president_f_name[name] for name in president_names]






def minuscule(dossier_entree, dossier_sortie):
    # parcourir tout les fichiers de dossier_entree(speeches)
    for fichier in os.listdir(dossier_entree):
        # creatiion d'un fichier entree prenant les informations de fichier
        fichier_entree = os.path.join(dossier_entree,
                                      fichier)  # est une méthode en Python qui est utilisée pour joindre différents composants d'un chemin de fichier ou de répertoire de manière à ce qu'ils soient correctement concaténés join va permettre de joindre le fichier dans le dossier

        with open(fichier_entree, 'r') as file:  # ouvrir fichier_entre en l'appelant file#indentation?
            contenu = file.read()
            contenu_min = ""
            for caractere in contenu:
                if 65 <= ord(caractere) <= 90:
                    contenu_min = chr(
                        ord(caractere) + 32)  # variable contant un chaine de caractere qui contoient les valeurs
                    # minuscules
                else:
                    contenu_min = contenu_min + caractere
            fichier_sortie = os.path.join(dossier_sortie, fichier)
            with open(fichier_sortie, 'w') as file:
                file.write(contenu_min)


def cleaned(dossier):
    for fichier in os.listdir(dossier):
        # creatiion d'un fichier entree prenant les informations de fichier
        fichier_entree = os.path.join(dossier, fichier)

        with open(fichier_entree, 'r') as file:  # (sorte de boucle)reouvrant un fichier et fait ces instructions
            contenu = file.read()  # lire le fichier pour pouvoir extraire les infos
            new_content = ""  # nouveaux chaine de caractere qui contiendra le contenu du fichier sans les ponctuatuoiob

            for caractere in file:
                if caractere == "," or caractere == ";" or caractere == "." or caractere == ":" or caractere == "?" or caractere == "!":
                    new_content = new_content + ''
                # rempacer les caracteres (' saut de ligne\n -)par des espaces
                elif caractere == "\n" or caractere == "." or caractere == "'":
                    new_content = new_content + ' '

                else:  # sinon on ajoute le caractere sans les ponctuation
                    new_content += caractere
            with open(fichier_entree, 'w') as file:
                file.write(new_content)


def tf_score(dossier):
    liste_tf = []
    for fichier in os.listdir(dossier):
        # creatiion d'un fichier entree prenant les informations de fichier
        fichier_entree = os.path.join(dossier, fichier)
        with open(fichier_entree, 'r') as file:  # ouvrir fichier_entre en l'appelant file#indentation?
            contenu = file.read()
            contenu = contenu.split()  # separer les mots de la chaine de caractere en une listge
            dico = {}
            for caractere in contenu:
                if caractere not in dico:
                    dico[caractere] = 0
                else:
                    dico[caractere] += 1
            liste_tf.append(dico)
    return liste_tf

