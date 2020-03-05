#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:56:39 2020

@author: adeela
"""
'''
    https://docs.scipy.org/doc/numpy/user/quickstart.html
'''

import numpy as np
import pandas as pd


df = pd.DataFrame({
        'A': np.random.randn(10),
        'B': np.arange(1,11),
        'C': np.arange(1,11)*2.1
        })

#to convert a single column to numpy() array
['B'].to_numpy()

#to convert a dataframe to numpy() matrix 
m = df.to_numpy()

#size of array/matrix
m.shape

# Add a additional row 
np.row_stack( ( np.arange(1,10), np.arange(1,10)) ).shape


# Add a additional column 
np.column_stack( ( np.arange(1,10), np.arange(1,10)) ).shape

#TO ADD AN ADDITIONAL ROW-->
# number of elements in added array == size of columns
np.arange(1,30,10).shape
np.row_stack((m, np.arange(1,30,10)))

#TO ADD AN ADDITIONAL COLUMN-->
# number of elements in added array == size of rows
#[np.nan]*10
np.column_stack((m, [1]*m.shape[0]))

##Sum of all alements in the array
np.sum(m)

# =============================================================================
#   Calculate Summary Statistics as done by df.describe
#       (min, mean, max, q1,q2,q3,variance of each numeric column in M array
# =============================================================================
summary_stats= []
for i in range(m.shape[1]):
    summary_stats.append((
    round(np.min(m[:, i]), 1),
    round(np.mean(m[:, i]), 1),
    round(np.max(m[:, i]), 1), 
    round((np.mean(m[:, i]) - np.min(m[:, i])), 1),
    round((np.mean(m[:, i]) - np.min(m[:, i])), 1),
    round((np.max(m[:, i]) - np.mean(m[:, i])), 1),
    round(np.std(m[:, i]), 1)
    ))
    
np.array(summary_stats).T   

 
# =============================================================================
#       Euclidean distance between two vectors
# =============================================================================

# In this example of matrix m --->
# m[i][0 to 2] represents one object that has 3 dimensions


def euclidean_dist(p1, p2):
    return  np.sqrt(np.sum(np.square(np.subtract(p1,p2))))
s
# NOW create a 10 by 10 matrix where each index represent the distance 
# between 2 points

from itertools import product

cartesian_p = product(range(m.shape[0]), range(m.shape[0]))

distances = []
for c in cartesian_p:
    distances.append(euclidean_dist(m[c[0], :], m[c[1], :]))
    
dist = np.array(distances)    

dist.shape
#reshape() function converts a array converts into matrix
test = pd.DataFrame(dist.reshape((10,10)))
test.shape

















