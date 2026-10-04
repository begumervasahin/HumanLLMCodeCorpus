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
        X = np.hstack((np.ones((X.shape[0], 1)), X))
        A = np.hstack([self._as_tall((X ** p).prod(axis=1)) for p in self.powers])
        return np.dot(A, self.coefficients)
    def error(self, X, Y):
        predictions = self.predict(X)
        return np.mean((predictions - Y) ** 2)
    @staticmethod
    def _as_tall(x):
        return x.reshape(-1, 1)
class PolyPy:
    def __init__(self, split=0.15, max_validation=5):
        self.split_ratio = split
        self.max_validation_attempts = max_validation
        self.lowest_test_error = None
        self.best_degree = 0
        self.error_log = []
    def fit(self, dataset):
        train_X, train_Y, test_X, test_Y = self._split_dataset(dataset)
        self._find_best_degree(train_X, train_Y, test_X, test_Y)
        return self._fit_model_with_degree(dataset[:, :-1], dataset[:, -1], self.best_degree)
    def _split_dataset(self, dataset):
        np.random.shuffle(dataset)
        split_index = int(len(dataset) * self.split_ratio)
        train, test = dataset[:split_index], dataset[split_index:]
        return train[:, :-1], train[:, -1], test[:, :-1], test[:, -1]
    def _find_best_degree(self, train_X, train_Y, test_X, test_Y):
        validation_attempts_remaining = self.max_validation_attempts
        degree = 1
        while validation_attempts_remaining > 0:
            model = self._fit_model_with_degree(train_X, train_Y, degree)
            train_error = model.error(train_X, train_Y)
            test_error = model.error(test_X, test_Y)
            self._log_degree_info(degree, model.coefficients, train_error, test_error)
            self.error_log.append(test_error)
            if self.lowest_test_error is None or test_error < self.lowest_test_error:
                self.lowest_test_error = test_error
                self.best_degree = degree
                validation_attempts_remaining = self.max_validation_attempts
            else:
                validation_attempts_remaining -= 1
            degree += 1
    def _fit_model_with_degree(self, X, Y, degree):
        X_augmented = self._augment_features(X)
        powers = self._generate_powers(X.shape[1] + 1, degree)
        A = np.hstack([self._as_tall((X_augmented ** p).prod(axis=1)) for p in powers])
        coefficients, _, _, _ = lstsq(A, Y, rcond=None)
        return PolynomialModel(powers, coefficients, degree, X.shape[1])
    @staticmethod
    def _augment_features(X):
        num_samples = X.shape[0]
        return np.hstack((np.ones((num_samples, 1)), X))
    @staticmethod
    def _generate_powers(num_covariates, degree):
        generators = [PolyPy._basis_vector(num_covariates, i) for i in range(num_covariates)]
        return [sum(comb) for comb in itertools.combinations_with_replacement(generators, degree)]
    @staticmethod
    def _basis_vector(length, index):
        vector = np.zeros(length, dtype=int)
        vector[index] = 1
        return vector
    @staticmethod
    def _as_tall(x):
        return x.reshape(-1, 1)
    @staticmethod
    def _log_degree_info(degree, coefficients, train_error, test_error):
        print(f"Degree: {degree}")
        print(f"Model Coefficients: {coefficients}")
        print(f"Train error: {train_error}")
        print(f"Test error: {test_error}\n")
if __name__ == "__main__":
    dataset = np.random.rand(100, 3)
    poly_model = PolyPy()
    best_model = poly_model.fit(dataset)
    print("Best polynomial degree:", poly_model.best_degree)
    print("Model coefficients:", best_model.coefficients)