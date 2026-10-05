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
                prediction = self.predict_sample(X_train[i])
                if y_train[i] * prediction <= 0:
                    self.update_weights(X_train[i], y_train[i])
            predictions = self.predict(X_train)
            if self.check_convergence(y_train, predictions):
                break
    def predict_sample(self, sample):
        '''
        Predict class label for a single input sample.
        Parameters
        ----------
        sample : numpy.ndarray
            Input sample of shape (n_features,).
        Returns
        -------
        int
            Predicted class label, 1 or -1.
        '''
        return np.sign(np.dot(sample, self.weights) + self.bias)
    def update_weights(self, sample, target):
        '''
        Update weights and bias based on misclassified sample.
        Parameters
        ----------
        sample : numpy.ndarray
            Input sample of shape (n_features,).
        target : int
            Target class label for the sample, 1 or -1.
        '''
        self.weights += target * sample
        self.bias += target
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
        return np.sign(np.dot(X, self.weights) + self.bias)
    def check_convergence(self, y_true, y_pred):
        '''
        Check if the model has converged based on accuracy.
        Parameters
        ----------
        y_true : numpy.ndarray
            True class labels of shape (n_samples,).
        y_pred : numpy.ndarray
            Predicted class labels of shape (n_samples,).
        Returns
        -------
        bool
            True if accuracy is 100%, False otherwise.
        '''
        return accuracy_score(y_true, y_pred) == 1
if __name__ == "__main__":
    X_train = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    y_train = np.array([1, 1, -1, -1])
    pla = PerceptronLearningAlgorithm()
    pla.fit(X_train, y_train)
    X_test = np.array([[1, 1], [2, 2], [3, 3], [4, 4]])
    predictions = pla.predict(X_test)
    print("Predictions:", predictions)