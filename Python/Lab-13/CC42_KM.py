# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 17:14:28 2018

@author: Shardul Negi
"""

# K-Means Clustering

# Importing the libraries
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('deliveryfleet.csv')
features = dataset.iloc[:, 1:].values

# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
 kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
 kmeans.fit(features)
 wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 0)
y_kmeans = kmeans.fit_predict(features)

# Visualising the clusters
plt.scatter(features[y_kmeans == 0, 0], features[y_kmeans == 0, 1], s = 100, c =
'orange', label = 'Cluster 1')
plt.scatter(features[y_kmeans == 1, 0], features[y_kmeans == 1, 1], s = 100, c =
'green', label = 'Cluster 2')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s =
100, c = 'blue', label = 'Centroids')
plt.scatter(features[y_kmeans == 2, 0], features[y_kmeans == 2, 1], s = 100, c =
'red', label = 'Cluster 3')
plt.scatter(features[y_kmeans == 3, 0], features[y_kmeans == 3, 1], s = 100, c =
'cyan', label = 'Cluster 4')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s =
100, c = 'blue', label = 'Centroids')

plt.title('Clusters of Drivers')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()
