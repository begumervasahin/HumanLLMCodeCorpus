import numpy as np
import scipy.special
import pca
class ICA:
    def __init__(self):
        self.__W = None
    def fit_transform(self, X, epochs, optimizer):
        n_samples, n_features = X.shape
        X_whitened = self._whiten_data(X, n_features)
        self.__W = self._initialize_unmixing_matrix(n_features)
        for _ in range(epochs):
            gradient = self._compute_gradient(X_whitened)
            self.__W += optimizer.optimize([gradient])[0]
        S = self._transform_data(X_whitened)
        return S
    def _whiten_data(self, X, n_features):
        pca_model = pca.PCA(n_features, whiten=True)
        return pca_model.fit_transform(X)
    def _initialize_unmixing_matrix(self, n_features):
        return np.random.rand(n_features, n_features)
    def _compute_gradient(self, X_whitened):
        n_samples = X_whitened.shape[0]
        gradient = np.zeros_like(self.__W)
        for x in X_whitened:
            term1 = 1 - 2 * scipy.special.expit(self.__W.dot(x.T))
            term2 = np.linalg.inv(self.__W.T)
            gradient += term1[:, None] * x + term2
        return gradient / n_samples
    def _transform_data(self, X_whitened):
        return X_whitened.dot(self.__W)