from models import User
from random import randint
from flask import Flask
from flask import request
from werkzeug.exceptions import HTTPException
app = Flask(__name__)


def quicksort(l):
    if l:
        left = [x for x in l if x < l[0]]
        right = [x for x in l if x > l[0]]
        if len(left) > 1:
            left = quicksort(left)
        if len(right) > 1:
            right = quicksort(right)
        return left + [l[0]] * l.count(l[0]) + right
    return []

@app.route('/')
def hello_world():
    return 'hello_world'


@app.route('/numero')
def numero():
    '''retorna um  inteiro de 5 a 200'''
    inteiro = str(randint(5, 200))
    return inteiro


@app.route('/par')
def par():
    '''retorna um par entra 6 e 40'''
    inicio = request.args.get('inicio', default=6, type=int)
    fim = request.args.get('fim', default=40, type=int)
    par_ = randint(inicio, fim)
    while par%2 != 0:
        par_ = randint(inicio, fim)
    return str(par_)


@app.route('/ordenar', methods=['GET', 'POST'])
def ordenar():
    '''ordena uma lista'''
    lista = request.args.get('lista', type=str)
    lista = lista.split(',')
    for i in range(len(lista)):
        try:
            lista[i] = int(lista[i])
        except ValueError:
            return '200'
    lista = str(quicksort(lista))
    return lista

@app.route('/user', methods=['GET', 'POST'])
def add_user():
    '''adiciona usuario'''
    last_name = request.args.get('l_name', type=str)
    first_name = request.args.get('f_name', type=str)
    password = request.args.get('password', type=str)
    email = request.args.get('email', type=str)
    if email == '' or last_name == '' or first_name == '' or password == '':
        return '200'
    if '@' not in email:
        return '200'
    user = User(last_name=last_name,first_name=first_name,password=password,email=email)
    user.save()
    return f"last_name = {last_name} first_name = {first_name}, password = {password}, email = {email}"
@app.route('/login', methods=['GET', 'POST'])
def login():
    password = request.args.get('password', type=str)
    email = request.args.get('email',type=str)
    user = User.get(User.email == email)
    if user.autenticate(password) is True:
        return 'True'
    return f"{email},{password}"