#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 23:06:41 2020

@author: adeela
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
tips.head()
tips.shape

'''
though: tip may increase as bill increases . Okay lets plot a regression line
hetroscedasicity point of view : Notice the shade region around line . 
Towards the end its broader that means compared to smaller bills its less 
predictable
    
'''
sns.regplot(data=tips, x='total_bill', y='tip')
plt.show()


'''
we can solidify this by looking at correlation 
0.65 means that there could be relationship but maynot not strong, 
there might be other factors at play
'''
np.corrcoef(tips['total_bill'], tips['tip'])

# OR below code gives tuple
from scipy.stats import pearsonr
pearsonr(tips.total_bill, tips.tip)


'''
How do you pick the two attributes ? total_bills vs tips?

Answer: you build a hypothesis and see the data. E.g. 
> Maybe smokers pay more tip or the other way around
> you build your reasoning and hypothesis
> you assume the things and see if there is an affect 
>


'''

sns.lmplot(data=tips, x='total_bill', y='tip', hue='smoker')
plt.show()

'''
If you look at graph, you'll notice that the line is sharper for non-smoker that
means if you are a non-smokerm a small increase in bill gives me higher tip.
but for a smoker, total_bill has to be more to get the same tip 

'''

'''
Now we can see do men pay more tips compared to women
'''

sns.lmplot(data=tips, x='total_bill', y='tip', hue='smoker', col='sex')
plt.show()

'''
For non-smoker men and women , we almost have the same trend, but for smoker women
the uncertaininty of prediction is higher towards the end because we have less data
>> we dont have informtion about women who smoke and have bill more than $45
Even for men smoker data is less towards the end but for women more less, look 
at the wide blue shaded area 
'''

'''
Let's see who is paying more

'''

sns.lmplot(data=tips, x='total_bill', y='tip', hue='sex', col='smoker')
plt.show()

'''
Non-smokers pay more in general. Men pay slightly more 
Smoker men slightly pay more tips
Also notice that the differene between lines is so small and that maybe becuase
maybe we don't have enough data to distinguish it. Maybe 'sex' as a column is
not a great column to differentiate tips vs bills

'''


'''
Since we have time lets look at that as well

'''

sns.lmplot(data=tips, x='total_bill', y='tip', hue='sex', col='smoker', 
           row='time')
plt.show()

'''
Non-smoker generally give more tip, even at lunch time

'''

'''
Secondary analaysis 
>> what's the difference between number of smokers between men and women 
'''

sns.catplot(data=tips, x='smoker', y='tip', hue='sex', kind='violin')
plt.show()


'''
above plot giving you the distribution of population 
'''


'''
cross-tab:
how many values are there for each of the categories we have
'''

tips.groupby(by=['smoker', 'sex']).size()

'''
notice we have more data for men compared to women.
ML model will give better prediction for group that has more data at the cost 
of other parts of the data 

look for overfitting for that group 

'''

'''
Another way to do cross tab is below.
Gives more readabale format 
'''

pd.crosstab(tips.smoker, tips.sex)

# now we can also see smokdr with time 
pd.crosstab([tips.smoker,tips.time], tips.sex)


'''
This is all giving you idea about data, what data you have
As a data scientist you want to lok at as much patterns as possible

One thing you might do is create a pivot 
lets see how tips are distributed accross different categories
'''

pd.pivot_table(data = tips, 
               index=['smoker', 'time'],
               columns='sex',
               values='tip', 
               aggfunc=[np.mean, np.max, np.min])

'''
Based on this you can build a startegy, who should i table for. 
If  i want a gaurented higher tip, then i'll go to a female who is a smoker (2)
If i want to be more balanced , then i'll look at the mean value

>> if you know what strategy you want to build, if you want a safer bet then 
you can go for a strategy where you prefer minimum over the mean 
For aggresive bet, we can go for max over mean 
>>for balanced, you say okay i'll work more time then you go for mean value

When you do ML, you need to know what strategy you are going to work with.

'''

'''
Now size of table can also be looked if if plays any role in tips?
'''

'''
> I am okay to make separate model for lunch and dinner... these discussions
can be done with pear that whether we should do it or not 
'''

sns.catplot(data=tips, x='smoker', y='tip', hue='sex', kind='box')
plt.show()



'''
for a continous data look at histogram/ density plot 
distplot stands for distribution plot--> how is data distributed 
kde --> density estimate ---> smoothed out histogram/ telling probability 
of geting value at vakue x
rug --> shows data points lines at the bottom 


'''

sns.distplot(tips['tip'], kde=False, rug=True)
plt.show()


# =============================================================================
# 
# =============================================================================

smoker_data = tips.query("smoker == 'Yes'")
#regplot doesn't have hue
#sns.regplot(data=tips, x='total_bill', y='tip', hue='smoker')
sns.lmplot(data=tips, x='total_bill', y='tip', hue='smoker')
plt.show()

from pandas.plotting import scatter_matrix
scatter_matrix(tips)


scatter_matrix(tips[tips['smoker'] == 'Yes'])
plt.show()

# 
sns.pairplot(data=tips, hue='smoker')


'''
jointplot() combines the information of lmplot and histogram 

'''

sns.jointplot('total_bill', 'tip', data=tips, kind='reg')
plt.show()


'''
So what we usually do ?
various ways to look at data and try to see patterns

>> Identify the column, what it means, their types (cat, continous, dates)
Rule of thumb --> if a column has few values then its categorical ; 
if unique_cat < sqrt(number of rows) then can consider it as categorical data
if the values have meaning relative to each other -->continous











'''





