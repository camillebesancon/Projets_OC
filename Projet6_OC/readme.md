# Classifiez automatiquement des biens de consommation

## Contexte professionnel / Approche métier
Vous êtes Data Scientist au sein de l’entreprise "Place de marché”, qui souhaite lancer une marketplace e-commerce. Sur "Place de marché", des vendeurs proposent des articles à des acheteurs en postant une photo et une description.
Pour l'instant, l'attribution de la catégorie d'un article est effectuée manuellement par les vendeurs, et est donc peu fiable. De plus, le volume des articles est pour l’instant très petit.

Pour rendre l’expérience utilisateur des vendeurs (faciliter la mise en ligne de nouveaux articles) et des acheteurs (faciliter la recherche de produits) la plus fluide possible, et dans l'optique d'un passage à l'échelle, il devient nécessaire d'automatiser cette tâche. Linda, Lead Data Scientist, vous demande donc d'étudier la faisabilité d'un moteur de classification des articles en différentes catégories, avec un niveau de précision suffisant.

Voici le mail qu’elle vous a envoyé.

## Mission 

Bonjour,

> Merci pour ton aide sur ce projet ! 
> Ta mission est de réaliser une première étude de faisabilité d'un moteur de classification d'articles, basé sur une image et une description, pour l'automatisation de l'attribution de la catégorie de l'article.
> Tu dois analyser le jeu de données en réalisant un prétraitement des descriptions des produits et des images, une réduction de dimension, puis un clustering. Les résultats de la réduction de dimension et du clustering seront à présenter sous la forme de graphiques en deux dimensions, et confirmés par un calcul de similarité entre les catégories réelles et les clusters. Ces résultats illustreront le fait que les caractéristiques extraites permettent de regrouper des produits de même catégorie. Pourrais-tu nous démontrer, par cette approche de modélisation, la faisabilité de regrouper automatiquement des produits de même catégorie ?

> Voici les contraintes :
> 1. Afin d’extraire les features texte, il sera nécessaire de mettre en œuvre :
>   - deux approches de type “bag-of-words”, comptage simple de mots et Tf-idf ;
>   - une approche de type word/sentence embedding classique avec Word2Vec (ou Glove ou FastText) ;
>   - une approche de type word/sentence embedding avec BERT ;
>   - une approche de type word/sentence embedding avec USE (Universal Sentence Encoder).
    
> En pièce jointe, tu trouveras un exemple de mise en œuvre de ces approches sur un autre dataset. Je t’invite à l’utiliser comme point de départ, cela va te faire gagner beaucoup de temps ! 

> 2. Afin d’extraire les features image, il sera nécessaire de mettre en œuvre :
>   - un algorithme de type SIFT / ORB / SURF ;
>   - un algorithme de type CNN Transfer Learning.
> Merci encore,
> Linda

> P.S. : j’insiste sur le fait qu’on n’a pas besoin d’un moteur de classification supervisée à
ce stade, mais bien d’une étude de faisabilité !

## Données 
- Jeu de données avec liens pour télécharger les images : https://s3-eu-west-1.amazonaws.com/static.oc-static.com/prod/courses/files/Parcours_data_scientist/Projet+-+Textimage+DAS+V2/Dataset+projet+pre%CC%81traitement+textes+images.zip
- Notebook d'exemple : https://s3.eu-west-1.amazonaws.com/course.oc-static.com/projects/Data_Scientist_P6/Exemple_Tweets_Feature-extraction_Sentence+Embedding_V1.1.ipynb
