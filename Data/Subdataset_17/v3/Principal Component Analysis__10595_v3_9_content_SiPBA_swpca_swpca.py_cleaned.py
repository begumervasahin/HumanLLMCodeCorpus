import numpy as np
from scipy.linalg import svd
from scipy.stats import f_oneway
def swpca(dataset, catvar, k=0.05, trset=None):
    N, D = dataset.shape
    if trset is None:
        trset = np.ones(N, dtype=bool)
        training = False
    else:
        training = True
    subj_mean = dataset.mean(axis=1)
    X = (dataset.T - subj_mean).T
    mean_tr = X[trset].mean(axis=0)
    X -= mean_tr
    var_tr = X[trset].var(axis=0)
    var_tr = np.maximum(var_tr, 1)
    X /= var_tr
    X_train = X[trset]
    X_test = X[~trset] if training else None
    U, s, Wt = svd(X_train, full_matrices=False)
    W = Wt.T
    sort_indices = np.argsort(s)[::-1]
    W = W[:, sort_indices]
    S_train = X_train.dot(W)
    S_test = X_test.dot(W) if training else None
    unique_labels = np.unique(catvar)
    F, p_val = f_oneway(S_train[catvar[trset] == unique_labels[0]],
                        S_train[catvar[trset] == unique_labels[1]])
    weights = 1 - np.exp(-p_val / k)
    A = np.linalg.pinv(W)
    weight_matrix = np.diag(weights)
    if training:
        X_train_hat = S_train.dot(weight_matrix).dot(A)
        X_test_hat = S_test.dot(weight_matrix).dot(A)
        X_hat = np.zeros((N, D))
        X_hat[trset] = X_train_hat
        X_hat[~trset] = X_test_hat
    else:
        X_hat = S_train.dot(weight_matrix).dot(A)
    X_hat = (X_hat * var_tr) + mean_tr
    X_hat = (X_hat.T + subj_mean).T
    return X_hat, weights, A
if __name__ == "__main__":
    dataset = np.random.rand(100, 10)
    catvar = np.random.randint(0, 2, 100)
    Xhat, weights, A = swpca(dataset, catvar)
    print("Reconstructed Dataset:\n", Xhat)
    print("Weights:\n", weights)
    print("Transformation Matrix:\n", A)