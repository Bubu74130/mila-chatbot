import sqlite3
import csv

DATABASE = "prospects.db"
OUTPUT_FILE = "corrected_prospects.csv"

def export_corrected_prospects():
    """Exporte les prospects corrigés manuellement dans un fichier CSV."""
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            
            # Récupérer les prospects corrigés manuellement
            cursor.execute("""
                SELECT id, name, email, product, status, timestamp, error_reason
                FROM prospects
                WHERE manually_corrected = 1
            """)
            corrected_prospects = cursor.fetchall()
            
            if not corrected_prospects:
                print("Aucun prospect corrigé manuellement à exporter.")
                return
            
            # Écrire les données dans un fichier CSV
            with open(OUTPUT_FILE, mode='w', newline='', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file)
                
                # Écrire l'en-tête du CSV
                writer.writerow(["ID", "Name", "Email", "Product", "Status", "Timestamp", "Error Reason"])
                
                # Écrire les données
                writer.writerows(corrected_prospects)
            
            print(f"Export réussi : {len(corrected_prospects)} prospects exportés vers '{OUTPUT_FILE}'.")
    except Exception as e:
        print(f"Erreur lors de l'exportation : {e}")

if __name__ == "__main__":
    export_corrected_prospects()
