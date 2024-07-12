from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
import hashlib
import random

app = Flask(__name__)
CORS(app)
# Configure MySQL

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'DB_AleekkCasino'

mysql = MySQL(app)

secret_seed = str(random.randint(1, 1000000))
nonce = str(random.randint(1, 1000000))
hash_value = hashlib.sha256((secret_seed + nonce).encode()).hexdigest()

@app.route('/')
def home():
    return jsonify({"Home" : "Flask"})

@app.route('/price')
def price():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM tbl_cryptos')
    results = cursor.fetchall()
    cursor.close()
    print(results)
    return jsonify(results)

@app.route('/balance', methods=['POST'])
def balance():
    data = request.get_json()
    # user_hash = data['hash']  #TODO : hash verify
    UserID = data['UserID']
    print(UserID)
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM tbl_users WHERE UserID=%s', (UserID,))
    results = cursor.fetchone()
    cursor.close()
    print(results)
    ETH = results[12]
    BNB = results[13]
    return jsonify({"ETH":ETH, "BNB":BNB})

@app.route('/get_hash', methods=['POST'])
def verify_player():
    data = request.get_json()
    # user_hash = data['hash']  #TODO : hash verify
    UserID = data['UserID']
    bet_amount = data['bet_amount']

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM players WHERE UserID=%s", (user_Id))
    player = cursor.fetchone()
    print(player)
    return jsonify({"server_hash" : "55"})


if __name__ == '__main__':
    app.run(debug=True)
