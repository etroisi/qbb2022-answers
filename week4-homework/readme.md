plink --vcf /Users/cmdb/qbb2022-answers/week4-homework/gwas_data/genotypes.vcf --pca 10 #take the top ten PCs for this data set

plink --freq --vcf /Users/cmdb/qbb2022-answers/week4-homework/gwas_data/genotypes.vcf #get allele frequency from it

plink --vcf /Users/cmdb/qbb2022-answers/week4-homework/gwas_data/genotypes.vcf --linear --pheno /Users/cmdb/qbb2022-answers/week4-homework/gwas_data/CB1908_IC50.txt --covar plink.eigenvec --allow-no-sex --out cb1908 #associate genotype with phenotype, ignoring population (covariate)

plink --vcf /Users/cmdb/qbb2022-answers/week4-homework/gwas_data/genotypes.vcf --linear --pheno /Users/cmdb/qbb2022-answers/week4-homework/gwas_data/GS451_IC50.txt --covar plink.eigenvec --allow-no-sex --out gs451 #same but for the second file


