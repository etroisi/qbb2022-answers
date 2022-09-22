Week 1 9/9/22 homework

Question 1.1. How many 100bp reads are needed to sequence a 1Mbp genome to 5x coverage? How many are needed for 15x coverage?
I need 10Mbp x 24x = 240Mbp of data
240Mbp / 120bp / read = 2M reads

1M * 5 = 5M
1M * 15 = 15M
5M/100 = 50000 reads
15M/100 = 150000 reads



#Question 1.2. Write a program (in Python) to simulate sequencing 5x coverage of a 1Mbp genome with 100bp reads
#see other file

Question 2.1
4

2.2
NODE_1_length_105830_cov_13.380572	105830	36	60	61
NODE_2_length_47860_cov_13.213179	47860	107665	60	61
NODE_3_length_41351_cov_13.316108	41351	156358	60	61
NODE_4_length_39426_cov_13.189810	39426	198434	60	61
total length = 234,467


Question 2.3
#/Users/cmdb/SPAdes-3.15.5-Darwin/bin/spades.py  -1 frag180.1.fq -2 frag180.2.fq --mp-1 1 jump2k.1.fq --mp-2 1 jump2k.2.fq -o .
#grep -c '>' contigs.fasta
4

#samtools faidx contigs.fasta
#cat contigs.fasta.fai
NODE_1_length_105830_cov_13.380572	105830	36	60	61
NODE_2_length_47860_cov_13.213179	47860	107665	60	61
NODE_3_length_41351_cov_13.316108	41351	156358	60	61
NODE_4_length_39426_cov_13.189810	39426	198434	60	61

#largest one is 105830
#n50: 
#tail -n+2 ref.fa | wc -m
#237147 total base pairs in the genome, halfway is 118573
#start from the smallest contig and add the next largest etc until you reach the halfway point of the genome or beyond
#128,637 --> n50 is 47860
#the average identity is 100 dnadiff ref.fa contigs.fasta, cat out.report
#What is the length of the longest alignment [Hint: try nucmer and show-coords]? nucmer ref.fa contigs.fasta

#show-coords out.delta

#all just showing coords and dnadiffing




