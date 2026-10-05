import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from scipy.spatial import distance
b1 = load_iris()
def fonk1(b10, X):
    b2 = b10.cluster_centers_
    b3 = b10.labels_
    b4 = np.bincount(b3)
    num_samples, b5 = X.shape
    b6 = sum(
        [
            sum(distance.cdist(X[np.where(b3 = = i)], [b2[i]], 'euclidean') ** 2)
            for i in range(b10.n_clusters)
        ]
    ) / (num_samples - b10.n_clusters) / b5
    b7 = 0.5 * b10.n_clusters * np.log(num_samples) * (b5 + 1)
    b8 = np.sum(
        [
            b4[i] * np.log(b4[i]) - b4[i] * np.log(num_samples)
            - (b4[i] * b5 / 2) * np.log(2 * np.pi * b6)
            - ((b4[i] - 1) * b5 / 2)
            for i in range(b10.n_clusters)
        ]
    ) - b7
    return b8
b9 = []
for num_clusters in range(2, int(np.sqrt(len(b1.data)))):
    b10 = KMeans(n_clusters=num_clusters)
    b3 = b10.fit_predict(b1.data)
    b8 = fonk1(b10, b1.data)
    b11 = silhouette_score(b1.data, b3)
    b9.append(b8 / b11)
plt.plot(range(2, int(np.sqrt(len(b1.data)))) , b9)
plt.xlabel('Number of Clusters')
plt.ylabel('BIC/Silhouette Ratio')
plt.title('BIC/Silhouette Ratio vs Number of Clusters')
plt.show()