import numpy as np
import pandas as pd
from numpy.linalg import eig
from scipy.stats import zscore
b1 = 'C:/Users/ebhavaniprasad/Desktop/magic04.txt'
b2 = pd.read_csv(b1, header=None)
b3 = b2.iloc[:, :-1]
b4 = zscore(b3, axis=0)
b5 = np.cov(b4, bias=True, rowvar=False)
eigen_values, b6 = eig(b5)
b7 = np.argsort(eigen_values)[::-1]
b8 = eigen_values[b7]
b9 = b6[:, b7]
b10 = b4.dot(b9[:, :2])
b11 = np.cov(b10, bias=True, rowvar=False)
b12 = np.trace(b11)
b13 = np.sum(b8[:2])
print("Covariance Matrix of the Projected Data Points:\n", b11)
print("Trace of Covariance Matrix:", b12)
print("Sum of Eigenvalues Corresponding to the First Two Principal Vectors:", b13)