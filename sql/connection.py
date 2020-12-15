import sqlite3

def initDB(sql):
    connect = sqlite3.connect('database.db')
    with open(sql) as arq:
        connect.executescript(arq.read())
    connect.execute("INSERT INTO usuarios (email, senha) VALUES ('admin', 'admin')")
    print('usuario inserido')
    connect.close()

def connection():
    conn = sqlite3.connect('database.sql')
    conn.row_factory = sqlite3.Row
    return conn