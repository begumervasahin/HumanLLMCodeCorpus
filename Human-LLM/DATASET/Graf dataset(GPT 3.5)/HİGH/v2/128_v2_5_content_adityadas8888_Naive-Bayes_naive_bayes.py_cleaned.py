import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from scipy.stats import norm
def fonk1(tsize0, tsize1):
    b1 = [1, 0]
    b2 = [0, 1]
    b3 = [[1, 0.75], [0.75, 1]]
    b4 = [[1, 0.75], [0.75, 1]]
    x1, b5 = np.random.multivariate_normal(b1, b3, tsize0).T
    x2, b6 = np.random.multivariate_normal(b2, b4, tsize1).T
    x3, b7 = np.random.multivariate_normal(b1, b3, 100).T
    x4, b8 = np.random.multivariate_normal(b2, b4, 100).T
    b9 = pd.DataFrame({'x': np.concatenate([x1, x2]),
                               'y': np.concatenate([b5, b6]),
                               'label': np.concatenate([np.zeros(tsize0), np.ones(tsize1)])})
    b10 = pd.DataFrame({'x': np.concatenate([x3, x4]),
                              'y': np.concatenate([b7, b8]),
                              'actual': np.concatenate([np.zeros(100), np.ones(100)])})
    return b9, b10
def fonk2(b9, b10):
    meanx0, b11 = b9[b9['label'] == 0][['x', 'y']].mean()
    meanx1, b12 = b9[b9['label'] == 1][['x', 'y']].mean()
    stdx0, b13 = b9[b9['label'] == 0][['x', 'y']].std()
    stdx1, b14 = b9[b9['label'] == 1][['x', 'y']].std()
    return meanx0, b11, stdx0, b13, meanx1, b12, stdx1, b14
def fonk3(b10, meanx0, b11, stdx0, b13, meanx1, b12, stdx1, b14):
    b15 = len(b9[b9['label'] == 0]) / len(b9)
    b16 = len(b9[b9['label'] == 1]) / len(b9)
    b10['post0'] = norm.pdf(b10['x'], b17 = meanx0, scale=stdx0) * norm.pdf(b10['y'], b17=b11, scale=b13) * b15
    b10['post1'] = norm.pdf(b10['x'], b17 = meanx1, scale=stdx1) * norm.pdf(b10['y'], b17=b12, scale=b14) * b16
    b10['predicted'] = np.where(b10['post0'] > b10['post1'], 0, 1)
    b10['b27'] = np.where(b10['predicted'] == 0, 'r', 'b')
    return b10
def fonk4(b10):
    b18 = ((b10['predicted'] == 1) & (b10['actual'] == 1)).sum()
    b19 = ((b10['predicted'] == 0) & (b10['actual'] == 0)).sum()
    b20 = ((b10['predicted'] == 1) & (b10['actual'] == 0)).sum()
    b21 = ((b10['predicted'] == 0) & (b10['actual'] == 1)).sum()
    b22 = (b18 + b19) / len(b10)
    b23 = 1 - b22
    b24 = b18 / (b18 + b21)
    b25 = b18 / (b18 + b20)
    print("Accuracy: {:.4f}".format(b22))
    print("Error Rate: {:.4f}".format(b23))
    print("Recall: {:.4f}".format(b24))
    print("Precision: {:.4f}".format(b25))
    return b22
def fonk5(b10):
    plt.figure(b26 = (10, 10))
    plt.scatter(b10['x'], b10['y'], b27 = b10['b27'], alpha=0.5, edgecolor='k', marker="x")
    plt.show()
def fonk6():
    b9, b10 = fonk1(500, 500)
    meanx0, b11, stdx0, b13, meanx1, b12, stdx1, b14 = fonk2(b9, b10)
    b10 = fonk3(b10, meanx0, b11, stdx0, b13, meanx1, b12, stdx1, b14)
    b22 = fonk4(b10)
    fonk5(b10)
if b28 = = "__main__":
    fonk6()