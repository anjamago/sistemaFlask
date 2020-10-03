from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask_migrate import Migrate
from flask_mail import Mail

login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
mail = Mail()


def create_app(settings_module):

    app = Flask(__name__)
    app.config.from_object(settings_module)
    app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://girhxuamacdmjr:b9117f7402c6ab1b7a8f0dc6a8ac048561f0de32a66f2d41c92883b8b1f8bbdd@ec2-23-23-36-227.compute-1.amazonaws.com:5432/d6lrqppsaj7t0b'
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    # Registro de los Blueprints

    from .Auth import auth_bp
    app.register_blueprint(auth_bp)


    return app