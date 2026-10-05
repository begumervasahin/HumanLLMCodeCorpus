import numpy as np
import pandas as pd
from numpy.linalg import norm, eig
from scipy.stats import zscore
b1 = 'C:/Users/ebhavaniprasad/Desktop/magic04.txt'
b2 = pd.read_csv(b1, header=None)
b3 = b2.iloc[:, :-1]
b4 = b3.mean(axis=1)
b5 = b3.var(axis=1)
b6 = np.sqrt(b5)
b7 = (b3.sub(b4, axis=0)).div(b6, axis=0)
b8 = np.cov(b7, bias=True, rowvar=False)
eigen_values, b9 = eig(b8)
b10 = np.argsort(eigen_values)[::-1]
b11 = eigen_values[b10]
b12 = b9[:, b10]
b13 = b7.dot(b12[:, :2])
b14 = np.cov(b13, bias=True, rowvar=False)
b15 = np.trace(b14)
b16 = np.sum(b11[:2])
print("Covariance Matrix of the Projected Data Points:\n", b14)
print("Trace of Covariance Matrix:", b15)
print("Sum of Eigenvalues Corresponding to the First Two Principal Vectors:", b16)