
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
column_names = [
    'area', 'perimeter', 'compactness', 'lengthOfKernel', 'widthOfKernel',
    'asymmetryCoefficient', 'lengthOfKernelGrove', 'classifier'
]
dataset = pd.read_csv("seeds_dataset.txt", delimiter='\s+', names=column_names)
features = dataset.drop('classifier', axis=1)
target = dataset['classifier']
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)
pca = PCA(n_components=2)
reduced_features = pca.fit_transform(scaled_features)
cluster_range = range(1, 7)
cluster_errors = []
for num_clusters in cluster_range:
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(reduced_features)
    cluster_errors.append(kmeans.inertia_)
plt.figure(figsize=(12, 6))
plt.plot(cluster_range, cluster_errors, marker="o")
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('Within-cluster Sum of Squares')
plt.grid(True)
plt.show()