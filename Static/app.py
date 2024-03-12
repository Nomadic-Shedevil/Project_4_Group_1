#import libraries
from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

model_path = 'rf_model_optimized.pkl'
ohe_model = 'ohe_model.pkl'

with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)
   
with open(ohe_model, 'rb') as model_file_2: 
    model_2 = pickle.load(model_file_2)

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

        data = [capshape_val, gillspace_val, gillcolor_val, stalkshape_val, stalkroot_val, stalkcolorbelowring_val, ring_val, sporeprint_val, 
            population_val, habitat_val]

     #For rendering results on HTML GUI
        form_data = [float(x) for x in request.form.values()]
        final_features = [np.array(form_data)]
        transformed_features = model_2.transform(final_features)
        prediction = model.predict(transformed_features)
        result = 'Edible' if prediction == 0 else 'Poisonous'
        return render_template('index.html', prediction_text='Mushroom is :{}'.format(result))


if __name__ == '__main__':
    app.run(debug=True)