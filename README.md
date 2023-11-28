Chemli Hechmi
Lahrichi Malik
1)# Appel de la fonction list_of_files(directory, extension)
directory = "speeches"
files_names = list_of_files(directory, "txt")
2)# Appel de la fonction nom_president
files_names = list_of_files(directory, "txt")
nom_president(files_names)
3)# Appel de la fonction prenom avec la liste des noms de présidents
p=nom_president(files_names)
president_first_names = prenom(p)
4)# Appel de la fonction minuscule
dossier_entree = "speeches"
dossier_sortie = "cleaned"
minuscule(dossier_entree, dossier_sortie)
5)# Appel de la fonction cleaned
dossier = "cleaned"
#cleaned(dossier)
6)# Appel de la fonction tf_score
dossier_tf = "cleaned"  # Modification du dossier selon vos commentaires
resultat_tf = tf_score(dossier_tf)
print(resultat_tf)
7)# Appel de la fonction idf
dossier_idf = "cleaned"
resultat_idf = idf(dossier_idf)
print(resultat_idf)
8)# appel de la fonction:
tf_idf_scores= tf_idf()
least_important_words_list = least_important_words(tf_idf_scores)
#print("Least Important Words:", least_important_words_list)
