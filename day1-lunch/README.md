# QBB2022 - Day 1 - Lunch Exercise Submission
1. I'm excited to learn how to code.

2. [/ $]cd Users/cmdb/qbb2022-answers/day1-lunch
[~/qbb2022-answers/day1-lunch $]cp ~/data/bed_files/genes.chr21.bed .
[~/qbb2022-answers/day1-lunch $]cp ~/data/bed_files/exons.chr21.bed .
[~/qbb2022-answers/day1-lunch $]ls
README.md	exons.chr21.bed	genes.chr21.bed
[~/qbb2022-answers/day1-lunch $]less genes.chr21.bed | wc
     219     657    5256
(base) [~/qbb2022-answers/day1-lunch $]less exons.chr21.bed | wc
   13653   40959  327672
   
 print the "word count" for the lines in 

2d. exons/genes = exons per gene
13653/219 = 62.34 exons per gene

2c. Sort by the average number of exons, numerically, then ask to read the line that is in the middle

3. cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | sort -n | uniq -c

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
cut -f 2,3 integrated_call_samples.panel | grep AFR | cut -f 1 | sort | uniq -c

grab columns 2,3, search for AFR, grab only the first column, sort it, then collapse to see how many lines for each pop

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
grab the first 9 columns, which has info for HG00100, and HG00100 column






