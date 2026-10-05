import random
class class1:
    def fonk1(self, b1 = False):
        self.b2 = {}
        self.b3 = False
        self.b4 = b1
    def fonk2(self):
        return list(self.b2.keys())
    def fonk3(self):
        b5 = set()
        b6 = []
        for v in self.fonk2():
            b7 = [(v, u, self.fonk8((v, u))) for u in self.fonk4(v)]
            for edge in b7:
                u, v, b8 = edge
                if (u, v) not in b5 and (v, u) not in b5:
                    b6.append(edge)
                    b5.add((u, v))
        return b6
    def fonk4(self, vertex):
        return list([x for x in self.b2[vertex].keys()])
    def fonk5(self, origin, vertex):
        return vertex in self.b2[origin]
    def fonk6(self, vertex):
        if vertex not in self.b2:
            self.b2[vertex] = {}
    def fonk7(self, edge, b8 = 1):
        x, b9 = edge
        self.b2[x][b9] = b8
        if self.fonk11():
            self.b2[b9][x] = b8
        self.b3 = self.b3 or b8 != 1
    def fonk8(self, edge):
        x, b9 = edge
        return self.b2[x][b9]
    def fonk9(self):
        b10 = self.fonk2()
        return b10[random.randint(0, len(b10) - 1)]
    def fonk10(self):
        return self.b3
    def fonk11(self):
        return self.b4
if b11 = = "__main__":
    b12 = class1()
    b12.fonk6('A')
    b12.fonk6('B')
    b12.fonk6('C')
    b12.fonk7(('A', 'B'), 3)
    b12.fonk7(('B', 'C'), 5)
    b12.fonk7(('A', 'C'), 2)
    print("Vertices:", b12.fonk2())
    print("Edges:", b12.fonk3())