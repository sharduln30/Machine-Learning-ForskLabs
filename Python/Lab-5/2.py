# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 17:47:15 2018

@author: Shardul Negi
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values #iloc=index location
y = dataset.iloc[:, 3].values


