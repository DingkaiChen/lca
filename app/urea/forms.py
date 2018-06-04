from flask_wtf import FlaskForm
from wtforms import IntegerField,StringField, FloatField, SelectField, SubmitField
from wtforms.validators import InputRequired
from app.models import User,Case,Rawmaterial,Transport,Processmaterial,Waste,Caserawmaterial,Casetransport,Caseprocessmaterial,Casewaste

class CaseForm(FlaskForm):
	id=IntegerField('ID')
	name=StringField('案例名称',validators=[InputRequired()])
	submit=SubmitField('添加')

class RawmaterialForm(FlaskForm):
	id=IntegerField('ID')
	name=StringField('原料名称',validators=[InputRequired()])
	unit=StringField('单位')
	default=FloatField('单位能耗默认值')
	rawmaterialsubmit=SubmitField('添加')

class TransportForm(FlaskForm):
	id=IntegerField('ID')
	rawmaterial=SelectField('原料',coerce=int,validators=[InputRequired()])
	method=StringField('运输方式',validators=[InputRequired()])
	unit=StringField('单位')
	default=FloatField('单位原料运输方式能耗默认值')
	transportsubmit=SubmitField('添加')

class ProcessmaterialForm(FlaskForm):
	id=IntegerField('ID')
	name=StringField('材料名称',validators=[InputRequired()])
	unit=StringField('单位')
	default=FloatField('单位能耗默认值')
	processmaterialsubmit=SubmitField('添加')

class WasteForm(FlaskForm):
	id=IntegerField('ID')
	name=StringField('废弃物处理途径',validators=[InputRequired()])
	unit=StringField('单位')
	default=FloatField('单位能耗默认值')
	wastesubmit=SubmitField('添加')
