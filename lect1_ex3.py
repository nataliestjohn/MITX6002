# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 14:44:47 2020

@author: natalirs
"""

def get_all_subsets(some_list):
    """Returns all subsets of size 0 - len(some_list) for some_list"""
    if len(some_list) == 0:
        # If the list is empty, return the empty list
        return [[]]
    subsets = []
    first_elt = some_list[0]
    rest_list = some_list[1:]
    # Strategy: Get all the subsets of rest_list; for each
    # of those subsets, a full subset list will contain both
    # the original subset as well as a version of the subset
    # that contains first_elt
    for partial_subset in get_all_subsets(rest_list):
        print(get_all_subsets(rest_list))
        print(partial_subset)
        subsets.append(partial_subset)
        next_subset = partial_subset[:] + [first_elt]
        subsets.append(next_subset)
        
    return subsets

lis  = [1,2,3,4,5]

subsets = get_all_subsets(lis)