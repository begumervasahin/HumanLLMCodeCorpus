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
                prediction = self.predict_single(X[i])
                if y[i] * prediction <= 0:
                    self.weights += y[i] * X[i]
                    self.bias += y[i]
            predictions = self.predict(X)
            if metrics.accuracy(y, predictions) == 1:
                break
    def predict_single(self, x):
        '''
        Predict class label for a single sample.
        Parameters
        ----------
        x : array-like, shape (n_features,)
            Single sample.
        Returns
        -------
        y_pred : int
            Predicted class label for the sample, where 1 or -1 indicate the class.
        '''
        return np.sign(np.dot(x, self.weights) + self.bias)
    def predict(self, X):
        '''
        Predict class labels for samples.
        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            Predicting data.
        Returns
        -------
        y_pred : array-like, shape (n_samples,)
            Predicted class labels for samples, where 1 or -1 indicate the class.
        '''
        return np.sign(np.dot(X, self.weights) + self.bias)