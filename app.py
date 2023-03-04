from flask import Flask, render_template, request,jsonify
import pickle
import numpy as np
import pandas as pd

app=Flask(__name__)


model=pickle.load(open('bostonRegModel.pkl','rb'))
scalar=pickle.load(open('scaling.pkl','rb'))
@app.route('/', methods=['GET'])
def landing():
    return render_template('index.html')


@app.route('/predict-api', methods=['POST'])
def makePrediction():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    print(np.array(list(data.values())).reshape(1,-1).shape)
    new_data=scalar.transform(np.array(list(data.values())).reshape(1,-1))
    print(new_data.shape)
    output=model.predict(new_data)
    print(output[0])
    return(jsonify(output[0]))

@app.route('/predict', methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()] 
    final_input= scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=model.predict(final_input)[0]
    return render_template('index.html', predicted_value=f"The predicted Price of the house based on the entered data is {output}")

if __name__=="__main__":
    app.run(debug=True, port=5000,host='0.0.0.0')