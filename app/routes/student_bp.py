from flask import Blueprint,render_template,request
from . import student_bp

student_bp = Blueprint('student_bp', __name__)

@student_bp.route('/student', methods=['GET', 'POST'])
def student():
    return render_template('student.html')
