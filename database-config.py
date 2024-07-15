import mysql.connector

db = mysql.connector.connect(host = "bbt-mysql-bluebigthink.e.aivencloud.com", user = "avnadmin", passwd = "AVNS_Uio0Wd1KKJsWVMVn9G2", port=22945, database = "DB_AleekkCasino")

cur = db.cursor()

def database():
    try:
        cur.execute("CREATE DATABASE DB_AleekkCasino")
        db.commit()
        print("Database created sucessfully!!")
        
    except:
        print("error")

database()











