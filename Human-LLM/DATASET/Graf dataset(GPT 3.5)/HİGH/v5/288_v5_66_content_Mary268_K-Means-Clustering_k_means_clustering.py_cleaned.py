
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
def fonk1():
    if int((sklearn.__version__).split(".")[1]) < 18:
        from sklearn.cross_validation import train_test_split
    else:
        from sklearn.model_selection import train_test_split
def fonk2():
    return load_digits()
def fonk3(b8):
    fig, b1 = plt.subplots(2, 5, figsize=(8, 3))
    b2 = b8.cluster_centers_.reshape(10, 8, 8)
    for axi, center in zip(b1.flat, b2):
        axi.set(b3 = [], yticks=[])
        axi.imshow(center, b4 = 'nearest', cmap=plt.cm.binary)
def fonk4(b9, target):
    b5 = np.zeros_like(b9)
    for i in range(10):
        b6 = (b9 == i)
        b5[b6] = mode(target[b6])[0]
    return b5
def fonk5(true_labels, predicted_labels):
    return accuracy_score(true_labels, predicted_labels)
def fonk6():
    b7 = fonk2()
    print("Shape of the dataset:", b7.b7.shape)
    b8 = KMeans(n_clusters=10, random_state=0)
    b9 = b8.fit_predict(b7.b7)
    print("Shape of cluster b2:", b8.cluster_centers_.shape)
    fonk3(b8)
    b5 = fonk4(b9, b7.target)
    b10 = fonk5(b7.target, b5)
    print("Accuracy:", b10)
if b11 = = "__main__":
    fonk6()