import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm
def fonk1(mean, b11, size):
    x, b1 = np.random.multivariate_normal(mean, b11, size).T
    return x, b1
def fonk2(b19):
    b2 = np.sum((b19['predicted'] == 0) & (b19['actual'] == 0))
    b3 = np.sum((b19['predicted'] == 1) & (b19['actual'] == 1))
    b4 = np.sum((b19['predicted'] == 0) & (b19['actual'] == 1))
    b5 = np.sum((b19['predicted'] == 1) & (b19['actual'] == 0))
    b6 = (b3 + b2) / (b3 + b4 + b5 + b2)
    b7 = 1 - b6
    b8 = b3 / (b3 + b5)
    b9 = b3 / (b3 + b4)
    return b6, b7, b8, b9, b3, b2, b4, b5
def fonk3(tsize0, tsize1):
    mean1, b10 = [1, 0], [0, 1]
    b11 = [[1, 0.75], [0.75, 1]]
    x1, b12 = fonk1(mean1, b11, tsize0)
    x2, b13 = fonk1(b10, b11, tsize1)
    x3, b14 = fonk1(mean1, b11, 100)
    x4, b15 = fonk1(b10, b11, 100)
    meanx0, meany0, stdx0, b16 = np.mean(x1), np.mean(b12), np.std(x1), np.std(b12)
    meanx1, meany1, stdx1, b17 = np.mean(x2), np.mean(b13), np.std(x2), np.std(b13)
    b18 = pd.DataFrame({'x': np.concatenate((x1, x2)), 'b1': np.concatenate((b12, b13)), 'label': np.concatenate((np.zeros(len(x1)), np.ones(len(x2))))})
    b19 = pd.DataFrame({'x': np.concatenate((x3, x4)), 'b1': np.concatenate((b14, b15)), 'actual': np.concatenate((np.zeros(len(x3)), np.ones(len(x4))))})
    prob0, b20 = tsize0 / (tsize0 + tsize1), tsize1 / (tsize0 + tsize1)
    b21 = norm.pdf(b19['x'], loc=meanx0, scale=stdx0) * norm.pdf(b19['b1'], loc=meany0, scale=b16)
    b22 = norm.pdf(b19['x'], loc=meanx1, scale=stdx1) * norm.pdf(b19['b1'], loc=meany1, scale=b17)
    post0, b23 = b21 * prob0, b22 * b20
    b19['post0'], b19['b23'] = post0, b23
    b19['predicted'] = np.where(post0 > b23, 0, 1)
    b19['b25'] = np.where(post0 > b23, 'r', 'b')
    b6, b7, b8, b9, b3, b2, b4, b5 = fonk2(b19)
    print(f"Accuracy: {b6:.3f}, Error Rate: {b7:.3f}, Recall: {b8:.3f}, Precision: {b9:.3f}")
    print(f"True Positive: {b3}, True Negative: {b2}, False Positive: {b4}, False Negative: {b5}")
    plt.figure(b24 = (10, 10))
    plt.scatter(b19['x'], b19['b1'], b25 = b19['b25'], alpha=0.5, edgecolor='k', marker="x")
    plt.title('Naive Bayes Classification Results')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    return b6
def fonk4(A, B):
    x, b1 = np.append(A, 1), np.append(B, 1)
    plt.plot(x, b1, b25 = 'blue')
    plt.xlabel('FPR', b26 = 16)
    plt.ylabel('TPR', b26 = 16)
    fonk5(x, b1)
    plt.title('ROC Curve')
    plt.show()
def fonk5(x, b1):
    b27 = np.trapz(b1, x)
    print(f"Area under the curve is {b27:.3f}")
def fonk6():
    b6 = fonk3(500, 500)
    print("ROC Curve and AUC calculation are not demonstrated here.")
if b28 = = "__main__":
    fonk6()