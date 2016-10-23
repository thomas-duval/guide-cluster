# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 11:10:00 2016

@author: Thomas
"""

from sklearn.cluster import KMeans

import collections
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

X = np.loadtxt(open("feature.txt"))
y = np.asarray(open("feature_list.txt").readlines())

# kmeans algorithm
n_clusters = 4
clusterer = KMeans(init='k-means++', n_clusters=n_clusters, n_init=100)
cluster_labels = clusterer.fit_predict(X)
np.savetxt('cluster_labels.txt', cluster_labels)

# Labeling the clusters
centers = clusterer.cluster_centers_
np.savetxt('cluster.txt', centers)

# Number of gene / cluster
counter = collections.Counter(cluster_labels)
distrib = []
for i in range(n_clusters):
    distrib.append(counter[i])
print(distrib)
np.savetxt('distribution.txt', distrib)

# average_X
average_X = []
for i in range(11):
    average_X.append(np.average(X[:, i]))
print(average_X)
np.savetxt('average_X.txt', average_X)

# Draw plot
colors = cm.Paired(cluster_labels / n_clusters)

# Plot 0-2
plt.scatter(X[:, 0], X[:, 2], marker='.', s=500, lw=0, alpha=0.7, c=colors)
plt.xlabel(y[0])
plt.ylabel(y[2])
plt.scatter(centers[:, 0], centers[:, 2],
            marker='o', c='white', alpha=1, s=500)
for i, c in enumerate(centers):
    plt.scatter(c[0], c[2], marker='$%d$' % i, alpha=1, s=50)
plt.scatter(average_X[0], average_X[2], marker='x', c='black', alpha=1, s=300)
plt.savefig('0-2.png')
plt.clf()

# Plot 1-3
plt.scatter(X[:, 1], X[:, 3], marker='.', s=500, lw=0, alpha=0.7, c=colors)
plt.xlabel(y[1])
plt.ylabel(y[3])
plt.scatter(centers[:, 1], centers[:, 3],
            marker='o', c='white', alpha=1, s=500)
for i, c in enumerate(centers):
    plt.scatter(c[1], c[3], marker='$%d$' % i, alpha=1, s=50)
plt.scatter(average_X[1], average_X[3], marker='x', c='black', alpha=1, s=300)
plt.savefig('1-3.png')
plt.clf()

# Plot 4-9
plt.scatter(X[:, 4], X[:, 9], marker='.', s=500, lw=0, alpha=0.7, c=colors)
plt.xlabel(y[4])
plt.ylabel(y[9])
plt.scatter(centers[:, 4], centers[:, 9],
            marker='o', c='white', alpha=1, s=500)
for i, c in enumerate(centers):
    plt.scatter(c[4], c[9], marker='$%d$' % i, alpha=1, s=50)
plt.scatter(average_X[4], average_X[9], marker='x', c='black', alpha=1, s=300)
plt.savefig('4-9.png')
plt.clf()

# Plot 5-10
plt.scatter(X[:, 5], X[:, 10], marker='.', s=500, lw=0, alpha=0.7, c=colors)
plt.xlabel(y[5])
plt.ylabel(y[10])
plt.scatter(centers[:, 5], centers[:, 10],
            marker='o', c='white', alpha=1, s=500)
for i, c in enumerate(centers):
    plt.scatter(c[5], c[10], marker='$%d$' % i, alpha=1, s=50)
plt.scatter(average_X[5], average_X[10], marker='x', c='black', alpha=1, s=300)
plt.savefig('5-10.png')
plt.show()
