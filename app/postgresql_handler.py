import psycopg2

DB_CONFIG = {
    "dbname": "my_database",
    "user": "postgres",
    "password": "Omar0303.",
    "host": "localhost",
    "port": 5432,
}

def save_to_postgresql(user_id, extracted_data):
    """Enregistre les prospects dans PostgreSQL"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        query = """
        INSERT INTO prospects (user_id, first_name, email, interest, product, offer, status, notes, source, date_collected)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (user_id) DO UPDATE SET
            first_name = EXCLUDED.first_name,
            email = EXCLUDED.email,
            interest = EXCLUDED.interest,
            product = EXCLUDED.product,
            offer = EXCLUDED.offer,
            status = EXCLUDED.status,
            notes = EXCLUDED.notes,
            source = EXCLUDED.source,
            date_collected = EXCLUDED.date_collected;
        """
        values = (
            user_id,
            extracted_data.get("first_name"),
            extracted_data.get("email"),
            extracted_data.get("interest"),
            extracted_data.get("product"),
            extracted_data.get("offer"),
            extracted_data.get("status"),
            extracted_data.get("notes"),
            extracted_data.get("source"),
            extracted_data.get("date_collected")
        )

        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()

        print(f"✅ Données enregistrées dans PostgreSQL pour {user_id}")

    except Exception as e:
        print(f"❌ Erreur PostgreSQL : {e}")


