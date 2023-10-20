from flask import Flask, render_template, request, redirect, url_for, jsonify, Blueprint
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

@college_bp.route('/delete_college/<string:college_code>', methods=['DELETE'])
def delete_college(college_code):
    if request.method == 'DELETE':
        result = college_model.delete_college(college_code)
        response = jsonify(result)
        return response

@college_bp.route('/update_college/<string:college_code>', methods=['GET', 'POST'])
def update_college(college_code):
    if request.method == 'POST':
        new_code = request.form.get('code')
        new_name = request.form.get('name')
        college_model.update_college(college_code, new_code, new_name)
        return redirect(url_for('college_bp.college'))

    # Fetch the current college data
    college = college_model.get_college_by_code(college_code)
    return render_template('college.html', college=college)
   
@college_bp.route('/search_college', methods=['GET'])
def search_college():
    search_query = request.args.get('search')
    colleges = college_model.search_colleges(search_query)
    return render_template('college.html', colleges=colleges)
