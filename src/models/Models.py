from flask_login import UserMixin
from settings import db


class UserModel(UserMixin, db.Model):
	__tablename__ = 'user'
	
	id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
	email = db.Column(db.String(20), unique=True)
	password = db.Column(db.String(20))
	name = db.Column(db.String(20))
	role = db.Column(db.Integer)