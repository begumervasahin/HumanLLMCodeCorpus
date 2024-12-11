import numpy as np
import pandas as pd
def fonk1(b13):
    ren, b1 = b13.shape
    b2 = (b13 - np.mean(b13)) / (np.std(b13))
    b3 = np.dot(b2.T, b2)
    sizeSRen, b4 = b3.shape
    b5 = np.identity(sizeSRen)
    b6 = np.diag(b3)
    b7 = np.sort(b6)
    b8 = b7[::-1]
    for i in range(40):
        b11, b9 = np.linalg.qr(b3)
        b3 = np.dot(b9, b11)
        b5 = np.dot(b5, b11)
    print("b3 shape:", b3.shape)
    print(np.diag(b3))
    print("b5 shape:", b5.shape)
    print(b5)
    b10 = np.dot(b2, b5)
    print("b10 shape:", b10.shape)
    print(b10)
def fonk2(b13):
    ren, b1 = b13.shape
    b2 = (b13 - np.mean(b13)) / (np.std(b13))
    P, D, b11 = np.linalg.svd(b2, full_matrices=True, compute_uv=True)
    print('P:', P)
    print('D:', D)
    print('b11:', b11)
def fonk3():
    b12 = pd.read_excel("Clean Data.xlsx")
    b13 = b12.values
    b13 = b13[:, 2:22]
    fonk1(b13)
    print("SVC!!!!!")
    fonk2(b13)
if b14 = = "__main__":
    fonk3()