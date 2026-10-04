import numpy as np
from sklearn.metrics import accuracy_score
class PerceptronLearningAlgorithm:
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        while True:
            no_errors = True
            for i in range(n_samples):
                prediction = self.predict_single(X[i])
                if y[i] * prediction <= 0:
                    self.weights += y[i] * X[i]
                    self.bias += y[i]
                    no_errors = False
            if no_errors:
                break
    def predict_single(self, x):
        return np.sign(np.dot(x, self.weights) + self.bias)
    def predict(self, X):
        return np.sign(np.dot(X, self.weights) + self.bias)
if __name__ == "__main__":
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    y = np.array([1, -1, 1, -1])
    pla = PerceptronLearningAlgorithm()
    pla.fit(X, y)
    predictions = pla.predict(X)
    print("Predictions:", predictions)
    print("Accuracy:", accuracy_score(y, predictions))