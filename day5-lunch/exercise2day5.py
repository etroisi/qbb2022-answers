#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from scipy import stats
import statsmodels.api as sm

df = np.genfromtxt("probandsandparentage", delimiter=' ', dtype=None, encoding=None, 
    names=["proband", "fatherage", "motherage", "fathermutation", "mothermutation"])



#fig, ax = plt.subplots()
#ax.scatter(df["motherage"], df["mothermutation"])
#ax.set_ylabel("mother mutation")
#ax.set_xlabel("mother age")
#ax.set_title('mother age vs mother mutation')
#ax.legend()
#plt.savefig('ex2_a.png')
#plt.show()


fig, ax = plt.subplots()
ax.scatter(df["fatherage"], df["fathermutation"])
ax.set_ylabel("fathermutation")
ax.set_xlabel("father age")
ax.set_title("father age vs father mutation")
#ax.legend()
#plt.savefig('ex2_b.png')
#plt.show()

full_model = smf.ols(formula = "fathermutation ~ 1 + fatherage", data = df).fit()

print(full_model.summary())
print(full_model.pvalues)

#fig, ax = plt.subplots()
#ax.hist(df["mothermutation"], alpha = 0.5, label = "mother mutation")
#ax.hist(df["fathermutation"], alpha = 0.5, label = "father mutation")
#ax.set_ylabel("frequency")
#ax.set_xlabel("number of mutations")
#ax.legend()
#plt.show()
#plt.savefig('histogramofmutationsandparentage.png')

new_data = df[0]
new_data.fill(0)
new_data['fatherage'] = 50.5
print(full_model.predict(new_data))

print(1.35*50.5 +10.33)


