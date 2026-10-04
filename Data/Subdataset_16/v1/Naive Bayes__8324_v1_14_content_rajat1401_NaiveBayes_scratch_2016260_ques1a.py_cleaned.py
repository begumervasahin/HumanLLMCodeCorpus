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
for i in range(len(b5)):
    b5[i][0] /= b7
    b6[i][0] /= b7
    b5[i][1] /= b8
    b6[i][1] /= b8
print("The prior trouser is:", b9)
print("The prior pullover is:", b10)
b11 = [0.3, 0.4, 0.5, 0.6, 0.7]
b12 = np.zeros((len(b11), len(b4)))
for k, threshold in enumerate(b11):
    for i in range(len(b4)):
        b13 = pdt2 = 0
        for j in range(len(b4[0])):
            if b4[i][j] == 1:
                b13 += math.log(b6[j][0])
                pdt2 += math.log(b6[j][1])
            else:
                b13 += math.log(b5[j][0])
                pdt2 += math.log(b5[j][1])
        b14 = (b13 * b9) / (b13 * b9 + pdt2 * b10)
        b12[k][i] = 0 if b14 <= threshold else 1
print("Lengths:", len(b12), len(b2))
print(b12[:, 0], b12[:, 1])
b15 = []
b16 = []
for i in range(len(b11)):
    b17 = np.zeros((2, 2))
    b18 = fp = fn = tn = 0
    for j in range(len(b2)):
        if b12[i][j] == 0 and b2[j] == 0:
            b18 += 1
        elif b12[i][j] == 1 and b2[j] == 1:
            tn += 1
        elif b12[i][j] == 0 and b2[j] == 1:
            fp += 1
        elif b12[i][j] == 1 and b2[j] == 0:
            fn += 1
    b17[0][0] = b18
    b17[1][1] = tn
    b17[0][1] = fp
    b17[1][0] = fn
    b15.append(b18 / (b18 + fn))
    b16.append(fp / (fp + tn))
    print(f"CASE {i + 1} :-")
    print(b17)
    print("The precision is:", b18 / (b18 + fp))
    print("The recall is:", b18 / (b18 + fn))
plt.plot(b16, b15)
plt.ylabel("True Positive Rate")
plt.xlabel("False Positive Rate")
plt.title("ROC Curve")
plt.show()