#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 13:17:37 2020

@author: adeela
"""

import pandas as pd 
import numpy as np 

data = pd.DataFrame({
        't_dates' : ['08-05-2019', '08-05-2019','08-05-2019','08-05-2019','08-05-2019','08-06-2019','08-08-2019','08-09-2019','08-09-2019','08-16-2019'],
         't_firm' : ['ABC','CDE','ABC','CDE','FGH','3CDE','ABC','ABC','FGH','CDE'],
         't_symbol' : [123,456,789,789,456,456,123,123,789,456],
         't_side' : ['B','B','S','S','B','X','B','S','B','S'],
         't_quantity' : [200, 601,600,600,200,300,300,300,2100,1100],
         't_price' : [41,60,70,70,62,61,40,30,71,63]
         })


data.describe()

'''
2)	Your business user asks you to show them a table output that includes an 
additional column categorizing the TRADES data into volume based Tiers, 
with a column named ‘Tier’. Quantities between 0-250 will be considered ‘Small’, 
quantities greater than ‘Small’ but less than or equal to 500 will be considered 
‘Medium’, quantities greater than ‘Medium’ but less than or equal to 500 will be considered 
‘Large’, and quantities greater than ‘Tier 3’ will be considered ‘Very Large’ .

a.	Please write the SQL query you would use to add the column to the table output.
b.	Please show the exact results you expect based on your SQL query.

'''
conditions= [data['t_quantity'] <= 200 ,  
             (data['t_quantity'] > 200) & (data['t_quantity'] <= 500),
             data['t_quantity'] > 500]

choices = ['small', 'medium', 'large']

data = data.assign(tier = np.select(conditions, choices))


'''
3)	Your business user asks you to show them a table output summarizing 
the TRADES data (Buy and Sell) on week-by-week basis. 

a.	Please write the SQL query you would use to query this table.
b.	Please show the exact results you expect based on your SQL query.

'''
data.t_dates = pd.to_datetime(data['t_dates'])
data.info()
data.assign(week= data['t_dates'].dt.week)
data.groupby(by=['t_side', 't_dates']).size() 









