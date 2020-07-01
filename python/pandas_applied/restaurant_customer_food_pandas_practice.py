#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 10:19:45 2020

@author: adeela
"""

'''
Restaurants in area server various food to customers. As long as cutomers keep 
showing  up to a restaurant regularly, that restaurant will keep serving the 
same dish.
If no customers visit a restaurant for more than 3 days, then that
restaurant will serve a new type of food starting when the next customer viists.

Unfortunately, some ingredients were containminated and caused a few customers
to suffer from food poisoning. 

The restaurants know which food was affected and
are now trying to figure out whuch customers were affected. 
The restaurants keep their own catalogue of customers, so there is no gaurentee that a customer
has the same customer ID at each restaurant. All restaurants serve food in the 
same order. Figure out which customer ate which food. 


'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_food = pd.DataFrame({'food_id': [1,2,3], 
           'food_name': ['Sphagetti', 'Chicken and Rice', 'Tacos']})

df = pd.DataFrame({
        'restaurant_id': [1, 2, 1, 3, 2, 3, 2,2,1,1,1,1,1,1,1], 
        'customer_id': [1,1,2,1,2,1,3, 3,1,1,2,4,3,5,1],
        'visit_date': ['2020-01-01','2020-01-01','2020-01-03','2020-01-04','2020-01-14', '2020-01-11', 
                       '2020-01-14', '2020-01-13', '2020-01-13', '2020-01-17',
                       '2020-01-18','2020-01-18','2020-01-28', '2020-02-02',
                       '2020-02-02']
        })

df['visit_date'] = pd.to_datetime(df['visit_date'])

df.describe
df.info()
NUM_FOOD_ITEMS = len(df_food)

# Rule 1 >> serve the 'same' food if everyday customers are showing up 
# Rule 2 >> If for more than 3 days no customer shows up then serve a new food
# Constraint 1 >> Customer Id at each restaurant is unique 
# Constraint 2 >> Every restaurant has their own record of customer Id 
# DATA given has : restaurant_id, customer_id and date 
# GOAL: figure out which food was served at each restaurant on each day  

## Shift() === lag()
df = df.assign(prev_date = df.sort_values(by ='visit_date').groupby('restaurant_id')['visit_date'].shift(1), 
                            date_diff = lambda x: x['visit_date'] - x['prev_date'])

##CONVERT the following code  TO MAKE IT PART OF ASSIGN as much as possible
## np.select is like a sql case statement
df['new_food'] = np.select([df['date_diff'] > pd.Timedelta(3, 'D'), 
           pd.isnull(df['date_diff'])], 
           ['n', 1], default='p')   

df = df.assign(rn = (df.groupby(['restaurant_id', 'new_food']).cumcount()+1)%NUM_FOOD_ITEMS)
 

# now pick food Id for 'new' food items

df['food_id'] = np.select([df['new_food'] == '1', 
           (df['new_food'] == 'n')], 
           [1, df['rn']+1], default=-99)


# now pick final food Id  <<WHAT IS A BETTER WAY TO DO IT IN PANDAS>>
sorted_df = df.sort_values(['restaurant_id', 'visit_date'])
sorted_df = sorted_df.reset_index(drop=True)
r_index = 0
for r in range(0, len(sorted_df)):
    if sorted_df.iloc[r_index, 7] == -99:
        sorted_df.iloc[r_index, 7] = sorted_df.iloc[r_index-1, 7]        
    r_index+=1    


# Now put food_id name
sorted_df = pd.merge(sorted_df, df_food, how ='inner', on='food_id')

# Final Result 
sorted_df [['restaurant_id', 'customer_id', 'visit_date', 'food_name']]
#############################

## see sorted data
df.sort_values(['restaurant_id', 'visit_date'])

## Make a bar plot to show restaurant_id on x-axis and each bar 
# reprensts diff food_items
'''
https://stackoverflow.com/questions/45299305/how-to-plot-pandas-groupby-values-in-a-graph

'''
sorted_df.plot(x='visit_date', y='food_name', type='barh')
to_be_ploted= sorted_df.groupby(['restaurant_id','food_name']).size()
to_be_ploted.plot.bar()


pd.crosstab(sorted_df['restaurant_id'],sorted_df['food_name']).plot.bar()
plt.show()


# =============================================================================
#                   Neat/Vectorized Implementation
# =============================================================================
#sort data
df = df.sort_values(by =['restaurant_id', 'visit_date'])
df = df.reset_index(drop=True)
# prev_date = group by restaurant id and shift visit date by a day (Similar to SQL lag() and lead())
# date_diff = difference between current visit and last visited customer
# new_food = specifies whether we sjhould use a new food_item or previoud day's food
# row_num = rank rows by restaurant_id, new_food--> this is used to get the id for new food item
# food_id = this is merely a almost final selection of what the final_id should be for new item

#Below code is like SQL with () caluse
df = df.assign(prev_date = df.groupby(by='restaurant_id')['visit_date'].shift(1), 
          date_diff = lambda x: x['visit_date'] - x['prev_date'],
          new_food = lambda x: np.select( [x['date_diff'] > pd.Timedelta(3,'D'), pd.isnull(x['date_diff'])], 
                                        ['n', 1], default='p'), 
          row_num = lambda x: x.groupby(by=['restaurant_id', 'new_food'])['new_food'].cumcount()+1,
          food_id = lambda x: np.select([ x['new_food'] == '1', x['new_food'] == 'n'],
                                        [1, (x['row_num']%NUM_FOOD_ITEMS)+1]), 
          final_food_id = lambda x: x['food_id'].mask(x['new_food'] == 'p').ffill() 
          )
          
          
# Now put food_id name
df = pd.merge(df, df_food, how ='inner', on='food_id')
df = df.sort_values(by =['restaurant_id', 'visit_date']).reset_index(drop=True)
# Final Result 
final_df = df.filter(['restaurant_id', 'customer_id', 'visit_date', 'food_name'])

# =============================================================================
#           Plotting on data
# =============================================================================
# Let's say now that we know whci restaurant served which food on which day.
# Let's summarize the results by week 


final_df.groupby(by=['restaurant_id', 'food_name']).size()
plt.bar(final_df.groupby(by=['restaurant_id', 'food_name']).size(), 1)
final_df.cross_tab()








