#!/usr/bin/env python
import sys
import numpy as np
import matplotlib.pyplot as plt

pca_list=np.genfromtxt("plink.eigenvec",
                    dtype = None,
                    encoding = None,
                    names = ["placeholder1", "placeholder2", "pca1", "pca2", "pca3", "pca4", "pca5", "pca6", "pca7", "pca8", "pca9", "pca10"])

fig, ax = plt.subplots()
ax.scatter(pca_list['pca1'], pca_list['pca2'])
ax.set_xlabel("pca1")
ax.set_ylabel("pca2")
ax.set_title("PCA")
plt.show()