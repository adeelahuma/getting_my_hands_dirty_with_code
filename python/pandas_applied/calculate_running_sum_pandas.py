#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 11:37:20 2020

@author: adeela
"""
# Given :
# -- salesdate customername amount
# -- 10-01-2019 X 100 
# -- 10-01-2019 Y 230 
# -- 10-02-2019 X 300 
# -- 10-03-2019 Y 330 
# -- 10-03-2019 X 400 
# -- 10-05-2019 Y 50
# Write code to find the cummulative sum by customer 
# -- tot
# -- 100
# -- 230
# -- 400
# -- 560
# -- 800
# -- 610
import pandas as pd
import numpy as np 

df = pd.DataFrame({
        'date': ['10-01-2019', '10-01-2019', '10-02-2019',
                 '10-03-2019', '10-03-2019', '10-05-2019'], 
         'name': ['X', 'Y', 'X', 'Y', 'X', 'Y'], 
         'amount': np.random.randint(50,500, 6)
        })

# df = pd.DataFrame({
#     'date' : pd.date_range('01/01/2020', '01/10/2020'),
#     'cust_name': np.random.choice(['X','Y','Z'], size= 10),
#     'amount': np.random.randint(50,100, size=10)
# })

# add a column for cummulative sum for each customer
# cumsum == cummulative sunm == running total 
df['cumsum_user'] = df.groupby('name').cumsum()

df.sort_values(by=['name', 'cumsum_user'])

df['cumsum_data'] = np.cumsum(df.loc[:, 'amount'])

df


# =============================================================================
#       ALTERNATE METHOD Where column is calculated within assign
# =============================================================================

df_n= df.assign(total = df.groupby(by='name').cumsum()).sort_values(['name'])