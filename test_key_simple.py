import openai

# Remplacez par votre clé API directement pour simplifier le test
openai.api_key = "votre_cle_api_ici"

try:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Test de la clé OpenAI",
        max_tokens=5
    )
    print("Clé valide ! Réponse obtenue :")
    print(response.choices[0].text.strip())
except openai.error.AuthenticationError:
    print("Erreur : Clé API OpenAI invalide.")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")

