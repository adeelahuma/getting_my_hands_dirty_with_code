#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 17:45:52 2020

@author: adeela
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sales  = pd.read_csv('dataset/walmart/sales.csv')
stores = pd.read_csv('dataset/walmart/stores.csv')

stores.info()
sales.info()

stores.columns
sales.columns

stores.groupby(by='Type')['Store'].count()
'''
>>What's the relationship between store type and store size? 
Can you use a visualization to help understand the relationship?

>>For department one, which Type of store has the most weekly sales? 
Can you explain it from the size of the store perspective?

'''

plt.scatter(stores['Type'], stores['Size'])
pd.crosstab(sorted_df['restaurant_id'],sorted_df['food_name']).plot.bar()
pd.crosstab(stores['Type'], stores['Size'])

'''
Based on stores and sales data, If we want to predict the department-wide sales 
for each store for the following year; 
what are your ideas on the next steps for Exploratory Data Analysis?
'''

