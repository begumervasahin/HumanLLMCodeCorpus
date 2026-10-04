from utils import initialize_single_source, relax
class class1:
    def fonk1(self):
        self.b1 = {}
        self.b2 = []
    def fonk2(self, vertex):
        if vertex not in self.b1:
            self.b1[vertex] = class2(vertex)
    def fonk3(self, u, v, b7):
        if u not in self.b1:
            self.fonk2(u)
        if v not in self.b1:
            self.fonk2(v)
        self.b2.append((u, v, b7))
        self.b1[u].fonk7(self.b1[v], b7)
    def fonk4(self):
        return self.b1.values()
    def fonk5(self):
        return self.b2
class class2:
    def fonk6(self, key):
        self.b3 = key
        self.b4 = {}
        self.b5 = float('Inf')
        self.b6 = False
    def fonk7(self, neighbor, b7 = 0):
        self.b4[neighbor] = b7
    def fonk8(self):
        return self.b4.keys()
    def fonk9(self):
        return self.b3
    def fonk10(self, neighbor):
        return self.b4[neighbor]
    def fonk11(self, dist):
        self.b5 = dist
    def fonk12(self):
        return self.b5
    def fonk13(self):
        self.b6 = True
    def fonk14(self):
        return self.b6
def fonk15(b9, start):
    initialize_single_source(b9, start)
    for _ in range(len(b9.fonk4()) - 1):
        for u, v, b7 in b9.fonk5():
            if v.fonk14():
                continue
            relax(u, v, b7)
    for u, v, b7 in b9.fonk5():
        if v.fonk12() > u.fonk12() + u.fonk10(v):
            print("class1 contains a negative b7 cycle")
            return False
    return True
if b8 = = "__main__":
    b9 = class1()
    b2 = [
        (0, 1, -1),
        (0, 2, 4),
        (1, 2, 3),
        (1, 3, 2),
        (1, 4, 2),
        (3, 2, 5),
        (3, 1, 1),
        (4, 3, -3)
    ]
    for u, v, w in b2:
        b9.fonk3(u, v, w)
    b10 = b9.b1[0]
    b11 = fonk15(b9, b10)
    print("No negative b7 cycle detected" if b11 else "class1 contains a negative b7 cycle")