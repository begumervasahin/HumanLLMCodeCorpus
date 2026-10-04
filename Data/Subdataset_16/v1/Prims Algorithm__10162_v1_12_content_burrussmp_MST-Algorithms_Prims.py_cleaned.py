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
    def fonk6(self, b23):
        return len(self.b6[b23])
    def fonk7(self, b23, b14):
        return self.b6[b23][b14]
    def fonk8(self):
        for vertex in self.b4:
            print(f"{vertex}: {self.b6[vertex]}")
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
            print(f"(b15 = {self.b10[b14][0]} w={self.b10[b14][1]}) ", end='')
        print('')
    def fonk13(self, vertex, parent):
        self.b12[vertex] = parent
    def fonk14(self, b20, b21):
        b16 = self.b10[0][0]
        if self.b12[b16] != -1 and b21[b16] == 0:
            b20.fonk5(class1(self.b12[b16], b16, self.b10[0][1]))
            b21[b16] = 1
        self.b10[0] = self.b10[self.b13 - 1]
        self.b11[b16] = -1
        self.b11[self.b10[0][0]] = 0
        self.b13 = self.b13 - 1
        self.fonk15(0)
        return b16
    def fonk15(self, b19):
        b16 = b19
        if 2 * b19 + 1 < self.b13 and self.b10[b16][1] > self.b10[2 * b19 + 1][1]:
            b16 = 2 * b19 + 1
        if 2 * b19 + 2 < self.b13 and self.b10[b16][1] > self.b10[2 * b19 + 2][1]:
            b16 = 2 * b19 + 2
        if b16 != b19:
            self.b10[b19], self.b10[b16] = self.b10[b16], self.b10[b19]
            self.b11[self.b10[b19][0]], self.b11[self.b10[b16][0]] = (
                self.b11[self.b10[b16][0]], self.b11[self.b10[b19][0]])
            self.fonk15(b16)
    def fonk16(self, b19, vertex):
        b17 = False
        while not b17:
            b18 = (b19 - 1)
            if self.b10[b18][1] > self.b10[b19][1]:
                self.b10[b19], self.b10[b18] = self.b10[b18], self.b10[b19]
                self.b11[vertex], self.b11[self.b10[b18][0]] = (
                    self.b11[self.b10[b18][0]], self.b11[vertex])
                b19 = b18
            else:
                b17 = True
    def fonk17(self):
        return self.b13 = = 0
    def fonk18(self, vertex):
        return self.b10[self.b11[vertex]][1]
    def fonk19(self, vertex, b3):
        b19 = self.b11[vertex]
        self.b10[b19] = (vertex, b3)
        self.fonk16(b19, vertex)
def fonk20(Adj):
    b4 = Adj.fonk4()
    b20 = class2(b4, [])
    b21 = [0 for _ in range(len(b4))]
    b22 = class4(b4)
    while not b22.fonk17():
        b23 = b22.fonk14(b20, b21)
        for b14 in range(Adj.fonk6(b23)):
            neighbor, b3 = Adj.fonk7(b23, b14)
            if b21[neighbor] == 0 and b22.fonk18(neighbor) > b3:
                b22.fonk13(neighbor, b23)
                b22.fonk19(neighbor, b3)
    return b20
if b24 = = '__main__':
    print("Original Adjacency b10")
    b25 = class3(100, 0.1, b7=2)
    b26 = b25.fonk10()
    b26.fonk12()
    b20 = fonk20(b26)
    print("b20: Prim's Algorithm")
    b20.fonk12()