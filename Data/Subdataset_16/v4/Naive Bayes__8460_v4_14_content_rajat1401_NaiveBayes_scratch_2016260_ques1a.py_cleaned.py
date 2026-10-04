import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import pickle
from mlxtend.data import loadlocal_mnist
X_train, b1 = loadlocal_mnist(images_path='./train-images.idx3-ubyte', labels_path='./train-labels.idx1-ubyte')
X_test, b2 = loadlocal_mnist(images_path='./t10k-images.idx3-ubyte', labels_path='./t10k-labels.idx1-ubyte')
b3 = [label - 1 for label in b1 if label in [1, 2]]
b4 = [label - 1 for label in b2 if label in [1, 2]]
with open('./bintrain.pkl', 'rb') as f:
    b5 = pickle.load(f)
with open('./bintest.pkl', 'rb') as f:
    b6 = pickle.load(f)
b7 = np.load('./b7.mat')
b8 = np.load('./b8.mat')
b9 = b3.count(0)
b10 = b3.count(1)
b11 = b9 / (b9 + b10)
b12 = b10 / (b9 + b10)
for i in range(len(b7)):
    b7[i] /= [b9, b10]
    b8[i] /= [b9, b10]
print("The prior trouser is:", b11)
print("The prior pullover is:", b12)
b13 = [0.3, 0.4, 0.5, 0.6, 0.7]
b14 = np.zeros((len(b13), len(b6)))
for k, threshold in enumerate(b13):
    for i, x in enumerate(b6):
        b15 = sum(math.log(b8[j][0 if x[j] == 1 else 1]) for j in range(len(x)))
        b16 = sum(math.log(b7[j][0 if x[j] == 1 else 1]) for j in range(len(x)))
        b17 = (b15 * b11) / (b15 * b11 + b16 * b12)
        b14[k][i] = 0 if b17 <= threshold else 1
print("Lengths:", len(b14), len(b4))
print(b14[:, 0], b14[:, 1])
b18 = []
b19 = []
for i in range(len(b13)):
    b20 = fp = fn = tn = 0
    for j, y_true in enumerate(b4):
        b21 = b14[i][j]
        if b21 = = 0 and y_true == 0:
            b20 += 1
        elif b21 = = 1 and y_true == 1:
            tn += 1
        elif b21 = = 0 and y_true == 1:
            fp += 1
        elif b21 = = 1 and y_true == 0:
            fn += 1
    b22 = b20 / (b20 + fn)
    b23 = fp / (fp + tn)
    b18.append(b22)
    b19.append(b23)
    print(f"CASE {i+1} :-")
    print(f"Confusion Matrix:\n[[{b20} {fp}]\n [{fn} {tn}]]")
    print(f"The precision is: {b20 / (b20 + fp)}")
    print(f"The recall is: {b22}")
plt.plot(b19, b18)
plt.ylabel("True Positive Rate")
plt.xlabel("False Positive Rate")
plt.title("ROC Curve")
plt.show()