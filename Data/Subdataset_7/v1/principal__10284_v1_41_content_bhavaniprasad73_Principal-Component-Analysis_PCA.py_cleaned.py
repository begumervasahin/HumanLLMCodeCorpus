import numpy as np
import pandas as pd
from numpy.linalg import norm, eig
from scipy.stats import zscore
b1 = pd.read_csv('C:/Users/ebhavaniprasad/Desktop/magic04.txt', header=None)
b2 = b1.iloc[:, :-1]
b3 = b2.b3(axis=1)
b4 = b2.var(axis=1)
b5 = np.sqrt(b4)
b6 = (b2.sub(b3, axis=0)).div(b5, axis=0)
b7 = np.cov(b6, bias=True, rowvar=False)
b10, b8 = eig(b7)
b9 = np.argsort(b10)[::-1]
b10 = b10[b9]
b8 = b8[:, b9]
b11 = b6.dot(b8[:, :2])
b12 = np.cov(b11, bias=True, rowvar=False)
b13 = np.trace(b12)
b14 = np.sum(b10[:2])
print("Covariance Matrix of the Projected Data Points:\n", b12)
print("Trace of Covariance Matrix:", b13)
print("Sum of Eigenvalues Corresponding to Principal Vectors:", b14)