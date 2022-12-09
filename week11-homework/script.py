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
#sc.pl.rank_genes_groups(adata)

#AC cells are cluster 5, Dpi and Fabp3
#MG cells are cluster 26, fcgr3 and c1qb
#OL cells are cluster 21, olig1 and 2
#aSMC cluster 4, slit3
#vEC cluster 16, hbb-bs
#aEC cluster 9, igfbp3

clusternames = {
    '5': 'AC',
    '26': 'MG',
    '21': 'OL',
    '4': 'aSMC',
    '16': 'vEC',
    '9': 'aEC'
}
adata.obs['cell_type'] = adata.obs['leiden'].map(clusternames).astype('category')
sc.pl.tsne(adata, color = 'cell_type')
sc.pl.tsne(adata, color = 'Dbi')
sc.pl.tsne(adata, color = 'Fcgr3')
sc.pl.tsne(adata, color = 'Olig1')
sc.pl.tsne(adata, color = 'Slit3')
sc.pl.tsne(adata, color = 'Hbb-bs')
sc.pl.tsne(adata, color = 'Igfbp3')
