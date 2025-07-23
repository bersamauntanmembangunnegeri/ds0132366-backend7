from flask import Blueprint, jsonify, request
from src.models.user import db
from src.models.content import MenuItem

menu_bp = Blueprint('menu', __name__)

@menu_bp.route('/admin/menu-items', methods=['GET'])
def get_menu_items():
    try:
        menu_items = MenuItem.query.all()
        return jsonify([{
            'id': item.id,
            'title': item.title,
            'url': item.url,
            'menu_type': item.menu_type,
            'order_index': item.order_index,
            'is_active': item.is_active,
            'target_blank': item.target_blank
        } for item in menu_items])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@menu_bp.route('/admin/menu-items', methods=['POST'])
def create_menu_item():
    try:
        data = request.get_json()
        menu_item = MenuItem(
            title=data.get('title'),
            url=data.get('url'),
            menu_type=data.get('menu_type', 'header'),
            order_index=data.get('order_index', 0),
            is_active=data.get('is_active', True),
            target_blank=data.get('target_blank', False)
        )
        db.session.add(menu_item)
        db.session.commit()
        
        return jsonify({
            'id': menu_item.id,
            'title': menu_item.title,
            'url': menu_item.url,
            'menu_type': menu_item.menu_type,
            'order_index': menu_item.order_index,
            'is_active': menu_item.is_active,
            'target_blank': menu_item.target_blank
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@menu_bp.route('/admin/menu-items/<int:item_id>', methods=['PUT'])
def update_menu_item(item_id):
    try:
        menu_item = MenuItem.query.get_or_404(item_id)
        data = request.get_json()
        
        menu_item.title = data.get('title', menu_item.title)
        menu_item.url = data.get('url', menu_item.url)
        menu_item.menu_type = data.get('menu_type', menu_item.menu_type)
        menu_item.order_index = data.get('order_index', menu_item.order_index)
        menu_item.is_active = data.get('is_active', menu_item.is_active)
        menu_item.target_blank = data.get('target_blank', menu_item.target_blank)
        
        db.session.commit()
        
        return jsonify({
            'id': menu_item.id,
            'title': menu_item.title,
            'url': menu_item.url,
            'menu_type': menu_item.menu_type,
            'order_index': menu_item.order_index,
            'is_active': menu_item.is_active,
            'target_blank': menu_item.target_blank
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@menu_bp.route('/admin/menu-items/<int:item_id>', methods=['DELETE'])
def delete_menu_item(item_id):
    try:
        menu_item = MenuItem.query.get_or_404(item_id)
        db.session.delete(menu_item)
        db.session.commit()
        return jsonify({'message': 'Menu item deleted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

