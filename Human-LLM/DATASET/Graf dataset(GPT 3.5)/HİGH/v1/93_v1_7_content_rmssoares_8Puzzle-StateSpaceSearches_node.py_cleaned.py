from copy import deepcopy
from queue import Queue
class class1:
    def fonk1(self, b1 = 3):
        self.b1 = b1
        self.b2 = self.fonk2()
    def fonk2(self):
        b2 = [[0] * self.b1 for _ in range(self.b1)]
        b3 = list(range(1, self.b1 * self.b1))
        b3.append(0)
        b3 = b3[::-1]
        for i in range(self.b1):
            for j in range(self.b1):
                b2[i][j] = b3.pop()
        return b2
    def fonk3(self):
        a1 = 1
        for i in range(self.b1):
            for j in range(self.b1):
                if self.b2[i][j] != a1 % (self.b1 * self.b1):
                    return False
                a1 += 1
        return True
    def fonk4(self, b5):
        zero_row, b4 = self.fonk5()
        if b5 = = 'R' and b4 < self.b1 - 1:
            self.b2[zero_row][b4], self.b2[zero_row][b4 + 1] = self.b2[zero_row][b4 + 1], 0
        elif b5 = = 'L' and b4 > 0:
            self.b2[zero_row][b4], self.b2[zero_row][b4 - 1] = self.b2[zero_row][b4 - 1], 0
        elif b5 = = 'U' and zero_row > 0:
            self.b2[zero_row][b4], self.b2[zero_row - 1][b4] = self.b2[zero_row - 1][b4], 0
        elif b5 = = 'D' and zero_row < self.b1 - 1:
            self.b2[zero_row][b4], self.b2[zero_row + 1][b4] = self.b2[zero_row + 1][b4], 0
    def fonk5(self):
        for i in range(self.b1):
            for j in range(self.b1):
                if self.b2[i][j] == 0:
                    return i, j
class class2:
    def fonk6(self, b2, b6 = None, b5=""):
        self.b7 = b2
        self.b6 = b6
        self.a2 = 0
        if b6 is None:
            self.a2 = 0
            self.b8 = b5
        else:
            self.a2 = b6.a2 + 1
            self.b8 = b6.b8 + b5
    def fonk7(self):
        return self.b7.fonk3()
    def fonk8(self):
        b9 = Queue()
        for m in self.b7.b8:
            b10 = deepcopy(self.b7)
            b10.fonk4(m)
            if b10.fonk5() != self.b7.fonk5():
                b9.put(class2(b10, self, m))
        return b9
    def fonk9(self, b11):
        return self.fonk10() if b11 = = 0 else self.fonk11()
    def fonk10(self):
        a3 = 0
        a1 = 1
        for i in range(0, self.b7.b1):
            for j in range(0, self.b7.b1):
                if self.b7.b2[i][j] != (a1 % (self.b7.b1 * self.b7.b1)):
                    a3 += 1
                a1 += 1
        return a3
    def fonk11(self):
        a3 = 0
        a1 = 1
        for i in range(0, self.b7.b1):
            for j in range(0, self.b7.b1):
                b12 = self.b7.b2[i][j] - 1
                b13 = (2 - i) + (2 - j) if b12 == -1 else abs(i - (b12
                a3 += b13
                a1 += 1
        return a3
    def fonk12(self):
        return str(self.b8)
def fonk13():
    b2 = class1()
    b14 = class2(b2)
    print("Initial b7:", b2.b2)
    print("Is the initial b7 a goal b7?", b14.fonk7())
    print("Possible b8 from the initial b7:", b2.b8)
    print("Successor states:", [str(s) for s in b14.fonk8()])
if b15 = = "__main__":
    fonk13()