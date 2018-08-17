# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 17:45:54 2018

@author: Shardul Negi
"""

# Polynomial Regression
# Importing the libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Importing the dataset
dataset = pd.read_csv('bluegills.csv')
features = dataset.iloc[:, 0:1].values
labels = dataset.iloc[:, 1].values


# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(features, labels)

# Visualising the Linear Regression results

plt.scatter(features,labels,color='red')
plt.plot(features,lin_reg.predict(features),color='blue')
plt.title('length vs age(linear regression)')
plt.xlabel('age')
plt.ylabel('length')
plt.show()



# Fitting Polynomial Regression to the dataset

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 2)
features_poly = poly_reg.fit_transform(features)
poly_reg.fit(features_poly, labels)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)
print "Predicting result with Linear Regression",
print lin_reg.predict(5)
print "Predicting result with Polynomial Regression",
print lin_reg_2.predict(poly_reg.fit_transform(5))

# Score for Linear Regression Model

linear_score = lin_reg.score(features,labels)

# Score for Polynomial Regression Model

poly_score = lin_reg_2.score(features_poly,labels)



# Visualising the Polynomial Regression results

plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg_2.predict(poly_reg.fit_transform(features)), color =
'blue')
plt.title('bluegill fish-Polynomial Regression')
plt.xlabel('age (in years)')
plt.ylabel('length (in mm)')
plt.show()

# Visualising the Polynomial Regression results (for higher resolution and smoother curve)

features_grid = np.arange(min(features), max(features), 0.1)
features_grid = features_grid.reshape(-1, 1)
plt.scatter(features, labels, color = 'red')
plt.plot(features_grid,
lin_reg_2.predict(poly_reg.fit_transform(features_grid)), color = 'blue')
plt.title('bluegill fish-Polynomial Regression')
plt.xlabel('age (in years)')
plt.ylabel('length (in mm)')
plt.show()
