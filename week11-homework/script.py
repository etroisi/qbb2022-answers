#!/usr/bin/env python3

import scanpy as sc

adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
adata.var_names_make_unique()

sc.tl.pca(adata)#pca for before
#sc.pl.pca(adata)

#flitering
sc.pp.recipe_zheng17(adata)
sc.tl.pca(adata)#make pca for after filtering
#sc.pl.pca(adata)

#using leiden for clustering
sc.pp.neighbors(adata)
sc.tl.leiden(adata)
#make tsne
sc.tl.tsne(adata)
#sc.pl.tsne(adata)

#make umap
sc.tl.umap(adata, maxiter=1000)
#sc.pl.umap(adata)

#rank using t-test
sc.tl.rank_genes_groups(adata, groupby='leiden', method='t-test')
#sc.pl.rank_genes_groups(adata)

#rank using logistic regression
sc.tl.rank_genes_groups(adata, groupby='leiden', method='logreg')
sc.pl.rank_genes_groups(adata)