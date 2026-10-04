class class1:
    def fonk1(self):
        self.b1 = {}
        self.b2 = {}
    def fonk2(self, vertex):
        self.b1[vertex] = vertex
        self.b2[vertex] = 0
    def fonk3(self, vertex):
        if self.b1[vertex] != vertex:
            self.b1[vertex] = self.fonk3(self.b1[vertex])
        return self.b1[vertex]
    def fonk4(self, vertex1, vertex2):
        b3 = self.fonk3(vertex1)
        b4 = self.fonk3(vertex2)
        if b3 != b4:
            if self.b2[b3] < self.b2[b4]:
                self.b1[b3] = b4
            else:
                self.b1[b4] = b3
                if self.b2[b3] == self.b2[b4]:
                    self.b2[b3] += 1
def fonk5(b9):
    b5 = class1()
    for vertex in b9['vertices']:
        b5.fonk2(vertex)
    b6 = set()
    b7 = sorted(b9['edges'], reverse=True)
    for weight, vertex1, vertex2 in b7:
        if b5.fonk3(vertex1) != b5.fonk3(vertex2):
            b5.fonk4(vertex1, vertex2)
            b6.add((weight, vertex1, vertex2))
    return b6
if b8 = = "__main__":
    b9 = {
        'vertices': ['A', 'B', 'C', 'D', 'E'],
        'edges': [
            (10, 'A', 'C'),
            (8, 'C', 'D'),
            (7, 'B', 'D'),
            (6, 'C', 'E'),
            (5, 'A', 'B'),
            (4, 'D', 'E')
        ]
    }
    b6 = fonk5(b9)
    print("Edges in the Maximum Bandwidth Path (Maximum Spanning Tree):")
    for edge in b6:
        print(edge)