import sqlite3
import os



def connection_database():
    folder = os.path.dirname(os.path.abspath(__file__))
    name_database = 'urls.db'
    path_end = os.path.join(folder,name_database)
    connection = sqlite3.connect(path_end)

    return connection

