import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.spatial import distance
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
b1 = load_iris()
def fonk1(b11, X):
    b2 = [b11.cluster_centers_]
    b3 = b11.labels_
    b4 = b11.n_clusters
    b5 = np.bincount(b3)
    num_samples, b6 = X.shape
    b7 = (1.0 / (num_samples - b4) / b6) * sum(
        [sum(distance.cdist(X[np.where(b3 = = i)], [b2[0][i]], 'euclidean') ** 2) for i in range(b4)]
    )
    b8 = 0.5 * b4 * np.log(num_samples) * (b6 + 1)
    b9 = np.sum(
        [
            b5[i] * np.log(b5[i]) - b5[i] * np.log(num_samples)
            - ((b5[i] * b6) / 2) * np.log(2 * np.pi * b7)
            - ((b5[i] - 1) * b6 / 2)
            for i in range(b4)
        ]
    ) - b8
    return b9
b10 = []
for b4 in range(2, int(math.sqrt(len(b1.data)))):
    b11 = KMeans(n_clusters=b4)
    b3 = b11.fit_predict(b1.data)
    b9 = fonk1(b11, b1.data)
    b12 = silhouette_score(b1.data, b3)
    b10.append(b9 / b12)
plt.plot(range(2, int(math.sqrt(len(b1.data)))), b10)
plt.xlabel('Number of Clusters')
plt.ylabel('BIC/Silhouette Ratio')
plt.title('BIC/Silhouette Ratio vs Number of Clusters')
plt.show()