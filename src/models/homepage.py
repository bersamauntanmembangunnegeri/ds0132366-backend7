from datetime import datetime
from .user import db

class HomepageSection(db.Model):
    __tablename__ = 'homepage_section'
    
    id = db.Column(db.Integer, primary_key=True)
    section_type = db.Column(db.String(50), nullable=False)  # 'hero', 'product_categories', 'info_block', 'custom'
    title = db.Column(db.String(200), nullable=True)
    content = db.Column(db.Text, nullable=True)
    order_index = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)
    css_classes = db.Column(db.String(500), nullable=True)  # Custom CSS classes
    background_color = db.Column(db.String(20), nullable=True)  # Hex color code
    text_color = db.Column(db.String(20), nullable=True)  # Hex color code
    image_url = db.Column(db.String(500), nullable=True)
    button_text = db.Column(db.String(100), nullable=True)
    button_url = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'section_type': self.section_type,
            'title': self.title,
            'content': self.content,
            'order_index': self.order_index,
            'is_active': self.is_active,
            'css_classes': self.css_classes,
            'background_color': self.background_color,
            'text_color': self.text_color,
            'image_url': self.image_url,
            'button_text': self.button_text,
            'button_url': self.button_url,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

class SiteSettings(db.Model):
    __tablename__ = 'site_settings'
    
    id = db.Column(db.Integer, primary_key=True)
    setting_key = db.Column(db.String(100), unique=True, nullable=False)
    setting_value = db.Column(db.Text, nullable=True)
    setting_type = db.Column(db.String(20), default='text')  # 'text', 'json', 'boolean', 'number'
    description = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'setting_key': self.setting_key,
            'setting_value': self.setting_value,
            'setting_type': self.setting_type,
            'description': self.description,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

