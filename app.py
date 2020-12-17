from flask import Flask, render_template, request, redirect, session, flash, url_for
import re
from sql.connection import getUserLogin, getAllUsers,createUser, deleteUser, getUser, setUser
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'


@app.route('/')
@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/checkLogin', methods=['POST',])
def checkLogin():
    if request.method == 'POST':
        email = request.form['email']
        email = re.match(r'^[\w|\d]+@[\w]+.[\w]+(.[\w]+)', email)
        password = request.form['password']
        password = re.sub(r'[^\w | [^\d]', '', password)
        if email and password:
            if getUserLogin(email.string, password):
                return redirect(url_for("files"))
            else:
                return render_template('login.html', invalid='d-block text-danger mb-3',
                                       messanger='Usuário ou senha Incorreto')
        else:
            return render_template('login.html', invalid='d-block text-danger mb-3', messanger='Dados Invalidos')


@app.route('/files')
def files():
    files = os.listdir('C:/')
    listFiles = []
    for file in files:
        tupleFile = (file, file)
        listFiles.append(tupleFile)
    return render_template("content.html", contents=listFiles)

@app.route('/users')
def users():
    users = getAllUsers()
    return render_template("content.html", contents=users)

@app.route('/delete/<int:id>', methods=('GET', 'POST'))
def delete(id):
    result = deleteUser(id)
    if result:
        return redirect(url_for("users"))

@app.route('/addUser', methods=['POST',])
def addUser():
    if request.method == 'POST':
        email = request.form['email']
        email = re.match(r'^[\w|\d]+@[\w]+.[\w]+(.[\w]+)', email)
        password = request.form['password']
        password = re.sub(r'[^\w | [^\d]', '', password)
        if email and password:
            if createUser(email.string, password):
                return redirect(url_for("users"))
            else:
                return render_template('content.html', invalid='d-block text-danger mb-3',
                                       messanger='Usuário ou senha Incorreto')
        else:
            return render_template('content.html', invalid='d-block text-danger mb-3', messanger='Dados Invalidos')


@app.route('/listUser/<int:id>')
def listUser(id):
    if id != None:
        user = getUser(id)
        return render_template("form.html", contents=user)
    else:
        return render_template('content.html', invalid='d-block text-danger mb-3', messanger='Erro ao obter dados do usuario')

@app.route('/update', methods=['POST'])
def updateUser():
    if request.method == 'POST':
        email = request.form['email']
        email = re.match(r'^[\w|\d]+@[\w]+.[\w]+(.[\w]+)', email)
        id = request.form['id']
        id = re.match(r'[\d]+', id)
        password = request.form['password']
        password = re.sub(r'[^\w | [^\d]', '', password)
        if email and password:
            if setUser(email.string, password, id.string):
                return redirect(url_for("users"))
            else:
                return render_template('form.html', invalid='d-block text-danger mb-3',
                                       messanger='Erro ao inserir no banco, tente novamente')
        else:
            return render_template('form.html', invalid='d-block text-danger mb-3', messanger='Dados Invalidos')

if __name__ == '__main__':
    app.run()