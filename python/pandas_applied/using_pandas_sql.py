#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: adeela
"""

'''
https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html
Pandas group by() >> https://www.drawingfromdata.com/filter-transform-group-with-pandas


'''
import pandas as pd
import numpy as np 

data_url = url = ('https://raw.github.com/pandas-dev/pandas/master/pandas/tests/data/tips.csv')
tips = pd.read_csv(url)

tips.describe()

tips.head()


# =============================================================================
#       SQL SELECT
# =============================================================================
'''
Select * from tips limit 10

'''

tips.head(10)

'''
Select total_bill, tip, time from tips limit 10
'''
tips[['total_bill','tip','time']].head(10)

'''
For a calculated column such as : 
>> Select *, tip/total_bill as tip_percentage from tips limit 10
'''
#assign() returns all columns in addition to the columns calculated within assign
tips.assign(tip_percent= tips['tip']/tips['total_bill'])

tips.assign(tip_percent= tips['tip']/tips['total_bill'], 
            tip_percentage= round((tips['tip']/tips['total_bill'])*100)).head()


### To add a new calculated column in the data
tips['tip_percentage'] = round((tips['tip']/tips['total_bill'])*100)
tips.describe()


# =============================================================================
#       SQL WHERE 
# =============================================================================

'''
Select total_bill, tip, time from tips where time ='Dinner'limit 10
'''

# the following code returns a Series of boolean. True where condition is met
is_dinner = tips['time'] == 'Dinner'
is_dinner.value_counts() ## tabulation of data

tips[tips['time'] == 'Dinner'].head(10)

# Can also do as below, its same as above line
tips[is_dinner].head(10)


'''
Select total_bill, tip, time from tips where time ='Dinner' and tip > 5 limit 10
'''
# & (ampersand) is used for bit wise comparison. In below case it returns 
# cases where both boolean are true. 
# If we use 'and' operator that means all or none

tips[(tips['time'] == 'Dinner') & (tips['tip'] > 5.0) ].head(10)

'''
Select total_bill, tip, time from tips where total_bill > 50.0 or tip > 5 limit 10
'''
# | (verical bar meaning or) is used for bit wise comparison. 

tips[(tips['total_bill'] > 50.0) | (tips['tip'] > 5.0) ][['total_bill', 'tip', 'time']].head(10)

# =============================================================================
#   IS NA and NOT NA
# =============================================================================

df = pd.DataFrame({
        'col1': ['a','b',np.nan, 'd'], 
        'col_2': [1,np.nan, np.nan, 100]
        })

'''
Select * from df where col_2 = Null
'''    
df[df['col_2'].isna()]

'''
Select * from df where col_2 IS NOT Null
'''    
df[df['col_2'].notna()]

# =============================================================================
#       SQL IN
# =============================================================================

'''
Goal : select where tip is 2 or 5 or 3
Select * from tips where tips in (2,5,3)
'''

tips[tips['tip'].isin([2,5,3])]     

# =============================================================================
#   GROUP BY
# =============================================================================
## groupby --> split the data into group, apply some functuon and then combine
# the groups together

'''
Select count(*), sex from tips
groupby sex
'''
# IMPORTANT: In pandas we use size() NOT count(), because count() applies the 
# function to each column 
 
tips.groupby(by = 'sex').size()
tips['sex'].value_counts()

# we could have applied count() to individual column 

tips.groupby(by ='sex')['total_bill'].count()

'''
Q:  how tip amount differs by day of the week. In other words, how mnay tips
you got on each day and what was avergae of tips for that dat

Select day, count(tip), avg(tip)
from tips
groupby day

'''
##IMPORTANT: value_counts() works on series not data frame. 
# 
tips[tips['day'] == 'Fri']['day'].value_counts()

#with apply(), you can apply only one function 
#with aggregate function agg() can apply multiple functions on DIFFERENT columns
tips.groupby(by='day')['tip'].apply(np.sum)

tips.groupby(by='day').agg({'tip':[np.size, np.mean],
                            'day': np.size})

'''
GROUP BY Multiple columns 

Select day, count(tip), avg(tip)
from tips
groupby smoker, day

'''
tips.groupby(by = ['day', 'smoker']).agg({
        'day': np.size, 
        'tip': np.mean
        })

# =============================================================================
#           GROUP BY Filter ()  equivalent to  sql having
# =============================================================================

#<<IMPORTANT>> Returns back rows matching the condition in filter 
    
'''
Select day, avg(total_bill)    
from tips
groupby day 
having avg(total_bill) > 21
'''    
   
tips.groupby(by='day')['total_bill'].filter(lambda x : x.mean() > 21) 
    
# =============================================================================
#           Group by transform()    
# =============================================================================
    
#<<IMPORTANT>> returns the same number of rows. Used to do some transformation 
# on each value and returns transformed value

tips.groupby(by='day')['tip'].transform(lambda x: round(x.mean(), 2))

# =============================================================================
#       JOIN
# =============================================================================
'''
Two options in pandas : join() , merge()
join() by default joins on indices
    
'''

df1 = pd.DataFrame({
        'key':['A', 'B', 'C', 'D', 'E', 'F'],
        'value': np.random.randn(6)
        })

df2 = pd.DataFrame({
        'key':['B', 'B', 'A', 'G', 'E', 'H'],
        'value': np.random.randn(6)
        })

    
df3 = pd.DataFrame({
        'key':['B', 'B', 'A', 'G', 'E', 'H'],
        'key_2': [10,20,30,40,50,60], 
        'value': np.random.randn(6)
        })

df4 = pd.DataFrame({
        'key':['B', 'B', 'A', 'G', 'E', 'H'],
        'key_2': [10,70,30,80,20,60], 
        'value': np.random.randn(6)
        })
    
# =============================================================================
#   INNER JOIN
# =============================================================================
'''
select *
from df1 and df2 
where df1.key = df2.key

OR 

select *
from df1 inner join df2 
on df1.key = df2.key

'''

# merge performs inner join by default 
pd.merge(df1,df2,on='key')


# =============================================================================
#   LEFT OUTER JOIN
# =============================================================================
#ALL Records from df1 + matched

pd.merge(df1, df2, on='key', how='left')


# =============================================================================
#   RIGHT OUTER JOIN
# =============================================================================

#All recrds from df2 + matched

pd.merge(df1, df2, on='key', how='right')

# =============================================================================
#   FULL JOIN
# =============================================================================
# All records from both tables

pd.merge(df1, df2, on='key', how='outer')


# =============================================================================
#  Joining on multiple keys 
# =============================================================================


pd.merge(df3, df4, left_on=['key', 'key_2'], right_on=['key', 'key_2'])

# OR If column names are same, we can use following syntax as well
pd.merge(df3, df4, on=['key', 'key_2'])
 
# =============================================================================
#   UNION ALL vs UNION
# =============================================================================

# union all combines all records and can have duplicates
pd.concat([df3.iloc[:,:2], df4.iloc[:,:2]])

# sql union 
pd.concat([df3.iloc[:,:2], df4.iloc[:,:2]]).drop_duplicates()


# =============================================================================
#   UPDATE 
# =============================================================================

tips['desired_tip'] = round(tips['total_bill']*.25, 1)
tips['flag_tips'] = False

'''
Update tips
set flag_tip =  True
where abs(desired_tip, tip) > 3
'''
#IMPORTANT SYNTAX --> 
#   df.loc[filter_criteria_for_row_selection, column_to_be_updated]
tips.loc[(tips['desired_tip'] - tips['tip']) > 3 , 'flag_tips'] = True

# 47 cases of tips SERIOUSLY needs to be looked at ;)
tips['flag_tips'].value_counts()


# =============================================================================
#   DELETE
# =============================================================================

# Syntax same as update. MAIN DIFFERENCE is 'filter criteria' should pick rows 
# that should not be deleted

'''
Delete tips
where tip_percentage > 30  # NO ONE TIPS that high ;)
'''

# TO BE DELETED CASE 
tips.loc[tips['tip_percentage'] > 30]

# Assign the reverse of it to tips data frame

tips = tips.loc[tips['tip_percentage'] < 30]


# =============================================================================
#   FANCY WINDOWS FUNCTIONS
# =============================================================================


'''
Q: Top 'n' rows per group 
LOGIC:
    > first sort rows
    > partition by day
    > add a column for cumulative count within parition
    > get first 'n' record from each partition

    select * from 
    (select t.*, row_number() over (partition by day order by total_bill) as rn
    from tips t ) where row_number < 3 
'''
#Cumcount -->
#Number each item in each group from 0 to the length of that group - 1.

tips.groupby('day').agg({'tip': np.size})

temp = tips.assign(rn = tips.sort_values(by =['total_bill'], ascending=True).
                   groupby(by='day').cumcount()+1)

# query() -->
#Query the columns of a DataFrame with a boolean expression.
temp.query('rn < 3').sort_values(by=['day', 'rn'])
tips.query('(total_bill >20 & total_bill <25) & tip< 5 & sex==\'Female\'')
##IMPOFRTANT : Do we need to sort before partitioning? 
# YES, answer will be different , see below code
tips.assign(rn=tips.groupby(by= 'day').cumcount()+1).query('rn < 3').sort_values(by=['day', 'rn'])


# Solution using rank()

temp_2=tips.assign(rn=tips.groupby(by='day')['total_bill'].rank(method='first',ascending=False))
temp_2.query('rn < 3')


'''
Question --> Let’s find tips with (rank < 3) per gender group for (tips < 2)
'''
# rank(method='min') means that while ranking if two values has the same value 
#   then assign the same rank to them in this case the minimum value
temp_tip= tips.assign(min_tip =tips[tips['tip'] < 2].groupby(by='sex')['tip'].rank(method='min'))
temp_tip.query('min_tip < 3')



'''
 Top 'n' rows with an offset 
'''
#nlarhest () -->Return the first n rows ordered by columns in descending order
#nsmalles() reverse of nlargest()

tips.nlargest(10, 'tip').tail(5)

tips.nsmallest(10, 'tip').tail(5)


tips.nlargest(10, 'tip')
