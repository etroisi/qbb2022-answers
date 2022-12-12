What percentage of reads are valid interactions (duplicates do not count as valid)?
37.8

What constitutes the majority of invalid 3C pairs? What does it actually mean (you may need to dig into the HiC-Pro manual)?
dangling end pairs: means that the fragments were not ligated after the restriction enzyme step. 

Were you able to see the highlighted difference from the original figure?
Yes, it is visible.

What impact did sequencing depth have?
more sequencing leads to more clarity in the results--makes it easier to distinguish signal from noise, because you get more reads per present locus (CTCF binding loci), not more new reads.

What does the highlighted signal indicate?
it shows where the CTCF site is and how it changes the TAD structure when eliminated.

For the heatmap plotting: python 40kbloaddata.py /Users/cmdb/qbb2022-answers/week6-homework/matrix/dCTCF_full.40000.matrix /Users/cmdb/qbb2022-answers/week6-homework/matrix/40000_bins.bed
