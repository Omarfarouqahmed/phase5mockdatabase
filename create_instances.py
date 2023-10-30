# Import your database models
from models import db, User, Admin, Service, Product, ServiceRequest, ProductOrder, PurchaseHistory, ServiceHistory

# Create an application context
from models import app
app.app_context().push()

# Create instances for User and Admin
new_user = User(username='john_doe', password='user_password', email='john@example.com', full_name='John Doe')
new_admin = Admin(username='admin_doe', password='admin_password', email='admin@example.com', full_name='Admin Doe')

# Create instances for Service and Product
new_service = Service(name='Pet Grooming', description='Groom your pets', price=50.00)
new_product = Product(name='Fish Pellets', description='High-quality fish food', price=5.99)

# Create instances for Service_Request and Product_Order
new_service_request = ServiceRequest(user=new_user, service=new_service)
new_product_order = ProductOrder(user=new_user, product=new_product)

# Create instances for Purchase_History and Service_History
new_purchase_history = PurchaseHistory(user=new_user, service=new_service, product=new_product)
new_service_history = ServiceHistory(user=new_user, service=new_service)

# Add these instances to the database and commit the changes
db.session.add(new_user)
db.session.add(new_admin)
db.session.add(new_service)
db.session.add(new_product)
db.session.add(new_service_request)
db.session.add(new_product_order)
db.session.add(new_purchase_history)
db.session.add(new_service_history)
db.session.commit()
