# 🧬 SRNA_Classification - Classification de Petits ARN

---

## 📌 Contexte

**Projet** : Classification de familles de petits ARN non-codants  
**Type** : Stage académique  
**Établissement** : INRAE (Institut National de Recherche pour l'Agriculture, l'Alimentation et l'Environnement)  
**Période** : Février - Juin 2023  
**Données** : Publiques et reproductibles  

Projet de classification basé sur **Deep Learning** pour analyser et classifier les séquences d'ARN de virus. Utilisation de réseaux de neurones convolutifs (CNN) appliqués à des données génomiques réelles.

---

## 🎯 Objectif du Projet

Déterminer **quelle information est la plus pertinente** pour classifier deux familles d'ARN non-codants :

- 🧵 **Séquence ARN brute** → Information primaire
- 🔀 **Structure secondaire ARN** → Information 3D
- 🔗 **Combinaison des deux** → Information complète

**Question centrale** : Deux modèles CNN peuvent-ils classifier mieux ensemble que séparément ?

---

## 📊 Architecture & Approche

### **1. Traitement des Données**

```
Séquences ARN brutes (FASTA)
    ↓
RNAfold (prédiction structure secondaire)
    ↓
Matrices d'appariement + Structures secondaires
    ↓
3 jeux de données :
  - Séquence seule (1D)
  - Structure seule (2D)
  - Séquence + Structure (3D)
```

### **2. Modèles Deep Learning (CNN)**

Trois architectures parallèles testées :

| Modèle | Input | Architecture | Objectif |
|--------|-------|--------------|----------|
| **CNN 1D** | Séquence ARN encodée | Convolutions 1D + MaxPooling | Capture patterns linéaires |
| **CNN 2D** | Matrice d'appariement | Convolutions 2D | Capture structure 2D |
| **Multi-Input CNN** | Séquence + Structure | 2 branches + fusion | Combine les deux signaux |

### **3. Performance Obtenue**

```
Meilleure performance : Multi-Input CNN
├── Accuracy : 100%
├── Cohen's Kappa : 0.998
├── Précision : Excellente (classification très stable)
└── Conclusion : La combinaison séquence+structure est optimale
```

---

## 💼 Mon Rôle & Contributions

### **Conception & Implémentation**

✅ **Exploration données génomiques** - Analyse des séquences ARN RFAM  
✅ **Développement 3 architectures CNN** (1D, 2D, multi-input)  
✅ **Optimisation hyperparamètres** - Tuning expérimental  
✅ **Validation croisée & métriques** - Cohen's Kappa, Accuracy, etc.  
✅ **Prédiction structures ARN** - Intégration RNAfold  

### **Améliorations Implémentées**

🔧 **Génération d'exemples positifs/négatifs** - Algorithmes custom  
🔧 **Data augmentation** - Techniques pour petits datasets  
🔧 **Optimisation mémoire** - Gestion données volumineuses  

---

## 📁 Structure du Projet

```
Stage_INRAE/
├── Data/                          # Données brutes (publiques)
│   ├── [Séquences ARN FASTA]
│   └── [Données RFAM]
│
├── RNAfold/                       # Prédictions structures secondaires
│   ├── Famille_1/
│   ├── Famille_2/
│   ├── Famille_3/
│   └── Famille_4/
│   └── [Matrices + Structures 2D pour chaque séquence]
│
├── Models/                        # Architectures Deep Learning
│   ├── cnn_1d.py                 # CNN 1D (séquences)
│   ├── cnn_2d.py                 # CNN 2D (structures)
│   └── multi_input_cnn.py        # Fusion séquence + structure
│
├── Functions/                     # Bibliothèques développées
│   ├── preprocessing.py           # Nettoyage données
│   ├── encoding.py               # Encodage séquences (one-hot, etc.)
│   ├── metrics.py                # Métriques custom
│   └── visualization.py          # Plots & analyses
│
├── Script_python/                 # Scripts d'entraînement
│   ├── train_cnn_1d.py
│   ├── train_cnn_2d.py
│   └── train_multi_input.py
│
├── Script_tuto_keras/             # Exemples & références
│   └── [Scripts de tutoriels Keras]
│
├── Results/                       # Résultats finaux
│   ├── accuracy_comparison.csv
│   ├── training_curves.png
│   ├── confusion_matrices/
│   └── predictions/
│
└── Presentation_of_the_week/     # Rapports hebdomadaires
    └── [Présentations superviseurs]
```

---

## 🛠️ Stack Technique

### **Deep Learning & ML**
- ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) - Langage principal
- ![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white) - Framework Deep Learning
- ![Keras](https://img.shields.io/badge/Keras-D00000?style=flat-square&logo=keras&logoColor=white) - API haut-niveau
- ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white) - Prétraitement & métriques

### **Bioinformatique & Données**
- ![RNAfold](https://img.shields.io/badge/RNAfold-009688?style=flat-square) - Prédiction structures ARN
- ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) - Manipulation données
- ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) - Calcul numérique
- ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square) - Visualisation

### **Développement**
- ![Jupyter](https://img.shields.io/badge/Jupyter-F37726?style=flat-square&logo=jupyter&logoColor=white) - Notebooks interactifs
- ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) - Versioning

---

## 📊 Résultats Clés

| Métrique | Valeur | Impact |
|----------|--------|--------|
| **Accuracy (Multi-Input)** | 100% | Classification parfaite |
| **Cohen's Kappa** | 0.998 | Excellent accord inter-annotateurs |
| **Familles d'ARN testées** | 4 | RFAM database |
| **Architectures comparées** | 3 | 1D vs 2D vs Fusion |
| **Temps d'entraînement** | Optimisé | GPU Tesla (INRAE) |

**Conclusion clé** : 
> La combinaison de la **séquence + structure secondaire** produit une classification bien supérieure à chacune séparément. Les CNNs multi-input capturent complémentairement les patterns linéaires (séquence) et structuraux (3D).

---

## 🔬 Approche Scientifique

### **Méthodologie**

1. **Extraction données** → RFAM (base de données ARN publique)
2. **Génération structures** → RNAfold (prédiction)
3. **Encoding** → One-hot encoding (séquences) + Matrices (structures)
4. **Modélisation** → 3 architectures CNN parallèles
5. **Validation croisée** → K-fold (k=5)
6. **Comparaison** → Accuracy, Precision, Recall, Cohen's Kappa

### **Données Publiques**

✅ Tous les jeux de données proviennent de **sources publiques accessibles** :
- RFAM (RNA Family Database) - https://rfam.org/
- RNAfold - http://rna.tbi.univie.ac.at/

Reproductibilité garantie ! 🎯

---

## 🎓 Compétences Développées

- ✅ **Bioinformatique** - Manipulation séquences ARN, structures ARN
- ✅ **Deep Learning** - CNN 1D, 2D, Multi-input architectures
- ✅ **Optimisation ML** - Hyperparamètres tuning, validation croisée
- ✅ **Data Engineering** - Prétraitement données génomiques
- ✅ **Visualisation** - Matrices de confusion, courbes d'apprentissage
- ✅ **Rigueur scientifique** - Métriques robustes, reproductibilité

---

## 📈 Axes d'Amélioration & Évolutions

- 🚀 **Transfer Learning** - Pré-entraînement sur datasets plus larges
- 🚀 **Attention Mechanisms** - Pour identifier régions clés de l'ARN
- 🚀 **Graph Neural Networks** - Modelage de la structure 3D
- 🚀 **Multi-tâche learning** - Classification + prédiction structure simultanée

---

## 👤 Auteur

**Hassan HOUSSEIN HOUMED**  
📚 Master 2 Ingénierie Mathématiques & Biostatistique - Université Paris Cité  
🏢 Stage INRAE (Institut National de Recherche pour l'Agriculture)  
📧 hassan.houssein.houmed@gmail.com  
🐙 GitHub : https://github.com/HASSANHOUSSEINHOUMED

---

## 📚 Références

- **RFAM Database** : https://rfam.org/
- **RNAfold** : http://rna.tbi.univie.ac.at/
- **TensorFlow/Keras Documentation** : https://www.tensorflow.org/
- **Cohen's Kappa** : Mesure de l'accord inter-annotateurs

---

**Dernière mise à jour** : Décembre 2025  
**Données** : Publiques et reproductibles ✅
