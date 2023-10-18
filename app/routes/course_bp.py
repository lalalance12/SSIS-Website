from flask import Blueprint,render_template,request
from . import course_bp

course_bp = Blueprint('course_bp', __name__)

@course_bp.route('/course', methods=['GET', 'POST'])
def course():

    return render_template('course.html')
