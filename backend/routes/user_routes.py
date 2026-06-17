from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from models.user_model import find_user, create_user

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message": "Email and password are required."}), 400

    existing_user = find_user(email)
    if existing_user:
        return jsonify({"message": "Email already registered."}), 409

    hashed_password = generate_password_hash(password)
    try:
        create_user({"email": email, "password": hashed_password})
        return jsonify({"message": "User registered successfully!"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 400

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message": "Email and password are required."}), 400

    user = find_user(email)
    if user and check_password_hash(user.get('password'), password):
        return jsonify({"message": "Login successful!"})

    return jsonify({"message": "Invalid credentials"}), 401