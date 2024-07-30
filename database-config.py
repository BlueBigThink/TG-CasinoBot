import mysql.connector

from environment import DB_HOST, DB_USER, DB_PWD, DB_PORT, DB_DATABASE

db = mysql.connector.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, port=DB_PORT, database = DB_DATABASE)

cur = db.cursor()

def database():
    try:
        cur.execute("CREATE DATABASE DB_AleekkCasino")
        db.commit()
        print("Database created sucessfully!!")
        
    except:
        print("error")

database()











