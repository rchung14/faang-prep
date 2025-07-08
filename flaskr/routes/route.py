from flask import Blueprint
from ..controllers.index import index_page
from ..controllers.problemlist import problemlist_page

bp = Blueprint('main', __name__)

# this file serves to handle the basic page layouts
# stores different routes for the app
@bp.route('/')
def index():
    return index_page()

@bp.route('/problemlist')
def problemlist(): 
    return problemlist_page()