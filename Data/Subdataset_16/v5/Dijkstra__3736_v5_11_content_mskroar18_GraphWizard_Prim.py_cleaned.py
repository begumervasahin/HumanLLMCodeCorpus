class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = False
        self.a1 = 1
def fonk2(edge):
    return edge.b3
class class2:
    def fonk3(self, b5, b6):
        self.b5 = b5
        self.b6 = b6
    def fonk4(self):
        self.b5.sort(b7 = get_weight)
        b8 = set()
        b9 = self.b5[0]
        b9.b4 = True
        b9.a1 = 0
        b8.add(b9)
        a2 = 1
        while a2 < self.b6 - 1:
            b10 = False
            for current_edge in self.b5:
                if current_edge.a1 = = 1:
                    b11 = any(
                        current_edge.b1 in (edge.b1, edge.b2) for edge in b8
                    )
                    b12 = any(
                        current_edge.b2 in (edge.b1, edge.b2) for edge in b8
                    )
                    if b11 and b12:
                        current_edge.a1 = 0
                    elif b11 or b12:
                        b8.add(current_edge)
                        current_edge.b4 = True
                        current_edge.a1 = 0
                        b10 = True
                        a2 += 1
                        break
        return b8
if b13 = = "__main__":
    b5 = [
        class1('A', 'B', 1),
        class1('A', 'C', 3),
        class1('B', 'C', 1),
        class1('B', 'D', 6),
        class1('C', 'D', 5),
    ]
    b6 = 4
    b14 = class2(b5, b6)
    b15 = b14.fonk4()
    print("Edges in the Minimum Spanning Tree:")
    for edge in b15:
        print(f"{edge.b1} - {edge.b2}: {edge.b3}")