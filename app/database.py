from sqlalchemy.orm import Query
from sqlalchemy import func

from app.extensions.database import db


class CRUDMixin(object):

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)  # noqa
        return instance.save()

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        return commit and db.session.commit()


class TimestampMixin(object):
    created_at = db.Column(db.TIMESTAMP, server_default=func.now())
    updated_at = db.Column(db.TIMESTAMP, onupdate=func.now())


class Model(db.Model, CRUDMixin):
    __abstract__ = True

    query: Query


class PkModel(Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
