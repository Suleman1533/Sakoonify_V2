import sqlite3
conn = sqlite3.connect("test.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY,
    user_id TEXT,
    message TEXT
)
""")

conn.commit()
