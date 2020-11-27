# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 17:53:35 2020

@author: natalirs
"""

# ex 4
'''You have a bucket with 3 red balls and 3 green balls. Assume that once you draw a ball out of the bucket, 

you don't replace it. What is the probability of drawing 3 balls of the same color?

Write a Monte Carlo simulation to solve the above problem. '''

import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    
    trial = 0
    ct = 0
    
    while trial <= numTrials:
        
        reds = ['r' for i in range(3)]
        greens = ['g' for i in range(3)]
        balls = reds + greens
        random.shuffle(balls)
        chosen = []
        
        for j in range(3):
            choice = balls.pop()
            chosen.append(choice)
            
        if len(set(chosen)) == 1:
            ct += 1
        
        trial += 1
        
    return ct * 1.0 / numTrials
