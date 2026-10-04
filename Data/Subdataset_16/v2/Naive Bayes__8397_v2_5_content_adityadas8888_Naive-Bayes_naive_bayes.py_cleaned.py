import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm
def fonk1(tsize0, tsize1):
    mean1, b1 = [1, 0], [0, 1]
    Sigma1, b2 = [[1, 0.75], [0.75, 1]], [[1, 0.75], [0.75, 1]]
    x1, b3 = np.random.multivariate_normal(mean1, Sigma1, tsize0).T
    x2, b4 = np.random.multivariate_normal(b1, b2, tsize1).T
    x3, b5 = np.random.multivariate_normal(mean1, Sigma1, 100).T
    x4, b6 = np.random.multivariate_normal(b1, b2, 100).T
    meanx0, b7 = np.mean(x1), np.mean(b3)
    stdx0, b8 = np.std(x1), np.std(b3)
    meanx1, b9 = np.mean(x2), np.mean(b4)
    stdx1, b10 = np.std(x2), np.std(b4)
    b11 = pd.DataFrame({
        'b29': np.concatenate((x1, x2)),
        'b30': np.concatenate((b3, b4)),
        'label': np.concatenate((np.zeros(len(x1)), np.ones(len(x2))))
    })
    b12 = pd.DataFrame({
        'b29': np.concatenate((x3, x4)),
        'b30': np.concatenate((b5, b6)),
        'actual': np.concatenate((np.zeros(len(x3)), np.ones(len(x4))))
    })
    b13 = tsize0 / (tsize0 + tsize1)
    b14 = tsize1 / (tsize0 + tsize1)
    b15 = norm.pdf(b12['b29'], loc=meanx0, scale=stdx0) * norm.pdf(b12['b30'], loc=b7, scale=b8)
    b16 = norm.pdf(b12['b29'], loc=meanx1, scale=stdx1) * norm.pdf(b12['b30'], loc=b9, scale=b10)
    b17 = b15 * b13
    b18 = b16 * b14
    b12['b17'] = b17
    b12['b18'] = b18
    b12['predicted'] = np.where(b17 > b18, 0, 1)
    b12['b28'] = np.where(b17 > b18, 'r', 'b')
    b19 = np.sum((b12['predicted'] == 0) & (b12['actual'] == 0))
    b20 = np.sum((b12['predicted'] == 1) & (b12['actual'] == 1))
    b21 = np.sum((b12['predicted'] == 0) & (b12['actual'] == 1))
    b22 = np.sum((b12['predicted'] == 1) & (b12['actual'] == 0))
    b23 = (b20 + b19) / (b20 + b21 + b22 + b19)
    b24 = 1 - b23
    b25 = b20 / (b20 + b22)
    b26 = b20 / (b20 + b21)
    print(f"Accuracy: {b23:.3f}, Error Rate: {b24:.3f}, Recall: {b25:.3f}, Precision: {b26:.3f}")
    print(f"True Positive: {b20}, True Negative: {b19}, False Positive: {b21}, False Negative: {b22}")
    plt.figure(b27 = (10, 10))
    plt.scatter(b12['b29'], b12['b30'], b28 = b12['b28'], alpha=0.5, edgecolor='k', marker="b29")
    plt.title('Naive Bayes Classification Results')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    return b23
def fonk2(A, B):
    b29 = np.append(A, 1)
    b30 = np.append(B, 1)
    plt.plot(b29, b30, b28 = 'blue')
    plt.xlabel('FPR', b31 = 16)
    plt.ylabel('TPR', b31 = 16)
    fonk3(b29, b30)
    plt.title('ROC Curve')
    plt.show()
def fonk3(b29, b30):
    b32 = np.trapz(b30, b29)
    print(f"Area under the curve is {b32:.3f}")
def fonk4():
    b23 = fonk1(500, 500)
    print("ROC Curve and AUC calculation are not demonstrated here.")
if b33 = = "__main__":
    fonk4()