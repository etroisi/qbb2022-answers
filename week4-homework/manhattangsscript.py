#!/usr/bin/env python
import sys
import numpy as np
import matplotlib.pyplot as plt

f=open("gs451.assoc.linear")

chromlist=[]
pvaluelist=[]
sigpvalues=[]
pvalxcoord=[]
pvalsigxcoord=[]
ADDrowCount = 0
for index, line in enumerate(f):
    if index == 0:#skip the header
        continue
    fields = line.rstrip().split()#make into a list you can grab info from
    fields[8]=float(fields[8])#make the p values into floats
    if fields[4] ==  "ADD": #want only the test = ADD lines
        chromlist.append(fields[0])#add items from first field into this list
        pvaluelist.append(fields[8])#add items from 8th field into this list, so you have chromosome number and the pvalue of the snp that's found there
        if fields[8] <= 10e-5:
            sigpvalues.append(fields[8])#grab the p values that are significant and put them in a separate list
            pvalsigxcoord.append(ADDrowCount)
        ADDrowCount += 1
    

neglogpval=np.array(pvaluelist)#do log of the p values by making an array of the p values
neglogpval= np.log10(neglogpval)#do log 10
neglogpval = -1 * neglogpval#make it negative log 10
#print(neglogpval)
#for x use length of pvalues
neglogsigpval=np.array(sigpvalues)
neglogsigpval=np.log10(neglogsigpval)
neglogsigpval= -1*neglogsigpval
#print(neglogsigpval)


fig, ax = plt.subplots()
ax.scatter(range(len(neglogpval)), neglogpval, c="royalblue")
ax.scatter(pvalsigxcoord, neglogsigpval, c="lightcoral")
ax.set_xlabel("SNP")
ax.set_ylabel("-log(pvalue)")
#plt.show()

f=open("gs451.assoc.linear")

for index, line in enumerate(f):
    if index == 0:#skip the header
        continue
    fields = line.rstrip().split()#make into a list you can grab info from
    fields[8]=float(fields[8])#make the p values into floats
    if index == 1:
        lowestpvalue = fields[8]
    if fields[8] < lowestpvalue:
        lowestpvalue = fields[8]
        snpid = fields[1]
        
f=open("/Users/cmdb/qbb2022-answers/week4-homework/gwas_data/genotypes.vcf")
for index, line in enumerate(f):
    if line.strip('"').startswith("##"):
        continue
    fields = line.strip('"\r\n').split('\t')
    snp = fields[2]
    if snp==snpid:
        importantsnp=fields

print(len(importantsnp))
f=open("/Users/cmdb/qbb2022-answers/week4-homework/gwas_data/GS451_IC50.txt")
pheno00=[]
pheno01=[]
pheno11=[]
for index, line in enumerate(f):
    if index == 0:
        continue
    fields = line.strip('"\r\n').split('\t')
    if fields[2] == "NA":
        continue
    ic50=float(fields[2])
    if importantsnp[index+8]=="0/0":
        pheno00.append(ic50)
    if importantsnp[index+8]=="0/1":
        pheno01.append(ic50)
    if importantsnp[index+8]=="1/0":
        pheno01.append(ic50)
    if importantsnp[index+8]=="1/1":
        pheno11.append(ic50)

print(pheno00)
print(pheno01)
print(pheno11)

fig, ax = plt.subplots()
plt.boxplot([pheno00, pheno01, pheno11])
ax.set_xlabel("genotype")
ax.set_ylabel("effect")
ax.set_title("GS IC50")
plt.show()
#print(pvalsigxcoord)