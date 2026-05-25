from app.database.connection import connection_database

def save_url(url_long, created_at):
    #criando conexao
    conect = connection_database()
    cursor = conect.cursor()
    #execultando sql para salvar url longa
    command_sql = 'INSERT INTO urls(original_url, created_at) VALUES (?,?)'
    cursor.execute(command_sql,(url_long, created_at))
    id_gerado = cursor.lastrowid
    #commit no banco
    conect.commit()
    #fechando cursor e conexao
    cursor.close()
    conect.close()
    return id_gerado

def search_id(id):
    #criando conexao
    conect = connection_database()
    cursor = conect.cursor()
    #execultando sql para salvar url longa
    command_sql = 'SELECT original_url FROM urls WHERE id = (?)'
    cursor.execute(command_sql,(id,))
    value_id = cursor.fetchone()
    #fechando cursor e conexao
    cursor.close()
    conect.close()
    return value_id[0]