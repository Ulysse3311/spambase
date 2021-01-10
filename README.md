## spambase
Classification of spam emails using Python on the Spambase Data Set. <br>
Final project for the Python For Data Analysis at ESILV <br>
In collaboration with Tristan Darrigol (https://github.com/UnicornRules) <br>
<br>
#### To have a quick overview of the project : SPAMBASE.pdf
#### To see our data exploration : data_exploration.ipynb
#### To see how we build the model : data_classification.ipynb

## Dataset :
data from https://archive.ics.uci.edu/ml/datasets/Spambase
* Task : classification of spam emails (2 class)
* Number of attributes : 57
* Attributes type : float
* Number of instances : 4601

## Machine Learning solution :


## How to set it up
* download : api.py, finalized_model.zip (and unzip), venv, request.py
* open a termimal and go to the directory 
* run the virtual env, type in the termimal : `venv\Scripts\activate`
* run the api, type in the terminal : `python api.py` , the api is now running on http://127.0.0.1:5000/
* to test sample request to the api, run in another terminal :  `python request.py`
