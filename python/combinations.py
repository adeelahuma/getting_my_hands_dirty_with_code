#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:49:04 2020

@author: adeela
"""

#Read Article: https://realpython.com/python-itertools/
# Question is how to extend it for to ncr where r can be 1, 2, 3,.. 
#def combinations_with_repetition():
nc1 = {'A', 'B' ,'C'}
nc2 =set()

for i in nc1:
    for j in nc1:        
        
        x = i+j    
        new_combo = ''.join(sorted(x))
        print(x, new_combo)
        if i == j: # same elements (AA, BB, CC)
            #ignore combo
            print('same element')
                 
        if new_combo in nc2:  #same elements , different positions
            #ignore combo    
            print('reverse elmenet')
        
        nc2.add(new_combo) 

print(nc2)        



# =============================================================================
#  =============================================================================
#  list(zip([1,2,3],['A', 'B', 'C']))  # combining elements of both arrays by position
#  list(map(len,['AA','BBX','A']))  # applying function len on each element of array
#  
#  list(zip([(1,2,3), (3,4,5)], [(10),(10)]))
#  list(map(sum, zip([1,2], [10,10])))
#  =============================================================================
# 
# =============================================================================
