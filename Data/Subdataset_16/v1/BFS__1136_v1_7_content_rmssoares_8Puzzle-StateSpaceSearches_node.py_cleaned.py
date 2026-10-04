from queue import Queue
from copy import deepcopy
class class1:
    def fonk1(self, b9, b1 = None, b14=""):
        self.b2 = b9
        self.b1 = b1
        self.a1 = 0
        if b1 is None:
            self.a1 = 0
            self.b3 = b14
        else:
            self.a1 = b1.a1 + 1
            self.b3 = b1.b3 + b14
    def fonk2(self):
        return self.b2.fonk11()
    def fonk3(self):
        b4 = Queue()
        for m in self.b2.b3:
            b5 = deepcopy(self.b2)
            b5.fonk10(m)
            if b5.b11 != self.b2.b11:
                b4.put(class1(b5, self, m))
        return b4
    def fonk4(self, b6):
        return self.fonk5() if b6 = = 0 else self.fonk6()
    def fonk5(self):
        a2 = 0
        a3 = 1
        for i in range(self.b2.b10):
            for b13 in range(self.b2.b10):
                if self.b2.b9[i][b13] != (a3 % (self.b2.b10 * self.b2.b10)):
                    a2 += 1
                a3 += 1
        return a2
    def fonk6(self):
        a2 = 0
        for i in range(self.b2.b10):
            for b13 in range(self.b2.b10):
                b7 = self.b2.b9[i][b13] - 1
                if b7 = = -1:
                    continue
                correct_row, b8 = divmod(b7, self.b2.b10)
                a2 += abs(i - correct_row) + abs(b13 - b8)
        return a2
    def fonk7(self):
        return str(self.b3)
class class2:
    def fonk8(self, b9):
        self.b9 = b9
        self.b10 = len(b9)
        self.b3 = ['U', 'D', 'L', 'R']
        self.b11 = self.fonk9()
    def fonk9(self):
        for i, row in enumerate(self.b9):
            for b13, b12 in enumerate(row):
                if b12 = = 0:
                    return (i, b13)
        return None
    def fonk10(self, b14):
        i, b13 = self.b11
        if b14 = = 'U' and i > 0:
            self.b9[i][b13], self.b9[i - 1][b13] = self.b9[i - 1][b13], self.b9[i][b13]
            self.b11 = (i - 1, b13)
        elif b14 = = 'D' and i < self.b10 - 1:
            self.b9[i][b13], self.b9[i + 1][b13] = self.b9[i + 1][b13], self.b9[i][b13]
            self.b11 = (i + 1, b13)
        elif b14 = = 'L' and b13 > 0:
            self.b9[i][b13], self.b9[i][b13 - 1] = self.b9[i][b13 - 1], self.b9[i][b13]
            self.b11 = (i, b13 - 1)
        elif b14 = = 'R' and b13 < self.b10 - 1:
            self.b9[i][b13], self.b9[i][b13 + 1] = self.b9[i][b13 + 1], self.b9[i][b13]
            self.b11 = (i, b13 + 1)
    def fonk11(self):
        b15 = list(range(1, self.b10 * self.b10)) + [0]
        return self.b9 = = [b15[i:i + self.b10] for i in range(0, len(b15), self.b10)]
if b16 = = "__main__":
    b17 = class2([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    b18 = class1(b17)
    print("Initial class1:")
    print(b18)
    print("Is Goal State:", b18.fonk2())
    print("Heuristic (number of wrong tiles):", b18.fonk4(0))
    print("Heuristic (Manhattan distance):", b18.fonk4(1))
    b19 = b18.fonk3()
    print("\nChildren States:")
    while not b19.empty():
        b20 = b19.get()
        print(b20)