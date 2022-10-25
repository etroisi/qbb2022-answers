#!/usr/bin/env python

import sys

import numpy
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import seaborn as sns

def main():
    # in1_fname should be ddCTCF
    # in2_fname should be dCTCF
    # bin_fname should be bed file with bin locations
    
    in1_fname, bin_fname, out_fname = sys.argv[1:4]
    data1 = numpy.loadtxt(in1_fname, dtype=numpy.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    frags = numpy.loadtxt(bin_fname, dtype=numpy.dtype([
        ('chr', 'S5'), ('start', int), ('end', int), ('bin', int)]))

    chrom = b'chr15'
    start_bin = 54878
    end_bin = 54951

    



    dctcf=data1[numpy.where((data1["F1"]>start_bin) & (data1["F2"]<end_bin))]
    dctcf["score"] = numpy.log10(dctcf["score"])
    dctcf["F1"] = dctcf["F1"]-start_bin
    dctcf["F2"] = dctcf["F2"]-start_bin
    dctcf["score"] = dctcf["score"]-numpy.min(dctcf["score"])
    things2=end_bin-start_bin
    mat2=numpy.zeros((things2, things2))
    mat2[dctcf['F1'], dctcf['F2']] = dctcf['score']
    mat2[dctcf['F2'], dctcf['F1']] = dctcf['score']
    #print(mat2)
    
    interactionscores=[]
    
    for i in range(5,end_bin-start_bin-10):#range of bins that we can actually look at--at the 0,0 position of the matrix, can't look at the 5 upstream bins, and for the end_bin,end_bin position, can't look at the 5 bins that are downstream, so only look at those bins that have 5 bins upstream and downstream of them
        meanscores=numpy.mean(mat2[(i - 5):i, i:(i + 5)])
        interactionscores.append(meanscores)
        
    location=numpy.linspace(10400000, 13400000, len(interactionscores))
    
    fig, ax = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, figsize=(5,6.25))
    ax[0].axis('off')
    ax[0].imshow(mat2, cmap="RdPu")
    plt.margins(x=0)
    ax[1].scatter(location,interactionscores)
    ax[1].set_xlim(10400000, 13400000)
    plt.subplots_adjust(left=0.15,
                    bottom=0.1,
                    right=1.0,
                    top=1.0,
                    wspace=0.4,
                    hspace=0.0)
    plt.tight_layout()
    plt.show()
    
# numpy.mean(mat[(i - 5):i, i:(i + 5)])
    
if __name__ == "__main__":
    main()
