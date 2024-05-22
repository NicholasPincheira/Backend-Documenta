from flask import Blueprint, jsonify

user_bp = Blueprint('user_bp', __name__)

# url para probar /api/v1/users/
@user_bp.route('/', methods=['GET'])
def get_users():
    users = [
        {'id': 1, 'username': 'user1'},
        {'id': 2, 'username': 'user2'},
    ]
    return jsonify(users)

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = {'id': user_id, 'username': f'user{user_id}'}
    return jsonify(user)
