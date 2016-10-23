# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 17:20:03 2016

@author: Thomas
"""
import numpy as np

rank = np.loadtxt('rank.txt', delimiter="\t")

print(rank[0])
print(len(rank))

quartile = np.zeros(shape=(4,4))
for q in range(4):
    for c in range(4):
        count = 0
        for g in range(len(rank)):
            if rank[g][1] == c and rank[g][0] < (25.0 + q * 25.0) and rank[g][0] >= (q * 25.0):
                count = count + 1
            if q == 4 and rank[g][1] == c and rank[g][0] == 100:
                count = count + 1
            if q == 0 and rank[g][1] == c and rank[g][0] == 0:
                count = count + 1
        quartile[c][q] = count                 
        
np.savetxt('prediction.txt', quartile)        
        
print(quartile)
c1 = sum(quartile[0])
c2 = sum(quartile[1])
c3 = sum(quartile[2])
c4 = sum(quartile[3])
print(c1, c2, c3, c4, c1+c2+c3+c4)
