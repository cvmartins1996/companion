from flask import Flask, render_template, request
from wtforms import Form, StringField, TextAreaField, PasswordField
from flask_pymongo import PyMongo, MongoClient

app = Flask(__name__)
##app.config['MONGO_DBNAME'] = 'companion'
##app.config['MONGO_URI'] = 'mongodb://cvmartins:teste1234@ds139645.mlab.com:39645/companion'

HOST = 'localhost'
PORT = 27017

client = MongoClient(HOST, PORT)
db = client.companion
users = db.users

class RegisterForm(Form):
    nome = StringField('Nome')


@app.route("/")
def home():
    return render_template("home.html", everyUser = users.find({}))

@app.route("/usuario")
def inserir():
    form = RegisterForm(request.form)
    
    if request.method == 'POST':
    
        nome = form.nome.data
        user = nome
        users.insert(user)

    return render_template("usuario.html")

if __name__ == '__main__':
    app.run(debug=True)