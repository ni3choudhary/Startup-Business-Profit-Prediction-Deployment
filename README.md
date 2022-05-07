# Startup-Business-Profit-Prediction-Deployment

[![Kaggle](https://img.shields.io/badge/Dataset-Kaggle-blue.svg)](https://www.kaggle.com/datasets/farhanmd29/50-startups?datasetId=21716&sortBy=dateRun&tab=profile) ![Python 3.6](https://img.shields.io/badge/Python-3.6-brightgreen.svg)

• This repository consists of files required for end to end implementation of Startup Business Profit Prediction ___Machine Learning Web App___ created with ___Flask___ on ___Heroku___ platform.

### Problem statement:
A ML project with EDA and model that helps in predicting the startup business profit in New York, California and Florida.

### Dataset
You can find the dataset [here.](https://www.kaggle.com/datasets/farhanmd29/50-startups?datasetId=21716&sortBy=dateRun&tab=profile)

### Dependencies:
* Python 
* Scikit-Learn
* Pandas
* Numpy
* Matplotlib
* Seaborn
* Flask 

## setup
To create a project from scratch use following steps - -

- Clone the repository : https://github.com/ni3choudhary/Startup-Business-Profit-Prediction-Deployment.git
- Inside the project root directory, Create Python Virtual Environment using below command.
```console
$ python3 -m venv env
``` 

Activate Virtual Environment
```console
$ .env/bin/activate 
          OR
$ .\env\Scripts\activate
```
Install Libraries using below command
```console
$ pip install -r requirements.txt
```
- Run jupyter notebook to get the pickle files

- Copy both pickle files and create a folder **models** inside **flask-app** directory and paste both the pickle files.

- Inside the **flask-app** directory run app.py on terminal to start local server.
```console
$ python app.py
```

• If you want to view the deployed model, click on the following link: Deployed at: https://start-up-app-profit-prediction.herokuapp.com/

• Please do ⭐ the repository, if it helped you in anyway.
