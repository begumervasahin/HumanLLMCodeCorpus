import numpy as np
def fonk1(filename: str) -> np.array:
    b1 = []
    with open(filename, "r") as file:
        b2 = file.readlines()
        for line in b2:
            b1.append([float(value) for value in line.strip().split('\t')] + [0])
    return np.asarray(b1)
def fonk2(X: np.array, b9: np.array) -> float:
    a1 = 0.0
    for x in X:
        b3 = int(x[-1])
        a1 += np.linalg.norm(x[:-1] - b9[b3])
    return a1 / X.shape[0]
def fonk3(X: np.array, b9: np.array) -> np.array:
    b4 = np.zeros(b9.shape)
    b5 = np.zeros(b9.shape[0])
    for x in X:
        b3 = int(x[-1])
        b4[b3] += x[:-1]
        b5[b3] += 1
    for i in range(b9.shape[0]):
        if b5[i] != 0:
            b4[i] /= b5[i]
        else:
            b4[i] = b9[i]
    return b4
def fonk4(X: np.array, b9: np.array) -> np.array:
    for x in X:
        b6 = np.linalg.norm(x[:-1] - b9, axis=1)
        b7 = np.argmin(b6)
        x[-1] = b7
    return X
def fonk5(filename: str, k: int, iterations: int) -> tuple:
    b1 = fonk1(filename)
    b8 = np.random.choice(b1.shape[0], k, replace=False)
    b9 = b1[b8, :-1]
    for _ in range(iterations):
        b1 = fonk4(b1, b9)
        b9 = fonk3(b1, b9)
    b10 = fonk2(b1, b9)
    print(f"Final clustering error: {b10}")
    return b1, b9
if b11 = = "__main__":
    b12 = "b1.txt"
    a2 = 3
    a3 = 100
    clustered_data, b9 = fonk5(b12, a2, a3)
    print("Clustered Data:\n", clustered_data)
    print("Centroids:\n", b9)