import numpy as np
def fonk1(b12: str) -> np.array:
    b1 = []
    with open(b12, "r") as file:
        for line in file.readlines():
            b1.append([float(value) for value in line.split('\t')] + [0])
    return np.asarray(b1)
def fonk2(b7: np.array, b9: np.array) -> float:
    a1 = 0.0
    for point in b7:
        b2 = b6(point[-1])
        a1 += np.linalg.norm(point[:-1] - b9[b2])
    return a1 / b7.shape[0]
def fonk3(b7: np.array, b9: np.array) -> np.array:
    b3 = np.zeros(b9.shape)
    b4 = np.zeros(b9.shape[0], dtype=b6)
    for point in b7:
        b2 = b6(point[-1])
        b3[b2] += point[:-1]
        b4[b2] += 1
    for i in range(b9.shape[0]):
        if b4[i] > 0:
            b3[i] /= b4[i]
    return b3
def fonk4(b7: np.array, b9: np.array) -> np.array:
    for point in b7:
        b5 = np.linalg.norm(point[:-1] - b9, axis=1)
        point[-1] = np.argmin(b5)
    return b7
def fonk5(b12: str, a2: b6, max_iterations: b6 = 100) -> (np.array, float):
    b7 = fonk1(b12)
    b8 = np.random.choice(b7.shape[0], a2, replace=False)
    b9 = b7[b8, :-1]
    for iteration in range(max_iterations):
        b7 = fonk4(b7, b9)
        b3 = fonk3(b7, b9)
        if np.allclose(b9, b3):
            print(f"Converged after {iteration} iterations.")
            break
        b9 = b3
    b10 = fonk2(b7, b9)
    return b9, b10
if b11 = = "__main__":
    b12 = "b1.txt"
    a2 = 3
    b9, b10 = fonk5(b12, a2)
    print("Final b9:")
    print(b9)
    print("Final b10:")
    print(b10)