import sqlite3

# Configuration de la base de données
DATABASE = "prospects.db"

# Fonction pour rechercher un prospect par email
def search_prospect_by_email(email):
    """
    Recherche un prospect par email.
    """
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM prospects WHERE email = ?", (email,))
            result = cursor.fetchone()
            if result:
                print("Prospect trouvé :", result)
            else:
                print(f"Aucun prospect trouvé avec l'email {email}.")
    except sqlite3.Error as e:
        print(f"Erreur SQLite : {e}")

# Fonction pour rechercher des prospects par statut
def search_prospects_by_status(status):
    """
    Recherche des prospects par statut.
    """
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM prospects WHERE status = ?", (status,))
            results = cursor.fetchall()
            if results:
                print(f"Prospects avec le statut '{status}':")
                for prospect in results:
                    print(prospect)
            else:
                print(f"Aucun prospect trouvé avec le statut '{status}'.")
    except sqlite3.Error as e:
        print(f"Erreur SQLite : {e}")

# Fonction pour marquer un prospect comme corrigé manuellement
def mark_prospect_as_corrected(email):
    """
    Marque un prospect comme corrigé manuellement.
    """
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE prospects
                SET manually_corrected = 1
                WHERE email = ?;
            """, (email,))
            conn.commit()
            print(f"Le prospect avec l'email {email} a été marqué comme corrigé manuellement.")
    except sqlite3.Error as e:
        print(f"Erreur SQLite : {e}")

# Fonction principale pour interagir avec l'utilisateur
def main():
    """
    Menu principal pour gérer les prospects.
    """
    print("Bienvenue dans la gestion des prospects.")
    while True:
        print("\nOptions :")
        print("1. Rechercher un prospect par email")
        print("2. Rechercher des prospects par statut")
        print("3. Marquer un prospect comme corrigé manuellement")
        print("4. Quitter")
        choice = input("Choisissez une option : ")
        
        if choice == "1":
            email = input("Entrez l'email à rechercher : ")
            search_prospect_by_email(email)
        elif choice == "2":
            status = input("Entrez le statut (pending/rejected/accepted) : ")
            search_prospects_by_status(status)
        elif choice == "3":
            email = input("Entrez l'email du prospect à marquer comme corrigé : ")
            mark_prospect_as_corrected(email)
        elif choice == "4":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Réessayez.")

# Exécution du script
if __name__ == "__main__":
    main()

