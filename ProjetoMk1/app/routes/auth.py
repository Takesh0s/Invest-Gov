from flask import Blueprint, request, jsonify
from app.models.user import User
from app import db, bcrypt
from flask_login import login_user, logout_user, login_required, current_user
from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix='/auth')

bp = Blueprint('home', __name__)

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email já registrado'}), 400
    hashed = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user = User(username=data['username'], email=data['email'], password=hashed, role=data['role'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'Usuário registrado com sucesso'})

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        login_user(user)
        return jsonify({'message': 'Login bem-sucedido', 'user': user.username, 'role': user.role})
    return jsonify({'message': 'Credenciais inválidas'}), 401

@bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout realizado'})

@bp.route('/me', methods=['GET'])
@login_required
def get_profile():
    return jsonify({
        'username': current_user.username,
        'email': current_user.email,
        'role': current_user.role
    })