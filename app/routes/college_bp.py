from flask import Blueprint,render_template,request,redirect 
from . import college_bp

college_bp = Blueprint('college_bp', __name__)

@college_bp.route('/college', methods=['GET', 'POST'])
def college():
    if request.method == 'POST':
        # Retrieve form data using request.form
        college_code = request.form.get('code')
        college_name = request.form.get('name')
        # Process the data (e.g., save it to a database)
        # Redirect to a success page or the same form page
        return render_template('success.html')  
    return render_template('college.html')


@college_bp.route('/college/success', methods=['GET'])
def success():
    return render_template('success.html')