from flask import Blueprint
from ..controllers.index import index_page

bp = Blueprint('main', __name__)

# a simple page that says hello
# route is used for simple html 
@bp.route('/')
def index():
    return index_page()
