import numpy as np
import scipy as sp
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
b1 = load_iris()
print("Iris Dataset Keys:")
print(b1.keys())
b2 = b1.data
b3 = b1.target
print("\nClass Labels are:")
print(b1.target_names)
b4 = len(b1.target_names)
print("{} class class1".format(b4))
n, b5 = b2.shape
print("\nWe have {} samples".format(n))
print("With {} features each".format(b5))
X_train, X_test, b11, b6 = train_test_split(b2, b3)
b7 = len(X_train)
b8 = len(X_test)
print("\n{} samples in the training set".format(b7))
print("{} samples in the test set".format(b8))
b9 = np.zeros((b4, b5), dtype=float)
b10 = np.zeros((b4, b5), dtype=float)
for i in range(0, b4):
    b9[i] = X_train[b11 = = i].mean(b15=0)
    b10[i] = X_train[b11 = = i].std(b15=0)
a1 = 0.01
b12 = np.zeros(b4, dtype=float)
for i in range(0, b4):
    b12[i] = (b11 = = i).sum() / b7
b13 = np.zeros((b8, b4), dtype=float)
for i in range(0, b8):
    for k in range(0, b4):
        b14 = np.log(b12[k])
        for j in range(0, b5):
            b14 += np.log(sp.stats.norm.pdf(X_test[i, j], b9[k, j], b10[k, j]) * 2 * a1)
        b13[i, k] = b14
print("\nProbability that the Model predicts the correct class class2:")
print((b13.argmax(b15 = 1) == b6).sum() / b8)