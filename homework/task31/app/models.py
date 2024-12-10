from app import app, db
from datetime import datetime

class Resume(db.Model):
    __tablename__ = "resume"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    dt_create = db.Column(db.DateTime, nullable=False)
    id_user = db.Column(db.ForeignKey('user.id'))
    experience = db.relationship('Experience', backref='resume')

    def get_date_format(self):
        return self.dt_create.strftime('%d-%m-%Y %H:%M:%S')

class User(db.Model):
     __tablename__ = "user"
     id = db.Column(db.Integer, primary_key=True)
     username = db.Column(db.String, unique=True, nullable=False)
     email = db.Column(db.String)
     phone = db.Column(db.String)
     age = db.Column(db.Integer, nullable=False)
     resume = db.relationship('Resume', backref='user')

class Experience(db.Model):
    __tablename__ = "experience"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=False)
    period = db.Column(db.String, nullable=False)
    id_resume = db.Column(db.ForeignKey('resume.id'))

with app.app_context():
    db.create_all()