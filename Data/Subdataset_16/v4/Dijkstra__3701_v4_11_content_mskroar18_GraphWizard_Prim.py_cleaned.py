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
        self.b5[0].b4 = True
        b8.add(self.b5[0])
        self.b5[0].a1 = 0
        a2 = 1
        while a2 < self.b6 - 1:
            b9 = False
            for current_edge in self.b5:
                if current_edge.a1 = = 1:
                    b10 = any(
                        current_edge.b1 = = edge.b1 or current_edge.b1 == edge.b2
                        for edge in b8
                    )
                    b11 = any(
                        current_edge.b2 = = edge.b1 or current_edge.b2 == edge.b2
                        for edge in b8
                    )
                    if b10 and b11:
                        current_edge.a1 = 0
                    elif b10 or b11:
                        b8.add(current_edge)
                        current_edge.b4 = True
                        current_edge.a1 = 0
                        b9 = True
                        a2 += 1
                        break
        return b8
if b12 = = "__main__":
    b5 = [
        class1('A', 'B', 1),
        class1('A', 'C', 3),
        class1('B', 'C', 1),
        class1('B', 'D', 6),
        class1('C', 'D', 5),
    ]
    b6 = 4
    b13 = class2(b5, b6)
    b14 = b13.fonk4()
    print("Edges in the Minimum Spanning Tree:")
    for edge in b14:
        print(f"{edge.b1} - {edge.b2}: {edge.b3}")