## spambase
Classification of spam emails using Python on the Spambase Data Set. <br>
Final project for the Python For Data Analysis at ESILV <br>
In collaboration with Tristan Darrigol (https://github.com/UnicornRules) <br>
<br>
#### To take a look at  the assignment : devoir_python_for_data_analysis.pdf
#### To have a quick overview of the project : SpamBase_Berthet_Darrigol.pdf
#### To see our data exploration : data_exploration.ipynb
#### To see how we build the model : data_classification.ipynb

## Dataset :
data from https://archive.ics.uci.edu/ml/datasets/Spambase
* Task : classification of spam emails (2 class)
* Number of attributes : 57
* Attributes type : float
* Number of instances : 4601

## Machine Learning solution :
  We chose precision as our main metrics, in order to optimize our "positive" prediction 
  <br>
  We then tried 10 differents models, and then focused on : 
  * Random Forest Classifier
  * Gradient Boosting Classifier
  * Adaptative Boosting Classifier
  * Support Vector Machine Classifier
  <br>
  Before tuning the best precision we had was of 96.6%
  <br>
  After tuning, we obtained a precision of 99% using Random Forest Classifier

## How to set it up
* download : api.py, finalized_model.zip (and unzip), venv, request.py
* open a termimal and go to the directory 
* run the virtual env, type in the termimal : `venv\Scripts\activate`
* run the api, type in the terminal : `python api.py` , the api is now running on http://127.0.0.1:5000/
* to test sample request to the api, run in another terminal :  `python request.py`
