from project import *
if __name__ == "__main__" :

    # Menu
    while True:
        print("\nMenu:")
        print("1. Afficher la liste des présidents")
        print("2. Afficher la liste des présidents avec leurs prénoms")
        print("3. Convertir en minuscules et sauvegarder")
        print("4. Nettoyer les fichiers")
        print("5. Calculer les scores TF")
        print("6. Calculer idf")
        print("7. Afficher  la matrice tf-idf")
        print("8. Afficher les mots avec le score TF-IDF le plus élevé")
        print("9. Afficher les mots répétés dans les discours de Chirac")
        print("0. Quitter")

        choix = input("Choisissez une option (0-17): ")

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
            dossier="cleaned"
            tf_scores = calcul_tf(dossier)
            print("Calcul des scores TF-IDF terminé.",tf_scores)

        elif choix == '6':
            print("Le dictionnaire idf est :")
            dossier = "cleaned"
            resultat_idf = calcul_idf(dossier)
            print(resultat_idf)

        elif choix == '7':
            tf_scores = calcul_tf(dossier_tf)
            resultat_idf = calcul_idf(dossier)
            resultat=tf_idf(tf_scores,resultat_idf)
            print("Liste des mots moins importants:", resultat)

        elif choix == '8':
            dossier="cleaned"
            tf_scores = calcul_tf(dossier)
            idf_scores = calcul_idf(dossier)
            mots_max_tf = mot_max_tf(tf_scores, idf_scores)
            print("Mots avec le score TF-IDF le plus élevé:", mots_max_tf)

        elif choix == '9':
            mots_rep_chirac = mots_repetes_chirac(dossier, resultat)
            print("Mots répétés dans les discours de Chirac:", mots_rep_chirac)

        elif choix == "10":
            question = input("Entrez la question: ")
            resultat_tokenisation = tokenisation(question)
            print("Liste des mots tokenisés:", resultat_tokenisation)
        elif choix == "11":
            question = input("Entrez la question: ")
            mots_commun = indentification_termes(question)
            print("Mots communs:", mots_commun)
        elif choix == "12":
            dossier="cleaned"
            tf_score=calcul_tf(dossier)
            idf_scores = calcul_idf(dossier)
            question = input("Entrez la question: ")
            resultat = calcul_tf_idf_question(question, tf_score, idf_scores)
            print("Le vecteur TF-IDF de la question est :", resultat)
        elif choix == "13":
            vecteur_a = eval(input("Entrez le vecteur A (liste): "))
            vecteur_b = eval(input("Entrez le vecteur B (liste): "))
            resultat_produit_scalaire = produit_scalaire(vecteur_a, vecteur_b)
            print("Produit scalaire des vecteurs A et B :", resultat_produit_scalaire)
        elif choix == "14":
            dossier = "cleaned"
            tf_score = calcul_tf(dossier)
            idf_scores = calcul_idf(dossier)
            tf_idf_corpus=tf_idf(tf_score,idf_scores)
            noms_fichiers= list_of_files(dossier, "txt")

            question = input("Entrez la question: ")
            nom_doc_pertinent = document_pertinent(tf_idf_corpus,calcul_tf_idf_question(question, tf_score, idf_scores),noms_fichiers)
            print("Document le plus pertinent :", nom_doc_pertinent)
        elif choix == "15":
            question = input("Entrez la question: ")
            mot_remarquable = obtenir_mot_remarquable(calcul_tf_idf_question(question, tf_score, idf_scores), question)
            print("Le mot remarquable de la question est :", mot_remarquable)
        elif choix == "16":
            question_posee = input("Entrez la question: ")
            reponse_generee = generer_reponse(question_posee)
            print(reponse_generee)
        elif choix == "17":
            print("Merci d'avoir utilisé le programme. Au revoir!")
            break



        else:
            print("Option invalide. Veuillez choisir une option entre 0 et 9.")
