import mysql.connector

db = mysql.connector.connect(user='avnadmin', password='AVNS_eH5lhulxL-_04Z-MH96', host='bbt-mysql-bluebigthink.f.aivencloud.com',port=22945, auth_plugin='mysql_native_password')

cur = db.cursor()

def database():
    try:
        cur.execute("CREATE DATABASE DB_AleekkCasino")
        db.commit()
        print("Database created sucessfully!!")
        
    except:
        print("error")

database()











