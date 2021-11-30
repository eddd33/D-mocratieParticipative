from flask import Flask
from flask import render_template
app=Flask(__name__)
@app.route('/')
def initial():
    return render_template('login.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/citoyen')
def citoyen():
    return render_template('citoyen.html',methods=["POST","GET"])
@app.route('/elu')
def elu():
    return render_template('elu.html')

