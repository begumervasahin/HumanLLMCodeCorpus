
import numpy as np
import pandas as pd
from collections import defaultdict
from sklearn import datasets
from sklearn.model_selection import train_test_split
from operator import itemgetter
def fonk1(u, v):
    return np.inner(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))
def fonk2(train, test, y_train, b1 = 5):
    b2 = []
    for test_sample in test:
        b3 = {i: fonk1(train_sample, test_sample)
                     for i, train_sample in enumerate(train)}
        b4 = sorted(b3.items(), key=itemgetter(1), reverse=True)[:b1]
        b5 = [neighbor[0] for neighbor in b4]
        b6 = [y_train[i] for i in b5]
        b7 = defaultdict(int)
        for target in b6:
            b7[target] += 1
        b8 = sorted(b7.items(), key=itemgetter(1), reverse=True)
        b9 = b8[0][0]
        b2.append(b9)
    return b2
def fonk3(b2, true_labels):
    return np.mean(np.array(b2) == true_labels) * 100
def fonk4():
    b10 = datasets.load_iris()
    b11 = pd.DataFrame(b10.data)
    b11['target'] = b10.target
    b12 = []
    for _ in range(20):
        b13 = b11.sample(frac=1).reset_index(drop=True)
        b14 = b13.drop('target', axis=1).values
        b15 = b13['target'].values
        X_train, X_test, y_train, b16 = train_test_split(b14, b15, test_size=0.2, random_state=None)
        b17 = fonk2(X_train, X_test, y_train, b1=5)
        b12.append(fonk3(b17, b16))
    print(f"Average accuracy for Iris dataset: {np.mean(b12):.2f}%")
    b18 = pd.read_csv("redwinequality.csv")
    b19 = []
    b20 = []
    for _ in range(20):
        b13 = b18.sample(frac=1).reset_index(drop=True)
        b21 = b13.drop('quality', axis=1).values
        b22 = b13['quality'].values
        X_train, X_test, y_train, b16 = train_test_split(b21, b22, test_size=0.1, random_state=None)
        b17 = fonk2(X_train, X_test, y_train, b1=5)
        b19.append(fonk3(b17, b16))
        b23 = np.mean(np.abs(np.array(b17) - b16) < 2) * 100
        b20.append(b23)
    print(f"Average strict accuracy for Red Wine dataset: {np.mean(b19):.2f}%")
    print(f"Average fuzzy accuracy for Red Wine dataset: {np.mean(b20):.2f}%")
if b24 = = '__main__':
    fonk4()