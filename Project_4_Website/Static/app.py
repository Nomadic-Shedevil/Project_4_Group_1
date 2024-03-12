#import libraries
import numpy as np
import pandas as pd
from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

model_path = 'rf_model_optimized.pkl'
ohe_model = 'ohe_model.pkl'

with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)
   
with open(ohe_model, 'rb') as model_file_2: 
    model_2 = pickle.load(model_file_2)

# with open(ohe_model, 'rb') as model_file_2: 
    # model_2 = pickle.load(model_file_2)

# make a function
def function(data):
    columns = ['cap-shape',	'gill-spacing',	'gill-color', 'stalk-shape', 'stalk-root', 
               'stalk-color-below-ring','ring-type', 'spore-print-color','population','habitat']
    
    input_df = pd.DataFrame([dict(zip(columns, data))])

# 1. convert raw input into transformed/ encoded as your X-train
    one_hot_encoded_df =  pd.DataFrame(model_2.transform(input_df[columns]), columns=model_2.get_feature_names_out())

# 2. test your function => 1, 0
    prediction = model.predict(one_hot_encoded_df)
    return prediction


#default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/predict', methods=['POST'])
def predict():

    capshape_val = request.form.get('cap-shape')
    gillspace_val = request.form.get("gill-spacing")
    gillcolor_val = request.form.get("gill-color")
    stalkshape_val = request.form.get("stalk-shape")
    stalkroot_val = request.form.get("stalk-root")
    stalkcolorbelowring_val = request.form.get("stalk-color-below-ring")
    ring_val = request.form.get("ring-type")
    sporeprint_val = request.form.get("spore-print-color")
    population_val = request.form.get("population")
    habitat_val = request.form.get("habitat")

    data = [capshape_val, gillspace_val, gillcolor_val, stalkshape_val, stalkroot_val, stalkcolorbelowring_val, ring_val, sporeprint_val,population_val, habitat_val]
        
        
    app.logger.info(data)
    my_prediction = function(data)

    # my_prediction = model_3.inverse_transform(np.reshape(my_prediction, (-1,1)))  

    prediction = 'Poisionous' if my_prediction == '1' else 'Edible'            
                              
    app.logger.info(f' this is pred :: {my_prediction}')

    return (render_template('index.html', prediction = f'This Mushrom is: {prediction}'))

if __name__ == '__main__':
    app.run(debug=True)
