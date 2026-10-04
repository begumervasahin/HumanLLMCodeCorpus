import numpy as np
from scipy import linalg as la
from scipy.sparse import linalg as spla
def L_Seed(
        A: spla.LinearOperator,
        B: np.ndarray,
        tol=5e-3,
        p_freq=5,
        maxit=50,
        verbose=True
    ) -> dict:
    n, t = A.shape[0], B.shape[1]
    X = np.zeros((n, t, maxit))
    R = np.zeros((n, t, maxit))
    U = np.zeros((n, t, maxit))
    Ï = np.zeros((t, maxit))
    Î² = np.zeros((t, maxit))
    Ï = np.zeros((t, maxit))
    Î³ = np.ones((t, maxit))
    Î´ = np.zeros((t, maxit))
    Ï[:, 0] = np.apply_along_axis(la.norm, 0, B)
    Î²[:, 0] = Ï[:, 0]
    R[:, :, 0] = B
    U[:, :, 0] = B / Î²[:, 0]
    j = 0
    converged = False
    while j < maxit - 1:
        tmp = A @ U[:, :, j]
        Î´[:, j] = np.diag(U[:, :, j].T @ tmp)
        tmp = tmp - U[:, :, j] * Î´[:, j] - Î²[:, j] * U[:, :, j - 1]
        Î²[:, j + 1] = np.apply_along_axis(la.norm, 0, tmp)
        U[:, :, j + 1] = tmp / Î²[:, j + 1]
        Î³[:, j] = 1 / (Î´[:, j] - Ï[:, j - 1] / Î³[:, j - 1])
        Ï[:, j] = (Î²[:, j + 1] * Î³[:, j]) ** 2
        Ï[:, j + 1] = -Î²[:, j + 1] * Î³[:, j] * Ï[:, j]
        R[:, :, j + 1] = Ï[:, j + 1] * U[:, :, j + 1]
        j += 1
        res_norm = np.amax(np.apply_along_axis(la.norm, 0, R[:, :, j]))
        if verbose and j % p_freq == 0:
            print(f"Error at step {j} is {res_norm:.4f}")
        if res_norm <= tol:
            converged = True
            break
    if verbose:
        if converged:
            print(f"Converged after {j} iterations.")
        else:
            print(f"Failed to converge after {j} iterations.")
    return {
        "U": U[:, :, :j],
        "Î²": Î²[:, :j],
        "Î´": Î´[:, :j],
        "Ï": Ï[:, :j]
    }