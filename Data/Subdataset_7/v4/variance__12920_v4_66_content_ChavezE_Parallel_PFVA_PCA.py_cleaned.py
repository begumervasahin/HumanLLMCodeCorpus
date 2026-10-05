import numpy as np
import pandas as pd
def fonk1(b9):
    return (b9 - np.mean(b9, b1 = 0)) / np.std(b9, b1=0)
def fonk2(b9):
    b2 = fonk1(b9)
    b3 = np.dot(b2.T, b2)
    b4 = np.identity(b9.shape[1])
    for _ in range(40):
        Q, b5 = np.linalg.qr(b3)
        b3 = np.dot(b5, Q)
        b4 = np.dot(b4, Q)
    b6 = np.dot(b2, b4)
    return b6
def fonk3(b9):
    b2 = fonk1(b9)
    U, D, b7 = np.linalg.svd(b2, full_matrices=True)
    return U, D, b7
def fonk4():
    b8 = pd.read_excel("Clean Data.xlsx")
    b9 = b8.values[:, 2:22]
    b10 = fonk2(b9)
    print("Principal Component Analysis Result:")
    print(b10)
    print("\nSingular Value Decomposition Result:")
    U, D, b7 = fonk3(b9)
    print("U:", U)
    print("D:", D)
    print("b7:", b7)
if b11 = = "__main__":
    fonk4()