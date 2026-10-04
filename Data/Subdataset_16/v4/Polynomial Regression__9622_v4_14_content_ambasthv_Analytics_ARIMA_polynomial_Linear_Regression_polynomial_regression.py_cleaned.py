import matrix_operation as mo
class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self, independent, dependent):
        if len(independent) != len(dependent):
            raise ValueError('Number of samples of dependent and independent variables must be the same')
        b2 = list(zip(independent, dependent))
        return self.fonk3(b2)
    def fonk3(self, b2):
        b3 = self.fonk4(b2)
        b4 = self.fonk5(b2)
        b5 = mo.getMatrixInverse(b3, tol=1)
        b6 = mo.multiply(b5, b4)
        return mo.transposeMatrix(b6)[0]
    def fonk4(self, b2):
        b7 = {power: sum(x**power for x, _ in b2) for power in range(self.b1 * 2 + 1)}
        b8 = self.b1 + 1
        b9 = [[b7[i + j] for j in range(b8)] for i in range(b8)]
        return b9
    def fonk5(self, b2):
        b8 = self.b1 + 1
        b10 = [[sum((x**j) * y for x, y in b2)] for j in range(b8)]
        return b10