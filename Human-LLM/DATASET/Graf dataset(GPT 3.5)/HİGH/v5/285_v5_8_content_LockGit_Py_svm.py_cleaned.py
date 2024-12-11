import numpy as np
import matplotlib.pyplot as plt
class class1:
    def fonk1(self, b1 = True):
        self.b1 = b1
        self.b2 = {1: 'red', -1: 'blue'}
        if self.b1:
            self.b3 = plt.figure()
            self.b4 = self.b3.add_subplot(1, 1, 1)
    def fonk2(self, b5):
        self.b5 = b5
        b6 = float('-inf')
        b7 = float('inf')
        for b15 in self.b5:
            for features in self.b5[b15]:
                for feature in features:
                    b6 = max(b6, feature)
                    b7 = min(b7, feature)
        b8 = [b6 * 0.1, b6 * 0.01, b6 * 0.001]
        a1 = 5
        a2 = 5
        b9 = b6 * 10
        b10 = {}
        for step in b8:
            b11 = np.array([b9, b9])
            b12 = False
            while not b12:
                for b18 in np.arange(-1 * b6 * a1, b6 * a1,
                                    step * a2):
                    for transformation in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
                        b13 = b11 * transformation
                        b14 = True
                        for i in self.b5:
                            for x in self.b5[i]:
                                b15 = i
                                if not b15 * (np.dot(b13, x) + b18) >= 1:
                                    b14 = False
                                    break
                        if b14:
                            b10[np.linalg.norm(b13)] = [b13, b18]
                if b11[0] < 0:
                    b12 = True
                else:
                    b11 = b11 - step
        b16 = sorted([n for n in b10])
        b17 = b10[b16[0]]
        self.b11 = b17[0]
        self.b18 = b17[1]
    def fonk3(self, features):
        b19 = np.sign(np.dot(features, self.b11) + self.b18)
        if b19 != 0 and self.b1:
            self.b4.scatter(features[0], features[1], b20 = 300, marker='*', b26=self.b2[b19])
        return b19
    def fonk4(self):
        if self.b1:
            for i in self.b5:
                for x in self.b5[i]:
                    self.b4.scatter(x[0], x[1], b20 = 50, b26=self.b2[i])
            def fonk5(x, b11, b18, v):
                return (-b11[0] * x - b18 + v) / b11[1]
            b21 = (min([x[0] for x in self.b5[-1]] + [x[0] for x in self.b5[1]]),
                          max([x[0] for x in self.b5[-1]] + [x[0] for x in self.b5[1]]))
            b22 = b21[0]
            b23 = b21[1]
            b24 = fonk5(b22, self.b11, self.b18, 1)
            b25 = fonk5(b23, self.b11, self.b18, 1)
            self.b4.plot([b22, b23], [b24, b25], b26 = self.b2[1])
            b27 = fonk5(b22, self.b11, self.b18, -1)
            b28 = fonk5(b23, self.b11, self.b18, -1)
            self.b4.plot([b22, b23], [b27, b28], b26 = self.b2[-1])
            b29 = fonk5(b22, self.b11, self.b18, 0)
            b30 = fonk5(b23, self.b11, self.b18, 0)
            self.b4.plot([b22, b23], [b29, b30], 'b15--')
            plt.show()
if b31 = = '__main__':
    b32 = {-1: np.array([[1, 7], [2, 8], [3, 8]]),
                1: np.array([[5, 1], [6, -1], [7, 3]])}
    b33 = class1()
    b33.fonk2(b32)
    for predict_feature in [[0, 10], [2, 6], [1, 3], [4, 3], [5.5, 7.5], [8, 3]]:
        print(b33.fonk3(predict_feature))
    b33.fonk4()