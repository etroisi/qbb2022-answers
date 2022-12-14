python ../../scripttt.py /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/SRR492183.kraken SRR492183

python ../../scripttt.py /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/SRR492186.kraken SRR492186

python ../../scripttt.py /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/SRR492188.kraken SRR492188

python ../../scripttt.py /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/SRR492189.kraken SRR492189
 
python ../../scripttt.py /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/SRR492190.kraken SRR492190

python ../../scripttt.py /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/SRR492193.kraken SRR492193

python ../../scripttt.py /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/SRR492194.kraken SRR492194

python ../../scripttt.py /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/SRR492197.kraken SRR492197


ktImportText /Users/cmdb/qbb2022-answers/week14-homework/Krona/KronaTools/SRR492183_krona.txt 

ktImportText /Users/cmdb/qbb2022-answers/week14-homework/Krona/KronaTools/SRR492186_krona.txt 

ktImportText /Users/cmdb/qbb2022-answers/week14-homework/Krona/KronaTools/SRR492188_krona.txt 

ktImportText /Users/cmdb/qbb2022-answers/week14-homework/Krona/KronaTools/SRR492189_krona.txt 

ktImportText /Users/cmdb/qbb2022-answers/week14-homework/Krona/KronaTools/SRR492190_krona.txt

ktImportText /Users/cmdb/qbb2022-answers/week14-homework/Krona/KronaTools/SRR492193_krona.txt 

ktImportText /Users/cmdb/qbb2022-answers/week14-homework/Krona/KronaTools/SRR492194_krona.txt

ktImportText /Users/cmdb/qbb2022-answers/week14-homework/Krona/KronaTools/SRR492197_krona.txt 

Trends: actinobacteria percentage increases over time. enterococcus faecalis decreases over time.

bwa index /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/assembly.fasta 

bwa mem -t4 /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/assembly.fasta /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/READS/SRR492183_1.fastq /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/READS/SRR492183_2.fastq > 183bwamemed.sam

then decided to do a for loop for bwa mem instead of typing it out 7 more times

for i in 83 86 88 89 90 93 94 97; do bwa mem -t4 /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/assembly.fasta /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/READS/SRR4921${i}_1.fastq /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/READS/SRR4921${i}_2.fastq > 1${i}bwamemed.sam; done



for i in 83 86 88 89 90 93 94 97; do samtools sort -o 1${i}samtoolssorted.sam 1${i}bwamemed.sam; done

jgi_summarize_bam_contig_depths --outputDepth depth.txt *sorted.sam

metabat2 -i /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/assembly.fasta  -a depth.txt -o bins_dir/bin

grep NODE *.fa | cut -d"_" -f 4 | paste -sd+ - | bc

3A. 6 bins
3B. 13187322 in bins, 38071686 in assembly file. 34.6%--percent of dna sequences that are assigned to a species. meaning, 2/3 of the reads, metabat cannot tell us what species they are coming from. 
3C. prokaryotic genomes appear to be around 5 million bases or less, and these look to be much smaller than that. each bin is what metabat thinks is one species. 
3D. contaiminated means coming from more than one species--metabat combined two species when it should not have. one way to check this would be to align the reads of a bin using blast. if all the reads in the bin align to one species, then metabat did its job correctly. if not, then "comtaimination" is occuring (ie, multiple species in one bin). to find how complete each bin is, compare the reads in the bin to the complete genome. 



Part 4
grep NODE bin.1.fa > nodesbin1.txt
grep NODE bin.2.fa > nodesbin2.txt
grep NODE bin.3.fa > nodesbin3.txt
grep NODE bin.4.fa > nodesbin4.txt
grep NODE bin.5.fa > nodesbin5.txt
grep NODE bin.6.fa > nodesbin6.txt

while read p; do grep p /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/assembly.kraken; done <nodesbin1.txt

while read p; do grep p /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/assembly.kraken; done <nodesbin2.txt | cut -f2 | sort | uniq -c | sort -n > bin2species.txt

while read p; do grep p /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/assembly.kraken; done <nodesbin3.txt | cut -f2 | sort | uniq -c | sort -n > bin3species.txt

while read p; do grep p /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/assembly.kraken; done <nodesbin4.txt | cut -f2 | sort | uniq -c | sort -n > bin4species.txt

while read p; do grep p /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/assembly.kraken; done <nodesbin5.txt | cut -f2 | sort | uniq -c | sort -n > bin5species.txt

while read p; do grep p /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/assembly.kraken; done <nodesbin6.txt | cut -f2 | sort | uniq -c | sort -n > bin6species.txt

4B. species with the most nodes bin 1: Finegoldia magna (28875 nodes, ATCC 29328)
species with the most nodes bin 2: Finegoldia magna (40950 nodes, ATCC 29328)
species with the most nodes bin 3: Finegoldia magna (4200 nodes, ATCC 29328)
species with the most nodes bin 4: Finegoldia magna (19425 nodes, ATCC 29328)
species with the most nodes bin 5: Finegoldia magna (6825 nodes, ATCC 29328)
species with the most nodes bin 6: Finegoldia magna (3150 nodes, ATCC 29328)
all bins appear to have the most nodes from the same species. the species with the second highest number of nodes in all of the bins is interestingly p. acnes, the bacteria that causes acne. 

4C. perhaps a better way would be to use a local alignment tool, like blast. 





