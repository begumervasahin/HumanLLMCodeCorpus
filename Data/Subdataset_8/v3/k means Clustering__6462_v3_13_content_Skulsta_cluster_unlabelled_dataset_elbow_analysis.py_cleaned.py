
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
COLUMN_NAMES = [
    'area', 'perimeter', 'compactness', 'lengthOfKernel', 'widthOfKernel',
    'asymmetryCoefficient', 'lengthOfKernelGrove', 'classifier'
]
def load_dataset(file_path, column_names):
    return pd.read_csv(file_path, delimiter='\s+', names=column_names)
def preprocess_data(data):
    X = data.drop('classifier', axis=1)
    y = data['classifier']
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled
def reduce_dimensions(X):
    pca = PCA(n_components=2)
    return pca.fit_transform(X)
def find_optimal_clusters(X, max_clusters=6):
    cluster_errors = []
    for num_clusters in range(1, max_clusters + 1):
        kmeans = KMeans(n_clusters=num_clusters)
        kmeans.fit(X)
        cluster_errors.append(kmeans.inertia_)
    return cluster_errors
def plot_elbow_method(cluster_range, cluster_errors):
    plt.figure(figsize=(12, 6))
    plt.plot(cluster_range, cluster_errors, marker="o")
    plt.title('Elbow Method')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Within-cluster Sum of Squares')
    plt.grid(True)
    plt.show()
dataset = load_dataset("seeds_dataset.txt", COLUMN_NAMES)
X_scaled = preprocess_data(dataset)
X_pca = reduce_dimensions(X_scaled)
cluster_errors = find_optimal_clusters(X_pca)
plot_elbow_method(range(1, 7), cluster_errors)