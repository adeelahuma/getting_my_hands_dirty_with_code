#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 14:53:16 2020

@author: adeela
"""

'''
XGBoost

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('dataset/Churn_Modelling.csv')

data.info()

# provides high perfromance 
# XGBoost is a powerful implementation of gradient boosting in terms of 
# model performnace and execution speed

'''
Goal : Predictig if the customer will leave the bank or not 

'''
X = data.iloc[:, 3:13].values
y = data.iloc[:, 13].values


from sklearn.preprocessing import LabelEncoder, OneHotEncoder

lc_x1 = LabelEncoder()
X[:, 1] = lc_x1.fit_transform(X[:, 1])

lc_x2 = LabelEncoder()
X[:, 2] = lc_x2.fit_transform(X[: , 2])

ohe = OneHotEncoder(categorical_features=[1])
X = ohe.fit_transform(X).toarray()
X = X[:, 1: ]
X


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Model 

from xgboost import XGBClassifier

# Grid Search parameter training 

xgb = XGBClassifier()
xgb.fit(X_train, y_train)


## predict 

y_pred = xgb.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)


# cross validtaion 
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(xgb, X_train, y_train, cv = 10)
accuracies.mean()
accuracies.std()




from sklearn.metrics import roc_curve
roc_curve(y_test,y_pred)
































