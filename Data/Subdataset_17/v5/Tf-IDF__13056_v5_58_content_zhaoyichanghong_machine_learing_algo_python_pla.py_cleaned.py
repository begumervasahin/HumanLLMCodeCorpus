import numpy as np
import metrics
class Perceptron:
    def __init__(self):
        self.weights = None
        self.bias = 0
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        while True:
            errors = False
            for i in range(n_samples):
                prediction = self._predict_single_sample(X[i])
                if y[i] * prediction <= 0:
                    self.weights += y[i] * X[i]
                    self.bias += y[i]
                    errors = True
            if not errors:
                break
    def predict(self, X):
        return np.sign(X.dot(self.weights) + self.bias)
    def _predict_single_sample(self, x):
        return np.sign(np.dot(x, self.weights) + self.bias)