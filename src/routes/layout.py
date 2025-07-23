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

layout_bp = Blueprint('layout', __name__)

# Specific layout component endpoints
@layout_bp.route('/admin/layout/header', methods=['GET'])
@require_admin()
def get_header_settings():
    """Get header-specific settings and sections"""
    try:
        # Get header sections
        header_sections = HomepageSection.query.filter_by(section_type='header').order_by(HomepageSection.order_index).all()
        
        # Get header-related site settings
        header_settings = SiteSettings.query.filter(
            SiteSettings.setting_key.like('header_%')
        ).all()
        
        return jsonify({
            'sections': [section.to_dict() for section in header_sections],
            'settings': [setting.to_dict() for setting in header_settings]
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@layout_bp.route('/admin/layout/header', methods=['POST'])
@require_admin()
def update_header_layout():
    """Update header layout configuration"""
    try:
        data = request.get_json()
        
        # Update or create header settings
        for key, value in data.get('settings', {}).items():
            setting = SiteSettings.query.filter_by(setting_key=f'header_{key}').first()
            if setting:
                setting.setting_value = str(value)
            else:
                setting = SiteSettings(
                    setting_key=f'header_{key}',
                    setting_value=str(value),
                    setting_type='text',
                    description=f'Header {key} setting'
                )
                db.session.add(setting)
        
        # Update header sections if provided
        if 'sections' in data:
            for section_data in data['sections']:
                if 'id' in section_data:
                    # Update existing section
                    section = HomepageSection.query.get(section_data['id'])
                    if section:
                        for key, value in section_data.items():
                            if key != 'id':
                                setattr(section, key, value)
                else:
                    # Create new header section
                    section = HomepageSection(
                        section_type='header',
                        **{k: v for k, v in section_data.items() if k != 'id'}
                    )
                    db.session.add(section)
        
        db.session.commit()
        return jsonify({'message': 'Header layout updated successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@layout_bp.route('/admin/layout/footer', methods=['GET'])
@require_admin()
def get_footer_settings():
    """Get footer-specific settings and sections"""
    try:
        # Get footer sections
        footer_sections = HomepageSection.query.filter_by(section_type='footer').order_by(HomepageSection.order_index).all()
        
        # Get footer-related site settings
        footer_settings = SiteSettings.query.filter(
            SiteSettings.setting_key.like('footer_%')
        ).all()
        
        return jsonify({
            'sections': [section.to_dict() for section in footer_sections],
            'settings': [setting.to_dict() for setting in footer_settings]
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@layout_bp.route('/admin/layout/footer', methods=['POST'])
@require_admin()
def update_footer_layout():
    """Update footer layout configuration"""
    try:
        data = request.get_json()
        
        # Update or create footer settings
        for key, value in data.get('settings', {}).items():
            setting = SiteSettings.query.filter_by(setting_key=f'footer_{key}').first()
            if setting:
                setting.setting_value = str(value)
            else:
                setting = SiteSettings(
                    setting_key=f'footer_{key}',
                    setting_value=str(value),
                    setting_type='text',
                    description=f'Footer {key} setting'
                )
                db.session.add(setting)
        
        # Update footer sections if provided
        if 'sections' in data:
            for section_data in data['sections']:
                if 'id' in section_data:
                    # Update existing section
                    section = HomepageSection.query.get(section_data['id'])
                    if section:
                        for key, value in section_data.items():
                            if key != 'id':
                                setattr(section, key, value)
                else:
                    # Create new footer section
                    section = HomepageSection(
                        section_type='footer',
                        **{k: v for k, v in section_data.items() if k != 'id'}
                    )
                    db.session.add(section)
        
        db.session.commit()
        return jsonify({'message': 'Footer layout updated successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@layout_bp.route('/admin/layout/main-content', methods=['GET'])
@require_admin()
def get_main_content_settings():
    """Get main content layout settings"""
    try:
        # Get main content sections (excluding header and footer)
        main_sections = HomepageSection.query.filter(
            ~HomepageSection.section_type.in_(['header', 'footer'])
        ).order_by(HomepageSection.order_index).all()
        
        # Get main content-related site settings
        main_settings = SiteSettings.query.filter(
            SiteSettings.setting_key.like('main_%')
        ).all()
        
        return jsonify({
            'sections': [section.to_dict() for section in main_sections],
            'settings': [setting.to_dict() for setting in main_settings]
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@layout_bp.route('/admin/layout/main-content', methods=['POST'])
@require_admin()
def update_main_content_layout():
    """Update main content layout configuration"""
    try:
        data = request.get_json()
        
        # Update or create main content settings
        for key, value in data.get('settings', {}).items():
            setting = SiteSettings.query.filter_by(setting_key=f'main_{key}').first()
            if setting:
                setting.setting_value = str(value)
            else:
                setting = SiteSettings(
                    setting_key=f'main_{key}',
                    setting_value=str(value),
                    setting_type='text',
                    description=f'Main content {key} setting'
                )
                db.session.add(setting)
        
        db.session.commit()
        return jsonify({'message': 'Main content layout updated successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@layout_bp.route('/admin/layout/preview', methods=['GET'])
@require_admin()
def get_layout_preview():
    """Get complete layout preview data"""
    try:
        # Get all sections organized by type
        all_sections = HomepageSection.query.filter_by(is_active=True).order_by(HomepageSection.order_index).all()
        
        layout_data = {
            'header': [s.to_dict() for s in all_sections if s.section_type == 'header'],
            'main': [s.to_dict() for s in all_sections if s.section_type not in ['header', 'footer']],
            'footer': [s.to_dict() for s in all_sections if s.section_type == 'footer']
        }
        
        # Get all site settings
        all_settings = SiteSettings.query.all()
        settings_dict = {}
        for setting in all_settings:
            settings_dict[setting.setting_key] = setting.setting_value
        
        return jsonify({
            'layout': layout_data,
            'settings': settings_dict
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

