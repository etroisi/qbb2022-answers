#!/usr/bin/env python

import numpy
#import pandas as pd
from scipy.stats import binomtest
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.multitest import multipletests

def simulate_coin_toss(n_tosses, prob_heads = 0.5, seed=None):#returns an array of results, in the form of 1 and 0, so output is going to be n_tosses
    '''
    Simulates a coin toss (fair or unfair depending on prob_heads)
    Input: n_tosses, an integer, number of coin tosses to simulate
           prob_heads, a float, the probability the coin toss will return heads; default is 0.5, meaning a fair coin
           seed, an integer, the random seed that will be used in the simulation; default is None
    Output: results_arr, an array of 1's and 0's with 1's representing heads and 0's representing tails
    Resources: https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html
    '''
    if seed is not None:
        numpy.random.seed(seed)
    results_arr = numpy.random.choice([0,1], size=n_tosses, p = [1-prob_heads, prob_heads])
    return (results_arr)

def perform_hypothesis_test(n_heads, n_tosses):
    '''
    Performs a two-sided binomial test
    Input: n_heads, an integer, number of coin tosses that resulted in heads/success
           n_tosses, an integer, total number of coin tosses/trials
    Output: pval, a float reporting the final pvalue from the binomial test
    Resources: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binomtest.html#scipy.stats.binomtest
    '''
    binom_result = binomtest(n_heads, n_tosses)
    pval = binom_result.pvalue
    return(pval)

def correct_pvalues(pvals):
    '''
    Will apply the bonferroni multiple hypothesis testing correction method to input pvalues
    Input: pvals, an array-like object containing uncorrected pvalues
    Output: corrected_pvalues[1], an array containing corrected pvalues
    Resources: https://www.statsmodels.org/dev/generated/statsmodels.stats.multitest.multipletests.html
    '''
    corrected_pvalues = multipletests(pvals, method='bonferroni')
    return(corrected_pvalues[1])

def interpret_pvalues(pvals):
    '''
    Will interpret or convert pvalues from floats to booleans (Trues or Falses) reporting whether or not you reject the null hypothesis
    True -- reject null Hypothesis
    False -- fail to reject null hypothesis
    Input: pvals, an array-like object containing pvalues (floats)
    Output: interpreted, an array containing booleans
    '''
    interpreted = numpy.array(pvals) < 0.05
    return (interpreted)

def compute_power(n_rejected_correctly, n_tests):
    '''
    Will compute the power, defined as the number of correctly rejected null hypothesis divided by the total number of tests (AKA the True Positive Rate or the probability of detecting something if it's there)
    Input: n_rejected_correctly, an integer, the total number of tests in which the null hypothesis was correctly rejected
           n_tests, an integer, the total number of hypothesis tests which were performed
    output: power, a float, the power
    '''
    power = n_rejected_correctly / n_tests
    return(power)

def run_experiment(prob_heads, n_toss, n_iters = 100, seed = 389, correct_the_pvalues = False):#if doing corrected pvalues, correct_the_pvalues = True
    '''
    Input: prob_heads, a float, the probability of a simulated coin toss returning heads
           n_toss, an integer, the number of coin tosses to simulate
           n_iters, an integer, the number of iterations for each simulation. default is 100
           seed, an integer, the random seed that you will set for the whole simulation experiment. default is 389
           correct_the_pvalues, a boolean, whether or not to perform multiple hypothesis testing correction
    Output: power, a float, the power of the experiment
    '''
    
    #n_tosses= [10, 50, 100]
    #prob_heads = [0.55, 0.75, 1.0]        
    numpy.random.seed(seed)
    pvals = []
    #i could put the other for loop here:
    #for i,p in enumerate(probs): #i is column, j is row. n is n_tosses, p is prob_heads
         #for j,n in enumerate(tosses): 
            #power=run_experiment(p, n)
            #power_mat[i,j] = power
    for k in range(n_iters):#if the above forloop was here we would need to indent the following lines
        results_arr = simulate_coin_toss(n_toss, prob_heads = prob_heads)
        n_success = numpy.sum(results_arr)
        pvals.append(perform_hypothesis_test(n_success, n_toss))
    if correct_the_pvalues:
        pvals = correct_pvalues(pvals)
    pvals_translated_to_bools = interpret_pvalues(pvals)
    power = compute_power(numpy.sum(pvals_translated_to_bools), n_iters)
    return(power)
    
    
tosses = numpy.array([10, 50, 100, 250, 500, 1000])
probs = numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)[::-1]
power_mat=numpy.zeros((len(probs), len(tosses)), dtype = float)

# for i,p in enumerate(probs): #i is column, j is row. n is n_tosses, p is prob_heads
#      print(p)
#      for j,n in enumerate(tosses):
#         power=run_experiment(n,p)
#         power_mat[i,j] = power
#seed = 1243
#numpy.random.seed(seed) <--if i put this here, the seed would only be set once. I have it now as setting every time i run experiment, because it is in the run experiment function.

for i,p in enumerate(probs): #i is column, j is row. n is n_tosses, p is prob_heads
     for j,n in enumerate(tosses): # you could put this within the run experiment function. it would go on top of the for loop that's already there, with the other for loop being nested underneath it
        power=run_experiment(p, n)
        power_mat[i,j] = power



# power1 = run_experiment(0.6, 500, correct_the_pvalues = True)
# power2 = run_experiment(0.95, 10, correct_the_pvalues = True)
# power2b = run_experiment(0.95, 10)
#
fig, ax = plt.subplots()
sns.heatmap(power_mat, vmin=0, vmax=1, xticklabels=tosses, yticklabels=probs, ax=None, cmap='mako')
sns.color_palette("mako") #, as_cmap=True)
plt.title('power uncorrected pvalues')#if using corrected pvalues, 'power corrected pvalues'
plt.xlabel('number of tosses')
plt.ylabel('prob of heads')
plt.show()
plt.savefig('powermapuncorrectedpvalues')#if using corrected values, 'powermapcorrectedpvalues'
# ax.set_xlabel("tosses")
# ax.set_ylabel("probability of heads")
# ax.set_title("Heatmap to Visualize Power")
# fig.savefig("heatmap.png")






#power1 = run_experiment(0.6, 500, correct_the_pvalues = True)
#power2 = run_experiment(0.95, 10, correct_the_pvalues = True)
#power2b = run_experiment(0.95, 10)




            #simulated_coin_toss(n,p) --> power output 
            #power_mat[i,j]-->power output
