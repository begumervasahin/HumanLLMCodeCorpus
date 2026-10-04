import numpy as np
def fonk1(b10):
    if not b10:
        return np.array([])
    return np.vstack([np.asarray(row).reshape(1, -1) for row in b10])
def fonk2(b10):
    if not b10:
        return np.array([])
    return np.hstack([np.asarray(col).reshape(-1, 1) for col in b10])
def fonk3(b4, b1 = 0):
    n, b2 = b4.shape
    if b1 <= 0 or b1 > n:
        b1 = n
    b3 = b4.mean(axis=0)
    b4 = b4 - b3
    if n > b2:
        b5 = np.dot(b4.T, b4)
        b8, b6 = np.linalg.eigh(b5)
    else:
        b5 = np.dot(b4, b4.T)
        b8, b6 = np.linalg.eigh(b5)
        b6 = np.dot(b4.T, b6)
    b6 = np.array([vec / np.linalg.norm(vec) for vec in b6.T]).T
    b7 = np.argsort(-b8)
    b8 = b8[b7][:b1]
    b6 = b6[:, b7][:, :b1]
    return b8, b6, b3
def fonk4(b4, b10, b3 = None):
    if b3 is None:
        return np.dot(b10, b4)
    return np.dot(b10 - b3, b4)
def fonk5(b4, Y, b3 = None):
    if b3 is None:
        return np.dot(Y, b4.T)
    return np.dot(Y, b4.T) + b3
if b9 = = "__main__":
    b10 = [np.array([1, 2, 3]), np.array([4, 5, 6]), np.array([7, 8, 9])]
    b11 = fonk1(b10)
    print("Row Matrix:\n", b11)
    b12 = fonk2(b10)
    print("Column Matrix:\n", b12)
    b8, b6, b3 = fonk3(b11, b1=2)
    print("Eigenvalues:\n", b8)
    print("Eigenvectors:\n", b6)
    print("Mean:\n", b3)
    b13 = fonk4(b6, b11, b3)
    print("Projected Data:\n", b13)
    b14 = fonk5(b6, b13, b3)
    print("Reconstructed Data:\n", b14)