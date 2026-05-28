from app.database.connection import connection_database
import sqlite3

def boot_database():
    conect = None
    cursor = None
    
    try:
        conect = connection_database()
        cursor = conect.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS urls(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_url TEXT NOT NULL,
        created_at DEFAULT CURRENT_TIMESTAMP)
    """)  
        
        conect.commit()
    except sqlite3.DatabaseError:
        raise
    finally:
        if cursor:
            cursor.close()
        if conect:
            conect.close()

if __name__ == "__main__":
    boot_database()