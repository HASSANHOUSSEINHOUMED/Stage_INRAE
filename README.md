# Contexte
Ce projet vise à classifier les familles de petits ARNs. Il étudie si la séquence d'ARN, la structure secondaire d'ARN, ou les deux peuvent mieux classifier deux familles appartenant aux ARNs non-codants. Les modèles d'apprentissage profond utilisés dans ce projet sont des réseaux de neurones convolutifs.
Ce travail a été réalisé dans le cadre d'un stage à l'INRAE (Institut National de Recherche pour l'Agriculture, l'Alimentation et l'Environnement), portant sur l'évaluation, l'optimisation et la mise en œuvre d'un classificateur basé sur un réseau de neurones pour l'analyse de séquences d'ARN de virus. Le projet a également impliqué la proposition et mise en œuvre de modifications pour améliorer la génération d'exemples positifs et négatifs, ainsi que le développement de modèles prédictifs.
Structure du projet

# Data : 
Contient toutes les données utilisées dans le projet.
# Functions : 
Regroupe les bibliothèques développées pour les notebooks du projet.
# Models : 
Comprend les différents modèles d'apprentissage profond créés pour le projet.
# Presentation of the Week : 
Contient les présentations hebdomadaires faites aux superviseurs de stage, servant de rapports hebdomadaires.
# RNAfold : 
Contient deux sous-dossiers, chacun représentant les données d'une famille. Les données contenues dans chaque dossier génèrent deux nouveaux fichiers pour chaque séquence : la matrice d'appariement et sa structure secondaire. Ces informations sont obtenues grâce à RNAfold.
# Results : 
Contient tous les résultats du projet.
# Python Script : 
Contient tous les scripts Python utilisés dans le projet.
# Python Keras Script : 
Contient des scripts Python qui ont été consultés pour créer les modèles du projet. Ces scripts servent d'exemples de modèles Keras disponibles en ligne.
