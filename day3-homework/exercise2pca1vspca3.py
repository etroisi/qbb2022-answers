#!/usr/bin/env python
import sys
import numpy as np
import matplotlib.pyplot as plt

pca_list=np.genfromtxt("plink.eigenvec",
                    dtype = None,
                    encoding = None,
                    usecols = (2,3,4),
                    names = ["pca1", "pca2", "pca3"])

fig, ax = plt.subplots()
ax.scatter(pca_list['pca1'], pca_list['pca3'])
plt.show()