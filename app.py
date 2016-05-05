import solar_app

from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/location")
def location():
    return render_template("location.html")

@app.route("/societies")
def societies():
    return render_template("societies.html")

@app.route("/sports")
def sports():
    return render_template("sports.html")

@app.route("/events")
def events():
    return render_template("events.html")

@app.route("/volunteering")
def volunteering():
    return render_template("volunteering.html")

@app.route("/contactus")
def contactus():
    return render_template("contactus.html")

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/find_student")
def get_sid():
    return render_template("get_sid.html")
    
@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")


@app.route("/student")
def get_student():
    solar_app.connect_to_db()
    student_github = request.args.get("github")
    row = solar_app.get_student_by_github(student_github)
    rows = solar_app.show_grade(student_github) # list of tuples
    html = render_template("student_info.html", first_name=row[0],
                                                last_name=row[1],
                                                github=row[2],
                                                projects=rows)
    return html



@app.route("/add_student")
def add_new_student():
    return render_template("add_student.html")


@app.route("/make_student")
def create_new_student():
    #####################################################3
    first_name = request.args.get("first_name")
    last_name = request.args.get("last_name")
    github = request.args.get("github")
    solar_app.connect_to_db()
    if solar_app.make_new_student(first_name, last_name, github):
        html = render_template("new_student.html", first_name=first_name,
                                                last_name=last_name,
                                                github=github)
    return html



@app.route("/add_grade")
def add_new_grade():
    # Get student_github, project_title, and grade from Grades 
    return render_template("add_grade.html")


@app.route("/new_grade")
def new_grade():
    student_github = request.args.get("github")
    project_title = request.args.get("project")
    grade = request.args.get("grade")
    solar_app.connect_to_db()
    if solar_app.give_grade(student_github, project_title, grade):
        html = render_template("new_grade.html", github=student_github,
                                                title=project_title,
                                                grade=grade)
    return html




if __name__ == '__main__':
    app.debug = True
    port = int(os.getenv('PORT', 8080))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host)