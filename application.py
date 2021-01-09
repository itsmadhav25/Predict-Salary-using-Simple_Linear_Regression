# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 10:25:03 2021

@author: madhv
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

flask_app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@flask_app.route('/')
def home():
    return render_template('index.html')

@flask_app.route('/predict',methods=['POST'])
def predict():
    ''' For rendering results on HTML GUI '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Employee Salary should be RS {}'.format(output))

@flask_app.route('/predict_api',methods=['POST'])
def predict_api():
    ''' For direct API calls trought request '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    flask_app.run(debug=True)