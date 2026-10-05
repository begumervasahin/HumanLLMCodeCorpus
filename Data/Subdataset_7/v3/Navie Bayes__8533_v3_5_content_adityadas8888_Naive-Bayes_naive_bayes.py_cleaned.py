import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
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
                               'b17': np.concatenate([np.zeros(tsize0), np.ones(tsize1)])})
    b10 = pd.DataFrame({'x': np.concatenate([x3, x4]),
                              'y': np.concatenate([b7, b8]),
                              'actual': np.concatenate([np.zeros(100), np.ones(100)])})
    return b9, b10
def fonk2(b9):
    b11 = {}
    for b17 in b9['b17'].unique():
        b12 = b9[b9['b17'] == b17][['x', 'y']]
        b11[b17] = (b12.mean(), b12.b15())
    return b11
def fonk3(b10, b11):
    b13 = len(b9[b9['b17'] == 0]) / len(b9)
    b14 = len(b9[b9['b17'] == 1]) / len(b9)
    for b17 in b11:
        mean, b15 = b11[b17]
        b10[f'post{b17}'] = norm.pdf(b10['x'], b16 = mean[0], scale=b15[0]) * \
                                    norm.pdf(b10['y'], b16 = mean[1], scale=b15[1]) * \
                                    (b13 if b17 = = 0 else b14)
    b10['predicted'] = np.where(b10['post0'] > b10['post1'], 0, 1)
    b10['b23'] = np.where(b10['predicted'] == 0, 'r', 'b')
    return b10
def fonk4(b10):
    b18 = pd.crosstab(b10['predicted'], b10['actual'])
    b19 = np.mean(b10['predicted'] == b10['actual'])
    b20 = b18.iloc[1, 1] / (b18.iloc[1, 1] + b18.iloc[1, 0])
    b21 = b18.iloc[1, 1] / (b18.iloc[1, 1] + b18.iloc[0, 1])
    print("Accuracy:", b19)
    print("Recall:", b20)
    print("Precision:", b21)
    return b19
def fonk5(b10):
    plt.figure(b22 = (10, 10))
    plt.scatter(b10['x'], b10['y'], b23 = b10['b23'], alpha=0.5, edgecolor='k', marker="x")
    plt.show()
def fonk6():
    b9, b10 = fonk1(500, 500)
    b11 = fonk2(b9)
    b10 = fonk3(b10, b11)
    fonk4(b10)
    fonk5(b10)
if b24 = = "__main__":
    fonk6()