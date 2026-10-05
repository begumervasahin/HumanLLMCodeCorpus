from __future__ import print_function
from sklearn.cluster import KMeans
from sklearn.metrics import classification_report
from sklearn.datasets import load_digits
from matplotlib import pyplot as plt
from scipy.stats import mode
from sklearn.metrics import accuracy_score
import numpy as np
import sklearn
if int((sklearn.__version__).split(".")[1]) < 18:
    from sklearn.cross_validation import train_test_split
else:
    from sklearn.model_selection import train_test_split
data = load_digits()
print(data.data.shape)
kmeans = KMeans(n_clusters=10, random_state=0)
clusters = kmeans.fit_predict(data.data)
print(kmeans.cluster_centers_.shape)
fig, ax = plt.subplots(2, 5, figsize=(8, 3))
centers = kmeans.cluster_centers_.reshape(10, 8, 8)
for axi, center in zip(ax.flat, centers):
    axi.set(xticks=[], yticks=[])
    axi.imshow(center, interpolation='nearest', cmap=plt.cm.binary)
labels = np.zeros_like(clusters)
for i in range(10):
    mask = (clusters == i)
    labels[mask] = mode(data.target[mask])[0]
print("Accuracy:", accuracy_score(data.target, labels))