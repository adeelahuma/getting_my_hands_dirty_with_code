#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 19:00:08 2020

@author: adeela
"""

'''
Hierarchical Clustering 

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('dataset/Mall_Customers.csv')

# We dont know the categories ahead of time, we are using clustering to 
#find out thoes classes based on income and spending score

X = data.iloc[:, [3,4]].values

#find optimal number of clusters using dendogram


#scipy contains tools to do hierrichcal clustering
import scipy.cluster.hierarchy as sch
# ward method tries to minimize variance within each cluster
dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))

plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distance')
plt.show()

# we see that optimal number of clusters is 5 
# Now lets fit the HC to the dataset 

from sklearn.cluster import AgglomerativeClustering

hc = AgglomerativeClustering(n_clusters=5, 
                             affinity='euclidean', 
                             linkage='ward'
                             )
y_hc = hc.fit_predict(X)


# Visualize the results


plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], c='red', s =300, label='Cluster 1')
plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], c='blue', s =300, label='Cluster 2')
plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], c='green', s =300, label='Cluster 3')
plt.scatter(X[y_hc == 3, 0], X[y_hc == 3, 1], c='cyan', s =300, label='Cluster 4')
plt.scatter(X[y_hc == 4, 0], X[y_hc == 4, 1], c='magenta', s =300, label='Cluster 5')

plt.title('Clusters of Customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()










