from flask import jsonify

def get_problems(): 
    data = {"name": "Two-Sum", "difficulty": "Easy", "date_solved": "6/24/2025"}
    return jsonify(data)