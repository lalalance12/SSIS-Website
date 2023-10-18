# Initalize all here the blueprints which contains the routes and connect the configurations here

from flask import Flask
# from flask_mysql_connector import MySQL
# from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] ='lol1412'

    from .routes.home_bp import home_bp
    from .routes.college_bp import college_bp
    from .routes.course_bp import course_bp
    from .routes.student_bp import student_bp
    

    app.register_blueprint(home_bp, url_prefix='/')
    app.register_blueprint(college_bp, url_prefix='/college/')
    app.register_blueprint(course_bp, url_prefix='/course/')
    app.register_blueprint(student_bp, url_prefix='/student/')
    

    return app
