from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
import hashlib
import random
import jwt
import datetime
from OpenSSL import SSL

context = SSL.Context(SSL.PROTOCOL_TLSv1_2)
context.use_privatekey_file('server.key')
context.use_certificate_file('server.crt')   

app = Flask(__name__)
CORS(app)
# Configure MySQL

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'DB_AleekkCasino'
app.config['SECRET_KEY'] = 'bluebigthinksecretkey' #BOT_TOKEN

mysql = MySQL(app)

def generateToken(userId):
    return jwt.encode({
        'user_id': userId,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }, app.config['SECRET_KEY'], algorithm="HS256")

def verifyExpiredToken(token):
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return False
    return True

def createHash():
    secret_seed = str(random.randint(1, 1000000))
    nonce = str(random.randint(1, 1000000))
    hash_value = hashlib.sha256((secret_seed + nonce).encode()).hexdigest()
    return secret_seed, nonce, hash_value

@app.route('/')
def home():
    return jsonify({"Home" : "Flask"})

@app.route('/price')
def price():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM tbl_cryptos')
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results)

@app.route('/balance', methods=['POST'])
def balance():
    data = request.get_json()
    # user_hash = data['hash']  #TODO : hash verify
    UserID = data['UserID']
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM tbl_users WHERE UserID=%s', (UserID,))
    results = cursor.fetchone()
    cursor.close()
    ETH = results[12]
    BNB = results[13]
    return jsonify({"ETH":ETH, "BNB":BNB})

@app.route('/bet_coinflip', methods=['POST'])
def bet_coinflip():
    data = request.get_json()
    # user_hash = data['hash']  #TODO : hash verify
    UserID = data['UserID']
    coin_type = data['coin_type']
    bet_amount = data['bet_amount']
    print("Bet Amount =================={}".format(bet_amount))

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM tbl_users WHERE UserID=%s", (UserID,))
    user = cursor.fetchone()

    balance = 0
    query = ""
    if coin_type == 0 :
        balance = user[12]
        query = "UPDATE tbl_users SET ETH_Amount="
    elif coin_type == 1 :
        balance = user[13]
        query = "UPDATE tbl_users SET BNB_Amount="
    if balance >= bet_amount :
        balance = balance - bet_amount
    cursor.execute((query + "%s WHERE UserID=%s"), (balance, UserID,))
    mysql.connection.commit()

    secret_seed, nonce, server_hash = createHash()
    token = generateToken(UserID)
    cursor.execute("INSERT INTO tbl_coinflip (user_id, server_hash, secret_seed, nonce, parent_id, straight, is_expire_token, flip_result, win, winning_rate, cashout) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (UserID, server_hash, secret_seed, nonce, -1, 1, token, "", False, 0, 0,))
    mysql.connection.commit()

    cursor.execute("SELECT * FROM tbl_users WHERE UserID=%s", (UserID,))
    user = cursor.fetchone()
    cursor.close()
        
    return jsonify({"hash":server_hash, "ETH":user[12], "BNB":user[13]})


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, ssl_context=context)
