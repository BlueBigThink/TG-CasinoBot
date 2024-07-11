# server.py
from flask import Flask, request, jsonify
import hashlib
import random

app = Flask(__name__)

secret_seed = str(random.randint(1, 1000000))
nonce = str(random.randint(1, 1000000))
hash_value = hashlib.sha256((secret_seed + nonce).encode()).hexdigest()

@app.route('/get_hash', methods=['GET'])
def get_hash():
    return jsonify({'hash': hash_value})

@app.route('/reveal', methods=['GET'])
def reveal():
    return jsonify({'secret_seed': secret_seed, 'nonce': nonce})

if __name__ == '__main__':
    app.run(debug=True)
