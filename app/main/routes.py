from app import db
from app.main import bp
from flask import render_template
from flask_login import login_required
from werkzeug.urls import url_parse

@bp.route('/')
@bp.route('/index',methods=['GET'])
@login_required
def index():
	return render_template('main/index.html',title='Home')
