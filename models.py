from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_database.db'
db = SQLAlchemy(app)

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(255), nullable=False)
    service_requests = db.relationship('ServiceRequest', backref='user')
    product_orders = db.relationship('ProductOrder', backref='user')
    purchase_history = db.relationship('PurchaseHistory', backref='user')
    service_history = db.relationship('ServiceHistory', backref='user')

class Admin(db.Model):
    admin_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(255), nullable=False)

class Service(db.Model):
    service_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    is_approved = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    service_requests = db.relationship('ServiceRequest', backref='service')
    purchase_history = db.relationship('PurchaseHistory', backref='service')
    service_history = db.relationship('ServiceHistory', backref='service')

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    is_approved = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    product_orders = db.relationship('ProductOrder', backref='product')
    purchase_history = db.relationship('PurchaseHistory', backref='product')

class ServiceRequest(db.Model):
    request_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.service_id'), nullable=False)
    is_approved = db.Column(db.Boolean, default=False)
    requested_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())

class ProductOrder(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), nullable=False)
    is_approved = db.Column(db.Boolean, default=False)
    ordered_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())

class PurchaseHistory(db.Model):
    purchase_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.service_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
    purchase_date = db.Column(db.DateTime, server_default=db.func.current_timestamp())

class ServiceHistory(db.Model):
    history_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.service_id'), nullable=False)
    service_date = db.Column(db.DateTime, server_default=db.func.current_timestamp())



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
