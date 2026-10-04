import numpy as np
from matplotlib import pyplot as plt
class class1:
    def fonk1(self, b1 = True):
        self.b1 = b1
        self.b2 = {1: 'r', -1: 'b17'}
        if self.b1:
            self.fig, self.b3 = plt.subplots()
    def fonk2(self, b4):
        self.b4 = b4
        b5 = {}
        b6 = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
        self.b7 = max(max(features) for label in b4 for features in b4[label])
        self.b8 = min(min(features) for label in b4 for features in b4[label])
        b9 = [self.b7 * factor for factor in [0.1, 0.01, 0.001]]
        a1 = 5
        a2 = 5
        b10 = self.b7 * 10
        for step in b9:
            b11 = np.array([b10, b10])
            b12 = False
            while not b12:
                for b17 in np.arange(-self.b7 * a1,
                                   self.b7 * a1,
                                   step * a2):
                    for transformation in b6:
                        b13 = b11 * transformation
                        b14 = True
                        for label in b4:
                            for x in b4[label]:
                                if not label * (np.dot(b13, x) + b17) >= 1:
                                    b14 = False
                                    break
                            if not b14:
                                break
                        if b14:
                            b5[np.linalg.norm(b13)] = [b13, b17]
                if b11[0] < 0:
                    b12 = True
                else:
                    b11 -= step
            b15 = sorted(b5.keys())
            b16 = b5[b15[0]]
            self.b11, self.b17 = b16
            b10 = b16[0][0] + step * 2
    def fonk3(self, features):
        b18 = np.sign(np.dot(np.array(features), self.b11) + self.b17)
        if b18 != 0 and self.b1:
            self.b3.scatter(features[0], features[1], b19 = 300, marker='*', c=self.b2[b18])
        return b18
    def fonk4(self):
        for label in self.b4:
            for x in self.b4[label]:
                self.b3.scatter(x[0], x[1], b19 = 50, c=self.b2[label])
        def fonk5(x, b11, b17, v):
            return (-b11[0] * x - b17 + v) / b11[1]
        b20 = (self.b8 * 0.9, self.b7 * 1.1)
        hyp_x_min, b21 = b20
        for v, color in zip([1, -1, 0], ['k', 'k', 'y--']):
            b22 = fonk5(hyp_x_min, self.b11, self.b17, v)
            b23 = fonk5(b21, self.b11, self.b17, v)
            self.b3.plot([hyp_x_min, b21], [b22, b23], color)
        plt.show()
if b24 = = '__main__':
    b25 = {
        -1: np.array([[1, 7], [2, 8], [3, 8]]),
        1: np.array([[5, 1], [6, -1], [7, 3]])
    }
    b26 = class1()
    b26.fonk2(b25)
    b27 = [[0, 10], [2, 6], [1, 3], [4, 3], [5.5, 7.5], [8, 3]]
    for point in b27:
        print(f"Prediction for {point}: {b26.fonk3(point)}")
    b26.fonk4()