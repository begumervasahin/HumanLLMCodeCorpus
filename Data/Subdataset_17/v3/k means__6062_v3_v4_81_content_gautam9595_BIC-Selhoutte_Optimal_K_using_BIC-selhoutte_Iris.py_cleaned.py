import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.spatial import distance
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
iris_data = load_iris()
X = iris_data.data
def calculate_bic(kmeans_model, X):
    labels = kmeans_model.labels_
    num_clusters = kmeans_model.n_clusters
    num_samples, num_features = X.shape
    cluster_sizes = np.bincount(labels)
    centers = kmeans_model.cluster_centers_
    cluster_variance = (1.0 / (num_samples - num_clusters) / num_features) * \
                       sum(sum(distance.cdist(X[labels == i], [centers[i]], 'euclidean')**2) for i in range(num_clusters))
    constant_term = 0.5 * num_clusters * np.log(num_samples) * (num_features + 1)
    bic = np.sum([
        cluster_sizes[i] * np.log(cluster_sizes[i]) - cluster_sizes[i] * np.log(num_samples) -
        ((cluster_sizes[i] * num_features) / 2) * np.log(2 * np.pi * cluster_variance) -
        ((cluster_sizes[i] - 1) * num_features / 2)
        for i in range(num_clusters)
    ]) - constant_term
    return bic
def evaluate_clusters(X, max_clusters):
    bic_values = []
    for n_clusters in range(2, max_clusters + 1):
        kmeans_model = KMeans(n_clusters=n_clusters, random_state=42)
        kmeans_model.fit(X)
        bic = calculate_bic(kmeans_model, X)
        silhouette_avg = silhouette_score(X, kmeans_model.labels_)
        normalized_bic = bic / silhouette_avg
        bic_values.append(normalized_bic)
    return bic_values
max_clusters = int(math.sqrt(len(X)))
bic_values = evaluate_clusters(X, max_clusters)
plt.figure(figsize=(10, 6))
plt.plot(range(2, max_clusters + 1), bic_values, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('Normalized BIC')
plt.title('Normalized BIC vs Number of Clusters')
plt.grid(True)
plt.show()