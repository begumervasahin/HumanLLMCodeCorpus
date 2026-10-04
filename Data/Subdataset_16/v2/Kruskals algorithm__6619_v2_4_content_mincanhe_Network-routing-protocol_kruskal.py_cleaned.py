class class1:
    def fonk1(self):
        self.b1 = {}
        self.b2 = {}
    def fonk2(self, vertice):
        self.b1[vertice] = vertice
        self.b2[vertice] = 0
    def fonk3(self, vertice):
        if self.b1[vertice] != vertice:
            self.b1[vertice] = self.fonk3(self.b1[vertice])
        return self.b1[vertice]
    def fonk4(self, vertice1, b8):
        b3 = self.fonk3(vertice1)
        b4 = self.fonk3(b8)
        if b3 != b4:
            if self.b2[b3] < self.b2[b4]:
                self.b1[b3] = b4
            else:
                self.b1[b4] = b3
                if self.b2[b3] == self.b2[b4]:
                    self.b2[b3] += 1
def fonk5(b10):
    b5 = class1()
    for vertice in b10['vertices']:
        b5.fonk2(vertice)
    b6 = set()
    b7 = sorted(b10['b7'], reverse=True)
    for edge in b7:
        weight, vertice1, b8 = edge
        if b5.fonk3(vertice1) != b5.fonk3(b8):
            b5.fonk4(vertice1, b8)
            b6.add(edge)
    return b6
if b9 = = "__main__":
    b10 = {
        'vertices': ['A', 'B', 'C', 'D', 'E'],
        'b7': [
            (5, 'A', 'B'),
            (10, 'A', 'C'),
            (7, 'B', 'D'),
            (8, 'C', 'D'),
            (6, 'C', 'E'),
            (4, 'D', 'E')
        ]
    }
    b6 = fonk5(b10)
    print("Edges in the Maximum Bandwidth Path (or Maximum Spanning Tree):")
    for edge in b6:
        print(edge)