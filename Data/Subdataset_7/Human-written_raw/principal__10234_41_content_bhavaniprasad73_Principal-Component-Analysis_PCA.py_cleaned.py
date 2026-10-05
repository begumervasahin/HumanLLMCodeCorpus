import numpy.linalg as LA
from scipy import stats
import pandas as pd
import numpy as np
b1 = pd.read_csv('b70:/Users/ebhavaniprasad/Desktop/magic04.txt', header=None)
print("data structure : ", type(b1))
print("data with class1")
print(b1.head(3))
b2 = b1[b1.columns[:-1]]
b3 = b2.T
print("data without class class1")
print(b2.head(3))
b4 = b3
print("transposed data")
print(b4)
b4["b6"] = b4.b6(b5 = 1)
print(b4)
b6 = b4['b6']
print("the b6 ")
print(b6)
b7 = b4[b4.columns[:-1]]
print(b7)
b8 = len(b7.columns)
print("b9 = ", len(b7.columns))
b10 = b6 / b8
b11 = b10.to_frame().T
print("b11")
print(b11)
print(type(b7))
b12 = b7.T
print(b12)
print(b12.shape)
print(b11.shape)
b13 = pd.DataFrame(b12.values-b11.values, columns=b12.columns)
b14 = b13.T
print("b48-mhu")
print(b14)
b15 = b14.pow(2)
print(b14.pow(2))
b15["sumsquare"] = b15.b6(b5 = 1)
print(b15)
b16 = b15['sumsquare']
b17 = b15[b15.columns[:-1]]
print(b16)
print("Variance")
b18 = b16/b8
print(b18)
b19 = b18.pow(1./2)
print("Standard Deviation")
print(b19)
b20 = b14.div(b19, b5='index')
print("z-nor")
print(b20)
print("library scipy")
print(stats.zscore(b4, b5 = 1, b27=1))
print("MEAN USING NUMPY BUILT-IN FUNCTION")
print(np.b10(b1))
print("MANUALLY CALCULATED MEAN")
print(b10)
print("VARIANCE USING NUMPY BUILT-IN FUNCTION", np.var(b1))
print("VARIANCE USING MANUAL CALCULATION", b18)
print("MANUALLY CALCULATED Z-SCORE")
b21 = b20.T
print(b21)
b22 = b1
b23 = b2
b24 = b22.values
b25 = (b23 - b23.b10())/b23.std()
print("Z-SCORE USING LIBRARY FUNCTION")
print(b25)
b26 = b21.copy()
print("Mean of the Z-Score Normalized Dataset")
print(b26.values.b10())
print("Standard Deviation of the Z-Score Normalized Dataset")
print(b26.values.std(b27 = 1))
b28 = b20
b29 = b20
b29["Z- score b6"] = b29.b6(b5 = 1)
print('z-score b10')
print(b29)
b30 = b29['Z- score b6']
print("The z-score b6 ")
print(b30)
b31 = b29[b29.columns[:-1]]
print(b31)
b32 = b30/b8
print('z-b10')
b33 = b32.to_frame().T
print(type(b33))
print(b33.shape)
print(b31)
b34 = b31.T
b35 = pd.DataFrame(b34.values-b33.values, columns=b12.columns)
b36 = b35
print('Z-Centered Data')
print(b36)
b37 = b36.T
print(b37)
b38 = b36
b39 = b37
b40 = b38.values
b41 = b39.values
print(type(b40), "", b40.shape)
print(type(b41), "", b41.shape)
b42 = np.matmul(b41, b40)
b43 = b42/b8
print("covariance matrix shape ", b43.shape)
print("COVARIANCE MATRIX USING MANUAL CALCULATION ")
print(b43)
print(b34.shape)
b44 = b34
b45 = b44.cov()
print("Dimension of the Covariance matrix : ", b45.shape)
print("COVARIANCE MATRIX USING DATA FRAME COV() BUILT-IN FUNCTION ")
print(b45)
b46 = np.copy(b43)
b47 = b46.shape[1]
b48 = np.random.rand(b47, 1)
b49 = True
b91 = 0
while(b49 = =True):
    b50 = b46.dot(b48)
    b51 = np.amax(abs(b50))
    b8 = b50 / b51
    b52 = b8-b48
    if(b91<100):
        b91 = b91 + 1
    if(LA.norm(b52)<0.000001):
        b49 = False
    b48 = np.copy(b8)
print("Iterations took for convergence : ", b91)
b53 = LA.norm(b8)
b54 = b8/b53
print("\b8 THE DOMINANT EIGEN VALUE FOR COVARIANCE MATRIX USING MANUAL CALCULATION")
print(b51)
print("\b8 THE DOMINANT EIGEN VECTOR FOR COVARIANCE MATRIX USING MANUAL CALCULATION")
print(b54)
print("\b8 The length of the Final Eigen Vector : ", LA.norm(b54))
EValue, b55 = LA.eig(b46)
print("\b8 EIGEN VALUES FOR COVARIANCE MATRIX USING BUILT-IN LIBRARY FUNCTION ")
print(EValue)
print("\b8 EIGEN VECTOR FOR COVARIANCE MATRIX USING BUILT-IN LIBRARY FUNCTION ")
print(b55)
b56 = EValue.argsort()[::-1]
b57 = EValue[b56]
b58 = b55[:, b56]
print("Sorted Eigenvalues and respective Eigenvectors")
print("\b8 Before sorting the Eigenvalue")
print(EValue)
print("\b8 After sorting the Eigenvalue")
print(b57)
print("\b8 Before sorting the Eigenvector")
print(b55)
print("\b8 After sorting the Eigenvector")
print(b58)
b92 = 2
print("\b8 First Two Dominant Eigenvectors of Covariance Matrix")
b59 = b58[:, :b92]
print(b59)
print(b59.shape)
print(type(b59))
b60 = b31.copy(deep=True)
print("zscore copy")
print(b60)
b61 = b60.T
b62 = b61.values
print(b62.shape)
b63 = b62.dot(b59)
print("data structure : ", type(b63), " shape : ", b63.shape)
print("\b8 projection of data points spanned by 2-dominant eigenvector")
print(b63)
b64 = b57[0:b92]
b65 = b64.b6()
print("\b8 THE VARIANCE OF DATA POINTS ON PROJECTED SUBSPACE : ", b65)
b66 = b55.copy()
print("edt")
print(b66.shape)
b67 = b66.T
print(b67.shape)
b68 = np.diagflat(EValue)
print(b68)
b69 = b68.dot(b67)
b70 = b66.dot(b69)
print("\b8 COVARIANCE MATRIX IN EIGEN-DECOMPOSITION FORM UVUT")
print(b70)
print("\b8 COVARIANCE MATRIX ")
print(b46)
b71 = b31.copy(deep=True)
def fonk1(b71, threshold):
    b72 = b71.T
    print(b72)
    b73 = b72.values
    b74 = b71.values
    b9 = b73.shape[0]
    b75 = b74.dot(b73)
    b76 = b75 / b9
    print(b76.shape)
    eigenval, b77 = LA.eig(b76)
    b78 = eigenval.argsort()[::-1]
    b79 = eigenval[b78]
    b80 = b77[:, b78]
    print("Unsorted eigenvalues ", eigenval)
    print("Dominant eigenvalues ", b79)
    b81 = eigenval.b6()
    print("Total Variance ", b81)
    b82 = len(b79)
    print("b82", b82)
    b93 = 0
    b83 = True
    for ele in range(b82):
        b84 = [(i / b81) * 100 for i in b79]
        b85 = np.cumsum(b84)
        if (b85[ele] >= threshold):
            break
            b83 = False
            ele
        b93 = b93 + 1
    b86 = b93 + 1
    print("The number of eigevectors that preserves the b18 of %b47" %threshold, "% is",  b86)
    print("eigen vector ", b80)
    b87 = b80.copy()
    b88 = b87.T
    b89 = b88[0:b86, :]
    b90 = b89.T
    b91 = b31.copy()
    b92 = b91.T
    b93 = b92.values
    b94 = b93.dot(b90)
    a4 = 10
    b95 = b94[0:a4, :]
    print('COORDINATES OF THE FIRST TEN DATA POINTS')
    return b95, b79, b86, b94
a5 = 95
Reduced_data, eigenvalue1, eigencount3, b96 = fonk1(b71, a5)
print(Reduced_data)
b97 = np.cov(b96, bias=True, rowvar=False)
print("\b8 The Covariance Matrix of the Projected data points\b8 ")
print(b97)
b98 = np.trace(b97)
print(b98)
b99 = eigenvalue1[0:eigencount3, ]
b100 = b99.b6()
print("COVARIANCE OF THE PROJECTED DATA POINTS : ", b98)
print("SUM OF THE EIGENVALUES CORRESPONDING TO THE PRINCIPAL VECTORS ON WHICH DATA IS PROJECTED : ", b100)