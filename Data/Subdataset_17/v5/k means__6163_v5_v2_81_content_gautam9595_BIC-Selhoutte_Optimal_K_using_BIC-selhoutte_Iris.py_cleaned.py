import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.spatial import distance
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
iris = load_iris()
data = iris.data
def calculate_bic(kmeans, X):
    centers = kmeans.cluster_centers_
    labels = kmeans.labels_
    num_clusters = kmeans.n_clusters
    num_samples, num_features = X.shape
    cluster_variance = (
        1.0 / (num_samples - num_clusters) / num_features
    ) * sum(
        [
            np.sum(distance.cdist(X[labels == i], [centers[i]], "euclidean") ** 2)
            for i in range(num_clusters)
        ]
    )
    constant_term = 0.5 * num_clusters * np.log(num_samples) * (num_features + 1)
    bic = (
        np.sum(
            [
                np.sum(labels == i) * np.log(np.sum(labels == i))
                - np.sum(labels == i) * np.log(num_samples)
                - ((np.sum(labels == i) * num_features) / 2) * np.log(
                    2 * np.pi * cluster_variance
                )
                - ((np.sum(labels == i) - 1) * num_features / 2)
                for i in range(num_clusters)
            ]
        )
        - constant_term
    )
    return bic
def calculate_bic_silhouette_ratios(data, cluster_range):
    bic_silhouette_ratios = []
    for num_clusters in cluster_range:
        kmeans = KMeans(n_clusters=num_clusters, random_state=42)
        labels = kmeans.fit_predict(data)
        bic = calculate_bic(kmeans, data)
        silhouette_avg = silhouette_score(data, labels)
        bic_silhouette_ratios.append(bic / silhouette_avg)
    return bic_silhouette_ratios
cluster_range = range(2, int(math.sqrt(len(data))) + 1)
bic_silhouette_ratios = calculate_bic_silhouette_ratios(data, cluster_range)
plt.figure(figsize=(10, 6))
plt.plot(cluster_range, bic_silhouette_ratios, marker="o")
plt.xlabel("Number of Clusters")
plt.ylabel("BIC/Silhouette Ratio")
plt.title("BIC/Silhouette Ratio vs Number of Clusters")
plt.grid(True)
plt.show()