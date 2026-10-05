import numpy as np
import pandas as pd
from collections import defaultdict
from sklearn import datasets
def fonk1(u, v):
    b1 = np.inner(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))
    return b1
def fonk2(train, test, Y_train, b2 = 5):
    b3 = []
    for test_instance in test:
        b4 = {}
        for idx, train_instance in enumerate(train):
            b5 = fonk1(train_instance, test_instance)
            b4[idx] = b5
        b6 = sorted(b4.items(), key=lambda x: x[1], reverse=True)
        b7 = [i[0] for i in b6[:b2]]
        b8 = [Y_train[idx] for idx in b7]
        b9 = defaultdict(int)
        for target in b8:
            b9[target] += 1
        b10 = max(b9, key=b9.get)
        b3.append(b10)
    return b3
def fonk3():
    b11 = datasets.load_iris()
    b12 = pd.DataFrame(b11.data, columns=b11.feature_names)
    b12['target'] = b11.target
    b13 = []
    for _ in range(20):
        b14 = b12.sample(frac=1).reset_index(drop=True)
        b15 = np.array(b14['target'])
        b16 = np.array(b14.drop('target', axis=1))
        b17 = b16[:120]
        b18 = b15[:120]
        b19 = b16[120:]
        b20 = b15[120:]
        b21 = fonk2(b17, b19, b18, b2=5)
        b22 = np.mean(b21 == b20) * 100
        b13.append(b22)
    print("Average accuracy for Iris dataset:", np.mean(b13))
    b23 = pd.read_csv("redwinequality.csv")
    b24 = []
    b25 = []
    for _ in range(20):
        b26 = b23.sample(frac=1).reset_index(drop=True)
        b27 = np.array(b26['quality'])
        b28 = np.array(b26.drop('quality', axis=1))
        b29 = b28[:1500]
        b30 = b27[:1500]
        b31 = b28[1500:1600]
        b32 = b27[1500:1600]
        b33 = fonk2(b29, b31, b30, b2=5)
        b34 = np.mean(b33 == b32) * 100
        b24.append(b34)
        b35 = np.mean(np.abs(b33 - b32) < 2) * 100
        b25.append(b35)
    print("Average strict accuracy for Wine dataset:", np.mean(b24))
    print("Average fuzzy accuracy for Wine dataset:", np.mean(b25))
if b36 = = "__main__":
    fonk3()