from flask import  Flask, render_template, request, redirect, url_for, jsonify, Blueprint
from app.models.course_m import course_model
from app.models.college_m import college_model

course_bp = Blueprint('course_bp', __name__)

@course_bp.route('/course', methods=['GET', 'POST'])
def course():
    colleges = college_model.get_colleges()
    course = None  

    if request.method == 'POST':
        code = request.form.get('code')
        name = request.form.get('name')
        college_code = request.form.get('college')
        course_model.create_course(code, name, college_code)
        print("Successfully created course")

    courses = course_model.get_courses()
    print(courses)
    return render_template('course.html', courses=courses, colleges=colleges, course=course)  

@course_bp.route('/delete_course/<string:course_code>', methods=['DELETE'])
def delete_course(course_code):
    print("Received course code:", course_code)  # Add this line
    if request.method == 'DELETE':
        result = course_model.delete_course(course_code)
        response = jsonify(result)
        return response
    
@course_bp.route('/update_course/<string:course_code>', methods=['POST'])
def update_course(course_code):
    new_code = request.form['code']
    new_name = request.form['name']
    new_college = request.form['college']
    course_model.update_course(course_code, new_code, new_name, new_college)
    courses = course_model.get_courses()
    colleges = college_model.get_colleges()
    return render_template('course.html', courses=courses, colleges=colleges)

@course_bp.route('/search_course', methods=['GET'])
def search_course():
    search_query = request.args.get('search')
    courses = course_model.search_courses(search_query)
    return render_template('course.html', courses=courses)