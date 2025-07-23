import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src', 'database', 'app.db')
SQL_DUMP_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src', 'database', 'seed_data.sql')

def seed_database_from_sql():
    if not os.path.exists(SQL_DUMP_PATH):
        print(f"SQL dump file not found at {SQL_DUMP_PATH}")
        return

    # Ensure the database directory exists
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    # Remove existing database file if it exists
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print(f"Removed existing database at {DB_PATH}")

    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        with open(SQL_DUMP_PATH, 'r', encoding='utf-8') as f:
            sql_script = f.read()
            cursor.executescript(sql_script)
        conn.commit()
        print("Database seeded successfully from SQL dump!")
    except sqlite3.Error as e:
        print(f"Error seeding database: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    seed_database_from_sql()