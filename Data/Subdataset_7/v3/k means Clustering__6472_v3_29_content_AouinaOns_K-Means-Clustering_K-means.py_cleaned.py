import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
np.random.seed(0)
a1 = 5000
b1 = [[4, 4], [-2, -1], [2, -3], [1, 1]]
a2 = 0.9
X, b2 = make_blobs(n_samples=a1, b1=b1, a2=a2)
plt.scatter(X[:, 0], X[:, 1], b3 = '.')
plt.show()
b4 = KMeans(n_clusters=4, init="k-means++", n_init=12)
b4.fit(X)
b5 = b4.labels_
b6 = b4.cluster_centers_
b7 = plt.cm.Spectral(np.linspace(0, 1, len(b6)))
fig, b8 = plt.subplots(figsize=(6, 4))
for k, col in zip(range(len(b6)), b7):
    b9 = (b5 == k)
    b10 = b6[k]
    b8.plot(X[b9, 0], X[b9, 1], 'w', b11 = col, b3='.')
    b8.plot(b10[0], b10[1], 'o', b11 = col, markeredgecolor='k', markersize=6)
b8.set_title('KMeans Clustering')
b8.set_xticks(())
b8.set_yticks(())
plt.show()