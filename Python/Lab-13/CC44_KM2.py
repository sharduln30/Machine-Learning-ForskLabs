# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 19:10:18 2018

@author: Shardul Negi
"""

import matplotlib.pyplot as plt
import pandas as pd
# Importing the dataset
dataset = pd.read_csv('tshirts.csv')
features = dataset.iloc[:, 1:4].values
# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans

# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters =3 , init = 'k-means++',random_state = 0)
y_kmeans = kmeans.fit_predict(features)
# Visualising the clusters
plt.scatter(features[y_kmeans == 0, 0], features[y_kmeans== 0, 1], s = 100, c = 'orange', label = 'Cluster 1')
plt.scatter(features[y_kmeans == 1, 0], features[y_kmeans== 1, 1], s = 100, c = 'red', label = 'Cluster 2')
plt.scatter(features[y_kmeans == 2, 0], features[y_kmeans== 2, 1], s = 100, c = 'green', label = 'Cluster 3')


plt.scatter(kmeans.cluster_centers_[:, 0],
kmeans.cluster_centers_[:, 1], s = 100, c = 'blue',label = 'Centroids')
plt.title('Clusters of TShirts')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()