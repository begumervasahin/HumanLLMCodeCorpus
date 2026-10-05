import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy.spatial import distance
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
iris = load_iris()
def find_bic(kmeans, X):
    centers = [kmeans.cluster_centers_]
    labels = kmeans.labels_
    m = kmeans.n_clusters
    n = np.bincount(labels)
    N, d = X.shape
    cl_var = (1.0 / (N - m) / d) * sum([sum(distance.cdist(X[np.where(labels == i)], [centers[0][i]], 'euclidean') ** 2) for i in range(m)])
    const_term = 0.5 * m * np.log(N) * (d + 1)
    BIC = np.sum([n[i] * np.log(n[i]) - n[i] * np.log(N) - ((n[i] * d) / 2) * np.log(2 * np.pi * cl_var) - ((n[i] - 1) * d / 2) for i in range(m)]) - const_term
    return BIC
BIC_silhouette_ratio = []
for i in range(2, int(math.sqrt(len(iris.data)))):
    kms = KMeans(n_clusters=i)
    label = kms.fit_predict(iris.data)
    BIC = find_bic(kms, iris.data)
    silhouette_avg = silhouette_score(iris.data, label)
    BIC_silhouette_ratio.append(BIC / silhouette_avg)
plt.plot(range(2, int(math.sqrt(len(iris.data)))), BIC_silhouette_ratio)
plt.xlabel('Number of Clusters')
plt.ylabel('BIC/Silhouette Ratio')
plt.title('BIC/Silhouette Ratio vs Number of Clusters')
plt.show()