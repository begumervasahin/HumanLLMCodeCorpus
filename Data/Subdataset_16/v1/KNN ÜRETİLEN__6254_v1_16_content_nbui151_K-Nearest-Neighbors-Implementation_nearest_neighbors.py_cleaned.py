
import numpy as np
import pandas as pd
import operator
from collections import defaultdict
from sklearn import datasets
from sklearn.model_selection import train_test_split
def fonk1(b6, b4):
    b1 = np.inner(b6, b4) / (np.linalg.norm(b6) * np.linalg.norm(b4))
    return b1
def fonk2(train, test, Y_train, b2 = 5):
    b3 = []
    for m in range(test.shape[0]):
        b4 = test[m]
        b5 = {}
        for i in range(train.shape[0]):
            b6 = train[i]
            b7 = fonk1(b6, b4)
            b5[i] = b7
        b8 = sorted(b5.items(), key=operator.itemgetter(1), reverse=True)
        b9 = []
        for i in range(b2):
            if b2 < len(b8):
                b9.append(b8[i][0])
        b10 = []
        for item in b9:
            b10.append(Y_train[item])
        b11 = defaultdict(int)
        for i in b10:
            b11[i] += 1
        b12 = sorted(b11.items(), key=operator.itemgetter(1), reverse=True)
        b13 = b12[0][0]
        b3.append(b13)
    return b3
b14 = datasets.load_iris()
b15 = pd.DataFrame(b14.data)
b15['target'] = b14.target
b16 = []
for _ in range(20):
    b17 = b15.sample(frac=1).reset_index(drop=True)
    b18 = np.array(b17.target)
    b19 = np.array(b17.drop('target', axis=1))
    train_iris, test_iris, Y_train_iris, b20 = train_test_split(b19, b18, test_size=0.2, random_state=None)
    b21 = fonk2(train_iris, test_iris, Y_train_iris, b2=5)
    b22 = np.mean(np.array(b21) == b20) * 100
    b16.append(b22)
print("Average accuracy for iris dataset is ", np.mean(b16))
b23 = pd.read_csv("redwinequality.csv")
b24 = []
b25 = []
for _ in range(20):
    b26 = b23.sample(frac=1).reset_index(drop=True)
    b27 = np.array(b26.quality)
    b28 = np.array(b26.drop('quality', axis=1))
    train_wine, test_wine, Y_train_wine, b29 = train_test_split(b28, b27, test_size=0.1, random_state=None)
    b30 = fonk2(train_wine, test_wine, Y_train_wine, b2=5)
    b31 = np.mean(np.array(b30) == b29) * 100
    b24.append(b31)
    b32 = np.mean(abs(np.array(b30) - b29) < 2) * 100
    b25.append(b32)
print("Average strict accuracy for red wine dataset is ", np.mean(b24))
print("Average fuzzy accuracy for red wine dataset is ", np.mean(b25))