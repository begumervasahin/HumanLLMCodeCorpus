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
        self.b7 = max(max(features) for features in b4.values())
        self.b8 = min(min(features) for features in b4.values())
        print(f"Max feature value: {self.b7}, Min feature value: {self.b8}")
        b9 = [
            self.b7 * 0.1,
            self.b7 * 0.01,
            self.b7 * 0.001,
        ]
        a1 = 5
        a2 = 5
        b10 = self.b7 * 10
        for step in b9:
            b11 = np.array([b10, b10])
            b12 = False
            while not b12:
                for b17 in np.arange(
                    -self.b7 * a1,
                    self.b7 * a1,
                    step * a2,
                ):
                    for transformation in b6:
                        b13 = b11 * transformation
                        b14 = all(
                            y * (np.dot(b13, x) + b17) >= 1
                            for y in b4
                            for x in b4[y]
                        )
                        if b14:
                            b5[np.linalg.norm(b13)] = [b13, b17]
                if b11[0] < 0:
                    b12 = True
                else:
                    b11 -= step
            b15 = sorted(b5)
            b16 = b5[b15[0]]
            self.b11, self.b17 = b16
            print(f"Optimal b11: {self.b11}, b17: {self.b17}")
            b10 = b16[0][0] + step * 2
    def fonk3(self, features):
        b18 = np.sign(np.dot(np.array(features), self.b11) + self.b17)
        if b18 != 0 and self.b1:
            self.b3.scatter(features[0], features[1], b19 = 300, marker='*', b24=self.b2[b18])
        return b18
    def fonk4(self):
        for y in self.b4:
            for x in self.b4[y]:
                self.b3.scatter(x[0], x[1], b19 = 50, b24=self.b2[y])
        def fonk5(x, b11, b17, v):
            return (-b11[0] * x - b17 + v) / b11[1]
        b20 = [self.b8 * 0.9, self.b7 * 1.1]
        hyp_x_min, b21 = b20
        b22 = fonk5(hyp_x_min, self.b11, self.b17, 1)
        b23 = fonk5(b21, self.b11, self.b17, 1)
        self.b3.plot([hyp_x_min, b21], [b22, b23], b24 = self.b2[1])
        b25 = fonk5(hyp_x_min, self.b11, self.b17, -1)
        b26 = fonk5(b21, self.b11, self.b17, -1)
        self.b3.plot([hyp_x_min, b21], [b25, b26], b24 = self.b2[-1])
        b27 = fonk5(hyp_x_min, self.b11, self.b17, 0)
        b28 = fonk5(b21, self.b11, self.b17, 0)
        self.b3.plot([hyp_x_min, b21], [b27, b28], 'y--')
        plt.show()
if b29 = = '__main__':
    b30 = {
        -1: np.array([[1, 7], [2, 8], [3, 8]]),
        1: np.array([[5, 1], [6, -1], [7, 3]]),
    }
    b31 = class1()
    b31.fonk2(b30)
    b32 = [[0, 10], [2, 6], [1, 3], [4, 3], [5.5, 7.5], [8, 3]]
    for point in b32:
        print(f"Point {point} classified as: {b31.fonk3(point)}")
    b31.fonk4()