import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from scipy.spatial import distance
iris = load_iris()
def calculate_bic(kmeans, X):
    centers = kmeans.cluster_centers_
    labels = kmeans.labels_
    cluster_sizes = np.bincount(labels)
    num_samples, num_features = X.shape
    cluster_variance = sum(
        [
            sum(distance.cdist(X[np.where(labels == i)], [centers[i]], 'euclidean') ** 2)
            for i in range(kmeans.n_clusters)
        ]
    ) / (num_samples - kmeans.n_clusters) / num_features
    constant_term = 0.5 * kmeans.n_clusters * np.log(num_samples) * (num_features + 1)
    bic = np.sum(
        [
            cluster_sizes[i] * np.log(cluster_sizes[i]) - cluster_sizes[i] * np.log(num_samples)
            - (cluster_sizes[i] * num_features / 2) * np.log(2 * np.pi * cluster_variance)
            - ((cluster_sizes[i] - 1) * num_features / 2)
            for i in range(kmeans.n_clusters)
        ]
    ) - constant_term
    return bic
bic_silhouette_ratio = []
for num_clusters in range(2, int(np.sqrt(len(iris.data)))):
    kmeans = KMeans(n_clusters=num_clusters)
    labels = kmeans.fit_predict(iris.data)
    bic = calculate_bic(kmeans, iris.data)
    silhouette_avg = silhouette_score(iris.data, labels)
    bic_silhouette_ratio.append(bic / silhouette_avg)
plt.plot(range(2, int(np.sqrt(len(iris.data)))) , bic_silhouette_ratio)
plt.xlabel('Number of Clusters')
plt.ylabel('BIC/Silhouette Ratio')
plt.title('BIC/Silhouette Ratio vs Number of Clusters')
plt.show()