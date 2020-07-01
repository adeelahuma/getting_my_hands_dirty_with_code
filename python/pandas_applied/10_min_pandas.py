#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 11:32:28 2020

@author: adeela
"""

'''
https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html#min
'''

import numpy as np 
import pandas as pd
 
s = pd.Series(['1', 1, np.nan, 1])
s

# gives 6 dates starting from 2020-01-01
dates = pd.date_range('2020-01-01', periods=6)

# returns list as ['A', 'B', 'C', 'D']
list('ABCD')

# returns a row matrix of size 6*4 with random entries
np.random.randn(6,4)  
df = pd.DataFrame(np.random.randn(6,4), 
                  index = dates,
                  columns=list('1234'))

## datframe from dictionary object 
df2 = pd.DataFrame({
        'A': 1, 
        'B': pd.Timestamp('20200101'), 
        'C': pd.Categorical(['yes', 'no', 'yes', 'no']), 
        'D': np.array([3] * 4),
        'E': pd.Series(1, index=range(4))
        })


df2.dtypes # types of columns in dataframe
df2.A # can access the whole column 

# to see the index of the dataframe
df2.index
df.index

#25%, 50%, 75% are q1, q2, q3 respectively
df.describe()

#transpose of data frame
df.T

# What is axis doing in sort by index???
df.sort_index(axis=0, ascending= True)
df.sort_index(axis=1, ascending= True)

#sort by values of column labeled '2'
df.sort_values(by = '2')

# =============================================================================
#       SELECTION
# =============================================================================

#selecting a single column gives you back a series
df['1']

# to get rows by slicing syntax
# return rows 0 and 1
df [0:2]

#returns row where index value matches
df['2020-01-01': '2020-01-03']
#df['2020-01-01'] doesn't work 

#getting data by the index value
df.loc['2020-01-01']

#select all rows for column named '1'
df.loc[:, '1']

#select all rows for column 1 and 2
df.loc[:, ['1', '2']]

# get values of column '1' and '2' where index value is ''
df.loc['2020-01-01', ['1','2']]

# get value of column '1' where index value is '' 
df.loc['2020-01-01', ['1']]


# =============================================================================
# Selection by POSITION
# =============================================================================

# return the fourth row all columns
df.iloc[3]

#get values for 3 to 5th row and 1st column 
df.iloc[2:5, 1]

#get values for 3 to 5th row and 2nd and 3rd column
df.iloc[2:5, 1:3]

#return 4th row all columns 
df.iloc[3, :]

# value at row i and colum j 
df.iloc[1,1]


# =============================================================================
#   Bolean Indexing 
# =============================================================================

#data where values of column '1' > 0
df[df['1']> 0 ]

#Adding a column 
df['5'] = ['a', 'b', 'c', 'd', 'e', 'f']

# check if column has a certain value OR 
# extract the row where column E has value a
df[df['5'].isin(['a'])]

## update value in data where column '5' has values a b and c
## Problem : it updated all values of column
# HOW TO JUST UPDATE THE VALUE OF COLUMN ???
df[df['5'].isin(list('abc'))] = 'g'


# =============================================================================
#    APPLY function
# =============================================================================

## sum all elements of column '1'
df['1'].apply(np.sum)

## sum of all elements in the data
# if it is string , it returns a concatenated result 
df.apply(np.sum)

## sum along the column meaning sum of each column  
df.apply(np.sum, axis=0)

df.iloc[:, :4] # this selets all rows and columns till 4th index
#axis = 1 --> row
df.iloc[:, :4].apply(np.sum, axis=1)
# axis =0 --> column 
df.iloc[:, :4].apply(np.sum, axis=0)




















