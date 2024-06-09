from flask import Flask
from app import errors

from app.extensions.cors import cors
from app.extensions.database import db, migrate

from app.extensions.security import jwt
from app.extensions.swagger import swagger
from app.routes.auth import bp as auth_bp
from app.routes.documents import bp as document_bp


def create_app(config_object='config.Config') -> Flask:
    app = Flask(__name__)
    app.config.from_object(obj=config_object)

    register_extensions(app=app)
    register_blueprints(app=app)
    register_error_handlers(app=app)

    return app


def register_extensions(app: Flask) -> None:
    db.init_app(app=app)
    migrate.init_app(app=app, db=db, directory='app/migrations')
    jwt.init_app(app=app)
    swagger.init_app(app=app)
    cors.init_app(app=app)


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(blueprint=auth_bp)
    app.register_blueprint(blueprint=document_bp)


def register_error_handlers(app: Flask) -> None:
    app.register_error_handler(errors.ValidationError, errors.handle_validation_error)
