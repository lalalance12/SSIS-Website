from flask import Flask
from flask_mysql_connector import MySQL
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET, CLOUDINARY_FOLDER
from flask_wtf.csrf import CSRFProtect
import cloudinary
from cloudinary.utils import cloudinary_url

mysql = MySQL()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['MYSQL_HOST'] = DB_HOST
    app.config['MYSQL_USER'] = DB_USERNAME
    app.config['MYSQL_PASSWORD'] = DB_PASSWORD
    app.config['MYSQL_DATABASE'] = DB_NAME

    cloudinary.config( 
        cloud_name = CLOUDINARY_CLOUD_NAME, 
        api_key = CLOUDINARY_API_KEY, 
        api_secret = CLOUDINARY_API_SECRET,
        secure=True 
        )

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
