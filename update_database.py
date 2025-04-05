import sqlite3

# Nom de votre base de données SQLite
DATABASE = "prospects.db"

def update_database():
    """Met à jour la structure de la base de données en ajoutant des colonnes et des index."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    try:
        # Créer un index pour accélérer les recherches par email
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON prospects(email);")
        print("Index 'idx_email' créé avec succès.")

        # Créer un index pour accélérer les recherches par statut
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_status ON prospects(status);")
        print("Index 'idx_status' créé avec succès.")

        # Ajouter une colonne pour indiquer les corrections manuelles
        cursor.execute("ALTER TABLE prospects ADD COLUMN manually_corrected BOOLEAN DEFAULT 0;")
        print("Colonne 'manually_corrected' ajoutée avec succès.")
    
    except sqlite3.OperationalError as e:
        # Gestion des erreurs (par exemple, si les colonnes ou index existent déjà)
        print(f"Erreur SQLite : {e}")

    # Sauvegarder les changements et fermer la connexion
    conn.commit()
    conn.close()
    print("Mise à jour de la base de données terminée.")

# Appeler la fonction
if __name__ == "__main__":
    update_database()

