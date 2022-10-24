# Week 3 Variant Calling -- Feedback

1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 0 = 9 points out of 10 possible points

1. Index genome

  * --> +1  

2. align reads

  * --> +1
  * would recommend listing all the samples if you're going to say something like "do this for all A01 files". Alternatively, you could employ a `for` loop in bash:
  ```
  for ID in 09 11 23 24 27 31 35 39 62 63; do
  	bwa mem -t 4 -R "@RG\tID:A01_${ID}\tSM:A01_${ID}" -o A01_${ID}aligned.sam  sacCer3.fa A01_${ID}.fastq
    samtools sort -o A01_${ID}alignedsorted.bam -O bam A01_${ID}aligned.sam
    samtools index -b A01_${ID}alignedsorted.bam
  done
  ```

3. sort bam files and index sorted bam files (0.5 points each)

  * --> +1

4. variant call with freebayes

  * perfect! --> +1

5. filter variants

  * --> +1

6. decompose complex haplotypes

  * --> +1

7. variant effect prediction

  * great! --> +1

8. python plotting script

  * beautiful script! --> +1

9. 4 panel plot (0.25 points each panel)

  * good! --> +1

10. 1000 line vcf

  * I don't see the vcf file. Did you do `git add --force <yourweek3.vcf>`? Please add the file and let a TA know if you need help --> +0
