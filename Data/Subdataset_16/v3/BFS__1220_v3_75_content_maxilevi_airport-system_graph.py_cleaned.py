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
            for u in self.fonk4(v):
                b7 = (v, u, self.fonk8((v, u)))
                if (v, u) not in b5 and (u, v) not in b5:
                    b6.append(b7)
                    b5.add((v, u))
                    if self.fonk11():
                        b5.add((u, v))
        return b6
    def fonk4(self, vertex):
        return list(self.b2[vertex].keys())
    def fonk5(self, origin, vertex):
        return vertex in self.b2[origin]
    def fonk6(self, vertex):
        if vertex not in self.b2:
            self.b2[vertex] = {}
    def fonk7(self, b7, b8 = 1):
        start, b9 = b7
        self.fonk6(start)
        self.fonk6(b9)
        self.b2[start][b9] = b8
        if self.fonk11():
            self.b2[b9][start] = b8
        if b8 != 1:
            self.b3 = True
    def fonk8(self, b7):
        start, b9 = b7
        return self.b2[start][b9]
    def fonk9(self):
        return random.choice(self.fonk2())
    def fonk10(self):
        return self.b3
    def fonk11(self):
        return self.b4
if b10 = = "__main__":
    b11 = class1(b1=True)
    b11.fonk6("A")
    b11.fonk6("B")
    b11.fonk6("C")
    b11.fonk7(("A", "B"), 5)
    b11.fonk7(("B", "C"), 3)
    b11.fonk7(("C", "A"), 2)
    print("Vertices:", b11.fonk2())
    print("Edges:", b11.fonk3())
    print("Is A adjacent to B?", b11.fonk5("A", "B"))
    print("Is A adjacent to C?", b11.fonk5("A", "C"))
    print("Random vertex:", b11.fonk9())
    print("Is the b11 weighted?", b11.fonk10())
    print("Is the b11 undirected?", b11.fonk11())