import mysql.connector

from environment import DB_HOST, DB_USER, DB_PWD, DB_PORT, DB_DATABASE

db = mysql.connector.connect(host = DB_HOST, user = DB_USER, passwd = DB_PWD, port=DB_PORT, database = DB_DATABASE)
cur = db.cursor()

def table():
    try:
        cur.execute("CREATE TABLE tbl_users(id INT AUTO_INCREMENT Primary Key, Role INT DEFAULT(0), Hash VARCHAR(255), RealName VARCHAR(50), UserName VARCHAR(100), UserID BIGINT, Wallet VARCHAR(42), ETH_Wagered FLOAT DEFAULT(0), BNB_Wagered FLOAT DEFAULT(0), Token_Wagered FLOAT DEFAULT(0), ETH_Wins FLOAT DEFAULT(0), BNB_Wins FLOAT DEFAULT(0), Token_Wins FLOAT DEFAULT(0), ETH_Amount FLOAT DEFAULT(0), BNB_Amount FLOAT DEFAULT(0), Token_Amount FLOAT DEFAULT(0), JoinDate TIMESTAMP DEFAULT(CURRENT_TIMESTAMP), UserAllowed bool DEFAULT(TRUE), ReadyTransfer bool DEFAULT(FALSE), Deployed_ETH bool DEFAULT(FALSE), Deployed_BSC bool DEFAULT(FALSE))")
        db.commit()
        cur.execute("CREATE TABLE tbl_cryptos(id INT AUTO_INCREMENT Primary Key, Symbol VARCHAR(50), CoinId VARCHAR(50), Price FLOAT DEFAULT(0))")
        db.commit()
        cur.execute("CREATE TABLE tbl_ads(id INT AUTO_INCREMENT Primary Key, UserID BIGINT, Url TEXT, Content TEXT, Time INT DEFAULT(0), Duration INT DEFAULT(0), Expired bool DEFAULT(FALSE), StartTime TIMESTAMP DEFAULT(CURRENT_TIMESTAMP), CreatedAt TIMESTAMP DEFAULT(CURRENT_TIMESTAMP), ExpiredAt TIMESTAMP DEFAULT(CURRENT_TIMESTAMP))")
        db.commit()
        cur.execute("CREATE TABLE tbl_coinflip(id INT AUTO_INCREMENT Primary Key, user_id BIGINT, server_hash VARCHAR(255), secret_seed VARCHAR(10), nonce VARCHAR(10), parent_id INT DEFAULT(0), straight INT DEFAULT(0), is_expire_token VARCHAR(255), flip_result VARCHAR(5), win bool DEFAULT(FALSE), winning_rate FLOAT DEFAULT(0), cashout FLOAT DEFAULT(0), bet_type INT DEFAULT(0), bet_amount FLOAT DEFAULT(0), bet_time TIMESTAMP DEFAULT(CURRENT_TIMESTAMP))")
        db.commit()
        cur.execute("INSERT INTO tbl_cryptos (Symbol, CoinId, Price) VALUES ('eth', 'ethereum', 3000)")
        db.commit()
        cur.execute("INSERT INTO tbl_cryptos (Symbol, CoinId, Price) VALUES ('bnb', 'binancecoin', 500)")
        db.commit()
        print("Tables created sucessfully")
    except:
        print("Tables created failed")

table()

