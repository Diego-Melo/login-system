from flask import Flask, render_template, url_for, session, redirect
import pymongo

app = Flask(__name__, template_folder='./templates')
# Configura a chave secreta usada na sessão
app.secret_key = b'wr\x01\xf4\x84U0\xec\x97\xbaA\xda\xd0^\x97\xab'

# Conexão com o banco de dados
client = pymongo.MongoClient('localhost',27017)
db = client.login

# Rotas
from estado import routes
from user import routes

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'logado' in session:
        return render_template('dashboard.html')
    else:
        return redirect('/')
    
if (__name__=="__main__"):
    app.run(host='0.0.0.0', port=80)