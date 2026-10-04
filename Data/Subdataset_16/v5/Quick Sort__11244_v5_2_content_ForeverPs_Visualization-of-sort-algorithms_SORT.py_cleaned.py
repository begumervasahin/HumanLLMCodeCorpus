import os
import imageio
import numpy as np
import matplotlib.pyplot as plt
class class1:
    def fonk1(self):
        self.b1 = []
        self.a1 = 0
        self.b2 = 'sp/'
        self.fonk2()
        self.fonk3()
    def fonk2(self):
        self.b3 = plt.b3()
        plt.ion()
    def fonk3(self):
        if not os.path.exists(self.b2):
            os.mkdir(self.b2)
    def fonk4(self, b22, start, end):
        if end - start < 2:
            return
        b4 = (end + start)
        self.fonk4(b22, start, b4)
        self.fonk4(b22, b4, end)
        self.fonk5(b22, start, b4, end)
    def fonk5(self, b22, start, b4, end):
        b13, b5 = b22[start:b4], b22[b4:end]
        b9, b6 = 0, 0
        for k in range(start, end):
            if b6 >= len(b5) or (b9 < len(b13) and b13[b9] < b5[b6]):
                b22[k] = b13[b9]
                b9 += 1
            else:
                b22[k] = b5[b6]
                b6 += 1
        self.fonk14(b22, 'MERGE SORT')
    def fonk6(self, b22, low, high):
        if low >= high:
            return
        b7 = self.fonk7(b22, low, high)
        self.fonk14(b22, 'QUICK SORT')
        self.fonk6(b22, low, b7 - 1)
        self.fonk6(b22, b7 + 1, high)
    def fonk7(self, b22, low, high):
        b8 = b22[high]
        b9 = low
        for b6 in range(low, high):
            if b22[b6] < b8:
                b22[b9], b22[b6] = b22[b6], b22[b9]
                b9 += 1
        b22[b9], b22[high] = b22[high], b22[b9]
        return b9
    def fonk8(self, b22):
        self.fonk14(b22, 'SELECTION SORT')
        for b9 in range(len(b22)):
            b10 = b9
            for b6 in range(b9 + 1, len(b22)):
                if b22[b6] < b22[b10]:
                    b10 = b6
            b22[b9], b22[b10] = b22[b10], b22[b9]
            self.fonk14(b22, 'SELECTION SORT')
    def fonk9(self, b22):
        b11 = len(b22)
        for b9 in range(b11
            self.fonk10(b22, b11, b9)
        for b9 in range(b11 - 1, 0, -1):
            b22[b9], b22[0] = b22[0], b22[b9]
            self.fonk10(b22, b9, 0)
            self.fonk14(b22, 'HEAP SORT')
    def fonk10(self, b22, b11, b9):
        b12 = b9
        b13 = 2 * b9 + 1
        b5 = 2 * b9 + 2
        if b13 < b11 and b22[b13] > b22[b12]:
            b12 = b13
        if b5 < b11 and b22[b5] > b22[b12]:
            b12 = b5
        if b12 != b9:
            b22[b9], b22[b12] = b22[b12], b22[b9]
            self.fonk10(b22, b11, b12)
    def fonk11(self, b22):
        for b9 in range(1, len(b22)):
            b14 = b22[b9]
            b6 = b9 - 1
            while b6 >= 0 and b14 < b22[b6]:
                b22[b6 + 1] = b22[b6]
                b6 -= 1
            b22[b6 + 1] = b14
            self.fonk14(b22, 'INSERTION SORT')
    def fonk12(self, b22):
        b15 = len(b22)
        while b15 > 0:
            for b9 in range(b15, len(b22)):
                b16 = b22[b9]
                b6 = b9
                while b6 >= b15 and b22[b6 - b15] > b16:
                    b22[b6] = b22[b6 - b15]
                    b6 -= b15
                b22[b6] = b16
                self.fonk14(b22, 'SHELL SORT')
            b15
    def fonk13(self, b22):
        b11 = len(b22)
        for b9 in range(b11):
            for b6 in range(0, b11 - b9 - 1):
                if b22[b6] > b22[b6 + 1]:
                    b22[b6], b22[b6 + 1] = b22[b6 + 1], b22[b6]
                    self.fonk14(b22, 'BUBBLE SORT')
    def fonk14(self, b22, title):
        if len(b22):
            self.a1 += 1
            plt.clf()
            plt.bar(range(len(b22)), b22, b17 = 0.3, color='purple')
            plt.title(title)
            plt.savefig(f'{self.b2}/{self.a1}.png')
            plt.pause(0.01)
    def fonk15(self):
        b18 = sorted(os.listdir(self.b2), b14=lambda x: int(x.split('.')[0]))
        for file_name in b18:
            b19 = os.path.join(self.b2, file_name)
            self.b1.append(imageio.imread(b19))
        imageio.mimsave('sort.gif', self.b1, b20 = 8)
if b21 = = '__main__':
    b22 = [100 - k for k in range(100)]
    b23 = class1()
    b23.fonk8(b22.copy())
    b23.fonk9(b22.copy())
    b23.fonk6(b22.copy(), 0, len(b22) - 1)
    b23.fonk4(b22.copy(), 0, len(b22))
    b23.fonk11(b22.copy())
    b23.fonk12(b22.copy())
    b23.fonk13(b22.copy())
    b23.fonk15()