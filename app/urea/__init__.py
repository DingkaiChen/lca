from flask import Blueprint

bp=Blueprint('urea',__name__)

from app.urea import routes
