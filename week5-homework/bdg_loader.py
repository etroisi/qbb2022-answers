#!/usr/bin/env python

import sys


import numpy
import matplotlib.pyplot as plt

def load_data(fname):
    # Load in the bedgraph with columns chr, start, end, and score
    bg = numpy.loadtxt(fname, usecols=(1,2,3), dtype=numpy.dtype([
        ('start', int), ('end', int), ('score', float)]))
    # Find the lowest coordinate
    start = bg['start'][0]
    # Create an array at bp resolution
    array = numpy.zeros(bg['end'][-1] - start, dtype=numpy.dtype(
        [('pos', int), ('score', float)]))
    # For each line in the bedgraph, set positions across range with score
    for i in range(bg.shape[0]):
        array['score'][bg['start'][i] - start:bg['end'][i] - start] = bg['score'][i]
    # Set coordinates in array
    array['pos'] = numpy.arange(start, start + array.shape[0])
    # Bin array into 100bp bins
    hist = numpy.histogram(array['pos'], weights=array['score'], bins=(array.shape[0] // 100))
    # Create final data dict
    X = (hist[1][1:] + hist[1][:-1]) / 2
    Y = hist[0]
    data = {'X': X, 'Y':Y}
    return data
    
d0h3k27acdata=load_data('scaledd0h3k27acropped')
d2h3k27acdata=load_data('scaledd2h3k27acropped')
klf4data=load_data('scaledklf4cropped')
sox2r1data=load_data('scaledsox2r1cropped')


fig, axs = plt.subplots(4)
axs[0].plot(d0h3k27acdata['X'],d0h3k27acdata['Y'])
axs[0].set_ylabel("D0_H3K27ac")


axs[1].plot(d2h3k27acdata['X'],d2h3k27acdata['Y'])
axs[1].set_ylabel("D2_H3K27ac")


axs[2].plot(klf4data['X'],klf4data['Y'])
axs[2].set_ylabel("KLF4")


axs[3].plot(sox2r1data['X'],sox2r1data['Y'])
axs[3].set_ylabel("Sox2_R1")
plt.show()
