from flask import Blueprint,render_template, redirect
from . import home_bp

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/')
def index():
    return redirect('/home')

@home_bp.route('/home')
def home():
    return render_template('home.html')