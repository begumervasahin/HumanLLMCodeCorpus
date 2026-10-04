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
    b4 = b1.target_names
    print(b4)
    b5 = len(b4)
    print(f"Number of class class1: {b5}")
    num_samples, b6 = b2.shape
    print(f"\nNumber of samples: {num_samples}")
    print(f"Number of features per sample: {b6}")
    return b2, b3, b5, b4, num_samples, b6
def fonk2(X_train, b9, b5, b6):
    b7 = np.zeros((b5, b6))
    b8 = np.zeros((b5, b6))
    for i in range(b5):
        b7[i] = X_train[b9 = = i].mean(axis=0)
        b8[i] = X_train[b9 = = i].std(axis=0)
    return b7, b8
def fonk3(b9, b5, b16):
    b10 = np.zeros(b5)
    for i in range(b5):
        b10[i] = (b9 = = i).sum() / b16
    return b10
def fonk4(X_test, b7, b8, b10, b11 = 0.01):
    b17, b6 = X_test.shape
    b5 = b7.shape[0]
    b12 = np.zeros((b17, b5))
    for i in range(b17):
        for k in range(b5):
            b13 = np.log(b10[k])
            for j in range(b6):
                b13 += np.log(stats.norm.pdf(X_test[i, j], b7[k, j], b8[k, j]) + b11)
            b12[i, k] = b13
    return b12
def fonk5(b18, b15):
    b14 = (b18 == b15).sum() / len(b15)
    return b14
def fonk6():
    b2, b3, b5, b4, num_samples, b6 = fonk1()
    X_train, X_test, b9, b15 = train_test_split(b2, b3, random_state=42)
    b16 = len(X_train)
    b17 = len(X_test)
    print(f"\nNumber of training samples: {b16}")
    print(f"Number of testing samples: {b17}")
    b7, b8 = fonk2(X_train, b9, b5, b6)
    b10 = fonk3(b9, b5, b16)
    b12 = fonk4(X_test, b7, b8, b10)
    b18 = b12.argmax(axis=1)
    b14 = fonk5(b18, b15)
    print("\nModel Accuracy:")
    print(f"{b14:.2f}")
if b19 = = '__main__':
    fonk6()