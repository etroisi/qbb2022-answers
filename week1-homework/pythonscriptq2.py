#!/usr/bin/env python3
#genome will be a list with the length of 1 million
#every element of the list will be a counter for how many times that nucleotide was seen (counted)

#Find start of the read
	#find start of read, and for the next 100 do the same thing
#numpy.zeros
#all the counts will be zero to start with
import numpy

genome = numpy.zeros(1000000)#made an array with one row of 1M zeros, which is a simulation 
#print(genome)

#genome[1] += 1 #increment it by one

#genome[1:3] += 1 #first number is inclusive, second number is exclusive, so this is actually 0,1, testing


#startsite = numpy.random.randint(0,990000)
#genome[startsite:startsite + 100] += 1

for i in range(50000):
  startsite = numpy.random.randint(0,990000)
  genome[startsite:startsite + 100] += 1
    
for i in range(15000):
  startsite = numpy.random.randint(0,990000)
  genome[startsite:startsite + 100] += 1

#for i in genome:
 #   print(i) <-- you can see it missed a lot
 