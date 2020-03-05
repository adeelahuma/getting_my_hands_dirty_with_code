#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 15:25:38 2020

@author: adeela
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('dataset/Social_Network_Ads.csv')

X = data.iloc[:, [2,3]].values
y = data.iloc[:, 4].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, 
                                                    random_state=0)
# DO NOT Need feature scaling for CART and Random Forest 
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#classifier Randomforest 
# RandomForest --> Army of Decision Trees 
# Play with n_estimators and pay attention to overfitting 

# Entropy --> After the split, the more homogenous the split is 
# the entropy will be reduced.
# Entropy in physics represnts the disorder. 
# Information gain is how much the entropy you managed to reduce before and after the split
# Information gain = entropy (Parent) - entropy(child)


from sklearn.ensemble import RandomForestClassifier
rf_classifier = RandomForestClassifier(
            n_estimators = 10,  # number of trees
            criterion='entropy',
            random_state =0             
        )

rf_classifier.fit(X_train, y_train)

# Predict 

y_pred = rf_classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)

# Visualization 
# Plotting 
# Best classifier may be kernel SVM or Navive Bayes classifier 
# Best Classifier for problem --> Better Accuracy and prevent Overfitting 













