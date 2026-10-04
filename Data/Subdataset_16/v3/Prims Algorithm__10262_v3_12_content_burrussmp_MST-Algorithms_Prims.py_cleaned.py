import math
import random
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
    def fonk2(self):
        return f"({self.b1} - {self.b2}: {self.b3})"
class class2:
    def fonk3(self, b4, b5):
        self.b4 = b4
        self.b5 = b5
        self.b6 = {vertex: [] for vertex in b4}
        for edge in b5:
            self.b6[edge.b1].append((edge.b2, edge.b3))
            self.b6[edge.b2].append((edge.b1, edge.b3))
    def fonk4(self):
        return self.b4
    def fonk5(self, edge):
        self.b5.append(edge)
        self.b6[edge.b1].append((edge.b2, edge.b3))
        self.b6[edge.b2].append((edge.b1, edge.b3))
    def fonk6(self, vertex):
        return len(self.b6[vertex])
    def fonk7(self, vertex, b20):
        return self.b6[vertex][b20]
    def fonk8(self):
        for vertex in self.b4:
            fonk12(f"{vertex}: {self.b6[vertex]}")
class class3:
    def fonk9(self, b8, b9, b7 = 2):
        self.b8 = b8
        self.b9 = b9
        self.b7 = b7
    def fonk10(self):
        b4 = [b14 for b14 in range(self.b8)]
        b5 = []
        for b14 in range(self.b8):
            for j in range(b14 + 1, self.b8):
                if random.random() <= self.b9:
                    b3 = random.randint(1, 10)
                    b5.append(class1(b14, j, b3))
        return class2(b4, b5)
class class4:
    def fonk11(self, b4):
        self.b10 = []
        self.b11 = []
        self.b12 = []
        self.b13 = len(b4)
        for b14 in range(len(b4)):
            if b14 = = 0:
                self.b10.append((0, 0))
                self.b11.append(0)
                self.b12.append(-1)
            else:
                self.b10.append((b14, math.inf))
                self.b11.append(b14)
                self.b12.append(-1)
        self.a1 = 0
    def fonk12(self):
        for b14 in range(self.b13):
            fonk12(f"(b15 = {self.b10[b14][0]} w={self.b10[b14][1]}) ", end='')
        fonk12('')
    def fonk13(self, vertex, parent):
        self.b12[vertex] = parent
    def fonk14(self, b21, b22):
        b16 = self.b10[0][0]
        if self.b12[b16] != -1 and b22[b16] == 0:
            b21.fonk5(class1(self.b12[b16], b16, self.b10[0][1]))
            b22[b16] = 1
        self.b10[0] = self.b10[self.b13 - 1]
        self.b11[b16] = -1
        self.b11[self.b10[0][0]] = 0
        self.b13 -= 1
        self.fonk15(0)
        return b16
    def fonk15(self, b20):
        b16 = b20
        b17 = 2 * b20 + 1
        b18 = 2 * b20 + 2
        if b17 < self.b13 and self.b10[b16][1] > self.b10[b17][1]:
            b16 = b17
        if b18 < self.b13 and self.b10[b16][1] > self.b10[b18][1]:
            b16 = b18
        if b16 != b20:
            self.fonk16(b20, b16)
            self.fonk15(b16)
    def fonk16(self, b14, j):
        self.b10[b14], self.b10[j] = self.b10[j], self.b10[b14]
        self.b11[self.b10[b14][0]], self.b11[self.b10[j][0]] = (
            self.b11[self.b10[j][0]], self.b11[self.b10[b14][0]]
        )
    def fonk17(self, b20, vertex):
        while b20 > 0:
            b19 = (b20 - 1)
            if self.b10[b19][1] > self.b10[b20][1]:
                self.fonk16(b20, b19)
                b20 = b19
            else:
                break
    def fonk18(self):
        return self.b13 = = 0
    def fonk19(self, vertex):
        return self.b10[self.b11[vertex]][1]
    def fonk20(self, vertex, b3):
        b20 = self.b11[vertex]
        self.b10[b20] = (vertex, b3)
        self.fonk17(b20, vertex)
def fonk21(b6):
    b4 = b6.fonk4()
    b21 = class2(b4, [])
    b22 = [0] * len(b4)
    b23 = class4(b4)
    while not b23.fonk18():
        b24 = b23.fonk14(b21, b22)
        for b14 in range(b6.fonk6(b24)):
            neighbor, b3 = b6.fonk7(b24, b14)
            if b22[neighbor] == 0 and b23.fonk19(neighbor) > b3:
                b23.fonk13(neighbor, b24)
                b23.fonk20(neighbor, b3)
    return b21
if b25 = = '__main__':
    fonk12("Original Adjacency List")
    b26 = class3(100, 0.1, b7=2)
    b27 = b26.fonk10()
    b27.fonk12()
    b21 = fonk21(b27)
    fonk12("MST: Prim's Algorithm")
    b21.fonk12()