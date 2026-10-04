"""
Created on Mon Feb 5 13:50:13 2018
Author:
"Given a string of English b1 and a paragraph b2,
design an algorithm to break the b1 into b6 not
exceeding the paragraph b2, and not too jagged."
"""
from itertools import product, combinations
class class1:
    def fonk1(self, b1 = "", b2=80):
        self.b1 = b1
        self.b2 = b2
        self.b3 = []
        self.b4 = []
    def fonk2(self):
        for b5 in range(len(self.b1)):
            if not self.b1[b5].isspace():
                if b5 = = 0 or self.b1[b5 - 1].isspace():
                    self.b3.append(b5)
        self.b3.append(len(self.b1))
    def fonk3(self):
        self.fonk2()
        b6 = ['']
        a1 = 0
        for b in self.b3:
            if b - a1 < self.b2:
                b6[-1] += self.b1[a1:b]
            else:
                b6.append(self.b1[a1:b])
                a1 = b
        return b6
    def fonk4(self, b8, b7 = False):
        if not b7:
            if b8 = = len(self.b3) - 1:
                return None
            b5, b9 = b8, len(self.b3) - 1
            a2 = 1
        else:
            if b8 = = 0:
                return None
            b5, b9 = 0, b8
            a2 = -1
        while b5 < b9:
            b10 = (b5 + b9)
            if self.b3[b10 - 1] <= self.b3[b8] + a2 * self.b2 <= self.b3[b10]:
                b8 = b10 - 1 * (not b7)
                break
            elif self.b3[b10] > self.b3[b8] + a2 * self.b2:
                b9 = b10
            else:
                b5 = b10
        return b8
    def fonk5(self):
        front_push, b11 = [], []
        a3 = 0
        while a3 is not None and a3 <= len(self.b3):
            front_push.append((a3, self.b3[a3]))
            a3 = self.fonk4(a3)
        a3 = len(self.b3) - 1
        while a3 is not None and a3 >= 0:
            b11.append((a3, self.b3[a3]))
            a3 = self.fonk4(a3, b7=True)
        b12 = float('inf')
        b13 = [range(back[0], front[0] + 1) for back, front in zip(b11[::-1], front_push)]
        for b17 in product(*b13):
            a4 = 0
            for k in range(1, len(b17)):
                b14 = self.b3[b17[k]] - self.b3[b17[k - 1]]
                if b14 > self.b2:
                    a4 = float('inf')
                    break
                else:
                    a4 += (self.b2 - b14) ** 2
            if a4 < b12:
                b12 = a4
                self.b4 = [self.b3[k] for k in b17]
        for b in range(1, len(self.b4)):
            print(self.b1[self.b4[b - 1]:self.b4[b]])
    def fonk6(self):
        self.fonk2()
        b15 = self.b3[1:-1]
        b16 = len(self.b1)
        b12 = float('inf')
        for b17 in combinations(b15, b16):
            a4 = 0
            b17 = [0] + list(b17) + [len(self.b1)]
            for k in range(1, len(b17)):
                b14 = b17[k] - b17[k - 1]
                if b14 > self.b2:
                    a4 = float('inf')
                    break
                else:
                    a4 += (self.b2 - b14) ** 2
            if a4 < b12:
                b12 = a4
                self.b4 = b17
        for b in range(1, len(self.b4)):
            print(self.b1[self.b4[b - 1]:self.b4[b]])
    def fonk7(self):
        pass
if b18 = = "__main__":
    b19 = (
        "Try this: Given a string of English b1 and a paragraph b2, "
        "design an algorithm to break the texts into b6 not exceeding the "
        "paragraph b2, and not too jagged."
    )
    b20 = class1(b19, 80)
    b20.fonk2()
    print("Word b15:", b20.b3)
    print("Using brute force approach:")
    b20.fonk6()
    print("Using optimized approach:")
    b20.fonk5()