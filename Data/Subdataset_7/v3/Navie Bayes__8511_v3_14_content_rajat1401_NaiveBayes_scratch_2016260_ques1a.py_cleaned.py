import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import pickle
from mlxtend.data import loadlocal_mnist
def fonk1(images_path, labels_path):
    X, b1 = loadlocal_mnist(images_path=images_path, labels_path=labels_path)
    return X, b1
def fonk2(X_train, b27, X_test, b28, b2 = [1, 2]):
    b3 = [label - 1 for label in b27 if label in b2]
    b4 = [label - 1 for label in b28 if label in b2]
    return b3, b4
def fonk3(train_path, test_path):
    with open(train_path, 'rb') as f:
        b5 = pickle.load(f)
    with open(test_path, 'rb') as f:
        b6 = pickle.load(f)
    return b5, b6
def fonk4(train0_path, train1_path):
    b7 = np.load(train0_path)
    b8 = np.load(train1_path)
    return b7, b8
def fonk5(b3):
    b9 = b3.count(0)
    b10 = b3.count(1)
    b11 = b9 / (b9 + b10)
    b12 = b10 / (b9 + b10)
    return b11, b12
def fonk6(b7, b8, b9, b10):
    b13 = b7 / b9
    b14 = b8 / b10
    return b13, b14
def fonk7(b6, b7, b8, b11, b12, b29):
    b15 = np.zeros(shape=(len(b29), len(b6)))
    for k, threshold in enumerate(b29):
        for i in range(len(b6)):
            b16 = sum(math.log(b8[j][0]) if b6[i][j] == 1 else math.log(b7[j][0]) for j in range(len(b6[0])))
            b17 = sum(math.log(b8[j][1]) if b6[i][j] == 1 else math.log(b7[j][1]) for j in range(len(b6[0])))
            b18 = (b16 * b11) / (b16 * b11 + b17 * b12)
            b15[k][i] = 0 if b18 <= threshold else 1
    return b15
def fonk8(b15, b4):
    b19 = []
    b20 = []
    for i in range(len(b15)):
        b21 = sum(b15[i][j] == 0 and b4[j] == 0 for j in range(len(b4)))
        b22 = sum(b15[i][j] == 1 and b4[j] == 1 for j in range(len(b4)))
        b23 = sum(b15[i][j] == 0 and b4[j] == 1 for j in range(len(b4)))
        b24 = sum(b15[i][j] == 1 and b4[j] == 0 for j in range(len(b4)))
        b19.append(b21 / (b21 + b24))
        b20.append(b23 / (b23 + b22))
        b25 = np.array([[b21, b23], [b24, b22]])
        print("CASE", i + 1, ":-")
        print(b25)
        print("The precision is:", b21 / (b21 + b23))
        print("The recall is:", b21 / (b21 + b24))
    return b19, b20
def fonk9(b20, b19):
    plt.plot(b20, b19)
    plt.ylabel("True Positive Rate")
    plt.xlabel("False Positive Rate")
    plt.title("ROC Curve")
    plt.show()
if b26 = = "__main__":
    X_train, b27 = fonk1(images_path='./train-images.idx3-ubyte', labels_path='./train-labels.idx1-ubyte')
    X_test, b28 = fonk1(images_path='./t10k-images.idx3-ubyte', labels_path='./t10k-labels.idx1-ubyte')
    b3, b4 = fonk2(X_train, b27, X_test, b28, b2=[1, 2])
    b5, b6 = fonk3(train_path='./bintrain.pkl', test_path='./bintest.pkl')
    b7, b8 = fonk4(train0_path='./b7.mat', train1_path='./b8.mat')
    b11, b12 = fonk5(b3)
    b13, b14 = fonk6(b7, b8, len(b3), len(b4))
    b29 = [0.3, 0.4, 0.5, 0.6, 0.7]
    b15 = fonk7(b6, b13, b14, b11, b12, b29)
    b19, b20 = fonk8(b15, b4)
    fonk9(b20, b19)