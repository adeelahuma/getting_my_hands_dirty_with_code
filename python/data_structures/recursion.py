#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 11:09:33 2020

@author: adeela
"""

'''
Link: https://www.khanacademy.org/computing/computer-science/algorithms/recursive-algorithms/a/recursion

 What is a recursive Algorithm?
 an algorithm to solve a problem by solving a smaller instance of the same problem, 
 unless the problem is so small that we can just solve it directly.
 We call this technique recursion.
 
 We can distill the idea of recursion into two simple rules:
     1) Each recursive call should be on a smaller instance of the same problem, 
        that is, a smaller subproblem.
    2) The recursive calls must eventually reach a base case, 
        which is solved without further recursion.
'''

'''
Example 1: Factorial  n! = n*(n-1)*(n-2)*...*2*1

Factorial is helpful in finding the permutations and combinations
'''


# =============================================================================
#       Iterative Factorial
# =============================================================================

#make sure n >= 0, else wrong result
def factorial(n):
    n_factorial = 1
    for i in range(1,n+1):
        n_factorial *= i
    return n_factorial
    


assert factorial(0) == 1, '0! = 1'
assert factorial(1) == 1, '1! = 1'
assert factorial(5) == 120, '5! = 120'


# =============================================================================
#       Recursive Factorial 
# =============================================================================

#make sure n >= 0, else it would never hit base case and would keep recursing 
#forever
def r_factorial(n):
    if n == 0:          #base case 
        return 1
    else:               #recursive case
        return n* r_factorial(n-1)

assert r_factorial(0) == 1, '0! = 1'
assert r_factorial(1) == 1, '1! = 1'
assert r_factorial(5) == 120, '5! = 120'



# =============================================================================
#       Memoized Recursive Factorial
# =============================================================================
'''
    Memoization (a form of caching) remembers the result of a function call 
    with particular inputs in a lookup table (the "memo") and 
    returns that result when the function is called again with the same inputs.
    
    Memoization makes a trade-off between time and space.
    As long as the lookup is efficient and the function is called repeatedly, 
    the computer can save time at the cost of using memory to store the memo.
    
    The memoized algorithm does requires more space, however; 
    enough for the memo to store every return value of n

    
'''
memo = {}
def memo_factorial(n):
    
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    else:
        n_fact = n * memo_factorial(n-1)
        memo[n] = n_fact
        return n_fact
 
assert memo_factorial(0) == 1, '0! = 1'
assert memo_factorial(1) == 1, '1! = 1'
assert memo_factorial(5) == 120, '5! = 120'       
        


# =============================================================================
#   Palindrome  ( Implemented Recursively)
# =============================================================================

'''
    A palindrome is a word that is spelled the same forward and backward. 
    For example, rotor, 02022020 is a palindrome
    
    - String with zero or one letter is a palindrome
'''
#function assumes input sequence is in lower case

def isPalindrome(sequence):
    
    if len(sequence) == 0 or len(sequence) == 1:  #base case
        return True
    
    #if first and last letter in the sequnce is same or not 
    if sequence[0] != sequence[-1]:               
        return False
    else:                          #recursive-case 
        #[could potentially be a palindrome]
        # strip the first and last letter and then check if substring is a palindrome 
        return isPalindrome (sequence[0+1:-1])
    
        
 
assert isPalindrome('') , 'Empty Sequence'
assert isPalindrome('a') , 'Sequence of length 1'    
assert isPalindrome('rotor') , 'odd sequence Palindrome'
assert isPalindrome('02022020') , '2nd Feb 2020'


# =============================================================================
#   Computing Power of a number  x^n
# =============================================================================

def power(x, n):
        
    if n == 0:
        return 1
    
    if n == 1 or n == -1:
        if n == 1:
            return x
        else:
            return 1/x
    else:
        if n > 1:
            return x * power(x,n-1)
        else:
            return 1/x * power(x,n+1)



assert power(0,0) == 1
assert power(3,0) == 1 
assert power(3,1) == 3 
assert power(3,2) == 9
assert power(3,3) == 27
assert '{0:.2f}'.format(power(3,-1)) == '0.33'   
assert '{0:.2f}'.format(power(3,-2)) == '0.11'   


# =============================================================================
#        Fibonacci
# =============================================================================

'''
The Fibonacci sequence is a famous series of numbers where the next number in 
the sequence is the sum of the previous 2 numbers. 
The first two numbers in the sequence are defined as 0 and 1. After that, 
the next number is 1 (from 0 + 1) and the number after that is 2 (from 1 + 1), 
and so on.
The first 10 Finoacci numbers are: 
    0 1 1 2 3 5 8 13 21 34
'''

# =============================================================================
#       Recursive Fibonacci
# =============================================================================

%time
def fibonacci(n):
    
    if n == 0 or n == 1:
        return n 
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
    
assert fibonacci(0) == 0
assert fibonacci(1) == 1 
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(9) == 34 
    
# =============================================================================
#       Recursive Fibonacci with memoization    
# =============================================================================
%time
fib_memo = {}
def fibonacci(n):
    
    if n == 0 or n == 1:
        return n
    else:
        if n in fib_memo:
            return fib_memo[n]
        else: 
            fib = fibonacci(n-1) + fibonacci(n-2)
            
            fib_memo[n] = fib
            
        return fib
    

assert fibonacci(0) == 0
assert fibonacci(1) == 1 
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(9) == 34 

    
# =============================================================================
#       Fibonacci Bottom Up Technique    
# =============================================================================
    
%time
def fibonacci(n):
    
    if n == 0 or n == 1:
        return n
    
    n1 = 0
    n2 = 1  
    final_fib = 0 
    
    for i in range(n-1):
        final_fib = n1 + n2
        n1 = n2 
        n2 = final_fib

    return final_fib
        
assert fibonacci(0) == 0
assert fibonacci(1) == 1 
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(9) == 34 
    
    
'''
Memoization and bottom-up are both techniques from dynamic programming, 
a problem-solving strategy used in mathematics and computer science.
Dynamic programming can be used when a problem has optimal substructure and 
overlapping subproblems.

'''    
    
# =============================================================================
#       Sierpinski Triangle
# =============================================================================

#TBD

import turtle
turtle.forward(15)



















   
        