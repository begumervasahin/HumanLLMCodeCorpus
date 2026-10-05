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
        self.fonk2(self.b3)
    def fonk2(self, directory):
        if not os.b3.exists(directory):
            os.mkdir(directory)
    def fonk3(self, sequence, start, end):
        if end - start < 2:
            return
        b4 = (end - start)
        self.fonk3(sequence, start, start + b4)
        self.fonk3(sequence, start + b4, end)
        self.fonk4(start, b4, end, sequence)
    def fonk4(self, start, b4, end, sequence):
        i, b5 = start, start + b4
        while i < start + b4 and b5 < end:
            if sequence[i] < sequence[b5]:
                i += 1
            else:
                sequence.insert(i, sequence[b5])
                b5 += 1
                sequence.pop(b5)
                self.fonk6(sequence, 'MERGE SORT')
    def fonk5(self, sequence, low, high):
        if low >= high:
            return
        b6 = sequence[high]
        left, b7 = low, high - 1
        while left <= b7:
            while left <= b7 and sequence[left] < b6:
                left += 1
            while left <= b7 and sequence[b7] > b6:
                b7 -= 1
            if left <= b7:
                sequence[left], sequence[b7] = sequence[b7], sequence[left]
                left, b7 = left + 1, b7 - 1
        sequence[left], sequence[high] = sequence[high], sequence[left]
        if left != high:
            self.fonk6(sequence, 'QUICK SORT')
        self.fonk5(sequence, low, left - 1)
        self.fonk5(sequence, left + 1, high)
    def fonk6(self, sequence, algorithm_name):
        if len(sequence):
            self.a1 += 1
            plt.clf()
            plt.bar(range(len(sequence)), sequence, b8 = 0.3, color='purple')
            plt.title(algorithm_name)
            plt.savefig(os.b3.join(self.b3, str(self.a1)))
            plt.pause(0.01)
    def fonk7(self):
        b9 = os.listdir(self.b3)
        b9.sort(b10 = lambda x: int(x[:-4]))
        for filename in b9:
            b11 = os.b3.join(self.b3, filename)
            self.b1.append(imageio.imread(b11))
        imageio.mimsave('sort.gif', self.b1, b12 = 8)
if b13 = = '__main__':
    b14 = [100 - k for k in range(100)]
    b15 = class1()
    b15.fonk5(list(b14), 0, len(b14) - 1)
    b15.fonk7()