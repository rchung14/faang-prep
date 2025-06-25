from flask import Blueprint
from ..controllers.hi import hi_logic

bp = Blueprint('main', __name__)

# a simple page that says hello
@bp.route('/')
def hello_route():
    return hi_logic()



