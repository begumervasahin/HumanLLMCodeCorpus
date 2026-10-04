import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import pickle
from mlxtend.data import loadlocal_mnist
def fonk1(b1, labels_path):
    return loadlocal_mnist(b1 = b1, labels_path=labels_path)
def fonk2(labels):
    return [label - 1 for label in labels if label in [1, 2]]
def fonk3(b18):
    b2 = b18.count(0)
    b3 = b18.count(1)
    b4 = b2 / (b2 + b3)
    b5 = b3 / (b2 + b3)
    return b4, b5, b2, b3
def fonk4(counts, b2, b3):
    for i in range(len(counts)):
        counts[i] /= [b2, b3]
    return counts
def fonk5(b21, b24, b22, b23, b4, b5):
    b6 = np.zeros((len(b24), len(b21)))
    for k, threshold in enumerate(b24):
        for i, x in enumerate(b21):
            b7 = sum(math.log(b23[j][0 if x[j] == 1 else 1]) for j in range(len(x)))
            b8 = sum(math.log(b22[j][0 if x[j] == 1 else 1]) for j in range(len(x)))
            b9 = (b7 * b4) / (b7 * b4 + b8 * b5)
            b6[k][i] = 0 if b9 <= threshold else 1
    return b6
def fonk6(b6, b19, b24):
    b10 = []
    b11 = []
    for i in range(len(b24)):
        b12 = fp = fn = tn = 0
        for j, y_true in enumerate(b19):
            b13 = b6[i][j]
            if b13 = = 0 and y_true == 0:
                b12 += 1
            elif b13 = = 1 and y_true == 1:
                tn += 1
            elif b13 = = 0 and y_true == 1:
                fp += 1
            elif b13 = = 1 and y_true == 0:
                fn += 1
        b14 = b12 / (b12 + fn)
        b15 = fp / (fp + tn)
        b10.append(b14)
        b11.append(b15)
        print(f"CASE {i+1} :-")
        print(f"Confusion Matrix:\n[[{b12} {fp}]\n [{fn} {tn}]]")
        print(f"The precision is: {b12 / (b12 + fp):.4f}")
        print(f"The recall is: {b14:.4f}")
    plt.plot(b11, b10)
    plt.ylabel("True Positive Rate")
    plt.xlabel("False Positive Rate")
    plt.title("ROC Curve")
    plt.show()
X_train, b16 = fonk1('./train-images.idx3-ubyte', './train-labels.idx1-ubyte')
X_test, b17 = fonk1('./t10k-images.idx3-ubyte', './t10k-labels.idx1-ubyte')
b18 = fonk2(b16)
b19 = fonk2(b17)
with open('./bintrain.pkl', 'rb') as f:
    b20 = pickle.load(f)
with open('./bintest.pkl', 'rb') as f:
    b21 = pickle.load(f)
b22 = np.load('./b22.npy')
b23 = np.load('./b23.npy')
b4, b5, b2, b3 = fonk3(b18)
b22 = fonk4(b22, b2, b3)
b23 = fonk4(b23, b2, b3)
print("The prior trouser is:", b4)
print("The prior pullover is:", b5)
b24 = [0.3, 0.4, 0.5, 0.6, 0.7]
b6 = fonk5(b21, b24, b22, b23, b4, b5)
print("Lengths:", len(b6), len(b19))
print(b6[:, 0], b6[:, 1])
fonk6(b6, b19, b24)