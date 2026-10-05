import numpy as np
import scipy.special
import pca
class Ica:
    def fit_transform(self, X, epochs, optimizer):
        '''
        Fits the Independent Component Analysis (ICA) model and transforms the input data.
        Parameters
        ----------
        X : numpy.ndarray, shape (n_samples, n_features)
            The input training data.
        epochs : int
            The number of epochs (iterations) for training the model.
        optimizer : object
            An optimizer object used for optimizing the ICA model parameters.
        Returns
        -------
        s : numpy.ndarray, shape (n_samples, n_features)
            Predicted sources per sample.
        '''
        n_samples, n_features = X.shape
        pca_model = pca.PCA(n_features, True)
        X_whitened = pca_model.fit_transform(X)
        self.unmixing_matrix = np.random.rand(n_features, n_features)
        for _ in range(epochs):
            gradient = self.compute_gradient(X_whitened)
            optimized_gradient = optimizer.optimize([gradient])[0]
            self.unmixing_matrix += optimized_gradient
        return X_whitened.dot(self.unmixing_matrix)
    def compute_gradient(self, X_whitened):
        '''
        Compute the gradient of the cost function.
        Parameters
        ----------
        X_whitened : numpy.ndarray, shape (n_samples, n_features)
            Whitened input data.
        Returns
        -------
        gradient : numpy.ndarray, shape (n_features, n_features)
            Gradient of the cost function.
        '''
        gradient = np.zeros_like(self.unmixing_matrix)
        for x in X_whitened:
            gradient += (1 - 2 * scipy.special.expit(self.unmixing_matrix.dot(x.T))).dot(x) + np.linalg.inv(self.unmixing_matrix.T)
        gradient /= X_whitened.shape[0]
        return gradient