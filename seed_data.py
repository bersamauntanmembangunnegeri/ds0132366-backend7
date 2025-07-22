import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from src.main import app, db
from src.models.product import Category, Product
import json

def seed_data():
    with app.app_context():
        # Create tables
        db.create_all()
        
        # Check if data already exists
        if Category.query.first():
            print("Data already exists, skipping seed...")
            return
        
        # Create categories
        categories_data = [
            {
                'name': 'Facebook Accounts',
                'description': 'Various Facebook accounts with different specifications'
            },
            {
                'name': 'Facebook Softregs',
                'description': 'Soft registered Facebook accounts'
            },
            {
                'name': 'Facebook With friends',
                'description': 'Facebook accounts with existing friends'
            },
            {
                'name': 'Facebook Aged',
                'description': 'Aged Facebook accounts from different years'
            },
            {
                'name': 'Facebook With friends and age',
                'description': 'Aged Facebook accounts with friends'
            },
            {
                'name': 'Facebook For advertising',
                'description': 'Facebook accounts optimized for advertising'
            }
        ]
        
        categories = []
        for cat_data in categories_data:
            category = Category(
                name=cat_data['name'],
                description=cat_data['description']
            )
            db.session.add(category)
            categories.append(category)
        
        db.session.commit()
        
        # Create sample products
        products_data = [
            {
                'name': 'FB Accounts | Verified by e-mail, there is no email in the set. Male or female.',
                'description': 'The account profiles may be empty or have limited entries such as photos and other information. 2FA included. Cookies are included. Accounts are registered in United Kingdom IP.',
                'price': 0.278,
                'stock': 384,
                'category_name': 'Facebook Accounts',
                'image_url': '/static/images/facebook-account.png'
            },
            {
                'name': 'FB Accounts | Verified by email (email not included). Male or female.',
                'description': 'The account profiles may be empty or have limited entries such as photos and other information. 2FA included. Registered from USA IP.',
                'price': 0.296,
                'stock': 1679,
                'category_name': 'Facebook Accounts',
                'image_url': '/static/images/facebook-account.png'
            },
            {
                'name': 'FB Accounts | The number of subscribers is 50+. Verified by e-mail.',
                'description': 'The account profiles may be empty or have limited entries such as photos and other information. 2FA in the set. Tokens are included in the package. Accounts are registered in Bangladesh IP.',
                'price': 0.999,
                'stock': 34,
                'category_name': 'Facebook With friends',
                'image_url': '/static/images/facebook-account.png'
            },
            {
                'name': 'FB Accounts | [PVA] 100+ followers (friends and followers). Verified by email.',
                'description': 'Email@gmail.com included. Female or male. Partially filled profiles. 2FA in the set. Registered from Bangladesh IP.',
                'price': 1.02,
                'stock': 154,
                'category_name': 'Facebook With friends',
                'image_url': '/static/images/facebook-account.png'
            },
            {
                'name': 'FB Accounts | The accounts are registered 09.2024. Verified by e-mail.',
                'description': 'There is no email in the set. Female or male. Partially filled profile. Registered from Bangladesh IP.',
                'price': 0.87,
                'stock': 3140,
                'category_name': 'Facebook Aged',
                'image_url': '/static/images/facebook-account.png'
            },
            {
                'name': 'FB Accounts | The accounts were registered in 2020. Verified by email.',
                'description': '@rambler.ru (email included). Male or female. The profiles information is partially filled. Registered from Ukraine IP.',
                'price': 1.39,
                'stock': 110,
                'category_name': 'Facebook Aged',
                'image_url': '/static/images/facebook-account.png'
            },
            {
                'name': 'FB Accounts | Activated 2 Business Managers, acceptable for ads. Verified by email.',
                'description': 'Email NOT included. Male and female. Partially filled profile. Cookies are included in the set. Registered from Turkey IP.',
                'price': 2.78,
                'stock': 56,
                'category_name': 'Facebook For advertising',
                'image_url': '/static/images/facebook-account.png'
            }
        ]
        
        for prod_data in products_data:
            # Find category
            category = Category.query.filter_by(name=prod_data['category_name']).first()
            if category:
                product = Product(
                    name=prod_data['name'],
                    description=prod_data['description'],
                    price=prod_data['price'],
                    stock=prod_data['stock'],
                    category_id=category.id,
                    image_url=prod_data['image_url'],
                    account_details=json.dumps({
                        'type': 'facebook_account',
                        'verification': 'email_verified',
                        'includes': ['cookies', '2fa', 'profile_data']
                    })
                )
                db.session.add(product)
        
        db.session.commit()
        print("Seed data created successfully!")

if __name__ == '__main__':
    seed_data()

