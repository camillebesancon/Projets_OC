import unittest
import requests
import json
import pandas as pd
import numpy as np

class TestAPI(unittest.TestCase):

    colnames= ['EXT_SOURCE_3', 'EXT_SOURCE_2', 'DAYS_ID_PUBLISH', 'DAYS_REGISTRATION', 'DAYS_LAST_PHONE_CHANGE', 'REGION_POPULATION_RELATIVE', 'AMT_INCOME_TOTAL', 'HOUR_APPR_PROCESS_START', 'AMT_REQ_CREDIT_BUREAU_YEAR', 'CODE_GENDER']
    values=[0.60927566738944, 0.588927250125261, -1247, -13169, -1626, 0.00702, 157500, 10, 2, 0]
    data_v=pd.DataFrame(values, index=colnames).transpose()


    data_v=pd.read_csv('final_data/df_train.csv', sep=',').drop(columns=['Unnamed: 0','TARGET']).sample(1)

    data_v_j=data_v.copy().to_json()

    def setUp(self):
        # SEt up de l'API
        self.api_url = 'http://ec2-51-20-104-253.eu-north-1.compute.amazonaws.com:5000/home/ubuntu/Projet7_OC'
       # self.api_url='http://172.31.29.100:5000'
        self.headers = {'Content-Type': 'application/json'}

    def test_endpoint_reachable(self):
        '''
        Test unitaire, API joignable pour requêtes
        '''
        print("Testing endpoint:")
        response = requests.post(self.api_url, json=self.data_v_j)
        print("ALED JPP"*30, response.status_code)
        self.assertEqual(response.status_code, 200)

    def test_valid_prediction(self):
        '''
        Test unitaire résultat de prédiction conformes
        '''
        print("Testing validity of restults:")
        response = requests.post(self.api_url, json=self.data_v_j)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertTrue('predictions' in response_data)
        predictions = response_data['predictions']
        self.assertIsInstance(predictions, list) # resultats sous forme de liste
        for predi in predictions:
            for elem in predi:
                self.assertTrue(isinstance(elem, (int,float))) # Resultats = nombres

    def test_invalid_prediction(self):
        '''
        Test unitaire de prédiction invalide si valeur incorrecte
        '''
        print("Testing invalid request")
        data_inv=self.data_v.copy()
        data_inv.iloc[0,4]="texte"
        response = requests.post(self.api_url, json=data_inv.copy().to_json())
        print("AAA"*60)
        print(response)
        self.assertEqual(response.status_code, 400)
        self.assertTrue('error' in response.json())

if __name__ == '__main__':
    unittest.main()

