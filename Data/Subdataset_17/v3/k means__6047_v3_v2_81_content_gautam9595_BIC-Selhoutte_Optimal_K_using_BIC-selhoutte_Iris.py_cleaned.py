import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.spatial import distance
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
iris = load_iris()
X = iris.data
def calculate_bic(kmeans, X):
    centers = kmeans.cluster_centers_
    labels = kmeans.labels_
    num_clusters = kmeans.n_clusters
    cluster_sizes = np.bincount(labels)
    num_samples, num_features = X.shape
    cluster_variance = (1.0 / (num_samples - num_clusters) / num_features) * sum(
        [sum(distance.cdist(X[labels == i], [centers[i]], 'euclidean') ** 2) for i in range(num_clusters)]
    )
    constant_term = 0.5 * num_clusters * np.log(num_samples) * (num_features + 1)
    bic = np.sum(
        [
            cluster_sizes[i] * np.log(cluster_sizes[i]) - cluster_sizes[i] * np.log(num_samples)
            - ((cluster_sizes[i] * num_features) / 2) * np.log(2 * np.pi * cluster_variance)
            - ((cluster_sizes[i] - 1) * num_features / 2)
            for i in range(num_clusters)
        ]
    ) - constant_term
    return bic
def compute_bic_silhouette_ratios(X, max_clusters):
    bic_silhouette_ratios = []
    for num_clusters in range(2, max_clusters + 1):
        kmeans = KMeans(n_clusters=num_clusters, random_state=42)
        labels = kmeans.fit_predict(X)
        bic = calculate_bic(kmeans, X)
        silhouette_avg = silhouette_score(X, labels)
        bic_silhouette_ratios.append(bic / silhouette_avg)
    return bic_silhouette_ratios
def plot_bic_silhouette_ratios(ratios, max_clusters):
    plt.figure(figsize=(10, 6))
    plt.plot(range(2, max_clusters + 1), ratios, marker='o')
    plt.xlabel('Number of Clusters')
    plt.ylabel('BIC/Silhouette Ratio')
    plt.title('BIC/Silhouette Ratio vs Number of Clusters')
    plt.grid(True)
    plt.show()
max_clusters = int(math.sqrt(len(X)))
bic_silhouette_ratios = compute_bic_silhouette_ratios(X, max_clusters)
plot_bic_silhouette_ratios(bic_silhouette_ratios, max_clusters)