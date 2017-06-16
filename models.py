from peewee import *
from playhouse.postgres_ext import *

db = PostgresqlExtDatabase('osm', user='osm', password='osm')

class BaseExtModel(Model):
    class Meta:
        database = db

class holidays(BaseExtModel):
#    __tablename__ = 'holidays'

    termin = DateField()
    opis = CharField(100)
    wariant = CharField(2)
    id = PrimaryKeyField()


class pociagi(BaseExtModel):
#    __tablename__ = 'pociagi'

    plan = CharField(4)
    obieg = CharField(2)
    nr_poc = CharField(7)
    termin = ArrayField(DateField)
    wyklucz = ArrayField(DateField)
    dolacz = ArrayField(DateField)
    wariant = CharField(2)
    st_pocz = CharField(40)
    st_konc = CharField(40)
    godz_pocz = TimeField()
    godz_konc = TimeField()
    tabor = CharField(10)
    id = PrimaryKeyField()


class users(BaseExtModel):
#    __tablename__ = 'users'

    user_id = PrimaryKeyField()
    user_name = CharField(6)
    user_username = CharField(45)
    user_password = CharField(45)
