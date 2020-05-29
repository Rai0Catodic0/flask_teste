'''modelos da API'''
from peewee import Model, SqliteDatabase, CharField

DB = SqliteDatabase('flask-api.db')

class User(Model):
    first_name = CharField()
    last_name = CharField()
    password = CharField()
    email = CharField()

    def __eq__(self,other):
        return self == other

    def autenticate(self, password):
        if self.password == password:
            return True
        return False

    def __repr__(self):
        return f'{self.first_name} {self.last_name} \n{self.password} \n{self.email}'
    class Meta:
        database = DB
