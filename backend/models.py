from datetime import datetime
from app import db
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# User model for Admin, Customer, and Service Professional
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Service(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False)
    time_required = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class ServiceRequest(db.Model):
    __tablename__ = 'service_requests'

    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer,
                           db.ForeignKey('services.id'),
                           nullable=False)
    customer_id = db.Column(db.Integer,
                            db.ForeignKey('users.id'),
                            nullable=False)
    professional_id = db.Column(db.Integer,
                                db.ForeignKey('users.id'),
                                nullable=True)
    date_of_request = db.Column(db.DateTime, default=datetime.utcnow)
    date_of_completion = db.Column(db.DateTime, nullable=True)
    service_status = db.Column(db.String(50), default='requested')
    remarks = db.Column(db.String(255), nullable=True)

    service = db.relationship('Service', backref='service_requests')
    customer = db.relationship('User',
                               foreign_keys=[customer_id],
                               backref='customer_requests')
    professional = db.relationship('User',
                                   foreign_keys=[professional_id],
                                   backref='professional_requests')


class Professional(db.Model):
    __tablename__ = 'professionals'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'),
                        nullable=False)
    service_id = db.Column(db.Integer,
                           db.ForeignKey('services.id'),
                           nullable=False)
    experience = db.Column(db.String(100), nullable=True)
    approved = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref='professional_profile')
    service = db.relationship('Service', backref='assigned_professionals')


