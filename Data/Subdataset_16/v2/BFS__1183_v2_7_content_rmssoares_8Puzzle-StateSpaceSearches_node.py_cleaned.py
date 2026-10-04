from queue import Queue
from copy import deepcopy
class class1:
    def fonk1(self, b10, b1 = None, b15=""):
        self.b2 = b10
        self.b1 = b1
        self.b3 = 0 if b1 is None else b1.b3 + 1
        self.b4 = b15 if b1 is None else b1.b4 + b15
    def fonk2(self):
        return self.b2.fonk11()
    def fonk3(self):
        b5 = Queue()
        for b15 in self.b2.b4:
            b6 = deepcopy(self.b2)
            b6.fonk10(b15)
            if b6.b12 != self.b2.b12:
                b5.put(class1(b6, self, b15))
        return b5
    def fonk4(self, b7):
        return self.fonk5() if b7 = = 0 else self.fonk6()
    def fonk5(self):
        a1 = 0
        a2 = 1
        for i in range(self.b2.b11):
            for b14 in range(self.b2.b11):
                if self.b2.b10[i][b14] != (a2 % (self.b2.b11 * self.b2.b11)):
                    a1 += 1
                a2 += 1
        return a1
    def fonk6(self):
        a1 = 0
        for i in range(self.b2.b11):
            for b14 in range(self.b2.b11):
                b8 = self.b2.b10[i][b14] - 1
                if b8 = = -1:
                    continue
                correct_row, b9 = divmod(b8, self.b2.b11)
                a1 += abs(i - correct_row) + abs(b14 - b9)
        return a1
    def fonk7(self):
        return str(self.b4)
class class2:
    def fonk8(self, b10):
        self.b10 = b10
        self.b11 = len(b10)
        self.b4 = ['U', 'D', 'L', 'R']
        self.b12 = self.fonk9()
    def fonk9(self):
        for i, row in enumerate(self.b10):
            for b14, b13 in enumerate(row):
                if b13 = = 0:
                    return (i, b14)
        return None
    def fonk10(self, b15):
        i, b14 = self.b12
        if b15 = = 'U' and i > 0:
            self.b10[i][b14], self.b10[i - 1][b14] = self.b10[i - 1][b14], self.b10[i][b14]
            self.b12 = (i - 1, b14)
        elif b15 = = 'D' and i < self.b11 - 1:
            self.b10[i][b14], self.b10[i + 1][b14] = self.b10[i + 1][b14], self.b10[i][b14]
            self.b12 = (i + 1, b14)
        elif b15 = = 'L' and b14 > 0:
            self.b10[i][b14], self.b10[i][b14 - 1] = self.b10[i][b14 - 1], self.b10[i][b14]
            self.b12 = (i, b14 - 1)
        elif b15 = = 'R' and b14 < self.b11 - 1:
            self.b10[i][b14], self.b10[i][b14 + 1] = self.b10[i][b14 + 1], self.b10[i][b14]
            self.b12 = (i, b14 + 1)
    def fonk11(self):
        b16 = list(range(1, self.b11 * self.b11)) + [0]
        return self.b10 = = [b16[i:i + self.b11] for i in range(0, len(b16), self.b11)]
if b17 = = "__main__":
    b18 = class2([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    b19 = class1(b18)
    print("Initial class1:")
    print(b19)
    print("Is Goal State:", b19.fonk2())
    print("Heuristic (number of wrong tiles):", b19.fonk4(0))
    print("Heuristic (Manhattan distance):", b19.fonk4(1))
    b20 = b19.fonk3()
    print("\nChildren States:")
    while not b20.empty():
        b21 = b20.get()
        print(b21)