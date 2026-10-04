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
    def fonk8(self, b7, b6 = None):
        self.b7 = b7
        self.b6 = b6
        self.a1 = 1
    def fonk9(self, b6):
        self.b6 = b6
    def fonk10(self, b10):
        if self.b6 is None:
            return self
        b10.append(self)
        b8 = self.b6.fonk10(b10)
        return b8
class class4:
    def fonk11(self, b17):
        self.b9 = [class3(i) for i in range(b17)]
    def fonk12(self, i):
        b10 = []
        b8 = self.b9[i].fonk10(b10)
        for node in b10:
            node.b6 = b8
        return b8
    def fonk13(self, root_x, root_y, edge, b11):
        b11.fonk6(edge)
        if root_x.a1 <= root_y.a1:
            root_y.fonk9(root_x)
            root_y.a1 += 1
        else:
            root_x.fonk9(root_y)
            root_x.a1 += 1
def fonk14(adj_list):
    b11 = class2(adj_list.fonk3(), [])
    b12 = class4(adj_list.fonk4())
    b13 = adj_list.fonk4()
    while b13 > 1:
        b14 = [class1(-1, -1, math.inf) for _ in range(adj_list.fonk4())]
        for edge in adj_list.fonk5():
            b15 = b12.fonk12(edge.b1)
            b16 = b12.fonk12(edge.b2)
            if b15 != b16:
                if b14[b15.b7].b3 > edge.b3:
                    b14[b15.b7] = edge
                if b14[b16.b7].b3 > edge.b3:
                    b14[b16.b7] = edge
        for edge in b14:
            if edge.b3 != math.inf:
                b15 = b12.fonk12(edge.b1)
                b16 = b12.fonk12(edge.b2)
                if b15 != b16:
                    b12.fonk13(b15, b16, edge, b11)
                    b13 -= 1
    return b11
class class5:
    def fonk15(self, b17, b18):
        self.b17 = b17
        self.b18 = b18
    def fonk16(self):
        b4 = list(range(self.b17))
        b5 = []
        for i in range(self.b17):
            for j in range(i + 1, self.b17):
                if random.random() < self.b18:
                    b3 = random.randint(1, 100)
                    b5.append(class1(i, j, b3))
        return class2(b4, b5)
if b19 = = '__main__':
    print("Original Adjacency List")
    b20 = class5(100, 0.1)
    b21 = b20.fonk16()
    b21.fonk7()
    b11 = fonk14(b21)
    print("\nMST: Sollin's Algorithm")
    b11.fonk7()