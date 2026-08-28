import sqlite3


def save_message(message, emotion):
    conn = sqlite3.connect("sakoonify.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT,
            emotion TEXT
        )
    """)

    cursor.execute(
        "INSERT INTO messages (message, emotion) VALUES (?, ?)",
        (message, emotion)
    )

    conn.commit()
    conn.close()


def fetch_messages():
    conn = sqlite3.connect("sakoonify.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM messages")

    rows = cursor.fetchall()

    conn.close()

    return rows


if __name__ == "__main__":
    save_message(
        "I am feeling really happy today",
        "joy"
    )

    messages = fetch_messages()

    for message in messages:
        print(message)