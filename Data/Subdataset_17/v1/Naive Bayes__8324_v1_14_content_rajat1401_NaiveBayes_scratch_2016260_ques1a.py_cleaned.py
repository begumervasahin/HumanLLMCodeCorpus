import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import pickle
from mlxtend.data import loadlocal_mnist
X_train, y_train = loadlocal_mnist(images_path='./train-images.idx3-ubyte', labels_path='./train-labels.idx1-ubyte')
X_test, y_test = loadlocal_mnist(images_path='./t10k-images.idx3-ubyte', labels_path='./t10k-labels.idx1-ubyte')
y_train = [label - 1 for label in y_train if label in [1, 2]]
y_test = [label - 1 for label in y_test if label in [1, 2]]
with open('./bintrain.pkl', 'rb') as f:
    x_train = pickle.load(f)
with open('./bintest.pkl', 'rb') as f:
    x_test = pickle.load(f)
counttrain0 = np.load('./counttrain0.mat')
counttrain1 = np.load('./counttrain1.mat')
a = y_train.count(0)
b = y_train.count(1)
prior_trouser = a / (a + b)
prior_pullover = b / (a + b)
for i in range(len(counttrain0)):
    counttrain0[i][0] /= a
    counttrain1[i][0] /= a
    counttrain0[i][1] /= b
    counttrain1[i][1] /= b
print("The prior trouser is:", prior_trouser)
print("The prior pullover is:", prior_pullover)
thresholds = [0.3, 0.4, 0.5, 0.6, 0.7]
y_pred = np.zeros((len(thresholds), len(x_test)))
for k, threshold in enumerate(thresholds):
    for i in range(len(x_test)):
        pdt1 = pdt2 = 0
        for j in range(len(x_test[0])):
            if x_test[i][j] == 1:
                pdt1 += math.log(counttrain1[j][0])
                pdt2 += math.log(counttrain1[j][1])
            else:
                pdt1 += math.log(counttrain0[j][0])
                pdt2 += math.log(counttrain0[j][1])
        prob0 = (pdt1 * prior_trouser) / (pdt1 * prior_trouser + pdt2 * prior_pullover)
        y_pred[k][i] = 0 if prob0 <= threshold else 1
print("Lengths:", len(y_pred), len(y_test))
print(y_pred[:, 0], y_pred[:, 1])
tp_array = []
fp_array = []
for i in range(len(thresholds)):
    conf_matrix = np.zeros((2, 2))
    tp = fp = fn = tn = 0
    for j in range(len(y_test)):
        if y_pred[i][j] == 0 and y_test[j] == 0:
            tp += 1
        elif y_pred[i][j] == 1 and y_test[j] == 1:
            tn += 1
        elif y_pred[i][j] == 0 and y_test[j] == 1:
            fp += 1
        elif y_pred[i][j] == 1 and y_test[j] == 0:
            fn += 1
    conf_matrix[0][0] = tp
    conf_matrix[1][1] = tn
    conf_matrix[0][1] = fp
    conf_matrix[1][0] = fn
    tp_array.append(tp / (tp + fn))
    fp_array.append(fp / (fp + tn))
    print(f"CASE {i + 1} :-")
    print(conf_matrix)
    print("The precision is:", tp / (tp + fp))
    print("The recall is:", tp / (tp + fn))
plt.plot(fp_array, tp_array)
plt.ylabel("True Positive Rate")
plt.xlabel("False Positive Rate")
plt.title("ROC Curve")
plt.show()