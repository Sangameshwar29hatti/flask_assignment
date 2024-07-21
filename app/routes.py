from flask import Blueprint, request, jsonify
from app import mongo
from bson.objectid import ObjectId

main = Blueprint('main', __name__)

@main.route('/users', methods=['GET'])
def get_all_users():
    users = mongo.db.users.find()
    data = []
    for user in users:
        data.append({
            'id': str(user['_id']),
            'name': user['name'],
            'email': user['email'],
            'password': user['password']
        })
    return jsonify(data)

@main.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = mongo.db.users.find_one({'_id': ObjectId(id)})
    if user:
        data = {
            'id': str(user['_id']),
            'name': user['name'],
            'email': user['email'],
            'password': user['password']
        }
        return jsonify(data)
    else:
        return jsonify({'error': 'User not found'}), 404

@main.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not name or not email or not password:
        return jsonify({'error': 'Missing fields'}), 400

    user_id = mongo.db.users.insert_one({
        'name': name,
        'email': email,
        'password': password
    }).inserted_id

    return jsonify({'id': str(user_id)}), 201

@main.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    updated_data = {}

    if 'name' in data:
        updated_data['name'] = data['name']
    if 'email' in data:
        updated_data['email'] = data['email']
    if 'password' in data:
        updated_data['password'] = data['password']

    result = mongo.db.users.update_one({'_id': ObjectId(id)}, {'$set': updated_data})

    if result.matched_count == 0:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({'msg': 'User updated'})

@main.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    result = mongo.db.users.delete_one({'_id': ObjectId(id)})

    if result.deleted_count == 0:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({'msg': 'User deleted'})
