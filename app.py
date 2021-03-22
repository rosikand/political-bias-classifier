"""
File: app.py
------------------
This is the file used to create the Flask app and assiociated routings. 
"""

from flask import Flask, render_template, request
from pred import predict_text

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html') 

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    model_result = predict_text(text)
    return render_template('answer.html', result=model_result)
