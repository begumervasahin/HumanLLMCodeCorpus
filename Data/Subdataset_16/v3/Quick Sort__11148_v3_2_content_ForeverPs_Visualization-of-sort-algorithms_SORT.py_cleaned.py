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
        if not os.b3.exists(self.b3):
            os.mkdir(self.b3)
    def fonk2(self, arr, start, end):
        if end - start < 2:
            return
        b4 = (end + start)
        self.fonk2(arr, start, b4)
        self.fonk2(arr, b4, end)
        self.fonk3(arr, start, b4, end)
    def fonk3(self, arr, start, b4, end):
        b5 = arr[start:b4]
        b6 = arr[b4:end]
        b7 = start
        while b5 and b6:
            if b5[0] <= b6[0]:
                arr[b7] = b5.pop(0)
            else:
                arr[b7] = b6.pop(0)
            b7 += 1
            self.fonk12(arr, 'MERGE SORT')
        while b5:
            arr[b7] = b5.pop(0)
            b7 += 1
        while b6:
            arr[b7] = b6.pop(0)
            b7 += 1
    def fonk4(self, arr, low, high):
        if low < high:
            b8 = self.fonk5(arr, low, high)
            self.fonk4(arr, low, b8 - 1)
            self.fonk4(arr, b8 + 1, high)
    def fonk5(self, arr, low, high):
        b9 = arr[high]
        b10 = low - 1
        for b15 in range(low, high):
            if arr[b15] <= b9:
                b10 += 1
                arr[b10], arr[b15] = arr[b15], arr[b10]
        arr[b10 + 1], arr[high] = arr[high], arr[b10 + 1]
        self.fonk12(arr, 'QUICK SORT')
        return b10 + 1
    def fonk6(self, arr):
        for b10 in range(len(arr)):
            b11 = b10
            for b15 in range(b10 + 1, len(arr)):
                if arr[b15] < arr[b11]:
                    b11 = b15
            arr[b10], arr[b11] = arr[b11], arr[b10]
            self.fonk12(arr, 'SELECTION SORT')
    def fonk7(self, arr):
        b12 = len(arr)
        for b10 in range(b12
            self.fonk8(arr, b12, b10)
        for b10 in range(b12 - 1, 0, -1):
            arr[b10], arr[0] = arr[0], arr[b10]
            self.fonk8(arr, b10, 0)
            self.fonk12(arr, 'HEAP SORT')
    def fonk8(self, arr, b12, b10):
        b13 = b10
        b5 = 2 * b10 + 1
        b6 = 2 * b10 + 2
        if b5 < b12 and arr[b5] > arr[b13]:
            b13 = b5
        if b6 < b12 and arr[b6] > arr[b13]:
            b13 = b6
        if b13 != b10:
            arr[b10], arr[b13] = arr[b13], arr[b10]
            self.fonk8(arr, b12, b13)
    def fonk9(self, arr):
        for b10 in range(1, len(arr)):
            b14 = arr[b10]
            b15 = b10 - 1
            while b15 >= 0 and b14 < arr[b15]:
                arr[b15 + 1] = arr[b15]
                b15 -= 1
            arr[b15 + 1] = b14
            self.fonk12(arr, 'INSERTION SORT')
    def fonk10(self, arr):
        b12 = len(arr)
        b16 = b12
        while b16 > 0:
            for b10 in range(b16, b12):
                b17 = arr[b10]
                b15 = b10
                while b15 >= b16 and arr[b15 - b16] > b17:
                    arr[b15] = arr[b15 - b16]
                    b15 -= b16
                arr[b15] = b17
                self.fonk12(arr, 'SHELL SORT')
            b16
    def fonk11(self, arr):
        b12 = len(arr)
        for b10 in range(b12):
            for b15 in range(0, b12 - b10 - 1):
                if arr[b15] > arr[b15 + 1]:
                    arr[b15], arr[b15 + 1] = arr[b15 + 1], arr[b15]
                    self.fonk12(arr, 'BUBBLE SORT')
    def fonk12(self, arr, title):
        self.a1 += 1
        plt.clf()
        plt.bar(range(len(arr)), arr, b18 = 0.3, color='purple')
        plt.title(title)
        plt.savefig(f'{self.b3}{self.a1}.png')
        plt.pause(0.01)
    def fonk13(self):
        b19 = sorted(os.listdir(self.b3), b14=lambda x: int(x.split('.')[0]))
        for filename in b19:
            self.b1.append(imageio.imread(os.b3.join(self.b3, filename)))
        imageio.mimsave('sort.gif', self.b1, b20 = 8)
if b21 = = '__main__':
    b22 = [100 - b7 for b7 in range(100)]
    b23 = class1()
    b23.fonk6(b22.copy())
    b23.fonk7(b22.copy())
    b23.fonk4(b22.copy(), 0, len(b22) - 1)
    b23.fonk2(b22.copy(), 0, len(b22))
    b23.fonk9(b22.copy())
    b23.fonk10(b22.copy())
    b23.fonk11(b22.copy())
    b23.fonk13()