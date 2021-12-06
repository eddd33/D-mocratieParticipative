from flask import Flask
from flask import render_template
from flask import redirect
app=Flask(__name__)
@app.route('/')
def initial():
    return redirect("/login")
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/citoyen')
def citoyen():
    return render_template('citoyen.html',methods=["POST","GET"])
@app.route('/elu')
def elu():
    return render_template('elu.html')
@app.route('/accueil_c')
def accueil_c():
    return render_template('accueil_c.html')
@app.route('/accueil_e')
def accueil_e():
    return render_template('accueil_e.html')
@app.route('/reponse')
def reponse():
    return render_template('login.html',methods=["POST","GET"])
@app.route('/inscriptcit')
def inscriptcit():
    return render_template('inscriptcit.html')
