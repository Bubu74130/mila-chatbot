import json

JSON_FILE = "user_data.json"

def save_to_json(user_id, extracted_data):
    """Enregistre les prospects dans un fichier JSON"""
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = {}

    users[user_id] = extracted_data
    
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4, ensure_ascii=False)
    
    print(f"📂 [LOG] Données enregistrées dans {JSON_FILE} pour {user_id}")

