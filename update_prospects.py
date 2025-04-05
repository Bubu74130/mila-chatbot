import sqlite3

DATABASE = "prospects.db"

def fetch_all_emails():
    """Récupère tous les emails valides disponibles dans la base de données."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT email FROM prospects WHERE email LIKE '%@%'")
        return [row[0] for row in cursor.fetchall()]

def update_prospect(email):
    """Met à jour un prospect en le marquant comme corrigé manuellement."""
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()

            # Vérification si l'email existe dans la base
            cursor.execute("SELECT * FROM prospects WHERE email = ?", (email,))
            prospect = cursor.fetchone()

            if not prospect:
                print(f"Aucun prospect trouvé avec l'email '{email}'.")
                return False

            # Mise à jour du prospect
            cursor.execute("UPDATE prospects SET manually_corrected = 1 WHERE email = ?", (email,))
            conn.commit()
            print(f"Le prospect avec l'email '{email}' a été mis à jour avec succès :")
            print(prospect)
            return True
    except sqlite3.Error as e:
        print(f"Erreur SQLite : {e}")
        return False

import re

def main():
    print("\n=== Mise à jour d'un prospect ===")

    # Liste des emails disponibles
    emails = fetch_all_emails()
    if not emails:
        print("Aucun prospect disponible dans la base de données.")
        return

    print("\nEmails valides disponibles dans la base :")
    for email in emails:
        print(f"- {email}")

    try:
        # Demander l'email à mettre à jour
        email_to_update = input("\nEntrez l'email du prospect à mettre à jour : ").strip()

        # Validation stricte de l'email
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email_to_update):
            print(f"L'email '{email_to_update}' n'est pas valide. Veuillez saisir un email valide.")
            return

        # Mise à jour
        if update_prospect(email_to_update):
            print("Mise à jour réussie.")
        else:
            print("La mise à jour a échoué.")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

if __name__ == "__main__":
    main()

