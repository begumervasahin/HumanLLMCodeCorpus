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
        for b14 in self.b5:
            for features in self.b5[b14]:
                for feature in features:
                    b6 = max(b6, feature)
                    b7 = min(b7, feature)
        b8 = [b6 * 0.1, b6 * 0.01, b6 * 0.001]
        a1 = 5
        a2 = 5
        b9 = b6 * 10
        for step in b8:
            b10 = np.array([b9, b9])
            b11 = False
            while not b11:
                for b17 in np.arange(-1 * b6 * a1, b6 * a1,
                                    step * a2):
                    for transformation in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
                        b12 = b10 * transformation
                        b13 = True
                        for i in self.b5:
                            for x in self.b5[i]:
                                b14 = i
                                if not b14 * (np.dot(b12, x) + b17) >= 1:
                                    b13 = False
                                    break
                        if b13:
                            opt_dict[np.linalg.norm(b12)] = [b12, b17]
                if b10[0] < 0:
                    b11 = True
                else:
                    b10 = b10 - step
            b15 = sorted([n for n in opt_dict])
            b16 = opt_dict[b15[0]]
            self.b10 = b16[0]
            self.b17 = b16[1]
            b9 = b16[0][0] + step * 2
    def fonk3(self, features):
        b18 = np.sign(np.dot(features, self.b10) + self.b17)
        if b18 != 0 and self.b1:
            self.b4.scatter(features[0], features[1], b19 = 300, marker='*', b25=self.b2[b18])
        return b18
    def fonk4(self):
        if self.b1:
            for i in self.b5:
                for x in self.b5[i]:
                    self.b4.scatter(x[0], x[1], b19 = 50, b25=self.b2[i])
            def fonk5(x, b10, b17, v):
                return (-b10[0] * x - b17 + v) / b10[1]
            b20 = (self.b7 * 0.9, self.b6 * 1.1)
            b21 = b20[0]
            b22 = b20[1]
            b23 = fonk5(b21, self.b10, self.b17, 1)
            b24 = fonk5(b22, self.b10, self.b17, 1)
            self.b4.plot([b21, b22], [b23, b24], b25 = self.b2[1])
            b26 = fonk5(b21, self.b10, self.b17, -1)
            b27 = fonk5(b22, self.b10, self.b17, -1)
            self.b4.plot([b21, b22], [b26, b27], b25 = self.b2[-1])
            b28 = fonk5(b21, self.b10, self.b17, 0)
            b29 = fonk5(b22, self.b10, self.b17, 0)
            self.b4.plot([b21, b22], [b28, b29], 'b14--')
            plt.show()
if b30 = = '__main__':
    b31 = {-1: np.array([[1, 7], [2, 8], [3, 8]]),
                1: np.array([[5, 1], [6, -1], [7, 3]])}
    b32 = class1()
    b32.fonk2(b31)
    for predict_feature in [[0, 10], [2, 6], [1, 3], [4, 3], [5.5, 7.5], [8, 3]]:
        print(b32.fonk3(predict_feature))
    b32.fonk4()