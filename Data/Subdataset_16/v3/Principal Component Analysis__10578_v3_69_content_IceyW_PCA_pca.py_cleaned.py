import numpy as np
def fonk1(data):
    b1 = np.b1(data, axis=0)
    b2 = data - b1
    return b2, b1
def fonk2(data):
    b2, b1 = fonk1(data)
    b3 = np.cov(b2, rowvar=0)
    eigenvalues, b4 = np.linalg.eig(np.mat(b3))
    b5 = np.argsort(eigenvalues)[::-1]
    b6 = eigenvalues[b5]
    b7 = b4[:, b5]
    return b6, b7
def fonk3(eigenvalues, percentage):
    b8 = np.sum(eigenvalues)
    a1 = 0
    a2 = 0
    for eigenvalue in eigenvalues:
        a1 += eigenvalue
        a2 += 1
        if a1 >= b8 * percentage:
            break
    b9 = eigenvalues[:a2] / b8
    return a2, b9
def fonk4(eigenvalues):
    _, b9 = fonk3(eigenvalues, 1)
    return b9
def fonk5(eigenvalues, b10 = 0.1):
    _, b9 = fonk3(eigenvalues, 1)
    a2 = np.sum(b9 > b10)
    return a2, b9[:a2]
def fonk6(data, b4, a2):
    b11 = b4[:, :a2]
    b12 = np.dot(data, b11)
    return b12
if b13 = = "__main__":
    b14 = np.array([
        [2.5, 2.4],
        [0.5, 0.7],
        [2.2, 2.9],
        [1.9, 2.2],
        [3.1, 3.0],
        [2.3, 2.7],
        [2.0, 1.6],
        [1.0, 1.1],
        [1.5, 1.6],
        [1.1, 0.9]
    ])
    eigenvalues, b4 = fonk2(b14)
    print("Eigenvalues:", eigenvalues)
    print("Eigenvectors:\n", b4)
    a2, b9 = fonk5(eigenvalues)
    print("Number of components with >10% variance:", a2)
    print("Percentage of variance for these components:", b9)
    b15 = fonk6(b14, b4, a2)
    print("Reduced data:\n", b15)