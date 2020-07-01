#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 08:23:10 2020

@author: adeela
"""

'''
Bikeshare Data
Link >> https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset


'''

import pandas as pd
import numpy as np

data = pd.read_csv( 'dataset/bike_share_day.csv', parse_dates=True, index_col='instant' )

data.columns
data.info()

# Convert variables to proper format 
data['dteday'] = pd.to_datetime(data['dteday'])

cat_var= ['season', 'yr', 'mnth', 'mnth', 'mnth', 'workingday', 'weathersit', 
          'holiday', 'weekday']
for col in cat_var: 
    data[col] = pd.Categorical(data[col])    

data.info()

data.head(10)

data.describe()


# =============================================================================
#       What is total bike rental per week 
# =============================================================================

#data.groupby(by = ['yr','season']).size()
#
#data.groupby(by = ['yr','season'])['cnt'].sum()
#
#
#data['dteday'].iloc[0].day
#data['dteday'].iloc[0].month
#data['dteday'].iloc[0].year
#data['dteday'].iloc[0].weekday()

# Add column to get the weekend date fromm the given date
# This behavior is similar to sql with() clause
# To use the column generated inside assign(), use it with lambda
data = data.assign(time_delta = pd.Series(map (lambda x: pd.Timedelta((6- x),'D'), data['weekday'] )), 
            weekend_date = lambda x: x['dteday'] + x['time_delta'] )

data.groupby(by='weekend_date').agg({
        'cnt' : [np.sum,  np.mean]
        })





