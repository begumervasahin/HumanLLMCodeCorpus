import numpy as np
def sigmoid(w):
    return 1 / (1 + np.exp(-w))
def sigmoid_derivative(w):
    exp_neg_w = np.exp(-w)
    if exp_neg_w < 1e16:
        if exp_neg_w > 1e-16:
            return exp_neg_w / ((1 + exp_neg_w) ** 2)
        else:
            return exp_neg_w
    else:
        return np.exp(w)
def sigmoid_second_derivative(w):
    exp_neg_w = np.exp(-w)
    if exp_neg_w < 1e16:
        if exp_neg_w > 1e-16:
            return -np.exp(w) * (np.exp(w) - 1) / ((1 + np.exp(w)) ** 3)
        else:
            return -exp_neg_w
    else:
        return np.exp(w)
def compute_loss(x, S, A, y, arg=1, penalization=False):
    num_features = A.shape[1]
    subset_size = len(S)
    loss_value = 0
    gradient = np.zeros(num_features) if arg >= 2 else None
    hessian = np.zeros((num_features, num_features)) if arg == 3 else None
    for i in range(subset_size):
        y_i = y[S[i]]
        A_i = A[S[i]]
        dot_product = np.dot(x, A_i)
        sigmoid_value = sigmoid(dot_product)
        loss_value += (y_i - sigmoid_value) ** 2
        if arg >= 2:
            sigmoid_derivative_value = sigmoid_derivative(dot_product)
            gradient += 2 * A_i * sigmoid_derivative_value * (sigmoid_value - y_i)
        if arg == 3:
            sigmoid_second_derivative_value = sigmoid_second_derivative(dot_product)
            hessian += 2 * ((sigmoid_value - y_i) * sigmoid_second_derivative_value + \
                            sigmoid_derivative_value ** 2) * np.outer(A_i, A_i)
    if penalization:
        loss_value += 0.5 * np.linalg.norm(x) ** 2
    loss_value /= subset_size
    if arg >= 2:
        if penalization:
            gradient += x
        gradient /= subset_size
    if arg == 3:
        hessian = (hessian + hessian.T) / (2 * subset_size)
        if penalization:
            hessian += np.eye(num_features) / subset_size
    if arg == 3:
        return loss_value, gradient, hessian
    elif arg == 2:
        return loss_value, gradient
    else:
        return loss_value