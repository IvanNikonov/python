from time import time
from app import app, db


class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String, unique=True, nullable=False)
    hash_password = db.Column(db.String, nullable=False)


class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    alias = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.Float)
    is_active = db.Column(db.Boolean)
    order_elements = db.relationship('OrderElement', backref='product')

class Order(db.Model):
    __tablename__ = "order"
    id = db.Column(db.Integer, primary_key=True)
    dt_create = db.Column(db.DateTime, default=time())
    sum = db.Column(db.Float)
    name = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    email = db.Column(db.String(255))
    comment = db.Column(db.String(255))
    id_status = db.Column(db.Integer(), db.ForeignKey('order_status.id'))
    order_elements = db.relationship('OrderElement', backref='order')

class OrderStatus(db.Model):
    __tablename__ = "order_status"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    orders = db.relationship('Order', backref='order_status')

class OrderElement(db.Model):
    __tablename__ = "order_element"
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)
    price = db.Column(db.Float)
    id_order = db.Column(db.Integer(), db.ForeignKey('order.id'))
    id_product = db.Column(db.Integer(), db.ForeignKey('product.id'))

with app.app_context():
    db.create_all()
