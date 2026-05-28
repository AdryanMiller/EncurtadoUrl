from app.database.connection import connection_database

def save_url(url_long):
    #criando conexao
    conect = None
    cursor = None
    try:
        conect = connection_database()
        cursor = conect.cursor()
        #execultando sql para salvar url longa
        command_sql = 'INSERT INTO urls(original_url) VALUES (?)'
        cursor.execute(command_sql,(url_long,))
        id_gerado = cursor.lastrowid
        #commit no banco
        conect.commit()
        return id_gerado
    finally:
    #fechando cursor e conexao
        if cursor:
            cursor.close()
        if conect:
            conect.close()

def search_id(id):
    #criando conexao
    conect = None
    cursor = None
    try:
        conect = connection_database()
        cursor = conect.cursor()
        #execultando sql para salvar url longa
        command_sql = 'SELECT original_url FROM urls WHERE id = (?)'
        cursor.execute(command_sql,(id,))
        value_id = cursor.fetchone()
        if value_id is None:
            return None
        return value_id[0]
    finally:
    #fechando cursor e conexao
        if cursor:
            cursor.close()
        if conect:
            conect.close()