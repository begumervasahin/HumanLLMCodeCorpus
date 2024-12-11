import numpy as np
import matplotlib.pyplot as plt
class class1:
    def fonk1(self):
        self.b1 = {1: 'r', -1: 'b12'}
        self.b2 = plt.figure()
        self.b3 = self.b2.add_subplot(1, 1, 1)
    def fonk2(self, b4):
        self.b4 = b4
        self.b5 = float('-inf')
        self.b6 = float('inf')
        for b13 in self.b4:
            for features in self.b4[b13]:
                self.b5 = max(self.b5, np.max(features))
                self.b6 = min(self.b6, np.min(features))
        b7 = [self.b5 * 0.1, self.b5 * 0.01, self.b5 * 0.001]
        a1 = 5
        a2 = 5
        b8 = self.b5 * 10
        for step in b7:
            b9 = np.array([b8, b8])
            b10 = False
            while not b10:
                for b12 in np.arange(-1 * self.b5 * a1, self.b5 * a1, step * a2):
                    for transformation in [[1, 1], [-1, 1], [-1, -1], [1, -1]]:
                        b11 = b9 * transformation
                        if self.fonk3(b11, b12):
                            self.b9 = b11
                            self.b12 = b12
                            b10 = True
                            break
                    if b10:
                        break
                if b9[0] < 0:
                    b10 = True
                else:
                    b9 -= step
    def fonk3(self, b9, b12):
        for i in self.b4:
            for x in self.b4[i]:
                b13 = i
                if not b13 * (np.dot(b9, x) + b12) >= 1:
                    return False
        return True
    def fonk4(self, features):
        b14 = np.sign(np.dot(features, self.b9) + self.b12)
        if b14 != 0:
            self.b3.scatter(features[0], features[1], b15 = 300, marker='*', c=self.b1[b14])
        return b14
    def fonk5(self):
        for i in self.b4:
            for x in self.b4[i]:
                self.b3.scatter(x[0], x[1], b15 = 50, c=self.b1[i])
        self.fonk6()
        plt.show()
    def fonk6(self):
        def fonk7(x, b9, b12, v):
            return (-b9[0] * x - b12 + v) / b9[1]
        b16 = (self.b6 * 0.9, self.b5 * 1.1)
        b17 = b16[0]
        b18 = b16[1]
        b19 = fonk7(b17, self.b9, self.b12, 1)
        b20 = fonk7(b18, self.b9, self.b12, 1)
        self.b3.plot([b17, b18], [b19, b20], 'k')
        b21 = fonk7(b17, self.b9, self.b12, -1)
        b22 = fonk7(b18, self.b9, self.b12, -1)
        self.b3.plot([b17, b18], [b21, b22], 'k')
        b23 = fonk7(b17, self.b9, self.b12, 0)
        b24 = fonk7(b18, self.b9, self.b12, 0)
        self.b3.plot([b17, b18], [b23, b24], 'b13--')
if b25 = = '__main__':
    b26 = {-1: np.array([[1, 7], [2, 8], [3, 8]]),
                1: np.array([[5, 1], [6, -1], [7, 3]])}
    b27 = class1()
    b27.fonk2(b26)
    for predict_feature in [[0, 10], [2, 6], [1, 3], [4, 3], [5.5, 7.5], [8, 3]]:
        print(b27.fonk4(predict_feature))
    b27.fonk5()