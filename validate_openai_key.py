import openai
import os
from dotenv import load_dotenv

# Charger la clé depuis le fichier .env
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key or not api_key.startswith("sk-"):
    print("Erreur : Clé API OpenAI invalide ou manquante.")
    exit(1)

# Valider la clé
openai.api_key = api_key
try:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Test de la clé"}]
    )
    print("Clé valide ! Réponse obtenue :")
    print(response)
except openai.error.AuthenticationError:
    print("Erreur d'authentification : Clé OpenAI invalide.")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")


