# Entreprise "Prêt à Dépenser" - Mise en place d'un modèle de scoring

## Objectifs du projet
L’entreprise souhaite mettre en œuvre un outil de “scoring crédit” pour calculer la probabilité qu’un client rembourse son crédit, puis classifie la demande en crédit accordé ou refusé. Elle souhaite donc développer un algorithme de classification en s’appuyant sur des sources de données variées (données comportementales, données provenant d'autres institutions financières, etc.).

De plus, les chargés de relation client ont fait remonter le fait que les clients sont de plus en plus demandeurs de transparence vis-à-vis des décisions d’octroi de crédit. Cette demande de transparence des clients va tout à fait dans le sens des valeurs que l’entreprise veut incarner.

L'objectif est donc de développer un dashboard interactif pour que les chargés de relation client puissent à la fois expliquer de façon la plus transparente possible les décisions d’octroi de crédit, mais également permettre à leurs clients de disposer de leurs informations personnelles et de les explorer facilement. 

## Données et missions :
Les données anonymisées de clients peuvent être téléchargées automatiquement depuis le notebook projet7.ipynb. Elles regroupent leurs informations ainsi que, lorsque c'est possible, l'information de remboursement ou non du prêt, utile pour entrainer un modèle de classification.

Il y a 3 missions principales :
 
- Construire un modèle de scoring qui donnera une prédiction sur la probabilité de faillite d'un client de façon automatique.
- Construire un dashboard interactif à destination des gestionnaires de la relation client permettant d'interpréter les prédictions faites par le modèle, et d’améliorer la connaissance client des chargés de relation client.
- Mettre en production le modèle de scoring de prédiction à l’aide d’une API, ainsi que le dashboard interactif qui appelle l’API pour les prédictions.

## Dossiers / fichiers

- app.py : Fichier python avec l'API renvoyant les résultats de prédiction et prenant en entrée le / les individus à tester
- dashboard.py : Fichier python générant un dashboard avec Streamlit qui permet d'entrer les caractéristiques du client, faire la prédiction / l'estimation et renvoyer les résultats sous forme lisible et interprétable simplement. Une seconde partie permet de visualiser les caractéristiques du client à évaluer par rapport aux clients précédents afin de comprendre plus en détail les résultats du modèle.
- projet7.ipynb : Notebook jupyter d'exploration des données et sélection de features pour entrainement du modèle.
- projet7_MLFlow.ipynb : Notebook jupyter utilisant les données finales du notebook projet7.ipynb pour tester plusieurs modèles différents, mesurer leurs performances et stockage des modèles. Le modèle sélectionné et le scaler adapté aux données sont sauvegardés dans le dossier "pipeline". 
- test_unit.py : Tests unitaires sur l'API

## Packages utilisés :

| Package     | Num. de version |
|-------------|-----------------|
| evidently   | 0.3.2.1         |
| Flask       | 2.3.2           |
| matplotlib  | 3.6.0           |
| mlflow      | 2.3.2           |
| numpy       | 1.23.4          |
| pandas      | 1.5.1           | 
| requests    | 2.31.0          |
| scikit-learn| 1.1.2           |
| scipy       | 1.9.3           |
| seaborn     | 0.12.1          |
| shap        | 0.41.0          |
| streamlit   | 1.9             |

