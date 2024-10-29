# create_tables.py
from app import db, app
from models import User, Service, ServiceRequest, Professional

with app.app_context():
    db.create_all()
    print("Tables created successfully!")

