class class1:
    def fonk1(self, vertices):
        self.b1 = vertices
        self.b2 = []
        self.b3 = []
        self.b4 = []
    def fonk2(self):
        for vertex in range(self.b1):
            self.b3.append(vertex)
            self.b4.append(0)
    def fonk3(self, u, v, b11):
        self.b2.append([u, v, b11])
    def fonk4(self, i):
        if self.b3[i] == i:
            return i
        self.b3[i] = self.fonk4(self.b3[i])
        return self.b3[i]
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
    graph.b2 = sorted(graph.b2, key=lambda b9: b9[2])
    a1 = 0
    for edge in graph.b2:
        u, v, b8 = edge
        b9 = graph.fonk4(u)
        b10 = graph.fonk4(v)
        if b9 != b10:
            a1 += 1
            b7.append([u, v, b8])
            graph.fonk5(b9, b10)
            if a1 = = graph.b1 - 1:
                break
    print("Result")
    b11 = sum(b8 for _, _, b8 in b7)
    for u, v, b8 in b7:
        print("%b12 -- %b12 = = b8: %b12" % (u, v, b8))
    print("The MST has a b11 of %b12" % b11)
    return b7
b13 = class1(5)
b13.fonk3(0, 1, 9)
b13.fonk3(0, 2, 7)
b13.fonk3(0, 3, 2)
b13.fonk3(1, 2, 2)
b13.fonk3(2, 3, 2)
b13.fonk3(1, 3, 2)
b13.fonk3(1, 4, 3)
b13.fonk3(3, 4, 3)
fonk6(b13)