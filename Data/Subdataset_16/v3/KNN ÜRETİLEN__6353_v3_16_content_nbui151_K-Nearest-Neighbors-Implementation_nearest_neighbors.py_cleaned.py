
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
        b5 = [y_train[neighbor[0]] for neighbor in b4]
        b6 = defaultdict(int)
        for target in b5:
            b6[target] += 1
        b7 = max(b6.items(), key=itemgetter(1))[0]
        b2.append(b7)
    return b2
def fonk3(b2, true_labels):
    return np.mean(np.array(b2) == true_labels) * 100
def fonk4():
    b8 = datasets.load_iris()
    b9 = pd.DataFrame(b8.data, columns=b8.feature_names)
    b9['target'] = b8.target
    return b9
def fonk5(file_path):
    b10 = pd.read_csv(file_path)
    return b10
def fonk6():
    b9 = fonk4()
    b11 = []
    for _ in range(20):
        b12 = b9.sample(frac=1).reset_index(drop=True)
        b13 = b12.drop('target', axis=1).values
        b14 = b12['target'].values
        X_train, X_test, y_train, b15 = train_test_split(b13, b14, test_size=0.2, random_state=None)
        b16 = fonk2(X_train, X_test, y_train, b1=5)
        b11.append(fonk3(b16, b15))
    print(f"Average accuracy for Iris dataset: {np.mean(b11):.2f}%")
    b10 = fonk5("redwinequality.csv")
    b17 = []
    b18 = []
    for _ in range(20):
        b12 = b10.sample(frac=1).reset_index(drop=True)
        b19 = b12.drop('quality', axis=1).values
        b20 = b12['quality'].values
        X_train, X_test, y_train, b15 = train_test_split(b19, b20, test_size=0.1, random_state=None)
        b16 = fonk2(X_train, X_test, y_train, b1=5)
        b17.append(fonk3(b16, b15))
        b21 = np.mean(np.abs(np.array(b16) - b15) < 2) * 100
        b18.append(b21)
    print(f"Average strict accuracy for Red Wine dataset: {np.mean(b17):.2f}%")
    print(f"Average fuzzy accuracy for Red Wine dataset: {np.mean(b18):.2f}%")
if b22 = = '__main__':
    fonk6()