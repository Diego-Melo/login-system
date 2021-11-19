from flask import Flask, render_template, request
from app import app 
from user.models import Usuarios

# Rotas de usuário
@app.route('/sair/')
def sair():
    return Usuarios().sair()

@app.route('/logar', methods=['POST'])
def logar():
    return Usuarios().logar()

@app.route('/nao-logado')
def naologado():
    return render_template('naoLogado.html')

@app.route('/cadastrar', methods=['POST', 'GET'])
def cadastrar():
    if request.method == 'POST':
        return Usuarios().cadastrar()
    else:
        return render_template('cadastrar.html')