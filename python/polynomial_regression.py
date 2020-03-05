#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 13:05:48 2020

@author: adeela
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('dataset/Position_Salaries.csv')

X = data.iloc[: , 1:2].values
y = data.iloc[: , 2].values

# Linear Regression libraray doess the feature scaling so we dont need to do it 
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X, y)

#Polynomial Regression
from sklearn.preprocessing import PolynomialFeatures
# will transform the features matrix to a new matrix 
# can add polynomial of power 1,2,3 etc
# you can increase/decrease degree   
poly_reg = PolynomialFeatures(degree=3)
X_poly = poly_reg.fit_transform(X)


lrp = LinearRegression()
lrp.fit(X_poly,y)

#Visualizing the Linear Regression results
#<<IMPORTANT>> See straight fit line vs actual points
plt.scatter(X,y)
plt.plot(X, lr.predict(X), c='r')
plt.show()

#Visualizing the Polynomial Regression Model

plt.scatter(X,y)
plt.plot(X, lrp.predict(X_poly), c='r')
plt.show()


#Visualizing the Polynomial Regression Model
# Visualization at increased resolution and will get a smoother curve
x_grid = np.arange(min(X), max(X), 0.1)
x_grid = x_grid.reshape(len(x_grid),1)


plt.scatter(X,y)
plt.plot(x_grid, lrp.predict(poly_reg.fit_transform(x_grid)), c='r')
plt.show()

#Linear vs non-linear model 
# linear gives straight line, non-linear --> anything but a straight line


# Predicting Linear Regression
lr.predict([[6.5]])

# Predicting Polynomial Regression

lrp.predict(poly_reg.transform([[6.5]]))















