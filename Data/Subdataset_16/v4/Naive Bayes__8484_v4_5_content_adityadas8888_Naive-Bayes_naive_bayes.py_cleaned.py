import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm
import math
def fonk1(train_size_class0, train_size_class1):
    b1 = [1, 0]
    b2 = [0, 1]
    b3 = [[1, 0.75], [0.75, 1]]
    x_train_class0, b4 = np.random.multivariate_normal(b1, b3, train_size_class0).T
    x_train_class1, b5 = np.random.multivariate_normal(b2, b3, train_size_class1).T
    x_test_class0, b6 = np.random.multivariate_normal(b1, b3, 100).T
    x_test_class1, b7 = np.random.multivariate_normal(b2, b3, 100).T
    mean_x_class0, b8 = np.mean(x_train_class0), np.mean(b4)
    std_x_class0, b9 = np.std(x_train_class0), np.std(b4)
    mean_x_class1, b10 = np.mean(x_train_class1), np.mean(b5)
    std_x_class1, b11 = np.std(x_train_class1), np.std(b5)
    b12 = pd.DataFrame({
        'x': np.concatenate((x_train_class0, x_train_class1)),
        'y': np.concatenate((b4, b5)),
        'label': np.concatenate((np.zeros(len(x_train_class0)), np.ones(len(x_train_class1))))
    })
    b13 = pd.DataFrame({
        'x': np.concatenate((x_test_class0, x_test_class1)),
        'y': np.concatenate((b6, b7)),
        'actual': np.concatenate((np.zeros(len(x_test_class0)), np.ones(len(x_test_class1))))
    })
    b14 = train_size_class0 / (train_size_class0 + train_size_class1)
    b15 = train_size_class1 / (train_size_class0 + train_size_class1)
    b16 = norm.pdf(b13['x'], loc=mean_x_class0, scale=std_x_class0) * norm.pdf(b13['y'], loc=b8, scale=b9)
    b17 = norm.pdf(b13['x'], loc=mean_x_class1, scale=std_x_class1) * norm.pdf(b13['y'], loc=b10, scale=b11)
    b18 = b16 * b14
    b19 = b17 * b15
    b13['post_class0'] = b18
    b13['post_class1'] = b19
    b13['predicted'] = np.where(b18 > b19, 0, 1)
    b13['b29'] = np.where(b18 > b19, 'r', 'b')
    b20 = np.sum((b13['predicted'] == 0) & (b13['actual'] == 0))
    b21 = np.sum((b13['predicted'] == 1) & (b13['actual'] == 1))
    b22 = np.sum((b13['predicted'] == 0) & (b13['actual'] == 1))
    b23 = np.sum((b13['predicted'] == 1) & (b13['actual'] == 0))
    b24 = (b21 + b20) / (b21 + b22 + b23 + b20)
    b25 = 1 - b24
    b26 = b21 / (b21 + b23)
    b27 = b21 / (b21 + b22)
    print(f"Accuracy: {b24}")
    print(f"Error Rate: {b25}")
    print(f"Recall: {b26}")
    print(f"Precision: {b27}")
    print(f"True Positives: {b21}, True Negatives: {b20}")
    print(f"False Positives: {b22}, False Negatives: {b23}")
    plt.figure(b28 = (10, 10))
    plt.scatter(b13['x'], b13['y'], b29 = b13['b29'], alpha=0.5, edgecolor='k', marker="x")
    plt.show()
    return b24
def fonk2(b30, b31):
    b30 = np.append(b30, 1)
    b31 = np.append(b31, 1)
    plt.plot(b30, b31, b29 = 'blue')
    plt.xlabel('False Positive Rate (FPR)', b32 = 16)
    plt.ylabel('True Positive Rate (TPR)', b32 = 16)
    plt.title('ROC Curve')
    b33 = np.trapz(b31, b30)
    print(f"Area Under the Curve (AUC): {b33}")
    plt.show()
def fonk3():
    b24 = fonk1(500, 500)
    print("Accuracy of the model:", b24)
if b34 = = "__main__":
    fonk3()