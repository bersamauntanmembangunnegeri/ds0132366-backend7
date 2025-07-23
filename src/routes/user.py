from flask import Blueprint, jsonify, request, session
from src.models.user import User, db

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@user_bp.route('/users', methods=['POST'])
def create_user():
    
    data = request.json
    user = User(username=data['username'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    db.session.commit()
    return jsonify(user.to_dict())

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return '', 204


@user_bp.route('/auth/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        # Simple hardcoded authentication for demo
        if username == 'admin' and password == 'admin123':
            session['admin_logged_in'] = True
            return jsonify({
                'success': True,
                'message': 'Login successful',
                'user': {
                    'id': 1,
                    'username': 'admin',
                    'role': 'admin'
                }
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Invalid credentials'
            }), 401
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Login failed',
            'error': str(e)
        }), 500

@user_bp.route('/auth/status', methods=['GET'])
def auth_status():
    if session.get('admin_logged_in'):
        return jsonify({
            'authenticated': True,
            'user': {
                'id': 1,
                'username': 'admin',
                'role': 'admin'
            }
        })
    else:
        return jsonify({
            'authenticated': False
        })

@user_bp.route('/auth/logout', methods=['POST'])
def logout():
    session.pop('admin_logged_in', None)
    return jsonify({
        'success': True,
        'message': 'Logout successful'
    })

