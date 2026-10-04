import numpy as np
from scipy.linalg import svd
from scipy.stats import f_oneway
def swpca(dataset, catvar, k=0.05, trset=None):
    N, _ = dataset.shape
    training = trset is not None
    if not training:
        trset = np.ones(N, dtype=bool)
    subj_mean = dataset.mean(axis=1)
    X = dataset - subj_mean[:, np.newaxis]
    mean_tr = X[trset].mean(axis=0)
    X -= mean_tr
    var_tr = np.maximum(X[trset].var(axis=0), 1)
    X /= var_tr
    if training:
        X_test = X[~trset]
    X_train = X[trset]
    U, s, Wt = svd(X_train, full_matrices=False)
    W = Wt.T
    sorted_indices = np.argsort(s)[::-1]
    U = U[:, sorted_indices]
    s = s[sorted_indices]
    W = W[:, sorted_indices]
    S_train = X_train.dot(W)
    if training:
        S_test = X_test.dot(W)
    unique_labels = np.unique(catvar)
    F, p_val = f_oneway(S_train[catvar[trset] == unique_labels[0]],
                        S_train[catvar[trset] == unique_labels[1]])
    weights = 1 - np.exp(-p_val / k)
    A = np.linalg.pinv(W)
    weight_matrix = np.diag(weights)
    if training:
        X_train_hat = S_train.dot(weight_matrix).dot(A)
        X_test_hat = S_test.dot(weight_matrix).dot(A)
        X_hat = np.zeros((N, X_train_hat.shape[1]))
        X_hat[trset] = X_train_hat
        X_hat[~trset] = X_test_hat
    else:
        X_hat = S_train.dot(weight_matrix).dot(A)
    X_hat = X_hat * var_tr
    X_hat += mean_tr
    X_hat += subj_mean[:, np.newaxis]
    return X_hat, weights, A