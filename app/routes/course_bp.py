from flask import Blueprint,render_template,request,redirect,jsonify
from app.models.course_m import course_model
from app.models.college_m import college_model

course_bp = Blueprint('course_bp', __name__)

@course_bp.route('/course', methods=['GET', 'POST'])
def course():
    colleges = college_model.get_colleges()

    if request.method == 'POST':
        code = request.form.get('code')
        name = request.form.get('name')
        college_code = request.form.get('college') 
        course_model.create_course(code, name, college_code)
        print("Successfully created course")

    courses = course_model.get_courses()     
    print(courses)
    return render_template('course.html', courses=courses, colleges=colleges)