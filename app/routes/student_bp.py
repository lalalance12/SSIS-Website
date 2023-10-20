from flask import Blueprint,render_template,request,jsonify,redirect,url_for
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

@student_bp.route('/delete_student/<string:student_id>', methods=['DELETE'])
def delete_student(student_id):
    try:
        result = student_model.delete_student(student_id)
        return jsonify(result)
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})\
        
@student_bp.route('/update_student/<string:student_id>', methods=['POST'])
def update_student(student_id):
    new_id = request.form['id']
    new_firstname = request.form['firstname']
    new_lastname = request.form['lastname']
    new_course = request.form['course']
    new_year = request.form['year']
    new_gender = request.form['gender']

    student_model.update_student(student_id, new_id, new_firstname, new_lastname, new_course, new_year, new_gender)

    students = student_model.get_students()
    courses = course_model.get_courses()
    return render_template('student.html', students=students, courses=courses)

@student_bp.route('/search_student', methods=['GET', 'POST'])
def search_student():
    if request.method == 'POST':
        search_query = request.form.get('search')
    else:
        search_query = request.args.get('search')
    students = student_model.search_students(search_query)
    return render_template('student.html', students=students)