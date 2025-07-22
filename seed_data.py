import os
import sys
from datetime import datetime

from src.main import app, db
from src.models.product import Category, Product, Order
from src.models.content import Page, MenuItem
from src.models.user import User
import json

def seed_data():
    with app.app_context():
        # Create tables
        db.create_all()
        
        # Path to the extracted seed data JSON file
        seed_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'database_seed_data.json')
        
        if not os.path.exists(seed_data_path):
            print(f"Seed data file not found at {seed_data_path}")
            return

        with open(seed_data_path, 'r', encoding='utf-8') as f:
            seed_data_json = json.load(f)

        # Clear existing data (optional, for fresh seeding)
        # It's important to delete in reverse order of foreign key dependencies
        db.session.query(Order).delete()
        db.session.query(Product).delete()
        db.session.query(Category).delete()
        db.session.query(Page).delete()
        db.session.query(MenuItem).delete()
        db.session.query(User).delete()
        db.session.commit()

        # Insert categories
        for item in seed_data_json.get('categories', []):
            category = Category(
                id=item['id'],
                name=item['name'],
                description=item['description'],
                created_at=datetime.fromisoformat(item['created_at']) if item['created_at'] else None
            )
            db.session.add(category)
        db.session.commit()
        print(f"Inserted {len(seed_data_json.get('categories', []))} categories.")

        # Insert products
        for item in seed_data_json.get('products', []):
            product = Product(
                id=item['id'],
                name=item['name'],
                description=item['description'],
                price=item['price'],
                stock=item['stock'],
                image_url=item['image_url'],
                category_id=item['category_id'],
                created_at=datetime.fromisoformat(item['created_at']) if item['created_at'] else None,
                updated_at=datetime.fromisoformat(item['updated_at']) if item['updated_at'] else None,
                account_details=item['account_details'],
                is_sold=item['is_sold']
            )
            db.session.add(product)
        db.session.commit()
        print(f"Inserted {len(seed_data_json.get('products', []))} products.")

        # Insert pages
        for item in seed_data_json.get('pages', []):
            page = Page(
                id=item['id'],
                title=item['title'],
                slug=item['slug'],
                content=item['content'],
                meta_description=item['meta_description'],
                meta_keywords=item['meta_keywords'],
                is_published=item['is_published'],
                created_at=datetime.fromisoformat(item['created_at']) if item['created_at'] else None,
                updated_at=datetime.fromisoformat(item['updated_at']) if item['updated_at'] else None
            )
            db.session.add(page)
        db.session.commit()
        print(f"Inserted {len(seed_data_json.get('pages', []))} pages.")

        # Insert menu_items
        for item in seed_data_json.get('menu_items', []):
            menu_item = MenuItem(
                id=item['id'],
                title=item['title'],
                url=item['url'],
                menu_type=item['menu_type'],
                order_index=item['order_index'],
                is_active=item['is_active'],
                target_blank=item['target_blank'],
                created_at=datetime.fromisoformat(item['created_at']) if item['created_at'] else None
            )
            db.session.add(menu_item)
        db.session.commit()
        print(f"Inserted {len(seed_data_json.get('menu_items', []))} menu items.")

        # Insert users
        for item in seed_data_json.get('users', []):
            user = User(
                id=item['id'],
                username=item['username'],
                email=item['email']
            )
            db.session.add(user)
        db.session.commit()
        print(f"Inserted {len(seed_data_json.get('users', []))} users.")

        # Insert orders
        for item in seed_data_json.get('orders', []):
            order = Order(
                id=item['id'],
                product_id=item['product_id'],
                customer_email=item['customer_email'],
                customer_name=item['customer_name'],
                quantity=item['quantity'],
                total_price=item['total_price'],
                status=item['status'],
                payment_method=item['payment_method'],
                account_details=item['account_details'],
                created_at=datetime.fromisoformat(item['created_at']) if item['created_at'] else None,
                updated_at=datetime.fromisoformat(item['updated_at']) if item['updated_at'] else None
            )
            db.session.add(order)
        db.session.commit()
        print(f"Inserted {len(seed_data_json.get('orders', []))} orders.")

        print("Seed data created successfully!")

if __name__ == '__main__':
    seed_data()


