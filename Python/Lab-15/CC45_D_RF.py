# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 17:13:01 2018

@author: Shardul Negi
"""
# Decision Tree Regression
# Importing the libraries
import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('PastHires.csv')
X = dataset.iloc[:, 0:6].values
y = dataset.iloc[:, 6].values

# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
X[:,1] = labelencoder.fit_transform(X[:,1])
X[:,3] = labelencoder.fit_transform(X[:,3])
X[:,4] = labelencoder.fit_transform(X[:,4])
X[:,5] = labelencoder.fit_transform(X[:,5])

# Encoding the Dependent Variable
y = labelencoder.fit_transform(y)

# Fitting Decision Tree Regression to the dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X, y)

# Fitting Random Forest Classification to the Training set
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy',
random_state = 0)
classifier.fit(X, y)

x1_ans= classifier.predict_proba(np.array([10, 1, 4, 0, 1, 0  ]).reshape(1,-1))

y1_ans= classifier.predict_proba(np.array([10, 0, 4, 1, 0, 0 ]).reshape(1,-1))
