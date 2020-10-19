# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 16:10:14 2020

@author: natalirs
"""



def powerSet(items):
    
    '''determine possible combinations of items'''
    
    N = len(items)
    
    for i in range(2 ** N):
        taken = []
        notTaken = []
        for j in range(N):
            if (i >> j) % 2 == 1:
                taken.append(items[j])
            else:
                notTaken.append(items[j])
                
        yield [taken, notTaken]
        
        
        
def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    for combo in powerSet(items):
        bag1 = combo[0]
        toTake = combo[1]
        
        for combo2 in powerSet(toTake):
            bag2 = combo2[0]
            
            yield (bag1, bag2)



# test function
lis = []
items = range(3)
for each in yieldAllCombos(items):
    lis.append(each)