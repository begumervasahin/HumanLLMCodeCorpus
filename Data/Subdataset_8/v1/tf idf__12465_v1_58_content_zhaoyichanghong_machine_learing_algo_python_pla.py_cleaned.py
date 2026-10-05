import numpy as np
from sklearn.metrics import accuracy_score
class Pla:
    def fit(self, X, y):
        '''
        Parameters
        ----------
        X : shape (n_samples, n_features)
            Training data
        y : shape (n_samples,)
            Target values, 1 or -1
        '''
        n_samples, n_features = X.shape
        self.__W = np.zeros(n_features)
        self.__b = 0
        while True:
            for i in range(n_samples):
                h = self.predict(X[i])
                if y[i] * h <= 0:
                    self.__W += (y[i] * X[i]).reshape(self.__W.shape)
                    self.__b += y[i]
            h = self.predict(X)
            if accuracy_score(y, h) == 1:
                break
    def predict(self, X):
        '''
        Parameters
        ----------
        X : shape (n_samples, n_features)
            Predicting data
        Returns
        -------
        y : shape (n_samples,)
            Predicted class label per sample, 1 or -1
        '''
        return np.sign(X.dot(self.__W) + self.__b)
if __name__ == "__main__":
    X_train = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    y_train = np.array([1, 1, -1, -1])
    pla = Pla()
    pla.fit(X_train, y_train)
    X_test = np.array([[1, 1], [2, 2], [3, 3], [4, 4]])
    predictions = pla.predict(X_test)
    print("Predictions:", predictions)