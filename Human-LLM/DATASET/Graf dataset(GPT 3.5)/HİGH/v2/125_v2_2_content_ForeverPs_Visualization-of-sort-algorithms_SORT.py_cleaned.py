import os
import imageio
import numpy as np
import matplotlib.pyplot as plt
class class1:
    def fonk1(self):
        self.b1 = []
        self.b2 = plt.figure()
        plt.ion()
        self.a1 = 0
        self.b3 = 'sort_animations/'
        if not os.b3.lexists(self.b3):
            os.mkdir(self.b3)
    def fonk2(self, s, start, end):
        if end - start < 2:
            return
        b4 = (end - start)
        self.fonk2(s, start, start + b4)
        self.fonk2(s, start + b4, end)
        self.fonk3(start, b4, end, s)
    def fonk3(self, start, b4, end, s):
        i, b5 = start, start + b4
        while i < start + b4 and b5 < end:
            if s[i] < s[b5]:
                i += 1
            else:
                s.insert(i, s[b5])
                b5 += 1
                s.pop(b5)
                self.fonk5(s, 'MERGE SORT')
    def fonk4(self, s, low, high):
        if low >= high:
            return
        b6 = s[high]
        left, b7 = low, high - 1
        while left <= b7:
            while left <= b7 and s[left] < b6:
                left += 1
            while left <= b7 and s[b7] > b6:
                b7 -= 1
            if left <= b7:
                s[left], s[b7] = s[b7], s[left]
                left, b7 = left + 1, b7 - 1
        s[left], s[high] = s[high], s[left]
        if left != high:
            self.fonk5(s, 'QUICK SORT')
        self.fonk4(s, low, left - 1)
        self.fonk4(s, left + 1, high)
    def fonk5(self, s, algorithm_name):
        if len(s):
            self.a1 += 1
            plt.clf()
            plt.bar(range(len(s)), s, b8 = 0.3, color='purple')
            plt.title(algorithm_name)
            plt.savefig(os.b3.join(self.b3, str(self.a1)))
            plt.pause(0.01)
    def fonk6(self):
        b9 = os.listdir(self.b3)
        b9.sort(b10 = lambda x: int(x[:-4]))
        for filename in b9:
            b11 = os.b3.join(self.b3, filename)
            self.b1.append(imageio.imread(b11))
        imageio.mimsave('sort.gif', self.b1, b12 = 8)
if b13 = = '__main__':
    b14 = [100 - k for k in range(100)]
    b15 = class1()
    b15.fonk4(list(b14), 0, len(b14) - 1)
    b15.fonk6()