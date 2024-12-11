import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import pickle
from mlxtend.data import loadlocal_mnist
def fonk1():
    X_train, b1 = loadlocal_mnist(images_path='./train-images.idx3-ubyte', labels_path='./train-labels.idx1-ubyte')
    X_test, b2 = loadlocal_mnist(images_path='./t10k-images.idx3-ubyte', labels_path='./t10k-labels.idx1-ubyte')
    b3 = [label - 1 for label in b1 if label in [1, 2]]
    b4 = [label - 1 for label in b2 if label in [1, 2]]
    return X_train, b3, X_test, b4
def fonk2():
    with open('./bintrain.pkl', 'rb') as f:
        b5 = pickle.load(f)
    with open('./bintest.pkl', 'rb') as f:
        b6 = pickle.load(f)
    return b5, b6
def fonk3():
    b7 = np.load('./b7.mat')
    b8 = np.load('./b8.mat')
    b9 = b1.count(0)
    b10 = b1.count(1)
    b11 = b9 / (b9 + b10)
    b12 = b10 / (b9 + b10)
    return b7, b8, b11, b12
def fonk4(b7, b8, b9, b10):
    for i in range(len(b7)):
        for j in range(2):
            b7[i][j] /= b9
            b8[i][j] /= b10
    return b7, b8
def fonk5(b6, b7, b8, b11, b12, b24):
    b13 = np.zeros(shape=(len(b24), len(b6)))
    for k, threshold in enumerate(b24):
        for i in range(len(b6)):
            b14 = sum(math.log(b8[j][0]) if b6[i][j] == 1 else math.log(b7[j][0]) for j in range(len(b6[0])))
            b15 = sum(math.log(b8[j][1]) if b6[i][j] == 1 else math.log(b7[j][1]) for j in range(len(b6[0])))
            b16 = (b14 * b11) / (b14 * b11 + b15 * b12)
            b13[k][i] = 0 if b16 <= threshold else 1
    return b13
def fonk6(b2, b13):
    b17 = []
    b18 = []
    for i in range(len(b13)):
        b19 = np.zeros(shape=(2, 2))
        b20 = sum(1 for j in range(len(b2)) if b13[i][j] == 0 and b2[j] == 0)
        b21 = sum(1 for j in range(len(b2)) if b13[i][j] == 1 and b2[j] == 1)
        b22 = sum(1 for j in range(len(b2)) if b13[i][j] == 0 and b2[j] == 1)
        b23 = sum(1 for j in range(len(b2)) if b13[i][j] == 1 and b2[j] == 0)
        b19[0][0] = b20
        b19[1][1] = b21
        b19[0][1] = b22
        b19[1][0] = b23
        b17.append(b20 / (b20 + b23))
        b18.append(b22 / (b22 + b21))
        print("CASE" + str(i + 1) + " :-")
        print(b19)
        print("The precision is: " + str((b20 / (b20 + b22))))
        print("The recall is: " + str((b20 / (b20 + b23))))
    return b17, b18
def fonk7(b18, b17):
    plt.plot(b18, b17)
    plt.ylabel("True Positive Rate")
    plt.xlabel("False Positive Rate")
    plt.title("ROC Curve")
    plt.show()
X_train, b1, X_test, b2 = fonk1()
b5, b6 = fonk2()
b7, b8, b11, b12 = fonk3()
b7, b8 = fonk4(b7, b8, len(b1.count(0)), len(b1.count(1)))
b24 = [0.3, 0.4, 0.5, 0.6, 0.7]
b13 = fonk5(b6, b7, b8, b11, b12, b24)
b17, b18 = fonk6(b2, b13)
fonk7(b18, b17)