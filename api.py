# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 19:47:28 2021

@author: ulyss
"""
from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json


app = Flask(__name__)


@app.route('/api', methods=['POST'])
def makecalc():
    data = request.get_json()
    print(data)
    prediction = [0,0,0]

    return jsonify(prediction)

if __name__ == '__main__':
    #modelfile = 'models/final_prediction.pickle'
    #model = p.load(open(modelfile, 'rb'))
    app.run()