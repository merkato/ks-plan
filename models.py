from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    def json(self):
        """
                Define a base way to jsonify models, dealing with datetime objects
        """
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }


class Pociagi(BaseModel, db.Model):
    """Model for the pociagi table"""
    __tablename__ = 'pociagi'
    id = db.Column(db.Integer, primary_key = True)
    plan = db.Column(db.String(4))
    obieg = db.Column(db.String(2))
    nr_poc = db.Column(db.String(7))
    termin = db.Column(db.DateTime)
    wyklucz = db.Column(db.DateTime)
    dolacz = db.Column(db.DateTime)
