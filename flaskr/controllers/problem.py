from flask import jsonify
from ..database.db import connect_db
import sqlite3

def get_problems(): 
    db = connect_db()
    db.row_factory = sqlite3.Row
    cur = db.cursor()

    cur.execute("DROP TABLE IF EXISTS problems")
    cur.execute("CREATE TABLE problems (pid integer primary key autoincrement, problem_name text, date_solved date, time_taken int)")
    cur.execute("INSERT INTO problems (problem_name, date_solved, time_taken) VALUES ('Two Sum', '2025-06-28', 15)")
    results = cur.execute("SELECT problem_name, date_solved, time_taken FROM problems")


    problem_info = results.fetchall()
    row = problem_info[0]
    return f"<h1>Name: {row['problem_name']}, <br>Date Solved: {row['date_solved']}, <br>Time Taken: {row['time_taken']} minutes"