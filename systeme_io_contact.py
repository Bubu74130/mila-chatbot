import requests

API_KEY = "ta5wxut559hmjoklyo5trsyuivpjxnzuzm7sdxacoegtewekifxdtpl289ko8nfi"
BASE_URL = "https://api.systeme.io/api"

def get_contact(email):
    """Récupérer un contact par email"""
    url = f"{BASE_URL}/contacts"
    headers = {
        "X-API-Key": API_KEY,
        "accept": "application/json"
    }
    params = {"email": email}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        contacts = response.json().get("items", [])
        return contacts[0] if contacts else None
    else:
        print("Erreur lors de la récupération du contact :", response.json())
        return None

def update_contact(contact_id, updates):
    """Mettre à jour un contact existant"""
    url = f"{BASE_URL}/contacts/{contact_id}"
    headers = {
        "X-API-Key": API_KEY,
        "Content-Type": "application/merge-patch+json"
    }
    response = requests.patch(url, headers=headers, json=updates)
    if response.status_code == 200:
        print("Contact mis à jour avec succès :", response.json())
    else:
        print("Erreur lors de la mise à jour du contact :", response.json())

email = "alice.dupont@gmail.com"
contact = get_contact(email)

if contact:
    print("Contact trouvé :", contact)
    updates = {
        "fields": [
            {"slug": "first_name", "value": "Alice"}
            # Ajoutez d'autres champs uniquement s'ils existent
        ]
    }
    update_contact(contact["id"], updates)
else:
    print(f"Aucun contact trouvé pour l'email : {email}")

