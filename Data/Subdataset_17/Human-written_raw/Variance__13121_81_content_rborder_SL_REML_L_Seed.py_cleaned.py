from numpy import *
from scipy import linalg as la
from scipy.sparse import linalg as spla
def L_Seed(
        A: spla.LinearOperator,
        B: ndarray,
        tol = 5e-3,
        p_freq = 5,
        maxit = 50,
        verbose = True
    ) -> dict:
    n = A.shape[0]
    t = B.shape[1]
    X = zeros((n,t,maxit))
    R = zeros((n,t,maxit))
    U = zeros((n,t,maxit))
    Ï = zeros((t,maxit))
    Î² = zeros((t,maxit))
    Ï = zeros((t,maxit))
    Î³ =  ones((t,maxit))
    Î´ = zeros((t,maxit))
    Ï[:,0] = apply_along_axis(la.norm,0,B)
    Î²[:,0] = Ï[:,0]
    R[:,:,0] = U[:,:,0] = B
    U[:,:,0] = R[:,:,0]/Î²[:,0]
    j = 0
    cnvg = False
    while j < maxit-1:
        tmp = A @ U[:,:,j]
        Î´[:,j] = diag(U[:,:,j].T @ tmp)
        tmp = tmp - U[:,:,j]*Î´[:,j] - Î²[:,j]*U[:,:,j-1]
        Î²[:,j+1] = apply_along_axis(la.norm,0,tmp)
        U[:,:,j+1] = tmp / Î²[:,j+1]
        Î³[:,j] = (Î´[:,j] - Ï[:,j-1]/Î³[:,j-1])**-1
        Ï[:,j] = (Î²[:,j+1]*Î³[:,j])**2
        Ï[:,j+1] = -Î²[:,j+1]*Î³[:,j]*Ï[:,j]
        R[:,:,j+1] = Ï[:,j+1]*U[:,:,j+1]
        j += 1
        res_norm = amax(apply_along_axis(la.norm,0,(R[:,:,j])))
        if verbose and j % p_freq ==0 : print("Error at step ",j,
                                  " is ", res_norm)
        if res_norm <= tol:
            cnvg = True
            break
    if verbose and cnvg: print("Converged after ",j," iterations.")
    elif verbose: print("Failed to converge after ",j," iterations.")
    return {
        "U":U[:,:,0:j],
        "Î²":Î²[:,0:j],
        "Î´":Î´[:,0:j],
        "Ï":Ï[:,0:j]
        }