import sqlite3


def save_message(user_id, message):
    conn = sqlite3.connect("sakoonify.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO messages (user_id, message) VALUES (?, ?)",
        (user_id, message)
    )

    conn.commit()
    conn.close()


def fetch_messages(user_id):
    conn = sqlite3.connect("sakoonify.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT message FROM messages WHERE user_id = ?",
        (user_id,)
    )

    messages = cursor.fetchall()

    conn.close()
    return messages