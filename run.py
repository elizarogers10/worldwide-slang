from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/expressions')
def expresssions():
    return render_template('expressions.html')

@app.route('/Objects')
def Objects():
    return render_template('Objects.html')

@app.route('/Sayings')
def Sayings():
    return render_template('Sayings.html')

@app.route('/R18')
def R18():
    return render_template('R18.html')
