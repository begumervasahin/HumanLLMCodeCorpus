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
        self.b3 = 'sp/'
        if not os.b3.lexists(self.b3):
            os.mkdir(self.b3)
    def fonk2(self, b18, start, end):
        if end - start < 2:
            return
        b4 = (end - start)
        self.fonk2(b18, start, start + b4)
        self.fonk2(b18, end - b4, end)
        self.fonk3(start, b4, end, b18)
    def fonk3(self, start, b4, end, b18):
        b9, b5 = start, b4
        while b9 < b4 and b5 < end:
            if b5 = = end or (b9 < b4 and b18[b9] < b18[b5]):
                b9 += 1
            else:
                b18.insert(b9, b18[b5])
                b5 += 1
                b18.pop(b5)
                self.fonk14(b18, 'MERGE SORT')
    def fonk4(self, b18, a, b):
        if a >= b:
            return
        b6 = b18[b]
        left, b7 = a, b - 1
        while left <= b7:
            while left <= b7 and b18[left] < b6:
                left += 1
            while left <= b7 and b18[b7] > b6:
                b7 -= 1
            if left <= b7:
                b18[left], b18[b7] = b18[b7], b18[left]
                left, b7 = left + 1, b7 - 1
        b18[left], b18[b] = b18[b], b18[left]
        if left != b:
            self.fonk14(b18, 'QUICK SORT')
        self.fonk4(b18, a, left - 1)
        self.fonk4(b18, left + 1, b)
    def fonk5(self, b18):
        self.fonk14(b18, 'SELECTION SORT')
        for b9 in range(len(b18)):
            if self.fonk6(b18, b9):
                self.fonk14(b18, 'SELECTION SORT')
    def fonk6(self, b18, b9):
        index, b8 = b9, b18[b9]
        for b5 in range(b9, len(b18)):
            if b18[b5] < b8:
                index, b8 = b5, b18[b5]
        b18[index], b18[b9] = b18[b9], b18[index]
        return index != b9
    def fonk7(self, b18, b4, length):
        b5 = 2 * b4 + 1
        if b5 = = length - 1:
            if b18[b4] < b18[b5]:
                b18[b4], b18[b5] = b18[b5], b18[b4]
        while b5 <  length - 1:
            if b18[b5] < b18[b5 + 1]:
                b5 += 1
            if b18[b4] > b18[b5]:
                break
            b18[b4], b18[b5], b4, b5 = b18[b5], b18[b4], b5, 2 * b5 + 1
    def fonk8(self, b18):
        b9 = len(b18)
        while b9 >= 0:
            self.fonk7(b18, b9, len(b18))
            b9 -= 1
        b9 = len(b18)
        while b9 > 0:
            b18[0], b18[b9 - 1], b9 = b18[b9 - 1], b18[0], b9 - 1
            self.fonk14(b18, 'HEAP SORT')
            self.fonk7(b18, 0, b9)
    def fonk9(self, b18):
        b9 = b5 = len(b18)
        while b9 > 0:
            if self.fonk10(b18, b5 - b9):
                self.fonk14(b18, 'INSERT SORT')
            b9 -= 1
    def fonk10(self, b18, k):
        index, b8 = k, b18[k]
        for b9 in range(k, len(b18)):
            if b18[b9] < b8:
                index, b8 = b9, b18[b9]
        b18[k], b18[index] = b18[index], b18[k]
        return index != k
    def fonk11(self, b18):
        a1, b10 = 1, int(np.log2(len(b18) + 1))
        while a1 <= b10:
            b11 = 2 ** (b10 - a1 + 1) - 1
            for b9 in range(0, len(b18) - b11):
                if self.fonk12(b18, b9, b9 + b11):
                    self.fonk14(b18, 'SHELL SORT')
            a1 += 1
    def fonk12(self, b18, start, end):
        index, b8 = start, b18[start]
        for b9 in range(start, end + 1):
            if b18[b9] < b8:
                index, b8 = b9, b18[b9]
        b18[start], b18[index] = b18[index], b18[start]
        return index != start
    def fonk13(self, b18):
        b12 = len(b18)
        for b5 in range(b12 - 1):
            for b9 in range(b12 - b5 - 1):
                if b18[b9] > b18[b9 + 1]:
                    b18[b9], b18[b9 + 1] = b18[b9 + 1], b18[b9]
                    self.fonk14(b18, 'BUBBLE SORT')
    def fonk14(self, b18, fun):
        if len(b18):
            self.a1 += 1
            plt.clf()
            plt.bar(range(len(b18)), b18, b13 = 0.3, color='purple')
            plt.title(fun)
            plt.savefig('sp/' + str(self.a1))
            plt.pause(0.01)
    def fonk15(self):
        b14 = os.listdir(self.b3)
        b14.sort(b15 = lambda x: int(x[:-4]))
        for ele in b14:
            b3 = self.b3 + ele
            self.b1.append(imageio.imread(b3))
        imageio.mimsave('sort.gif', self.b1, b16 = 8)
if b17 = = '__main__':
    b18 = [100 - k for k in range(100)]
    b19 = class1()
    b19.fonk5(list(b18))
    b19.fonk8(list(b18))
    b19.fonk4(list(b18), 0, len(b18) - 1)
    b19.fonk2(list(b18), 0, len(b18))
    b19.fonk9(list(b18))
    b19.fonk11(list(b18))
    b19.fonk15()