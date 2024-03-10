from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)
app.secret_key = "secret key"

model_path = 'rf_model_optimized.pkl'
ohe_model = 'ohe_model.pkl'

with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)
   
with open(ohe_model, 'rb') as model_file_2: 
    model_2 = pickle.load(model_file_2)
    
@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'GET':

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

        form_data = [int(data[attribute]) for attribute in data]
        model_2.transform([form_data])
        prediction = model.predict([form_data])
        result = 'Edible' if prediction == 0 else 'Poisonous'
        return jsonify(result=result)
    
    elif request.method == 'POST':
        return render_template('template.html')
    

if __name__ == '__main__':
    app.run(debug=True)
