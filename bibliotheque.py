import json

# Chemin du fichier JSON
FICHIER_JSON = "bibliotheque.json"


def charger_bibliotheque():
    """Charge les livres depuis le fichier JSON."""
    try:
        with open(FICHIER_JSON, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def sauvegarder_bibliotheque(bibliotheque):
    """Sauvegarde les livres dans le fichier JSON."""
    with open(FICHIER_JSON, "w") as f:
        json.dump(bibliotheque, f)


def afficher_livres(bibliotheque):
    """Affiche tous les livres de la bibliothèque."""
    if not bibliotheque:
        print("La bibliothèque est vide.")
    else:
        for livre in bibliotheque:
            statut = "Lu" if livre["Lu"] else "Non lu"
            print(
                f"ID: {livre['ID']} | Titre: {livre['Titre']} | "
                f"Auteur: {livre['Auteur']} | Année: {livre['Année']} | "
                f"Statut: {statut}"
            )


def menu_principal():
    """Menu principal pour interagir avec la bibliothèque."""
    bibliotheque = charger_bibliotheque()

    while True:
        print("\n--- Menu Principal ---")
        print("1. Afficher tous les livres")
        print("2. Quitter")
        choix = input("Choisissez une option : ")

        if choix == "1":
            afficher_livres(bibliotheque)
        elif choix == "2":
            sauvegarder_bibliotheque(bibliotheque)
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")


if __name__ == "__main__":
    menu_principal()
