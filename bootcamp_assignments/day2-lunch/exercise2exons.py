#!/usr/bin/env python
from bed_parser_extended import parse_bed

import statistics
#read in random snippet vcf

bed = parse_bed("hg38_gencodev41_chr21.bed")
#the output of the bed parser extended is a list of lists
#need to get blockcount (# of exons)
#need to go through the list of lists and take from every nested list, take the 10th item, and store it in a new list
#then you need to get the median of the list, you need to sort the list numerically, then index list by length/2, then just in case it's odd do a double divison sign so python doesn't get confused when the number is a decimal 
number_of_exons = []
##making the list
for i in range(len(bed)) :
    number_of_exons.append(bed[i][9])
##putting the exon numbers into the list that we made
##specified it by saying hey its a number
number_of_exons.sort()
##sorted it
#print(number_of_exons)
print(statistics.median(number_of_exons))
##printing the median
##used statistics import to do median