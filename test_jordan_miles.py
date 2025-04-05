import requests

SYSTEME_IO_API_KEY = "ta5wxut559hmjoklyo5trsyuivpjxnzuzm7sdxacoegtewekifxdtpl289ko8nfi"
SYSTEME_IO_URL = "https://api.systeme.io/api/contacts"

data = {
    "email": "jordan.miles@gmail.com",
    "first_name": "Jordan Miles",
    "tags": ["Puravive"]
}

headers = {
    "X-API-Key": SYSTEME_IO_API_KEY,
    "Content-Type": "application/json"
}

response = requests.post(SYSTEME_IO_URL, json=data, headers=headers)

print("Requête envoyée :", data)
print("Statut de la réponse :", response.status_code)
print("Contenu de la réponse :", response.text)

