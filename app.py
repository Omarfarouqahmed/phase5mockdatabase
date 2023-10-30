from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import User, Admin, Service, Product, ServiceRequest, ProductOrder, PurchaseHistory, ServiceHistory

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Replace with your actual database URI
db = SQLAlchemy(app)

# Define your models (User, Admin, Service, Product, etc.) here

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

# Add similar endpoints for other tables (Admin, Product, ServiceRequest, ProductOrder, PurchaseHistory, ServiceHistory)

# Define endpoints for relationships (e.g., ServiceRequest, ProductOrder, PurchaseHistory, ServiceHistory)

if __name__ == '__main__':
    app.run(debug=True)
