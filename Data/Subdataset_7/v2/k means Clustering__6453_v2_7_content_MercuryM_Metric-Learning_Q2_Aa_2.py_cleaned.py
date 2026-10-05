import numpy as np
import time
from sklearn.cluster import KMeans
from scipy.optimize import linear_sum_assignment
import matplotlib.pyplot as plt
def fonk1(a, b):
    return np.linalg.norm(a - b)
def fonk2(record, b22):
    b1 = len(record)
    b2 = np.zeros((b1, b1))
    for i in range(b1):
        b3 = record[i]
        for j in range(len(b3)):
            b4 = b3[j]
            b5 = b22[0, b4]
            b2[i, :] += 1
            b2[i, b5 - 1] -= 1
    return b2
def fonk3(b1, a1, a2, test_data, b22):
    b6 = []
    b7 = []
    np.random.seed(a2)
    for i in range(a1):
        b8 = np.random.randint(0, 1000)
        b20, b9 = fonk5(b1, b8, test_data)
        b2 = fonk2(b20, b22)
        row_ind, b10 = linear_sum_assignment(b2)
        b11 = b2[row_ind, b10].sum()
        b12 = fonk4(b1, b11)
        b7.append(b9)
        b6.append(b12)
    b13 = np.mean(b7)
    b14 = np.mean(b6)
    return b14, b13
def fonk4(b1, b11):
    return (10 * b1 - b11) / (10 * b1)
def fonk5(b1, b8, test_data):
    b15 = test_data.T
    b16 = time.time()
    b17 = KMeans(n_clusters=b1, b8=b8).fit(b15)
    b18 = time.time()
    b19 = b17.labels_
    b20 = []
    for i in range(b1):
        b3 = [j for j, label in enumerate(b19) if label == i]
        b20.append(b3)
    return b20, b18 - b16
def fonk6():
    pass
b21 = fonk6()
b26, b22 = b21['train']
num_train_samples, b23 = b26.shape
b27, b24 = b21['test']
num_test_samples, b25 = b27.shape
b26 = b26 / np.apply_along_axis(np.linalg.norm, 0, b26)
b27 = b27 / np.apply_along_axis(np.linalg.norm, 0, b27)
b1 = 32
a1 = 1
a2 = 10
b12, b13 = fonk3(b1, a1, a2, b26, b22)
print("Average Accuracy:", b12)
print("Average Time:", b13)