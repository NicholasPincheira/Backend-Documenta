from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Registrar rutas generales
    with app.app_context():
        from . import routes
        from . import db
        from .models import User, Documentation, DocumentationLang  
    from flask_jwt_extended import jwt_required
       
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    # inicializar admin
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    
    # Configurar Flask-Admin
    admin = Admin(app, name='Admin Panel', template_mode='bootstrap3')
    
    # Registrar vistas de modelos con AdminModelView
    admin.add_view(AdminModelView(User, db.session))
    admin.add_view(AdminModelView(Documentation, db.session))
    admin.add_view(AdminModelView(DocumentationLang, db.session))
    

    # Registrar Blueprints aquí
    from app.controllers.user_controller import user_bp
    app.register_blueprint(user_bp, url_prefix='/api/v1/users')
    from .controllers.documentation_controller import documentation_bp
    app.register_blueprint(documentation_bp, url_prefix='/api/v1')
    from .controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')

    return app

