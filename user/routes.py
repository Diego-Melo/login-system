from flask import Flask
from app import app 
from user.models import Usuarios

@app.route('/usuario/')
def sair():
    # return 'oi'
    return Usuarios().sair()

@app.route('/logar', methods=['POST'])
def logar():
    return Usuarios().logar()