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
    rho = np.zeros((t, maxit))
    beta = np.zeros((t, maxit))
    omega = np.zeros((t, maxit))
    gamma = np.ones((t, maxit))
    delta = np.zeros((t, maxit))
    rho[:, 0] = np.apply_along_axis(la.norm, 0, B)
    beta[:, 0] = rho[:, 0]
    R[:, :, 0] = B
    U[:, :, 0] = B / beta[:, 0]
    j = 0
    converged = False
    while j < maxit - 1:
        tmp = A @ U[:, :, j]
        delta[:, j] = np.diag(U[:, :, j].T @ tmp)
        tmp = tmp - U[:, :, j] * delta[:, j] - beta[:, j] * U[:, :, j - 1]
        beta[:, j + 1] = np.apply_along_axis(la.norm, 0, tmp)
        U[:, :, j + 1] = tmp / beta[:, j + 1]
        gamma[:, j] = 1 / (delta[:, j] - omega[:, j - 1] / gamma[:, j - 1])
        omega[:, j] = (beta[:, j + 1] * gamma[:, j]) ** 2
        rho[:, j + 1] = -beta[:, j + 1] * gamma[:, j] * rho[:, j]
        R[:, :, j + 1] = rho[:, j + 1] * U[:, :, j + 1]
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
        "beta": beta[:, :j],
        "delta": delta[:, :j],
        "rho": rho[:, :j]
    }