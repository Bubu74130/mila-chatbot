from flask import Flask, render_template, request, jsonify
import requests
import uuid

app = Flask(__name__)

# URL de ton workflow N8N
N8N_WORKFLOW_URL = "https://mila74.app.n8n.cloud/webhook-test/mila"

# Route d'accueil pour afficher la page index.html
@app.route('/')
def home():
    return render_template('index.html')  # Assurez-vous que ce fichier est dans le dossier /templates

# Route pour gérer les messages avec le chatbot
@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    message = data.get('message')

    if not message:
        return jsonify({"error": "Message requis"}), 400

    # Récupérer l'ID utilisateur ou créer un nouvel ID unique
    user_id = request.cookies.get("mila_user_id") or str(uuid.uuid4())

    # Envoyer le message à N8N via le webhook
    response = requests.post(
        N8N_WORKFLOW_URL,
        json={
            "user_id": user_id,
            "message": message
        }
    )

    # Ajouter une gestion d'erreur si le statut n'est pas 200
    if response.status_code != 200:
        print(f"Erreur lors de l'envoi de la requête à N8N : {response.status_code} - {response.text}")
        return jsonify({"error": "Erreur avec le workflow N8N"}), 500

    # Si N8N répond avec une réponse, afficher les données brutes pour diagnostic
    print(f"Réponse brute de N8N : {response.json()}")  # Log des données reçues

    n8n_data = response.json()
    mila_reply = n8n_data.get('response', 'Désolé, je n\'ai pas compris.')
    return jsonify({"response": mila_reply}), 200

# Lancement du serveur Flask
if __name__ == '__main__':
    app.run(debug=True, port=5002)
