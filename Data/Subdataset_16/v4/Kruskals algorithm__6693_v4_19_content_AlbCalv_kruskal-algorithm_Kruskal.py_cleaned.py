class class1:
    def fonk1(self, vertices):
        self.b1 = vertices
        self.b2 = []
        self.b3 = []
        self.b4 = []
    def fonk2(self):
        self.b3 = list(range(self.b1))
        self.b4 = [0] * self.b1
    def fonk3(self, u, v, b9):
        self.b2.append([u, v, b9])
    def fonk4(self, i):
        if self.b3[i] == i:
            return i
        self.b3[i] = self.fonk4(self.b3[i])
        return self.b3[i]
    def fonk5(self, b10, b11):
        b5 = self.fonk4(b10)
        b6 = self.fonk4(b11)
        if self.b4[b5] < self.b4[b6]:
            self.b3[b5] = b6
        elif self.b4[b5] > self.b4[b6]:
            self.b3[b6] = b5
        else:
            self.b3[b6] = b5
            self.b4[b5] += 1
def fonk6(graph):
    graph.fonk2()
    b7 = []
    i, b8 = 0, 0
    graph.b2 = sorted(graph.b2, key=lambda item: item[2])
    while b8 < graph.b1 - 1:
        u, v, b9 = graph.b2[i]
        i += 1
        b10 = graph.fonk4(u)
        b11 = graph.fonk4(v)
        if b10 != b11:
            b8 += 1
            b7.append([u, v, b9])
            graph.fonk5(b10, b11)
    print("Resulting Minimum Spanning Tree (MST):")
    a1 = 0
    for u, v, b9 in b7:
        print(f"{u} -- {v} == Weight: {b9}")
        a1 += b9
    print(f"The total weight of the MST is {a1}")
    return b7
b12 = class1(5)
b12.fonk3(0, 1, 9)
b12.fonk3(0, 2, 7)
b12.fonk3(0, 3, 2)
b12.fonk3(1, 2, 2)
b12.fonk3(2, 3, 2)
b12.fonk3(1, 3, 2)
b12.fonk3(1, 4, 3)
b12.fonk3(3, 4, 3)
fonk6(b12)