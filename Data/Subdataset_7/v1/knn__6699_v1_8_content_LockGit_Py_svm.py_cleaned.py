import numpy as np
import matplotlib.pyplot as plt
class class1:
    def fonk1(self):
        self.b1 = {1: 'r', -1: 'b14'}
        self.b2 = plt.figure()
        self.b3 = self.b2.add_subplot(1, 1, 1)
    def fonk2(self, b4):
        self.b4 = b4
        self.b5 = float('-inf')
        self.b6 = float('inf')
        for b13 in self.b4:
            for features in self.b4[b13]:
                for feature in features:
                    if feature > self.b5:
                        self.b5 = feature
                    if feature < self.b6:
                        self.b6 = feature
        b7 = [self.b5 * 0.1, self.b5 * 0.01, self.b5 * 0.001]
        a1 = 5
        a2 = 5
        b8 = self.b5 * 10
        for step in b7:
            b9 = np.array([b8, b8])
            b10 = False
            while not b10:
                for b14 in np.arange(-1 * self.b5 * a1, self.b5 * a1, step * a2):
                    for transformation in [[1, 1], [-1, 1], [-1, -1], [1, -1]]:
                        b11 = b9 * transformation
                        b12 = True
                        for i in self.b4:
                            for x in self.b4[i]:
                                b13 = i
                                if not b13 * (np.dot(b11, x) + b14) >= 1:
                                    b12 = False
                        if b12:
                            self.b9 = b11
                            self.b14 = b14
                            b10 = True
                if b9[0] < 0:
                    b10 = True
                else:
                    b9 -= step
    def fonk3(self, features):
        b15 = np.sign(np.dot(features, self.b9) + self.b14)
        if b15 != 0:
            self.b3.scatter(features[0], features[1], b16 = 300, marker='*', c=self.b1[b15])
        return b15
    def fonk4(self):
        for i in self.b4:
            for x in self.b4[i]:
                self.b3.scatter(x[0], x[1], b16 = 50, c=self.b1[i])
        def fonk5(x, b9, b14, v):
            return (-b9[0] * x - b14 + v) / b9[1]
        b17 = (self.b6 * 0.9, self.b5 * 1.1)
        b18 = b17[0]
        b19 = b17[1]
        b20 = fonk5(b18, self.b9, self.b14, 1)
        b21 = fonk5(b19, self.b9, self.b14, 1)
        self.b3.plot([b18, b19], [b20, b21], 'k')
        b22 = fonk5(b18, self.b9, self.b14, -1)
        b23 = fonk5(b19, self.b9, self.b14, -1)
        self.b3.plot([b18, b19], [b22, b23], 'k')
        b24 = fonk5(b18, self.b9, self.b14, 0)
        b25 = fonk5(b19, self.b9, self.b14, 0)
        self.b3.plot([b18, b19], [b24, b25], 'b13--')
        plt.show()
if b26 = = '__main__':
    b27 = {-1: np.array([[1, 7], [2, 8], [3, 8]]),
                1: np.array([[5, 1], [6, -1], [7, 3]])}
    b28 = class1()
    b28.fonk2(b27)
    for predict_feature in [[0, 10], [2, 6], [1, 3], [4, 3], [5.5, 7.5], [8, 3]]:
        print(b28.fonk3(predict_feature))
    b28.fonk4()