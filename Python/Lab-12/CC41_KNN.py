# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 17:58:35 2018

@author: Shardul Negi
"""

# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing the dataset
data = pd.read_csv("mushrooms.csv")
features = data.iloc[:, [5, 21, 22]].values
labels = data.iloc[:, 0].values

# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
features[:,0] = labelencoder.fit_transform(features[:,0])
features[:,1] = labelencoder.fit_transform(features[:,1])
features[:,2] = labelencoder.fit_transform(features[:,2])

# OneHotEncoding the labelled data
onehotencoder = OneHotEncoder(categorical_features=[0])
features = onehotencoder.fit_transform(features).toarray()

features = features[:,1:]

onehotencoder = OneHotEncoder(categorical_features=[8])
features = onehotencoder.fit_transform(features).toarray()

features = features[:,[0,1,2,3,4,5,6,7,8,9,10,11,12,14]]

# Encoding the Dependent Variable
labels = labelencoder.fit_transform(labels)

onehotencoder = OneHotEncoder(categorical_features=[13])
features = onehotencoder.fit_transform(features).toarray()

features = features[:,0:19]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.25,random_state=0)




# Fitting K-NN to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5,p=2)
classifier.fit(features_train, labels_train)


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, classifier.predict(features_test))

# Getting Model Score
Score = classifier.score(features_test, labels_test)


