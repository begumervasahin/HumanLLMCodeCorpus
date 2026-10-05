import numpy as np
import pandas as pd
def fonk1(b8):
    b1 = (b8 - np.mean(b8)) / np.std(b8)
    b2 = np.dot(b1.T, b1)
    b3 = np.identity(b8.shape[1])
    for _ in range(40):
        Q, b4 = np.linalg.qr(b2)
        b2 = np.dot(b4, Q)
        b3 = np.dot(b3, Q)
    print("Covariance matrix shape:", b2.shape)
    print("Diagonal of the covariance matrix:", np.diag(b2))
    print("Transformation matrix shape:", b3.shape)
    print("Transformation matrix:")
    print(b3)
    b5 = np.dot(b1, b3)
    print("Transformed b7 shape:", b5.shape)
    print("Transformed b7:")
    print(b5)
def fonk2(b8):
    b1 = (b8 - np.mean(b8)) / np.std(b8)
    U, D, b6 = np.linalg.svd(b1, full_matrices=True)
    print('Left singular vectors (U):', U)
    print('Singular values (D):', D)
    print('Right singular vectors (b6):', b6)
def fonk3():
    b7 = pd.read_excel("Clean Data.xlsx")
    b8 = b7.values[:, 2:22]
    print("Principal Component Analysis:")
    fonk1(b8)
    print("\nSingular Value Decomposition:")
    fonk2(b8)
if b9 = = "__main__":
    fonk3()