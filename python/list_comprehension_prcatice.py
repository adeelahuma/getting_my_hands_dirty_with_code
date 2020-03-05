#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 20:09:12 2020

@author: adeela
"""

'''

https://www.thepythoncorner.com/2017/12/the-art-of-avoiding-nested-code/
https://nedbatchelder.com/text/iter.html
https://nedbatchelder.com/blog/201608/breaking_out_of_two_loops.html
https://book.pythontips.com/en/latest/map_filter.html
Good Explanation of reduce() at the top --> 
    https://www.geeksforgeeks.org/reduce-in-python/

'''

# =============================================================================
#   find odd numbers in list  using list comprehension
# =============================================================================

A = [1,2,3,4,5,6,7,8,9,11]

##same old for loop
O = []
for x in A:
    if x % 2 != 0:
        O.append(x)        
        
## fancy straight forward list comprehension syntax        
X = [x for x in A if x%2!=0]        
print(X)


# =============================================================================
#    Manipulate elements in the list   
# =============================================================================
# add letter 'a' times the element in the list
import itertools
#itertools.chain(*E) --> E is a list of lists and choice() flattens it to one list
B = [1,3,4,5]

B_ = ['a '* i for i in B]
print(B_)
# output --> ['a ', 'a a a ', 'a a a a ', 'a a a a a ']

#Now let's suppose C represents the weights of elements in array B 
# we can multiple weights OR we would like to exapnd elements in B as per weights in C 
C = [4,5,2,1]
#explanation of line 76 
# integer * string means string is replicated number of times indicated by integer 
# join in this case is adding space between each element of string we got from step 1; its still one string
# split() will make split the string and put each element as a separte element in list
# 4 * '1' --> '4444' -->'4 4 4 4' --> ['4', '4', '4', '4']
 
E = [(' '.join(C[i]* str(B[i]))).split(' ') for i in range(len(B))]
E = list(itertools.chain(*E))  # flatten list of list 
E = [int(x) for x in E ]       # convert to integer list 

# =============================================================================
#       Filter the numbers from list using list comprehension vs filter()
# =============================================================================

#filter out number that are NOT multiple of 11 

#LIST COMPREHENSION way
X = [1,2,3,4,5,5,6,7,11,22,55,44]

multiples_11 = [x for x in X if x%11 == 0]

# FILTER way 
# filter (function_to_apply, Iterable) and it returns Iterable object thats
# why we need to wrap the results in list() to get a list object 
# lambda lets us define an anonymus function 
#
multiples_11_f = list(filter(lambda x: x%11==0, X))


# =============================================================================
#       Find coordinate pairs using zip() vs list comprehension
# =============================================================================

X = range(0,100, 1)   # numbers from 0 to 100 with jump_size == 1
Y = range(0,200, 2)   # numbers from 0 to 200 with jump_size == 2

# create (x,y) pairs by combining elements in both list by indices 
# meaning x0 combined with y0, x1 with y1 and so on. 
# The final size of list is same as size of X or Y
X_Y = list(zip (X,Y))   

# this gives the cartesian pair of tuples 
X_Y_cartesian = [(x, y) for x in X for y in Y]

# Now we can expnd it further to filter out some of the pairs
# only pairs where both x and y is positive 
X_Y_cartesian_even = [(x,y) for x in X for y in Y if x%2== 0 and y%2==0]


# =============================================================================
#       sum(product) numbers using list comprehension vs reduce() 
#                                                       from functools library
# =============================================================================

X =  range(1,100)

# Plain old way to calculate sum 
temp = 0 
for x in X:
    temp +=x
    
# As per google search sum not possible via list comprehension

from functools import reduce
#Using reduce() ; It takes lambda function with two inputs only    
# first x and y are first two elements of list and its result s computed then 
# in the next iteration next element and result from prevuious 
# computation is picked and result is computed and so on

X_sum = reduce(lambda x,y: x+y, X)  


# =============================================================================
#   changing elements of the list via map() vs list comprehension
# =============================================================================
 
# Task: convert all elments in a list of int to string and append a space after 
# the number

X = range(1,5)

# plain old way to do it 
X_m= []
for x in X:
    X_m.append(str(x) + '  ')

# list comprehension 
    
X_m = [str(x)+ ' ' for x in X]

# map() , map also returns an Iterable object so we need to wrap it with list()
# to get list of elements

X_m = list(map (lambda x: str(x) + ' ', X ))










