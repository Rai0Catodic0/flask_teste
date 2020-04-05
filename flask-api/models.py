'''modelos da API'''
from peewee import *

DB = SqliteDatabase('flask-api.db')

class User(Model):
    first_name = CharField()
    last_name = CharField()
    password = CharField()
    email = CharField()

    class Meta:
        database = DB
