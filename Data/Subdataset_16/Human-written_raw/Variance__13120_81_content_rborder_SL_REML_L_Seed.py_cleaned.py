from numpy import *
from scipy import linalg as la
from scipy.sparse import linalg as spla
def fonk1(
        A: spla.LinearOperator,
        B: ndarray,
        b1 = 5e-3,
        b2 = 5,
        b3 = 50,
        b4 = True
    ) -> dict:
    b5 = A.shape[0]
    b6 = B.shape[1]
    b7 = zeros((b5,b6,b3))
    b8 = zeros((b5,b6,b3))
    b9 = zeros((b5,b6,b3))
    Ï = zeros((b6,b3))
    b10 = zeros((b6,b3))
    Ï = zeros((b6,b3))
    b11 = ones((b6,b3))
    Î´ = zeros((b6,b3))
    Ï[:,0] = apply_along_axis(la.norm,0,B)
    b10[:,0] = Ï[:,0]
    b8[:,:,0] = b9[:,:,0] = B
    b9[:,:,0] = b8[:,:,0]/b10[:,0]
    a1 = 0
    b12 = False
    while a1 < b3-1:
        b13 = A @ b9[:,:,a1]
        Î´[:,a1] = diag(b9[:,:,a1].T @ b13)
        b13 = b13 - b9[:,:,a1]*Î´[:,a1] - b10[:,a1]*b9[:,:,a1-1]
        b10[:,a1+1] = apply_along_axis(la.norm,0,b13)
        b9[:,:,a1+1] = b13 / b10[:,a1+1]
        b11[:,a1] = (Î´[:,a1] - Ï[:,a1-1]/b11[:,a1-1])**-1
        Ï[:,a1] = (b10[:,a1+1]*b11[:,a1])**2
        Ï[:,a1+1] = -b10[:,a1+1]*b11[:,a1]*Ï[:,a1]
        b8[:,:,a1+1] = Ï[:,a1+1]*b9[:,:,a1+1]
        a1 += 1
        b14 = amax(apply_along_axis(la.norm,0,(b8[:,:,a1])))
        if b4 and a1 % b2 = =0 : print("Error at step ",a1,
                                  " is ", b14)
        if b14 <= b1:
            b12 = True
            break
    if b4 and b12: print("Converged after ",a1," iterations.")
    elif b4: print("Failed to converge after ",a1," iterations.")
    return {
        "b9":b9[:,:,0:a1],
        "b10":b10[:,0:a1],
        "Î´":Î´[:,0:a1],
        "Ï":Ï[:,0:a1]
        }