import numpy as np
import scipy.special
class PCA:
    def __init__(self, n_components, whiten=False):
        self.n_components = n_components
        self.whiten = whiten
    def fit_transform(self, X):
        X_centered = X - np.mean(X, axis=0)
        U, S, Vt = np.linalg.svd(X_centered, full_matrices=False)
        X_pca = U @ np.diag(S)[:, :self.n_components]
        if self.whiten:
            X_pca /= np.std(X_pca, axis=0)
        return X_pca
class Optimizer:
    def optimize(self, gradients):
        return [0.01 * grad for grad in gradients]
class Ica:
    def fit_transform(self, X, epochs, optimizer):
        n_samples, n_features = X.shape
        pca_model = PCA(n_features, whiten=True)
        X_whiten = pca_model.fit_transform(X)
        self.W = np.random.rand(n_features, n_features)
        for epoch in range(epochs):
            gradient_W = np.zeros_like(self.W)
            for x in X_whiten:
                gradient_W += (1 - 2 * scipy.special.expit(self.W @ x.T)) @ x + np.linalg.inv(self.W.T)
            gradient_W /= n_samples
            optimized_gradient = optimizer.optimize([gradient_W])[0]
            self.W += optimized_gradient
        return X_whiten @ self.W
def main():
    np.random.seed(0)
    X = np.random.rand(100, 5)
    ica = Ica()
    optimizer = Optimizer()
    sources = ica.fit_transform(X, epochs=1000, optimizer=optimizer)
    print(sources[:5])
if __name__ == "__main__":
    main()