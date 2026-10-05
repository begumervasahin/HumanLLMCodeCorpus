import numpy as np
def sigmoid(w):
    return 1 / (1 + np.exp(-w))
def sigmoid_prime(w):
    exp_neg_w = np.exp(-w)
    if exp_neg_w < 10 ** 16:
        if exp_neg_w > 10 ** (-16):
            f = exp_neg_w / ((1 + exp_neg_w) ** 2)
        else:
            f = exp_neg_w
    else:
        f = np.exp(w)
    return f
def sigmoid_double_prime(w):
    exp_neg_w = np.exp(-w)
    if exp_neg_w < 10 ** 16:
        if exp_neg_w > 10 ** (-16):
            f = -exp_neg_w * (np.exp(w) - 1) / ((1 + np.exp(w)) ** 3)
        else:
            f = -exp_neg_w
    else:
        f = np.exp(w)
    return f
def loss_function(x, S, A, y, arg=1, penalization=False):
    d = np.size(A, 1)
    card_S = len(S)
    f = 0
    if arg == 2 or arg == 3:
        gradient = np.zeros(d)
    if arg == 3:
        Hessian = np.zeros((d, d))
    for i in range(card_S):
        y_S_i = y[S[i]]
        A_S_i = A[S[i]]
        scal_prod = np.dot(x, A_S_i)
        f += (y_S_i - sigmoid(scal_prod)) ** 2
        if arg == 2 or arg == 3:
            gradient += 2 * A_S_i * sigmoid_prime(scal_prod) * (sigmoid(scal_prod) - y_S_i)
        if arg == 3:
            Hessian += 2 * ((sigmoid(scal_prod) - y_S_i) * sigmoid_double_prime(scal_prod) +
                            sigmoid_prime(scal_prod) ** 2) * np.dot(np.transpose([A_S_i]), [A_S_i])
    if penalization:
        f += 0.5 * np.linalg.norm(x) ** 2
    f /= card_S
    if arg == 3:
        Hessian = 0.5 * (Hessian + np.transpose(Hessian))
        if penalization:
            gradient += x
            Hessian += np.eye(d)
        gradient /= card_S
        Hessian /= card_S
        return f, gradient, Hessian
    elif arg == 2:
        if penalization:
            gradient += x
        gradient /= card_S
        return f, gradient
    else:
        return f