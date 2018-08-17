# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 19:05:44 2018

@author: Shardul Negi
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 17:44:06 2018

@author: Shardul Negi
"""

import pandas as pd

data=pd.read_csv("Automobile.csv")

for col in data.columns:
    data[col] = data[col].fillna(data[col].mode()[0])

for col in data.columns:
    print 'column', col,':', type(data[col][0])

data["body_style"] = data["body_style"].astype('category')
data["body_style"] = data["body_style"].cat.codes

df = data.select_dtypes(include=['object'])

features=data.iloc[:,:-1].values
labels=data.iloc[:,-1].values

data = pd.get_dummies(data,columns=['drive_wheels'])


from sklearn.preprocessing import LabelEncoder, OneHotEncoder
for i in [2,3,4,5,6,7,8,14,15,17]:
    labelencoder=LabelEncoder()
    features[:,i]=labelencoder.fit_transform(features[:,i])

view = pd.DataFrame(features)
 
    
onehotencoder = OneHotEncoder(categorical_features=[6])
features = onehotencoder.fit_transform(features).toarray()





