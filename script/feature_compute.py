# -*- coding: utf-8 -*-

"""Compute 11 features from guide RNAs to be used for clustering

- Import guides RNAs as a text file created from the provided tsv file.
- Import Melting point (provided by dnaMATE ) for each guide as a text file.
- Use Tm and nucleotide count to characterize each guide with 11 features.
- Export the resulting array as a text file.

"""

import csv
import numpy as np

sequence_import = []
tm_import = []
sequence = []
tm = []
feature = []


# Open files containing sgRNA and transfer them into an array
with open('../data/RNA.txt', newline='') as inputfile:
    for row in csv.reader(inputfile):
        sequence_import.append(row)
sequence = np.asarray(
    [item for sublist in sequence_import for item in sublist])

# Open files containing melting temperature and transfer them into an array
with open('../data/Tm.txt', newline='') as inputfile:
    for row in csv.reader(inputfile):
        tm_import.append(row)
tm = [item for sublist in tm_import for item in sublist]

# Compute nucleotides feature for each sgRNA
feature = np.zeros((len(sequence), 11))
for idx, guide in enumerate(sequence):
    feature[idx, 0] = guide.count('A')
    feature[idx, 1] = guide.count('T')
    feature[idx, 2] = guide.count('G')
    feature[idx, 3] = guide.count('C')
    feature[idx, 4] = guide.count('GG')
    feature[idx, 5] = guide.count('TA')
    feature[idx, 6] = guide.count('TT')
    feature[idx, 7] = guide.count('AG')
    feature[idx, 8] = guide.count('AC')
    feature[idx, 9] = guide.count('GC')

# Add melting temperature to the feature array
for idx, temp in enumerate(tm):
    feature[idx, 10] = temp

np.savetxt('../data/feature.txt', feature)
