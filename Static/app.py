from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

model_path = '../rf_model.pkl'
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form
    form_data = [int(data[attribute]) for attribute in data]
    prediction = model.predict([form_data])[0]
    result = 'Edible' if prediction == 0 else 'Poisonous'
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
