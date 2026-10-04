import matrix_operation as mo
class PolynomialRegression:
    def __init__(self, order):
        self.order = order
    def fit(self, independent, dependent):
        if len(independent) != len(dependent):
            raise ValueError('Number of samples of dependent and independent variables must be the same')
        data = list(zip(independent, dependent))
        return self._fit(data)
    def _fit(self, data):
        A = self._get_coefficient_matrix(data)
        b = self._get_result_vector(data)
        A_inverse = mo.getMatrixInverse(A, tol=1)
        X = mo.multiply(A_inverse, b)
        return mo.transposeMatrix(X)[0]
    def _get_coefficient_matrix(self, data):
        power_sums = {power: sum(x**power for x, _ in data) for power in range(self.order * 2 + 1)}
        dim = self.order + 1
        coefficient_matrix = [[power_sums[i + j] for j in range(dim)] for i in range(dim)]
        return coefficient_matrix
    def _get_result_vector(self, data):
        dim = self.order + 1
        result_vector = [[sum((x**j) * y for x, y in data)] for j in range(dim)]
        return result_vector