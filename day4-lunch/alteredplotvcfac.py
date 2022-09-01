#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt

vcf = sys.argv[1]
fs = open( vcf )

ac = []
for i, line in enumerate( fs ):
    if "#" in line:
        continue
    fields = line.split()
    info = fields[7].split(";")
    ac.append( int(info[0].replace("AC=","")) )

fig, ax = plt.subplots()
ax.hist( ac, density=True )

ax.set_yscale('log')
ax.set_title('histogram of allele frequency')
ax.set_xlabel('allele count')
ax.set_ylabel('frequency of allele')
#ax.set_ylim([0, 0.02])
ax.set_ylim([10e-6, 0.02]) #if using log, can't do log of 0. so need to change the y min to something that can be log'ed and be essentially 0, like 10e-6
fig.savefig( vcf + ".png" )

fs.close()
