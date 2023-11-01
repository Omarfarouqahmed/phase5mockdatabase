from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import User, Admin, Service, Product, ServiceRequest, ProductOrder, PurchaseHistory, ServiceHistory
from models import db, app
from flask_login import LoginManager, login_user, current_user, login_required
from functools import wraps
from werkzeug.security import check_password_hash
app.secret_key = 'asdfghjklpoiuytrewq1234567890'
# from flask_login import current_user

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_database.db'
# db = SQLAlchemy(app)

# Define your models (User, Admin, Service, Product, ServiceRequest, ProductOrder, PurchaseHistory, ServiceHistory) here

# Endpoint to get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [{'user_id': user.user_id, 'username': user.username, 'email': user.email, 'full_name': user.full_name} for user in users]
    return jsonify(user_list)

# Endpoint to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], password=data['password'], email=data['email'], full_name=data['full_name'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

# Endpoint to get all admins
@app.route('/admins', methods=['GET'])
def get_admins():
    admins = Admin.query.all()
    admin_list = [{'admin_id': admin.admin_id, 'username': admin.username, 'email': admin.email, 'full_name': admin.full_name} for admin in admins]
    return jsonify(admin_list)

# Endpoint to create a new admin
@app.route('/admins', methods=['POST'])
def create_admin():
    data = request.get_json()
    new_admin = Admin(username=data['username'], password=data['password'], email=data['email'], full_name=data['full_name'])
    db.session.add(new_admin)
    db.session.commit()
    return jsonify({'message': 'Admin created successfully'}), 201

# Add similar endpoints for other tables (Service, Product, ServiceRequest, ProductOrder, PurchaseHistory, ServiceHistory)

# Define endpoints for relationships (e.g., ServiceRequest, ProductOrder, PurchaseHistory, ServiceHistory)
# Endpoint to get all services
@app.route('/services', methods=['GET'])
def get_services():
    services = Service.query.all()
    service_list = [{'service_id': service.service_id, 'name': service.name, 'description': service.description, 'price': float(service.price)} for service in services]
    return jsonify(service_list)

# Endpoint to create a new service
@app.route('/services', methods=['POST'])
def create_service():
    data = request.get_json()
    new_service = Service(name=data['name'], description=data['description'], price=data['price'])
    db.session.add(new_service)
    db.session.commit()
    return jsonify({'message': 'Service created successfully'}), 201

# Add endpoints for Product table and its relationships
# Endpoint to get all products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_list = [{'product_id': product.product_id, 'name': product.name, 'description': product.description, 'price': float(product.price)} for product in products]
    return jsonify(product_list)

# Endpoint to create a new product
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(name=data['name'], description=data['description'], price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product created successfully'}), 201

# Add endpoints for ServiceRequest table
# Endpoint to get all service requests
@app.route('/service-requests', methods=['GET'])
def get_service_requests():
    service_requests = ServiceRequest.query.all()
    requests = [{'request_id': request.request_id, 'user_id': request.user_id, 'service_id': request.service_id, 'is_approved': request.is_approved, 'requested_at': request.requested_at} for request in service_requests]
    return jsonify(requests)

# Add endpoints for ProductOrder table
# Endpoint to get all product orders
@app.route('/product-orders', methods=['GET'])
def get_product_orders():
    product_orders = ProductOrder.query.all()
    orders = [{'order_id': order.order_id, 'user_id': order.user_id, 'product_id': order.product_id, 'is_approved': order.is_approved, 'ordered_at': order.ordered_at} for order in product_orders]
    return jsonify(orders)

# Add endpoints for PurchaseHistory table
# Endpoint to get all purchase history
@app.route('/purchase-history', methods=['GET'])
def get_purchase_history():
    purchase_history = PurchaseHistory.query.all()
    history = [{'purchase_id': record.purchase_id, 'user_id': record.user_id, 'service_id': record.service_id, 'product_id': record.product_id, 'purchase_date': record.purchase_date} for record in purchase_history]
    return jsonify(history)

# Add endpoints for ServiceHistory table
# Endpoint to get all service history
@app.route('/service-history', methods=['GET'])
def get_service_history():
    service_history = ServiceHistory.query.all()
    history = [{'history_id': record.history_id, 'user_id': record.user_id, 'service_id': record.service_id, 'service_date': record.service_date} for record in service_history]
    return jsonify(history)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        login_user(user)
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Login failed'}, 401)
    

def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_admin:
            return jsonify({'message': 'Access denied. You must be an admin.'}, 403)
        return func(*args, **kwargs)
    return login_required(decorated_view)

@app.route('/admin/dashboard', methods=['GET'])
@admin_required
def admin_dashboard():
    # Your admin dashboard logic here
    return jsonify({'message': 'Admin dashboard'})



if __name__ == '__main__':
    

    app.run(port=5555, debug=True)