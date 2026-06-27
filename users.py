import sqlite3

DATABASE = "LAD-AI.db"


def signup(username, password):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=?",
        (username,)
    )

    if cursor.fetchone():
        conn.close()
        return "❌ Username already exists."

    cursor.execute(
        "INSERT INTO users(username, password) VALUES(?, ?)",
        (username, password)
    )

    conn.commit()
    conn.close()

    return "✅ Account created successfully."


def login(username, password):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    if user:
        return f"✅ Welcome, {username}!"

    return "❌ Invalid username or password."