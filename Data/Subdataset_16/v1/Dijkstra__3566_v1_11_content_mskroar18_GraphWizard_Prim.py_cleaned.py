class class1:
    def fonk1(self, vertex1, vertex2, b3):
        self.b1 = vertex1
        self.b2 = vertex2
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
        self.b5.sort(b7 = returnweight)
        b8 = set()
        self.b5[0].b4 = True
        b8.add(self.b5[0])
        a2 = 0
        self.b5[0].a1 = 0
        while a2 < self.b6 - 1:
            a3 = 1
            b9 = False
            while a3 < len(self.b5) and b9 is False:
                b10 = False
                b11 = False
                b12 = False
                if self.b5[a3].a1 = = 1:
                    for k in b8:
                        if self.b5[a3].b2 = = k.b1 or self.b5[a3].b2 == k.b2:
                            b11 = True
                        if self.b5[a3].b1 = = k.b1 or self.b5[a3].b1 == k.b2:
                            b10 = True
                    if b10 and b11:
                        b12 = True
                        self.b5[a3].a1 = 0
                    elif (b11 or b10) and not b12:
                        b8.add(self.b5[a3])
                        self.b5[a3].b4 = True
                        self.b5[a3].a1 = 0
                        b9 = True
                a3 += 1
            a2 += 1
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