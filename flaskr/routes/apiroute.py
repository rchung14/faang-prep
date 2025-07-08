from flask import Blueprint
from ..controllers.get_problem import get_problems

apibp = Blueprint('api', __name__, url_prefix='/api')

#api is used for data serving routes 

@apibp.route('/problem')
def get_problems_route():
    return get_problems()