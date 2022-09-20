#vcf parser: basically makes every column into a list for a specific SNP, items in a list are different columns in the original vcf file.

#cross referencing the random snippet vcf with dbSNP to find the SNPs that overlap between the two files and also the ID of the SNP, which is in the dbSNP

#search through as a dictionary because you search through fewer things


#!/usr/bin/env python3
#read in random_snippet.vcf
#read in dbSNP.vcf

import vcfParser
kgp = vcfParser.parse_vcf("random_snippet.vcf")
dbSNP = vcfParser.parse_vcf("dbSNP_snippet.vcf")
print(dnSNP)


#want to create a dictionary to store dbSNP info and look up random snippet SNPs in the dbSNP dictionary, and then match each SNP to a dbSNP ID

#create a dictionary that stores the info 

