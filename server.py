from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import hashlib
import random

app = Flask(__name__)

# Configure MySQL

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'DB_AleekkCasino'

mysql = MySQL(app)

@app.route('/')
def home():
    return jsonify({"Home" : "Flask"})

@app.route('/verify_player', methods=['POST'])
def verify_player():
    data = request.get_json()
    # user_hash = data['hash']  #TODO : hash verify
    user_Id = data['user_id']

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM players WHERE UserID=%s", (user_Id))
    player = cursor.fetchone()



if __name__ == '__main__':
    app.run(debug=True)
