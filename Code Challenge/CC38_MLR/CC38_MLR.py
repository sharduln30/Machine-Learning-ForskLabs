# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 18:12:20 2018

@author: Shardul Negi
"""

# Multiple Linear Regression
# Importing the libraries
import numpy as np
import pandas as pd
# Importing the dataset
dataset = pd.read_csv('iq_size.csv')
features = dataset.iloc[:, 1:].values
labels = dataset.iloc[:, :1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split 

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

## Feature Scaling
#from sklearn.preprocessing import StandardScaler
#sc = StandardScaler()
#features_train = sc.fit_transform(features_train)
#features_test = sc.transform(features_test)

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)

# Predicting the Test set results
Pred = regressor.predict(features_test)



# Getting Score for the Multi Linear Reg model
Score = regressor.score(features_train, labels_train)

# Predicting the results
test_pred = regressor.predict(np.array([90,70,150]).reshape(1,-1))

# Building the optimal model using Backward Elimination
import statsmodels.formula.api as sm
features = np.append(arr = np.ones((38, 1)).astype(int), values = features, axis = 1)

features_opt = features[:, [0, 1, 2, 3]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:, [0, 1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:, [1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:, [1]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()





