import sqlite3
import requests

# Configuration de l'API Systeme.io
API_KEY = "ta5wxut559hmjoklyo5trsyuivpjxnzuzm7sdxacoegtewekifxdtpl289ko8nfi"
BASE_URL = "https://api.systeme.io/api"

# Fonction pour vérifier si un email existe dans Systeme.io
def check_systeme_contact(email):
    response = requests.get(
        f"{BASE_URL}/contacts",
        headers={"Content-Type": "application/json", "X-API-Key": API_KEY},
    )
    if response.status_code == 200:
        contacts = response.json()["items"]
        return any(contact["email"] == email for contact in contacts)
    else:
        print(f"Erreur lors de la vérification de {email} : {response.json()}")
        return False

# Fonction pour ajouter un prospect localement
def add_local_prospect(email, first_name, product):
    conn = sqlite3.connect("prospects.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT OR IGNORE INTO prospects (email, first_name, product) VALUES (?, ?, ?)",
        (email, first_name, product),
    )
    conn.commit()
    conn.close()

# Fonction pour synchroniser un prospect avec Systeme.io
def sync_to_systeme(email, first_name, product):
    response = requests.post(
        f"{BASE_URL}/contacts",
        json={
            "email": email,
            "fields": [{"slug": "first_name", "value": first_name}],
        },
        headers={"Content-Type": "application/json", "X-API-Key": API_KEY},
    )
    if response.status_code == 201:
        print(f"{email} synchronisé avec succès.")
        return True
    else:
        print(f"Erreur lors de la synchronisation de {email} : {response.json()}")
        return False

# Fonction principale
def process_prospects():
    conn = sqlite3.connect("prospects.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM prospects WHERE systeme_synced = 0")
    prospects = cursor.fetchall()

    for prospect in prospects:
        id, email, first_name, product, systeme_synced = prospect
        print(f"Traitement de {email}...")

        if check_systeme_contact(email):
            print(f"{email} existe déjà dans Systeme.io.")
            cursor.execute(
                "UPDATE prospects SET systeme_synced = 1 WHERE email = ?", (email,)
            )
        else:
            if sync_to_systeme(email, first_name, product):
                cursor.execute(
                    "UPDATE prospects SET systeme_synced = 1 WHERE email = ?", (email,)
                )
        conn.commit()

    conn.close()

# Exécution du script
if __name__ == "__main__":
    process_prospects()

