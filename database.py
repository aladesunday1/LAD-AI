import sqlite3

DATABASE = "LAD-AI.db"

def create_database():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    # Translation History
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        english TEXT,
        language TEXT,
        translation TEXT
    )
    """)

    # Favorites
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS favorites(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        english TEXT,
        language TEXT,
        translation TEXT
    )
    """)

    conn.commit()
    conn.close()


create_database()