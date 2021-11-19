from flask import Flask, session, redirect
from app import app
from estado.models import Estado

# Rotas dos estados
@app.route('/estados/pobres')
def estadosPobres():
    if 'logado' in session:
        return Estado().listarPobres()
    else:
        return redirect('/nao-logado')

@app.route('/estados/ricos')
def estadosRicos():
    if 'logado' in session:
        return Estado().listarRicos()
    else:
        return redirect('/nao-logado')