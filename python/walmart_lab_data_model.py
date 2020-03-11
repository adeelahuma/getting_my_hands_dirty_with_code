#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 10:14:01 2020

@author: adeela
"""

'''

Walmart Labs data :
    
    1) Clustering
    2) PCA
    3) Regression
        - Random Forest
        - XGBoost
        - Catboost

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

stores =  pd.read_csv('dataset/walmart/stores.csv')
sales  =  pd.read_csv('dataset/walmart/sales.csv')

# Clean stores data to remove duplicates and missing record 
# <<KNOW this from previous analysis, refer to Walmart data EDA notebook>>

stores.drop_duplicates(inplace=True)
stores.dropna(inplace=True)

# Merge Sales and Stores data
walmart = pd.merge(sales, stores, how='inner')  

# Convert Date to datetime Type
walmart['Date'] = pd.to_datetime(sales['Date'])

# Add additional columns derived from date 

walmart = walmart.assign(day_name = walmart['Date'].dt.day_name(), 
             is_weekend = np.select ([(walmart['Date'].dt.dayofweek).isin([5,6])], 
                                      [1], default=0 ),
             quarter = walmart['Date'].dt.quarter, 
             month = walmart['Date'].dt.month
             )
walmart.info()

# Convert cateogorical variables to 'Categorical varibales'
cat_var =['IsHoliday', 'day_name', 'is_weekend', 'quarter', 'month', 'Type']
for cat in cat_var:
    walmart[cat] = pd.Categorical(walmart[cat])

# for applying ML Models ignoring storeId, dept_id and date     
data = walmart[['month', 'quarter', 'is_weekend', 'day_name', 'IsHoliday',
                'Size', 'Type', 'Weekly_Sales' ]]

pd.to_pickle(data, 'dataset/walmart/data.pkl')
    
# =============================================================================
#       Load preprocessed data
# =============================================================================

data = pd.read_pickle('dataset/walmart/data.pkl')
#X = data.iloc[:, :-1].values
#y = data.iloc[: , -1].values   # Weekly_sales

# =============================================================================
#                            CLUSTERING 
# =============================================================================
# >>Things to consider:
# 1) Do I need to scale data?
# 2) Are there any categorical variables in the data that i need to dummify?
# 3) What parameters do I need to specify?
# 4) Can I plot my results? Explain the reasoning
#
from sklearn.cluster import KMeans

# =============================================================================
# 
# GOAL-1 ---> cluster stores based on size and analyze if same sizes fall under 
#             same cluster as in original data            
# 
# =============================================================================

Xc= data['Size'].values
yc = data['Type'].values
wcss = []
for i in range(1,15):
    kmeans = KMeans(n_clusters = i, init='k-means++', random_state=0)
    kmeans.fit(Xc)
    wcss.append(kmeans.inertia_)
    
    
    
'''
GOAL-2 --> cluster stores based on store sizes and weekly_sales
'''
Xc= data[['Size', 'Weekly_Sales']]
yc = data['Type']

# kmeans gives clusters as 0 to k numbers 
y_c = np.select([data['Type'] == 'A',  
               data['Type'] == 'B', 
               data['Type'] == 'C'], [0,1,2])

# sacle data
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
Xc = sc.fit_transform(Xc)

# KMEANS CLUSTERING
from sklearn.cluster import KMeans

# Determine Number of cluster, plot elbow curve
wcss = []
for i in range(1,15):
    kmeans = KMeans(n_clusters=i, 
                init='k-means++', 
                random_state=0)
    kmeans.fit(Xc)
    wcss.append(kmeans.inertia_)
    
# plot 
plt.plot(range(1,15), wcss)    
plt.title('KMeans Elbow curve on Walmart data')
plt.xlabel('WCSS')
plt.ylabel('Number of Clusters')
plt.show()

#<<IMPORTANT>> Elbow is at k=6 
# Now lets try to puild cluster by specifying the value of k 

kmeans = KMeans(n_clusters=3, 
       init='k-means++', 
       random_state=0, 
       verbose =0)

y_kmeans = kmeans.fit_predict(Xc)


#
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_c, y_kmeans)
cm


'''
GOAL-3 ---> cluster stores based on all varaibles (numerical +categorical) and 
            see how it is different than actual store Types
'''


'''
GOAL-4 ---> Find Principle componendts and then clustering on components 
            that explain at least 70% total varaibles of data
'''








# =============================================================================
#       REGRESSION - Predict Weekly Sales 
# =============================================================================



# =============================================================================
# 
# =============================================================================












