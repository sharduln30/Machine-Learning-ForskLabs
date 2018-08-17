# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 18:00:07 2018

@author: Shardul Negi
"""

#Importing the dataset
import pandas as pd

dataset = pd.read_csv('Cars.csv')

x = dataset.iloc[:, 1:3].values

from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values = 'NaN', strategy = 'median', axis = 0)

imputer = imputer.fit(x[:, 1:2])

x[:, 1:2] = imputer.transform(x[:, 1:2])




 