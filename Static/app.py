from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained Random Forest model
model_path = '../rf_model.pkl'  
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        # Extract and prepare form data for prediction
        form_data = [int(request.form[attribute]) for attribute in request.form]
        prediction = model.predict([form_data])[0]
        # Translate prediction into human-readable format
        prediction_text = 'Edible' if prediction == 0 else 'Poisonous'
    else:
        prediction_text = None

    return render_template('index.html', prediction=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)
