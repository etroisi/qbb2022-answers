plink --vcf ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf.gz --pca 3

unix command line: 
sort plink.eigenvec | sort integrated_call_samples.panel | join integrated_call_samples.panel plink.eigenvec > joinedfile