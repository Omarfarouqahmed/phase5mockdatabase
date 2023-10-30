from models import app, db, User

with app.app_context():
    # Create a new user
    new_user = User(username='john_doe', password='password', email='john@example.com')
    db.session.add(new_user)
    db.session.commit()

    # Query the users
    users = User.query.all()
    for user in users:
        print(user.username, user.email)
