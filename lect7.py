# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 17:01:31 2020

@author: natalirs
"""

def mean(L):
    return sum(L) / len(L)

def std(L):
    '''returns std of numbers in list L'''
    u = mean(L)
    n = len(L)
    val = 0
    for i in L:
        val += (i - u) ** 2
    
    return (val / n) ** 0.5

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    
    n = len(L)
   
    if n == 0:
        ans = float('NaN')
        
    else:
        u = sum([len(i) for i in L]) / float(n)
        val = 0
    
        for i in L:
            val += (len(i) - u) ** 2
        ans = (val / n) ** 0.5
    
    return ans
    

# ex 3
L = ['a', 'z', 'p']
stdL = stdDevOfLengths(L)


# ex 4
'''Compute the coefficient of variation of [10, 4, 12, 15, 20, 5] to 3 decimal places.'''
v = [10, 4, 12, 15, 20, 5] 
cv = round(std(v) / mean(v), 3)