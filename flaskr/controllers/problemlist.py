from flask import render_template
from .get_problem import get_problems

# rendering the problem list page 
def problemlist_page():
    problems = get_problems()
    return render_template('problemlist.html', problems=problems)