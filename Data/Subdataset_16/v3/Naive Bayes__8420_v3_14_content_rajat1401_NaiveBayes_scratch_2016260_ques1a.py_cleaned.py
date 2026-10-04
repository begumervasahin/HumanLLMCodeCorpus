import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import pickle
from mlxtend.data import loadlocal_mnist
X_train, b1 = loadlocal_mnist(images_path='./train-images.idx3-ubyte', labels_path='./train-labels.idx1-ubyte')
X_test, b2 = loadlocal_mnist(images_path='./t10k-images.idx3-ubyte', labels_path='./t10k-labels.idx1-ubyte')
b1 = [label - 1 for label in b1 if label in [1, 2]]
b2 = [label - 1 for label in b2 if label in [1, 2]]
with open('./bintrain.pkl', 'rb') as f:
    b3 = pickle.load(f)
with open('./bintest.pkl', 'rb') as f:
    b4 = pickle.load(f)
b5 = np.load('./b5.mat')
b6 = np.load('./b6.mat')
b7 = b1.count(0)
b8 = b1.count(1)
b9 = b7 / (b7 + b8)
b10 = b8 / (b7 + b8)
b5[:, 0] /= b7
b6[:, 0] /= b7
b5[:, 1] /= b8
b6[:, 1] /= b8
print(f"The prior for trouser is: {b9}")
print(f"The prior for pullover is: {b10}")
b11 = [0.3, 0.4, 0.5, 0.6, 0.7]
b12 = np.zeros((len(b11), len(b4)))
def fonk1(x, count0, count1):
    a1 = 0
    a2 = 0
    for j in range(len(x)):
        if x[j] == 1:
            a1 += math.log(count1[j][0])
            a2 += math.log(count1[j][1])
        else:
            a1 += math.log(count0[j][0])
            a2 += math.log(count0[j][1])
    return a1, a2
for k, threshold in enumerate(b11):
    for i in range(len(b4)):
        a1, a2 = fonk1(b4[i], b5, b6)
        b13 = (a1 * b9) / (a1 * b9 + a2 * b10)
        b12[k][i] = 0 if b13 <= threshold else 1
print(f"Prediction lengths: {len(b12)}, {len(b2)}")
print(b12[:, 0], b12[:, 1])
b14 = []
b15 = []
def fonk2(y_true, b12):
    b16 = fp = fn = b18 = 0
    for i in range(len(y_true)):
        if b12[i] == 0 and y_true[i] == 0:
            b16 += 1
        elif b12[i] == 1 and y_true[i] == 1:
            b18 += 1
        elif b12[i] == 0 and y_true[i] == 1:
            fp += 1
        elif b12[i] == 1 and y_true[i] == 0:
            fn += 1
    return np.array([[b16, fp], [fn, b18]])
for i, threshold in enumerate(b11):
    b17 = fonk2(b2, b12[i])
    b16, fp, fn, b18 = b17.flatten()
    b19 = b16 / (b16 + fn)
    b20 = fp / (fp + b18)
    b14.append(b19)
    b15.append(b20)
    b21 = b16 / (b16 + fp) if (b16 + fp) != 0 else 0
    b22 = b19
    print(f"CASE {i + 1} (b23 = {threshold}):")
    print(b17)
    print(f"Precision: {b21}")
    print(f"Recall: {b22}")
plt.plot(b15, b14)
plt.ylabel("True Positive Rate")
plt.xlabel("False Positive Rate")
plt.title("ROC Curve")
plt.show()