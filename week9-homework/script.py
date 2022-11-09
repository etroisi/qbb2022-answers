#!/usr/bin/env python3

import numpy as np
import sys
import scipy
import seaborn as sns
import matplotlib.pyplot as plt

input_arr = np.genfromtxt("dros_gene_expression.csv", delimiter=',', names=True, dtype=None, encoding='utf-8')

col_names = list(input_arr.dtype.names)

t_name=input_arr["t_name"]

fpkm_values=input_arr[["male_10","male_11","male_12","male_13","male_14","female_10","female_11","female_12","female_13","female_14"]]

import numpy.lib.recfunctions as rfn
fpkm_values_2d = rfn.structured_to_unstructured(fpkm_values, dtype=np.float)

stuffthatsgreaterthan0=fpkm_values_2d[np.median(fpkm_values_2d,axis=1) > 0]

logstuffthatsgreaterthan0=np.log2(stuffthatsgreaterthan0 + 0.1)

LSTGT0cluster=scipy.cluster.hierarchy.linkage(logstuffthatsgreaterthan0)
LSTGT0cluster_T=scipy.cluster.hierarchy.linkage(logstuffthatsgreaterthan0.T)

LSTGT0c_leaves=scipy.cluster.hierarchy.leaves_list(LSTGT0cluster)

LSTGT0c_T_leaves=scipy.cluster.hierarchy.leaves_list(LSTGT0cluster_T)

rows=logstuffthatsgreaterthan0[LSTGT0c_leaves, :]
columns=rows[: , LSTGT0c_T_leaves]

fig, ax = plt.subplots()
sns.color_palette("husl", as_cmap=True)
sns.heatmap(columns, xticklabels='auto', yticklabels='auto', ax=None)

fig, ax = plt.subplots()
scipy.cluster.hierarchy.dendrogram(LSTGT0cluster_T, labels=col_names[1:])

plt.show()