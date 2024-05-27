from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash

from application.all_users.users import User

user_bp = Blueprint('user', __name__)


@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists'}), 400

    new_user = User(username=username, password=generate_password_hash(password))
    new_user.save()

    return jsonify({'message': 'User registered successfully'}), 201


@user_bp.route('/register_customer_1', methods=['POST'])
def register_customer_1():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists'}), 400

    new_user = User(username=username, password=generate_password_hash(password))
    new_user.save()

    return jsonify({'message': 'Customer 1 registered successfully'}), 201


@user_bp.route('/register_customer_1', methods=['POST'])
def register_customer_2():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists'}), 400

    new_user = User(username=username, password=generate_password_hash(password))
    new_user.save()

    return jsonify({'message': 'Customer 1 registered successfully'}), 201


@user_bp.route('/register_customer_1', methods=['POST'])
def register_customer_3():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists'}), 400

    new_user = User(username=username, password=generate_password_hash(password))
    new_user.save()

    return jsonify({'message': 'Customer 1 registered successfully'}), 201


def forgot_password():
    return None


def reset_password():
    return None


def verify_email():
    return None


def login():
    return None