import pickle
from flask import Flask, render_template, url_for, request, app, jsonify
import numpy as np
import pandas as pd

app = Flask(__name__)

## Loading the model and Scaler:
reg_model = pickle.load(open('reg_model.pkl','rb'))
reg_scaler = pickle.load(open('scaling.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def prediction_api():
    data = request.json['data']
    print(data) 
    print(np.array(list(data.values)).reshape(1,-1))
    new_data = reg_scaler.transform(np.array(list(data.values)).reshape(1,-1))
    output = regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

if __name__=='__main__':
    app.run(debug=True)