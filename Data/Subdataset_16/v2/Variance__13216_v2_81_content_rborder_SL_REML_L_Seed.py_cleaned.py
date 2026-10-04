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
    Ï = np.zeros((b5, b3))
    b9 = np.zeros((b5, b3))
    Ï = np.zeros((b5, b3))
    b10 = np.ones((b5, b3))
    Î´ = np.zeros((b5, b3))
    Ï[:, 0] = np.apply_along_axis(la.norm, 0, B)
    b9[:, 0] = Ï[:, 0]
    b7[:, :, 0] = B
    b8[:, :, 0] = B / b9[:, 0]
    a1 = 0
    b11 = False
    while a1 < b3 - 1:
        b12 = A @ b8[:, :, a1]
        Î´[:, a1] = np.diag(b8[:, :, a1].T @ b12)
        b12 = b12 - b8[:, :, a1] * Î´[:, a1] - b9[:, a1] * b8[:, :, a1 - 1]
        b9[:, a1 + 1] = np.apply_along_axis(la.norm, 0, b12)
        b8[:, :, a1 + 1] = b12 / b9[:, a1 + 1]
        b10[:, a1] = 1 / (Î´[:, a1] - Ï[:, a1 - 1] / b10[:, a1 - 1])
        Ï[:, a1] = (b9[:, a1 + 1] * b10[:, a1]) ** 2
        Ï[:, a1 + 1] = -b9[:, a1 + 1] * b10[:, a1] * Ï[:, a1]
        b7[:, :, a1 + 1] = Ï[:, a1 + 1] * b8[:, :, a1 + 1]
        a1 += 1
        b13 = np.amax(np.apply_along_axis(la.norm, 0, b7[:, :, a1]))
        if b4 and a1 % b2 = = 0:
            print(f"Error at step {a1} is {b13:.4f}")
        if b13 <= b1:
            b11 = True
            break
    if b4:
        if b11:
            print(f"Converged after {a1} iterations.")
        else:
            print(f"Failed to converge after {a1} iterations.")
    return {
        "b8": b8[:, :, :a1],
        "b9": b9[:, :a1],
        "Î´": Î´[:, :a1],
        "Ï": Ï[:, :a1]
    }