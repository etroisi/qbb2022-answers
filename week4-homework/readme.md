Week 4 homework

Question 2. plink --vcf /Users/cmdb/qbb2022-answers/week4-homework/gwas_data/genotypes.vcf --pca 10 #take the top ten PCs for this data set

Question 3. plink --freq --vcf /Users/cmdb/qbb2022-answers/week4-homework/gwas_data/genotypes.vcf #get allele frequency from it

Question 4. plink --vcf /Users/cmdb/qbb2022-answers/week4-homework/gwas_data/genotypes.vcf --linear --pheno /Users/cmdb/qbb2022-answers/week4-homework/gwas_data/CB1908_IC50.txt --covar plink.eigenvec --allow-no-sex --out cb1908 #associate genotype with phenotype, ignoring population (covariate)

plink --vcf /Users/cmdb/qbb2022-answers/week4-homework/gwas_data/genotypes.vcf --linear --pheno /Users/cmdb/qbb2022-answers/week4-homework/gwas_data/GS451_IC50.txt --covar plink.eigenvec --allow-no-sex --out gs451 #same but for the second file

top associated snp for gs: 1.43e-07, rs7257475
Human Gene ZNF826: a zinc finger protein, a pseudogene, "predicted to enable DNA binding transcription factor activity", specifically RNA pol II cis-regulatory sequence DNA binding activity, according to NCBI



