from __future__ import print_function
import numpy as np
import sklearn
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
from scipy.stats import mode
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
fig, b7 = plt.subplots(2, 5, figsize=(8, 3))
b8 = b5.cluster_centers_.reshape(10, 8, 8)
for ax, center in zip(b7.flat, b8):
    ax.set(b9 = [], yticks=[])
    ax.imshow(center, b10 = 'nearest', cmap=plt.cm.binary)
plt.show()
b11 = np.zeros_like(b6)
for i in range(10):
    b12 = (b6 == i)
    b11[b12] = mode(b4[b12])[0]
b13 = accuracy_score(b4, b11)
print("Accuracy of clustering:", b13)