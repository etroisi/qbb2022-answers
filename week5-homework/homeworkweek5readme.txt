Week 5 Homework, 10/10/22
Step 1. 
samtools view -q 10 D2_Sox2_R1_input.bam > samviewsox2r1input

samtools view -q 10 D2_Sox2_R2_input.bam > samviewsox2r2input

samtools view -q 10 D2_Sox2_R2.bam > samviewsox2r2

samtools view -q 10 D2_Sox2_R1.bam > samviewsox2r1

Step 2.
macs2 callpeak -t samviewsox2r1 -c samviewsox2r1input -g 95000000 -n peakssox2r1.bed -B

macs2 callpeak -t samviewsox2r2 -c samviewsox2r2input -g 95000000 -n peakssox2r2.bed -B

Step 3.
bedtools intersect -a peakssox2r1.bed_peaks.narrowPeak -b peakssox2r2.bed_peaks.narrowPeak > sox2peaksintersect.bed

Step 4. 
bedtools intersect -a sox2peaksintersect.bed -b D2_Klf4_peaks.bed > sox2intersectklf4.bed
wc -l sox2intersectklf4.bed : 40 peaks
wc -l D2_Klf4_peaks.bed : 60
wc -l peakssox2r1.bed_peaks.narrowPeak : 765

40 peaks shared by klf4 and sox2. 60 peaks for klf4 total. 40/60 = 66.67%


Step 5.
python scale_bdg.py peakssox2r1.bed_treat_pileup.bdg scaledsox2r1peaks
python scale_bdg.py D2_klf4_treat.bdg scaledklf4
python scale_bdg.py D2_H3K27ac_treat.bdg scaledd2h3k27ac
python scale_bdg.py D0_H3K27ac_treat.bdg scaledd0h3k27ac

awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' scaledd0h3k27ac > scaledd0h3k27acropped
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' scaledd2h3k27ac > scaledd2h3k27acropped
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' scaledklf4 > scaledklf4cropped
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' scaledsox2r1peaks > scaledsox2r1cropped

Motif finding.
sort -k 5 peakssox2r1.bed_peaks.narrowPeak > peakssox2r1sorted
head -n 300 peakssox2r1sorted > 300peakssox2r1
awk '{ printf "%s:%i-%i\n", $1, $2, $3 }' 300peakssox2r1 > 300peakssox2r1reformated
samtools faidx mm10.fa -r 300peakssox2r1reformated > mm10300sox2r1peaks
note: switch conda environments here to meme
meme-chip -maxw 7 mm10300sox2r1peaks
note: output is memechip_out directory, use combined.meme file for next line
tomtom /Users/cmdb/qbb2022-answers/week5-homework/memechip_out/combined.meme motif_databases/MOUSE/HOCOMOCOv11_full_MOUSE_mono_meme_format.meme
examine file:///Users/cmdb/qbb2022-answers/week5-homework/tomtom_out/tomtom.html (note: lots of Gs, similar sequences)

grep -e "Klf4" -e "Sox2" /Users/cmdb/qbb2022-answers/week5-homework/tomtom_out/tomtom.tsv > klf4sox2matches

conda deactivate