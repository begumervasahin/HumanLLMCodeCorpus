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
for k, threshold in enumerate(b11):
    for i in range(len(b4)):
        a1 = 0
        a2 = 0
        for j in range(len(b4[0])):
            if b4[i][j] == 1:
                a1 += math.log(b6[j][0])
                a2 += math.log(b6[j][1])
            else:
                a1 += math.log(b5[j][0])
                a2 += math.log(b5[j][1])
        b13 = (a1 * b9) / (a1 * b9 + a2 * b10)
        b12[k][i] = 0 if b13 <= threshold else 1
print(f"Prediction lengths: {len(b12)}, {len(b2)}")
print(b12[:, 0], b12[:, 1])
b14 = []
b15 = []
for i in range(len(b11)):
    b16 = fp = fn = tn = 0
    for j in range(len(b2)):
        if b12[i][j] == 0 and b2[j] == 0:
            b16 += 1
        elif b12[i][j] == 1 and b2[j] == 1:
            tn += 1
        elif b12[i][j] == 0 and b2[j] == 1:
            fp += 1
        elif b12[i][j] == 1 and b2[j] == 0:
            fn += 1
    b17 = np.array([[b16, fp], [fn, tn]])
    b18 = b16 / (b16 + fn)
    b19 = fp / (fp + tn)
    b14.append(b18)
    b15.append(b19)
    print(f"CASE {i + 1}:")
    print(b17)
    print(f"Precision: {b16 / (b16 + fp)}")
    print(f"Recall: {b18}")
plt.plot(b15, b14)
plt.ylabel("True Positive Rate")
plt.xlabel("False Positive Rate")
plt.title("ROC Curve")
plt.show()