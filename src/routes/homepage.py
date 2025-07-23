from flask import Blueprint, request, jsonify, session
from functools import wraps
from ..models.homepage import HomepageSection, SiteSettings
from ..models.user import db

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

homepage_bp = Blueprint('homepage', __name__)

# Public endpoints for frontend
@homepage_bp.route('/homepage-sections', methods=['GET'])
def get_homepage_sections():
    """Get all active homepage sections ordered by order_index"""
    try:
        sections = HomepageSection.query.filter_by(is_active=True).order_by(HomepageSection.order_index).all()
        return jsonify([section.to_dict() for section in sections])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@homepage_bp.route('/site-settings', methods=['GET'])
def get_site_settings():
    """Get all site settings"""
    try:
        settings = SiteSettings.query.all()
        settings_dict = {}
        for setting in settings:
            if setting.setting_type == 'json':
                import json
                try:
                    settings_dict[setting.setting_key] = json.loads(setting.setting_value)
                except:
                    settings_dict[setting.setting_key] = setting.setting_value
            elif setting.setting_type == 'boolean':
                settings_dict[setting.setting_key] = setting.setting_value.lower() == 'true'
            elif setting.setting_type == 'number':
                try:
                    settings_dict[setting.setting_key] = float(setting.setting_value)
                except:
                    settings_dict[setting.setting_key] = setting.setting_value
            else:
                settings_dict[setting.setting_key] = setting.setting_value
        
        return jsonify(settings_dict)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Admin endpoints
@homepage_bp.route('/admin/homepage-sections', methods=['GET'])
@require_admin()
def admin_get_homepage_sections():
    """Get all homepage sections for admin"""
    try:
        sections = HomepageSection.query.order_by(HomepageSection.order_index).all()
        return jsonify([section.to_dict() for section in sections])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@homepage_bp.route('/admin/homepage-sections', methods=['POST'])
@require_admin()
def admin_create_homepage_section():
    """Create a new homepage section"""
    try:
        data = request.get_json()
        
        section = HomepageSection(
            section_type=data.get('section_type'),
            title=data.get('title'),
            content=data.get('content'),
            order_index=data.get('order_index', 0),
            is_active=data.get('is_active', True),
            css_classes=data.get('css_classes'),
            background_color=data.get('background_color'),
            text_color=data.get('text_color'),
            image_url=data.get('image_url'),
            button_text=data.get('button_text'),
            button_url=data.get('button_url')
        )
        
        db.session.add(section)
        db.session.commit()
        
        return jsonify(section.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@homepage_bp.route('/admin/homepage-sections/<int:section_id>', methods=['PUT'])
@require_admin()
def admin_update_homepage_section(section_id):
    """Update a homepage section"""
    try:
        section = HomepageSection.query.get_or_404(section_id)
        data = request.get_json()
        
        section.section_type = data.get('section_type', section.section_type)
        section.title = data.get('title', section.title)
        section.content = data.get('content', section.content)
        section.order_index = data.get('order_index', section.order_index)
        section.is_active = data.get('is_active', section.is_active)
        section.css_classes = data.get('css_classes', section.css_classes)
        section.background_color = data.get('background_color', section.background_color)
        section.text_color = data.get('text_color', section.text_color)
        section.image_url = data.get('image_url', section.image_url)
        section.button_text = data.get('button_text', section.button_text)
        section.button_url = data.get('button_url', section.button_url)
        
        db.session.commit()
        
        return jsonify(section.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@homepage_bp.route('/admin/homepage-sections/<int:section_id>', methods=['DELETE'])
@require_admin()
def admin_delete_homepage_section(section_id):
    """Delete a homepage section"""
    try:
        section = HomepageSection.query.get_or_404(section_id)
        db.session.delete(section)
        db.session.commit()
        
        return jsonify({'message': 'Section deleted successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@homepage_bp.route('/admin/homepage-sections/reorder', methods=['POST'])
@require_admin()
def admin_reorder_homepage_sections():
    """Reorder homepage sections"""
    try:
        data = request.get_json()
        section_orders = data.get('sections', [])
        
        for item in section_orders:
            section = HomepageSection.query.get(item['id'])
            if section:
                section.order_index = item['order_index']
        
        db.session.commit()
        
        return jsonify({'message': 'Sections reordered successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Site Settings Admin endpoints
@homepage_bp.route('/admin/site-settings', methods=['GET'])
@require_admin()
def admin_get_site_settings():
    """Get all site settings for admin"""
    try:
        settings = SiteSettings.query.all()
        return jsonify([setting.to_dict() for setting in settings])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@homepage_bp.route('/admin/site-settings', methods=['POST'])
@require_admin()
def admin_create_site_setting():
    """Create a new site setting"""
    try:
        data = request.get_json()
        
        setting = SiteSettings(
            setting_key=data.get('setting_key'),
            setting_value=data.get('setting_value'),
            setting_type=data.get('setting_type', 'text'),
            description=data.get('description')
        )
        
        db.session.add(setting)
        db.session.commit()
        
        return jsonify(setting.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@homepage_bp.route('/admin/site-settings/<int:setting_id>', methods=['PUT'])
@require_admin()
def admin_update_site_setting(setting_id):
    """Update a site setting"""
    try:
        setting = SiteSettings.query.get_or_404(setting_id)
        data = request.get_json()
        
        setting.setting_key = data.get('setting_key', setting.setting_key)
        setting.setting_value = data.get('setting_value', setting.setting_value)
        setting.setting_type = data.get('setting_type', setting.setting_type)
        setting.description = data.get('description', setting.description)
        
        db.session.commit()
        
        return jsonify(setting.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@homepage_bp.route('/admin/site-settings/<int:setting_id>', methods=['DELETE'])
@require_admin()
def admin_delete_site_setting(setting_id):
    """Delete a site setting"""
    try:
        setting = SiteSettings.query.get_or_404(setting_id)
        db.session.delete(setting)
        db.session.commit()
        
        return jsonify({'message': 'Setting deleted successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

