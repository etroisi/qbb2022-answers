Homework Day 5

Code to isolate mutations from mother, mutations from father, combine them into a file, and combine that file with the parents' ages
cut -d ',' -f 5,6 aau1043_dnm.csv | grep mother > dnmmother
cut -d ',' -f 1 dnmmother > dnmmothercut
sort -n dnmmothercut | uniq -c > dnmmothercutsorted
awk -v OFS='\t' '{print $1, $2}' dnmmothercutsorted > dnmmothercutsortedtab

cut -d ',' -f 5,6 aau1043_dnm.csv | grep father > dnmfather
cut -d ',' -f 1 dnmfather > dnmfathercut
sort -n dnmfathercut | uniq -c > dnmfathercutsorted
awk -v OFS='\t' '{print $1, $2}' dnmfathercutsorted > dnmfathercutsortedtab

join -1 2 -2 2 -t $'\t' dnmfathercutsortedtab dnmmothercutsortedtab > parentsprobandssortedjoined


sed 's/,/\t/g' aau1043_parental_age.csv > sedparentage 
grep -v 'Proband' sedparentage > sedparentnoheader
join sedparentnoheader parentsprobandssortedjoined > probandsandparentage
join sedparentnoheader parentsandprobandssortedjoined > probandsandparentage

yes, statistically signficant relationship between mother age and mother mutation (mutations from mother)
(6.878e-24). it is 0.3776 (in the equation y=mx+b for linear regression, m = 0.3776 (slope of the line). as x increases (age), y increases by 0.3776(mutation))

yes, statistically signficant relationship between father age and father mutation (mutations from father)
(1.552e-84). it is 1.3538 (in the equation y=mx+b for linear regression, m = 1.3538 (slope of the line). as x increases (age), y increases by 1.3538(mutation))

78.50500000000001 mutations if the father was 50.5

6. Ttest_indResult(statistic=53.40356528726923, pvalue=2.198603179308129e-264)
code to get here: print(stats.ttest_ind(df["fathermutation"], df["mothermutation"]))
Yes, the number of maternally inhereted de novo mutations per proband is significantly different than the paternally inherited de novo mutations per proband.





