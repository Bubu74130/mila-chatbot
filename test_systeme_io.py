import requests

SYSTEME_IO_API_KEY = "ta5wxut559hmjoklyo5trsyuivpjxnzuzm7sdxacoegtewekifxdtpl289ko8nfi"
SYSTEME_IO_URL = "https://api.systeme.io/api/contacts"

# Données de test
data = {
    "email": "ton.email@gmail.com",  # Remplace par une adresse valide et active
    "first_name": "John Doe",
    "tags": ["Product1"]
}

headers = {
    "X-API-Key": SYSTEME_IO_API_KEY,
    "Content-Type": "application/json"
}

# Envoi de la requête
response = requests.post(SYSTEME_IO_URL, json=data, headers=headers)

# Logs pour débogage
print("Requête envoyée :", data)
print("Headers envoyés :", headers)
print("Statut de la réponse :", response.status_code)
print("Contenu de la réponse :", response.text)

