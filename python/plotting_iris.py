#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 21:11:49 2020

@author: adeela
"""

'''
iris dataset

>>Seaborn documentation: https://seaborn.pydata.org/api.html

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

irisdf = pd.read_csv('https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/d546eaee765268bf2f487608c537c05e22e4b221/iris.csv')

from pandas.plotting import scatter_matrix
scatter_matrix(irisdf)

'''
It shows multiple graphs together and letting us see in one graph 
>> sepal_length vs petal length : As sepal length increases , sepal length also increases
>> Diagonal plots are histograms of the varibale. No points of plotting x1 vs x1
>> histogram : tells the distribution of values.  At diferent sepal length values how many data points i have

'''

# want more functionality that pands is not provinding then we go to seaborn 
sns.pairplot(irisdf, hue='species')
plt.show()
'''
species column is providing the color [categories]
Now just by looking at graph i can do some classification in my head. 
>>Look at column for 'petal_length', i can see that if petal_length is less than 2;
sepcies is 'setosa'. 
Also if value is less than 5 there is a higher chance that this is 'versicolor'
>>Also if i look at petal_width vs petal_length, i can see a clean distinction
 between three classes

'''


'''
Line Plot --> shows a line
'''
# both works, hue shows coloring by the category
sns.lineplot(data=irisdf, x= 'petal_length', y ='petal_width')
sns.lineplot(data=irisdf, x= 'petal_length', y ='petal_width', hue='species')
plt.show()

'''
Scatter_plot --> shows points
'''
#both works
sns.scatterplot(data=irisdf, x= 'petal_length', y ='petal_width')
sns.scatterplot(data=irisdf, x= 'petal_length', y ='petal_width', hue='species')
plt.show()

#Seaborn 
'''
Relplot --> how continous values are related to each other 
'''
sns.relplot(data= irisdf, x= 'petal_length', y ='petal_width', hue = 'species')
plt.show()

#show data per category in a separte COLUMN for each category 
sns.relplot(data= irisdf, x= 'petal_length', y ='petal_width', hue = 'species', col='species')
plt.show()

#show data per category in a separte ROW for each category 
sns.relplot(data= irisdf, x= 'petal_length', y ='petal_width', hue = 'species', row='species')
plt.show()

# Let's add another category column and see how we can see graph for both 
# categorical variables
irisdf['random'] = np.random.choice(['A','B','C'], 150)

sns.relplot(data= irisdf, x= 'petal_length', y ='petal_width', hue = 'species', 
            row='species', col='random')
plt.show()

'''
With these graphs you don't need to create subplots yourself, or put different 
colors, headers etc. Seaborn is doing it for you in tandem with pandas 

Everything that line and scatter plot can do, relplot can do it as well.
By specifying the type you can change the graph i.e. kind='line' or kind='scatter'
'''

sns.relplot(data= irisdf, x= 'petal_length', y ='petal_width', hue = 'species', 
            row='species', kind='line')
plt.show()


'''
catplot() is for Categorical data. Specially when we have categorical and 
continous data together.


This can be still broken down into rows and columns 
'''

sns.catplot(data=irisdf, x='species', y='petal_length', hue='species')
plt.show()

'''
with catplot by specifying kind='box', it'll show the box plot

Box plot--> 
line in the middle = mean value
the shaded area shows that 25% to 75% data is here. The extreme lines/lines 
at both ends show 
Also 25% (first quartile), we can say that 25% values are below the Q1
Also 75% (3rd quartile), we can say that 75% values are above the Q2

area between least value and Q1 is considered outlier area?? or the outside?
the dots outside the extreme bars are outlier. We should remove them because 
they are too from from the mean value



'''

sns.catplot(data=irisdf, x='species', y='petal_length', hue='species', kind='box')
plt.show()


'''
Violin chart tells how data is distributed 
narrower the violin means less values, wider shows ther are more values in that 
range/area 
for example look at setosa's fat belly that means there are lot of values for 
petal length 1.5

This gives idea where do i have more values and where do i have less values 
and can help you make a distinction


'''

sns.catplot(data=irisdf, x='species', y='petal_length', hue='species', 
            kind='violin')
plt.show()

'''
Swarm plot:
    like a scatter plot , when there are too many values it speards out so that 
    you can see the actual values. it does not put them on too of each other 
'''

sns.catplot(data=irisdf, x='species', y='petal_length', hue='species', 
            kind='swarm')
plt.show()


'''
Above plots show how data is distributed 
To go adavnce we can use lmplot()
>> library does  acvery simple linear regression and thats how the line has 
come.
Line in the graph is the best fit line. The shaded region shows the confidence 
interval 
For the setosa line, there is no data toward the end, so its not possible to 
know for the system if the prediction will be accurate this far from the given data 
thats why the confidence interval is too large
>> in other words, also its ability to predict is decreasing as we move away 
from middle point where mostly data is located.
>> for green and orange line we have larger spread of data thats why error 
margins are much smaller
>> when the shaded area is smaller that means higher predictability, less error, 
the more sure you are about the result
>>
>> gives a scater plot and a regression line 
Suppose aim was to use 'petal_length' to figure out 'sepal_length', 
lines ae different for each species. So, species is a good way to segregate the data before i build the model. 
I should build model seperately for each species 

'''

sns.lmplot(data=irisdf, x='petal_length', y ='sepal_length', hue='species')
plt.show()

'''
When we add another category 'random', we can see that when random=C, 
the lines are closer, when random = B, we strat to see differences and 
for random A its very different for setosa but almost same for other two categories.
So we should build a seperate model for setosa 
'''

sns.lmplot(data=irisdf, x='petal_length', y ='sepal_length', hue='species', 
           col='random')
plt.show()


'''
graph tells that sepal_length tends to increases as petal_length increases.
Its sharp for 'setosa' but not much sharper for 'virginica' and 'versicolor'
2) for setosa data is concentrated around 2, if we expect petal length away 
from 2 then you need to add data away from 2 so that margin of error 
(light blue shaded area) starts decreasing. EVen if I hve one data point for 
setosa at petal_length=8 then suddebly the margin of error will become very small
becuase then it'll be much sure about its results

You also combine this from what you learn from histogram (scatter_plot) and say
I don't expect it to be more than 2 so I am fine


'''