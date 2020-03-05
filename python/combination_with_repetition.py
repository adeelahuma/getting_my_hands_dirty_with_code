#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 14:37:25 2020

@author: adeela
"""

'''
Implement combination with Repition

>> https://www.mathsisfun.com/combinatorics/combinations-permutations.html
>> https://www.cs.sfu.ca/~ggbaker/zju/math/perm-comb-more.html

'''

from itertools import product, combinations, combinations_with_replacement

# =============================================================================
#    Things to remember is DIFFERENTIATE between ORDER and REPETITION
#    In COMBINATIONS ORDER DOESN'T matter BUT items can or cannot be repeated 
# =============================================================================


# =============================================================================
#   CARTESIAN Product
# =============================================================================
A = list('ABC')
cartesian_p = [(a,b) for a in A for b in A]
cartesian_p
len(cartesian_p) # size equals to len(A) * len(A)

## ITERTOOLs way 
p = list(product(A, A))
print(p)
len(p)


# =============================================================================
#       COMBINATIONS ORDER DOES NOT MATTER (AB is same as BA) 
#       --- Combinations w/o replacement
#       --- Combinations with replacement
# =============================================================================
#In a set with elements [A,B,C], combiations taken 2 at a time--> 
#    will not include both combination AB, BA. It will be either AB or BA 
#    because order DOESN'T matter. Its the same group of elements 

# =============================================================================
#       Combinations with out Replcaemnet/Repetition 
# =============================================================================

# FORMULA to know how many combinations will be there -->
#     n!/r!(n-r)!    ; r = how many elements to choose 
#
# In this approach, while selecting combinations taken 2 at a time, combos 
#   that have similar element twice such as AA, BB, CC are not selected

# <<IMPORTANT>> This is what is mostly needed in a nested comparison loop 
# where we don't want to test an item with itself (i == i) AND also don't want 
# to do test two items twice (i == j) or (j == i). One test (i == j) is enough 

c = list(combinations(A, 2))
print(c)
len(c)


# =============================================================================
#       Combinations with out Replcaemnet/Repetition 
# =============================================================================
#
#
# In this approach, while selecting combinations taken 2 at a time, combos 
#   that have similar elements twice such as AA, BB, CC ARE also selected.

# FORMULA to know hjow many combinations will be there-->
#    (n+r-1)! / r!(n-1)!

# <<IMPORTANT>>For example, 
#    choosing two candies out of 3; selecting two chocolate candies(AA)
#    is fine (Repetition is allowed) whereas selecting 
#   'one chocolate and one vanilla'(AB) is same as selecting 
#   'one vanilla and one chocolate'(BA) (Order Doesn't matter)
#
#

cc = list(combinations_with_replacement(list('ABC'), 2))
print(cc)
len(cc)