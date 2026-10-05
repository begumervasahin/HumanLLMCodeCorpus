import numpy as np
import pandas as pd
def PCA(X):
    ren, col = X.shape
    Xc = (X - np.mean(X)) / (np.std(X))
    A = np.dot(Xc.T, Xc)
    sizeSRen, sizeSCol = A.shape
    S = np.identity(sizeSRen)
    TempA = np.diag(A)
    TempASorted = np.sort(TempA)
    TempASortedReversed = TempASorted[::-1]
    for i in range(40):
        Q, R = np.linalg.qr(A)
        A = np.dot(R, Q)
        S = np.dot(S, Q)
    print("A shape:", A.shape)
    print(np.diag(A))
    print("S shape:", S.shape)
    print(S)
    F = np.dot(Xc, S)
    print("F shape:", F.shape)
    print(F)
def SVC(X):
    ren, col = X.shape
    Xc = (X - np.mean(X)) / (np.std(X))
    P, D, Q = np.linalg.svd(Xc, full_matrices=True, compute_uv=True)
    print('P:', P)
    print('D:', D)
    print('Q:', Q)
def main():
    X_input = pd.read_excel("Clean Data.xlsx")
    X = X_input.values
    X = X[:, 2:22]
    PCA(X)
    print("SVC!!!!!")
    SVC(X)
if __name__ == "__main__":
    main()