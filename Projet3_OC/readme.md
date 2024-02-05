# Projet 3 - Concevoir une application de santé publique

## Contexte professionnel / métier
L'agence "Santé publique France" a lancé un appel à projets pour trouver des idées innovantes d’applications en lien avec l'alimentation. Vous souhaitez y participer et proposer une idée d’application.

## Les données
Extrait de l’appel à projets :

### Jeu de données

- Lien de téléchargement : https://s3-eu-west-1.amazonaws.com/static.oc-static.com/prod/courses/files/parcours-data-scientist/P2/fr.openfoodfacts.org.products.csv.zip
- Définition des variables : https://world.openfoodfacts.org/data/data-fields.txt

### Définition des variables 
Les champs sont séparés en quatre sections :

- Les informations générales sur la fiche du produit : nom, date de modification, etc.
- Un ensemble de tags : catégorie du produit, localisation, origine, etc.
- Les ingrédients composant les produits et leurs additifs éventuels.
- Des informations nutritionnelles : quantité en grammes d’un nutriment pour 100 grammes du produit.

# Missions
Après avoir lu l’appel à projets, voici les différentes étapes que vous avez identifiées :

1. Traiter le jeu de données, en :
  - Réfléchissant à une idée d’application.
  - Repérant des variables pertinentes pour les traitements à venir, et nécessaires pour votre idée d’application.
  
2. Nettoyer les données en :
  - mettant en évidence les éventuelles valeurs manquantes, avec au moins 3 méthodes de traitement adaptées aux variables concernées,
identifiant et en quantifiant les éventuelles valeurs aberrantes de chaque variable.
  - Automatisant ces traitements pour éviter de répéter ces opérations
  - Le programme doit fonctionner si la base de données est légèrement modifiée (ajout d’entrées, par exemple).

3. Tout au long de l’analyse, produire des visualisations afin de mieux comprendre les données. Effectuer une analyse univariée pour chaque variable intéressante, afin de synthétiser son comportement.


L’appel à projets spécifie que l’analyse doit être simple à comprendre pour un public néophyte. **Soyez donc attentif à la lisibilité** : taille des textes, choix des couleurs, netteté suffisante, et variez les graphiques (boxplots, histogrammes, diagrammes circulaires, nuages de points…) pour illustrer au mieux votre propos.

4. Confirmer ou infirmer les hypothèses à l’aide d’une analyse multivariée. Effectuer les tests statistiques appropriés pour vérifier la significativité des résultats.

5. Justifier votre idée d’application. Identifier des arguments justifiant la faisabilité (ou non) de l’application à partir des données Open Food Facts.

6. Rédiger un rapport d’exploration et pitcher votre idée durant la soutenance du projet.
