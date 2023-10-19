from flask import Blueprint,render_template,request,redirect 
from app.models.college_m import college_model

college_bp = Blueprint('college_bp', __name__)

@college_bp.route('/college', methods=['GET', 'POST'])
def college():
    if request.method == 'POST':
        code = request.form.get('code')
        name = request.form.get('name')
        college_model.create_college(code, name)
        print("Successfully created college")
        
    colleges = college_model.get_colleges()     
    print(colleges)
    return render_template('college.html', colleges=colleges)


@college_bp.route('/college/success', methods=['GET'])
def success():
    return render_template('success.html')