import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
colnames = ['area', 'perimeter', 'compactness', 'lengthOfKernel', 'widthOfKernel', 'asymmetryCoefficient', 'lengthOfKernelGrove', 'classifier']
data = pd.read_csv("seeds_dataset.txt", delimiter='\s+', names=colnames)
X = data.drop('classifier', axis=1)
y = data['classifier']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
cluster_range = range(1, 7)
cluster_errors = []
for num_clusters in cluster_range:
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(X_pca)
    cluster_errors.append(kmeans.inertia_)
plt.figure(figsize=(12, 6))
plt.plot(cluster_range, cluster_errors, marker="o")
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('Within-cluster Sum of Squares')
plt.grid(True)
plt.show()