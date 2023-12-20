from project import *



if __name__ == "__main__" :

    # Menu
    while True:
        print("\nMenu:")
        print("1. Afficher la liste des présidents")
        print("2. Afficher la liste des présidents avec leurs prénoms")
        print("3. Convertir en minuscules et sauvegarder")
        print("4. Nettoyer les fichiers")
        print("5. Calculer les scores TF-IDF")
        print("6. Afficher la matrice TF-IDF")
        print("7. Afficher les mots moins importants")
        print("8. Afficher les mots avec le score TF-IDF le plus élevé")
        print("9. Afficher les mots répétés dans les discours de Chirac")
        print("0. Quitter")

        choix = input("Choisissez une option (0-9): ")

        if choix == '1':
            files_names = list_of_files(directory, "txt")
            print("Liste des présidents:", nom_president(files_names))

        elif choix == '2':
            files_names = list_of_files(directory, "txt")
            president_names = nom_president(files_names)
            print("Liste des présidents avec prénoms:")
            prenom(president_names)

        elif choix == '3':
            minuscule(dossier_entree, dossier_sortie)
            print("Fichiers convertis en minuscules et sauvegardés.")

        elif choix == '4':
            cleaned(dossier)
            print("Fichiers nettoyés et sauvegardés.")

        elif choix == '5':
            tf_scores = calcul_tf(dossier_tf)
            idf_scores = calcul_idf(dossier)
            resultat = tf_idf(tf_scores, idf_scores)
            print("Calcul des scores TF-IDF terminé.",resultat)

        elif choix == '6':
            print("Matrice TF-IDF:")
            for row in resultat:
                print(row)

        elif choix == '7':
            tf_scores = calcul_tf(dossier_tf)
            moins_importants = liste_moins_importants(resultat, tf_scores)
            print("Liste des mots moins importants:", moins_importants)

        elif choix == '8':
            mots_max_tf = mot_max_tf(tf_scores, idf_scores)
            print("Mots avec le score TF-IDF le plus élevé:", mots_max_tf)

        elif choix == '9':
            mots_rep_chirac = mots_repetes_chirac(dossier, resultat)
            print("Mots répétés dans les discours de Chirac:", mots_rep_chirac)

        elif choix == '0':
            print("Programme terminé.")
            break

        else:
            print("Option invalide. Veuillez choisir une option entre 0 et 9.")
