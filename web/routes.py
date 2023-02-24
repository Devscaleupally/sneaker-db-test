from flask import Blueprint
from . import views

# Create the blueprint
web = Blueprint('web', __name__, url_prefix='/')

@web.route('/')
def home(): return views.home()

@web.route('add-data', methods=['POST'])
def post_details(): return views.post_details()