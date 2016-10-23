# -*- coding: utf-8 -*-
"""Run a k-means algorithm to divide guides based on the 11 features

- Import features for each guide and features' name from a text file.
- Use scikit-learn to run a k-means algorithm.
- Export clusters coordinates, labels and distributin as text files.
- Draw plots to visualize clusters based on several features.

"""

from sklearn.cluster import KMeans

import collections
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Import features values and names from text files
X = np.loadtxt(open("feature.txt"))
y = np.asarray(open("feature_list.txt").readlines())

# kmeans algorithm using scikit-learn
n_clusters = 4
clusterer = KMeans(init='k-means++', n_clusters=n_clusters, n_init=100)
cluster_labels = clusterer.fit_predict(X)

# Labeling the clusters
centers = clusterer.cluster_centers_

# Number of gene / cluster
counter = collections.Counter(cluster_labels)
distrib = []
for i in range(n_clusters):
    distrib.append(counter[i])

# Export results to text files
np.savetxt('cluster_labels.txt', cluster_labels)  # clusters label for each RNA
np.savetxt('cluster.txt', centers)  # clusters coordinate
np.savetxt('distribution.txt', distrib)  # cluster distribution among guides

# coordinate for average guide
average_X = []
for i in range(11):
    average_X.append(np.average(X[:, i]))

# Set colors for plots
colors = cm.Paired(cluster_labels / n_clusters)

# Plot between feature number 0 (A) and number 2 (G)
plt.scatter(X[:, 0], X[:, 2], marker='.', s=500, lw=0, alpha=0.7, c=colors)  # Plot guides 
plt.xlabel(y[0])
plt.ylabel(y[2])
plt.scatter(centers[:, 0], centers[:, 2],
            marker='o', c='white', alpha=1, s=500)  # Plot clusters
for i, c in enumerate(centers):
    plt.scatter(c[0], c[2], marker='$%d$' % i, alpha=1, s=50)
plt.scatter(average_X[0], average_X[2], marker='x', c='black', alpha=1, s=300)  # Plot average guide
plt.savefig('0-2.png')
plt.clf()

# Plot between feature number 1 (T) and number 3 (C)
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

# Plot between feature number 4 (GG) and number 9 (GC)
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

# Plot between feature number 5 (TA) and number 10 (Tm)
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
