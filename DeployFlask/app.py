import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)

pkl_file_path = "/Users/ervinballa/Desktop/UNYT/Year 3/Senior Project/ML_Grad/footy/model56.pkl"  #filepath of your pkl file 
modelx = pickle.load(open(pkl_file_path, 'rb'))
model = pickle.load(open("/Users/ervinballa/Desktop/UNYT/Year 3/Senior Project/ML_Grad/footy/model56.pkl", 'rb'))
print(type(model))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='The Market Value is estimated to be € {}'.format(output))


@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
