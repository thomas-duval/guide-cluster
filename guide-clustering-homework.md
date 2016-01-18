# Guide RNA Clustering Homework
## Objectives

Cluster the CRISPR guide RNAs in the included TSV file, determine predictors of guide RNA activity, and generally comment on the “shape” of the data and any interesting trends or patterns you find.

## Rules
This task is untimed. You may use any programming language, libraries, or frameworks available to you provided they are available to others to reproduce your analysis. You should clearly distinguish your original code from 3rd party code. Clearly demonstrating your process and laying out your “thoughts in code” is more important than runtime performance. We must be able to re-create your analysis.

## Instructions
Fork this repository, write one or more scripts to analyze the included guide_data.tsv file, then make a pull request back with your code and email getin@desktopgenetics.com with the subject “Homework Complete” including a summary of your results. You may also want to generate documents, makefiles, plots, figures, or other pieces of code to support your analysis or allow it to be reproduced by us.

If you are selected for the third and final round, you should then prepare a 30 minute presentation on your approach and findings for the Desktop Genetics team.

In your analysis, consider the following topics:

1. Are there any interesting clusters of guides based on their sequence or other properties. You may compute further properties such as location in the human reference genome, one or more measures of energy or entropy, melting temperature, mass, or presence of hairpins. The activity of a guide is defined as: -log2(count_t2/count_t1). Relative activity can also be computed.

2. Discuss the distribution of guide activities or other properties with respect to any clusters found above. Are you able to find any positive or negative predictors of guide activity? 

3. What genes appear to be essential (guides in them are most depleted)? Why?


## A very basic CRISPR introduction
In CRISPR/Cas9 genome editing, a DNA cutting enzyme (nuclease) known as Cas9 is targeted toward a specific part(s) of the genome by encoding instructions in a nucleic acid sequence, known as a guide RNA. The nuclease is thought to search the genome by jumping to a random point and then linearly scanning for the pattern NGG before detaching and repeating the cycle at a new location. If the pattern NGG is found, the nuclease then checks the 20 character programmable pattern right to left. If the match is *sufficiently close*, typically fewer than 4 mismatches, then the nuclease will cut the genome at this location. Otherwise it will detach and try another location.

The host cell will then attempt to repair this cut with one of several different repair pathways each with a characteristic, at times imperfect, outcome. If the genome is cut inside of functional region, a gene, this gene may be disabled if the repair is imperfect. If this gene is essential and imperfectly repaired, then the cell can die. By repeating this process in parallel millions of times with different guide sequences, we can use CRISPR to determine the genes a cell needs to survive. These genes are often good drug targets when the cell is a cancer cell.

## Sample CRISPR Library Functional Screening Data
CRISPR can be performed in a massively parallel manner to determine the function of many genes simultaneously in an experiment called a functional screen. In a screen, a set of several thousand guide RNAs targeting thousands of genes are synthesized together in a pool and then introduced to a population of cells such that each cell gets (ideally) one and only one member of the guide set. The distribution (mass function) of this guide RNA set can be measured by DNA sequencing, which maps each guide sequence to a “normalized read count” in a given sample. When a particular member sequence of the population decreases in abundance, this may be because it targets an essential gene and the host cell for the guide was killed. It is thought that greater depletion is correlated with greater guide *activity* (potency). In practice, not all guides perform equally for reasons that are still unknown.

The data provided here comes from a recent real-world experiment. Several hundred genes (col 1) in a cancer cell line where targeted. Several guides (formally spacer sequences, col 2/3) where selected at different locations within each of several hundred genes. Using massively parallel sequencing and some minor data processing the normalized counts of each guide where computed under the following circumstances:

- Immediately upon construction of the delivery plasmid before introduction to cells. Column 4
- 7 days after introduction to cells  without drugs (2 replicates).  Columns 5 and 6.
- 14 days after introduction to cells (2 replicates) without drugs (2 replicates). Columns 7 and 8
- 7 days after introduction to cells along with the drug PLX (2 replicates). Columns 9 and 10.
- 14 days after introduction to cells along with the drug PLX (2 replicates). Columns 11 and 12.

All other factors, such as the number of cells and the nuclease, where held constant.

## Prior Art 
Scientists are currently trying to figure out what features of a guide and the location it targets influence its behavior. Information is present in nucleic acids in mechanical (ie. curvature), chemical (ie. binding thermodynamics), and symbolic (ie. ATG is a start codon) forms. Some scientists have used Support Vector Machines and Logistic Regression to try and determine if particular bases or pairs of bases at particular positions in the guide make it more active. For example, a “G” in the right-most position may be beneficial. The results have been mixed and possibly suffer from over-fitting. A few key points are known:
- Cut sites with the same sequence but in different locations and contexts occur with different frequencies.
- Guides with different sequences but cutting right next to each other have different activities.






 


