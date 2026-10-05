class class1:
    def fonk1(self):
        self.b1 = {}
    def fonk2(self, vertice):
        self.b1[vertice] = vertice
    def fonk3(self, vertice):
        if self.b1[vertice] != vertice:
            self.b1[vertice] = self.fonk3(self.b1[vertice])
        return self.b1[vertice]
    def fonk4(self, u, b7):
        b2 = self.fonk3(u)
        b3 = self.fonk3(b7)
        if b2 != b3:
            self.b1[b2] = b3
def fonk5(b8):
    b4 = set()
    b5 = class1()
    for vertice in b8['V']:
        b5.fonk2(vertice)
    b6 = sorted(b8['E'])
    for edge in b6:
        weight, u, b7 = edge
        if b5.fonk3(u) != b5.fonk3(b7):
            b4.add(edge)
            b5.fonk4(u, b7)
    return b4
b8 = {
    'V': ['A', 'B', 'C', 'D', 'E'],
    'E': [(1, 'A', 'B'), (3, 'A', 'C'), (2, 'B', 'C'), (5, 'B', 'D'), (4, 'C', 'D'), (6, 'C', 'E'), (7, 'D', 'E')]
}
b9 = fonk5(b8)
print("Minimum Spanning Tree:", b9)