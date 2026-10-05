import numpy as np
import pandas as pd
def fonk1(b10):
    b1 = np.mean(b10, axis=0)
    b2 = np.std(b10, axis=0)
    return (b10 - b1) / b2
def fonk2(b10):
    b3 = fonk1(b10)
    b4 = np.dot(b3.T, b3)
    b5 = np.identity(b10.shape[1])
    a1 = 40
    for _ in range(a1):
        Q, b6 = np.linalg.qr(b4)
        b4 = np.dot(b6, Q)
        b5 = np.dot(b5, Q)
    b7 = np.dot(b3, b5)
    return b7
def fonk3(b10):
    b3 = fonk1(b10)
    U, D, b8 = np.linalg.svd(b3, full_matrices=True)
    return U, D, b8
def fonk4():
    b9 = pd.read_excel("Clean Data.xlsx")
    b10 = b9.iloc[:, 2:22].values
    b11 = fonk2(b10)
    print("Principal Component Analysis Result:")
    print(b11)
    print("\nSingular Value Decomposition Result:")
    U, D, b8 = fonk3(b10)
    print("U:", U)
    print("D:", D)
    print("b8:", b8)
if b12 = = "__main__":
    fonk4()