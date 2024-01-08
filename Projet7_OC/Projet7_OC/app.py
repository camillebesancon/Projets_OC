import pickle
import pandas as pd
from flask import Flask, request, jsonify
import mlflow
import smtplib

app = Flask(__name__)

with open('pipeline/pipeline.pkl', 'rb') as file:
    modele_mlflow = pickle.load(file)

@app.route('/home/ubuntu/Projet7_OC/', methods=['POST'])
def predict():
    try:
        # Récupérer les données de la requête POST
        data = request.get_json()

        df = pd.read_json(data)

            # Log inputs

        predictions = modele_mlflow.predict_proba(df).tolist() # from ndarray -> list 
        return jsonify({'predictions': predictions})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


