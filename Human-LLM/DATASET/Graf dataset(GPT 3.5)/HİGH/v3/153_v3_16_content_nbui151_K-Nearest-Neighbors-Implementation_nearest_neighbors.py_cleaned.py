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
def fonk3(b11, Y_true):
    return np.mean(b11 = = Y_true) * 100
def fonk4():
    b12 = datasets.load_iris()
    b13 = pd.DataFrame(b12.data, columns=b12.feature_names)
    b13['target'] = b12.target
    b14 = []
    for _ in range(20):
        b15 = b13.sample(frac=1).reset_index(drop=True)
        b16 = np.array(b15['target'])
        b17 = np.array(b15.drop('target', axis=1))
        b18 = b17[:120]
        b19 = b16[:120]
        b20 = b17[120:]
        b21 = b16[120:]
        b22 = fonk2(b18, b20, b19, b2=5)
        b23 = fonk3(b22, b21)
        b14.append(b23)
    print("Average accuracy for Iris dataset:", np.mean(b14))
    b24 = pd.read_csv("redwinequality.csv")
    b25 = []
    b26 = []
    for _ in range(20):
        b27 = b24.sample(frac=1).reset_index(drop=True)
        b28 = np.array(b27['quality'])
        b29 = np.array(b27.drop('quality', axis=1))
        b30 = b29[:1500]
        b31 = b28[:1500]
        b32 = b29[1500:1600]
        b33 = b28[1500:1600]
        b34 = fonk2(b30, b32, b31, b2=5)
        b35 = fonk3(b34, b33)
        b25.append(b35)
        b36 = fonk3(np.abs(b34 - b33) < 2, np.ones(len(b33)))
        b26.append(b36)
    print("Average strict accuracy for Wine dataset:", np.mean(b25))
    print("Average fuzzy accuracy for Wine dataset:", np.mean(b26))
if b37 = = "__main__":
    fonk4()