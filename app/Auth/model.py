from flask_login import UserMixin
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


posts = db.relationship('Post', backref="author", lazy=True)

class User(db.Model, UserMixin):
    __bind_key__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    birthdate = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    identification = db.Column(db.Integer)
    phone = db.Column(db.Integer)
    userTypeId = db.Column(db.Integer, db.ForeignKey('typeusers.id'),
        nullable=False)


    def __init__(self, name, address, birthdate, email,  identification, phone, usertype):
        self.name = name
        self.address = address
        self.birthdate = birthdate
        self.email = email
        self.identification = identification
        self.phone = phone
        self.userType = usertype

    def __repr__(self):
        return f'<User {self.name}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_all():
        return User.query.all()


class TypeUsers(db.Model):
    __tablename__ = 'typeusers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    user = db.relationship('users', backref='typeusers', lazy=True)

    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_all():
        return TypeUsers.query.all()

class Services(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, name):
        self.name = name