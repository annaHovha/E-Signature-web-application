from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug.security import generate_password_hash

from app.models import User


def create_auth_tokens(user_id: int) -> {str, str}:
    access_token = create_access_token(identity=user_id)
    refresh_token = create_refresh_token(identity=user_id)

    return access_token, refresh_token


def login_user(user):
    return create_auth_tokens(user_id=user.id)


def register_user(data):
    user = User.create(
        email=data['email'],
        password=generate_password_hash(data['password']),
        first_name=data['first_name'],
        last_name=data['last_name'],
    )
    user.save()

    return user
