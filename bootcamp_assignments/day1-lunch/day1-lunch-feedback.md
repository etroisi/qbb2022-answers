This is really great work! Most of your work is correct, and your comments throughout the code are a great strategy for organizing your thoughts. A few small comments on specific parts: 

3b. Good job on sorting the classifications numerically – this makes things a lot easier to read imo. 

3c. This is a good idea. Your code will sort the list and will figure out which of the classifications has the most occurrences in the bed file. This will show that group 7 is the most common. That said, this doesn't necessarily mean that classification 7 takes up most of the chromosome - it's possible that many of the regions annotated as classification 7 are small. In that case, there could be another classification taking up more of the chromosome. How would you find the classification that takes up the most nucleotides? It's not something that can just be done with the output of `cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | sort -n | uniq -c`, so I would look at the other fields of the bed file for ideas. Also remember that you don't need actual code for the answer here - just the general idea of how it could be done! 

4. It is indeed possible to get out two columns and sort and unique from there! That's a solid idea. Maybe grep could be used here as you suggested, but an easier way would be `cut -f 2,3` which you can then sort and uniq -c. 

5c. Good work on this one! 

In response to this note: #note this prints the header lines too...not sure how to get rid of that

If you know how many lines you want to skip, you can use the `tail` command with the flag `-n+2`. So this says, start showing me the file from the second line. 

This should get you the same result, without the header line: `cut -f 10 HG00100.vcf | tail -n+2 sort | uniq -c`

5d-f. So AF is the allele frequency, and then we have superpopulation-specfic allele frequencies, which are AFR_AF, EUR_AF, etc. 

In 5d. you use grep to find all lines with the text "AF=1", whether that text is written as AF=1, or if it is written as AFR_AF=1. That works perfectly well!

For 5e you are completely correct! There are multiple possibilities for AF=1 to appear in the row, such as when it is a part of EAS_AF=1. 

For 5f, we just want to isolate the AFR_AF values. So essentially printing out AFR_AF=n for each row. It's not something you have to actually implement, the question is mostly designed to get you thinking about how to extract data from the complex info string. 

- Andrew
