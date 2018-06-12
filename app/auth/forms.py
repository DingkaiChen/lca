from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired,DataRequired,ValidationError,Email,EqualTo
from app.models import User,Register

class LoginForm(FlaskForm):
	username=StringField('Username',validators=[DataRequired()])
	password=PasswordField('Password',validators=[DataRequired()])
	remember_me=BooleanField('Remember Me')
	submit=SubmitField('Sign In')

class RegistrationForm(FlaskForm):
	username=StringField('Username',validators=[DataRequired()])
	email=StringField('Email',validators=[DataRequired(),Email()])
	password=PasswordField('Password',validators=[DataRequired()])
	password2=PasswordField('Repeat Password',validators=[DataRequired(),EqualTo('password')])
	phone=StringField('联系电话',validators=[InputRequired()])
	name=StringField('姓名',validators=[InputRequired()])
	submit=SubmitField('Register')

	def validate_username(self,username):
		user=User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('您所申请的用户名已被其他用户申请，请更换用户名.')
		else:
			register=Register.query.filter_by(username=username.data,verified=1).first()
			if register is not None:
				raise ValidationError('您所申请的用户名已被其他用户申请，请更换用户名.')

	def validate_email(self,email):
		user=User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('邮箱已被注册，请使用其它邮箱注册.')
		else:
			register=Register.query.filter_by(email=email.data,verified=1).first()
			if register is not None:
				raise ValidationError('邮箱已被注册，请使用其它邮箱注册.')

class ResetPasswordRequestForm(FlaskForm):
	email=StringField('Email',validators=[DataRequired(),Email()])
	submit=SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
	password=PasswordField('Password',validators=[DataRequired()])
	password2=PasswordField('Repeat Password',validators=[DataRequired(),EqualTo('password')])
	submit=SubmitField('Request Password Reset')
