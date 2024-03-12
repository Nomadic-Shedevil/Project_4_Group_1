from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

model_path = 'rf_model_optimized.pkl'
ohe_model = 'ohe_model.pkl'

with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)
   
with open(ohe_model, 'rb') as model_file_2: 
    model_2 = pickle.load(model_file_2)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract form data
    # Your code to extract form data
    
    # Make prediction
    # Your code to make prediction

    # Format prediction result
    result = 'Edible' if prediction == 0 else 'Poisonous'
    
    # Generate summary
    summary = 'Your summary goes here'

    # Render template with prediction result and summary
    return render_template('index.html', prediction_text='Mushroom is: {}'.format(result), summary=summary)

if __name__ == '__main__':
    app.run(debug=True)