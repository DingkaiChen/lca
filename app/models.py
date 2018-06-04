from app import db,login
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from time import time
import jwt

@login.user_loader
def load_user(id):
	return User.query.get(int(id))

class User(UserMixin,db.Model):
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(64),index=True,unique=True)
	email=db.Column(db.String(120),index=True,unique=True)
	password_hash=(db.Column(db.String(128)))
	cases=db.relationship('Case',backref='user',lazy='dynamic')

	def __repr__(self):
		return '<User {}>'.format(self.username)

	def set_password(self,password):
		self.password_hash=generate_password_hash(password)

	def check_password(self,password):
		return check_password_hash(self.password_hash,password)
	
	def get_reset_password_token(self,expires_in=600):
		return jwt.encode(\
			{'reset_password':self.id,'exp':time()+expires_in},\
			current_app.config['SECRET_KEY'],algorithm='HS256').decode('utf-8')

	@staticmethod
	def verify_reset_password_token(token):
		try:
			id=jwt.decode(token,current_app.config['SECRET_KEY'],algorithms=['HS256'])['reset_password']
		except:
			return
		return User.query.get(id)

class Rawmaterial(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(50),unique=True)
	unit=db.Column(db.String(50))
	transports=db.relationship('Transport',backref='rawmaterial',lazy='dynamic')
	cases=db.relationship('Caserawmaterial',backref='rawmaterial',lazy='dynamic')
	default=db.Column(db.Float)

	def __repr__(self):
		return '<Rawmaterial {}>'.format(self.name)

class Transport(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	method=db.Column(db.Integer)
	unit=db.Column(db.String(50))
	rawmaterial_id=db.Column(db.Integer,db.ForeignKey('rawmaterial.id'))
	cases=db.relationship('Casetransport',backref='transport',lazy='dynamic')
	default=db.Column(db.Float)

class Processmaterial(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(50),unique=True)
	unit=db.Column(db.String(50))
	cases=db.relationship('Caseprocessmaterial',backref='processmaterial',lazy='dynamic')
	default=db.Column(db.Float)
	
	def __repr__(self):
		return '<Processmaterial {}>'.format(self.name)

class Waste(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(50),unique=True)
	unit=db.Column(db.String(50))
	cases=db.relationship('Casewaste',backref='waste',lazy='dynamic')
	default=db.Column(db.Float)
	
	def __repr__(self):
		return '<Waste {}>'.format(self.name)
class Case(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
	name=db.Column(db.String(50))
	productquantity=db.Column(db.Float)
	efficiency=db.Column(db.Float)
	energyconsumption=db.Column(db.Float)
	quantitytype=db.Column(db.String(50))
	rawmaterials=db.relationship('Caserawmaterial',backref='case',lazy='dynamic')
	transports=db.relationship('Casetransport',backref='case',lazy='dynamic')
	processmaterials=db.relationship('Caseprocessmaterial',backref='case',lazy='dynamic')
	wastes=db.relationship('Casewaste',backref='case',lazy='dynamic')

class Caserawmaterial(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	case_id=db.Column(db.Integer,db.ForeignKey('case.id'))
	rawmaterial_id=db.Column(db.Integer,db.ForeignKey('rawmaterial.id'))
	unitquantity=db.Column(db.Float)
	unitenergyconsumption=db.Column(db.Float)

class Casetransport(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	case_id=db.Column(db.Integer,db.ForeignKey('case.id'))
	transport_id=db.Column(db.Integer,db.ForeignKey('transport.id'))
	unitquantity=db.Column(db.Float)
	unitenergyconsumption=db.Column(db.Float)

class Caseprocessmaterial(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	case_id=db.Column(db.Integer,db.ForeignKey('case.id'))
	processmaterial_id=db.Column(db.Integer,db.ForeignKey('processmaterial.id'))
	unitquantity=db.Column(db.Float)
	unitenergyconsumption=db.Column(db.Float)

class Casewaste(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	case_id=db.Column(db.Integer,db.ForeignKey('case.id'))
	waste_id=db.Column(db.Integer,db.ForeignKey('waste.id'))
	unitquantity=db.Column(db.Float)
	unitenergyconsumption=db.Column(db.Float)

