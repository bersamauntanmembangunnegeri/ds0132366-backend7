from flask import Blueprint, request, jsonify, session
from src.models.user import db
from src.models.product import Product, Category, Order
from datetime import datetime
import json
import random
import string

admin_bp = Blueprint('admin', __name__, url_prefix='/api/admin')

# Simple admin authentication
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def require_admin():
    """Decorator to require admin authentication"""
    def decorator(f):
        def wrapper(*args, **kwargs):
            if not session.get('admin_logged_in'):
                return jsonify({'error': 'Admin authentication required'}), 401
            return f(*args, **kwargs)
        wrapper.__name__ = f.__name__
        return wrapper
    return decorator

# Authentication routes
@admin_bp.route('/auth/login', methods=['POST'])
def admin_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        session['admin_logged_in'] = True
        return jsonify({'message': 'Login successful', 'success': True})
    
    return jsonify({'error': 'Invalid credentials', 'success': False}), 401

@admin_bp.route('/auth/logout', methods=['POST'])
def admin_logout():
    session.pop('admin_logged_in', None)
    return jsonify({'message': 'Logout successful'})

@admin_bp.route('/auth/check', methods=['GET'])
def check_auth():
    return jsonify({'authenticated': session.get('admin_logged_in', False)})

# Product management routes
@admin_bp.route('/products', methods=['GET'])
@require_admin()
def get_products():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    search = request.args.get('search', '')
    
    query = Product.query
    if search:
        query = query.filter(Product.name.contains(search))
    
    products = query.paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    return jsonify({
        'products': [product.to_dict() for product in products.items],
        'total': products.total,
        'pages': products.pages,
        'current_page': page
    })

@admin_bp.route('/products', methods=['POST'])
@require_admin()
def create_product():
    data = request.get_json()
    
    try:
        product = Product(
            name=data['name'],
            description=data.get('description', ''),
            price=float(data['price']),
            stock=int(data.get('stock', 0)),
            category_id=int(data['category_id']),
            image_url=data.get('image_url', '')
        )
        
        db.session.add(product)
        db.session.commit()
        
        return jsonify({
            'message': 'Product created successfully',
            'product': product.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@admin_bp.route('/products/<int:product_id>', methods=['GET'])
@require_admin()
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify(product.to_dict())

@admin_bp.route('/products/<int:product_id>', methods=['PUT'])
@require_admin()
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    data = request.get_json()
    
    try:
        product.name = data.get('name', product.name)
        product.description = data.get('description', product.description)
        product.price = float(data.get('price', product.price))
        product.stock = int(data.get('stock', product.stock))
        product.category_id = int(data.get('category_id', product.category_id))
        product.image_url = data.get('image_url', product.image_url)
        product.updated_at = datetime.utcnow()
        
        db.session.commit()
        
        return jsonify({
            'message': 'Product updated successfully',
            'product': product.to_dict()
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@admin_bp.route('/products/<int:product_id>', methods=['DELETE'])
@require_admin()
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    
    try:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Category management routes
@admin_bp.route('/categories', methods=['GET'])
@require_admin()
def get_categories():
    categories = Category.query.all()
    return jsonify([category.to_dict() for category in categories])

@admin_bp.route('/categories', methods=['POST'])
@require_admin()
def create_category():
    data = request.get_json()
    
    try:
        category = Category(
            name=data['name'],
            description=data.get('description', '')
        )
        
        db.session.add(category)
        db.session.commit()
        
        return jsonify({
            'message': 'Category created successfully',
            'category': category.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@admin_bp.route('/categories/<int:category_id>', methods=['PUT'])
@require_admin()
def update_category(category_id):
    category = Category.query.get_or_404(category_id)
    data = request.get_json()
    
    try:
        category.name = data.get('name', category.name)
        category.description = data.get('description', category.description)
        
        db.session.commit()
        
        return jsonify({
            'message': 'Category updated successfully',
            'category': category.to_dict()
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@admin_bp.route('/categories/<int:category_id>', methods=['DELETE'])
@require_admin()
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    
    # Check if category has products
    if category.products:
        return jsonify({'error': 'Cannot delete category with existing products'}), 400
    
    try:
        db.session.delete(category)
        db.session.commit()
        return jsonify({'message': 'Category deleted successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Order management routes
@admin_bp.route('/orders', methods=['GET'])
@require_admin()
def get_orders():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    status = request.args.get('status', '')
    
    query = Order.query
    if status:
        query = query.filter(Order.status == status)
    
    orders = query.order_by(Order.created_at.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    return jsonify({
        'orders': [order.to_dict() for order in orders.items],
        'total': orders.total,
        'pages': orders.pages,
        'current_page': page
    })

@admin_bp.route('/orders/<int:order_id>', methods=['GET'])
@require_admin()
def get_order(order_id):
    order = Order.query.get_or_404(order_id)
    order_dict = order.to_dict()
    
    # Add account credentials if available
    if order.account_details:
        try:
            order_dict['account_credentials'] = json.loads(order.account_details)
        except:
            order_dict['account_credentials'] = []
    
    return jsonify(order_dict)

@admin_bp.route('/orders/<int:order_id>/status', methods=['PUT'])
@require_admin()
def update_order_status(order_id):
    order = Order.query.get_or_404(order_id)
    data = request.get_json()
    
    try:
        order.status = data['status']
        order.updated_at = datetime.utcnow()
        
        db.session.commit()
        
        return jsonify({
            'message': 'Order status updated successfully',
            'order': order.to_dict()
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@admin_bp.route('/orders/<int:order_id>/deliver', methods=['POST'])
@require_admin()
def deliver_accounts(order_id):
    order = Order.query.get_or_404(order_id)
    
    try:
        # Generate account credentials for the order
        credentials = []
        for i in range(order.quantity):
            username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
            email = f"{username}@{''.join(random.choices(['gmail.com', 'yahoo.com', 'hotmail.com']))}"
            
            credentials.append({
                'username': username,
                'password': password,
                'email': email,
                'additional_info': 'Account ready for use'
            })
        
        order.account_details = json.dumps(credentials)
        order.status = 'completed'
        order.updated_at = datetime.utcnow()
        
        db.session.commit()
        
        return jsonify({
            'message': 'Accounts delivered successfully',
            'credentials': credentials
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Analytics routes
@admin_bp.route('/analytics/dashboard', methods=['GET'])
@require_admin()
def get_dashboard_analytics():
    try:
        # Total products
        total_products = Product.query.count()
        
        # Total orders
        total_orders = Order.query.count()
        
        # Total revenue
        total_revenue = db.session.query(db.func.sum(Order.total_price)).scalar() or 0
        
        # Orders by status
        orders_by_status = db.session.query(
            Order.status, db.func.count(Order.id)
        ).group_by(Order.status).all()
        
        # Recent orders
        recent_orders = Order.query.order_by(Order.created_at.desc()).limit(5).all()
        
        # Low stock products
        low_stock_products = Product.query.filter(Product.stock < 10).all()
        
        return jsonify({
            'total_products': total_products,
            'total_orders': total_orders,
            'total_revenue': float(total_revenue),
            'orders_by_status': dict(orders_by_status),
            'recent_orders': [order.to_dict() for order in recent_orders],
            'low_stock_products': [product.to_dict() for product in low_stock_products]
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Payment method management routes
@admin_bp.route('/payment-methods', methods=['GET'])
@require_admin()
def get_payment_methods():
    # For now, return static payment methods
    # In a real application, this would be stored in database
    payment_methods = [
        {
            'id': 1,
            'name': 'Cryptocurrency',
            'type': 'crypto',
            'enabled': True,
            'description': 'Bitcoin, Ethereum, and other cryptocurrencies'
        },
        {
            'id': 2,
            'name': 'Credit/Debit Card',
            'type': 'card',
            'enabled': True,
            'description': 'Visa, Mastercard, American Express'
        }
    ]
    
    return jsonify(payment_methods)

@admin_bp.route('/payment-methods/<int:method_id>', methods=['PUT'])
@require_admin()
def update_payment_method(method_id):
    data = request.get_json()
    
    # In a real application, this would update the database
    # For now, just return success
    return jsonify({
        'message': 'Payment method updated successfully',
        'method_id': method_id,
        'enabled': data.get('enabled', True)
    })

