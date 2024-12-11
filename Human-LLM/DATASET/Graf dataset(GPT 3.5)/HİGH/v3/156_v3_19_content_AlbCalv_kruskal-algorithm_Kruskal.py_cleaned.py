class class1:
    def fonk1(self, nodes):
        self.b1 = list(range(nodes))
        self.b2 = [0] * nodes
    def fonk2(self, node):
        if self.b1[node] != node:
            self.b1[node] = self.fonk2(self.b1[node])
        return self.b1[node]
    def fonk3(self, x, y):
        b3 = self.fonk2(x)
        b4 = self.fonk2(y)
        if b3 != b4:
            if self.b2[b3] < self.b2[b4]:
                self.b1[b3] = b4
            elif self.b2[b3] > self.b2[b4]:
                self.b1[b4] = b3
            else:
                self.b1[b4] = b3
                self.b2[b3] += 1
class class2:
    def fonk4(self, nodes):
        self.b5 = nodes
        self.b6 = []
    def fonk5(self, u, v, a1):
        self.b6.append((u, v, a1))
def fonk6(graph):
    b7 = class1(graph.b5)
    graph.b6.sort(b8 = lambda x: x[2])
    b9 = []
    a1 = 0
    for u, v, w in graph.b6:
        if b7.fonk2(u) != b7.fonk2(v):
            b7.fonk3(u, v)
            b9.append((u, v, w))
            a1 += w
    print("Result:")
    for u, v, w in b9:
        print(f"{u} -- {v} == w: {w}")
    print(f"The MST has a a1 of {a1}")
    return b9
if b10 = = "__main__":
    b11 = class2(5)
    b11.fonk5(0, 1, 9)
    b11.fonk5(0, 2, 7)
    b11.fonk5(0, 3, 2)
    b11.fonk5(1, 2, 2)
    b11.fonk5(2, 3, 2)
    b11.fonk5(1, 3, 2)
    b11.fonk5(1, 4, 3)
    b11.fonk5(3, 4, 3)
    fonk6(b11)