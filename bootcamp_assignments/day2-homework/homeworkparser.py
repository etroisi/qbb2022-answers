#vcf parser: basically makes every column into a list for a specific SNP, items in a list are different columns in the original vcf file.

#cross referencing the random snippet vcf with dbSNP to find the SNPs that overlap between the two files and also the ID of the SNP, which is in the dbSNP

#search through as a dictionary because you search through fewer things


#!/usr/bin/env python3
#read in random_snippet.vcf
#read in dbSNP.vcf

import vcfParser
kgp = vcfParser.parse_vcf("random_snippet.vcf")#read in random_snippet.vcf
dbSNP = vcfParser.parse_vcf("dbSNP_snippet.vcf")#read in dbSNP.vcf
#print(dbSNP)
#vcf parser already skipped headers

dbSNP_dict = {}#make a dictionary

#add info to the dictionary
#for every snp in dbsnp, add snp to dictionary
#dictionary entry is {key : value} key is what you use to look things up, like the word in a dictionary. so you need to search by the position.
#for every dictionary, key is chrm+pos and value is ID 
#method one: can store them as a tuple (chrom, pos) ("chr21", ###)
#method two: can store as a string "chrom_pos" "chr21_#"
#so final dictionary entry is {("chr21, ###pos") : ID}
for snp in dbSNP:
    #print(snp)#every line is a list of the columns for that snp
    #add stuff to dictionary by doing dict_name[key] = value
    #dbSNP_dict[]
    chrom = snp[0]
    pos = snp[1]
    newkey = (chrom, pos) #need to specify which member of the list it is #new key grabs crhom and pos
    newvalue = snp[2]#choose 
    dbSNP_dict[newkey] = newvalue #for loop is going through every item in dbsnp and is pulling up chr, position, and ID, and the key : value 
#mylist = [["chr1", 1], ["chr2", 2]]
    #for item in mylist:
        #chrom = item[0]

#print(dbSNP) <-- IF YOU PRINT HERE IT WORKS
#want to create a dictionary to store dbSNP info and look up random snippet SNPs in the dbSNP dictionary, and then match each SNP to a dbSNP ID

#now we want to look up randon snippet SNPs in the dbSNP dictionary, using their chr and position, match SNP to SNP ID. go through kgp, grab position, find it in dictionary, grab matching ID info
#need to make the counter variable too before the for loop, need to have the things before you put them in the box
no_id_counter = 0 #it's zero before you actually do the for loop
for snp in kgp:
#if snp is in dictionary (dbsnp_dict), grab its ID
     #print(snp)
     chrom = snp[0]
     pos = snp[1]
     query_key = (chrom, pos)
     #how to search in a dictionary with a key? 1. is the key in the dictionary, and 2. if it is, extract associated value
     if query_key in dbSNP_dict:#hey dictionary to you have an entry called (chrom, pos) (but specific chromosomes and position)
     #dict_name[key] this will give the value associated with the key you put in
         id_of_interest = dbSNP_dict[query_key]#gives the value for the qiery key we just made #but you want to
     else:
         no_id_counter += 1 #if no id, add 1 to 0
print(no_id_counter)
         
#snp looks like this: ['chr21', 43029868, '.', 'A', 'T', '.', 'PASS', {'AC': 1, 'AN': 5096, 'DP': 317256, 'AF': 0.0, 'EAS_AF': 0.0, 'EUR_AF': 0.0, 'AFR_AF': 0.0, 'AMR_AF': 0.0, 'SAS_AF': 0.0, 'EX_TARGET': None, 'VT': 'SNP', 'NS': 2548}, 'GT', '0|0'....]
#make a tuple of the first and second rows
#create a query key that looks like chr, pos
#create a dictionary that stores the info 
#there's 100 malformed entries!!--24 lines for the input file that that didn't match the format, and the 100 is the number of SNPs with no ID 

