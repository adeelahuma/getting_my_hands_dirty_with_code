#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 14:12:35 2020

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

# =============================================================================
#           Backward Elimination
# =============================================================================
import statsmodels.api as sm
#statsmodels.formula.api libbaray does not take x^0 == 1 into a
# ccount for contant b0
# To resolve this issue , add a first column with x=1
# Now first column corresponds to b0 in the multiple regresssion equation

X = np.append(arr = np.ones((X.shape[0], 1)).astype(int), 
          values= X, 
          axis=1)
# significane level for a varaible to stay in the model 
sl = 0.05

# X_opt will finally contain independent varaibles that are only statistically 
# significant for dependent variable

X_opt = X[:, [0,1,2,3,4,5]]  # original matrix of features 
regressor = sm.OLS(endog= y, exog= X_opt).fit()
regressor.summary()

#removed index=2 as x2 has the highest p-value
X_opt = X[:, [0,1,3,4,5]] 
regressor = sm.OLS(endog= y, exog= X_opt).fit()
regressor.summary()

#removed index=1 as x1 has the highest p-value
X_opt = X[:, [0,3,4,5]] 
regressor = sm.OLS(endog= y, exog= X_opt).fit()
regressor.summary()

#removed index=2 as x2 has the highest p-value
X_opt = X[:, [0,3,5]] 
regressor = sm.OLS(endog= y, exog= X_opt).fit()
regressor.summary()

#Now  we get 6% p value we should remove it as per sl=0.05 value


#removed index=2 as x2 has the highest p-value
X_opt = X[:, [0,3]] 
regressor = sm.OLS(endog= y, exog= X_opt).fit()
regressor.summary()

# So column 0 and 3 in original matrix are the good independt 
# variables with p-values of almost 0 
# =============================================================================
#       R^2 vs Adjusted R^2
# =============================================================================
#R^2  - tells about the goodness of fit . want it closer to 1.
# R^2 is biased because of the way model is run. 
# The more variables you add the R^2 will grow. 
# We can also throw random varaible such as weather, even though 
# its unrelated to the problem but r^2 is still going to grow and would imply 
# that model is better fitted thats where Adjusted r^2 comes into play
# adjusted r^2 similar to r^2 but has penalizing factor which makes it small 
# as you add more varaibles.
# When adjusted r^2 goes up , that means we have improved our model
# If its dropping then stop and ask the question what is the trade off 
# including/excluding a certain varaile

# =============================================================================
#       Interpreting Co-eeficients
# =============================================================================
'''
    if sign is positive--> varaible is correlated with 'y' 
    if sign is negative ---> its  opposite effect 
    Magitude:  DON'T think bigger means that varaible has more impact.
        Always say magnitude in terms of the per unit of the independent variable
        remember 'units' of independent variables can be different 
            (kilometer vs dollar; they are not comparable) 
    Coefficients tell about the additional affect of every single varaible 
    brings into the model          

   Profit = revenue - expense 
        
        
        
        
        
'''













  




