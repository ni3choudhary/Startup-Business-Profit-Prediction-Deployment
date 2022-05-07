# Importing essential libraries
from flask import Flask, request, render_template
import pickle
import json
import numpy as np


app = Flask(__name__)

def predict_startup_profit(r_d_expenses, administration_expenses, marketing_expenses, state):
    """
    * method: get_predict_profit
    * description: method to predict the results
    * return: prediction result
    
    * Parameters
    *   r_d_expenses: R&D spent
    *   administration_expenses: admin cost
    *   marketing_expenses: marketing expenses
    *   state: state name
    """

    # Load the Linear Regression model
    with open('models/startp_profit_prediction_lr_model.pkl', 'rb') as f:
        model = pickle.load(f)

    # Load columns list saved as json file
    with open("models/columns.json", "r") as f:
        data_columns = json.load(f)['data_columns']


    try:
        state_index = data_columns.index('state_'+str(state).lower())
    except:
        state_index = -1

    x = np.zeros(len(data_columns))
    x[0] = r_d_expenses
    x[1] = administration_expenses
    x[2] = marketing_expenses
    if state_index >= 0:
        x[state_index] = 1

    return round(model.predict([x])[0],2)

@app.route('/')
def index_page():
    """
    * method: index_page
    * description: method to call index html page
    * return: index.html
    """
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    """
    * method: predict
    * description: method to predict
    * return: result.html
    """
    if request.method == 'POST':
        r_d_expenses = request.form['r_d_expenses']
        administration_expenses = request.form["administration_expenses"]
        marketing_expenses = request.form["marketing_expenses"]
        state = request.form["state"]
        output = predict_startup_profit(r_d_expenses, administration_expenses, marketing_expenses, state)
        return render_template('result.html',show_hidden=True, prediction_text='Startup Business Profit must be ${}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)