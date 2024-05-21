# pip install flask
from flask import Flask, jsonify, request
from utilities import predict_pipeline

app = Flask(__name__)

@app.post('/predict') # post request
def predict():
    data = request.json # get data input from user
    # foolproof this
    try:
        sample = data['text']
    except KeyError: #tried accessing key not on dict
        return jsonify({'error':'No  text sent'})
    # ensure text is in a list
    sample = [sample]
    # run model pipeline
    predictions = predict_pipeline(sample)
    # one more error checking
    try:
        result = jsonify(predictions[0])
    except TypeError as e:
        return jsonify({'error':str(e)})
    # return actual result if no errors
    return result

# run if main
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)