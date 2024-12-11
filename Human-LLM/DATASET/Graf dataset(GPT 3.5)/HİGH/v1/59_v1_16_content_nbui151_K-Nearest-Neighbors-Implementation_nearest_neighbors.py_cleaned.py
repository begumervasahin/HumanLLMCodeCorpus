import numpy as np
import pandas as pd
from collections import defaultdict
from sklearn import datasets
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
        b8 = sorted(b5.items(), key=lambda t: t[1], reverse=True)
        b9 = [b8[i][0] for i in range(b2) if b2 < len(b8)]
        b10 = [Y_train[item] for item in b9]
        b11 = defaultdict(int)
        for i in b10:
            b11[i] += 1
        b12 = sorted(b11.items(), key=lambda t: t[1], reverse=True)
        b13 = b12[0][0]
        b3.append(b13)
    return b3
def fonk3():
    b14 = datasets.load_iris()
    b15 = pd.DataFrame(b14.data)
    b15['target'] = b14.target
    b16 = []
    for i in range(20):
        b17 = b15.sample(frac=1).reset_index(drop=True)
        b18 = np.array(b17.target)
        b19 = np.array(b17.drop('target', axis=1))
        b20 = b19[:120]
        b21 = b18[:120]
        b22 = b19[120:]
        b23 = b18[120:]
        b24 = fonk2(b20, b22, b21, b2=5)
        b25 = np.mean(b24 == b23) * 100
        b16.append(b25)
    print("Average accuracy for iris dataset is ", np.mean(b16))
    b26 = pd.read_csv("redwinequality.csv")
    b27 = []
    b28 = []
    for i in range(20):
        b29 = b26.sample(frac=1).reset_index(drop=True)
        b30 = np.array(b29.quality)
        b31 = np.array(b29.drop('quality', axis=1))
        b32 = b31[:1500]
        b33 = b30[:1500]
        b34 = b31[1500:1600]
        b35 = b30[1500:1600]
        b36 = fonk2(b32, b34, b33, b2=5)
        b37 = np.mean(b36 == b35) * 100
        b27.append(b37)
        b38 = np.mean(abs(b36 - b35) < 2) * 100
        b28.append(b38)
    print("Average strict accuracy for red wine dataset is ", np.mean(b27))
    print("Average fuzzy accuracy for red wine dataset is ", np.mean(b28))
if b39 = = "__main__":
    fonk3()