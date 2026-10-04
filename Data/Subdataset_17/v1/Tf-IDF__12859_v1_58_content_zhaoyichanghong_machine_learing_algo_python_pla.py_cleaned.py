import numpy as np
from sklearn.metrics import accuracy_score
class PLA:
    def fit(self, X, y):
        '''
        Parameters
        ----------
        X : numpy.ndarray, shape (n_samples, n_features)
            Training data
        y : numpy.ndarray, shape (n_samples,)
            Target values, 1 or -1
        '''
        n_samples, n_features = X.shape
        self.__W = np.zeros(n_features)
        self.__b = 0
        while True:
            errors = False
            for i in range(n_samples):
                h = self.predict(X[i])
                if y[i] * h <= 0:
                    self.__W += y[i] * X[i]
                    self.__b += y[i]
                    errors = True
            if not errors:
                break
    def predict(self, X):
        '''
        Parameters
        ----------
        X : numpy.ndarray, shape (n_samples, n_features) or (n_features,)
            Predicting data
        Returns
        -------
        y : numpy.ndarray or int
            Predicted class label per sample, 1 or -1
        '''
        return np.sign(X.dot(self.__W) + self.__b)
if __name__ == "__main__":
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    y = np.array([1, -1, 1, -1])
    pla = PLA()
    pla.fit(X, y)
    predictions = pla.predict(X)
    print("Predictions:", predictions)
    print("Accuracy:", accuracy_score(y, predictions))