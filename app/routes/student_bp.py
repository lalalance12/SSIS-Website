from flask import Blueprint,render_template,request,jsonify,flash
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
        
        if student_model.create_student(id, firstname, lastname, course, year, gender) == "Student created successfully":
            flash("Student created successfully!")
        else:
            flash("Failed to create student!")

    students = student_model.get_students()
    return render_template('student.html', students=students, courses=courses)

@student_bp.route('/delete_student/<string:student_id>', methods=['DELETE'])
def delete_student(student_id):
    try:
        result = student_model.delete_student(student_id)
        flash("Student is deleted")
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

    if student_model.update_student(student_id, new_id, new_firstname, new_lastname, new_course, new_year, new_gender) == "Student updated successfully":
        flash("Student updated successfully!")
    else:
        flash("Failed to update student!")

    students = student_model.get_students()
    courses = course_model.get_courses()
    return render_template('student.html', students=students, courses=courses)


@student_bp.route('/search_student', methods=['GET', 'POST'])
def search_student():
    courses = course_model.get_courses()

    if request.method == 'POST':
        search_query = request.form.get('search')
        filter_by = request.form.get('filter_by')
    else:
        search_query = request.args.get('search')
        filter_by = request.args.get('filter_by')
    
    if filter_by == 'id':
        students = student_model.search_students_by_id(search_query)
    elif filter_by == 'firstname':
        students = student_model.search_students_by_firstname(search_query)
    elif filter_by == 'lastname':
        students = student_model.search_students_by_lastname(search_query)
    elif filter_by == 'course':
        students = student_model.search_students_by_course(search_query)
    elif filter_by == 'year':
        students = student_model.search_students_by_year(search_query)
    elif filter_by == 'gender':
        students = student_model.search_students_by_gender(search_query)
    elif filter_by == 'college':
        students = student_model.search_students_by_college(search_query)
    else:
        students = student_model.get_students()
    
    return render_template('student.html', students=students, courses=courses)