# Initalize all here the blueprints which contains the routes and connect the configurations here

from flask import Flask
# from flask_mysql_connector import MySQL
# from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY

app = Flask(__name__)

def create_app():
    #app.config.from_object(config)

    from app.routes.home_bp import home_bp
    app.register_blueprint(home_bp)

    return app
