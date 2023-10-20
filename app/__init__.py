from flask import Flask
from flask_mysql_connector import MySQL
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY
from flask_wtf.csrf import CSRFProtect
from wtforms.validators import DataRequired

mysql = MySQL()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['MYSQL_HOST'] = DB_HOST
    app.config['MYSQL_USER'] = DB_USERNAME
    app.config['MYSQL_PASSWORD'] = DB_PASSWORD
    app.config['MYSQL_DATABASE'] = DB_NAME

    mysql.init_app(app)
    CSRFProtect(app)

    from .routes.home_bp import home_bp
    from .routes.college_bp import college_bp
    from .routes.course_bp import course_bp
    from .routes.student_bp import student_bp
    

    app.register_blueprint(home_bp, url_prefix='/')
    app.register_blueprint(college_bp, url_prefix='/college')
    app.register_blueprint(course_bp, url_prefix='/course')
    app.register_blueprint(student_bp, url_prefix='/student')

    return app
