from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Konfigurasi MongoDB
client = MongoClient('localhost', 27017)
db = client['MaintenanceTracker']
users_collection = db['users']
machines_collection = db['machines']
machine_data_collection = db['machine_data']

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if 'username' in data and 'password' in data and 'role' in data:
        if users_collection.find_one({'username': data['username']}):
            return jsonify({'error': 'Username already exists'}), 400
        users_collection.insert_one({
            'username': data['username'],
            'password': data['password'],
            'role': data['role']
        })
        return jsonify({'status': 'User registered successfully'}), 201
    else:
        return jsonify({'error': 'Username, password, and role are required'}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if 'username' in data and 'password' in data:
        user = users_collection.find_one({'username': data['username']})
        if user and user['password'] == data['password']:
            return jsonify({'status': 'Login successful'}), 200
        else:
            return jsonify({'error': 'Invalid username or password'}), 400
    else:
        return jsonify({'error': 'Username and password are required'}), 400

@app.route('/add_machine_data', methods=['POST'])
def add_machine_data():
    data = request.json
    machine_code = data.get('machine_code')
    if machine_code:
        machine_data_collection.insert_one(data)
        return jsonify({'status': 'Machine data added successfully'}), 201
    else:
        return jsonify({'error': 'Machine code is required'}), 400

@app.route('/machine_data', methods=['GET'])
def get_machine_data():
    machine_code = request.args.get('machine_code')
    if machine_code:
        data = list(machine_data_collection.find({'machine_code': machine_code}, {'_id': False}))
        return jsonify(data)
    else:
        return jsonify({'error': 'Machine code is required'}), 400





if __name__ == '__main__':
    app.run(debug=True)
