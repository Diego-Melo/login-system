from flask import Flask
from app import app
from estado.models import Estado

@app.route('/estados/pobres')
def estadosPobres():
    return Estado().listarPobres()

@app.route('/estados/ricos')
def estadosRicos():
    return Estado().listarRicos()