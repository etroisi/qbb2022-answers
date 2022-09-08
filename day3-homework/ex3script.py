#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt

joinedfile=np.genfromtxt("sortedeigenvecandpanel.txt",
                    dtype = None,
                    encoding = None,
                    names = ["person", "population", "superpopulation", "sex", "person1", "pca1", "pca2", "pca3"])
superpop = (np.unique(joinedfile["superpopulation"]))
gender = (np.unique(joinedfile["sex"]))
pop = (np.unique(joinedfile["population"]))

#pca plot colored for superpopulation:
# fig, ax = plt.subplots()
# xs = []
# ys = []
# for i, suppop in enumerate(superpop):
#     row1 = np.where(joinedfile["superpopulation"] == suppop)
#     xs.append(joinedfile["pca1"][row1])
#     ys.append(joinedfile["pca2"][row1])
#     ax.scatter(xs[i], ys[i], label = suppop)
# ax.set_xlabel("pca1")
# ax.set_ylabel("pca2")
# ax.set_title("PCA 1 versus 2 superpopulation")
# plt.show()

#pca plot colored for gender:
# fig, ax = plt.subplots()
# xg = []
# yg = []
# for i, gender in enumerate(gender):
#     row1 = np.where(joinedfile["sex"] == gender)
#     xg.append(joinedfile["pca1"][row1])
#     yg.append(joinedfile["pca2"][row1])
#     ax.scatter(xg[i], yg[i], label = gender)
# ax.set_xlabel("pca1")
# ax.set_ylabel("pca2")
# ax.set_title("PCA 1 versus 2 gender")
# plt.show()

#pca plot colored for population
fig, ax = plt.subplots()
xg = []
yg = []
for i, pop in enumerate(pop):
    row1 = np.where(joinedfile["population"] == pop)
    xg.append(joinedfile["pca1"][row1])
    yg.append(joinedfile["pca2"][row1])
    ax.scatter(xg[i], yg[i], label = pop)
ax.set_xlabel("pca1")
ax.set_ylabel("pca2")
ax.set_title("PCA 1 versus 2 population")
plt.show()


