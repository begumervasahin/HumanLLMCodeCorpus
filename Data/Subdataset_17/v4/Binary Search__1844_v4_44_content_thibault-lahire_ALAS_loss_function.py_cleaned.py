import numpy as np
def phi(w):
    return 1 / (1 + np.exp(-w))
def phiprim(w):
    exp_neg_w = np.exp(-w)
    if exp_neg_w < 10**16:
        if exp_neg_w > 10**-16:
            result = exp_neg_w / ((1 + exp_neg_w) ** 2)
        else:
            result = exp_neg_w
    else:
        result = np.exp(w)
    return result
def phi2prim(w):
    exp_neg_w = np.exp(-w)
    if exp_neg_w < 10**16:
        if exp_neg_w > 10**-16:
            result = -np.exp(w) * (np.exp(w) - 1) / ((1 + np.exp(w)) ** 3)
        else:
            result = -exp_neg_w
    else:
        result = np.exp(w)
    return result
def loss(x, S, A, y, arg=1, penalization=False):
    d = A.shape[1]
    card_S = len(S)
    f = 0
    g = np.zeros(d) if arg >= 2 else None
    H = np.zeros((d, d)) if arg == 3 else None
    for i in range(card_S):
        y_S_i = y[S[i]]
        A_S_i = A[S[i]]
        scal_prod = np.dot(x, A_S_i)
        f += (y_S_i - phi(scal_prod)) ** 2
        if arg >= 2:
            g += 2 * A_S_i * phiprim(scal_prod) * (phi(scal_prod) - y_S_i)
        if arg == 3:
            H += 2 * ((phi(scal_prod) - y_S_i) * phi2prim(scal_prod) + \
                      phiprim(scal_prod) ** 2) * np.outer(A_S_i, A_S_i)
    if penalization:
        f += 0.5 * np.linalg.norm(x) ** 2
    f /= card_S
    if arg >= 2:
        if penalization:
            g += x
        g /= card_S
    if arg == 3:
        H = (H + H.T) / (2 * card_S)
        if penalization:
            H += np.eye(d) / card_S
    if arg == 3:
        return f, g, H
    elif arg == 2:
        return f, g
    else:
        return f