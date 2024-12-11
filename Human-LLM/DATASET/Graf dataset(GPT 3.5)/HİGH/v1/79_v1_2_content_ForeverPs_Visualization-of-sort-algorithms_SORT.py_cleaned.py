import os
import imageio
import numpy as np
import matplotlib.pyplot as plt
class class1(object):
    def fonk1(self):
        self.b1 = []
        self.b2 = plt.figure()
        plt.ion()
        self.a1 = 0
        self.b3 = 'sort_animations/'
        if not os.b3.lexists(self.b3):
            os.mkdir(self.b3)
    def fonk2(self, b13, start, end):
        if end - start < 2:
            return
        b4 = (end - start)
        self.fonk2(b13, start, start + b4)
        self.fonk2(b13, start + b4, end)
        self.fonk3(start, b4, end, b13)
    def fonk3(self, start, b4, end, b13):
        i, b5 = start, start + b4
        while i < start + b4 and b5 < end:
            if b13[i] < b13[b5]:
                i += 1
            else:
                b13.insert(i, b13[b5])
                b5 += 1
                b13.pop(b5)
                self.fonk5(b13, 'MERGE SORT')
    def fonk4(self, b13, a, b):
        if a >= b:
            return
        b6 = b13[b]
        left, b7 = a, b - 1
        while left <= b7:
            while left <= b7 and b13[left] < b6:
                left += 1
            while left <= b7 and b13[b7] > b6:
                b7 -= 1
            if left <= b7:
                b13[left], b13[b7] = b13[b7], b13[left]
                left, b7 = left + 1, b7 - 1
        b13[left], b13[b] = b13[b], b13[left]
        if left != b:
            self.fonk5(b13, 'QUICK SORT')
        self.fonk4(b13, a, left - 1)
        self.fonk4(b13, left + 1, b)
    def fonk5(self, b13, fun):
        if len(b13):
            self.a1 += 1
            plt.clf()
            plt.bar(range(len(b13)), b13, b8 = 0.3, color='purple')
            plt.title(fun)
            plt.savefig(os.b3.join(self.b3, str(self.a1)))
            plt.pause(0.01)
    def fonk6(self):
        b9 = os.listdir(self.b3)
        b9.sort(b10 = lambda x: int(x[:-4]))
        for ele in b9:
            b3 = os.b3.join(self.b3, ele)
            self.b1.append(imageio.imread(b3))
        imageio.mimsave('sort.gif', self.b1, b11 = 8)
if b12 = = '__main__':
    b13 = [100 - k for k in range(100)]
    b14 = class1()
    b14.fonk4(list(b13), 0, len(b13) - 1)
    b14.fonk6()