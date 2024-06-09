from http import HTTPStatus

from flasgger import swag_from
from flask import Blueprint, request
from werkzeug.security import check_password_hash

from app.errors import UnauthorizedError
from app.schemas.auth import AccessTokenSchema, UserLoginSchema, RegisterSchema
from app.services.auth import create_auth_tokens, login_user, register_user
from app.services.users import get_user_by_email

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=['post'])
@swag_from('../apidoc/auth/login.yaml')
def login():
    data = UserLoginSchema().load(request.json)
    user = get_user_by_email(data['email'])

    if not user or not check_password_hash(user.password, data['password']):
        raise UnauthorizedError(message='Wrong email or password.')

    access_token, refresh_token = login_user(user=user)

    return AccessTokenSchema().dump({'access_token': access_token, 'refresh_token': refresh_token}), HTTPStatus.OK


@bp.route("/register", methods=["post"])
@swag_from('../apidoc/auth/register.yaml')
def register():
    data = RegisterSchema().load(request.json)
    user = get_user_by_email(data['email'])

    if user:
        raise UnauthorizedError(message='User already exists.')

    register_user(data)

    return {'message': 'The user created successfully'}, HTTPStatus.CREATED
