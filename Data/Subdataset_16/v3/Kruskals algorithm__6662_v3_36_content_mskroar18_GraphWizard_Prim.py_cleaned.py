class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
    def fonk2(self):
        return f"class1({self.b1}, {self.b2}, {self.b3})"
def fonk3(b8, a1):
    b8.sort(b4 = lambda edge: edge.b3)
    b5 = []
    b6 = set()
    b7 = b8[0]
    b5.append(b7)
    b6.update([b7.b1, b7.b2])
    while len(b5) < a1 - 1:
        for edge in b8:
            if (edge.b1 in b6) ^ (edge.b2 in b6):
                b5.append(edge)
                b6.update([edge.b1, edge.b2])
                break
    return b5
b8 = [
    class1('A', 'B', 1),
    class1('A', 'C', 2),
    class1('B', 'C', 3),
    class1('B', 'D', 4),
    class1('C', 'D', 5)
]
a1 = 4
b5 = fonk3(b8, a1)
for edge in b5:
    print(f"class1: {edge.b1} - {edge.b2}, Weight: {edge.b3}")