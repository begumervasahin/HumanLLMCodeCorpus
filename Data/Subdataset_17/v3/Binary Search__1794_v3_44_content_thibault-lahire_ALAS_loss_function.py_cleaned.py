import numpy as np
def sigmoid(w):
    return 1 / (1 + np.exp(-w))
def sigmoid_derivative(w):
    exp_neg_w = np.exp(-w)
    if exp_neg_w < 1e16:
        if exp_neg_w > 1e-16:
            return exp_neg_w / (1 + exp_neg_w) ** 2
        else:
            return exp_neg_w
    else:
        return np.exp(w)
def sigmoid_second_derivative(w):
    exp_neg_w = np.exp(-w)
    if exp_neg_w < 1e16:
        if exp_neg_w > 1e-16:
            exp_w = np.exp(w)
            return -exp_w * (exp_w - 1) / (1 + exp_w) ** 3
        else:
            return -exp_neg_w
    else:
        return np.exp(w)
def compute_loss(x, S, A, y, output_type=1, penalize=False):
    d = A.shape[1]
    card_S = len(S)
    loss_value = 0
    gradient = np.zeros(d) if output_type >= 2 else None
    hessian = np.zeros((d, d)) if output_type == 3 else None
    for i in S:
        y_i = y[i]
        A_i = A[i]
        dot_product = np.dot(x, A_i)
        sigmoid_value = sigmoid(dot_product)
        loss_value += (y_i - sigmoid_value) ** 2
        if output_type >= 2:
            sigmoid_deriv = sigmoid_derivative(dot_product)
            gradient += 2 * A_i * sigmoid_deriv * (sigmoid_value - y_i)
        if output_type == 3:
            sigmoid_2nd_deriv = sigmoid_second_derivative(dot_product)
            hessian += 2 * (
                (sigmoid_value - y_i) * sigmoid_2nd_deriv +
                sigmoid_deriv ** 2
            ) * np.outer(A_i, A_i)
    if penalize:
        loss_value += 0.5 * np.linalg.norm(x) ** 2
    loss_value /= card_S
    if output_type == 3:
        hessian = 0.5 * (hessian + hessian.T)
        if penalize:
            gradient += x
            hessian += np.eye(d)
        gradient /= card_S
        hessian /= card_S
        return loss_value, gradient, hessian
    elif output_type == 2:
        if penalize:
            gradient += x
        gradient /= card_S
        return loss_value, gradient
    else:
        return loss_value
