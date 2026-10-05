import numpy as np
from sklearn.metrics import accuracy_score
class PerceptronLearningAlgorithm:
    def fit(self, X_train, y_train):
        '''
        Fit the Perceptron Learning Algorithm to the training data.
        Parameters
        ----------
        X_train : numpy.ndarray
            Training data of shape (n_samples, n_features).
        y_train : numpy.ndarray
            Target values of shape (n_samples,).
        '''
        n_samples, n_features = X_train.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        while True:
            for i in range(n_samples):
                prediction = self.predict(X_train[i])
                if y_train[i] * prediction <= 0:
                    self.weights += (y_train[i] * X_train[i]).reshape(self.weights.shape)
                    self.bias += y_train[i]
            predictions = self.predict(X_train)
            if accuracy_score(y_train, predictions) == 1:
                break
    def predict(self, X):
        '''
        Predict class labels for input data.
        Parameters
        ----------
        X : numpy.ndarray
            Input data of shape (n_samples, n_features).
        Returns
        -------
        numpy.ndarray
            Predicted class labels of shape (n_samples,).
        '''
        return np.sign(X.dot(self.weights) + self.bias)
if __name__ == "__main__":
    X_train = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    y_train = np.array([1, 1, -1, -1])
    pla = PerceptronLearningAlgorithm()
    pla.fit(X_train, y_train)
    X_test = np.array([[1, 1], [2, 2], [3, 3], [4, 4]])
    predictions = pla.predict(X_test)
    print("Predictions:", predictions)