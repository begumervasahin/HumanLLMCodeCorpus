class class1:
    def fonk1(self, vertices):
        self.b1 = vertices
        self.b2 = []
        self.b3 = []
        self.b4 = []
    def fonk2(self):
        self.b3 = list(range(self.b1))
        self.b4 = [0] * self.b1
    def fonk3(self, u, v, weight):
        self.b2.append((u, v, weight))
    def fonk4(self, vertex):
        if self.b3[vertex] != vertex:
            self.b3[vertex] = self.fonk4(self.b3[vertex])
        return self.b3[vertex]
    def fonk5(self, set1, set2):
        b5 = self.fonk4(set1)
        b6 = self.fonk4(set2)
        if b5 != b6:
            if self.b4[b5] > self.b4[b6]:
                self.b3[b6] = b5
            elif self.b4[b5] < self.b4[b6]:
                self.b3[b5] = b6
            else:
                self.b3[b6] = b5
                self.b4[b5] += 1
def fonk6(graph):
    graph.fonk2()
    b7 = []
    b8 = sorted(graph.b2, key=lambda edge: edge[2])
    for u, v, weight in b8:
        b9 = graph.fonk4(u)
        b10 = graph.fonk4(v)
        if b9 != b10:
            b7.append((u, v, weight))
            graph.fonk5(b9, b10)
        if len(b7) == graph.b1 - 1:
            break
    fonk7(b7)
    return b7
def fonk7(b7):
    print("Resulting Minimum Spanning Tree (MST):")
    b11 = sum(weight for _, _, weight in b7)
    for u, v, weight in b7:
        print(f"{u} -- {v} == Weight: {weight}")
    print(f"The total weight of the MST is {b11}")
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