from database import get_connection

def add_user(telegram_id, full_name, phone):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO users (telegram_id, full_name, phone)
                VALUES (%s, %s, %s)
                ON CONFLICT (telegram_id) DO NOTHING;
            """, (telegram_id, full_name, phone))
            conn.commit()
