from flask import Flask, render_template, url_for
import pymongo
app = Flask(__name__, template_folder='./templates')
app.secret_key = b'wr\x01\xf4\x84U0\xec\x97\xbaA\xda\xd0^\x97\xab'
client = pymongo.MongoClient('localhost',27017)
db = client.login

from user import routes
@app.route('/')
def home():
    return render_template('login.html')


# if (__name__=="__main__"):
#     app.run(host='0.0.0.0', port=80)