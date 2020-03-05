#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 15:29:56 2020

@author: adeela
"""

'''
Naive Baye's Classifier 

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('dataset/Social_Network_Ads.csv')

X = data.iloc[:, [2,3]].values
y = data.iloc[:, 4].values

#Split the datset 

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.25, random_state=0)

#Feature Scaling 
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train= sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Naive Baye's classifier 

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()

classifier.fit(X_train, y_train)

#prediction 
y_pred = classifier.predict(X_test)

# Confusion Matrix 
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# Exercise--> see based on curve how it works 

import seaborn as sns
from pandas.plotting import scatter_matrix

sns.pairplot(data, hue = 'Purchased')
scatter_matrix(data)















