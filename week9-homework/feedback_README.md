Awesome job! This all looks great. Just one minor comment:
1. The type of multiple-testing correction that you're currently doing is called bonferroni correction. This type of correction essentially setting the chance of getting any false positives at all. So if you make your bonferroni alpha 0.1, it means that there's only a 10% you have ANY false positives. What we want to correct is the False Discovery rate, which sets the expected proportion of false positives in your significant results. Because of this, your significance threshold is actually much  stricter than it needs to be. `statsmodels.stats.multitest.multipletests()` has an argument called `method` that let's you set the type of correction you want to do. The default is bonferroni, but you can set it to do FDR instead. (-0.2 points)

Really really great work though.

(9.8/10)
