import gspread
from oauth2client.service_account import ServiceAccountCredentials

# 📌 Configuration Google Sheets
CREDENTIALS_FILE = "path_to_your_google_credentials.json"  # 🔹 Remplace par ton fichier JSON de credentials
SPREADSHEET_NAME = "Nom_de_ton_Google_Sheet"  # 🔹 Remplace par le nom de ton Google Sheet

def save_to_google_sheets(user_id, extracted_data):
    """Enregistre les prospects dans Google Sheets"""
    try:
        credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ["https://spreadsheets.google.com/feeds"])
        client = gspread.authorize(credentials)
        sheet = client.open(SPREADSHEET_NAME).sheet1

        row = [
            user_id,
            extracted_data.get("first_name", ""),
            extracted_data.get("email", ""),
            extracted_data.get("interest", ""),
            extracted_data.get("product", ""),
            extracted_data.get("offer", ""),
            extracted_data.get("status", ""),
            extracted_data.get("notes", ""),
            extracted_data.get("source", ""),
            extracted_data.get("date_collected", ""),
        ]
        sheet.append_row(row)
        print(f"✅ Données envoyées à Google Sheets : {row}")

    except Exception as e:
        print(f"❌ Erreur lors de l'envoi à Google Sheets : {e}")

