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
    print("\nClass Labels are:")
    print(b1.target_names)
    b4 = len(b1.target_names)
    print(f"{b4} class class1")
    num_samples, b5 = b2.shape
    print(f"\nWe have {num_samples} samples")
    print(f"With {b5} features each")
    return b2, b3, b4, num_samples, b5
def fonk2(b2, b3):
    X_train, X_test, b14, b6 = train_test_split(b2, b3, random_state=42)
    b7 = len(X_train)
    b8 = len(X_test)
    print(f"\n{b7} samples in the training set")
    print(f"{b8} samples in the test set")
    return X_train, X_test, b14, b6, b7, b8
def fonk3(X_train, b14, b4, b5):
    b9 = np.zeros((b4, b5), dtype=float)
    b10 = np.zeros((b4, b5), dtype=float)
    for class_index in range(b4):
        b11 = X_train[b14 == class_index]
        b9[class_index] = b11.mean(b12 = 0)
        b10[class_index] = b11.std(b12 = 0)
    return b9, b10
def fonk4(b14, b4, b7):
    b13 = np.zeros(b4, dtype=float)
    for class_index in range(b4):
        b13[class_index] = (b14 = = class_index).sum() / b7
    return b13
def fonk5(X_test, b9, b10, b13, b15 = 0.01):
    b8 = len(X_test)
    b4 = len(b13)
    b5 = X_test.shape[1]
    b16 = np.zeros((b8, b4), dtype=float)
    for i in range(b8):
        for class_index in range(b4):
            b17 = np.log(b13[class_index])
            for feature_index in range(b5):
                b17 += np.log(stats.norm.pdf(X_test[i, feature_index],
                                                  b9[class_index, feature_index],
                                                  b10[class_index, feature_index]) + b15)
            b16[i, class_index] = b17
    return b16
def fonk6(b16, b6):
    b18 = (b16.argmax(b12=1) == b6).sum() / len(b6)
    print("\nProbability that the model predicts the correct class class2:")
    print(b18)
    print()
    return b18
def fonk7():
    b2, b3, b4, num_samples, b5 = fonk1()
    X_train, X_test, b14, b6, b7, b8 = fonk2(b2, b3)
    b9, b10 = fonk3(X_train, b14, b4, b5)
    b13 = fonk4(b14, b4, b7)
    b16 = fonk5(X_test, b9, b10, b13)
    fonk6(b16, b6)
if b19 = = "__main__":
    fonk7()