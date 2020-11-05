# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 11:23:26 2020

@author: natalirs
"""

'''In the following examples, assume all graphs are undirected. That is, an edge from A to B is the same as an edge from B to A and counts as exactly one edge.
A clique is an unweighted graph where each node connects to all other nodes. We denote the clique with  n  nodes as KN. Answer the following questions in terms of  n . 
Calculate the number of paths of length  m  from A to B, where  1≤m≤(n−1) , and write this number as a ratio of factorials.'''

nodes = [1]

for i in range(3, 20):
    nextNum = nodes[-1] + sum(nodes)
    nodes.append(nextNum)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def numPaths(n, m):
    return factorial(n - 2) / factorial(n - m - 1)

# test function
    
pathDict = {}    
for n in range(2, 10):
    nSum = 0
    for m in range(1, n):
        paths = numPaths(n,m)
        nSum += paths
        
    pathDict[n] = nSum