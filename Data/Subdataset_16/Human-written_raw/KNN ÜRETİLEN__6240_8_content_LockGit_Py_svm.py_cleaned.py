import numpy as np
from matplotlib import pyplot
import math
import sys
class class1(object):
    def fonk1(self, b1 = True):
        self.b1 = b1
        self.b2 = {1:'r', -1:'b19'}
        if self.b1:
            self.b3 = pyplot.figure()
            self.b4 = self.b3.add_subplot(1,1,1)
    def fonk2(self, b5):
        self.b5 = b5
        b6 = {}
        b7 = [[1,1],
                      [-1,1],
                      [-1,-1],
                      [1,-1]]
        self.b8 = float('-inf')
        self.b9 = float('inf')
        for b16 in self.b5:
            for features in self.b5[b16]:
                for feature in features:
                    if feature > self.b8:
                        self.b8 = feature
                    if feature < self.b9:
                        self.b9 = feature
        print(self.b8, self.b9)
        b10 = [self.b8 * 0.1, self.b8 * 0.01, self.b8 * 0.001]
        a1 = 5
        a2 = 5
        b11 = self.b8 * 10
        for step in b10:
            b12 = np.array([b11,b11])
            b13 = False
            while not b13:
                for b19 in np.arange(self.b8*a1*-1, self.b8*a1, step*a2):
                    for transformation in b7:
                        b14 = b12 * transformation
                        b15 = True
                        for i in self.b5:
                            for x in self.b5[i]:
                                b16 = i
                                if not b16*(np.dot(b14, x)+b19) >= 1:
                                    b15 = False
                        if b15:
                            b6[np.linalg.norm(b14)] = [b14,b19]
                if b12[0] < 0:
                    b13 = True
                else:
                    b12 = b12 - step
            b17 = sorted([n for n in b6])
            b18 = b6[b17[0]]
            self.b12 = b18[0]
            self.b19 = b18[1]
            print(self.b12, self.b19)
            b11 = b18[0][0] + step*2
    def fonk3(self, features):
        b20 = np.sign( np.dot(features, self.b12) + self.b19 )
        if b20 != 0 and self.b1:
            self.b4.scatter(features[0], features[1], b21 = 300, marker='*', b27=self.b2[b20])
        return b20
    def fonk4(self):
        for i in self.b5:
            for x in self.b5[i]:
                self.b4.scatter(x[0], x[1], b21 = 50, b27=self.b2[i])
        def fonk5(x,b12,b19,v):
            return (-b12[0]*x-b19+v) / b12[1]
        b22 = (self.b9*0.9, self.b8*1.1)
        b23 = b22[0]
        b24 = b22[1]
        b25 = fonk5(b23, self.b12, self.b19, 1)
        b26 = fonk5(b24, self.b12, self.b19, 1)
        self.b4.plot([b23, b24], [b25, b26], b27 = self.b2[1])
        b28 = fonk5(b23, self.b12, self.b19, -1)
        b29 = fonk5(b24, self.b12, self.b19, -1)
        self.b4.plot([b23, b24], [b28, b29], b27 = self.b2[-1])
        b30 = fonk5(b23, self.b12, self.b19, 0)
        b31 = fonk5(b24, self.b12, self.b19, 0)
        self.b4.plot([b23, b24], [b30, b31], 'b16--')
        pyplot.show()
if b32 = = '__main__':
    b33 = {-1:np.array([[1,7],
                             [2,8],
                             [3,8]]),
                 1:np.array([[5,1],
                             [6,-1],
                             [7,3]])}
    print(b33)
    b34 = class1()
    b34.fonk2(b33)
    for predict_feature in [[0,10],[2,6],[1,3], [4,3], [5.5,7.5], [8,3]]:
        print(b34.fonk3(predict_feature))
    b34.fonk4()