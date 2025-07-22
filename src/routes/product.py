from flask import Blueprint, request, jsonify
from src.models.product import db, Product, Category, Order
import json
import random
import string

product_bp = Blueprint('product', __name__)

# Category routes
@product_bp.route('/categories', methods=['GET'])
def get_categories():
    """Get all categories"""
    categories = Category.query.all()
    return jsonify([category.to_dict() for category in categories])

@product_bp.route('/categories', methods=['POST'])
def create_category():
    """Create a new category"""
    data = request.get_json()
    
    if not data or 'name' not in data:
        return jsonify({'error': 'Category name is required'}), 400
    
    # Check if category already exists
    existing_category = Category.query.filter_by(name=data['name']).first()
    if existing_category:
        return jsonify({'error': 'Category already exists'}), 400
    
    category = Category(
        name=data['name'],
        description=data.get('description', '')
    )
    
    try:
        db.session.add(category)
        db.session.commit()
        return jsonify(category.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Product routes
@product_bp.route('/products', methods=['GET'])
def get_products():
    """Get all products with optional category filter"""
    category_id = request.args.get('category_id')
    
    query = Product.query
    if category_id:
        query = query.filter_by(category_id=category_id)
    
    products = query.all()
    return jsonify([product.to_dict() for product in products])

@product_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Get a specific product"""
    product = Product.query.get_or_404(product_id)
    return jsonify(product.to_dict())

@product_bp.route('/products', methods=['POST'])
def create_product():
    """Create a new product"""
    data = request.get_json()
    
    required_fields = ['name', 'price', 'category_id']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'{field} is required'}), 400
    
    # Check if category exists
    category = Category.query.get(data['category_id'])
    if not category:
        return jsonify({'error': 'Category not found'}), 404
    
    product = Product(
        name=data['name'],
        description=data.get('description', ''),
        price=float(data['price']),
        stock=int(data.get('stock', 0)),
        image_url=data.get('image_url', ''),
        category_id=data['category_id'],
        account_details=json.dumps(data.get('account_details', {})) if data.get('account_details') else None
    )
    
    try:
        db.session.add(product)
        db.session.commit()
        return jsonify(product.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@product_bp.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update a product"""
    product = Product.query.get_or_404(product_id)
    data = request.get_json()
    
    if 'name' in data:
        product.name = data['name']
    if 'description' in data:
        product.description = data['description']
    if 'price' in data:
        product.price = float(data['price'])
    if 'stock' in data:
        product.stock = int(data['stock'])
    if 'image_url' in data:
        product.image_url = data['image_url']
    if 'category_id' in data:
        # Check if category exists
        category = Category.query.get(data['category_id'])
        if not category:
            return jsonify({'error': 'Category not found'}), 404
        product.category_id = data['category_id']
    if 'account_details' in data:
        product.account_details = json.dumps(data['account_details'])
    
    try:
        db.session.commit()
        return jsonify(product.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@product_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product"""
    product = Product.query.get_or_404(product_id)
    
    try:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

def generate_account_credentials(quantity):
    """Generate fake account credentials for demo purposes"""
    accounts = []
    for i in range(quantity):
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        email = f"{username}@{random.choice(['gmail.com', 'outlook.com', 'yahoo.com'])}"
        
        accounts.append({
            'username': username,
            'password': password,
            'email': email,
            'additional_info': 'Account ready for use'
        })
    
    return accounts

# Order routes
@product_bp.route('/orders', methods=['POST'])
def create_order():
    """Create a new order (guest checkout)"""
    data = request.get_json()
    
    required_fields = ['customer_name', 'customer_email', 'product_id', 'quantity']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'{field} is required'}), 400
    
    # Check if product exists and has enough stock
    product = Product.query.get(data['product_id'])
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    quantity = int(data['quantity'])
    if product.stock < quantity:
        return jsonify({'error': 'Insufficient stock'}), 400
    
    total_price = product.price * quantity
    
    order = Order(
        customer_name=data['customer_name'],
        customer_email=data['customer_email'],
        product_id=data['product_id'],
        quantity=quantity,
        total_price=total_price,
        payment_method=data.get('payment_method', 'pending'),
        status='completed'  # Auto-complete for demo purposes
    )
    
    try:
        db.session.add(order)
        # Reduce stock
        product.stock -= quantity
        
        # Generate account credentials for the order
        if order.status == 'completed':
            account_credentials = generate_account_credentials(quantity)
            order.account_details = json.dumps(account_credentials)
        
        db.session.commit()
        return jsonify(order.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@product_bp.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """Get a specific order"""
    order = Order.query.get_or_404(order_id)
    order_dict = order.to_dict()
    
    # Include account details if order is completed
    if order.status == 'completed' and order.account_details:
        try:
            order_dict['account_credentials'] = json.loads(order.account_details)
        except:
            order_dict['account_credentials'] = []
    
    return jsonify(order_dict)

@product_bp.route('/orders', methods=['GET'])
def get_orders():
    """Get all orders (admin only)"""
    orders = Order.query.all()
    return jsonify([order.to_dict() for order in orders])

@product_bp.route('/orders/<int:order_id>/status', methods=['PUT'])
def update_order_status(order_id):
    """Update order status"""
    order = Order.query.get_or_404(order_id)
    data = request.get_json()
    
    if 'status' not in data:
        return jsonify({'error': 'Status is required'}), 400
    
    valid_statuses = ['pending', 'paid', 'completed', 'cancelled']
    if data['status'] not in valid_statuses:
        return jsonify({'error': 'Invalid status'}), 400
    
    old_status = order.status
    order.status = data['status']
    
    # Generate account credentials when order is completed
    if old_status != 'completed' and order.status == 'completed':
        account_credentials = generate_account_credentials(order.quantity)
        order.account_details = json.dumps(account_credentials)
    
    try:
        db.session.commit()
        return jsonify(order.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

