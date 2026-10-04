import numpy as np
from matplotlib import pyplot as plt
class class1:
    def fonk1(self, b1 = True):
        self.b1 = b1
        self.b2 = {1: 'r', -1: 'b18'}
        if self.b1:
            self.b3 = plt.figure()
            self.b4 = self.b3.add_subplot(1, 1, 1)
    def fonk2(self, b5):
        self.b5 = b5
        b6 = {}
        b7 = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
        self.b8 = max(max(map(max, b5.values())))
        self.b9 = min(min(map(min, b5.values())))
        print(f"Max feature value: {self.b8}, Min feature value: {self.b9}")
        b10 = [
            self.b8 * 0.1,
            self.b8 * 0.01,
            self.b8 * 0.001,
        ]
        a1 = 5
        a2 = 5
        b11 = self.b8 * 10
        for step in b10:
            b12 = np.array([b11, b11])
            b13 = False
            while not b13:
                for b18 in np.arange(
                    -self.b8 * a1,
                    self.b8 * a1,
                    step * a2,
                ):
                    for transformation in b7:
                        b14 = b12 * transformation
                        b15 = all(
                            y * (np.dot(b14, x) + b18) >= 1
                            for y in b5
                            for x in b5[y]
                        )
                        if b15:
                            b6[np.linalg.norm(b14)] = [b14, b18]
                if b12[0] < 0:
                    b13 = True
                else:
                    b12 -= step
            b16 = sorted(b6)
            b17 = b6[b16[0]]
            self.b12, self.b18 = b17
            print(f"Optimal b12: {self.b12}, b18: {self.b18}")
            b11 = b17[0][0] + step * 2
    def fonk3(self, features):
        b19 = np.sign(np.dot(np.array(features), self.b12) + self.b18)
        if b19 != 0 and self.b1:
            self.b4.scatter(features[0], features[1], b20 = 300, marker='*', b25=self.b2[b19])
        return b19
    def fonk4(self):
        for y in self.b5:
            for x in self.b5[y]:
                self.b4.scatter(x[0], x[1], b20 = 50, b25=self.b2[y])
        def fonk5(x, b12, b18, v):
            return (-b12[0] * x - b18 + v) / b12[1]
        b21 = [self.b9 * 0.9, self.b8 * 1.1]
        hyp_x_min, b22 = b21
        b23 = fonk5(hyp_x_min, self.b12, self.b18, 1)
        b24 = fonk5(b22, self.b12, self.b18, 1)
        self.b4.plot([hyp_x_min, b22], [b23, b24], b25 = self.b2[1])
        b26 = fonk5(hyp_x_min, self.b12, self.b18, -1)
        b27 = fonk5(b22, self.b12, self.b18, -1)
        self.b4.plot([hyp_x_min, b22], [b26, b27], b25 = self.b2[-1])
        b28 = fonk5(hyp_x_min, self.b12, self.b18, 0)
        b29 = fonk5(b22, self.b12, self.b18, 0)
        self.b4.plot([hyp_x_min, b22], [b28, b29], 'y--')
        plt.show()
if b30 = = '__main__':
    b31 = {
        -1: np.array([[1, 7], [2, 8], [3, 8]]),
        1: np.array([[5, 1], [6, -1], [7, 3]]),
    }
    print(b31)
    b32 = class1()
    b32.fonk2(b31)
    b33 = [[0, 10], [2, 6], [1, 3], [4, 3], [5.5, 7.5], [8, 3]]
    for point in b33:
        print(f"Point {point} classified as: {b32.fonk3(point)}")
    b32.fonk4()