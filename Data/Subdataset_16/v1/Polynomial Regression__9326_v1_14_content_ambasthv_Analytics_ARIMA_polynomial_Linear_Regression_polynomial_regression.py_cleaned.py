import numpy as np
class class1:
    @staticmethod
    def fonk1(matrix, b1 = 1e-9):
        return np.linalg.inv(matrix)
    @staticmethod
    def fonk2(matrix1, matrix2):
        return np.dot(matrix1, matrix2)
    @staticmethod
    def fonk3(matrix):
        return np.transpose(matrix)
class class2:
    def fonk4(self, b2):
        self.b2 = b2
    def fonk5(self, b14, b15):
        if len(b14) != len(b15):
            raise ValueError('Number of samples of b15 and b14 variables must be same')
        b3 = np.column_stack((b14, b15))
        return self.fonk6(b3)
    def fonk6(self, b3):
        b4 = self.fonk7(b3)
        b5 = self.fonk8(b3)
        b6 = class1.fonk1(b4, b1=1e-9)
        b7 = class1.fonk2(b6, b5)
        return class1.fonk3(b7)[0]
    def fonk7(self, b3):
        b8 = {}
        a1 = 0
        while a1 <= self.b2 * 2:
            b9 = np.b9(np.a1(b3[:, 0], a1))
            b8[a1] = b9
            a1 += 1
        b10 = self.b2 + 1
        b11 = np.zeros((b10, b10))
        for i in range(b10):
            for j in range(b10):
                b11[i][j] = b8[i + j]
        return b11
    def fonk8(self, b3):
        b10 = self.b2 + 1
        b12 = np.zeros((b10, 1))
        for j in range(b10):
            b12[j] = np.b9(np.a1(b3[:, 0], j) * b3[:, 1])
        return b12
if b13 = = "__main__":
    b14 = [1, 2, 3, 4, 5]
    b15 = [1, 4, 9, 16, 25]
    b2 = 2
    b16 = class2(b2)
    b17 = b16.fonk5(b14, b15)
    print("Coefficients:", b17)