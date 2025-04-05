import sqlite3

DATABASE = "prospects.db"

def clean_duplicates():
    """Supprime les doublons en conservant la première occurrence."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM prospects
            WHERE id NOT IN (
                SELECT MIN(id)
                FROM prospects
                GROUP BY email
            )
        ''')
        conn.commit()
        print("Doublons supprimés avec succès.")

if __name__ == "__main__":
    clean_duplicates()

