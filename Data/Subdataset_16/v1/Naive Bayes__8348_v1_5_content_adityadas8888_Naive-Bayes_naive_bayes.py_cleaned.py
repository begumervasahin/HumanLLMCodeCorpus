import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics
import math
from scipy.stats import norm
import matplotlib.patches as mpatches
def fonk1(tsize0, tsize1):
    b1 = [1, 0]
    b2 = [0, 1]
    b3 = [[1, 0.75], [0.75, 1]]
    b4 = [[1, 0.75], [0.75, 1]]
    x1, b5 = np.random.multivariate_normal(b1, b3, tsize0).T
    x2, b6 = np.random.multivariate_normal(b2, b4, tsize1).T
    x3, b7 = np.random.multivariate_normal(b1, b3, 100).T
    x4, b8 = np.random.multivariate_normal(b2, b4, 100).T
    meanx0, b9 = np.mean(x1), np.mean(b5)
    stdx0, b10 = np.std(x1), np.std(b5)
    meanx1, b11 = np.mean(x2), np.mean(b6)
    stdx1, b12 = np.std(x2), np.std(b6)
    b13 = pd.DataFrame({
        'b31': np.concatenate((x1, x2)),
        'b32': np.concatenate((b5, b6)),
        'label': np.concatenate((np.zeros(len(x1)), np.ones(len(x2))))
    })
    b14 = pd.DataFrame({
        'b31': np.concatenate((x3, x4)),
        'b32': np.concatenate((b7, b8)),
        'actual': np.concatenate((np.zeros(len(x3)), np.ones(len(x4))))
    })
    b15 = tsize0 / (tsize0 + tsize1)
    b16 = tsize1 / (tsize0 + tsize1)
    b17 = norm.pdf(b14['b31'], loc=meanx0, scale=stdx0) * norm.pdf(b14['b32'], loc=b9, scale=b10)
    b18 = norm.pdf(b14['b31'], loc=meanx1, scale=stdx1) * norm.pdf(b14['b32'], loc=b11, scale=b12)
    b19 = b17 * b15
    b20 = b18 * b16
    b14['b19'] = b19
    b14['b20'] = b20
    b14['predicted'] = np.where(b19 > b20, 0, 1)
    b14['b30'] = np.where(b19 > b20, 'r', 'b')
    b21 = np.sum((b14['predicted'] == 0) & (b14['actual'] == 0))
    b22 = np.sum((b14['predicted'] == 1) & (b14['actual'] == 1))
    b23 = np.sum((b14['predicted'] == 0) & (b14['actual'] == 1))
    b24 = np.sum((b14['predicted'] == 1) & (b14['actual'] == 0))
    b25 = (b22 + b21) / (b22 + b23 + b24 + b21)
    b26 = 1 - b25
    b27 = b22 / (b22 + b24)
    b28 = b22 / (b22 + b23)
    print(f"b25 is {b25}, error rate is {b26}, b27 is {b27}, b28 is {b28},"
          f" True positive is {b22}, true negative is {b21}, False positive is {b23}, False negative is {b24}")
    b29 = plt.figure(figsize=(10, 10))
    plt.scatter(b14['b31'], b14['b32'], b30 = b14['b30'], alpha=0.5, edgecolor='k', marker="b31")
    plt.show()
    return b25
def fonk2(A, B):
    b31 = np.array(A)
    b32 = np.array(B)
    b31 = np.append(b31, 1)
    b32 = np.append(b32, 1)
    plt.plot(b31, b32, b30 = 'blue')
    plt.xlabel('FPR', b33 = 16)
    plt.ylabel('TPR', b33 = 16)
    fonk3(b31, b32)
    plt.show()
def fonk3(b31, b32):
    b34 = np.trapz(b32, b31)
    print("Area under the curve is", b34)
def fonk4():
    b25 = fonk1(500, 500)
    print("ROC Curve and AUC calculation are not demonstrated here.")
if b35 = = "__main__":
    fonk4()