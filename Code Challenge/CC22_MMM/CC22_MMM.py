# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 19:17:59 2018

@author: Shardul Negi
"""

import numpy as np

import matplotlib.pyplot as plt

incomes = np.random.normal(100.0, 20.0, 10000)

print incomes

plt.hist(incomes, 50)

np.median(incomes)

np.mean(incomes)

incomes = np.append(incomes, [10000000000])

