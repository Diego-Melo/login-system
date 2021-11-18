from flask import Flask, render_template
from app import app 
from user.models import Usuarios

@app.route('/sair/')
def sair():
    # return 'oi'
    return Usuarios().sair()

@app.route('/logar', methods=['POST'])
def logar():
    return Usuarios().logar()

@app.route('/nao-logado')
def naologado():
    return render_template('naologado.html')