# QBB2022 - Day 1 - Homework Exercises Submission

#Exercise 1: 
#Error message: awk: illegal field $(), name "nuc" 
#Error message means that awk does not accept nuc, because nuc is a bash command. so you have to basically make nuc into something awk can understand. you do this by adding -v to then make nuc a variable, that awk can then consider in the rest of the awk statement

for nuc in A C G T
do
  echo "Considering " $nuc
  awk -v var=$nuc '/^#/{next} {if ($4 == var) {print $5}}' $1 | sort | uniq -c
done

(base) [~/qbb2022-answers/day1-homework $]bash exercise1.sh /Users/cmdb/data/vcf_files/random_snippet.vcf 
Considering  A
 354 C
1315 G
 358 T
Considering  C
 484 A
 384 G
2113 T
Considering  G
2041 A
 405 C
 485 T
Considering  T
 358 A
1317 C
 386 G
 
#yes, A is replaced with G. This makes sense because they are both purines--easier to miss this mistake because they are more similarly shaped than a purine vs a pyrimidine.  


#Exercise 2:
#No, it is not clearly defined.

#We use state 1 as promoter region.

genefile=~/data/vcf_files/random_snippet.vcf
 
bedfile=~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed

awk '{if ($4 == "1") {print}}' ~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed > state1
bedtools intersect -a $genefile -b state1 > intersect
awk '{if ($4 == "C") {print $5}}' intersect | sort | uniq -c
#87 intersections (87 locations on chromosome 21 that are promoters), sort by reference allele C and print what alternates there are; sort these (alphabetically) so they can be collapsed and counted-- shows that T is the most common alternate allele, which makes sense because they are both pyrimidines.

#Exercise 3:
#!/bin/bash

#USAGE: bash exercise3.sh input_VCF

awk '/^#/{next} {print $1,$2-1, $2}' $1 > variants.bed
sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed
bedtools closest -a variants.bed -b genes.sorted.bed
[~/qbb2022-answers/day1-homework $]bash exercise3.sh ~/data/vcf_files/random_snippet.vcf 
Error: unable to open file or unable to determine types for file variants.bed

- Please ensure that your file is TAB delimited (e.g., cat -t FILE).
- Also ensure that your file has integer chromosome coordinates in the expected columns (e.g., cols 2 and 3 for BED).
#Bedtools closest wants the file to be tabulated. bedtools closest wants input files to be sorted by chromosome and then start position. need to sort the bed file by chromosome and start first. need to make the bed file tab delimited
#add "/t" to the awk script when specifying 

#after doing that, error reads: Error: Sorted input specified, but the file variants.bed has the following out of order record


 