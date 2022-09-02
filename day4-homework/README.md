Exercise 1A:

inside the numpy.arange, 0.55 is the number you want to start your array to start with, 1.05 is the number you want the array to go up to but not include, and 0.05 is the increment you want the values in your array to increase by.

[::-1] reverses a list (thus the printout is end to start). 

probs = numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)[::-1] vs probs = numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2):

the coordinates of the array are switched (ie reflected on a vertical axis), so when [::-1] is used the top left most value is now the top right value