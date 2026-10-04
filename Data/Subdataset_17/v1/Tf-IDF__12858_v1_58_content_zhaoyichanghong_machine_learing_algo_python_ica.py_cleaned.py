import numpy as np
import scipy.special
class PCA:
    def __init__(self, n_components, whiten=False):
        self.n_components = n_components
        self.whiten = whiten
    def fit_transform(self, X):
        X_centered = X - np.mean(X, axis=0)
        U, S, V = np.linalg.svd(X_centered, full_matrices=False)
        X_pca = U @ np.diag(S)[:, :self.n_components]
        if self.whiten:
            X_pca /= np.std(X_pca, axis=0)
        return X_pca
class Optimizer:
    def optimize(self, gradients):
        return [0.01 * grad for grad in gradients]
class Ica:
    def fit_transform(self, X, epochs, optimizer):
        '''
        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            Training data
        epochs : int
            The number of epochs
        optimizer : Optimizer object
            Optimizer instance, should have an 'optimize' method
        Returns
        -------
        s : array-like, shape (n_samples, n_features)
            Predicted source per sample.
        '''
        n_samples, n_features = X.shape
        pca_model = PCA(n_features, whiten=True)
        X_whiten = pca_model.fit_transform(X)
        self.__W = np.random.rand(n_features, n_features)
        for epoch in range(epochs):
            g_W = np.zeros_like(self.__W)
            for x in X_whiten:
                g_W += (1 - 2 * scipy.special.expit(self.__W.dot(x.T))).dot(x) + np.linalg.inv(self.__W.T)
            g_W /= n_samples
            g_W = optimizer.optimize([g_W])[0]
            self.__W += g_W
        return X_whiten.dot(self.__W)
if __name__ == "__main__":
    np.random.seed(0)
    X = np.random.rand(100, 5)
    ica = Ica()
    optimizer = Optimizer()
    sources = ica.fit_transform(X, epochs=1000, optimizer=optimizer)
    print(sources[:5])