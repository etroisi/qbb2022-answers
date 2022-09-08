Exercise 1:

inside the numpy.arange, 0.55 is the number you want to start your array to start with, 1.05 is the number you want the array to go up to but not include, and 0.05 is the increment you want the values in your array to increase by.

[::-1] reverses a list (thus the printout is end to start). 

probs = numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)[::-1] vs probs = numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2):

the coordinates of the array are switched (ie reflected on a vertical axis), so when [::-1] is used the top left most value is now the top right value. learned in homework review that this is for aesthetics.

Exercise 1C:
The higher the probability of heads (more biased the coin), the higher the power (to determine that the coin is biased). The higher the number of tosses, the higher the power. Two important things: increase sample size (number of tosses), and you see the signal (ie, high power), or increase the strength of the signal (make the coin very biased), and you'll see the signal, even with fewer tosses.

Exercise 1D:

In this paper, they are testing Mendel's hypothesis that alleles are inherited without favor to one allele, ie, that the alleles from two heterozygous parents 