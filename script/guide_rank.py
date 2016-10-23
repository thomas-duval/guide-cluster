# -*- coding: utf-8 -*-
"""Compute percent-rank activity distribution for each cluster

- Load percent-rank activity and cluster for each guide.
- Divide guide into quartile based on their percent-rank activity and cluster.
- Export the resulting table into a text file.

"""
import numpy as np

# Import activity and cluster assignement for each guide
rank = np.loadtxt('../data/rank.txt', delimiter="\t")

# Divide guides based on their activity and cluster
quartile = np.zeros(shape=(4, 4))
for q in range(4):
    for c in range(4):
        count = 0
        for g in range(len(rank)):
            cluster = rank[g][1]
            activity = rank[g][0]
            if cluster == c and activity < (25.0 + q * 25.0) and activity >= (q * 25.0):
                count = count + 1
            if q == 4 and cluster == c and activity == 100:
                count = count + 1
            if q == 0 and cluster == c and activity == 0:
                count = count + 1
        quartile[c][q] = count

# Export results as a text file
np.savetxt('../data/prediction.txt', quartile)