# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 19:47:28 2021

@author: ulyss
"""
from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json
import re
import pandas as pd

"""
Request to the api must have the following format :
either :
data = [1,[xi]*57]
with every xi corresponding to a columns
or :
data = [0,"raw email text"]

data[0] is a flag to know if the data is a row email or a vector 
"""


app = Flask(__name__)

@app.route('/api', methods=['POST'])
def makecalc():
    data = request.get_json()
    print("incoming data : \n",data)
    line=0
    if data[0]==1 and len(data[1][0])==57:
        print("Request type : vector")
        line = data[1]
    elif data[0]==0:
        print("Request type :raw email")
        line=[conv(d,col_names) for d in data[1]]

    if line!=0:
        prediction = np.array2string(model.predict(line))
        print("pred : \n",prediction)
        return jsonify(prediction)
    else :
        print("non compatible data")

def conv(mail,columns_names,prt=False):
    vect=[]
    nb_word=len(re.findall(r'\w+',mail))
    
    #word/char freq
    mail_low=mail.lower()
    for col in columns_names[:-4]: # the last tree dont look for word/char freq
        ref=col.split("_")[2] # the columns names a in the format : word/char_freq_ref
        if ref in ["(","["]:
            ref="\\"+ref
        match_count=len(re.findall(f"({ref})",mail_low))
        if prt:
            print(ref,match_count)
        vect.append(100*match_count/nb_word)
    
    # last 3 variables
    # every sentence in capital letters
    capital =re.findall("[A-Z, ,\d,\,]{2,}",mail)
    longest=0
    sum_cap=0
    if len(capital)!=0:
        for match in capital:
            sum_cap+=len(match.replace(" ","")) # removing " " to get the total number of capital letter
            size=len(match)
            if size>longest:
                longest=size
    else :
        capital=[1]
    vect.append(sum_cap/len(capital)) # average length of uninterrupted sequences of capital letters
    vect.append(longest) # length of longest uninterrupted sequence of capital letters
    vect.append(sum_cap) # total number of capital letters in the e-mail
    
    return vect

def get_col_names():
    columns=[]
    with open("columns.txt","r") as doc:
        lines=doc.readlines()
        for line in lines :
            columns.append(line.split(":")[0])
    return columns

if __name__ == '__main__':
    modelfile = r'finalized_model.pickle'
    model = p.load(open(modelfile, 'rb'))
    col_names=get_col_names()
    app.run()
