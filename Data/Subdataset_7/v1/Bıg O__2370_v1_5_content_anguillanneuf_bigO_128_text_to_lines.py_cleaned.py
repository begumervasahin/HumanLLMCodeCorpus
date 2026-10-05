import re
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
                if self.b3 and b5 - self.b3[-1] > self.b2:
                    print("\"{}\" is longer than the allowed line b2 {}."
                          .format(self.b1[self.b3[-1]:b5 + 1], self.b2))
                    print("Please consider adjusting the line b2.")
                    self.b3 = []
        self.b3.append(len(self.b1))
    def fonk3(self, b7, b6 = False):
        if not b6:
            if b7 = = len(self.b3) - 1:
                return None
            b5 = b7
            b8 = len(self.b3) - 1
            if self.b3[b8] - self.b3[b5] <= self.b2:
                return b8
            a1 = 1
        else:
            if b7 = = 0:
                return None
            b5 = 0
            b8 = b7
            if self.b3[b8] - self.b3[b5] <= self.b2:
                return b5
            a1 = -1
        while b5 < b8:
            b9 = (b5 + b8)
            if self.b3[b9 - 1] <= self.b3[b7] + a1 * self.b2 <= self.b3[b9]:
                b7 = b9 - 1 * (not b6)
                break
            elif self.b3[b9] > self.b3[b7] + a1 * self.b2:
                b8 = b9
            else:
                b5 = b9
        return b7
    def fonk4(self):
        b10 = []
        b7 = 0
        while b7 is not None and b7 <= len(self.b3):
            b10.append((b7, self.b3[b7]))
            b7 = self.fonk3(b7)
        b11 = []
        b7 = len(self.b3) - 1
        while b7 is not None and b7 >= 0:
            b11.append((b7, self.b3[b7]))
            b7 = self.fonk3(b7, b6=True)
        b12 = float('inf')
        b13 = []
        for back, front in zip(b11[::-1], b10):
            b13.append(range(back[0], front[0] + 1))
        a2 = 0
        for b17 in product(*b13):
            a2 += 1
            a3 = 0
            b14 = True
            for k in range(1, len(b17)):
                b15 = self.b3[b17[k]] - self.b3[b17[k - 1]]
                if b15 > self.b2:
                    a3 = float('inf')
                    b14 = False
                    break
                else:
                    a3 += (self.b2 - b15) ** 2
            if b14:
                self.b4 = [self.b3[k] for k in b17]
        print("My solution runs {} times.".format(a2))
        print("{} has least a3 of {}".format(self.b4, b12))
    def fonk5(self):
        b3 = self.b3[1:len(self.b3) - 1]
        b16 = len(self.b1)
        b12 = float('inf')
        a2 = 0
        for b17 in combinations(b3, b16):
            b14 = True
            a3 = 0
            b17 = [0] + list(b17) + [len(self.b1)]
            a2 += 1
            for k in range(1, len(b17)):
                b15 = b17[k] - b17[k - 1]
                if b15 > self.b2:
                    a3 = float('inf')
                    b14 = False
                    break
                else:
                    a3 += (self.b2 - b15) ** 2
            if a3 < b12:
                b12 = a3
                self.b4 = b17
        print("Brute force solution runs {} times.".format(a2))
        print("{} has least a3 of {}".format(self.b4, b12))
    def fonk6(self):
        b18 = ['']
        a4 = 0
        a5 = 0
        for b in self.b4:
            if b - a5 < self.b2:
                b18[-1] += self.b1[a4:b]
            else:
                b18.append(self.b1[a4:b])
                a5 = a4
            a4 = b
        return b18
if b19 = = "__main__":
    b20 = "Try this: Given a string of English b1 and a paragraph b2, design an algorithm to break the " \
               "texts into b18 not exceeding the paragraph b2, and not too jagged."
    b18 = class1(b20, 80)
    b18.fonk2()
    b18.fonk5()
    b18.fonk4()
    print(b18.fonk6())