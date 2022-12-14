#!/usr/bin/env python3
import numpy
import matplotlib.pyplot as plt

def wrongfisher(allelefreq, popsize):
    listofallelefreq = [allelefreq]
    while allelefreq < 1 and allelefreq > 0:
        gameteswiththatallele=numpy.random.binomial(popsize*2, allelefreq)
        allelefreq=gameteswiththatallele/(popsize*2)
        listofallelefreq.append(allelefreq)
    return listofallelefreq

AFs = wrongfisher(0.5, 100)

listoftimestofixation=[]
for i in range(1000):
    listoftimestofixation.append(len(wrongfisher(0.5, 100)))
    
popsizes = [100, 51402, 5882739, 289143, 9223, 10000000]
listoftimestofixation2=[]
for i in popsizes:
    listoftimestofixation2.append(len(wrongfisher(0.5, i)))
    

fig, ax=plt.subplots()
ax.hist(listoftimestofixation)
ax.set_ylabel("frequency")#how often fixation occurs at x number of generations
ax.set_xlabel("generations")
#plt.show()


fig, ax=plt.subplots()
ax.scatter(popsizes,listoftimestofixation2)
ax.set_ylabel("time to fixation")
ax.set_xlabel("popsize")
ax.set_xticks(popsizes)
plt.show()

def plotsssss(listofallelefreq):
    fig, ax=plt.subplots()
    ax.plot(range(len(listofallelefreq)),listofallelefreq)
    ax.set_xlabel("generations")
    ax.set_ylabel("allele frequency")
    #plt.show()
    
#plotsssss(AFs)

partaf5=[0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
listpart5=[]
for i in partaf5:
    individuallist=[]
    for j in range(100):
        individuallist.append(len(wrongfisher(i, 101)))
    listpart5.append(individuallist)
    
#part 5 violin plots
fig, ax=plt.subplots()
plt.violinplot(listpart5, positions=partaf5, widths=0.05)
ax.set_xlabel("allele frequency")
ax.set_ylabel("time to fixation")
ax.set_xticks(partaf5)

plt.show()
