# AccsMarket Backend

Backend API untuk website e-commerce AccsMarket yang mirip dengan accsmarket.com.

## Fitur

- **Manajemen Produk**: CRUD operations untuk produk digital (akun media sosial)
- **Manajemen Kategori**: Organisasi produk berdasarkan kategori
- **Guest Checkout**: Pembelian tanpa perlu registrasi
- **Order Management**: Tracking pesanan dan status pembayaran
- **CORS Support**: Mendukung frontend React
- **SQLite Database**: Database ringan untuk development

## Tech Stack

- **Framework**: Flask
- **Database**: SQLite dengan SQLAlchemy ORM
- **CORS**: Flask-CORS
- **Authentication**: Tidak diperlukan untuk guest checkout

## API Endpoints

### Categories
- `GET /api/categories` - Get all categories
- `POST /api/categories` - Create new category

### Products
- `GET /api/products` - Get all products (optional: ?category_id=X)
- `GET /api/products/{id}` - Get specific product
- `POST /api/products` - Create new product
- `PUT /api/products/{id}` - Update product
- `DELETE /api/products/{id}` - Delete product

### Orders
- `POST /api/orders` - Create new order (guest checkout)
- `GET /api/orders/{id}` - Get specific order
- `GET /api/orders` - Get all orders (admin)
- `PUT /api/orders/{id}/status` - Update order status

## Installation

1. Clone repository
2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run seed data:
   ```bash
   python seed_data.py
   ```
5. Start server:
   ```bash
   python src/main.py
   ```

## Database Schema

### Category
- id (Primary Key)
- name (Unique)
- description
- created_at

### Product
- id (Primary Key)
- name
- description
- price
- stock
- image_url
- category_id (Foreign Key)
- account_details (JSON string)
- is_sold
- created_at
- updated_at

### Order
- id (Primary Key)
- customer_name
- customer_email
- product_id (Foreign Key)
- quantity
- total_price
- status (pending, paid, completed, cancelled)
- payment_method
- created_at
- updated_at

## Deployment

Aplikasi ini siap untuk di-deploy ke platform seperti:
- Render
- Heroku
- Railway
- Vercel (untuk full-stack)

Pastikan untuk:
1. Update `requirements.txt`
2. Set environment variables jika diperlukan
3. Configure database untuk production

