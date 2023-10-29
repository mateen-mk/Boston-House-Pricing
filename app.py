import pickle as pkl
import pandas as pd
import numpy as np
from Flask import Flask,request,app,jsonify, url_for, render_template

app = Flask(__name__)
regmodel = pkl.load(open('regmodel.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods = ['POST'])