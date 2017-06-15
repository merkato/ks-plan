# coding: utf-8
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import ARRAY, Column, Date, Integer, String, Time, text
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()

Base = declarative_base()
metadata = Base.metadata


class Holiday(Base):
    __tablename__ = 'holidays'

    termin = Column(Date)
    opis = Column(String(100))
    wariant = Column(String(2))
    id = Column(Integer, primary_key=True, server_default=text("nextval('holidays_id_seq'::regclass)"))


class Pociagi(Base):
    __tablename__ = 'pociagi'

    plan = Column(String(4))
    obieg = Column(String(2))
    nr_poc = Column(String(7))
    termin = Column(ARRAY(Date()))
    wyklucz = Column(ARRAY(Date()))
    dolacz = Column(ARRAY(Date()))
    wariant = Column(String(2))
    st_pocz = Column(String(40))
    st_konc = Column(String(40))
    godz_pocz = Column(Time)
    godz_konc = Column(Time)
    tabor = Column(String(10))
    id = Column(Integer, primary_key=True, server_default=text("nextval('pociagi_id_seq'::regclass)"))


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, server_default=text("nextval('users_user_id_seq'::regclass)"))
    user_name = Column(String(6))
    user_username = Column(String(45))
    user_password = Column(String(45))
    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False
