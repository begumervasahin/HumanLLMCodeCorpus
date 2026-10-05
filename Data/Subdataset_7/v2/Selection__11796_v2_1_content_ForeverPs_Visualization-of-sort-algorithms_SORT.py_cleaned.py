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
        self.b3 = 'sort_process/'
        if not os.b3.exists(self.b3):
            os.mkdir(self.b3)
    def fonk2(self, b19, start, end):
        if end - start < 2:
            return
        b4 = (end - start)
        self.fonk2(b19, start, start + b4)
        self.fonk2(b19, start + b4, end)
        self.fonk3(start, b4, end, b19)
    def fonk3(self, start, b4, end, b19):
        i, b5 = start, start + b4
        while i < start + b4 and b5 < end:
            if b5 = = end or (i < start + b4 and b19[i] < b19[b5]):
                i += 1
            else:
                b19.insert(i, b19[b5])
                b5 += 1
                b19.pop(b5)
                self.fonk14(b19, 'MERGE SORT')
    def fonk4(self, b19, left, right):
        if left >= right:
            return
        b6 = b19[right]
        l, b7 = left, right - 1
        while l <= b7:
            while l <= b7 and b19[l] < b6:
                l += 1
            while l <= b7 and b19[b7] > b6:
                b7 -= 1
            if l <= b7:
                b19[l], b19[b7] = b19[b7], b19[l]
                l += 1
                b7 -= 1
        b19[l], b19[right] = b19[right], b19[l]
        if l != right:
            self.fonk14(b19, 'QUICK SORT')
        self.fonk4(b19, left, l - 1)
        self.fonk4(b19, l + 1, right)
    def fonk5(self, b19):
        self.fonk14(b19, 'SELECTION SORT')
        for i in range(len(b19)):
            if self.fonk6(b19, i):
                self.fonk14(b19, 'SELECTION SORT')
    def fonk6(self, b19, i):
        b8 = i
        for b5 in range(i, len(b19)):
            if b19[b5] < b19[b8]:
                b8 = b5
        if b8 != i:
            b19[i], b19[b8] = b19[b8], b19[i]
            return True
        return False
    def fonk7(self, b19, root, b10):
        b9 = 2 * root + 1
        if b9 = = b10 - 1:
            if b19[root] < b19[b9]:
                b19[root], b19[b9] = b19[b9], b19[root]
        while b9 < b10 - 1:
            if b19[b9] < b19[b9 + 1]:
                b9 += 1
            if b19[root] > b19[b9]:
                break
            b19[root], b19[b9] = b19[b9], b19[root]
            root, b9 = b9, 2 * b9 + 1
    def fonk8(self, b19):
        b10 = len(b19)
        for i in range(b10
            self.fonk7(b19, i, b10)
        for i in range(b10 - 1, 0, -1):
            b19[0], b19[i] = b19[i], b19[0]
            self.fonk14(b19, 'HEAP SORT')
            self.fonk7(b19, 0, i)
    def fonk9(self, b19):
        for i in range(1, len(b19)):
            if self.fonk10(b19, i):
                self.fonk14(b19, 'INSERT SORT')
    def fonk10(self, b19, k):
        index, b11 = k, b19[k]
        for i in range(k, len(b19)):
            if b19[i] < b11:
                index, b11 = i, b19[i]
        b19[k], b19[index] = b19[index], b19[k]
        return index != k
    def fonk11(self, b19):
        b12 = int(np.log2(len(b19) + 1))
        for a1 in range(1, b12 + 1):
            b13 = 2 ** (b12 - a1 + 1) - 1
            for i in range(len(b19) - b13):
                if self.fonk12(b19, i, i + b13):
                    self.fonk14(b19, 'SHELL SORT')
    def fonk12(self, b19, start, end):
        index, b11 = start, b19[start]
        for i in range(start, end + 1):
            if b19[i] < b11:
                index, b11 = i, b19[i]
        b19[start], b19[index] = b19[index], b19[start]
        return index != start
    def fonk13(self, b19):
        for i in range(len(b19) - 1):
            for b5 in range(len(b19) - i - 1):
                if b19[b5] > b19[b5 + 1]:
                    b19[b5], b19[b5 + 1] = b19[b5 + 1], b19[b5]
                    self.fonk14(b19, 'BUBBLE SORT')
    def fonk14(self, b19, sort_name):
        if len(b19):
            self.a1 += 1
            plt.clf()
            plt.bar(range(len(b19)), b19, b14 = 0.3, color='purple')
            plt.title(sort_name)
            plt.savefig(self.b3 + str(self.a1))
            plt.pause(0.01)
    def fonk15(self):
        b15 = os.listdir(self.b3)
        b15.sort(b16 = lambda x: int(x[:-4]))
        for name in b15:
            b3 = self.b3 + name
            self.b1.append(imageio.imread(b3))
        imageio.mimsave('sort.gif', self.b1, b17 = 8)
if b18 = = '__main__':
    b19 = [100 - k for k in range(100)]
    b20 = class1()
    b20.fonk5(list(b19))
    b20.fonk8(list(b19))
    b20.fonk4(list(b19), 0, len(b19) - 1)
    b20.fonk2(list(b19), 0, len(b19))
    b20.fonk9(list(b19))
    b20.fonk11(list(b19))
    b20.fonk15()