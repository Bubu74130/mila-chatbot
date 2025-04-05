import requests

# URL de l'endpoint Flask
URL = "http://127.0.0.1:5000/chatbot"

# Données à envoyer
data = {
    "name": "Alice",
    "email": "alice.test@gmail.com",
    "product": "Sugar Defender"
}

# Headers pour préciser le type de contenu
headers = {
    "Content-Type": "application/json"
}

# Envoi de la requête POST
response = requests.post(URL, json=data, headers=headers)

# Affichage des résultats
print("Statut :", response.status_code)
print("Réponse :", response.text)

