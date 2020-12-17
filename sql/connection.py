import mysql.connector

def getUserLogin(email, password):
    conn = mysql.connector.connect(host="localhost", database="ftp", user="root", password="")
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM usuarios where email = '"+email+"' and senha = '"+password+"' ")
        result = cursor.fetchone()
        if result != None:
            conn.close()
            cursor.close()
            return True
        else:
            conn.close()
            cursor.close()
            return False
    else:
        print("Erro ao conectar ao banco")

def getAllUsers():
    conn = mysql.connector.connect(host="localhost", database="ftp", user="root", password="")
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("SELECT email, id FROM usuarios")
        result = cursor.fetchall()
        if result != None:
            conn.close()
            cursor.close()
            return result
        else:
            conn.close()
            cursor.close()
            return False
    else:
        print("Erro ao conectar ao banco")

def getUser(id):
    conn = mysql.connector.connect(host="localhost", database="ftp", user="root", password="")
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("SELECT email, id, senha FROM usuarios where id = "+str(id)+" ")
        result = cursor.fetchall()
        if result != None:
            conn.close()
            cursor.close()
            return result
        else:
            conn.close()
            cursor.close()
            return False
    else:
        print("Erro ao conectar ao banco")

def createUser(email, senha):
    conn = mysql.connector.connect(host="localhost", database="ftp", user="root", password="")
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (email, senha) VALUES ('"+email+"', '"+senha+"') ")
        conn.commit()
        conn.close()
        cursor.close()
        return True
    else:
        print("Erro ao conectar ao banco")

def deleteUser(id):
    conn = mysql.connector.connect(host="localhost", database="ftp", user="root", password="")
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = "+str(id)+" ")
        conn.commit()
        conn.close()
        cursor.close()
        return True
    else:
        print("Erro ao conectar ao banco")

def setUser(email, senha, id):
    conn = mysql.connector.connect(host="localhost", database="ftp", user="root", password="")
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("UPDATE usuarios SET email = '"+email+"', senha = '"+senha+"' where id = "+id+" ")
        conn.commit()
        conn.close()
        cursor.close()
        return True
    else:
        print("Erro ao conectar ao banco")
