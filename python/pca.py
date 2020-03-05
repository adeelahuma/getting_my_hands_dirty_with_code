#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 13:52:37 2020

@author: adeela
"""

'''
Links:
    >> https://stats.stackexchange.com/questions/2691/making-sense-of-principal-component-analysis-eigenvectors-eigenvalues/140579#140579
    




'''

# =============================================================================
#               What is PCA?? 
# =============================================================================
'''
 Its a way of summarizing the data
 Example : You have different wine bottels and each can be described by its color, 
 age, strength etc. But some of these atributes will be related  and will be 
 redundant. SO we should summarize each wine with fewer attributes 
 
 Q--> does PCA finds redundant attributes and discards them?
 No, It creates new atributes using the old ones that summarizes our data
 (aka linear combinations). Such as calculating new attribute by subtracting 
 wine_age and aciditity level. 
 
 Q--> How does PCA summarize the data?
 We are looking for wine attributes that 
     1) strongly differ across wines and
     2) allow to reconstruct the original wine attributes
Suppose , If we come up with an attribute that is same for all wines; wines are 
different and this new attribute makes to look all wine same. This would be bad 
summary. 
>> PCA looks for properties that show as much variation across wines as possible
Now suppose, you come up with a new property that has no relation to original 
attributes, if we use ths we can't reconstruct data.This is again bad summary. 
>>PCA looks for attributes that allow to reconstruct the original attributes as well.

Q--> 
    
    
'''
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt



data = pd.read_csv('dataset/Wine.csv')

# .values creates a numpy matrix or array
X = data.iloc[:, 0:13].values 
Y = data.iloc[:, -1].values

from sklearn.model_selection import train_test_split
train_X, test_X, train_Y, test_y = train_test_split(X, Y, test_size=0.2, random_state=0)


#Feature Scaling MUST be applied when we apply dimensionality reduction techniques 
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
train_X= sc.fit_transform(train_X)
test_X = sc.transform(test_X)

# Applying PCA after data preprocessing and before model 
from sklearn.decomposition import PCA
pca = PCA(n_components = 2 )
train_X = pca.fit_transform(train_X)
test_X = pca.transform(test_X)
explained_variance = pca.explained_variance_ratio_

#Model 
from sklearn.linear_model import LogisticRegression
lc = LogisticRegression()
lc.fit(train_X, train_Y)

y_pred = lc.predict(test_X)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(test_y, y_pred)


# Visualising the Training set results
from matplotlib.colors import ListedColormap
X_set, y_set = train_X, train_Y
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, lc.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green', 'blue')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green', 'blue'))(i), label = j)
plt.title('Logistic Regression (Training set)')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.legend()
plt.show()




# Visualising the Test set results
from matplotlib.colors import ListedColormap
X_set, y_set = test_X, test_y
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, lc.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green', 'blue')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green', 'blue'))(i), label = j)
plt.title('Logistic Regression (Test set)')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.legend()
plt.show()













