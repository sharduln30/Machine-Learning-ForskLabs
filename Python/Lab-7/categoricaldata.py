# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 17:44:06 2018

@author: Shardul Negi
"""

import pandas as pd
# Importing the dataset


data= pd.read_csv("Automobile.csv")

data.select_dtypes(include=['object'])

x=data.iloc[:,0:2].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder, Imputer
labelencoder = LabelEncoder()


data["normalized_losses"] = data["normalized_losses"].fillna(data["normalized_losses"].median())
imputer= Imputer(missing_values='NaN', strategy='median', axis=0)
imputer=imputer.fit(x[:, 1:2])
x[:,1:2]=imputer.transform(x[:,1:2])

print data["normalized_losses"]

#drive_wheels
pd.get_dummies(data, columns=["drive_wheels"]).head()

#body_style
lb_make = LabelEncoder()
data["body_style_code"] = lb_make.fit_transform(data["body_style"])
data[["body_style", "body_style_code"]].head(11)

