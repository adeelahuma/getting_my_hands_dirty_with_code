#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 18:19:23 2020

@author: adeela
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x1 = np.arange(1,22)
#x2 = np.arange(1,42,2)
y1 = np.sin(x1)
#y2 = np.cos(x2)

df = pd.DataFrame({
        'x1': x1, 
        #'x2': x2, 
        'y1': y1,
        #'y2': y2,
        'cat' : np.random.choice(['A','B','C'], 21)
        })



# this will plot the result on the same graph 
# can set ticks, x/y limts and move the spine(x/y line) to center etc 
plt.figure(figsize=(16,4), dpi=80) # 14 units width , 6 units height, dpi = dots per inch 
plt.xlim(x1.min()*1.2, x1.max()*1.5)  # set x limits
plt.ylim(y1.min()*2, y1.max()*3)
plt.plot(x1,y1)
plt.show()

# This will show scatter matrix of continous variables ONLY
from pandas.plotting import scatter_matrix
scatter_matrix(df)
plt.show()

# SNS Pairplot aslso shows the scatter matrix of continous variables but with 
# hue='categorical' variable we can see the category in color 
sns.pairplot(df, hue='cat')
plt.show()

## SNS Relplot is showing relationship between two varaibles per categories
sns.relplot(data= df, x= 'x1', y= 'y1',  col= 'cat', hue='cat', kind='scatter')
plt.show()

# SNS Catplot is a plot between a categorical and continous variable
sns.catplot(data=df, x='cat', y='y1', hue='cat', kind='swarm')
plt.show()

#what happens if we reverse it ?
sns.catplot(data=df, x='y1', y='cat', hue='cat', kind='swarm')
plt.show()

# SNS lmplot plot ??
sns.lmplot(data=df, x='x1', y='y1', hue='cat', col='cat')
plt.show()

# SNS Reg plot ??










