
# Gestion des étudiants

def afficher_etudiant(nom, prenom, age, filiere):
    print("\n===== INFORMATIONS DE L'ETUDIANT =====")
    print(f"Nom      : {nom}")
    print(f"Prénom   : {prenom}")
    print(f"Âge      : {age} ans")
    print(f"Filière  : {filiere}")
    print("=====================================")


# Programme principal
print("Bienvenue dans le système de gestion des étudiants")

nom = input("Entrez le nom : ")
prenom = input("Entrez le prénom : ")
age = int(input("Entrez l'âge : "))
filiere = input("Entrez la filière : ")

afficher_etudiant(nom, prenom, age, filiere)

