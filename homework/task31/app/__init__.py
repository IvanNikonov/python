from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://resume:tester@PostgreSQL-16:5432'
db.init_app(app)

from app import models
from app import routes