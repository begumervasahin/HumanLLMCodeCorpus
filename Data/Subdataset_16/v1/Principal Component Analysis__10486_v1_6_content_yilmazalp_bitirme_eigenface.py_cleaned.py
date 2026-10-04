import numpy as np
def fonk1(b10):
    if len(b10) == 0:
        return np.array([])
    b1 = np.empty((0, b10[0].size), dtype=b10[0].dtype)
    for row in b10:
        b1 = np.vstack((b1, np.asarray(row).reshape(1, -1)))
    return b1
def fonk2(b10):
    if len(b10) == 0:
        return np.array([])
    b1 = np.empty((b10[0].size, 0), dtype=b10[0].dtype)
    for col in b10:
        b1 = np.hstack((b1, np.asarray(col).reshape(-1, 1)))
    return b1
def fonk3(b4, b2 = 0):
    [n, d] = b4.shape
    if (b2 <= 0) or (b2 > n):
        b2 = n
    b3 = b4.mean(axis=0)
    b4 = b4 - b3
    if n > d:
        b5 = np.dot(b4.T, b4)
        [b8, b6] = np.linalg.eigh(b5)
    else:
        b5 = np.dot(b4, b4.T)
        [b8, b6] = np.linalg.eigh(b5)
        b6 = np.dot(b4.T, b6)
    for i in range(n):
        b6[:, i] = b6[:, i] / np.linalg.norm(b6[:, i])
    b7 = np.argsort(-b8)
    b8 = b8[b7]
    b6 = b6[:, b7]
    b8 = b8[0:b2].copy()
    b6 = b6[:, 0:b2].copy()
    return [b8, b6, b3]
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
    b8, b6, b3 = fonk3(b11, b2=2)
    print("Eigenvalues:\n", b8)
    print("Eigenvectors:\n", b6)
    print("Mean:\n", b3)
    b13 = fonk4(b6, b11, b3)
    print("Projected Data:\n", b13)
    b14 = fonk5(b6, b13, b3)
    print("Reconstructed Data:\n", b14)