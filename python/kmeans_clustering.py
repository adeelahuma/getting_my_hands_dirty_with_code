#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 12:53:37 2020

@author: adeela
"""

'''
K-Means Clustering 

GOAL: Segment the Malls data based on 
    the annual income and spending score
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#TODO >>  how to not use default pandas index while reading file and 
# how to specify index by specifying a column name
data = pd.read_csv('dataset/Mall_Customers.csv')

# note using array syntax to specify the columns to pick
# .values convert the dataframe to array
X = data.iloc[:,[3,4]].values

# Using Elbow Method to find the optimal number of clusters
from sklearn.cluster import KMeans

wcss = [] 

for i in range(1,11):
    kmeans = KMeans(n_clusters=i, 
                    init='k-means++', 
                    max_iter=300, 
                    n_init= 10, 
                    random_state = 0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()


## At k=5 is elbow

## Applying the k-means to data
kmeans = KMeans(n_clusters =5, 
                init='k-means++', 
                max_iter=300, 
                n_init =10, 
                random_state = 0)

#for each observation tell to which cluster customer belongs
y_kmeans = kmeans.fit_predict(X)

#Visualizing the clusters
# ONLY for two dimensions
# for higher dimensions, reduce the dimension and can then plot 
# it on reduced dimension
# scatter plot of all observations
##X[y_kmeans ==0] cluster one observations
#<<IMPORTANT >> analysis of results is very important 
plt.scatter(X[y_kmeans ==0, 0], X[y_kmeans ==0, 1], s=100, c='red', label='Cluster 1')
plt.scatter(X[y_kmeans ==1, 0], X[y_kmeans ==1, 1], s=100, c='blue', label='Cluster 2')
plt.scatter(X[y_kmeans ==2, 0], X[y_kmeans ==2, 1], s=100, c='green', label='Cluster 3')
plt.scatter(X[y_kmeans ==3, 0], X[y_kmeans ==3, 1], s=100, c='cyan', label='Cluster 4')
plt.scatter(X[y_kmeans ==4, 0], X[y_kmeans ==4, 1], s=100, c='magenta', label='Cluster 5')

plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=300, c='yellow', label='Centroids')
plt.title('Clusters of Client')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()






