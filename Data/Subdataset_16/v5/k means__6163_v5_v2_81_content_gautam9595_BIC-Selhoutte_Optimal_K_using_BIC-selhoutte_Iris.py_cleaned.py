import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.spatial import distance
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
b1 = load_iris()
b2 = b1.b2
def fonk1(b11, X):
    b3 = b11.cluster_centers_
    b4 = b11.labels_
    b5 = b11.n_clusters
    num_samples, b6 = X.shape
    b7 = (
        1.0 / (num_samples - b5) / b6
    ) * sum(
        [
            np.sum(distance.cdist(X[b4 = = i], [b3[i]], "euclidean") ** 2)
            for i in range(b5)
        ]
    )
    b8 = 0.5 * b5 * np.log(num_samples) * (b6 + 1)
    b9 = (
        np.sum(
            [
                np.sum(b4 = = i) * np.log(np.sum(b4 == i))
                - np.sum(b4 = = i) * np.log(num_samples)
                - ((np.sum(b4 = = i) * b6) / 2) * np.log(
                    2 * np.pi * b7
                )
                - ((np.sum(b4 = = i) - 1) * b6 / 2)
                for i in range(b5)
            ]
        )
        - b8
    )
    return b9
def fonk2(b2, b13):
    b10 = []
    for b5 in b13:
        b11 = KMeans(n_clusters=b5, random_state=42)
        b4 = b11.fit_predict(b2)
        b9 = fonk1(b11, b2)
        b12 = silhouette_score(b2, b4)
        b10.append(b9 / b12)
    return b10
b13 = range(2, int(math.sqrt(len(b2))) + 1)
b10 = fonk2(b2, b13)
plt.figure(b14 = (10, 6))
plt.plot(b13, b10, b15 = "o")
plt.xlabel("Number of Clusters")
plt.ylabel("BIC/Silhouette Ratio")
plt.title("BIC/Silhouette Ratio vs Number of Clusters")
plt.grid(True)
plt.show()