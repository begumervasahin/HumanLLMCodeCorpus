import numpy as np
import scipy.special
import pca
class ICA:
    def __init__(self):
        self.__W = None
    def fit_transform(self, X, epochs, optimizer):
        n_samples, n_features = X.shape
        pca_model = pca.PCA(n_features, whiten=True)
        X_whitened = pca_model.fit_transform(X)
        self.__W = np.random.rand(n_features, n_features)
        for epoch in range(epochs):
            g_W = np.zeros_like(self.__W)
            for x in X_whitened:
                term1 = 1 - 2 * scipy.special.expit(self.__W.dot(x.T))
                term2 = np.linalg.inv(self.__W.T)
                g_W += term1[:, None] * x + term2
            g_W /= n_samples
            self.__W += optimizer.optimize([g_W])[0]
        S = X_whitened.dot(self.__W)
        return S