from models import app, db
from models import User, Admin, Service, Product, ServiceRequest, ProductOrder, PurchaseHistory, ServiceHistory

if __name__ == '__main__':
    with app.app_context():
        # Seed Users and Admins
        user1 = User(username='user1', password='password1', email='user1@example.com', full_name='User One')
        user2 = User(username='user2', password='password2', email='user2@example.com', full_name='User Two')
        admin1 = Admin(username='admin1', password='admin_password1', email='admin1@example.com', full_name='Admin One')
        admin2 = Admin(username='admin2', password='admin_password2', email='admin2@example.com', full_name='Admin Two')

        db.session.add_all([user1, user2, admin1, admin2])
        db.session.commit()

        # Seed Services and Products
        service1 = Service(name='Service 1', description='Description for Service 1', price=50.0)
        service2 = Service(name='Service 2', description='Description for Service 2', price=75.0)
        product1 = Product(name='Product 1', description='Description for Product 1', price=25.0)
        product2 = Product(name='Product 2', description='Description for Product 2', price=30.0)

        db.session.add_all([service1, service2, product1, product2])
        db.session.commit()

        # Seed Service Requests and Product Orders
        request1 = ServiceRequest(user=user1, service=service1, is_approved=True)
        request2 = ServiceRequest(user=user2, service=service2, is_approved=True)
        order1 = ProductOrder(user=user1, product=product1, is_approved=True)
        order2 = ProductOrder(user=user2, product=product2, is_approved=True)

        db.session.add_all([request1, request2, order1, order2])
        db.session.commit()

        # Seed Purchase History and Service History
        purchase1 = PurchaseHistory(user=user1, service=service1, product=product1)
        purchase2 = PurchaseHistory(user=user2, service=service2, product=product2)
        service_history1 = ServiceHistory(user=user1, service=service1)
        service_history2 = ServiceHistory(user=user2, service=service2)

        db.session.add_all([purchase1, purchase2, service_history1, service_history2])
        db.session.commit()
