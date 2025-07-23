from datetime import datetime
from .user import db

class FeaturedProductsSection(db.Model):
    __tablename__ = 'featured_products_section'
    
    id = db.Column(db.Integer, primary_key=True)
    homepage_section_id = db.Column(db.Integer, db.ForeignKey('homepage_section.id'), nullable=False)
    product_ids = db.Column(db.Text, nullable=True)  # JSON string of product IDs
    max_products = db.Column(db.Integer, default=8)  # Maximum number of products to display
    sort_by = db.Column(db.String(50), default='id')  # 'id', 'price', 'name', 'created_at'
    sort_order = db.Column(db.String(10), default='asc')  # 'asc' or 'desc'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship
    homepage_section = db.relationship('HomepageSection', backref='featured_products_config')
    
    def to_dict(self):
        return {
            'id': self.id,
            'homepage_section_id': self.homepage_section_id,
            'product_ids': self.product_ids,
            'max_products': self.max_products,
            'sort_by': self.sort_by,
            'sort_order': self.sort_order,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

