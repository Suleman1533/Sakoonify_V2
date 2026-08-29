import sqlite3
DATABASE_NAME = "sakoonify.db"

def get_connection():
    return sqlite3.connect(DATABASE_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS users(
                       id INTEGAR PRIMARY KEY AUTOINCREMENT, 
                       username TEXT NOT NULL,
                       message TEXT NOT NULL, 
                       emotion TEXT NOT NULL
                   )
                   """)
    conn.commit()
    conn.close()
    
    
def create_user(username, password_hash):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        """
        INSERT INTO users
        (username, password_hash)
        VALUES (?,?)
        """,
        (username, password_hash)
        
    )
    conn.commit()
    conn.close()
    

def get_user(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT username, password_hash
        FROM users 
        WHERE username = ?
    
        """,
        (username,)
        
    )
    user = cursor.fetchone()
    conn.close()
    return user


def save_message(username, message, emotion):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        """
        INSERT INTO messages
        (username, message, emotion)
        VALUES (?,?,?)
        """,
        (username, message, emotion)
        
    )
    conn.commit()
    conn.close()
    
    