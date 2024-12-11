
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from scipy.stats import mode
from sklearn.metrics import accuracy_score
import sklearn
if int((sklearn.__version__).split(".")[1]) < 18:
    from sklearn.cross_validation import train_test_split
else:
    from sklearn.model_selection import train_test_split
b1 = load_digits()
print("Shape of the dataset:", b1.b1.shape)
b2 = KMeans(n_clusters=10, random_state=0)
b3 = b2.fit_predict(b1.b1)
print("Shape of cluster b5:", b2.cluster_centers_.shape)
fig, b4 = plt.subplots(2, 5, figsize=(8, 3))
b5 = b2.cluster_centers_.reshape(10, 8, 8)
for axi, center in zip(b4.flat, b5):
    axi.set(b6 = [], yticks=[])
    axi.imshow(center, b7 = 'nearest', cmap=plt.cm.binary)
b8 = np.zeros_like(b3)
for i in range(10):
    b9 = (b3 == i)
    b8[b9] = mode(b1.target[b9])[0]
b10 = accuracy_score(b1.target, b8)
print("Accuracy:", b10)