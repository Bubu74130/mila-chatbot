import re
from datetime import datetime

def process_conversation(user_id, user_message):
    """ Analyse le message et extrait les informations clés : prénom, email, objectif, produit, etc. """

    extracted_data = {
        "first_name": None,
        "email": None,   
        "interest": None,
        "product": None,
        "offer": None, 
        "status": None,
        "notes": None,
        "source": "Chatbot Mila",
        "date_collected": datetime.now().strftime("%Y-%m-%d")
    }
    
    # 🔹 Extraction du prénom
    name_match = re.search(r"je m'appelle ([A-Za-zÀ-ÿ-]+)", user_message, re.IGNORECASE)
    if name_match:
        extracted_data["first_name"] = name_match.group(1)
    
    # 🔹 Extraction de l'email
    email_match = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", user_message)
    if email_match:
        extracted_data["email"] = email_match.group(0)

    # 🔹 Extraction de l’objectif
    if any(keyword in user_message.lower() for keyword in ["perdre du poids", "mincir", "régime"]):
        extracted_data["interest"] = "Perte de poids"
    elif any(keyword in user_message.lower() for keyword in ["glycémie", "diabète", "sucre dans le sang"]):
        extracted_data["interest"] = "Contrôle de la glycémie"

    return extracted_data

