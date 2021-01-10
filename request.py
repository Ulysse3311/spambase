# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 19:52:54 2021

@author: ulyss
"""

import requests
import json



def send_request(data):
    j_data = json.dumps(data)
    print("SENDING :\n",j_data)
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, data=j_data, headers=headers)
    print("ANSWER :\n",r, r.text)

def send_zeros(): #send a vector of 0
    line = [[0] * 57]
    data = [1, line]
    send_request(data)

def send_first_mail(): #send the first line from the dataset, it should be labeled as a spam (1)
    line = [[  0.,   1.,   1.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
         1.,   0.,   0.,   0.,   0.,   0.,   1.,   2.,   0.,   1.,   0.,
         0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
         0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
         0.,   0.,   0.,   0.,   0.,   0.,   0.,   1.,   0.,   0.,   4.,
        61., 278.]]
    data=[1,line]
    send_request(data)

def send_raw_emails():
    email1 = "You have won 1 000 000 dollars, please send your address !"
    email2= "Hello George, How are you ?"
    line =[email1,email2]
    data=[0,line]
    send_request(data)

if __name__=="__main__":
    url = 'http://127.0.0.1:5000/api'
    input("\nPress ENTER to launch the first request (vector of 0)")
    send_zeros()
    input("\nPress ENTER to launch the next request (first line from the dataset)")
    send_first_mail()
    input("\nPress ENTER to launch the last request (2 emails)")
    send_raw_emails()
    print ("\nEnd of demo requests, press ENTER to exit")

