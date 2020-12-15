from flask import Flask, render_template, request, redirect, session, flash, url_for
import re
import sqlite3

app = Flask(__name__)


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
            return redirect(url_for("files"))
        else:
            return render_template('login.html', invalid='d-block text-danger mb-3', messanger='Dados Invalidos')


@app.route('/files')
def files():
    return render_template("content.html")

if __name__ == '__main__':
    app.run()