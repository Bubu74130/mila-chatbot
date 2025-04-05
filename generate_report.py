import sqlite3
from prettytable import PrettyTable

# Chemin vers votre base de données
DATABASE = "prospects.db"

def generate_report():
    """Génère un rapport des prospects enregistrés."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Requête SQL pour obtenir les données
    cursor.execute("SELECT name, email, product, status, error_reason FROM prospects")
    rows = cursor.fetchall()
    
    # Afficher les données dans un tableau formaté
    table = PrettyTable(["Nom", "Email", "Produit", "Statut", "Raison d'erreur"])
    for row in rows:
        table.add_row(row)
    
    print("\nRapport des Prospects")
    print(table)
    
    conn.close()

if __name__ == "__main__":
    generate_report()

