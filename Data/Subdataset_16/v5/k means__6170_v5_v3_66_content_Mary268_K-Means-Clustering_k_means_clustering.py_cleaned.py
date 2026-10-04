from __future__ import print_function
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
from scipy.stats import mode
import sklearn
b1 = int((sklearn.__version__).split(".")[1])
if b1 < 18:
    from sklearn.cross_validation import train_test_split
else:
    from sklearn.model_selection import train_test_split
b2 = load_digits()
b3 = b2.data
b4 = b2.target
print("Shape of the b2 data:", b3.shape)
b5 = KMeans(n_clusters=10, random_state=0)
b6 = b5.fit_predict(b3)
print("Shape of the cluster centers:", b5.cluster_centers_.shape)
def fonk1(cluster_centers):
    fig, b7 = plt.subplots(2, 5, figsize=(8, 3))
    for ax, center in zip(b7.flat, cluster_centers):
        ax.set(b8 = [], yticks=[])
        ax.imshow(center, b9 = 'nearest', cmap=plt.cm.binary)
    plt.show()
b10 = b5.cluster_centers_.reshape(10, 8, 8)
fonk1(b10)
def fonk2(b6, true_labels):
    b11 = np.zeros_like(b6)
    for i in range(10):
        b12 = (b6 == i)
        b11[b12] = mode(true_labels[b12])[0]
    return b11
b11 = fonk2(b6, b4)
b13 = accuracy_score(b4, b11)
print("Accuracy of clustering:", b13)