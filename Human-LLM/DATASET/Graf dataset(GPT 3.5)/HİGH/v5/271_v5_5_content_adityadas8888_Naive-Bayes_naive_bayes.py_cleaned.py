import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from scipy.stats import norm
def fonk1(tsize0, tsize1):
    b1 = [1, 0]
    b2 = [0, 1]
    b3 = Sigma2 = [[1, 0.75], [0.75, 1]]
    x1, b4 = np.random.multivariate_normal(b1, b3, tsize0).T
    x2, b5 = np.random.multivariate_normal(b2, Sigma2, tsize1).T
    return x1, b4, x2, b5
def fonk2(x1, b4, x2, b5):
    b6 = pd.DataFrame({'x': np.concatenate([x1, x2]), 'y': np.concatenate([b4, b5]), 'label': np.concatenate([np.zeros(len(x1)), np.ones(len(x2))])})
    b7 = pd.DataFrame({'x': np.concatenate([x1, x2]), 'y': np.concatenate([b4, b5]), 'actual': np.concatenate([np.zeros(len(x1)), np.ones(len(x2))])})
    b8 = len(x1) / (len(x1) + len(x2))
    b9 = len(x2) / (len(x1) + len(x2))
    meanx0, b10 = np.mean(x1), np.mean(b4)
    meanx1, b11 = np.mean(x2), np.mean(b5)
    stdx0, b12 = np.std(x1), np.std(b4)
    stdx1, b13 = np.std(x2), np.std(b5)
    b14 = norm.pdf(b7['x'], loc=meanx0, scale=stdx0) * norm.pdf(b7['y'], loc=b10, scale=b12)
    b15 = norm.pdf(b7['x'], loc=meanx1, scale=stdx1) * norm.pdf(b7['y'], loc=b11, scale=b13)
    post0, b16 = b14 * b8, b15 * b9
    b7['post0'], b7['b16'] = post0, b16
    b7['pred'] = b7[['post0', 'b16']].max(b17 = 1)
    b7['predicted'] = np.where(b7['pred'] == b16, 0, 1)
    b7['b26'] = np.where(b7['pred'] == b16, 'r', 'b')
    return b7
def fonk3(b7):
    b18 = np.sum((b7['predicted'] == 1) & (b7['actual'] == 1))
    b19 = np.sum((b7['predicted'] == 0) & (b7['actual'] == 0))
    b20 = np.sum((b7['predicted'] == 1) & (b7['actual'] == 0))
    b21 = np.sum((b7['predicted'] == 0) & (b7['actual'] == 1))
    b22 = (b18 + b19) / (b18 + b20 + b21 + b19)
    b23 = 1 - b22
    b24 = b18 / (b18 + b21)
    b25 = b18 / (b18 + b20)
    print("Accuracy: {:.2f}, Error Rate: {:.2f}, Recall: {:.2f}, Precision: {:.2f}".format(b22, b23, b24, b25))
    print("True Positive: {}, True Negative: {}, False Positive: {}, False Negative: {}".format(b18, b19, b20, b21))
    return b22
def fonk4(b7):
    plt.scatter(b7['x'], b7['y'], b26 = b7['b26'], alpha=0.5, edgecolor='k', marker='x')
    plt.show()
def fonk5():
    x1, b4, x2, b5 = fonk1(500, 500)
    b7 = fonk2(x1, b4, x2, b5)
    b22 = fonk3(b7)
    fonk4(b7)
if b27 = = "__main__":
    fonk5()