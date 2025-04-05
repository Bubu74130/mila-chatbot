import sqlite3
import csv

DATABASE = "prospects.db"
INPUT_FILE = "new_prospects.csv"

def init_db():
    """Initialiser la base de données si elle n'existe pas encore."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS prospects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT UNIQUE,
                product TEXT,
                status TEXT DEFAULT 'pending',
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                error_reason TEXT,
                is_completed INTEGER DEFAULT 0,
                manually_corrected BOOLEAN DEFAULT 0
            )
        ''')
        conn.commit()

def import_prospects():
    """Importer les prospects à partir d'un fichier CSV."""
    try:
        with open(INPUT_FILE, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)

            # Vérifier les colonnes attendues
            expected_columns = {"name", "email", "product", "status"}
            if not expected_columns.issubset(reader.fieldnames):
                raise ValueError(f"Colonnes manquantes. Attendu : {expected_columns}. Trouvé : {reader.fieldnames}")

            imported_count = 0
            skipped_count = 0

            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
                for row in reader:
                    try:
                        cursor.execute('''
                            INSERT INTO prospects (name, email, product, status)
                            VALUES (?, ?, ?, ?)
                        ''', (row["name"], row["email"], row["product"], row["status"]))
                        imported_count += 1
                    except sqlite3.IntegrityError as e:
                        skipped_count += 1
                        print(f"Doublon ou erreur d'intégrité pour l'email {row['email']}: {e}")

                conn.commit()

            print(f"Importation terminée : {imported_count} prospects importés, {skipped_count} doublons ignorés.")

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{INPUT_FILE}' est introuvable.")
    except ValueError as e:
        print(f"Erreur lors de l'importation : {e}")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

if __name__ == "__main__":
    init_db()
    import_prospects()

