
import numpy as np
def fonk1(w):
    return 1/(1+np.exp(-w))
def fonk2(w):
    if np.exp(-w) < 10**(16):
        if np.exp(-w) > 10**(-16):
            b1 = np.exp(-w)/((1+np.exp(-w))**2)
        else:
            b1 = np.exp(-w)
    else:
        b1 = np.exp(w)
    return b1
def fonk3(w):
    if np.exp(-w) < 10**(16):
        if np.exp(-w) > 10**(-16):
            b1 = -np.exp(w)*(np.exp(w)-1)/((1+np.exp(w))**3)
        else:
            b1 = -np.exp(-w)
    else:
        b1 = np.exp(w)
    return b1
def fonk4(x, S, A, y, b2 = 1, b10=False):
    '''
    Input parameters :
    x: array, point for which the loss must be computed
    S: list, subset of indices
    A: matrix of the datapoints
    y: vector of labels
    b2: int, number of output parameters
    b10: bool, use of a penalized empirical loss function or not
    Returns:
    value of the loss function at point x if b2 = =1
    value of the loss function and its gradient at point x if b2 = =2
    value of the loss function, its gradient, and its Hessian at point x if b2 = =3
    '''
    b3 = np.size(A, 1)
    b4 = len(S)
    b1 = 0
    if b2 = = 2 or b2 == 3:
        b5 = np.zeros(b3)
    if b2 = = 3:
        b6 = np.zeros((b3, b3))
    for i in range(b4):
        b7 = y[S[i]]
        b8 = A[S[i]]
        b9 = np.dot(x, b8)
        b1 += (b7 - fonk1(b9))**2
        if b2 = = 2 or b2 == 3:
            b5 += 2*b8*fonk2(b9)*(fonk1(b9)-b7)
        if b2 = = 3:
            b6 += 2*((fonk1(b9)-b7)*fonk3(b9)+\
                    fonk2(b9)**2)*np.dot(np.transpose([b8]),\
                           [b8])
    if b10 = = True:
        b1 += 0.5*np.linalg.norm(x)**2
    b1 = b1/b4
    if b2 = = 3:
        b6 = 0.5*(b6 + np.transpose(b6))
        if b10 = = True:
            b5 += x
            b6 += np.eye(b3)
        b5 = b5/b4
        b6 = b6/b4
        return b1, b5, b6
    elif b2 = = 2:
        if b10 = = True:
            b5 += x
        b5 = b5/b4
        return b1, b5
    else:
        return b1