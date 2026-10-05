import numpy as np
import time
from sklearn.cluster import KMeans
from scipy.optimize import linear_sum_assignment
import matplotlib.pyplot as plt
def fonk1(a, b):
    return np.linalg.norm(a - b)
def fonk2(b18, b20):
    b1 = len(b18)
    b2 = np.zeros((b1, b1))
    for i, cluster_indices in enumerate(b18):
        for index in cluster_indices:
            b3 = b20[0, index]
            b2[i, :] += 1
            b2[i, b3 - 1] -= 1
    return b2
def fonk3(b1, a1, a2, test_data, b20):
    b4 = []
    b5 = []
    np.random.seed(a2)
    for _ in range(a1):
        b6 = np.random.randint(0, 1000)
        b18, b7 = fonk5(b1, b6, test_data)
        b2 = fonk2(b18, b20)
        row_ind, b8 = linear_sum_assignment(b2)
        b9 = b2[row_ind, b8].sum()
        b10 = fonk4(b1, b9)
        b5.append(b7)
        b4.append(b10)
    b11 = np.mean(b5)
    b12 = np.mean(b4)
    return b12, b11
def fonk4(b1, b9):
    return (10 * b1 - b9) / (10 * b1)
def fonk5(b1, b6, test_data):
    b13 = test_data.T
    b14 = time.time()
    b15 = KMeans(n_clusters=b1, b6=b6).fit(b13)
    b16 = time.time()
    b17 = b15.labels_
    b18 = [[] for _ in range(b1)]
    for index, label in enumerate(b17):
        b18[label].append(index)
    return b18, b16 - b14
def fonk6():
    pass
b19 = fonk6()
b24, b20 = b19['train']
num_train_samples, b21 = b24.shape
b25, b22 = b19['test']
num_test_samples, b23 = b25.shape
b24 = b24 / np.apply_along_axis(np.linalg.norm, 0, b24)
b25 = b25 / np.apply_along_axis(np.linalg.norm, 0, b25)
b1 = 32
a1 = 1
a2 = 10
b10, b11 = fonk3(b1, a1, a2, b24, b20)
print("Average Accuracy:", b10)
print("Average Time:", b11)