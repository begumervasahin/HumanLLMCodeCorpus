import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import pickle
from mlxtend.data import loadlocal_mnist
X_train, b1 = loadlocal_mnist(images_path='./train-images.idx3-ubyte', labels_path='./train-labels.idx1-ubyte')
X_test, b2 = loadlocal_mnist(images_path='./t10k-images.idx3-ubyte', labels_path='./t10k-labels.idx1-ubyte')
b3 = [label - 1 for label in b1 if label in [1, 2]]
b4 = [label - 1 for label in b2 if label in [1, 2]]
with open('./bintrain.pkl', 'rb') as f:
    b5 = pickle.load(f)
with open('./bintest.pkl', 'rb') as f:
    b6 = pickle.load(f)
b7 = np.load('./b7.mat')
b8 = np.load('./b8.mat')
b9 = b3.count(0)
b10 = b3.count(1)
b11 = b9 / (b9 + b10)
b12 = b10 / (b9 + b10)
for i in range(len(b7)):
    for j in range(2):
        b7[i][j] /= b9
        b8[i][j] /= b10
b13 = [0.3, 0.4, 0.5, 0.6, 0.7]
b14 = np.zeros(shape=(5, len(b6)))
for k, threshold in enumerate(b13):
    for i in range(len(b6)):
        a1 = 0
        a2 = 0
        for j in range(len(b6[0])):
            if b6[i][j] == 1:
                a1 += math.log(b8[j][0])
                a2 += math.log(b8[j][1])
            else:
                a1 += math.log(b7[j][0])
                a2 += math.log(b7[j][1])
        b15 = (a1 * b11) / (a1 * b11 + a2 * b12)
        b14[k][i] = 0 if b15 <= threshold else 1
b16 = []
b17 = []
for i in range(5):
    b18 = sum(b14[i][j] == 0 and b4[j] == 0 for j in range(len(b4)))
    b19 = sum(b14[i][j] == 1 and b4[j] == 1 for j in range(len(b4)))
    b20 = sum(b14[i][j] == 0 and b4[j] == 1 for j in range(len(b4)))
    b21 = sum(b14[i][j] == 1 and b4[j] == 0 for j in range(len(b4)))
    b16.append(b18 / (b18 + b21))
    b17.append(b20 / (b20 + b19))
    b22 = np.array([[b18, b20], [b21, b19]])
    print("CASE", i + 1, ":-")
    print(b22)
    print("The precision is:", b18 / (b18 + b20))
    print("The recall is:", b18 / (b18 + b21))
plt.plot(b17, b16)
plt.ylabel("True Positive Rate")
plt.xlabel("False Positive Rate")
plt.title("ROC Curve")
plt.show()