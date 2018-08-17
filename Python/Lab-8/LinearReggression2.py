# -*- coding: utf-8 -*-
"""
Created on Fri Mar 09 18:35:14 2018

@author: Shardul Negi
"""

# Importing the libraries
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Bahubali2_vs_Dangal.csv')
features = dataset.iloc[:, :1].values
labels1 = dataset.iloc[:, 1:2].values
labels2 = dataset.iloc[:, 2:3].values


# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor1 = LinearRegression()
regressor2 = LinearRegression()
regressor1.fit(features, labels1)
regressor2.fit(features, labels2)

# Predicting the Test set results
labels_pred = regressor1.predict(features)
tenthday_bahu_pred = regressor1.predict(10)

labels_pred = regressor2.predict(features)
tenthday_dan_pred = regressor2.predict(10)

# Model Score
Score = regressor1.score(features,labels1)
Score = regressor2.score(features,labels2)

# Visualising the Training set results
plt.plot(features, labels1, color = 'red')
plt.plot(features, labels2, color = 'green')
plt.scatter(10, regressor1.predict(10), color = 'blue')
plt.scatter(10, regressor2.predict(10), color = 'black')

plt.title('Movie vs Days (Training set)')
plt.xlabel('Days')
plt.ylabel('Movie')
plt.show()

# Visualising the Test set results
plt.scatter(features, labels1, color = 'red')
plt.scatter(features, labels2, color = 'green')
plt.plot(features, regressor1.predict(features), color = 'blue')
plt.plot(features, regressor2.predict(features), color = 'black')

plt.title('Movie vs Days (Test set)')
plt.xlabel('Days')
plt.ylabel('Movie')
plt.show()