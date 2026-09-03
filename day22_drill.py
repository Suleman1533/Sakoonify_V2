from fastapi import FastAPI
import sqlite3
DATABASE_NAME = "sakoonify.db"

def get_connection():
    return sqlite3.connect("DATABASE_NAME")
def init_db():
    conn = get_connection()
    
    cursor = conn.cursor()
    cursor.execute(
        """
        
        """
        
    )
    
    
