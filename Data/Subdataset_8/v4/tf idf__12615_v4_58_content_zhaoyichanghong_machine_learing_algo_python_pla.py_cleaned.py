import numpy as np
import metrics
class PerceptronLearningAlgorithm:
    def fit(self, X, y):
        '''
        Train the Perceptron model.
        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            Training data.
        y : array-like, shape (n_samples,)
            Target values, where 1 or -1 indicate the class.
        '''
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        while True:
            for i in range(n_samples):
                prediction = self.predict(X[i])
                if y[i] * prediction <= 0:
                    self.weights += (y[i] * X[i]).reshape(self.weights.shape)
                    self.bias += y[i]
            predictions = self.predict(X)
            if metrics.accuracy(y, predictions) == 1:
                break
    def predict(self, X):
        '''
        Predict class labels for samples.
        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            Predicting data.
        Returns
        -------
        y : array-like, shape (n_samples,)
            Predicted class label per sample, where 1 or -1 indicate the class.
        '''
        return np.sign(X.dot(self.weights) + self.bias)