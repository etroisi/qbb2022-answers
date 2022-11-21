#!/usr/bin/env python
import sys
import numpy as np
import matplotlib.pyplot as plt

maf=np.genfromtxt("plink.frq", skip_header=1)
#print(maf)

maflist=[]
for a in maf:
    maflist.append(a[4])
    

fig, ax = plt.subplots()
ax.hist(maflist, bins=100)
ax.set_xlabel("frequency")
ax.set_ylabel("distribution")
ax.set_title("minor allele frequency")
plt.show()