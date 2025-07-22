from flask import Blueprint, request, jsonify, session
from functools import wraps
from src.models.user import db
from src.models.content import Page, MenuItem
from datetime import datetime

content_bp = Blueprint('content', __name__, url_prefix='/api')

def require_admin():
    """Decorator to require admin authentication"""
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if not session.get('admin_logged_in'):
                return jsonify({'error': 'Admin authentication required'}), 401
            return f(*args, **kwargs)
        return wrapper
    return decorator

# Public routes for pages
@content_bp.route('/pages/<slug>', methods=['GET'])
def get_page_by_slug(slug):
    page = Page.query.filter_by(slug=slug, is_published=True).first()
    if not page:
        return jsonify({'error': 'Page not found'}), 404
    return jsonify(page.to_dict())

@content_bp.route('/menu/<menu_type>', methods=['GET'])
def get_menu_items(menu_type):
    items = MenuItem.query.filter_by(
        menu_type=menu_type, 
        is_active=True
    ).order_by(MenuItem.order_index).all()
    return jsonify([item.to_dict() for item in items])

# Admin routes for content management
@content_bp.route('/admin/pages', methods=['GET'])
@require_admin()
def get_admin_pages():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    search = request.args.get('search', '')
    
    query = Page.query
    if search:
        query = query.filter(Page.title.contains(search))
    
    pages = query.order_by(Page.updated_at.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    return jsonify({
        'pages': [page.to_dict() for page in pages.items],
        'total': pages.total,
        'pages_count': pages.pages,
        'current_page': page
    })

@content_bp.route('/admin/pages', methods=['POST'])
@require_admin()
def create_page():
    data = request.get_json()
    
    try:
        # Check if slug already exists
        existing_page = Page.query.filter_by(slug=data['slug']).first()
        if existing_page:
            return jsonify({'error': 'Page with this slug already exists'}), 400
        
        page = Page(
            title=data['title'],
            slug=data['slug'],
            content=data['content'],
            meta_description=data.get('meta_description', ''),
            meta_keywords=data.get('meta_keywords', ''),
            is_published=data.get('is_published', True)
        )
        
        db.session.add(page)
        db.session.commit()
        
        return jsonify({
            'message': 'Page created successfully',
            'page': page.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@content_bp.route('/admin/pages/<int:page_id>', methods=['GET'])
@require_admin()
def get_admin_page(page_id):
    page = Page.query.get_or_404(page_id)
    return jsonify(page.to_dict())

@content_bp.route('/admin/pages/<int:page_id>', methods=['PUT'])
@require_admin()
def update_page(page_id):
    page = Page.query.get_or_404(page_id)
    data = request.get_json()
    
    try:
        # Check if slug already exists (excluding current page)
        if data.get('slug') != page.slug:
            existing_page = Page.query.filter_by(slug=data['slug']).first()
            if existing_page:
                return jsonify({'error': 'Page with this slug already exists'}), 400
        
        page.title = data.get('title', page.title)
        page.slug = data.get('slug', page.slug)
        page.content = data.get('content', page.content)
        page.meta_description = data.get('meta_description', page.meta_description)
        page.meta_keywords = data.get('meta_keywords', page.meta_keywords)
        page.is_published = data.get('is_published', page.is_published)
        page.updated_at = datetime.utcnow()
        
        db.session.commit()
        
        return jsonify({
            'message': 'Page updated successfully',
            'page': page.to_dict()
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@content_bp.route('/admin/pages/<int:page_id>', methods=['DELETE'])
@require_admin()
def delete_page(page_id):
    page = Page.query.get_or_404(page_id)
    
    try:
        db.session.delete(page)
        db.session.commit()
        return jsonify({'message': 'Page deleted successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Menu management routes
@content_bp.route('/admin/menu-items', methods=['GET'])
@require_admin()
def get_admin_menu_items():
    menu_type = request.args.get('menu_type', '')
    
    query = MenuItem.query
    if menu_type:
        query = query.filter_by(menu_type=menu_type)
    
    items = query.order_by(MenuItem.menu_type, MenuItem.order_index).all()
    return jsonify([item.to_dict() for item in items])

@content_bp.route('/admin/menu-items', methods=['POST'])
@require_admin()
def create_menu_item():
    data = request.get_json()
    
    try:
        item = MenuItem(
            title=data['title'],
            url=data['url'],
            menu_type=data['menu_type'],
            order_index=data.get('order_index', 0),
            is_active=data.get('is_active', True),
            target_blank=data.get('target_blank', False)
        )
        
        db.session.add(item)
        db.session.commit()
        
        return jsonify({
            'message': 'Menu item created successfully',
            'item': item.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@content_bp.route('/admin/menu-items/<int:item_id>', methods=['PUT'])
@require_admin()
def update_menu_item(item_id):
    item = MenuItem.query.get_or_404(item_id)
    data = request.get_json()
    
    try:
        item.title = data.get('title', item.title)
        item.url = data.get('url', item.url)
        item.menu_type = data.get('menu_type', item.menu_type)
        item.order_index = data.get('order_index', item.order_index)
        item.is_active = data.get('is_active', item.is_active)
        item.target_blank = data.get('target_blank', item.target_blank)
        
        db.session.commit()
        
        return jsonify({
            'message': 'Menu item updated successfully',
            'item': item.to_dict()
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@content_bp.route('/admin/menu-items/<int:item_id>', methods=['DELETE'])
@require_admin()
def delete_menu_item(item_id):
    item = MenuItem.query.get_or_404(item_id)
    
    try:
        db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'Menu item deleted successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

