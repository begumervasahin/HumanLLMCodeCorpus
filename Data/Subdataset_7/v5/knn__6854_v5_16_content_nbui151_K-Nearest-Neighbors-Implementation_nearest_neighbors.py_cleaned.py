import numpy as np
import pandas as pd
from sklearn import datasets
from collections import defaultdict
import operator
def fonk1(u, v):
    b1 = np.inner(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))
    return b1
def fonk2(train, test, b18, b2 = 5):
    b3 = []
    for test_vector in test:
        b4 = {}
        for i, train_vector in enumerate(train):
            b5 = fonk1(train_vector, test_vector)
            b4[i] = b5
        b6 = sorted(b4.items(), key=operator.itemgetter(1), reverse=True)
        b7 = [idx for idx, _ in b6[:b2]]
        b8 = [b18[idx] for idx in b7]
        b9 = defaultdict(int)
        for target in b8:
            b9[target] += 1
        b10 = sorted(b9.items(), key=operator.itemgetter(1), reverse=True)
        b11 = b10[0][0]
        b3.append(b11)
    return b3
def fonk3(data, target_name, n_train_samples, n_test_samples, n_trials, b12 = False):
    b13 = []
    for _ in range(n_trials):
        b14 = data.sample(frac=1).reset_index(drop=True)
        b15 = np.array(b14[target_name])
        b16 = np.array(b14.drop(target_name, axis=1))
        b17 = b16[:n_train_samples]
        b18 = b15[:n_train_samples]
        b19 = b16[n_train_samples:n_train_samples + n_test_samples]
        b20 = b15[n_train_samples:n_train_samples + n_test_samples]
        b21 = fonk2(b17, b19, b18, b2=5)
        if b12:
            b22 = np.mean(np.abs(np.array(b21) - np.array(b20)) < 2) * 100
        else:
            b22 = np.mean(np.array(b21) == np.array(b20)) * 100
        b13.append(b22)
    return np.mean(b13)
if b23 = = '__main__':
    b24 = datasets.load_iris()
    b25 = pd.DataFrame(b24.data, columns=b24.feature_names)
    b25['target'] = b24.target
    b26 = fonk3(b25, 'target', 120, 30, 20)
    print("Average b22 for iris dataset is:", b26)
    b27 = pd.read_csv("redwinequality.csv")
    b28 = fonk3(b27, 'quality', 1500, 100, 20)
    b29 = fonk3(b27, 'quality', 1500, 100, 20, b12=True)
    print("Average strict b22 for red wine dataset is:", b28)
    print("Average b12 b22 for red wine dataset is:", b29)