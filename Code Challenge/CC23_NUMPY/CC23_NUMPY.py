# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 19:28:12 2018

@author: Shardul Negi
"""

import matplotlib.pyplot as plt
import numpy as np

print "Make a 3 row x 4 column array of random numbers"
x = np.random.random((3, 4))
print x

print "Add 1 to every element"
x = x + 1
print x

print "Get the element at row 1, column 2"
print x[1, 2]

# The colon syntax is called "slicing" the array. 
print "Get the first row"
print x[0, :]


print "Get every 2nd column of the first row"
print x[0, ::2]

np.max(x)

np.min(x)

np.mean(x)

x.max(axis=1)

x = np.random.binomial(500, .5)
print "number of heads:", x

plt.hist(x)

x = np.random.binomial(500, 1)
print "number of heads:", x

plt.hist(x)

