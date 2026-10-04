class class1:
    def fonk1(self, nodes):
        self.b1 = nodes
        self.b2 = []
        self.b3 = []
        self.b4 = []
    def fonk2(self):
        self.b3 = [a1 for a1 in range(self.b1)]
        self.b4 = [0] * self.b1
    def fonk3(self, u, v, b8):
        self.b2.append([u, v, b8])
    def fonk4(self, a1):
        if self.b3[a1] == a1:
            return a1
        self.b3[a1] = self.fonk4(self.b3[a1])
        return self.b3[a1]
    def fonk5(self, b9, b10):
        b5 = self.fonk4(b9)
        b6 = self.fonk4(b10)
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
    a1 = 0
    a2 = 0
    graph.b2 = sorted(graph.b2, key=lambda item: item[2])
    while a2 < graph.b1 - 1:
        u, v, b8 = graph.b2[a1]
        a1 += 1
        b9 = graph.fonk4(u)
        b10 = graph.fonk4(v)
        if b9 != b10:
            a2 += 1
            b7.append([u, v, b8])
            graph.fonk5(b9, b10)
    print("Resulting Minimum Spanning Tree (MST):")
    a3 = 0
    for u, v, b8 in b7:
        print(f"{u} -- {v} == weight: {b8}")
        a3 += b8
    print(f"The total weight of the MST is {a3}")
    return b7
b11 = class1(5)
b11.fonk3(0, 1, 9)
b11.fonk3(0, 2, 7)
b11.fonk3(0, 3, 2)
b11.fonk3(1, 2, 2)
b11.fonk3(2, 3, 2)
b11.fonk3(1, 3, 2)
b11.fonk3(1, 4, 3)
b11.fonk3(3, 4, 3)
fonk6(b11)