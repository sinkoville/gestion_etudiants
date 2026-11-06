
# =====================================
# SYSTEME DE GESTION DES ETUDIANTS
# =====================================

# Liste des étudiants
etudiants = []


# Fonction pour ajouter un étudiant
def ajouter_etudiant(nom, prenom, age, filiere):
    etudiant = {
        "nom": nom,
        "prenom": prenom,
        "age": age,
        "filiere": filiere
    }
    etudiants.append(etudiant)
    print("\nEtudiant ajouté avec succès !")


# Fonction pour afficher les étudiants
def afficher_etudiants():
    print("\n===== LISTE DES ETUDIANTS =====")

    if not etudiants:
        print("Aucun étudiant enregistré.")
        return

    for etudiant in etudiants:
        print(f"{etudiant['nom']} {etudiant['prenom']} - "
              f"{etudiant['age']} ans - {etudiant['filiere']}")


# Fonction de recherche
def rechercher_etudiant(recherche):
    print("\n===== RESULTAT DE LA RECHERCHE =====")

    resultats = [
        etudiant for etudiant in etudiants
        if recherche.lower() in etudiant["nom"].lower()
        or recherche.lower() in etudiant["prenom"].lower()
    ]

    if resultats:
        for etudiant in resultats:
            print(f"Nom : {etudiant['nom']}")
            print(f"Prénom : {etudiant['prenom']}")
            print(f"Âge : {etudiant['age']} ans")
            print(f"Filière : {etudiant['filiere']}")
            print("----------------------------")
    else:
        print("Aucun étudiant trouvé.")


# Programme principal
print("BIENVENUE DANS LA GESTION DES ETUDIANTS")

while True:
    print("\n1. Ajouter un étudiant")
    print("2. Afficher les étudiants")
    print("3. Rechercher un étudiant")
    print("4. Quitter")

    choix = input("\nVotre choix : ")

    if choix == "1":
        nom = input("Nom : ")
        prenom = input("Prénom : ")
        age = int(input("Age : "))
        filiere = input("Filière : ")

        ajouter_etudiant(nom, prenom, age, filiere)

    elif choix == "2":
        afficher_etudiants()

    elif choix == "3":
        recherche = input("Nom ou prénom à rechercher : ")
        rechercher_etudiant(recherche)

    elif choix == "4":
        print("Au revoir !")
        break

    else:
        print("Choix invalide. Réessayez.")
