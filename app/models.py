from app.database import PkModel, TimestampMixin
from app.extensions.database import db


class User(PkModel, TimestampMixin):
    __tablename__ = 'users'

    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'<User {self.email}>'
