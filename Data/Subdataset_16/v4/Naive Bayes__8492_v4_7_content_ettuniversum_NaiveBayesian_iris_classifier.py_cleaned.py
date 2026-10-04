import numpy as np
import scipy.stats as stats
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
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
X_train, X_test, b11, b6 = train_test_split(b2, b3, random_state=42)
b7 = len(X_train)
b8 = len(X_test)
print(f"\n{b7} samples in the training set")
print(f"{b8} samples in the test set")
b9 = np.zeros((b4, b5), dtype=float)
b10 = np.zeros((b4, b5), dtype=float)
for class_index in range(b4):
    b9[class_index] = X_train[b11 = = class_index].mean(axis=0)
    b10[class_index] = X_train[b11 = = class_index].std(axis=0)
a1 = 0.01
b12 = np.zeros(b4, dtype=float)
for class_index in range(b4):
    b12[class_index] = (b11 = = class_index).sum() / b7
b13 = np.zeros((b8, b4), dtype=float)
for i in range(b8):
    for class_index in range(b4):
        b14 = np.log(b12[class_index])
        for feature_index in range(b5):
            b14 += np.log(stats.norm.pdf(X_test[i, feature_index], b9[class_index, feature_index], b10[class_index, feature_index]) + a1)
        b13[i, class_index] = b14
b15 = (b13.argmax(axis=1) == b6).sum() / b8
print("\nProbability that the model predicts the correct class class2:")
print(b15)
print()