#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 13:57:03 2020

@author: adeela
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('dataset/Social_Network_Ads.csv')

X = data.iloc[:, [2,3]].values
y = data.iloc[:, 4].values

from sklearn.model_selection import train_test_split
X_train,X_test, y_train, y_test  = train_test_split(X, y, test_size=0.25, 
                                                    random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train) 
X_test = sc.transform(X_test)


#classifier KNN
from sklearn.neighbors import KNeighborsClassifier
#minkowski, 2 specifies euclidean distance
knn = KNeighborsClassifier(n_neighbors=5,
                           metric ='minkowski',
                           p =2
                           )
knn.fit(X_train, y_train)

#Predict
y_pred = knn.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
cm
