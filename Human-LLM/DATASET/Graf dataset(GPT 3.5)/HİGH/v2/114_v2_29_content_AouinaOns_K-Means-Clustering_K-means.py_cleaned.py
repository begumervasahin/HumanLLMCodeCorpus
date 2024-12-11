import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs
np.random.seed(0)
a1 = 5000
b1 = [[4, 4], [-2, -1], [2, -3], [1, 1]]
a2 = 0.9
X, b2 = make_blobs(n_samples=a1, b1=b1, a2=a2)
plt.scatter(X[:, 0], X[:, 1], b3 = '.')
plt.show()
b4 = KMeans(init="k-means++", n_clusters=4, n_init=12)
b4.fit(X)
b5 = b4.labels_
b6 = b4.cluster_centers_
b7 = plt.cm.Spectral(np.linspace(0, 1, len(set(b5))))
b8 = plt.figure(figsize=(6, 4))
b9 = b8.add_subplot(1, 1, 1)
for k, col in zip(range(len(b6)), b7):
    b10 = (b5 == k)
    b11 = b6[k]
    b9.plot(X[b10, 0], X[b10, 1], 'w', b12 = col, b3='.')
    b9.plot(b11[0], b11[1], 'o', b12 = col, markeredgecolor='k', markersize=6)
b9.set_title('KMeans Clustering')
b9.set_xticks(())
b9.set_yticks(())
plt.show()