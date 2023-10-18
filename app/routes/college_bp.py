from flask import Blueprint,render_template,request
from . import college_bp

college_bp = Blueprint('college_bp', __name__)

@college_bp.route('/college', methods=['GET', 'POST'])
def college():
    return render_template('college.html')
