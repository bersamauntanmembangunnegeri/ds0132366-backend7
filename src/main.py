import os
import sys
import os
# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory
from flask_cors import CORS
from src.models.user import db
from src.models.product import Category, Product, Order
from src.models.content import Page, MenuItem
from src.models.homepage import HomepageSection, SiteSettings
from src.models.featured_products import FeaturedProductsSection
from src.routes.user import user_bp
from src.routes.product import product_bp
from src.routes.content import content_bp
from src.routes.homepage import homepage_bp
from src.routes.layout import layout_bp
from src.routes.menu import menu_bp
from src.routes.admin import admin_bp

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

# Enable CORS for all routes
CORS(app)

# Add cache control headers to prevent caching issues
@app.after_request
def after_request(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(product_bp, url_prefix='/api')
app.register_blueprint(content_bp, url_prefix='/api')
app.register_blueprint(homepage_bp, url_prefix='/api')
app.register_blueprint(layout_bp, url_prefix='/api')
app.register_blueprint(menu_bp, url_prefix='/api')
app.register_blueprint(admin_bp)

# uncomment if you need to use database
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'app.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
            return "Static folder not configured", 404

    # Handle API routes first - don't serve static files for API calls
    # if path.startswith("api/"):
    #     return "API route not found", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "index.html not found", 404

@app.errorhandler(404)
def not_found(error):
    return {"error": "Not found"}, 404

@app.errorhandler(500)
def internal_error(error):
    return {"error": "Internal server error"}, 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
