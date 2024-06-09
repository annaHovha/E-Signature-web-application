from http import HTTPStatus

from flask_jwt_extended.exceptions import JWTExtendedException, NoAuthorizationError
from marshmallow import ValidationError


class UnauthorizedError(Exception):
    message: str = 'Unauthorized request.'

    def __init__(self, message=None):
        self.message = message or self.message


class ForbiddenError(Exception):
    message = 'Current user cannot execute this action.'


class NotFoundError(Exception):
    message = 'Requested resource was not found.'


class InvalidRequestError(Exception):
    message = 'There are some errors in your input.'


class ModelNotFoundError(Exception):
    message = 'Requested model was not found.'


def handle_validation_error(error: ValidationError):
    return {'errors': error.messages}, HTTPStatus.UNPROCESSABLE_ENTITY


def handle_unauthorized_error(error: UnauthorizedError):
    return {'error': error.message}, HTTPStatus.UNAUTHORIZED


def handle_jwt_unauthorized_error(error: NoAuthorizationError):
    return {'error': str(error)}, HTTPStatus.UNAUTHORIZED


def handle_forbidden_error(error: ForbiddenError):
    return {'error': error.message}, HTTPStatus.FORBIDDEN


def handle_not_found_error(error: NotFoundError):
    return {'error': error.message}, HTTPStatus.NOT_FOUND


def handle_invalid_request_error(error: InvalidRequestError):
    return {'errors': error.message}, HTTPStatus.BAD_REQUEST


def handle_jwt_unprocessable_entities_error(error: JWTExtendedException):
    return {'error': str(error)}, HTTPStatus.UNPROCESSABLE_ENTITY
