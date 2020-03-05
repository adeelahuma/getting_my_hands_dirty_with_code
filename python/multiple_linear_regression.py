#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:27:37 2020

@author: adeela
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('dataset/50_Startups.csv')
X = data.iloc[:, :-1].values 
y = data.iloc[:, 4].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
lc = LabelEncoder()
X[:, 3] = lc.fit_transform(X[:, 3])

ohe = OneHotEncoder(categorical_features=[3])
X = ohe.fit_transform(X).toarray()

# Avoiding the Dummy Variable Trap 
X = X[:, 1: ]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, 
                                                    random_state=0)

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train, y_train)

y_pred = lm.predict(X_test)


# Can't plot it because of 5 dimensions