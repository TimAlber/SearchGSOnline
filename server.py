#!/usr/bin/python

from flask import Flask, render_template,request
from data import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/nach',methods = ['POST','GET'])
def nach():
    if request.method == 'POST':
       name = searchsheet(request.form['name'])
    if name == 'Produkt is not in Database':
       return 'Sorry, that Produkt is not in out Dataase. <br> <a href="/">Back</a>'
    else:
       return render_template('nach.html', st=str(request.form['name']), name=name, nach=nach)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
