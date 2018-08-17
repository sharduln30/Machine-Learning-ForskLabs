# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 17:26:08 2018

@author: Shardul Negi
"""

import numpy as np
import matplotlib.pyplot as plt

income = np.random.normal(5, 2, 1000)

plt.hist(income,100)
plt.show()

income.std()#standard deviation
income.var()#variation

