import sqlite3

# Fonction pour réinitialiser la base de données
def reset_db():
    conn = sqlite3.connect("prospects.db")
    cursor = conn.cursor()
    # Supprime la table existante si elle existe
    cursor.execute("DROP TABLE IF EXISTS prospects")
    # Recrée la table avec la colonne timestamp
    cursor.execute("""
        CREATE TABLE prospects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            product TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

# Appeler la fonction pour réinitialiser la base
if __name__ == "__main__":
    reset_db()

