from peewee import *
from playhouse.postgres_ext import *

db = PostgresqlExtDatabase('ks', user='osm', password='osm')

class BaseExtModel(Model):
    class Meta:
        database = db
        db_schema = 'grafik'

class holidays(BaseExtModel):

	termin = DateField()
	opis = CharField(100)
	wariant = CharField(2)
	id = PrimaryKeyField()


class pociagi(BaseExtModel):

    plan = CharField(6)
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

class sluzby(BaseExtModel):

    plan = CharField(6)
    godz_pocz = TimeField()
    godz_konc = TimeField()
    st_pocz = CharField(40)
    termin = ArrayField(DateField)
    wariant = CharField(2)
    id = PrimaryKeyField()

class users(BaseExtModel):

    user_id = PrimaryKeyField()
    user_name = CharField(6)
    user_username = CharField(45)
    user_password = CharField(45)
