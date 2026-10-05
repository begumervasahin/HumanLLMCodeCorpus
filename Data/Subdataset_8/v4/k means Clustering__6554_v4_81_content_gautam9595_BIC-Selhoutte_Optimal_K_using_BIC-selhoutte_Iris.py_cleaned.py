import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy.spatial import distance
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
iris_data = load_iris()
def find_bic(kmeans_model, X):
    centers = [kmeans_model.cluster_centers_]
    labels = kmeans_model.labels_
    num_clusters = kmeans_model.n_clusters
    cluster_sizes = np.bincount(labels)
    num_samples, num_features = X.shape
    cluster_variance = (1.0 / (num_samples - num_clusters) / num_features) * \
                       sum([sum(distance.cdist(X[np.where(labels == i)], [centers[0][i]], 'euclidean') ** 2)
                            for i in range(num_clusters)])
    constant_term = 0.5 * num_clusters * np.log(num_samples) * (num_features + 1)
    bic = np.sum([cluster_sizes[i] * np.log(cluster_sizes[i]) - cluster_sizes[i] * np.log(num_samples) -
                  ((cluster_sizes[i] * num_features) / 2) * np.log(2 * np.pi * cluster_variance) -
                  ((cluster_sizes[i] - 1) * num_features / 2) for i in range(num_clusters)]) - constant_term
    return bic
bic_values = []
for i in range(2, int(math.sqrt(len(iris_data.data)))):
    kmeans_model = KMeans(n_clusters=i)
    labels = kmeans_model.fit_predict(iris_data.data)
    bic_values.append(find_bic(kmeans_model, iris_data.data) / silhouette_score(iris_data.data, labels))
plt.plot(range(2, int(math.sqrt(len(iris_data.data)))), bic_values)
plt.show()