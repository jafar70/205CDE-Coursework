from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/find_student")
def get_sid():
    return render_template("get_sid.html")





@app.route("/add_student")
def add_new_student():
    return render_template("add_student.html")






@app.route("/add_grade")
def add_new_grade():
    # Get student_github, project_title, and grade from Grades 
    return render_template("add_grade.html")







if __name__ == '__main__':
    app.debug = True
    port = int(os.getenv('PORT', 8080))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host)