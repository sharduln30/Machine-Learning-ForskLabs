# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 18:05:09 2018

@author: Shardul Negi
"""

# Logistic Regression
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('affairs.csv')
features = dataset.iloc[:,0:8].values
labels = dataset.iloc[:, 8].values


from sklearn.preprocessing import OneHotEncoder
     
onehotencoder = OneHotEncoder(categorical_features=[6])
features = onehotencoder.fit_transform(features).toarray() 
features = features[:,1:]  
onehotencoder = OneHotEncoder(categorical_features=[7])
features = onehotencoder.fit_transform(features).toarray()
features = features[:,1:]


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split 
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)

# Feature Scaling
#from sklearn.preprocessing import StandardScaler
#sc = StandardScaler()
#features_train = sc.fit_transform(features_train)
#features_test = sc.transform(features_test)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
