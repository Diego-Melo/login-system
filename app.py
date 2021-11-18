from flask import Flask, render_template, url_for
import pymongo
app = Flask(__name__, template_folder='./templates')

client = pymongo.MongoClient('localhost',27017)
db = client.login

from user import routes
@app.route('/')
def home():
    return render_template('login.html')


# if (__name__=="__main__"):
#     app.run(host='0.0.0.0', port=80)