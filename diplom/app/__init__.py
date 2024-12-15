from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://learning_shop:tester@PostgreSQL-16:5432'
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
db.init_app(app)

from app import models
from app import routes