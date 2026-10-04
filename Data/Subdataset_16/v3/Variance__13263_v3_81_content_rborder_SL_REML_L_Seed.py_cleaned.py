import numpy as np
from scipy import linalg as la
from scipy.sparse import linalg as spla
def fonk1(
        A: spla.LinearOperator,
        B: np.ndarray,
        b1 = 5e-3,
        b2 = 5,
        b3 = 50,
        b4 = True
    ) -> dict:
    n, b5 = A.shape[0], B.shape[1]
    b6 = np.zeros((n, b5, b3))
    b7 = np.zeros((n, b5, b3))
    b8 = np.zeros((n, b5, b3))
    b9 = np.zeros((b5, b3))
    b10 = np.zeros((b5, b3))
    b11 = np.zeros((b5, b3))
    b12 = np.ones((b5, b3))
    b13 = np.zeros((b5, b3))
    b9[:, 0] = np.apply_along_axis(la.norm, 0, B)
    b10[:, 0] = b9[:, 0]
    b7[:, :, 0] = B
    b8[:, :, 0] = B / b10[:, 0]
    a1 = 0
    b14 = False
    while a1 < b3 - 1:
        b15 = A @ b8[:, :, a1]
        b13[:, a1] = np.diag(b8[:, :, a1].T @ b15)
        b15 = b15 - b8[:, :, a1] * b13[:, a1] - b10[:, a1] * b8[:, :, a1 - 1]
        b10[:, a1 + 1] = np.apply_along_axis(la.norm, 0, b15)
        b8[:, :, a1 + 1] = b15 / b10[:, a1 + 1]
        b12[:, a1] = 1 / (b13[:, a1] - b11[:, a1 - 1] / b12[:, a1 - 1])
        b11[:, a1] = (b10[:, a1 + 1] * b12[:, a1]) ** 2
        b9[:, a1 + 1] = -b10[:, a1 + 1] * b12[:, a1] * b9[:, a1]
        b7[:, :, a1 + 1] = b9[:, a1 + 1] * b8[:, :, a1 + 1]
        a1 += 1
        b16 = np.amax(np.apply_along_axis(la.norm, 0, b7[:, :, a1]))
        if b4 and a1 % b2 = = 0:
            print(f"Error at step {a1} is {b16:.4f}")
        if b16 <= b1:
            b14 = True
            break
    if b4:
        if b14:
            print(f"Converged after {a1} iterations.")
        else:
            print(f"Failed to converge after {a1} iterations.")
    return {
        "b8": b8[:, :, :a1],
        "b10": b10[:, :a1],
        "b13": b13[:, :a1],
        "b9": b9[:, :a1]
    }