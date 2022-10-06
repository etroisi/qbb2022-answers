#!/usr/bin/env python
import sys
import numpy as np
import matplotlib.pyplot as plt

f=open("cb1908.assoc.linear")

chromlist=[]
pvaluelist=[]
for index, line in enumerate(f):
    if index == 0:#skip the header
        continue
    fields = line.rstrip().split()#make into a list you can grab info from
    fields[8]=float(fields[8])#make the p values into floats
    if fields[4] ==  "ADD": #want only the test = ADD lines
        chromlist.append(fields[0])#add items from first field into this list
        pvaluelist.append(fields[8])#add items from 8th field into this list, so you have chromosome number and the pvalue of the snp that's found there

neglogpval=np.array(pvaluelist)#do log of the p values by making an array of the p values
neglogpval= np.log10(neglogpval)#do log 10
neglogpval = -1 * neglogpval#make it negative log 10
print(neglogpval)
for x use length of pvalues
