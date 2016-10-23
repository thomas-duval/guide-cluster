# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 21:04:24 2016

@author: Thomas
"""
import numpy as np
import collections 

average = []
genes = np.asarray(open("genes.txt").readlines())
activity = np.loadtxt('activity.txt', delimiter="\t")
count = collections.Counter(genes)
print(genes[0:10])

genes_short = []
print(genes[0] not in genes_short)
genes_short = ['A1BG\n']
print(genes[0] not in genes_short)

for g in range(10):
    if genes[g] not in genes_short:
        genes_short = np.append(genes_short, genes[g], axis=0)

print(genes_short)   
np.savetxt('genes_short.txt', genes_short, delimiter='\s', fmt="%s")

"""
print(len(count))

for g in range(len(count)):
    n_gene = count[genes[0]]
    average = np.append(average, sum(activity[0:n_gene])/n_gene)  
    for i in range(n_gene):
        genes = np.delete(genes, 0)
        activity = np.delete(activity, 0)
    #print(len(average), len(genes), len(activity))
    if len(genes) == 0:
        break
    
print(average[0:10]) 
np.savetxt('average_activity.txt', average)



"""

