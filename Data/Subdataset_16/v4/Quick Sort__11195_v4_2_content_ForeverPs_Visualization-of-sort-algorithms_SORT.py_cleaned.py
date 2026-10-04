import os
import imageio
import numpy as np
import matplotlib.pyplot as plt
class class1:
    def fonk1(self):
        self.b1 = []
        self.b2 = plt.b2()
        plt.ion()
        self.a1 = 0
        self.b3 = 'sp/'
        if not os.path.exists(self.b3):
            os.mkdir(self.b3)
    def fonk2(self, b22, start, end):
        if end - start < 2:
            return
        b4 = (end + start)
        self.fonk2(b22, start, b4)
        self.fonk2(b22, b4, end)
        self.fonk3(b22, start, b4, end)
    def fonk3(self, b22, start, b4, end):
        b12, b5 = b22[start:b4], b22[b4:end]
        b6 = b14 = 0
        for k in range(start, end):
            if b14 >= len(b5) or (b6 < len(b12) and b12[b6] < b5[b14]):
                b22[k] = b12[b6]
                b6 += 1
            else:
                b22[k] = b5[b14]
                b14 += 1
        self.fonk12(b22, 'MERGE SORT')
    def fonk4(self, b22, low, high):
        if low >= high:
            return
        b7 = self.fonk5(b22, low, high)
        self.fonk12(b22, 'QUICK SORT')
        self.fonk4(b22, low, b7 - 1)
        self.fonk4(b22, b7 + 1, high)
    def fonk5(self, b22, low, high):
        b8 = b22[high]
        b6 = low
        for b14 in range(low, high):
            if b22[b14] < b8:
                b22[b6], b22[b14] = b22[b14], b22[b6]
                b6 += 1
        b22[b6], b22[high] = b22[high], b22[b6]
        return b6
    def fonk6(self, b22):
        self.fonk12(b22, 'SELECTION SORT')
        for b6 in range(len(b22)):
            b9 = b6
            for b14 in range(b6 + 1, len(b22)):
                if b22[b14] < b22[b9]:
                    b9 = b14
            b22[b6], b22[b9] = b22[b9], b22[b6]
            self.fonk12(b22, 'SELECTION SORT')
    def fonk7(self, b22):
        b10 = len(b22)
        for b6 in range(b10
            self.fonk8(b22, b10, b6)
        for b6 in range(b10 - 1, 0, -1):
            b22[b6], b22[0] = b22[0], b22[b6]
            self.fonk8(b22, b6, 0)
            self.fonk12(b22, 'HEAP SORT')
    def fonk8(self, b22, b10, b6):
        b11 = b6
        b12 = 2 * b6 + 1
        b5 = 2 * b6 + 2
        if b12 < b10 and b22[b12] > b22[b11]:
            b11 = b12
        if b5 < b10 and b22[b5] > b22[b11]:
            b11 = b5
        if b11 != b6:
            b22[b6], b22[b11] = b22[b11], b22[b6]
            self.fonk8(b22, b10, b11)
    def fonk9(self, b22):
        for b6 in range(1, len(b22)):
            b13 = b22[b6]
            b14 = b6 - 1
            while b14 >= 0 and b13 < b22[b14]:
                b22[b14 + 1] = b22[b14]
                b14 -= 1
            b22[b14 + 1] = b13
            self.fonk12(b22, 'INSERTION SORT')
    def fonk10(self, b22):
        b15 = len(b22)
        while b15 > 0:
            for b6 in range(b15, len(b22)):
                b16 = b22[b6]
                b14 = b6
                while b14 >= b15 and b22[b14 - b15] > b16:
                    b22[b14] = b22[b14 - b15]
                    b14 -= b15
                b22[b14] = b16
                self.fonk12(b22, 'SHELL SORT')
            b15
    def fonk11(self, b22):
        b10 = len(b22)
        for b6 in range(b10):
            for b14 in range(0, b10 - b6 - 1):
                if b22[b14] > b22[b14 + 1]:
                    b22[b14], b22[b14 + 1] = b22[b14 + 1], b22[b14]
                    self.fonk12(b22, 'BUBBLE SORT')
    def fonk12(self, b22, title):
        if len(b22):
            self.a1 += 1
            plt.clf()
            plt.bar(range(len(b22)), b22, b17 = 0.3, color='purple')
            plt.title(title)
            plt.savefig(f'{self.b3}/{self.a1}.png')
            plt.pause(0.01)
    def fonk13(self):
        b18 = sorted(os.listdir(self.b3), b13=lambda x: int(x.split('.')[0]))
        for file_name in b18:
            b19 = os.path.join(self.b3, file_name)
            self.b1.append(imageio.imread(b19))
        imageio.mimsave('sort.gif', self.b1, b20 = 8)
if b21 = = '__main__':
    b22 = [100 - k for k in range(100)]
    b23 = class1()
    b23.fonk6(b22.copy())
    b23.fonk7(b22.copy())
    b23.fonk4(b22.copy(), 0, len(b22) - 1)
    b23.fonk2(b22.copy(), 0, len(b22))
    b23.fonk9(b22.copy())
    b23.fonk10(b22.copy())
    b23.fonk11(b22.copy())
    b23.fonk13()