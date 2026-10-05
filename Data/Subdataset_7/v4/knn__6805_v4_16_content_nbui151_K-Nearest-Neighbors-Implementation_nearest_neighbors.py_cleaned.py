import numpy as np
import pandas as pd
from sklearn import datasets
from collections import defaultdict
import operator
def fonk1(b6, b4):
    b1 = np.inner(b6, b4) / (np.linalg.norm(b6) * np.linalg.norm(b4))
    return b1
def fonk2(train, test, b20, b2 = 5):
    b3 = []
    for m in range(test.shape[0]):
        b4 = test[m]
        b5 = {}
        for i in range(train.shape[0]):
            b6 = train[i]
            b7 = fonk1(b6, b4)
            b5[i] = b7
        b8 = sorted(b5.items(), key=operator.itemgetter(1), reverse=True)
        b9 = [b8[i][0] for i in range(b2) if b2 < len(b8)]
        b10 = [b20[item] for item in b9]
        b11 = defaultdict(int)
        for i in b10:
            b11[i] += 1
        b12 = sorted(b11.items(), key=operator.itemgetter(1), reverse=True)
        b13 = b12[0][0]
        b3.append(b13)
    return b3
def fonk3(data, target_name, n_train_samples, n_test_samples, n_trials, b14 = False):
    b15 = []
    for i in range(n_trials):
        b16 = data.sample(frac=1).reset_index(drop=True)
        b17 = np.array(b16[target_name])
        b18 = np.array(b16.drop(target_name, axis=1))
        b19 = b18[:n_train_samples]
        b20 = b17[:n_train_samples]
        b21 = b18[n_train_samples:n_train_samples + n_test_samples]
        b22 = b17[n_train_samples:n_train_samples + n_test_samples]
        b23 = fonk2(b19, b21, b20, b2=5)
        if b14:
            b24 = np.mean(abs(np.array(b23) - np.array(b22)) < 2) * 100
        else:
            b24 = np.mean(np.array(b23) == np.array(b22)) * 100
        b15.append(b24)
    return np.mean(b15)
if b25 = = '__main__':
    b26 = datasets.load_iris()
    b27 = pd.DataFrame(b26.data)
    b27['target'] = b26.target
    b28 = fonk3(b27, 'target', 120, 30, 20)
    print("Average b24 for iris dataset is:", b28)
    b29 = pd.read_csv("redwinequality.csv")
    b30 = fonk3(b29, 'quality', 1500, 100, 20)
    b31 = fonk3(b29, 'quality', 1500, 100, 20, b14=True)
    print("Average strict b24 for red wine dataset is:", b30)
    print("Average b14 b24 for red wine dataset is:", b31)