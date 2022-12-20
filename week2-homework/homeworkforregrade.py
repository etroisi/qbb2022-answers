#!/usr/bin/env python3

import numpy as np
import sys
from fasta import readFASTA

#========================#
# Set sequences to align #
#========================#

# In the homework assignment, you'll reading sequences from a
# FASTA file. For the live-coding, we'll define them
# explicitly in the script.

#sequence1 = 'TGTTACGG'
#sequence2 = 'GGTTGACTA'

#input_sequences = readFASTA(open(<fasta_file>))

#seq1_id, sequence1 = input_sequences[0]
#seq2_id, sequence2 = input_sequences[1]


#blosum = np.loadtxt('needleman-wunsch/BLOSUM62.txt')

#print(blosum)



scoringmatrix=sys.argv[1]
dnafasta=sys.argv[2]
gap_penalty = int(sys.argv[3])
outputfile=sys.argv[4]

alphabet = {} #make a dictionary
sigma = [] #make a list
for i, line in enumerate(open(scoringmatrix)):#use hoxd for DNA
    #print(i, line)
    fields = line.strip().split()#looks like:['N', '-2', '0', '6', '1', '-3', '0', '0', '0', '1', '-3', '-3', '0', '-2', '-3', '-2', '1', '0', '-4', '-2', '-3', '3', '0', '-1']
    #print(fields)
    if i == 0: #if the line is 0, make it an entry in the dictionary as {A,0} 
        for j, char in enumerate(fields): 
            alphabet[char] = j
        continue
    sigma.append([float(x) for x in fields[1:]])
sigma = np.array(sigma)
      

input_sequences = readFASTA(open(dnafasta))#use dna file

seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]

F_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))

tracebackmatrix = np.empty((len(sequence1)+1, len(sequence2)+1), dtype=str)

for i in range(len(sequence1)+1):
    tracebackmatrix[i,0] = 'v'

for j in range(len(sequence2)+1):
    tracebackmatrix[0,j] = 'h'
    


#print(tracebackmatrix)

for i in range(len(sequence1)+1):
     F_matrix[i,0] = i * gap_penalty
#
# # Now fill in the first row
#
for j in range(len(sequence2)+1):
     F_matrix[0,j] = j * gap_penalty
#
#print(F_matrix)

for i in range(1, len(sequence1)+1):
    for j in range(1, len(sequence2)+1):
       
        d = F_matrix[i-1,j-1] + sigma[alphabet[sequence1[i-1]],alphabet[sequence2[j-1]]]
        h = F_matrix[i,j-1] + gap_penalty
        v = F_matrix[i-1,j] + gap_penalty
        F_matrix[i,j] = max(d, h, v)
        if d > h and d > v:
            tracebackmatrix[i,j] = 'd'
        if h > v and h > d:
            tracebackmatrix[i,j] = 'h'
        if v > h and v > d:
            tracebackmatrix[i,j] = 'v'
        if d == v and d == h:
            tracebackmatrix[i,j] = 'd'
        if v > d and v==h:
            tracebackmatrix[i,j] = 'h'
        if d==v and d > h:
            tracebackmatrix[i,j] = 'd'
        if d==h and d > v:
            tracebackmatrix[i,j] = 'd'
        

#1. start in bottom right corner = (i,j) = lengths of sequence 1 and 2, plus 1 for each perhaps           #2. while loop, as in, while not as (0,0) (i>0, j>0)
#i = len(sequence1)
#j = len(sequence2)
#3. if 'd'
    #to actaully move, change coordinates, so like (i-1) (j-1)
    #while (i>0, j>0)
        #if 'd'
            #move i-1 and j-1
        #if 'v'
            #move whichever it is
        #if 'h'
            #move whichever it is

#make the alignment...


i = len(sequence1)
j = len(sequence2)

seq1=""#put the values you're going to grab into a string
seq2=""
numofgapsinseq1=0
numofgapsinseq2=0
alignmentscore=F_matrix[i,j]
while i > 0 and j >0:
    if tracebackmatrix[i,j] == 'd':#print when no gap, or when penalty for mismatch is lower than gap penalty
        i=i-1
        j=j-1
        seq1=seq1 + sequence1[i]
        seq2=seq2 + sequence2[j]
    if tracebackmatrix[i,j] =='v':
        i=i-1
        seq1=seq1 + sequence1[i]
        seq2=seq2 + '_'
        numofgapsinseq2+=1
    if tracebackmatrix[i,j] == 'h':
        j=j-1  
        seq1=seq1 + '_'
        seq2=seq2+sequence2[j]
        numofgapsinseq1+=1

print('num of gaps in seq 1', 'num of gaps in seq 2', 'alignmentscore')        
print(numofgapsinseq1, numofgapsinseq2, alignmentscore)
seq1=seq1[::-1]
seq2=seq2[::-1]

f = open(outputfile,'w')
f.write(seq1)
f.write(seq2)

#print(tracebackmatrix)


#print(F_matrix)
#===========================================================#
# Read in match, mismatch, and gap scores from command line #
#===========================================================#

# We can use `sys.argv` to read arguments in from the command
# line, stored in a list. The first thing in the list is
# always the name of the script.

#print(sys.argv)
#print(sys.argv[1:])
#want the matched score, unmatched score

# match_score=float(sys.argv[1])
# mismatch_score=float(sys.argv[2]) #want your scores to be floats
# gap_penalty=float(sys.argv[3]) #gap should be negative
#
# #print(gap_penalty) #will be -2
#
# list_of_lists=[[1,2,3],[4,5,6],[7,8,9]]
# my_2D_array=np.array(list_of_lists)
# #print(my_2D_array)
# # The rest of the elements of the list are any arguments
# # passed when we run the script in the command line
#
#
# my_list=[3,1,4,5]
# #print(my_list[0:3])
#
# # Assuming three arguments: match score, mismatch score, and
# # gap penalty, store these arguments as variables we can use
# # in our script.
#
# #print(my_2D_array[1,0:3]) #grab first row, everything from column 1 to column 3
# #print(my_2D_array[:3,1])#grab all the rows from 0-3, but grab only column 1
# my_2D_array[1,1]=314#changes item at 1,1 to 314
#
#
#
# #============================#
# # Playing around with arrays #
# #============================#
#
# # Numpy is a Python package built around matrices (arrays).
# # You can think of an array as a (potentially)
# # multi-dimensional list. In fact, a 2D numpy array is
# # essentially a list of lists. We can create a numpy
# # array using the `np.array()` function.
#
#
#
# # If we want to know what the dimensions of our array
# # are, we can check the `.shape` attribute
#
#
#
# # Just like we can index lists, we can also index numpy
# # arrays. When we index a numpy array, we first index
# # the rows, then the columns.
#
#
#
# # Like with lists, numpy arrays also support item assignment.
#
# #for row in my_2D_array:
#  #   for val in row:
#   #      print(val)
#
#
# # We can also loop through numpy arrays. When we loop through
# # a 2D array, we loop through the rows
#
#
#
# # Because each row is just a 1D numpy array, we can also loop
# # through the row itself
# #for row in my_2D_array
#  #   for val in row:
#   #      print(val)#<--try to make this but use range instead
#
# #for i in range(0,my_2D_array.shape[0]): #array.shape gives a tuple of rows,columns, so if you want to know how rows their are use this
#  #   for j in range(0, my_2D_array.shape[1]):
#   #      print(my_2D_array[i,j])
#
#
#
# # We can also use the range() function to loop through each
# # value in the array
#
#
#
#
# #=====================#
# # Initialize F-matrix #
# #=====================#
#
# # The first thing we need to do is create an empty F-matrix.
# # The number of rows should be equal to the length of
# # sequence1 plus one (to allow for leading gaps). Similarly,
# # the number of columns should be equal to the length of
# # sequence2 plus one.
#
# F_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))
#
# # Now we need to fill in the values in the first row and
# # first column, based on the gap penalty. Let's fill in the
# # first column.
#
# for i in range(len(sequence1)+1):
#     F_matrix[i,0] = i * gap_penalty
#
# # Now fill in the first row
#
# for j in range(len(sequence1)+1):
#     F_matrix[j,0] = j * gap_penalty
#
# #print(F_matrix)
#
#
# #=======================#
# # Populate the F-matrix #
# #=======================#
#
# # Now that we've filled in the first row and column, we need
# # to go row-by-row, and within each row go column-by-column,
# # calculating the scores for the three possible alignments
# # and storing the maximum score
#
# for i in range(1, len(sequence1)+1):
#     for j in range(1, len(sequence2)+1):
#         if sequence1[i-1] == sequence2[j-1]:
#             d = F_matrix[i-1,j-1] + match_score
#         else:
#             d = F_matrix[i-1,j-1] + mismatch_score
#         h = F_matrix[i,j-1] + gap_penalty
#         v = F_matrix[i-1,j] + gap_penalty
#         F_matrix[i,j] = max(d, h, v)
#
# #====================#
# # Print the F-matrix #
# #====================#
#
#
#
# #=========================#
# # A primer on while loops #
# #=========================#
#
# # While loops are a useful tool in Python (and most other languages)
# # that allows you to continue doing a process until some condition
# # stops being met. If we want, we can have them mimic a for loop:
#
# # Let's make a for loop that prints out the integers from 0 to 10
# # (non-inclusive)
# for i in range(0,10):
#     print(i)
#
#
# # We can do the exact same thing with a while loop
# i = 0
# while i < 10:
#     print(i)
#     i+=1
#
# # While loops can also let us easily go backwards
# i = 9
# while i >= 0:
#     print(1)
#     i = i-1
