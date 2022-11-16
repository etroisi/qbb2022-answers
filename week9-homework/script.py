#!/usr/bin/env python3

import numpy as np
import sys
import scipy
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
import statsmodels.stats


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

#plt.show()

#part 2: differential gene expression
sexes=[]
stages=[]
for i in range(1, len(col_names)):
    sexandstage=col_names[i].split('_')#grab the first row and split on the underscore to get sex, stage in a list
    sexes.append(sexandstage[0])#the first thing in the list of stuff for each row is sex
    stages.append(sexandstage[1])#the second thing is stage
pvalues=[]
betavalues=[]
    
#print(stages)
    
for i in range(logstuffthatsgreaterthan0.shape[0]): 
    list_of_tuples = []
    for j in range(len(col_names)-1): #have to do - 1 because col_names for me was defined before removal of the first column so the length does not match what is expected by the pre-written code
        list_of_tuples.append((t_name[i],logstuffthatsgreaterthan0[i,j], sexes[j], stages[j]))
    longdf = np.array(list_of_tuples, dtype=[('transcript', 'S11'), ('fpkm', float), ('sex', 'S6'), ('stage', int)])
    full_model=smf.ols(formula = "fpkm ~ stage", data = longdf).fit()
    pvalues.append(full_model.pvalues["stage"])
    betavalues.append(full_model.params["stage"])

sm.qqplot(np.array(pvalues), dist = scipy.stats.uniform)
#plt.show()

tnamesfiltered=t_name[np.median(fpkm_values_2d,axis=1) > 0]


#false discovery rate part
multipletestresults=statsmodels.stats.multitest.multipletests(pvalues, alpha=0.1)

print(tnamesfiltered[multipletestresults[0]])
#alpha is 0.1 so FDR is 10% #this gives you a list of false and true, which means either not significant p value or significant p value, respectively

pvalues2=[]
betavalues2=[]
    
#print(stages)
    
for i in range(logstuffthatsgreaterthan0.shape[0]): 
    list_of_tuples = []
    for j in range(len(col_names)-1): #have to do - 1 because col_names for me was defined before removal of the first column so the length does not match what is expected by the pre-written code
        list_of_tuples.append((t_name[i],logstuffthatsgreaterthan0[i,j], sexes[j], stages[j]))
    longdf = np.array(list_of_tuples, dtype=[('transcript', 'S11'), ('fpkm', float), ('sex', 'S6'), ('stage', int)])
    full_model=smf.ols(formula = "fpkm ~ stage + sex", data = longdf).fit()
    pvalues2.append(full_model.pvalues["stage"])
    betavalues2.append(full_model.params["stage"])

sm.qqplot(np.array(pvalues2), dist = scipy.stats.uniform)
#plt.show()



#false discovery rate part
multipletestresults2=statsmodels.stats.multitest.multipletests(pvalues2, alpha=0.1)

#print(tnamesfiltered[multipletestresults2[0]])
print(sum(multipletestresults2[0])/sum(multipletestresults[0])*100) #because they are booleans, true is 1 and false is 0, so instead of putting the "true" items into its own variable and comparing, just sum because the trues will be 1 and the falses will not add to the sum

#volcano plot
colors=[]
for i in multipletestresults2[0]:
    if i == True:
        colors.append('m')
    else:
        colors.append('c')
fig, ax = plt.subplots()
ax.scatter(betavalues2, -np.log10(pvalues2), color=colors)#a volcano plot is just a scatter plot

plt.show()

