from flask import Blueprint

bp = Blueprint('main', __name__)

from app_pkg.main import routes