class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = False
    def fonk2(self):
        return f"class1({self.b1}, {self.b2}, {self.b3})"
def fonk3(edgelist, a1):
    edgelist.sort(b5 = lambda edge: edge.b3)
    b6 = set()
    b7 = set()
    b8 = edgelist[0]
    b8.b4 = True
    b6.add(b8)
    b7.update([b8.b1, b8.b2])
    while len(b6) < a1 - 1:
        for edge in edgelist:
            if (edge.b1 in b7) ^ (edge.b2 in b7):
                edge.b4 = True
                b6.add(edge)
                b7.update([edge.b1, edge.b2])
                break
    return b6
b9 = [
    class1('A', 'B', 1),
    class1('A', 'C', 2),
    class1('B', 'C', 3),
    class1('B', 'D', 4),
    class1('C', 'D', 5)
]
a1 = 4
b10 = fonk3(b9, a1)
for edge in b10:
    print(f"class1: {edge.b1} - {edge.b2}, Weight: {edge.b3}")