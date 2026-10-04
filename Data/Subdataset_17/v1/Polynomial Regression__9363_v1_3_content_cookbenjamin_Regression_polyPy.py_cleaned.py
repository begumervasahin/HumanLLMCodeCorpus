import numpy as np
import itertools
from numpy.linalg import lstsq
class PolynomialModel:
    def __init__(self, powers, coefficients, degree, num_covariates):
        self.powers = powers
        self.coefficients = coefficients
        self.degree = degree
        self.num_covariates = num_covariates
    def predict(self, X):
        X = np.hstack((np.ones((X.shape[0], 1), dtype=X.dtype), X))
        A = np.hstack(np.asarray([self.as_tall((X ** p).prod(1)) for p in self.powers]))
        return np.dot(A, self.coefficients)
    def error(self, X, Y):
        predictions = self.predict(X)
        return np.mean((predictions - Y) ** 2)
    def as_tall(self, x):
        return x.reshape(x.shape + (1,))
class polyPy:
    def __init__(self, split=0.15, max_validation=5):
        self._lowest_test_error = None
        self._max_validation = max_validation
        self._validation_timer = None
        self._split = split
        self._best_degree = 0
        self._error = []
    def fit(self, dataset):
        train_X, train_Y, test_X, test_Y = self.split(dataset)
        self.trial(train_X, train_Y, test_X, test_Y)
        model = self.fit_model_with_degree(dataset[:, :-1], dataset[:, -1], self._best_degree)
        return model
    def split(self, dataset):
        np.random.shuffle(dataset)
        index = int(len(dataset) * self._split)
        train_X = dataset[:index][:, :-1]
        train_Y = dataset[:index][:, -1]
        test_X = dataset[index:][:, :-1]
        test_Y = dataset[index:][:, -1]
        return train_X, train_Y, test_X, test_Y
    def trial(self, train_X, train_Y, test_X, test_Y):
        self._validation_timer = 5
        degree = 1
        while self._validation_timer > 0:
            model = self.fit_model_with_degree(train_X, train_Y, degree)
            print("Degree:", degree)
            print("Model Coefficients:", model.coefficients)
            error = model.error(test_X, test_Y)
            print("Train error:", model.error(train_X, train_Y))
            print("Test error:", error)
            print()
            self._error.append(error)
            self.check_error(error, degree)
            degree += 1
    def check_error(self, error, degree):
        if self._lowest_test_error is None or error < self._lowest_test_error:
            self._lowest_test_error = error
            self._best_degree = degree
            self._validation_timer = self._max_validation
        else:
            self._validation_timer -= 1
    def fit_model_with_degree(self, X, Y, degree):
        Y = np.asarray(Y).squeeze()
        rows = Y.shape[0]
        X = np.asarray(X)
        num_covariates = X.shape[1]
        X = np.hstack((np.ones((X.shape[0], 1), dtype=X.dtype), X))
        generators = [self.basis_vector(num_covariates + 1, i) for i in range(num_covariates + 1)]
        powers = list(map(sum, itertools.combinations_with_replacement(generators, degree)))
        A = np.hstack(np.asarray([self.as_tall((X ** p).prod(1)) for p in powers]))
        beta, _, _, _ = lstsq(A, Y, rcond=None)
        model = PolynomialModel(powers, beta, degree, num_covariates)
        return model
    def basis_vector(self, n, i):
        x = np.zeros(n, dtype=int)
        x[i] = 1
        return x
    def as_tall(self, x):
        return x.reshape(x.shape + (1,))
if __name__ == "__main__":
    dataset = np.random.rand(100, 3)
    poly_model = polyPy()
    best_model = poly_model.fit(dataset)
    print("Best polynomial degree:", poly_model._best_degree)
    print("Model coefficients:", best_model.coefficients)