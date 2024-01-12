from app import app
from flask import render_template, request, flash, redirect

nome = "Zeh Hey"
dados = {'Profissão': 'Desenvolvedor', 'Redes': '@zeh_hey'}

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html', nome=nome, dados=dados)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    if usuario == 'admin' and senha == '0000':
        return f'Usuário {usuario} e senha {senha}'
    else:
        flash('Dados invalidos')
        return redirect('/login')
    