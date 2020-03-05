#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:08:27 2020

@author: adeela
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('dataset/Salary_Data.csv')

X = data.iloc[:, :-1].values
y = data.iloc[:, 1].values


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, 
                                                    random_state=0)

#Linear Regression Model 
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train, y_train)

#predict 
y_pred = lr.predict(X_test)

lr.coef_
lr.intercept_
lr._residues

#Training Data
plt.scatter(X_train, y_train)
plt.plot(X_train, lr.predict(X_train), c='r')
plt.show()

#Test Data
plt.scatter(X_test,y_test)
plt.plot(X_test, y_pred, c='r')
plt.show()