# -*- coding: utf-8 -*-
"""
Created on Fri Mar 09 18:04:52 2018

@author: Shardul Negi
"""

# Importing the libraries
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Foodtruck.csv')
features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = regressor.predict(features_test)

# Predicting the Test set results
jaipur_pred = regressor.predict(3.073)

# Model Score
Score = regressor.score(features_test,labels_test)

# Visualising the Training set results
plt.scatter(features_train, labels_train, color = 'red')
plt.plot(features_train, regressor.predict(features_train), color = 'blue')
plt.title('Profit vs Population (Training set)')
plt.xlabel('Population')
plt.ylabel('Profit')
plt.show()

# Visualising the Test set results
plt.scatter(features_test, labels_test, color = 'red')
plt.plot(features_train, regressor.predict(features_train), color = 'blue')
plt.title('Profit vs Population (Test set)')
plt.xlabel('Population')
plt.ylabel('Profit')
plt.show()