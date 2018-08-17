# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 18:39:04 2018

@author: MUJ
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('affairs.csv')
X = dataset.iloc[:,:8].values
Y = dataset.iloc[:,-1].values

from sklearn.preprocessing import OneHotEncoder                
onehotencoder1 = OneHotEncoder(categorical_features = [6])  
X = onehotencoder1.fit_transform(X).toarray()
X = X[:,1:]
onehotencoder2 = OneHotEncoder(categorical_features = [11])
X = onehotencoder2.fit_transform(X).toarray()
X = X[:,1:]

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test =train_test_split(X,Y, test_size = 0.25, random_state = 0)


from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, Y_train)
Y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, Y_pred)

y_ans= classifier.predict(np.array([1,0,0,0,0,0,0,1,0,0,3,25,3,1,4,16]).reshape(1,-1))
y_ans= classifier.predict_proba(np.array([1,0,0,0,0,0,0,1,0,0,3,25,3,1,4,16]).reshape(1,-1))

model_score = classifier.score(X_test,Y_test)

no_of_affairs=Y.mean()