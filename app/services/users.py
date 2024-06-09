from app.errors import NotFoundError
from app.models import User


def get_user_by_email(email: str, silent: bool = True):
    user = User.query.filter_by(email=email).first()
    if not silent and not user:
        raise NotFoundError()
    return user


def get_user_by_id(user_id: int, silent: bool = True):
    user = User.query.get(ident=user_id)
    if not silent and not user:
        raise NotFoundError()
    return user
