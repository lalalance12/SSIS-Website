from flask import Blueprint,render_template,request
from app.models.course_m import course_model
from app.models.student_m import student_model

student_bp = Blueprint('student_bp', __name__)

@student_bp.route('/student', methods=['GET', 'POST'])
def student():
    courses = course_model.get_courses()

    if request.method == 'POST':
        id = request.form.get('id')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        course = request.form.get('course')
        year = request.form.get('year')
        gender = request.form.get('gender')
        student_model.create_student(id, firstname, lastname, course, year, gender)

        print("Successfully created student")

    students = student_model.get_students()
    print(students)
    return render_template('student.html', students=students, courses=courses)
