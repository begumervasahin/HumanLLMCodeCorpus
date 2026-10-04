import numpy as np
def fonk1(b13):
    b1 = np.b1(b13, axis=0)
    b2 = b13 - b1
    return b2, b1
def fonk2(b13):
    b2, b1 = fonk1(b13)
    b3 = np.cov(b2, rowvar=0)
    eigvals, b4 = np.linalg.eig(np.mat(b3))
    b5 = np.argsort(eigvals)
    b5 = b5[-1::-1]
    b6 = eigvals[b5]
    b7 = b4[:, b5]
    return b6, b7
def fonk3(eigvals, percentage):
    b8 = sum(eigvals)
    a1 = 0
    a2 = 0
    for i in eigvals:
        a1 = a1 + i
        a2 = a2 + 1
        if a1 >= b8 * percentage:
            break
    b9 = np.zeros(a2)
    for i in range(a2):
        b9[i] = eigvals[i] / b8
    return a2, b9
def fonk4(eigvals):
    s, b10 = fonk3(eigvals, 1)
    return b10
def fonk5(eigvals):
    s, b10 = fonk3(eigvals, 1)
    a2 = 0
    for i in b10:
        if i > 0.1:
            a2 = a2 + 1
    b10 = b10[:a2]
    return a2, b10
def fonk6(b13, eigvect, a2):
    b7 = eigvect[:, 0:a2]
    b11 = np.dot(b13, b7)
    return b11
if b12 = = "__main__":
    b13 = np.array([[2.5, 2.4],
                        [0.5, 0.7],
                        [2.2, 2.9],
                        [1.9, 2.2],
                        [3.1, 3.0],
                        [2.3, 2.7],
                        [2, 1.6],
                        [1, 1.1],
                        [1.5, 1.6],
                        [1.1, 0.9]])
    eigvals, b4 = fonk2(b13)
    print("Eigenvalues:", eigvals)
    print("Eigenvectors:\n", b4)
    a2, b10 = fonk5(eigvals)
    print("Number of components with >10% variance:", a2)
    print("Percentage of variance for these components:", b10)
    b11 = fonk6(b13, b4, a2)
    print("Reduced data:\n", b11)