from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

 
    # Registrar rutas generales
    with app.app_context():
        from . import routes
        from . import db
        from .models import User
    db.init_app(app)

    migrate.init_app(app, db)

    # Registrar Blueprints aquí
    from app.controllers.user_controller import user_bp
    app.register_blueprint(user_bp, url_prefix='/api/v1/users')
    
    return app

