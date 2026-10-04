
import numpy as np
import pandas as pd
from collections import defaultdict
from sklearn import datasets
def fonk1(u, v):
    return np.inner(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))
def fonk2(train, test, b15, b1 = 5):
    b2 = []
    for test_vector in test:
        b3 = {i: fonk1(train_vector, test_vector) for i, train_vector in enumerate(train)}
        b4 = sorted(b3.items(), key=lambda item: item[1], reverse=True)
        b5 = [b4[i][0] for i in range(min(b1, len(b4)))]
        b6 = [b15[i] for i in b5]
        b7 = defaultdict(int)
        for label in b6:
            b7[label] += 1
        b8 = max(b7.items(), key=lambda item: item[1])[0]
        b2.append(b8)
    return b2
def fonk3():
    b9 = datasets.load_iris()
    b10 = pd.DataFrame(b9.data, columns=b9.feature_names)
    b10['target'] = b9.target
    b11 = []
    for _ in range(20):
        b12 = b10.sample(frac=1).reset_index(drop=True)
        b13 = b12['target'].values
        b14 = b12.drop('target', axis=1).values
        x_train, b15 = b14[:120], b13[:120]
        x_test, b16 = b14[120:], b13[120:]
        b17 = fonk2(x_train, x_test, b15, b1=5)
        b18 = np.mean(b17 == b16) * 100
        b11.append(b18)
    print(f"Average b18 for b9 dataset: {np.mean(b11):.2f}%")
def fonk4():
    b19 = pd.read_csv("redwinequality.csv")
    b11 = []
    b20 = []
    for _ in range(20):
        b12 = b19.sample(frac=1).reset_index(drop=True)
        b21 = b12['quality'].values
        b22 = b12.drop('quality', axis=1).values
        x_train, b15 = b22[:1500], b21[:1500]
        x_test, b16 = b22[1500:1600], b21[1500:1600]
        b17 = fonk2(x_train, x_test, b15, b1=5)
        b23 = np.mean(b17 == b16) * 100
        b24 = np.mean(np.abs(np.array(b17) - b16) < 2) * 100
        b11.append(b23)
        b20.append(b24)
    print(f"Average strict b18 for red wine dataset: {np.mean(b11):.2f}%")
    print(f"Average fuzzy b18 for red wine dataset: {np.mean(b20):.2f}%")
if b25 = = '__main__':
    fonk3()
    fonk4()