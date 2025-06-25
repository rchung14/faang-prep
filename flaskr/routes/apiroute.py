from flask import Blueprint
from ..controllers.problem import get_problems

apibp = Blueprint('api', __name__, url_prefix='/api')

@apibp.route('/problem')
def get_problems_route():
    return get_problems()



