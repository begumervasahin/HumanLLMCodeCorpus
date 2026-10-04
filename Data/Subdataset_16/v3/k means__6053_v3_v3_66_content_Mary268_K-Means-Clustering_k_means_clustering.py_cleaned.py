
from __future__ import print_function
import numpy as np
import sklearn
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
from scipy.stats import mode
if int((sklearn.__version__).split(".")[1]) < 18:
    from sklearn.cross_validation import train_test_split
else:
    from sklearn.model_selection import train_test_split
b1 = load_digits()
data, b2 = b1.data, b1.b2
print("Shape of the digits data:", data.shape)
b3 = KMeans(n_clusters=10, random_state=0)
b4 = b3.fit_predict(data)
print("Shape of the cluster centers:", b3.cluster_centers_.shape)
fig, b5 = plt.subplots(2, 5, figsize=(8, 3))
b6 = b3.cluster_centers_.reshape(10, 8, 8)
for ax, center in zip(b5.flat, b6):
    ax.set(b7 = [], yticks=[])
    ax.imshow(center, b8 = 'nearest', cmap=plt.cm.binary)
plt.show()
b9 = np.zeros_like(b4)
for i in range(10):
    b10 = (b4 == i)
    b9[b10] = mode(b2[b10])[0]
b11 = accuracy_score(b2, b9)
print("Accuracy of clustering:", b11)