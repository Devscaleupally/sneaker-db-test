from flask import Blueprint
from . import views

# Create the blueprint
api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/sneakers/<string:style>')
def get_sneaker(style): return views.get_sneaker(style)