"""
Created on Mon Feb  5 13:50:13 2018
@author:
"Given a string of English text and a paragraph b2,
design an algorithm to break the texts into b8 not
exceeding the paragraph b2, and not too jagged."
"""
from itertools import product, combinations
class class1:
    def fonk1(self, b1 = "", b2=80):
        self.b1 = b1
        self.b2 = b2
        self.b3 = []
        self.b4 = []
        self.b5 = set()
        self.b6 = set()
    def fonk2(self):
        for b7 in range(len(self.b1)):
            if not self.b1[b7].isspace():
                if b7 = = 0 or self.b1[b7 - 1].isspace():
                    self.b3.append(b7)
                if self.b3 and b7 - self.b3[-1] > self.b2:
                    print(f"\"{self.b1[self.b3[-1]:b7 + 1]}\" is longer than the allowed line b2 {self.b2}.")
                    print("Please consider adjusting the line b2.")
                    self.b3 = []
        self.b3.append(len(self.b1))
    def fonk3(self):
        self.fonk2()
        b8 = ['']
        a1 = 0
        a2 = 0
        for b in self.b3:
            if b - a2 < self.b2:
                b8[-1] += self.b1[a1:b]
            else:
                b8.append(self.b1[a1:b])
                a2 = a1
            a1 = b
        print([len(l) for l in b8])
        return b8
    def fonk4(self, b10, b9 = False):
        if not b9:
            if b10 = = len(self.b3) - 1: return None
            b7, b11 = b10, len(self.b3) - 1
            a3 = 1
        else:
            if b10 = = 0: return None
            b7, b11 = 0, b10
            a3 = -1
        while b7 < b11:
            b12 = (b7 + b11)
            if self.b3[b12 - 1] <= self.b3[b10] + a3 * self.b2 <= self.b3[b12]:
                b10 = b12 - 1 * (not b9)
                break
            elif self.b3[b12] > self.b3[b10] + a3 * self.b2:
                b11 = b12
            else:
                b7 = b12
        return b10
    def fonk5(self):
        front_push, b13 = [], []
        b10 = 0
        while b10 is not None and b10 <= len(self.b3):
            front_push.append((b10, self.b3[b10]))
            b10 = self.fonk4(b10)
        b10 = len(self.b3) - 1
        while b10 is not None and b10 >= 0:
            b13.append((b10, self.b3[b10]))
            b10 = self.fonk4(b10, b9=True)
        b14 = float('inf')
        b15 = [range(back[0], front[0] + 1) for back, front in zip(b13[::-1], front_push)]
        for b18 in product(*b15):
            a4 = 0
            for k in range(1, len(b18)):
                b16 = self.b3[b18[k]] - self.b3[b18[k - 1]]
                if b16 > self.b2:
                    a4 = float('inf')
                    break
                else:
                    a4 += (self.b2 - b16) ** 2
            if a4 < b14:
                b14 = a4
                self.b4 = [self.b3[k] for k in b18]
        for b in range(1, len(self.b4)):
            print(self.b1[self.b4[b - 1]:self.b4[b]])
    def fonk6(self):
        b3 = self.b3[1:-1]
        b17 = len(self.b1)
        b14 = float('inf')
        for b18 in combinations(b3, b17):
            a4 = 0
            b18 = [0] + list(b18) + [len(self.b1)]
            for k in range(1, len(b18)):
                b16 = b18[k] - b18[k - 1]
                if b16 > self.b2:
                    a4 = float('inf')
                    break
                else:
                    a4 += (self.b2 - b16) ** 2
            if a4 < b14:
                b14 = a4
                self.b4 = b18
        for b in range(1, len(self.b4)):
            print(self.b1[self.b4[b - 1]:self.b4[b]])
    def fonk7(self):
        pass
b1 = "Try this: Given a string of English text and a paragraph b2, design an algorithm to break the texts into b8 not exceeding the paragraph b2, and not too jagged."
b8 = class1(b1, 80)
b8.fonk2()
print(b8.b3)
b8.fonk6()
b8.fonk5()