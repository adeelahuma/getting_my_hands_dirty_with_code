#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 08:26:35 2020

@author: adeela
"""

import scipy.stats as st
st.pearsonr(np.arange(1,10), np.arange(1,10))


import seaborn as sns 
  
# generating correlation heatmap 
sns.heatmap(df_restaurant.corr(), annot = True) 
  
# posting correlation heatmap to output console  
plt.show()

