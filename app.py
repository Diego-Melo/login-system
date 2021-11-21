from flask import Flask, render_template, url_for, session, redirect
import pymongo

app = Flask(__name__, template_folder='./templates')
# Configura a chave secreta usada na sessão
app.secret_key = b'wr\x01\xf4\x84U0\xec\x97\xbaA\xda\xd0^\x97\xab'

# Conexão com o banco de dados
client = pymongo.MongoClient('localhost', 27017)
db = client.login

# Rotas
from user import routes
from estado import routes
@app.route('/')
def home():
    if 'logado' in session:
        return redirect(url_for('dashboard'))
    else:
        return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'logado' in session:
        return render_template('dashboard.html')
    else:
        return redirect('/nao-logado')

# Rotas de erro
@app.errorhandler(404)
def naoEncontrado(err):
    return render_template('erro404.html'), 404

@app.errorhandler(409)
def naoEncontrado(err):
    return render_template('erro409.html'), 409

@app.errorhandler(401)
def naoEncontrado(err):
    return render_template('erro401.html'), 401


if (__name__ == "__main__"):
    app.run(host='0.0.0.0', port=80)
    