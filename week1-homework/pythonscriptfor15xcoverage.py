#!/usr/bin/env python3
#genome will be a list with the length of 1 million
#every element of the list will be a counter for how many times that nucleotide was seen (counted)

#Find start of the read
	#find start of read, and for the next 100 do the same thing
#numpy.zeros
#all the counts will be zero to start with
import numpy
import matplotlib.pyplot as plt
import scipy

#this is the thing for coverage 5

genome = numpy.zeros(1000000)#made an array with one row of 1M zeros, which is a simulation 
#print(genome)

#genome[1] += 1 #increment it by one

#genome[1:3] += 1 #first number is inclusive, second number is exclusive, so this is actually 0,1, testing


#startsite = numpy.random.randint(0,990000)
#genome[startsite:startsite + 100] += 1

for i in range(150000):
  startsite = numpy.random.randint(0,1000000 - 100)
  genome[startsite:startsite + 100] += 1
  
  
# coverage={} #make dictionary
# for i in genome:
#     if i in coverage.keys(): #for each position in genome
#         coverage[i] +=1 #count if that value is unique to the key
#     else:
#         coverage[i] = 1

x = numpy.arange(0,max(genome))
y = scipy.stats.poisson.pmf(x, 15)*len(genome)

fig, ax = plt.subplots()
ax.hist(genome, label = "coverage", bins=len(set(genome)))
ax.scatter(x,y, c ="#2ca02c")
ax.set_ylabel("distribution")
ax.set_xlabel("number of reads")
ax.legend()
#plt.show()

count=0
for i in genome:
    if i == 0:
        count +=1
print(count)
print(y[0])
    
# for i in range(15000):
#   startsite = numpy.random.randint(0,990000)
#   genome[startsite:startsite + 100] += 1

#for i in genome:
 #   print(i) <-- you can see it missed a lot
 