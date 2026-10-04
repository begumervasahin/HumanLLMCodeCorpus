class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = False
        self.a1 = 1
def fonk2(edgelist, a3):
    edgelist.sort(b5 = lambda edge: edge.b3)
    b6 = set()
    edgelist[0].b4 = True
    b6.add(edgelist[0])
    edgelist[0].a1 = 0
    a2 = 1
    while a2 < a3 - 1:
        for edge in edgelist:
            if edge.a1 = = 1:
                b8, b7 = False, False
                for selected_edge in b6:
                    if edge.b1 in (selected_edge.b1, selected_edge.b2):
                        b8 = True
                    if edge.b2 in (selected_edge.b1, selected_edge.b2):
                        b7 = True
                if b8 and b7:
                    edge.a1 = 0
                elif b8 or b7:
                    b6.add(edge)
                    edge.b4 = True
                    edge.a1 = 0
                    a2 += 1
                    break
    return b6
b9 = [
    class1('A', 'B', 1),
    class1('A', 'C', 2),
    class1('B', 'C', 3),
    class1('B', 'D', 4),
    class1('C', 'D', 5)
]
a3 = 4
b10 = fonk2(b9, a3)
for edge in b10:
    print(f"class1: {edge.b1} - {edge.b2}, Weight: {edge.b3}")