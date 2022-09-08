Exercise 1:
*** Subsetting .vcf for each feature
--- Subsetting exons.chr21.bed.vcf
    + Covering 1107407 bp
--- Subsetting processed_pseudogene.chr21.bed.vcf
    + Covering 956640 bp
--- Subsetting protein_coding.chr21.bed.vcf
    + Covering 13780687 bp

	creates file subset_regions.sh
	
	to confirm if the graphs match: open the files and compare
	-cmp -b file1 file2
	b will print where the files differ
	note: files differ on the version of matplotlib
	-diff
	-md5sum used for sequencing data, will show you a long sequence of numbers and letters, if it's the same for both your files then they're the same 
	
	snRNA, pseudogene, lncRNA, MT_tRNA
	
	
	most SNPs are low frequency. fewer individuals have a high number of SNPs, because SNPs are rare. a few have higher frequency, indicating that multiple individuals have SNPs in that specific genetic location.
	
	
	Exercise 3:
	
	Synopsis: It takes genetic location info from the bed file and applies it to the vcf file, allowing it to align SNP location with individual and info about the genetic location of the SNP.
	Usage: bash do_all.sh <bed file><vcf file>
	Dependencies: bedtools, bash, matplotlib, python3. 
	Description: 1. First it ensures that the VCF and GTF file can be found. 
	2. Then it calls in the bed file, which it proceeds to create the bed file of interest by using bedtools to search for the lines tha contain info about gene type
	3. it then intersects the vcf file (contains info about whether a given genome has a SNP in a specific location) and bed file (contains info about where the SNPs are and what gene type the are in)
	4. this gives a file with info about how many alleles in the sample population have a given SNP and what gene type the SNP is in.
	5. this information can be plotted in a histogram.
	Output: The output will be a vcf file. 
	
	
This script parses the genetic location of a SNP and gives the frequency of SNPs in that genetic location across a sample of genomes. 


	explain the input file, what is the output file, etc, for the do_all file 
	explain each setp of the code, what does the
	documentation: 
	dependies: softwhere on the conda environment (ie, bedtools, matplotlib)
	