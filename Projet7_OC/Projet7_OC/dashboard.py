import pandas as pd
import streamlit as st
import os
import matplotlib.pyplot as plt
import requests
from sklearn.preprocessing import RobustScaler
import numpy as np
import seaborn as sns

# Chargement datas
datas = pd.read_csv("final_data/df_train.csv", sep=",").drop(columns=["Unnamed: 0"])

# initialisation pour la jauge / graphique
proba = 0
plr = 100

# Input valeurs du client:
st.sidebar.header("Caractéristiques client:")
indiv_input = {}
for column in datas.drop(columns=["TARGET"]).columns:
    indiv_input[column] = st.sidebar.number_input(f"Valeur de {column} pour le client à évaluer:", value=datas[column].iloc[0])

indiv = pd.DataFrame(indiv_input, columns=datas.drop(columns=["TARGET"]).columns, index=["0"])

st.title("Dashboard d'évaluation client")

st.markdown("**Utilisation :** Entrez les caractéristiques du client dans la barre lattérale **\"Caractéristiques clients\"** puis cliquez sur le bouton \"Estimer\" ci-dessous. L'estimation de la capacité du client à rembourser le prêt s'affichera  ensuite." )
st.markdown("Les résultats sont affichés comme un pourcentage estimé de chances de rembourser le prêt.")
st.markdown("La section **\"Détails\"** aide à visualiser les caractéristiques du client évalué par rapport aux caractéristiques de l'ensemble des clients ayant remboursés ou non leurs prêts. Cela permet de comprendre quelles variables ont orienté la décision du modèle.")

########### PARTIE PREDICTION ###########

st.header("Estimation de la capacité à rembourser un prêt")

if st.button("Estimer"):
    try:

        url = 'http://ec2-51-20-104-253.eu-north-1.compute.amazonaws.com:5000/home/ubuntu/Projet7_OC'

        response = requests.post(url, json=indiv.to_json())
        result = response.json()
        proba=np.round(result['predictions'][0][0],3)
        plr=np.round(result['predictions'][0][1],3)
        # Variable pour les coordonnées polaire du graph -> sens de rotation antihoraire par défaut (cercle trigo)
        # donc en prenant la val. complémentaire (proba de résultat=1), on rétabli le sens voulu
        
        # Enregistrement des réstulats de prédiction
        indiv["PREDICTED_0"]=proba
        indiv["PREDICTED_1"]=plr
        if os.path.exists('final_data/model_outputs.csv'):
            modeloutputs=(pd.concat([pd.read_csv('final_data/model_outputs.csv', sep=','),indiv]))
            modeloutputs.to_csv(r'final_data/model_outputs.csv')
        else:
            indiv.to_csv(r'final_data/model_outputs.csv')
            

    except Exception as e:
        st.error(f"Error: {e}")

############# JAUGE ##############

    colors = ['#4dab6d', "#72c66e", "#c1da64", "#f6ee54", "#fabd57", "#f36d54", "#ee4d55"]
    # gradient de couleurs pour la jauge 

    values = [100,80,60,40,20,0]

    x_axis_vals =[0, 0.62, 1.25, 1.88, 2.51]

    fig = plt.figure(figsize=(18,13))

    ax = fig.add_subplot(projection="polar")

    ax.bar(x=[0, 0.62, 1.25, 1.88, 2.51], width=0.62, height=0.48, bottom=2,
       linewidth=3, edgecolor="white",
       color=colors, align="edge")
       
    plt.annotate("Excellente", xy=(0.18,1.98), rotation=-73, color="k", fontweight="bold", fontsize=18)
    plt.annotate("Bonne", xy=(0.95,1.97), rotation=-40, color="k", fontweight="bold", fontsize=18)
    plt.annotate("Incertaine", xy=(1.7,2.23), color="k", fontweight="bold", fontsize=18)
    plt.annotate("Mauvaise", xy=(2.35,2.25), rotation=40, color="k", fontweight="bold", fontsize=18)
    plt.annotate("Très mauvaise", xy=(3.02,2.33), rotation=72, color="k", fontweight="bold", fontsize=18)
    # Annotations de la jauge

    for loc, val in zip([0, 0.6, 1.25, 1.98, 2.51, 3.14], values):
        plt.annotate(val, xy=(loc, 2.5), ha="right" if val<=20 else "left", fontsize=18)
    # Positionnement des label des différentes sections

    plt.annotate(str( np.round(proba*100,2) )+"%", xytext=(0,0), xy=(plr*3.14, 2.0),
    arrowprops=dict(arrowstyle="wedge, tail_width=0.5", color="black", shrinkA=0),
             bbox=dict(boxstyle="circle", facecolor="black", linewidth=2.0, ),
             fontsize=35, color="white", ha="center"
            );

    plt.title("Probabilité de rembourserment du prêt", loc="center", pad=20, fontsize=35, fontweight="bold")
    
    ax.set_thetamin(0)
    ax.set_thetamax(180)

    ax.set_axis_off()
    st.pyplot(fig, bbox_inches='tight')
    st.markdown("**PROBABILITÉ DE REMBOURSEMENT:** "+str(proba*100)+"%")

########### PARTIE GRAPHES ###########

sns.set_palette('colorblind')

st.header("Détails")

# Comparaison individu VS training data:

for column in datas.drop(columns='TARGET').columns:
    fig, ax = plt.subplots()

    if column == "CODE_GENDER":
        sns.kdeplot(
            datas[datas['TARGET'] == 1][column], label='Non remboursé', 
            ax=ax, fill=True, linestyle="dashed", linewidth=2, zorder=0
        )
        sns.kdeplot(
            datas[datas['TARGET'] == 0][column], label='Remboursé', 
            ax=ax, fill=True, linestyle="dotted", linewidth=2, zorder=0
        )
    else:
        sns.kdeplot(
        datas[datas['TARGET'] == 1][column], label='Non remboursé', 
        ax=ax, fill=True , linestyle="dashed", linewidth=2, zorder=0
        )
        sns.kdeplot(
        datas[datas['TARGET'] == 0][column], label='Remboursé', 
            ax=ax, fill=True, linestyle="dotted", linewidth=2, zorder=0
        )

    # Valeur client en ligne verticale
    indiv_value = np.round(indiv[column].iloc[0],2)
    ax.axvline(indiv_value, linestyle='dashdot', label='Valeur client', zorder=1, linewidth=1.5, color="red",
     markeredgecolor="k", markeredgewidth=3)
    
    ax.set_xlabel(column)
    ax.set_ylabel("Densité")
    ax.set_title(f'Distribution de {column}')
    ax.legend()
    st.pyplot(fig)

    st.markdown(f"**Valeur du client pour {column}:** {indiv_value}")
    st.markdown("---")
