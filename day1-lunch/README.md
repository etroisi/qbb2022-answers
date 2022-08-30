# QBB2022 - Day 1 - Lunch Exercise Submission
1. I'm excited to learn how to code.

2. [/ $]cd Users/cmdb/qbb2022-answers/day1-lunch
#moving to day1-lunch
[~/qbb2022-answers/day1-lunch $]cp ~/data/bed_files/genes.chr21.bed .
#copy genes.chr21.bed to current directory, which is qbb2022-answers/day1-lunch
[~/qbb2022-answers/day1-lunch $]cp ~/data/bed_files/exons.chr21.bed .
#copy exons.chr21.bed to current directory, which is qbb2022-answers/day1-lunch

[~/qbb2022-answers/day1-lunch $]ls
README.md	exons.chr21.bed	genes.chr21.bed
#check that those files got there, they did
[~/qbb2022-answers/day1-lunch $]less genes.chr21.bed | wc
     219     657    5256
#wc: gives a count of line, character, byte count. we care about line count because it corresponds to number of genes
(base) [~/qbb2022-answers/day1-lunch $]less exons.chr21.bed | wc
   13653   40959  327672
#do wc for exons, which will tell us (don't need the less and the pipe, this was me not realizing i could just do wc filename; wc filename prints the values and the file name, see next line)
[~/qbb2022-answers/day1-lunch $]wc exons.chr21.bed
   13653   40959  327672 exons.chr21.bed
 

2d. exons/genes = exons per gene
13653/219 = 62.34 exons per gene

2c. Sort by the average number of exons, numerically, then ask to read the line that is in the middle

3. cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | sort -n | uniq -c
#grab the 4th column of chromHMM, sort it numerically, collapse and count unique numbers

3b. 15 classifications;
 305 1
 678 2
  79 3
 377 4
 808 5
 148 6
1050 7
 156 8
 654 9
  17 10
  17 11
  30 12
  62 13
 228 14
 992 15
 
3c. | sort -k 1 -r (sort the first column and reverse), then ask for the first line

4. cp ~/data/metadata_and_txt_files/integrated_call_samples.panel .
#copy integrated_call_samples.panel into working directory, which is qbb2022-answers/day1-lunch

cut -f 2,3 integrated_call_samples.panel | grep AFR | cut -f 1 | sort | uniq -c
#grab columns 2 (pop), 3 (superpop), pick out for AFR in those columns (because we're interested in the AFR superpop), grab only the first column (pop, which we're interested in), sort it, then collapse to see how many lines for each pop

4b.  123 ACB
 112 ASW
 173 ESN
 180 GWD
 122 LWK
 128 MSL
 206 YRI
 
4c. Repeat 5 times with the different superpopulations; use a for loop if possible. Would be cool if you could grep --include each superpopulation so it would grab each superpopulation in the 3rd field and its corresponding 2nd field and then sort and uniq from there

5. cp ~/data/vcf_files/random_snippet.vcf .

5b. cut -f 1-9,13 random_snippet.vcf > HG00100.vcf
#this grabs the first 9 columns, which has info for HG00100, and HG00100 column, and makes a new file, which is saved in /day1-lunch
note to self: make sure you are in the right directory to make sure you're saving the file in the right place. furthermore, check GUI if unsure. tried to repeat this code and got error "permission denied", looked at the GUI and noticed it was telling me I already had a file in this folder named "random_snippet.vcf" from when i saved it earlier. "permission denied" was bash's way of telling me i already had a file called that (i think)

5c. need to know what field 0|0 and its variants are in. found out it is field 10. 
cut -f 10 HG00100.vcf
#grabs field 10 with the 0|0 or 1|0 or 0|1 or 1|1 info
need to sort and uniq again?
cut -f 10 HG00100.vcf | sort | uniq -c
all the header lines
9514 0|0
 127 0|1
 178 1|0
 181 1|1
   1 HG00100
#note this prints the header lines too...not sure how to get rid of that

5d. need to find how many rows have AF=1, so search for AF=1
grep AF=1 HG00100.vcf
#this gives all the rows with AF=1, but we want to know a number
grep AF=1 HG00100.vcf | cut -f 1 | uniq -c
	34 chr 21

34 rows contain AF=1

5e. i think this means somehow count how many AF=1 there are in each row, and then pick the max, which would assume that the max is a row that has AF=1 in every place it could? otherwise i can just count the places where AF= is in the row.
5, which are EAS_AF=1, EUR_AF=1, AFR_AF=1, AMR_AF=1, SAS_AF=1

5f. not sure if this means you want the AFR value for each row (ie chr21 at 41814849 is AFR_AF=1), or just want to know all the possible AFR values (ie, AFR_AF=1 or AFR_AF=0.99, etc) contained in this file












