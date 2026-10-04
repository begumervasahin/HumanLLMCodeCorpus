import numpy as np
import scipy.stats as stats
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
def fonk1():
    b1 = load_iris()
    print("\nIris Dataset Keys:")
    print(b1.keys())
    b2 = b1.data
    b3 = b1.target
    print("\nClass Labels:")
    print(b1.target_names)
    b4 = len(b1.target_names)
    print(f"Number of class class1: {b4}")
    n, b5 = b2.shape
    print(f"\nNumber of samples: {n}")
    print(f"Number of features per sample: {b5}")
    X_train, X_test, b11, b6 = train_test_split(b2, b3, random_state=42)
    b7 = len(X_train)
    b8 = len(X_test)
    print(f"\nNumber of training samples: {b7}")
    print(f"Number of testing samples: {b8}")
    b9 = np.zeros((b4, b5))
    b10 = np.zeros((b4, b5))
    for i in range(b4):
        b9[i] = X_train[b11 = = i].mean(axis=0)
        b10[i] = X_train[b11 = = i].std(axis=0)
    a1 = 0.01
    b12 = np.zeros(b4)
    for i in range(b4):
        b12[i] = (b11 = = i).sum() / b7
    b13 = np.zeros((b8, b4))
    for i in range(b8):
        for k in range(b4):
            b14 = np.log(b12[k])
            for j in range(b5):
                b14 += np.log(stats.norm.pdf(X_test[i, j], b9[k, j], b10[k, j]) + a1)
            b13[i, k] = b14
    b15 = b13.argmax(axis=1)
    b16 = (b15 == b6).sum() / b8
    print("\nModel Accuracy:")
    print(f"{b16:.2f}")
if b17 = = '__main__':
    fonk1()