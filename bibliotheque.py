# bibliotheque.py
# Projet – Gestion d’une bibliothèque personnelle
# Étudiant : Mohand Lhacene Hemmiche
# Collège Boréal – Été 2025

import json
import os

# Charger la bibliothèque
def charger_bibliotheque():
    if os.path.exists("bibliotheque.json"):
        try:
            with open("bibliotheque.json", "r") as f:
                contenu = f.read()
                if contenu.strip() == "":
                    return []
                return json.loads(contenu)
        except json.JSONDecodeError:
            return []
    return []

# Sauvegarder la bibliothèque
def sauvegarder_bibliotheque(bibliotheque):
    with open("bibliotheque.json", "w") as f:
        json.dump(bibliotheque, f, indent=4)

# Afficher les livres
def afficher_livres(bibliotheque):
    if not bibliotheque:
        print("📂 Aucun livre dans la bibliothèque.")
        return

    for livre in bibliotheque:
        lu = "✅ Lu" if livre["Lu"] else "❌ Non lu"
        print(f'{livre["ID"]}: {livre["Titre"]} - {livre["Auteur"]} ({livre["Année"]}) | {lu} | Note: {livre["Note"]}')

# Ajouter un livre
def ajouter_livre(bibliotheque):
    titre = input("Entrez le titre du livre : ")
    auteur = input("Entrez l'auteur du livre : ")
    annee = input("Entrez l'année de publication : ")
    nouvel_id = max([livre["ID"] for livre in bibliotheque], default=0) + 1

    livre = {
        "ID": nouvel_id,
        "Titre": titre,
        "Auteur": auteur,
        "Année": annee,
        "Lu": False,
        "Note": None
    }

    bibliotheque.append(livre)
    print("✅ Livre ajouté avec succès !")

# Supprimer un livre
def supprimer_livre(bibliotheque):
    try:
        id_supprimer = int(input("Entrez l'ID du livre à supprimer : "))
        for livre in bibliotheque:
            if livre["ID"] == id_supprimer:
                bibliotheque.remove(livre)
                print("🗑️ Livre supprimé avec succès.")
                return
        print("❌ Aucun livre trouvé avec cet ID.")
    except ValueError:
        print("❌ Veuillez entrer un ID valide.")

# Rechercher un livre
def rechercher_livre(bibliotheque):
    mot_cle = input("Entrez un mot-clé pour chercher dans le titre ou l'auteur : ").lower()
    resultats = [livre for livre in bibliotheque if mot_cle in livre["Titre"].lower() or mot_cle in livre["Auteur"].lower()]

    if not resultats:
        print("🔍 Aucun résultat trouvé.")
        return

    for livre in resultats:
        lu = "✅ Lu" if livre["Lu"] else "❌ Non lu"
        print(f'{livre["ID"]}: {livre["Titre"]} - {livre["Auteur"]} ({livre["Année"]}) | {lu} | Note: {livre["Note"]}')

# Marquer un livre comme lu et ajouter une note
def marquer_comme_lu(bibliotheque):
    try:
        id_livre = int(input("Entrez l'ID du livre à marquer comme lu : "))
        for livre in bibliotheque:
            if livre["ID"] == id_livre:
                livre["Lu"] = True
                note = input("Entrez une note sur 10 (ou laissez vide) : ")
                if note.isdigit():
                    livre["Note"] = int(note)
                print("📖 Livre marqué comme lu.")
                return
        print("❌ Livre non trouvé.")
    except ValueError:
        print("❌ ID invalide.")

# Trier les livres
def trier_livres(bibliotheque):
    if not bibliotheque:
        print("📂 La bibliothèque est vide.")
        return

    print("\n📊 Choisissez un critère de tri :")
    print("1. Par année")
    print("2. Par auteur")
    print("3. Par note")

    choix = input("Votre choix : ")

    if choix == "1":
        livres_tries = sorted(bibliotheque, key=lambda x: x["Année"])
    elif choix == "2":
        livres_tries = sorted(bibliotheque, key=lambda x: x["Auteur"].lower())
    elif choix == "3":
        livres_tries = sorted(bibliotheque, key=lambda x: (x["Note"] is None, x["Note"]))
    else:
        print("❌ Choix invalide.")
        return

    print("\n📚 Livres triés :")
    for livre in livres_tries:
        lu = "✅ Lu" if livre["Lu"] else "❌ Non lu"
        print(f'{livre["ID"]}: {livre["Titre"]} - {livre["Auteur"]} ({livre["Année"]}) | {lu} | Note: {livre["Note"]}')

# Menu principal
def menu_principal():
    bibliotheque = charger_bibliotheque()

    while True:
        print("\nBienvenue dans la bibliothèque personnelle de MOHAND LHACENE HAMMICHE\n")
        print("1. Afficher tous les livres")
        print("2. Ajouter un livre")
        print("3. Supprimer un livre")
        print("4. Rechercher un livre")
        print("5. Marquer un livre comme lu")
        print("6. Trier les livres")
        print("7. Quitter")

        choix = input("Choisissez une option : ")

        if choix == "1":
            afficher_livres(bibliotheque)
        elif choix == "2":
            ajouter_livre(bibliotheque)
        elif choix == "3":
            supprimer_livre(bibliotheque)
        elif choix == "4":
            rechercher_livre(bibliotheque)
        elif choix == "5":
            marquer_comme_lu(bibliotheque)
        elif choix == "6":
            trier_livres(bibliotheque)
        elif choix == "7":
            sauvegarder_bibliotheque(bibliotheque)
            print("📦 Bibliothèque sauvegardée. Au revoir !")
            break
        else:
            print("❌ Option invalide. Veuillez réessayer.")

# Lancer le programme
if __name__ == "__main__":
    menu_principal()
import json

# 1. Liste globale pour stocker les livres
bibliotheque = []

# 2. Fonctions
def charger():
    global bibliotheque
    try:
        with open("bibliotheque.json", "r") as f:
            bibliotheque = json.load(f)
    except FileNotFoundError:
        bibliotheque = []

def sauvegarder():
    with open("bibliotheque.json", "w") as f:
        json.dump(bibliotheque, f)

def afficher_livres():
    if not bibliotheque:
        print("La bibliothèque est vide.")
    else:
        for i, livre in enumerate(bibliotheque, 1):
            statut = "Lu" if livre["lu"] else "Non lu"
            print(f"{i}. {livre['titre']} - {livre['auteur']} ({livre['annee']}) - {statut}")

def ajouter_livre():
    titre = input("Entrez le titre du livre : ")
    auteur = input("Entrez l'auteur du livre : ")
    annee = int(input("Entrez l'année de publication : "))
    livre = {"titre": titre, "auteur": auteur, "annee": annee, "lu": False}
    bibliotheque.append(livre)
    print("Livre ajouté avec succès !")

def supprimer_livre():
    afficher_livres()
    choix = int(input("Entrez le numéro du livre à supprimer : "))
    if 1 <= choix <= len(bibliotheque):
        livre_supprime = bibliotheque.pop(choix - 1)
        print(f"Le livre '{livre_supprime['titre']}' a été supprimé.")
    else:
        print("Numéro invalide.")

def rechercher_livre():
    recherche = input("Entrez le titre ou une partie du titre à rechercher : ").lower()
    resultats = [livre for livre in bibliotheque if recherche in livre["titre"].lower()]
    if resultats:
        for livre in resultats:
            print(f"{livre['titre']} - {livre['auteur']} ({livre['annee']})")
    else:
        print("Aucun livre trouvé.")

def marquer_comme_lu():
    afficher_livres()
    choix = int(input("Entrez le numéro du livre à marquer comme lu : "))
    if 1 <= choix <= len(bibliotheque):
        bibliotheque[choix - 1]["lu"] = True
        print(f"Le livre '{bibliotheque[choix - 1]['titre']}' est maintenant marqué comme lu.")
    else:
        print("Numéro invalide.")

def trier_livres():
    print("1. Trier par titre")
    print("2. Trier par année")
    choix = input("Choisissez le critère de tri : ")
    if choix == "1":
        bibliotheque.sort(key=lambda x: x["titre"])
        print("Livres triés par titre.")
    elif choix == "2":
        bibliotheque.sort(key=lambda x: x["annee"])
        print("Livres triés par année.")
    else:
        print("Choix invalide.")

def menu():
    print("\n1. Afficher tous les livres")
    print("2. Ajouter un livre")
    print("3. Supprimer un livre")
    print("4. Rechercher un livre")
    print("5. Marquer un livre comme lu")
    print("6. Trier les livres")
    print("7. Quitter")

# 3. Programme principal
charger()

print("Bienvenue dans la bibliothèque personnelle de MOHAND LHACENE HAMMICHE")

while True:
    menu()
    choix = input("Choisissez une option : ")
    if choix == "1":
        afficher_livres()
    elif choix == "2":
        ajouter_livre()
    elif choix == "3":
        supprimer_livre()
    elif choix == "4":
        rechercher_livre()
    elif choix == "5":
        marquer_comme_lu()
    elif choix == "6":
        trier_livres()
    elif choix == "7":
        sauvegarder()
        print("Bibliothèque sauvegardée. Au revoir !")
        break
    else:
        print("Option invalide, réessayez.")
livre = {
    "ID": 1,
    "Titre": "Nations Nègres et Culture",
    "Auteur": "Cheikh Anta Diop",
    "Année": 1954,
    "Lu": False,
    "Note": None
}
try:
    id_choisi = int(input("Entrez l'ID du livre : "))
except ValueError:
    print("Erreur : l'ID doit être un nombre.")

    
bibliotheque = [
    {"ID": 1, "Titre": "Nations Nègres et Culture", "Auteur": "Cheikh Anta Diop", "Année": 1954, "Lu": False, "Note": None},
    # autres livres...
]
