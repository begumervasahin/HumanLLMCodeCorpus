import math
import random
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
class class2:
    def fonk2(self, b4, b5):
        self.b4 = b4
        self.b5 = b5
    def fonk3(self):
        return self.b4
    def fonk4(self):
        return len(self.b4)
    def fonk5(self):
        return self.b5
    def fonk6(self, edge):
        self.b5.append(edge)
    def fonk7(self):
        for edge in self.b5:
            print(f"({edge.b1}, {edge.b2}) - Weight: {edge.b3}")
class class3:
    def fonk8(self, b6, b7):
        self.b6 = b6
        self.b7 = b7
        self.a1 = 1
    def fonk9(self, b7):
        self.b7 = b7
    def fonk10(self, b10):
        if self.b7 is None:
            return self
        else:
            b10.append(self)
            b8 = self.b7.fonk10(b10)
            return b8
class class4:
    def fonk11(self, b18):
        self.b9 = [class3(i, None) for i in range(b18)]
    def fonk12(self, i):
        b10 = []
        b8 = self.b9[i].fonk10(b10)
        for node in b10:
            node.b7 = b8
        return b8
    def fonk13(self, rootX, rootY, edge, b11):
        b11.fonk6(edge)
        if rootX.a1 <= rootY.a1:
            rootY.fonk9(rootX)
            rootY.a1 += 1
        else:
            rootX.fonk9(rootY)
            rootX.a1 += 1
def fonk14(Adj):
    b11 = class2(Adj.fonk3(), [])
    b12 = class4(Adj.fonk4())
    b13 = Adj.fonk4()
    while b13 > 1:
        b14 = [class1(-1, -1, math.inf) for _ in range(Adj.fonk4())]
        for edge in Adj.fonk5():
            b15 = b12.fonk12(edge.b1)
            b16 = b12.fonk12(edge.b2)
            if b15 != b16:
                if b14[b15.b6].b3 >= edge.b3:
                    b14[b15.b6] = edge
                if b14[b16.b6].b3 >= edge.b3:
                    b14[b16.b6] = edge
        for edge in b14:
            if edge.b3 != math.inf:
                b15 = b12.fonk12(edge.b1)
                b16 = b12.fonk12(edge.b2)
                if b15 != b16:
                    b12.fonk13(b15, b16, edge, b11)
                    b13 -= 1
    return b11
class class5:
    def fonk15(self, b18, b19, b17 = 2):
        self.b18 = b18
        self.b19 = b19
        self.b17 = b17
    def fonk16(self):
        b4 = list(range(self.b18))
        b5 = []
        for i in range(self.b18):
            for j in range(i + 1, self.b18):
                if random.random() < self.b19:
                    b3 = random.randint(1, 100)
                    b5.append(class1(i, j, b3))
        return class2(b4, b5)
if b20 = = '__main__':
    print("Original Adjacency List")
    b21 = class5(100, 0.1, b17=2)
    b22 = b21.fonk16()
    b22.fonk7()
    b11 = fonk14(b22)
    print("\nMST: Sollin's Algorithm")
    b11.fonk7()