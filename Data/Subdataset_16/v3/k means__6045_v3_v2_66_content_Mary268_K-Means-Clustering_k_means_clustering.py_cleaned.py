
from __future__ import print_function
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
from scipy.stats import mode
b1 = load_digits()
b2 = b1.b2
b3 = b1.target
print("Shape of the b1 b2:", b2.shape)
b4 = KMeans(n_clusters=10, random_state=0)
b5 = b4.fit_predict(b2)
print("Shape of the cluster centers:", b4.cluster_centers_.shape)
def fonk1(cluster_centers):
    fig, b6 = plt.subplots(2, 5, figsize=(8, 3))
    b7 = cluster_centers.reshape(10, 8, 8)
    for ax, center in zip(b6.flat, b7):
        ax.set(b8 = [], yticks=[])
        ax.imshow(center, b9 = 'nearest', cmap=plt.cm.binary)
    plt.show()
fonk1(b4.cluster_centers_)
def fonk2(b5, true_labels, n_clusters):
    b10 = np.zeros_like(b5)
    for i in range(n_clusters):
        b11 = (b5 == i)
        b10[b11] = mode(true_labels[b11])[0]
    return b10
b10 = fonk2(b5, b3, 10)
b12 = accuracy_score(b3, b10)
print("Accuracy of clustering:", b12)