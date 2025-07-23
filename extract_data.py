import os
import sys
import json
from datetime import datetime

# Add the parent directory to the sys.path to import src modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.main import app, db
from src.models.product import Category, Product, Order
from src.models.content import Page, MenuItem
from src.models.user import User

def extract_data():
    with app.app_context():
        all_data = {
            "categories": [],
            "products": [],
            "pages": [],
            "menu_items": [],
            "users": [],
            "orders": []
        }

        # Extract Categories
        categories = Category.query.all()
        for cat in categories:
            all_data["categories"].append(cat.to_dict())

        # Extract Products
        products = Product.query.all()
        for prod in products:
            prod_dict = prod.to_dict()
            # Remove category_name as it's a relationship, not a direct column
            prod_dict.pop("category_name", None)
            all_data["products"].append(prod_dict)

        # Extract Pages
        pages = Page.query.all()
        for page in pages:
            all_data["pages"].append(page.to_dict())

        # Extract Menu Items
        menu_items = MenuItem.query.all()
        for item in menu_items:
            all_data["menu_items"].append(item.to_dict())

        # Extract Users
        users = User.query.all()
        for user in users:
            user_dict = user.to_dict()
            # Remove password_hash as it's sensitive and not needed for seeding
            user_dict.pop("password_hash", None)
            all_data["users"].append(user_dict)

        # Extract Orders
        orders = Order.query.all()
        for order in orders:
            order_dict = order.to_dict()
            # Remove product_name as it's a relationship, not a direct column
            order_dict.pop("product_name", None)
            all_data["orders"].append(order_dict)

        # Custom JSON serializer for datetime objects
        def json_serial(obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            raise TypeError ("Type %s not serializable" % type(obj))

        print(json.dumps(all_data, indent=4, default=json_serial))

if __name__ == '__main__':
    extract_data()


