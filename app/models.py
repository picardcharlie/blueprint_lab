from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import datetime

# from app import db
# from app.blogger import app

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True, index=True)
    # password = db.Column(db.String(50))
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(50), unique=True, index=True)
    dateofreg = db.Column(db.DateTime, default=datetime.datetime.now)

    @property
    def password(self):
        raise AttributeError("Password is not readable") #Error message if hashed password is called

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, firstname, lastname, username, password, email):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.email = email


class Post(db.Model):
    __tablename__ = 'posts'
    pid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    puid = db.Column(db.Integer, db.ForeignKey('users.uid'))

    def __init__(self, title, description, puid):
        self.title = title
        self.description = description
        self.puid = puid
