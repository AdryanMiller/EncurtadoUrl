from app.database.connection import connection_database

def boot_database():
    conect = connection_database()
    cursor = conect.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS urls(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    original_url TEXT NOT NULL,
    created_at DATETIME)
""")  
    
    conect.commit()
    cursor.close()
    conect.close()

if __name__ == "__main__":
    boot_database()