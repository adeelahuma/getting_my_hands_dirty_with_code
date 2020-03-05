#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 19:48:28 2020

@author: adeela
"""

import pandas as pd
import numpy as np
import random as choices 


# =============================================================================
#       Synthetic Data
# =============================================================================
data_size = 500
#Data about who consumed candy given in month of Feb, 2020, 
#age of the person, sweet_level of candy
data = pd.DataFrame({
        'label': np.random.choice(['yes', 'no'], data_size), 
        'sweetness_level': np.random.choice(pd.Series(pd.Series(np.arange(1,10,3))), data_size),
        'age':   np.random.choice(np.arange(4,65,1), data_size), 
        'date': np.random.choice(pd.date_range('20200201', '20200229', freq='1d'), data_size)
        })

#frequency of each class  
data.label.value_counts()

#no     265
#yes    235

# =============================================================================
#       Train/Test Split of data 
# =============================================================================

#https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html

from sklearn.model_selection import train_test_split

train, test = train_test_split(data, test_size=0.3)

train.label.value_counts() 
#no     184
#yes    166

test.label.value_counts()

#no     81
#yes    69

'''
 OR DO IT THIS WAY BY SPRITTING LABEL FROM THE DATA ATTRIBUTES 
 AS X (x, x2, ...xn) and y(class label)
'''

X = data.iloc[:, 1:]
y = data.iloc[:, :1]

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3)


# =============================================================================
#   Train/Test Split with Startification
# =============================================================================
'''
    Stratification is a sampling technique to balance the proportion of 
    class samples in test and train samples. ?????
'''
train_s, test_s = train_test_spl7it(data, test_size= 0.3, 
                                   stratify = data['label'])

train_s.label.value_counts()
#no     185
#yes    165
test_s.label.value_counts()
#no     80
#yes    70


# =============================================================================
#  Training, Validation and Test set
# =============================================================================



# =============================================================================
#   Cross Validation
# =============================================================================

#https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html

from sklearn.model_selection import KFold

kf = KFold(n_splits = 10)
#num_splits = kf.get_n_splits(data)

# each iteration gives split of data indices >> 90% as train nd 10% as test
for train_cv_index, test_cv_index in kf.split(data):
    #print(train_cv_index)    
    #print(test_cv_index)
    train_cv = data.iloc[train_cv_index]
    test_cv = data.iloc[test_cv_index]
    break      

assert round(len(data)*.9) == len(train_cv), '90% of data == train'
assert round(len(data)*.1) == len(test_cv) , '10% of data == test'

#test_cv_index in train_cv_index  # are the indices diferent --> must be True

# =============================================================================
#       Stratified Cross Validation
# =============================================================================



# =============================================================================
#   Leave-one out
# =============================================================================


# =============================================================================
#   Bootstrap
# =============================================================================
































