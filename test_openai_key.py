import openai
import os
from dotenv import load_dotenv

# Charger la clé API depuis le fichier .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Vérifier que la clé API est présente
if not api_key or not api_key.startswith("sk-"):
    print("Erreur : Clé API OpenAI invalide ou manquante.")
    exit()

# Configurer la clé API
openai.api_key = api_key

# Test de la clé avec une requête simple
try:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Test de la clé API"}],
        max_tokens=10
    )
    print("Clé API valide. Réponse obtenue :")
    print(response.choices[0].message['content'])
except openai.error.AuthenticationError:
    print("Erreur : Clé API invalide ou permissions incorrectes.")
except Exception as e:
    print(f"Erreur inattendue : {e}")


