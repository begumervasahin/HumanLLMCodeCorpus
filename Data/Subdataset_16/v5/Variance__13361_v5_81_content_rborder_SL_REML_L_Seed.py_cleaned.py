from numpy import zeros, ones, diag, apply_along_axis, amax
from scipy import linalg as la
from scipy.sparse import linalg as spla
from numpy import ndarray
def fonk1(
    A: spla.LinearOperator,
    B: ndarray,
    tol: b1 = 5e-3,
    b13: b2 = 5,
    maxit: b2 = 50,
    verbose: b3 = True
) -> dict:
    n, b4 = A.shape[0], B.shape[1]
    b5 = zeros((n, b4, maxit))
    b6 = zeros((n, b4, maxit))
    b7 = zeros((n, b4, maxit))
    Ï = zeros((b4, maxit))
    b8 = zeros((b4, maxit))
    Ï = zeros((b4, maxit))
    b9 = ones((b4, maxit))
    Î´ = zeros((b4, maxit))
    Ï[:, 0] = apply_along_axis(la.norm, 0, B)
    b8[:, 0] = Ï[:, 0]
    b6[:, :, 0] = B
    b7[:, :, 0] = B / b8[:, 0]
    a1 = 0
    b10 = False
    while a1 < maxit - 1:
        b11 = A @ b7[:, :, a1]
        Î´[:, a1] = diag(b7[:, :, a1].T @ b11)
        if a1 > 0:
            b11 = b11 - b7[:, :, a1] * Î´[:, a1] - b8[:, a1] * b7[:, :, a1 - 1]
        else:
            b11 = b11 - b7[:, :, a1] * Î´[:, a1]
        b8[:, a1 + 1] = apply_along_axis(la.norm, 0, b11)
        b7[:, :, a1 + 1] = b11 / b8[:, a1 + 1]
        if a1 > 0:
            b9[:, a1] = 1 / (Î´[:, a1] - Ï[:, a1 - 1] / b9[:, a1 - 1])
        else:
            b9[:, a1] = 1 / Î´[:, a1]
        Ï[:, a1] = (b8[:, a1 + 1] * b9[:, a1]) ** 2
        Ï[:, a1 + 1] = -b8[:, a1 + 1] * b9[:, a1] * Ï[:, a1]
        b6[:, :, a1 + 1] = Ï[:, a1 + 1] * b7[:, :, a1 + 1]
        a1 += 1
        b12 = amax(apply_along_axis(la.norm, 0, b6[:, :, a1]))
        if verbose and a1 % b13 = = 0:
            print(f"Error at step {a1} is {b12}")
        if b12 <= tol:
            b10 = True
            break
    if verbose:
        if b10:
            print(f"Converged after {a1} iterations.")
        else:
            print(f"Failed to converge after {a1} iterations.")
    return {
        "b7": b7[:, :, :a1],
        "b8": b8[:, :a1],
        "Î´": Î´[:, :a1],
        "Ï": Ï[:, :a1]
    }